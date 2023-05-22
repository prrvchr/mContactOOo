# ![mContactOOo logo][1] mContactOOo

**Ce [document][2] en français.**

**The use of this software subjects you to our** [**Terms Of Use**][3] **and** [**Data Protection Policy**][4]

# version [0.0.1][5]

## Introduction:

**mContactOOo** is part of a [Suite][6] of [LibreOffice][7] and/or [OpenOffice][8] extensions allowing to offer you innovative services in these office suites.  
This extension gives you access to your Microsoft Outlook contacts in LibreOffice / OpenOffice.

Being free software I encourage you:
- To duplicate its [source code][9].
- To make changes, corrections, improvements.
- To open [issue][10] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

## Requirement:

mContactOOo uses a local [HsqlDB][11] database version 2.7.1.  
HsqlDB being a database written in Java, its use requires the [installation and configuration][12] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][13] as your Java installation source.

If you are using **LibreOffice on Linux**, you need to make sure of two things:
  - You are subject to [bug 139538][14]. To work around the problem, please **uninstall the packages** with commands:
    - `sudo apt remove libreoffice-sdbc-hsqldb`
    - `sudo apt remove libhsqldb1.8.0-java`

  If you still want to use the Embedded HsqlDB functionality provided by LibreOffice, then install the [HsqlDBembeddedOOo][15] extension.  

  - If the python3-cffi-backend package is installed then you need to **install the python3-cffi package** with the command:
    - `dpkg -s python3-cffi-backend` (to know if the package is installed)
    - `sudo apt install python3-cffi`

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![OAuth2OOo logo][16] **[OAuth2OOo.oxt][17]** extension version 0.0.6.

You must install this extension, if it is not already installed.

- Install ![jdbcDriverOOo logo][18] **[jdbcDriverOOo.oxt][19]** extension version 0.0.4.

You must install this extension, if it is not already installed.

- Install ![mContactOOo logo][1] **[mContactOOo.oxt][20]** extension version 0.0.1.

Restart LibreOffice / OpenOffice after installation.

## Use:

In LibreOffice / OpenOffice go to **File -> Wizards -> Address Data Source**:

![mContactOOo screenshot 1][21]

In step: 1. Address Book Type:
- select: Other external data source
- click on: Next(Button)

![mContactOOo screenshot 2][22]

In step: 2. Connection Settings:
- click on: Settings(Button)

![mContactOOo screenshot 3][23]

In Database type list:
- select: **Microsoft Contacts**
- click on: Next(Button)

![mContactOOo screenshot 4][24]

In General: Datasource Url:
- put: your Google account (ie: your_account@your_provider.com)

Then:
- click on: Test connection (button)

![mContactOOo screenshot 5][25]

After authorizing the [OAuth2OOo][26] application to access your Contacts, normally you should see: Connection Test: The connection was established successfully.

![mContactOOo screenshot 6][27]

Have fun...

![mContactOOo screenshot 7][28]

![mContactOOo screenshot 8][29]

![mContactOOo screenshot 9][30]

## Has been tested with:

* LibreOffice 6.4.4.2 - Ubuntu 20.04 -  LxQt 0.14.1

* LibreOffice 7.0.0.0.alpha1 - Ubuntu 20.04 -  LxQt 0.14.1

* OpenOffice 4.1.8 x86_64 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.2.0.Build:9820 x86_64 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.1.5.2 - Raspbian 10 buster - Raspberry Pi 4 Model B

* LibreOffice 6.4.4.2 (x64) - Windows 7 SP1

I encourage you in case of problem :-(  
to create an [issue][10]  
I will try to solve it ;-)

## Historical:

### Introduction:

This extension was written in order to make usable in free software (LibreOffice or OpenOffice) your personal data stored in your Microsoft Outlook address book.

With the [smtpMailerOOo][31] extension, it can be the data source for [mail merge][32] by email, to your correspondents contained in your Microsoft Outlook address book.

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
[11]: <http://hsqldb.org/>
[12]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[13]: <https://adoptium.net/releases.html?variant=openjdk11>
[14]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[15]: <https://prrvchr.github.io/HsqlDBembeddedOOo/>
[16]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.png>
[17]: <https://github.com/prrvchr/OAuth2OOo/raw/master/OAuth2OOo.oxt>
[18]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.png>
[19]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/source/jdbcDriverOOo/dist/jdbcDriverOOo.oxt>
[20]: <https://github.com/prrvchr/mContactOOo/raw/main/source/mContactOOo/dist/mContactOOo.oxt>
[21]: <img/mContactOOo-1.png>
[22]: <img/mContactOOo-2.png>
[23]: <img/mContactOOo-3.png>
[24]: <img/mContactOOo-4.png>
[25]: <img/mContactOOo-5.png>
[26]: <https://prrvchr.github.io/OAuth2OOo>
[27]: <img/mContactOOo-6.png>
[28]: <img/mContactOOo-7.png>
[29]: <img/mContactOOo-8.png>
[30]: <img/mContactOOo-9.png>
[31]: <https://github.com/prrvchr/smtpMailerOOo/blob/master/source/smtpMailerOOo/dist/smtpMailerOOo.oxt>
[32]: <https://en.wikipedia.org/wiki/Mail_merge>
