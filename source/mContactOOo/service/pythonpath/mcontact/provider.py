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

from .jsonparser import JsonParser

from .unotool import getUrl

from .providerbase import ProviderBase

import traceback

from com.sun.star.auth.RestRequestTokenType import TOKEN_NONE
from com.sun.star.auth.RestRequestTokenType import TOKEN_URL
from com.sun.star.auth.RestRequestTokenType import TOKEN_REDIRECT
from com.sun.star.auth.RestRequestTokenType import TOKEN_QUERY
from com.sun.star.auth.RestRequestTokenType import TOKEN_JSON
from com.sun.star.auth.RestRequestTokenType import TOKEN_SYNC

from .configuration import g_page
from .configuration import g_member
from .configuration import g_userfields
from .configuration import g_errorlog
from .configuration import g_basename

from . import ijson

import traceback


class Provider(ProviderBase):
    def __init__(self, ctx, scheme, server):
        self._ctx = ctx
        self._scheme = scheme
        self._server = server
        self._chunk =  64 * 1024


    def insertUser(self, database, request, scheme, server, name, pwd):
        userid = self._getNewUserId(request, name)
        # FIXME: The Microsoft API only offers one address book, we need to initialize it now...
        #return database.insertUser(scheme, server, userid, name, 'Tous mes contacts')
        return database.insertUser(scheme, server, userid, name)

    def _getNewUserId(self, request, name):
        parameter = self._getRequestParameter('getUser')
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
        iterator = response.iterContent(self._chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('id', 'string'):
                    userid = value
                    break
            del events[:]
            # FIXME: We got what we wanted we can leave
            if userid is not None:
                break
        parser.close()
        return userid

    def initAddressbooks(self, database, user):
        if self.isOnLine():
            count, modified = self._updateAllAddressbook(database, user)
            if not count:
                #TODO: Raise SqlException with correct message!
                print("User.initAddressbooks() 1 %s" % (user.Name, ))
                raise self.getSqlException(1004, 1108, 'initAddressbooks', '%s has no support of CardDAV!' % user.Server)
            if modified:
                database.initAddressbooks(user)

    def _updateAllAddressbook(self, database, user):
        parameter = self._getRequestParameter('getAddressbooks')
        response = user.Request.executeRequest(parameter)
        if not response.Ok:
            response.close()
            #TODO: Raise SqlException with correct message!
            raise self.getSqlException(1006, 1107, 'getAllAddressbook()', user)
        count, modified = user.Addressbooks.initAddressbooks(database, user.Id, self._parseAllAddressbook(response))
        response.close()
        return count, modified

    def _parseAllAddressbook(self, response):
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        url = name = tag = token = None
        iterator = response.iterContent(self._chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('value.item.id', 'string'):
                    url = value
                elif (prefix, event) == ('value.item.displayName', 'string'):
                    name = value
                elif (prefix, event) == ('value.item.wellKnownName', 'string'):
                    tag = value
                elif (prefix, event) == ('value.item.parentFolderId', 'string'):
                    token = value
                if all((url, name, tag, token)):
                    yield  url, name, tag, token
                    url = name = tag = token = None
            del events[:]
        parser.close()

    def getAddressbookCards(self, request, user, password, url):
        parameter = self._getRequestParameter('getAddressbookCards')
        response = request.execute(parameter)
        if not response.IsPresent:
            #TODO: Raise SqlException with correct message!
            raise self.getSqlException(1006, 1107, 'getAddressbookCards()', user)
        print("Provider.getAddressbookCards() Response: %s" % response.Data)
        return ()

    def transcode(self, name, value):
        if name == 'People':
            value = self._getResource('people', value)
        elif name == 'Group':
            value = self._getResource('contactGroups', value)
        return value
    def transform(self, name, value):
        #if name == 'Resource' and value.startswith('people'):
        #    value = value.split('/').pop()
        return value

    def _getUser(self, request):
        parameter = self._getRequestParameter('getUser')
        return request.executeRequest(parameter)

    def getUser(self, request, fields):
        parameter = self._getRequestParameter('getUser')
        return request.executeRequest(parameter)
    def getUserId(self, user):
        return user.getValue('id')
    def getUserName(self, user):
        return user.getValue('userPrincipalName')
    def getUserDisplayName(self, user):
        return user.getValue('displayName')

    def getItemId(self, item):
        return item.getDefaultValue('resourceName', '').split('/').pop()

    def _getResource(self, resource, keys):
        groups = []
        for k in keys:
            groups.append('%s/%s' % (resource, k))
        return tuple(groups)

    def _getRequestParameter(self, method, data=None):
        parameter = uno.createUnoStruct('com.sun.star.rest.RequestParameter')
        parameter.Name = method
        parameter.Url = self.BaseUrl
        if method == 'getUser':
            parameter.Method = 'GET'
            parameter.Url += '/me'
            parameter.Query = '{"select": "%s"}' % g_userfields
        elif method == 'getAddressbooks':
            parameter.Method = 'GET'
            parameter.Url += '/me/contactFolders'
        elif method == 'getAddressbookCards':
            parameter.Method = 'GET'
            parameter.Url += '/me/contactFolders/%s/contacts/delta' % data
        elif method == 'Group':
            parameter.Method = 'GET'
            parameter.Url += '/contactGroups'
            page = '"pageSize": %s' % g_page
            query = [page]
            sync = data.GroupSync
            if sync:
                query.append('"syncToken": "%s"' % sync)
            parameter.Query = '{%s}' % ','.join(query)
            token = uno.createUnoStruct('com.sun.star.auth.RestRequestToken')
            token.Type = TOKEN_QUERY | TOKEN_SYNC
            token.Field = 'nextPageToken'
            token.Value = 'pageToken'
            token.SyncField = 'nextSyncToken'
            enumerator = uno.createUnoStruct('com.sun.star.auth.RestRequestEnumerator')
            enumerator.Field = 'contactGroups'
            enumerator.Token = token
            parameter.Enumerator = enumerator
        elif method == 'Connection':
            parameter.Method = 'GET'
            parameter.Url += '/contactGroups:batchGet'
            resources = '","'.join(data.getKeys())
            parameter.Query = '{"resourceNames": ["%s"], "maxMembers": %s}' % (resources, g_member)
        return parameter

