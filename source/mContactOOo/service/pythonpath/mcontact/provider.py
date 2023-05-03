#!
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020 https://prrvchr.github.io                                     ║
║                                                                                    ║
║   Permission is hereby granted, free of charge, to any person obtaining            ║
║   a copy of this software and associated documentation files (the "Software"),     ║
║   to deal in the Software without restriction, including without limitation        ║
║   the rights to use, copy, modify, merge, publish, distribute, sublicense,         ║
║   and/or sell copies of the Software, and to permit persons to whom the Software   ║
║   is furnished to do so, subject to the following conditions:                      ║
║                                                                                    ║
║   The above copyright notice and this permission notice shall be included in       ║
║   all copies or substantial portions of the Software.                              ║
║                                                                                    ║
║   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                  ║
║   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES                  ║
║   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.        ║
║   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY             ║
║   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,             ║
║   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE       ║
║   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                    ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
"""

import uno

from .card import Provider as ProviderBase

from .dbtool import currentDateTimeInTZ
from .dbtool import currentUnoDateTime

from .configuration import g_host
from .configuration import g_url
from .configuration import g_page
from .configuration import g_member
from .configuration import g_chunk

from . import ijson
import traceback


class Provider(ProviderBase):
    def __init__(self, ctx, database):
        self._ctx = ctx

    def insertUser(self, database, request, scheme, server, name, pwd):
        userid = self._getNewUserId(request, scheme, server, name)
        # FIXME: The Microsoft API only offers one address book, we need to initialize it now...
        #return database.insertUser(scheme, server, userid, name, 'Tous mes contacts')
        return database.insertUser(userid, scheme, server, g_path, name)

    def _getNewUserId(self, request, scheme, server, name):
        url = scheme + server + g_path
        parameter = self._getRequestParameter('getUser', url)
        response =  request.executeRequest(parameter)
        if not response.Ok:
            #TODO: Raise SqlException with correct message!
            raise self.getSqlException(1004, 1108, '_getNewUserId', 'Cant retrieve User: %s' % name)
        userid = self._parseUserId(response)
        response.close()
        if userid is None:
            #TODO: Raise SqlException with correct message!
            raise self.getSqlException(1004, 1108, '_getNewUserId', 'Cant retrieve Id for User: %s' % name)
        print("Provider._getNewUserId() UserId: %s" % userid)
        return userid

    def _parseUserId(self, response):
        userid = None
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('id', 'string'):
                    userid = value
                    break
            del events[:]
        parser.close()
        return userid

    def initAddressbooks(self, database, user):
        print("Provider.initAddressbooks() 1 %s" % (user.Name, ))
        count, modified = self._updateAllAddressbook(database, user)
        if not count:
            #TODO: Raise SqlException with correct message!
            print("Provider.initAddressbooks() 2 %s" % (user.Name, ))
            raise self.getSqlException(1004, 1108, 'initAddressbooks', '%s has no support of CardDAV!' % user.Server)
        print("Provider.initAddressbooks() 3 %s" % (user.Name, ))
        if modified:
            print("Provider.initAddressbooks() 4 %s" % (user.Name, ))
            database.initAddressbooks(user)
        self._initAddressbookGroups(database, user)
        print("Provider.initAddressbooks() 5 %s" % (user.Name, ))

    def _updateAllAddressbook(self, database, user):
        try:
            parameter = self._getRequestParameter('getAddressbooks', user.BaseUrl)
            response = user.Request.executeRequest(parameter)
            if not response.Ok:
                response.close()
                #TODO: Raise SqlException with correct message!
                raise self.getSqlException(1006, 1107, 'getAllAddressbook()', user.Name)
            count, modified = user.Addressbooks.initAddressbooks(database, user.Id, self._parseAllAddressbook(response))
            response.close()
            return count, modified
        except Exception as e:
            msg = "Error: %s" % traceback.format_exc()
            print(msg)

    def _parseAllAddressbook(self, response):
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        url = name = tag = None
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('value.item.id', 'string'):
                    url = value
                elif (prefix, event) == ('value.item.displayName', 'string'):
                    name = value
                elif (prefix, event) == ('value.item.parentFolderId', 'string'):
                    tag = value
                if all((url, name, tag)):
                    yield  url, name, tag, ''
                    url = name = tag = None
            del events[:]
        parser.close()

    def _initAddressbookGroups(self, database, user):
        try:
            parameter = self._getRequestParameter('getAddressbookGroups', user.BaseUrl)
            response = user.Request.executeRequest(parameter)
            if not response.Ok:
                response.close()
                #TODO: Raise SqlException with correct message!
                raise self.getSqlException(1006, 1107, '_initAddressbookGroups()', user.Name)
            for group in database.insertGroups(user, self._parseGroups(response)):
                print("Provider._initAddressbookGroups() GID: %s - Name: %s" % group)
                #database.initUserGroupView(group)
            response.close()
        except Exception as e:
            msg = "Error: %s" % traceback.format_exc()
            print(msg)

    def firstPullCard(self, database, user, addressbook):
        parameter = self._getRequestParameter('getAddressbookCards', user.BaseUrl, addressbook.Uri)
        response = user.Request.executeRequest(parameter)
        if not response.Ok:
            response.close()
            #TODO: Raise SqlException with correct message!
            print("Provider.firstCardPull() Error: %s" % response.Reason)
            raise self.getSqlException(1006, 1107, 'getAddressbookCards()', user.Name)
        count = database.mergeCard(addressbook.Id, self._parseCards(response))
        response.close()
        return count

    def _parseCards(self, response):
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        url = tag = data = None
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            chunk = iterator.nextElement().value
            print("Provider._parseCards() Content:\n%s" % chunk)
            parser.send(chunk)
            for prefix, event, value in events:
                print("Provider._parseCards() Prefix: %s - Event: %s - Value: %s" % (prefix, event, value))
                if (prefix, event) == ('value.item', 'start_map'):
                    url = name = None
                    email = []
                elif (prefix, event) == ('value.item.id', 'string'):
                    url = value
                elif (prefix, event) == ('value.item.displayName', 'string'):
                    name = value
                elif (prefix, event) == ('value.item.emailAddresses.item.name', 'string'):
                    email.append(('Name', value))
                elif (prefix, event) == ('value.item.emailAddresses.item.type', 'string'):
                    email.append(('Type', value))
                elif (prefix, event) == ('value.item', 'end_map'):
                    yield  url, tag, email
            del events[:]
        parser.close()

    def _parseGroups(self, response):
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        url = tag = data = None
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            chunk = iterator.nextElement().value
            print("Provider._parseGroups() Content:\n%s" % chunk)
            parser.send(chunk)
            for prefix, event, value in events:
                print("Provider._parseGroups() Prefix: %s - Event: %s - Value: %s" % (prefix, event, value))
                if (prefix, event) == ('value', 'start_map'):
                    uri = name = None
                elif (prefix, event) == ('value.id', 'string'):
                    uri = value
                elif (prefix, event) == ('value.displayName', 'string'):
                    name = value
                elif (prefix, event) == ('value', 'end_map'):
                    yield  uri, name
            del events[:]
        parser.close()

    def pullCard(self, database, user, addressbook, dltd, mdfd):
        token, deleted, modified = self._getCardByToken(user, addressbook)
        if addressbook.Token != token:
            if deleted:
                dltd += database.deleteCard(addressbook.Id, deleted)
            if modified:
                mdfd += self._mergeCardByToken(database, user, addressbook)
            database.updateAddressbookToken(addressbook.Id, token)
        return dltd, mdfd

    def parseCard(self, connection):
        pass

    def _getRequestParameter(self, method, url, data=None):
        parameter = uno.createUnoStruct('com.sun.star.rest.RequestParameter')
        parameter.Name = method
        parameter.Url = url
        if method == 'getUser':
            parameter.Method = 'GET'
            parameter.Url += '/me'
            parameter.Query = '{"select": "%s"}' % g_userfields
        elif method == 'getAddressbooks':
            parameter.Method = 'GET'
            parameter.Url += '/me/contactFolders'
        elif method == 'getAddressbookCards':
            parameter.Method = 'GET'
            parameter.Url += '/me/contactfolders/%s/contacts' % data
            parameter.Query = '{"select": "%s"}' % g_cardfields
        elif method == 'getAddressbookGroups':
            parameter.Method = 'GET'
            parameter.Url += '/groups'
            parameter.Query = '{"select": "%s"}' % g_groupfields
        elif method == 'getModifiedCardByToken':
            parameter.Method = 'GET'
            parameter.Url += '/me/contactFolders/%s/contacts/delta' % data
            parameter.Query = '{"select": "%s"}' % g_cardfields
        return parameter

