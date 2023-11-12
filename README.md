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
# [![mContactOOo logo][0]][-1] Documentation

**Ce [document][1] en français.**

**The use of this software subjects you to our [Terms Of Use][2] and [Data Protection Policy][3].**

# version [1.0.3][4]

## Introduction:

**mContactOOo** is part of a [Suite][5] of [LibreOffice][6] ~~and/or [OpenOffice][7]~~ extensions allowing to offer you innovative services in these office suites.  
This extension gives you access, in LibreOffice, to your Microsoft Outlook contacts.

Being free software I encourage you:
- To duplicate its [source code][8].
- To make changes, corrections, improvements.
- To open [issue][9] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

In order to take advantage of the latest versions of the Python libraries used in mContactOOo, version 2 of Python has been abandoned in favor of **Python 3.8 minimum**.  
This means that **mContactOOo no longer supports OpenOffice and LibreOffice 6.x on Windows since version 1.0.0**.
I can only advise you **to migrate to LibreOffice 7.x**.

mContactOOo uses a local [HsqlDB][10] database version 2.7.2.  
HsqlDB being a database written in Java, its use requires the [installation and configuration][11] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][12] as your Java installation source.

If you are using **LibreOffice Community on Linux**, you are subject to [bug 139538][13]. To work around the problem, please **uninstall the packages** with commands:
- `sudo apt remove libreoffice-sdbc-hsqldb` (to uninstall the libreoffice-sdbc-hsqldb package)
- `sudo apt remove libhsqldb1.8.0-java` (to uninstall the libhsqldb1.8.0-java package)

If you still want to use the Embedded HsqlDB functionality provided by LibreOffice, then install the [HyperSQLOOo][14] extension.  

___

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- [![OAuth2OOo logo][15]][16] Install **[OAuth2OOo.oxt][17]** extension [![Version][18]][17]

    You must install this extension, if it is not already installed.

- [![jdbcDriverOOo logo][19]][20] Install **[jdbcDriverOOo.oxt][21]** extension [![Version][22]][21]

    You must install this extension, if it is not already installed.

- ![mContactOOo logo][23] Install **[mContactOOo.oxt][24]** extension version [![Version][25]][24]

Restart LibreOffice / OpenOffice after installation.

___

## Use:

In LibreOffice / OpenOffice go to **File -> Wizards -> Address Data Source**:

![mContactOOo screenshot 1][26]

In step: 1. Address Book Type:
- select: Other external data source
- click on: Next(Button)

![mContactOOo screenshot 2][27]

In step: 2. Connection Settings:
- click on: Settings(Button)

![mContactOOo screenshot 3][28]

In Database type list:
- select: **Microsoft Contacts**
- click on: Next(Button)

![mContactOOo screenshot 4][29]

In General: Datasource Url:
- put: your Google account (ie: your_account@your_provider.com)

Then:
- click on: Test connection (button)

![mContactOOo screenshot 5][30]

After authorizing the [OAuth2OOo][16] application to access your Contacts, normally you should see: Connection Test: The connection was established successfully.

![mContactOOo screenshot 6][31]

Have fun...

![mContactOOo screenshot 7][32]

![mContactOOo screenshot 8][33]

![mContactOOo screenshot 9][34]

___

## Has been tested with:

* LibreOffice 7.3.7.2 - Lubuntu 22.04 - Python version 3.10.12 - OpenJDK-11-JRE (amd64)

* LibreOffice 7.5.4.2(x86) - Windows 10 - Python version 3.8.16 - Adoptium JDK Hotspot 11.0.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 7.4.3.2(x64) - Windows 10(x64) - Python version 3.8.15  - Adoptium JDK Hotspot 11.0.17 (x64) (under Lubuntu 22.04 / VirtualBox 6.1.38)

* **Does not work with OpenOffice on Windows** see [bug 128569][35]. Having no solution, I encourage you to install **LibreOffice**.

I encourage you in case of problem :confused:  
to create an [issue][9]  
I will try to solve it :smile:

___

## Historical:

### Introduction:

This extension was written in order to make usable in free software (LibreOffice or OpenOffice) your personal data stored in your Microsoft Outlook address book.

With the [eMailerOOo][36] extension, it can be the data source for [mail merge][37] by email, to your correspondents contained in your Microsoft Outlook address book.

It will give you access to an information system that only larges companies are able, today, to implement.

### What has been done for version 1.0.1:

- The absence or obsolescence of the **OAuth2OOo** and/or **jdbcDriverOOo** extensions necessary for the proper functioning of **mContactOOo** now displays an error message.

- Many other things...

### What has been done for version 1.0.2:

- Support for version **1.2.0** of the **OAuth2OOo** extension. Previous versions will not work with **OAuth2OOo** extension 1.2.0 or higher.

### What has been done for version 1.0.3:

- Support for version **1.2.1** of the **OAuth2OOo** extension. Previous versions will not work with **OAuth2OOo** extension 1.2.1 or higher.

### What remains to be done for version 1.0.3:

- Add new languages for internationalization...

- Anything welcome...

[0]: </img/contact.svg#collapse>
[-1]: <https://prrvchr.github.io/mContactOOo/>
[1]: <https://prrvchr.github.io/mContactOOo/README_fr>
[2]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/TermsOfUse_en>
[3]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/PrivacyPolicy_en>
[4]: <https://prrvchr.github.io/mContactOOo#historical>
[5]: <https://prrvchr.github.io/>
[6]: <https://www.libreoffice.org/download/download/>
[7]: <https://www.openoffice.org/download/index.html>
[8]: <https://github.com/prrvchr/mContactOOo>
[9]: <https://github.com/prrvchr/mContactOOo/issues/new>
[10]: <http://hsqldb.org/>
[11]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[12]: <https://adoptium.net/releases.html?variant=openjdk11>
[13]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[14]: <https://prrvchr.github.io/HyperSQLOOo/>
[15]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.svg#middle>
[16]: <https://prrvchr.github.io/OAuth2OOo/>
[17]: <https://github.com/prrvchr/OAuth2OOo/releases/latest/download/OAuth2OOo.oxt>
[18]: <https://img.shields.io/github/v/tag/prrvchr/OAuth2OOo?label=latest#right>
[19]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[20]: <https://prrvchr.github.io/jdbcDriverOOo/>
[21]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[22]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[23]: <img/mContactOOo.svg#middle>
[24]: <https://github.com/prrvchr/mContactOOo/releases/latest/download/mContactOOo.oxt>
[25]: <https://img.shields.io/github/downloads/prrvchr/mContactOOo/latest/total?label=v1.0.3#right>
[26]: <img/mContactOOo-1.png>
[27]: <img/mContactOOo-2.png>
[28]: <img/mContactOOo-3.png>
[29]: <img/mContactOOo-4.png>
[30]: <img/mContactOOo-5.png>
[31]: <img/mContactOOo-6.png>
[32]: <img/mContactOOo-7.png>
[33]: <img/mContactOOo-8.png>
[34]: <img/mContactOOo-9.png>
[35]: <https://bz.apache.org/ooo/show_bug.cgi?id=128569>
[36]: <https://prrvchr.github.io/eMailerOOo>
[37]: <https://en.wikipedia.org/wiki/Mail_merge>
