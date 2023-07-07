# Documentation

**Ce [document][2] en français.**

**The use of this software subjects you to our [Terms Of Use][3] and [Data Protection Policy][4].**

# version [1.0.0][5]

## Introduction:

**mContactOOo** is part of a [Suite][6] of [LibreOffice][7] ~~and/or [OpenOffice][8]~~ extensions allowing to offer you innovative services in these office suites.  
This extension gives you access, in LibreOffice, to your Microsoft Outlook contacts.

Being free software I encourage you:
- To duplicate its [source code][9].
- To make changes, corrections, improvements.
- To open [issue][10] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

## Requirement:

In order to take advantage of the latest versions of the Python libraries used in mContactOOo, version 2 of Python has been abandoned in favor of **Python 3.8 minimum**.  
This means that **mContactOOo no longer supports OpenOffice and LibreOffice 6.x on Windows since version 1.0.0**.
I can only advise you **to migrate to LibreOffice 7.x**.

mContactOOo uses a local [HsqlDB][12] database version 2.7.1.  
HsqlDB being a database written in Java, its use requires the [installation and configuration][13] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][14] as your Java installation source.

If you are using **LibreOffice on Linux**, you are subject to [bug 139538][15]. To work around the problem, please **uninstall the packages** with commands:
- `sudo apt remove libreoffice-sdbc-hsqldb` (to uninstall the libreoffice-sdbc-hsqldb package)
- `sudo apt remove libhsqldb1.8.0-java` (to uninstall the libhsqldb1.8.0-java package)

If you still want to use the Embedded HsqlDB functionality provided by LibreOffice, then install the [HsqlDBembeddedOOo][16] extension.  

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![OAuth2OOo logo][17] **[OAuth2OOo.oxt][18]** extension version 1.1.0.

You must install this extension, if it is not already installed.

- Install ![jdbcDriverOOo logo][19] **[jdbcDriverOOo.oxt][20]** extension version 0.0.4.

You must install this extension, if it is not already installed.

- Install ![mContactOOo logo][1] **[mContactOOo.oxt][21]** extension version 1.0.0.

Restart LibreOffice / OpenOffice after installation.

## Use:

In LibreOffice / OpenOffice go to **File -> Wizards -> Address Data Source**:

![mContactOOo screenshot 1][22]

In step: 1. Address Book Type:
- select: Other external data source
- click on: Next(Button)

![mContactOOo screenshot 2][23]

In step: 2. Connection Settings:
- click on: Settings(Button)

![mContactOOo screenshot 3][24]

In Database type list:
- select: **Microsoft Contacts**
- click on: Next(Button)

![mContactOOo screenshot 4][25]

In General: Datasource Url:
- put: your Google account (ie: your_account@your_provider.com)

Then:
- click on: Test connection (button)

![mContactOOo screenshot 5][26]

After authorizing the [OAuth2OOo][27] application to access your Contacts, normally you should see: Connection Test: The connection was established successfully.

![mContactOOo screenshot 6][28]

Have fun...

![mContactOOo screenshot 7][29]

![mContactOOo screenshot 8][30]

![mContactOOo screenshot 9][31]

## Has been tested with:

* LibreOffice 7.3.7.2 - Lubuntu 22.04 - Python version 3.10.12 - OpenJDK-11-JRE (amd64)

* LibreOffice 7.5.4.2(x86) - Windows 10 - Python version 3.8.16 - Adoptium JDK Hotspot 11.0.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 7.4.3.2(x64) - Windows 10(x64) - Python version 3.8.15  - Adoptium JDK Hotspot 11.0.17 (x64) (under Lubuntu 22.04 / VirtualBox 6.1.38)

* **Does not work with OpenOffice on Windows** see [bug 128569][11]. Having no solution, I encourage you to install **LibreOffice**.

I encourage you in case of problem :-(  
to create an [issue][10]  
I will try to solve it ;-)

## Historical:

### Introduction:

This extension was written in order to make usable in free software (LibreOffice or OpenOffice) your personal data stored in your Microsoft Outlook address book.

With the [smtpMailerOOo][32] extension, it can be the data source for [mail merge][33] by email, to your correspondents contained in your Microsoft Outlook address book.

It will give you access to an information system that only larges companies are able, today, to implement.

[1]: <img/mContactOOo.png>
[2]: <https://prrvchr.github.io/mContactOOo/README_fr>
[3]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/TermsOfUse_en>
[4]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/PrivacyPolicy_en>
[5]: <https://prrvchr.github.io/mContactOOo#historical>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://github.com/prrvchr/mContactOOo>
[10]: <https://github.com/prrvchr/mContactOOo/issues/new>
[11]: <https://bz.apache.org/ooo/show_bug.cgi?id=128569>
[12]: <http://hsqldb.org/>
[13]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[14]: <https://adoptium.net/releases.html?variant=openjdk11>
[15]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[16]: <https://prrvchr.github.io/HsqlDBembeddedOOo/>
[17]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.png>
[18]: <https://github.com/prrvchr/OAuth2OOo/raw/master/OAuth2OOo.oxt>
[19]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.png>
[20]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/source/jdbcDriverOOo/dist/jdbcDriverOOo.oxt>
[21]: <https://github.com/prrvchr/mContactOOo/raw/main/source/mContactOOo/dist/mContactOOo.oxt>
[22]: <img/mContactOOo-1.png>
[23]: <img/mContactOOo-2.png>
[24]: <img/mContactOOo-3.png>
[25]: <img/mContactOOo-4.png>
[26]: <img/mContactOOo-5.png>
[27]: <https://prrvchr.github.io/OAuth2OOo>
[28]: <img/mContactOOo-6.png>
[29]: <img/mContactOOo-7.png>
[30]: <img/mContactOOo-8.png>
[31]: <img/mContactOOo-9.png>
[32]: <https://github.com/prrvchr/smtpMailerOOo/blob/master/source/smtpMailerOOo/dist/smtpMailerOOo.oxt>
[33]: <https://en.wikipedia.org/wiki/Mail_merge>
