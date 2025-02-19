<!--
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
-->
# [![mContactOOo logo][1]][2] Documentation

**Ce [document][3] en français.**

**The use of this software subjects you to our [Terms Of Use][4] and [Data Protection Policy][5].**

# version [1.2.1][6]

## Introduction:

**mContactOOo** is part of a [Suite][7] of [LibreOffice][8] ~~and/or [OpenOffice][9]~~ extensions allowing to offer you innovative services in these office suites.

This extension gives you access, in LibreOffice, to your Microsoft Outlook contacts.  
It uses [Microsoft Graph API][10] to synchronize your remote Microsoft Outlook contacts into a local HsqlDB 2.7.2 database.  
This extension is seen by LibreOffice as a [database driver][11] responding to the URL: `sdbc:address:microsoft:*`.

Being free software I encourage you:
- To duplicate its [source code][12].
- To make changes, corrections, improvements.
- To open [issue][13] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

The mContactOOo extension uses the OAuth2OOo extension to work.  
It must therefore meet the [requirement of the OAuth2OOo extension][14].

The mContactOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][15].

**On Linux and macOS the Python packages** used by the extension, if already installed, may come from the system and therefore **may not be up to date**.  
To ensure that your Python packages are up to date it is recommended to use the **System Info** option in the extension Options accessible by:  
**Tools -> Options -> Internet -> mContactOOo -> View log -> System Info**  
If outdated packages appear, you can update them with the command:  
`pip install --upgrade <package-name>`

For more information see: [What has been done for version 1.1.0][16].

___

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- [![OAuth2OOo logo][17]][18] Install **[OAuth2OOo.oxt][19]** extension [![Version][20]][19]

    You must install this extension, if it is not already installed.

- [![jdbcDriverOOo logo][21]][22] Install **[jdbcDriverOOo.oxt][23]** extension [![Version][24]][23]

    You must install this extension, if it is not already installed.

- ![mContactOOo logo][25] Install **[mContactOOo.oxt][26]** extension version [![Version][27]][26]

Restart LibreOffice after installation.  
**Be careful, restarting LibreOffice may not be enough.**
- **On Windows** to ensure that LibreOffice restarts correctly, use Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice shuts down (and kill it if so).
- **Under Linux or macOS** you can also ensure that LibreOffice restarts correctly, by launching it from a terminal with the command `soffice` and using the key combination `Ctrl + C` if after stopping LibreOffice, the terminal is not active (no command prompt).

___

## Use:

In LibreOffice / OpenOffice go to: **File -> Wizards -> Address Data Source...**

![mContactOOo screenshot 1][28]

The **Address Book Datasource Wizard** open.

In step: **1.Address Book Type**:
- Select: **Other external data source**.
- Click button: **Next**.

![mContactOOo screenshot 2][29]

In step: **2.Connection Settings**:
- Click button: **Settings**.

![mContactOOo screenshot 3][30]

A new wizard opens. **Data source properties**.

In step: **1.Advanced Properties**.  
In Database type list:
- Select: **Microsoft Contacts**.
- Click button: **Next**.

![mContactOOo screenshot 4][31]

In step: **2.Connection Settings**.  
In General: Enter the DBMS/driver-specific connection string here.
- Put your Microsoft account (ie: your_account@outlook.com)
- Click button: **Test connection**.

![mContactOOo screenshot 5][32]

After authorizing the [OAuth2OOo][18] application to access your Contacts, normally you should see: Connection Test: The connection was established successfully.

![mContactOOo screenshot 6][33]

If the connection has been established, you can complete this wizard with the **Finish** button.

![mContactOOo screenshot 7][34]

In step: **3.Table Selection**.  
If your data source has multiple tables, you will be asked to select the primary table.  
In this case select the table: **All my contacts**. If necessary and before any connection it is possible to rename the main table name in: **Tools -> Options -> Internet -> mContactOOo -> Main table name**.

In step: **4.Field Assignment**.  
If necessary it is possible to rename the names of the columns of the data source using the button: **Field Assignment**.  
Please continue this wizard with the button: **Next**.

![mContactOOo screenshot 8][35]

In step: **5.Data Source Title**.

