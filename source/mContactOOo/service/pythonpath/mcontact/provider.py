#!
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020-25 https://prrvchr.github.io                                  ║
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

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from .card import Provider as ProviderMain

from .dbtool import currentDateTimeInTZ

from .configuration import g_host
from .configuration import g_url
from .configuration import g_chunk
from .configuration import g_userfields
from .configuration import g_groupfields

import json
import ijson
import traceback


class Provider(ProviderMain):
    def __init__(self, ctx, src, database):
        ProviderMain.__init__(self, ctx, src)
        paths, lists, maps, types, tmps, fields = database.getMetaData('item')
        self._paths = paths
        self._lists = lists
        self._maps = maps
        self._types = types
        self._tmps = tmps
        self._fields = fields

    @property
    def Host(self):
        return g_host
    @property
    def BaseUrl(self):
        return g_url

# Method called from Provider.insertUser()
    def getNewUserId(self, request, scheme, server, name, pwd):
        parameter = self._getRequestParameter(request, 'getUser')
        response = request.execute(parameter)
        if not response.Ok:
            self.raiseForStatus('getNewUserId', response, name)
        userid = self._parseUser(response)
        return userid

# Method called from DataSource.getConnection()
    def getUserUri(self, server, name):
        return name

# Method called from Provider.initAddressbooks()
    def getAddressbooks(self, database, user):
        parameter = self._getRequestParameter(user.Request, 'getBooks')
        response = user.Request.execute(parameter)
        if not response.Ok:
            self.raiseForStatus('initAddressbooks', response, user.Name)
        return self._parseAllBooks(response)

    def getUserGroups(self, database, user, book):
        parameter = self._getRequestParameter(user.Request, 'getGroups')
        response = user.Request.execute(parameter)
        if not response.Ok:
            self.raiseForStatus('initUserGroups', response, user.Name)
        print("Provider.initUserGroups() Response: %s" % response.Text)
        return self._parseGroups(response)

    # Private method
    def _parseUser(self, response):
        userid = None
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('id', 'string'):
                    userid = value
            del events[:]
        parser.close()
        response.close()
        return userid

    def _parseAllBooks(self, response):
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
        response.close()

