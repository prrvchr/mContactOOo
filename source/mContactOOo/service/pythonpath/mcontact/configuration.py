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

# General configuration
g_extension = 'mContactOOo'
g_identifier = 'io.github.prrvchr.%s' % g_extension
g_protocol = 'sdbc:address:microsoft'

# Resource strings files folder
g_resource = 'resource'
g_basename = 'Driver'

g_defaultlog = 'mContactLog'
g_synclog = 'mContactSync'
g_errorlog = 'mContactError'

g_scheme = 'https'
g_host = 'graph.microsoft.com'
g_version = 'beta'
g_url = '%s://%s/%s' % (g_scheme, g_host, g_version)
g_scope = '%s/People' % g_host

g_chunk = 320 * 1024
g_page = 100
g_member = 1000
g_admin = False

g_userfields = 'id,userPrincipalName,displayName'

g_cardfields = 'displayName,surname,givenName,middleName,title,CompanyName,emailAddresses,phones,postalAddresses'

g_groupfields = 'id,displayName'