You must create an odb file. To do this you must:
- **Uncheck the box**: Embed this address book definition in the current document.
- Named the odb file in the field: **Location**.

This odb file must also be made accessible. To do this you must:
- **Check the box**: Make this address book available to all modules in LibreOffice
- Named the address book in the field: **Address book name**.

![mContactOOo screenshot 9][36]

Have fun...

___

## Has been tested with:

* LibreOffice 7.3.7.2 - Lubuntu 22.04 - Python version 3.10.12 - OpenJDK-11-JRE (amd64)

* LibreOffice 7.5.4.2(x86) - Windows 10 - Python version 3.8.16 - Adoptium JDK Hotspot 11.0.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 7.4.3.2(x64) - Windows 10(x64) - Python version 3.8.15  - Adoptium JDK Hotspot 11.0.17 (x64) (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 24.8.0.3 (x86_64) - Windows 10(x64) - Python version 3.9.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* **Does not work with OpenOffice on Windows** see [bug 128569][37]. Having no solution, I encourage you to install **LibreOffice**.

I encourage you in case of problem :confused:  
to create an [issue][13]  
I will try to solve it :smile:

___

## Historical:

### Introduction:

This extension was written in order to make usable in free software (LibreOffice or OpenOffice) your personal data stored in your Microsoft Outlook address book.

With the [eMailerOOo][38] extension, it can be the data source for [mail merge][39] by email, to your correspondents contained in your Microsoft Outlook address book.

It will give you access to an information system that only larges companies are able, today, to implement.

### What has been done for version 1.0.1:

- The absence or obsolescence of the **OAuth2OOo** and/or **jdbcDriverOOo** extensions necessary for the proper functioning of **mContactOOo** now displays an error message.

- Many other things...

### What has been done for version 1.0.2:

- Support for version **1.2.0** of the **OAuth2OOo** extension. Previous versions will not work with **OAuth2OOo** extension 1.2.0 or higher.

### What has been done for version 1.0.3:

- Support for version **1.2.1** of the **OAuth2OOo** extension. Previous versions will not work with **OAuth2OOo** extension 1.2.1 or higher.

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][40] file following [PEP 508][41].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][42] section.

### What has been done for version 1.1.1:

- Using Python package `dateutil` to convert timestamp strings to UNO DateTime.
- Many other fixes...

### What has been done for version 1.1.2:

