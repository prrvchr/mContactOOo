# Documentation

**This [document][2] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][3] et à notre [Politique de protection des données][4].**

# version [1.0.0][5]

## Introduction:

**mContactOOo** fait partie d'une [Suite][6] d'extensions [LibreOffice][7] ~~et/ou [OpenOffice][8]~~ permettant de vous offrir des services inovants dans ces suites bureautique.  
Cette extension vous donne l'accès, dans LibreOffice, à vos contacts Microsoft Outlook.

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][9].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][10] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___
## Prérequis:

Afin de profiter des dernières versions des bibliothèques Python utilisées dans mContactOOo, la version 2 de Python a été abandonnée au profit de **Python 3.8 minimum**.  
Cela signifie que **mContactOOo ne supporte plus OpenOffice et LibreOffice 6.x sous Windows depuis sa version 1.0.0**.
Je ne peux que vous conseiller **de migrer vers LibreOffice 7.x**.

mContactOOo utilise une base de données locale [HsqlDB][12] version 2.7.1.  
HsqlDB étant une base de données écrite en Java, son utilisation nécessite [l'installation et la configuration][13] dans LibreOffice / OpenOffice d'un **JRE version 11 ou ultérieure**.  
Je vous recommande [Adoptium][14] comme source d'installation de Java.

Si vous utilisez **LibreOffice sous Linux**, vous êtes sujet au [dysfonctionnement 139538][15]. Pour contourner le problème, veuillez **désinstaller les paquets** avec les commandes:
- `sudo apt remove libreoffice-sdbc-hsqldb` (pour désinstaller le paquet libreoffice-sdbc-hsqldb)
- `sudo apt remove libhsqldb1.8.0-java` (pour désinstaller le paquet libhsqldb1.8.0-java)

Si vous souhaitez quand même utiliser la fonctionnalité HsqlDB intégré fournie par LibreOffice, alors installez l'extension [HsqlDBembeddedOOo][16].  

___
## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- Installer l'extension ![OAuth2OOo logo][17] **[OAuth2OOo.oxt][18]** version 1.1.0.

Vous devez installer cette extension, si elle n'est pas déjà installée.

- Installer l'extension ![jdbcDriverOOo logo][19] **[jdbcDriverOOo.oxt][20]** version 0.0.4.

Vous devez installer cette extension, si elle n'est pas déjà installée.

- Installer l'extension ![mContactOOo logo][1] **[mContactOOo.oxt][21]** version 1.0.0.

Redémarrez LibreOffice / OpenOffice après l'installation.

___
## Utilisation:

Dans LibreOffice / OpenOffice aller à: **Fichier -> Assistants -> Source de données des adresses**:

![mContactOOo screenshot 1][22]

À l'étape: 1. Type de carnet d'adresses:
- sélectionner: Autre source de données externes
- cliquez sur: Suivant (bouton)

![mContactOOo screenshot 2][23]

À l'étape: 2. Paramètres de Connexion:
- cliquez sur: Paramètres (bouton)

![mContactOOo screenshot 3][24]

Dans Type de base de données:
- sélectionner: **Contacts Microsoft**
- cliquez sur: Suivant (bouton)

![mContactOOo screenshot 4][25]

Dans Général: URL de la source de données:
- mettre: votre compte Microsoft (c'est-à-dire: votre_compte@votre_adresse.com)

Puis:
- cliquez sur: Tester la connexion (bouton)

![mContactOOo screenshot 5][26]

Après avoir autorisé l'application [OAuth2OOo][27] à accéder à vos contacts, normalement vous devez voir s'afficher: Test de connexion: Connexion établie.

![mContactOOo screenshot 6][28]

Maintenant à vous d'en profiter...

![mContactOOo screenshot 7][29]

![mContactOOo screenshot 8][30]

![mContactOOo screenshot 9][31]

___
## A été testé avec:

* LibreOffice 7.3.7.2 - Lubuntu 22.04 - Python version 3.10.12 - OpenJDK-11-JRE (amd64)

* LibreOffice 7.5.4.2(x86) - Windows 10 - Python version 3.8.16 - Adoptium JDK Hotspot 11.0.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 7.4.3.2(x64) - Windows 10(x64) - Python version 3.8.15  - Adoptium JDK Hotspot 11.0.17 (x64) (under Lubuntu 22.04 / VirtualBox 6.1.38)

* **Ne fonctionne pas avec OpenOffice sous Windows** voir [dysfonctionnement 128569][11]. N'ayant aucune solution, je vous encourrage d'installer **LibreOffice**.

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][10]  
J'essaierai de le résoudre :smile:

___
## Historique:

### Introduction:

Cette extension a été écrite afin de rendre utilisables dans un logiciel libre (LibreOffice ou OpenOffice) vos données personnelles stockées dans votre carnet d'adresses Microsoft Outlook.

Avec l'extension [smtpMailerOOo][32], elle peut être la source de données pour des [publipostages][33] par courriel (email), à vos correspondants contenus dans votre carnet d'adresses Microsoft Outlook.

Elle vous donnera accès à un système d'information que seules les grandes entreprises sont capables, aujourd'hui, de mettre en œuvre.

[1]: <img/mContactOOo.png>
[2]: <https://prrvchr.github.io/mContactOOo>
[3]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/TermsOfUse_fr>
[4]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/PrivacyPolicy_fr>
[5]: <https://prrvchr.github.io/mContactOOo/README_fr#historique>
[6]: <https://prrvchr.github.io/README_fr>
[7]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[8]: <https://www.openoffice.org/fr/Telecharger/>
[9]: <https://github.com/prrvchr/mContactOOo>
[10]: <https://github.com/prrvchr/mContactOOo/issues/new>
[11]: <https://bz.apache.org/ooo/show_bug.cgi?id=128569>
[12]: <http://hsqldb.org/>
[13]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10/fr>
[14]: <https://adoptium.net/releases.html?variant=openjdk11>
[15]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[16]: <https://prrvchr.github.io/HsqlDBembeddedOOo/README_fr>
[17]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.png>
[18]: <https://github.com/prrvchr/OAuth2OOo/raw/master/OAuth2OOo.oxt>
[19]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.png>
[20]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/source/jdbcDriverOOo/dist/jdbcDriverOOo.oxt>
[21]: <https://github.com/prrvchr/mContactOOo/raw/main/source/mContactOOo/dist/mContactOOo.oxt>
[22]: <img/mContactOOo-1_fr.png>
[23]: <img/mContactOOo-2_fr.png>
[24]: <img/mContactOOo-3_fr.png>
[25]: <img/mContactOOo-4_fr.png>
[26]: <img/mContactOOo-5_fr.png>
[27]: <https://prrvchr.github.io/OAuth2OOo/README_fr>
[28]: <img/mContactOOo-6_fr.png>
[29]: <img/mContactOOo-7_fr.png>
[30]: <img/mContactOOo-8_fr.png>
[31]: <img/mContactOOo-9_fr.png>
[32]: <https://github.com/prrvchr/smtpMailerOOo/blob/master/source/smtpMailerOOo/dist/smtpMailerOOo.oxt>
[33]: <https://fr.wikipedia.org/wiki/Publipostage>