# Method called from Replicator.run()
    def firstPullCard(self, database, user, book, page, count):
        return self._pullCard(database, 'firstPullCard()', user, book, page, count)

    def pullCard(self, database, user, book, page, count):
        return self._pullCard(database, 'pullCard()', user, book, page, count)

    def parseCard(self, database):
        start = database.getLastUserSync()
        stop = currentDateTimeInTZ()
        iterator = self._parseCardValue(database, start, stop)
        database.mergeCardValue(iterator)
        database.updateUserSync(stop)

    # Private method
    def _pullCard(self, database, mtd, user, book, page, count):
        args = []
        parameter = self._getRequestParameter(user.Request, 'getCards', book.Uri)
        iterator = self._parseCards(user, parameter, mtd, args)
        count += database.mergeCard(book.Id, iterator)
        page += parameter.PageCount
        if not args:
            if parameter.SyncToken:
                database.updateAddressbookToken(book.Id, parameter.SyncToken)
        self.initUserGroups(database, user, book)
        return page, count, args

    def _parseCards(self, user, parameter, mtd, args):
        key = tmp = False
        redirect = uno.getConstantByName('com.sun.star.rest.ParameterType.REDIRECT')
        while parameter.hasNextPage():
            response = user.Request.execute(parameter)
            if not response.Ok:
                args += self.getLoggerArgs(response, mtd, parameter, user.Name)
                break
            events = ijson.sendable_list()
            parser = ijson.parse_coro(events)
            iterator = response.iterContent(g_chunk, False)
            while iterator.hasMoreElements():
                parser.send(iterator.nextElement().value)
                for prefix, event, value in events:
                    if (prefix, event) == ('@odata.nextLink', 'string'):
                        parameter.setNextPage('', value, redirect)
                    elif (prefix, event) == ('@odata.deltaLink', 'string'):
                        parameter.SyncToken = value
                    elif (prefix, event) == ('value.item', 'start_map'):
                        cid = etag = tmp = None
                        data = {}
                        deleted = False
                    elif (prefix, event) == ('value.item.deleted', 'boolean'):
                        deleted = value
                    elif (prefix, event) == ('value.item.id', 'string'):
                        cid = value
                    elif (prefix, event) == ('value.item.@odata.etag', 'string'):
                        etag = value
                    # FIXME: All the data parsing is done based on the tables: Resources, Properties and Types 
                    # FIXME: Only properties listed in these tables will be parsed
                    # FIXME: This is the part for simple property import (use of tables: Resources and Properties)
                    elif event == 'string' and prefix in self._paths:
                        data[self._paths.get(prefix)] = value
                    # FIXME: This is the part for simple list property import (use of tables: Resources and Properties)
                    elif event == 'start_array' and value is None and prefix + '.item' in self._lists:
                        data[self._lists.get(prefix + '.item')] = []
                    elif event == 'string' and prefix in self._lists:
                        data[self._lists.get(prefix)].append(value)
                    # FIXME: This is the part for typed property import (use of tables: Resources, Properties and Types)
                    elif event == 'start_map' and prefix in self._maps:
                        key = tmp = None
                        suffix = ''
                    elif event == 'map_key' and prefix in self._maps and value in self._maps.get(prefix):
                        suffix = value
                    elif event == 'string' and key is None and prefix in self._types:
                        key = self._types.get(prefix).get(value + suffix)
                    elif event == 'string' and tmp is None and prefix in self._tmps:
                        tmp = value
                    elif event == 'end_map' and key and tmp and prefix in self._maps:
                        data[key] = tmp
                        key = tmp = False
                    elif (prefix, event) == ('value.item', 'end_map'):
                        yield cid, etag, deleted, json.dumps(data)
                del events[:]
            parser.close()
            response.close()

    def _pullGroup(self, database, mtd, user, book, page, count):
        parameter = self._getRequestParameter(user.Request, 'getGroups', book)
        response = user.Request.execute(parameter)
        if not response.Ok:
            args = self.getLoggerArgs(response, mtd, parameter, user.Name)
            return page, count, args
        iterator = self._parseGroups(response)
        count += database.mergeGroup(book.Id, iterator)
        page += parameter.PageCount
        return page, count, []

    def _parseGroups(self, response):
        events = ijson.sendable_list()
        parser = ijson.parse_coro(events)
        iterator = response.iterContent(g_chunk, False)
        while iterator.hasMoreElements():
            parser.send(iterator.nextElement().value)
            for prefix, event, value in events:
                if (prefix, event) == ('value.item', 'start_map'):
                    uri = name = None
                elif (prefix, event) == ('value.item.id', 'string'):
                    uri = value
                elif (prefix, event) == ('value.item.displayName', 'string'):
                    name = value
                elif (prefix, event) == ('value.item', 'end_map'):
                    if all((uri, name)):
                        yield  uri, name
            del events[:]
        parser.close()
        response.close()

    def _parseCardValue(self, database, start, stop):
        indexes = database.getColumnIndexes({'categories': -1})
        for book, card, query, data in database.getChangedCard(start, stop):
            if query == 'Deleted':
                continue
            else:
                for column, value in json.loads(data).items():
                    yield book, card, indexes.get(column), value

    def _getRequestParameter(self, request, method, data=None):
        parameter = request.getRequestParameter(method)
        parameter.Url = self.BaseUrl

        if method == 'getUser':
            parameter.Url += '/me'
            parameter.setQuery('select', g_userfields)

        elif method == 'getBooks':
            parameter.Url += '/me/contactFolders'

        elif method == 'getCards':
            parameter.Url += '/me/contactFolders/%s/contacts' % data
            parameter.setQuery('select', self._fields)

        elif method == 'getGroups':
            parameter.Url += '/me/outlook/masterCategories'
            parameter.setQuery('select', g_groupfields)

        elif method == 'getModifiedCardByToken':
            parameter.Url += '/me/contactFolders/%s/contacts/delta' % data
            parameter.setQuery('select', self._fields)

        return parameter