- Integration of a fix to workaround the [issue #159988][43].

### What has been done for version 1.1.3:

- The creation of the database, during the first connection, uses the UNO API offered by the jdbcDriverOOo extension since version 1.3.2. This makes it possible to record all the information necessary for creating the database in 9 text tables which are in fact [9 csv files][44].
- The extension will ask you to install the OAuth2OOo and jdbcDriverOOo extensions in versions 1.3.4 and 1.3.2 respectively minimum.
- Many fixes.

### What has been done for version 1.1.4:

- Updated the [Python python-dateutil][45] package to version 2.9.0.post0.
- Updated the [Python decorator][46] package to version 5.1.1.
- Updated the [Python ijson][47] package to version 3.3.0.
- Updated the [Python packaging][48] package to version 24.1.
- Updated the [Python setuptools][49] package to version 72.1.0 in order to respond to the [Dependabot security alert][50].
- Updated the [Python validators][51] package to version 0.33.0.
- The extension will ask you to install the OAuth2OOo and jdbcDriverOOo extensions in versions 1.3.6 and 1.4.2 respectively minimum.

### What has been done for version 1.1.5:

- Updated the [Python setuptools][49] package to version 73.0.1.
- The extension will ask you to install the OAuth2OOo and jdbcDriverOOo extensions in versions 1.3.7 and 1.4.5 respectively minimum.
- Changes to extension options that require a restart of LibreOffice will result in a message being displayed.
- Support for LibreOffice version 24.8.x.

### What has been done for version 1.1.6:

- The extension will ask you to install the OAuth2OOo and jdbcDriverOOo extensions in versions 1.3.8 and 1.4.6 respectively minimum.
- Modification of the extension options accessible via: **Tools -> Options... -> Internet -> mContactOOo** in order to comply with the new graphic charter.

### What has been done for version 1.2.0:

- The extension will ask you to install the OAuth2OOo and jdbcDriverOOo extensions in versions 1.4.0 and 1.4.6 respectively minimum.
- It is possible to build the extension archive (ie: the oxt file) with the [Apache Ant][52] utility and the [build.xml][53] script file.
- The extension will refuse to install under OpenOffice regardless of version or LibreOffice other than 7.x or higher.
- Added binaries needed for Python libraries to work on Linux and LibreOffice 24.8 (ie: Python 3.9).

### What has been done for version 1.2.1:

- Updated the [Python packaging][48] package to version 24.2.
- Updated the [Python setuptools][49] package to version 75.8.0.
- Updated the [Python six][54] package to version 1.17.0.
- Updated the [Python validators][51] package to version 0.34.0.
- Support for Python version 3.13.

### What remains to be done for version 1.2.1:

- Add new languages for internationalization...

- Anything welcome...

[1]: </img/contact.svg#collapse>
[2]: <https://prrvchr.github.io/mContactOOo/>
[3]: <https://prrvchr.github.io/mContactOOo/README_fr>
[4]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/PrivacyPolicy_en>
[6]: <https://prrvchr.github.io/mContactOOo#what-has-been-done-for-version-121>
[7]: <https://prrvchr.github.io/>
[8]: <https://www.libreoffice.org/download/download/>
[9]: <https://www.openoffice.org/download/index.html>
[10]: <https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview>
[11]: <https://wiki.openoffice.org/wiki/Documentation/DevGuide/Database/Driver_Service>
[12]: <https://github.com/prrvchr/mContactOOo>
[13]: <https://github.com/prrvchr/mContactOOo/issues/new>
[14]: <https://prrvchr.github.io/OAuth2OOo/#requirement>
[15]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[16]: <https://prrvchr.github.io/mContactOOo/#what-has-been-done-for-version-110>
[17]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.svg#middle>
[18]: <https://prrvchr.github.io/OAuth2OOo/>
[19]: <https://github.com/prrvchr/OAuth2OOo/releases/latest/download/OAuth2OOo.oxt>
[20]: <https://img.shields.io/github/v/tag/prrvchr/OAuth2OOo?label=latest#right>
[21]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[22]: <https://prrvchr.github.io/jdbcDriverOOo/>
[23]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[24]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[25]: <img/mContactOOo.svg#middle>
[26]: <https://github.com/prrvchr/mContactOOo/releases/latest/download/mContactOOo.oxt>
[27]: <https://img.shields.io/github/downloads/prrvchr/mContactOOo/latest/total?label=v1.2.1#right>
[28]: <img/mContactOOo-1.png>
[29]: <img/mContactOOo-2.png>
[30]: <img/mContactOOo-3.png>
[31]: <img/mContactOOo-4.png>
[32]: <img/mContactOOo-5.png>
[33]: <img/mContactOOo-6.png>
[34]: <img/mContactOOo-7.png>
[35]: <img/mContactOOo-8.png>
[36]: <img/mContactOOo-9.png>
[37]: <https://bz.apache.org/ooo/show_bug.cgi?id=128569>
[38]: <https://prrvchr.github.io/eMailerOOo>
[39]: <https://en.wikipedia.org/wiki/Mail_merge>
[40]: <https://github.com/prrvchr/mContactOOo/releases/latest/download/requirements.txt>
[41]: <https://peps.python.org/pep-0508/>
[42]: <https://prrvchr.github.io/mContactOOo/#requirement>
[43]: <https://bugs.documentfoundation.org/show_bug.cgi?id=159988>
[44]: <https://github.com/prrvchr/mContactOOo/tree/main/source/mContactOOo/hsqldb>
[45]: <https://pypi.org/project/python-dateutil/>
[46]: <https://pypi.org/project/decorator/>
[47]: <https://pypi.org/project/ijson/>
[48]: <https://pypi.org/project/packaging/>
[49]: <https://pypi.org/project/setuptools/>
[50]: <https://github.com/prrvchr/mContactOOo/security/dependabot/1>
[51]: <https://pypi.org/project/validators/>
[52]: <https://ant.apache.org/>
[53]: <https://github.com/prrvchr/mContactOOo/blob/master/source/mContactOOo/build.xml>
[54]: <https://pypi.org/project/six/>
