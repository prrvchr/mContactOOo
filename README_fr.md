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
# Documentation

**This [document][3] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][4] et à notre [Politique de protection des données][5].**

# version [1.2.1][6]

## Introduction:

**mContactOOo** fait partie d'une [Suite][7] d'extensions [LibreOffice][8] ~~et/ou [OpenOffice][9]~~ permettant de vous offrir des services inovants dans ces suites bureautique.

Cette extension vous donne l'accès, dans LibreOffice, à vos contacts Microsoft Outlook.  
Elle utilise [l'API Microsoft Graph][10] pour synchroniser vos contacts Microsoft Outlook distant dans une base de données locale HsqlDB 2.7.2.  
Cette extension est vu par LibreOffice comme un [pilote de base de données][11] répondant à l'URL: `sdbc:address:microsoft:*`.

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][12].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][13] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

L'extension mContactOOo utilise l'extension OAuth2OOo pour fonctionner.  
Elle doit donc répondre aux [prérequis de l'extension OAuth2OOo][14].

L'extension mContactOOo utilise l'extension jdbcDriverOOo pour fonctionner.  
Elle doit donc répondre aux [prérequis de l'extension jdbcDriverOOo][15].

**Sous Linux et macOS les paquets Python** utilisés par l'extension, peuvent s'il sont déja installé provenir du système et donc, **peuvent ne pas être à jour**.  
Afin de s'assurer que vos paquets Python sont à jour il est recommandé d'utiliser l'option **Info système** dans les Options de l'extension accessible par:  
**Outils -> Options -> Internet -> mContactOOo -> Voir journal -> Info système**  
Si des paquets obsolètes apparaissent, vous pouvez les mettre à jour avec la commande:  
`pip install --upgrade <package-name>`

Pour plus d'information voir: [Ce qui a été fait pour la version 1.1.0][16].

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![OAuth2OOo logo][17]][18] Installer l'extension **[OAuth2OOo.oxt][19]** [![Version][20]][19]

    Vous devez installer cette extension, si elle n'est pas déjà installée.

- [![jdbcDriverOOo logo][21]][22] Installer l'extension **[jdbcDriverOOo.oxt][23]** [![Version][24]][23]

    Vous devez installer cette extension, si elle n'est pas déjà installée.

- ![mContactOOo logo][25] Installer l'extension **[mContactOOo.oxt][26]** [![Version][27]][26]

Redémarrez LibreOffice après l'installation.  
**Attention, redémarrer LibreOffice peut ne pas suffire.**
- **Sous Windows** pour vous assurer que LibreOffice redémarre correctement, utilisez le Gestionnaire de tâche de Windows pour vérifier qu'aucun service LibreOffice n'est visible après l'arrêt de LibreOffice (et tuez-le si ç'est le cas).
- **Sous Linux ou macOS** vous pouvez également vous assurer que LibreOffice redémarre correctement, en le lançant depuis un terminal avec la commande `soffice` et en utilisant la combinaison de touches `Ctrl + C` si après l'arrêt de LibreOffice, le terminal n'est pas actif (pas d'invité de commande).

___

## Utilisation:

Dans LibreOffice / OpenOffice aller à: **Fichier -> Assistants -> Source de données des adresses...**

![mContactOOo screenshot 1][28]

L'**Assistant source de données du carnet d'adresses** s'ouvre.

À l'étape: **1.Type de carnet d'adresses**:
- Sélectionner: **Autre source de données externes**.
- Cliquez sur le bouton: **Suivant**.

![mContactOOo screenshot 2][29]

À l'étape: **2.Paramètres de Connexion**:
- Cliquez sur le bouton: **Paramètres**.

![mContactOOo screenshot 3][30]

Un nouvel assistant s'ouvre. **Propriétés de la source de données**.

A l'étape: **1.Propriétés avancées**.  
Dans Type de base de données:
- Sélectionner: **Contacts Microsoft**.
- Cliquez sur le bouton: **Suivant**.

![mContactOOo screenshot 4][31]

A l'étape: **2.Paramètres de connexion**.  
Dans Général: Entrer ici la chaîne de connexion spécifique au SGDB / pilote.
- Mettre votre compte Microsoft (ie: votre_compte@outlook.fr)
- Cliquez sur le bouton: **Tester la connexion**.

![mContactOOo screenshot 5][32]

Après avoir autorisé l'application [OAuth2OOo][18] à accéder à vos contacts, normalement vous devez voir s'afficher: Test de connexion: Connexion établie.

![mContactOOo screenshot 6][33]

Si la connexion a été etablie, vous pouvez terminer cet assistant avec le bouton **Terminer**.

![mContactOOo screenshot 7][34]

A l'étape: **3.Sélection de table**.  
Si votre source de données comporte plusieurs tables, il vous sera demandé de sélectionner la table principale.  
Dans ce cas sélectionnez la table: **Tous mes contacts**. Si nécessaire et avant toute connexion il est possible de renommer le nom de la table principale dans: **Outils -> Options -> Internet -> mContactOOo -> Nom de la table principale**.

A l'étape: **4.Assignation de champ**.  
Si nécessaire il est possible de renommer les noms des colonnes de la source de données à l'aide du bouton: **Assignation de champ**.  
Veuillez poursuivre cet assistant par le bouton: **Suivant**.

![mContactOOo screenshot 8][35]

A l'étape: **5.Titre de la source de données**.

Il faut créer un fichier odb. Pour cela vous devez:
- **Décocher la case**: Intégrer cette définition du carnet d'adresses dans le document actuel.
- Nommer le fichier odb dans le champ: **Emplacement**.

Il faut également rendre accessible ce fichier odb. Pour cela vous devez:
- **Cocher la case**: Rendre ce carnet d'adresses accessible à tous les modules de LibreOffice
- Nommer le carnet d'adresses dans le champ: **Nom du carnet d'adresses**.

![mContactOOo screenshot 9][36]

Maintenant à vous d'en profiter...

___

## A été testé avec:

* LibreOffice 7.3.7.2 - Lubuntu 22.04 - Python version 3.10.12 - OpenJDK-11-JRE (amd64)

* LibreOffice 7.5.4.2(x86) - Windows 10 - Python version 3.8.16 - Adoptium JDK Hotspot 11.0.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 7.4.3.2(x64) - Windows 10(x64) - Python version 3.8.15  - Adoptium JDK Hotspot 11.0.17 (x64) (under Lubuntu 22.04 / VirtualBox 6.1.38)

* LibreOffice 24.8.0.3 (X86_64) - Windows 10(x64) - Python version 3.9.19 (sous Lubuntu 22.04 / VirtualBox 6.1.38)

* **Ne fonctionne pas avec OpenOffice sous Windows** voir [dysfonctionnement 128569][37]. N'ayant aucune solution, je vous encourrage d'installer **LibreOffice**.

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][13]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Introduction:

Cette extension a été écrite afin de rendre utilisables dans un logiciel libre (LibreOffice ou OpenOffice) vos données personnelles stockées dans votre carnet d'adresses Microsoft Outlook.

Avec l'extension [eMailerOOo][38], elle peut être la source de données pour des [publipostages][39] par courriel (email), à vos correspondants contenus dans votre carnet d'adresses Microsoft Outlook.

Elle vous donnera accès à un système d'information que seules les grandes entreprises sont capables, aujourd'hui, de mettre en œuvre.

### Ce qui a été fait pour la version 1.0.1:

- L'absence ou l'obsolescence des extensions **OAuth2OOo** et/ou **jdbcDriverOOo** nécessaires au bon fonctionnement de **mContactOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Ce qui a été fait pour la version 1.0.2:

- Prise en charge de la version 1.2.0 de l'extension **OAuth2OOo**. Les versions précédentes ne fonctionneront pas avec l'extension **OAuth2OOo** 1.2.0 ou ultérieure.

### Ce qui a été fait pour la version 1.0.3:

- Prise en charge de la version 1.2.1 de l'extension **OAuth2OOo**. Les versions précédentes ne fonctionneront pas avec l'extension **OAuth2OOo** 1.2.1 ou ultérieure.

### Ce qui a été fait pour la version 1.1.0:

- Tous les paquets Python nécessaires à l'extension sont désormais enregistrés dans un fichier [requirements.txt][40] suivant la [PEP 508][41].
- Désormais si vous n'êtes pas sous Windows alors les paquets Python nécessaires à l'extension peuvent être facilement installés avec la commande:  
  `pip install requirements.txt`
- Modification de la section [Prérequis][42].

### Ce qui a été fait pour la version 1.1.1:

- Utilisation du package Python `dateutil` pour convertir les chaînes d'horodatage en UNO DateTime.
- De nombreuses autres corrections...

### Ce qui a été fait pour la version 1.1.2:

- Intégration d'un correctif pour contourner le [dysfonctionnement #159988][43].

### Ce qui a été fait pour la version 1.1.3:

- La création de la base de données, lors de la première connexion, utilise l'API UNO proposée par l'extension jdbcDriverOOo depuis la version 1.3.2. Cela permet d'enregistrer toutes les informations nécessaires à la création de la base de données dans 9 tables texte qui sont en fait [9 fichiers csv][44].
- L'extension vous demandera d'installer les extensions OAuth2OOo et jdbcDriverOOo en version respectivement 1.3.4 et 1.3.2 minimum.
- De nombreuses corrections.

### Ce qui a été fait pour la version 1.1.4:

- Mise à jour du paquet [Python python-dateutil][45] vers la version 2.9.0.post0.
- Mise à jour du paquet [Python decorator][46] vers la version 5.1.1.
- Mise à jour du paquet [Python ijson][47] vers la version 3.3.0.
- Mise à jour du paquet [Python packaging][48] vers la version 24.1.
- Mise à jour du paquet [Python setuptools][49] vers la version 72.1.0 afin de répondre à l'[alerte de sécurité Dependabot][50].
- Mise à jour du paquet [Python validators][51] vers la version 0.33.0.
- L'extension vous demandera d'installer les extensions OAuth2OOo et jdbcDriverOOo en version respectivement 1.3.6 et 1.4.2 minimum.

### Ce qui a été fait pour la version 1.1.5:

- Mise à jour du paquet [Python setuptools][49] vers la version 73.0.1.
- L'extension vous demandera d'installer les extensions OAuth2OOo et jdbcDriverOOo en version respectivement 1.3.7 et 1.4.5 minimum.
- Les modifications apportées aux options de l'extension, qui nécessitent un redémarrage de LibreOffice, entraîneront l'affichage d'un message.
- Support de LibreOffice version 24.8.x.

### Ce qui a été fait pour la version 1.1.6:

- L'extension vous demandera d'installer les extensions OAuth2OOo et jdbcDriverOOo en version respectivement 1.3.8 et 1.4.6 minimum.
- Modification des options de l'extension accessibles via : **Outils -> Options... -> Internet -> mContactOOo** afin de respecter la nouvelle charte graphique.

### Ce qui a été fait pour la version 1.2.0:

- L'extension vous demandera d'installer les extensions OAuth2OOo et jdbcDriverOOo en version respectivement 1.4.0 et 1.4.6 minimum.
- Il est possible de construire l'archive de l'extension (ie: le fichier oxt) avec l'utilitaire [Apache Ant][52] et le fichier script [build.xml][53].
- L'extension refusera de s'installer sous OpenOffice quelle que soit la version ou LibreOffice autre que 7.x ou supérieur.
- Ajout des fichiers binaires nécessaires aux bibliothèques Python pour fonctionner sous Linux et LibreOffice 24.8 (ie: Python 3.9).

### Ce qui a été fait pour la version 1.2.1:

- Mise à jour du paquet [Python packaging][48] vers la version 24.2.
- Mise à jour du paquet [Python setuptools][49] vers la version 75.8.0.
- Mise à jour du paquet [Python six][54] vers la version 1.17.0.
- Mise à jour du paquet [Python validators][51] vers la version 0.34.0.
- Support de Python version 3.13.

### Que reste-t-il à faire pour la version 1.2.1:

- Ajouter de nouvelles langues pour l’internationalisation...

- Tout ce qui est bienvenu...

[1]: </img/contact.svg#collapse>
[2]: <https://prrvchr.github.io/mContactOOo/>
[3]: <https://prrvchr.github.io/mContactOOo>
[4]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/TermsOfUse_fr>
[5]: <https://prrvchr.github.io/mContactOOo/source/mContactOOo/registration/PrivacyPolicy_fr>
[6]: <https://prrvchr.github.io/mContactOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-121>
[7]: <https://prrvchr.github.io/README_fr>
[8]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[9]: <https://www.openoffice.org/fr/Telecharger/>
[10]: <https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview>
[11]: <https://wiki.openoffice.org/wiki/Documentation/DevGuide/Database/Driver_Service>
[12]: <https://github.com/prrvchr/mContactOOo>
[13]: <https://github.com/prrvchr/mContactOOo/issues/new>
[14]: <https://prrvchr.github.io/OAuth2OOo/README_fr#pr%C3%A9requis>
[15]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#pr%C3%A9requis>
[16]: <https://prrvchr.github.io/mContactOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-110>
[17]: <https://prrvchr.github.io/OAuth2OOo/img/OAuth2OOo.svg#middle>
[18]: <https://prrvchr.github.io/OAuth2OOo/README_fr>
[19]: <https://github.com/prrvchr/OAuth2OOo/releases/latest/download/OAuth2OOo.oxt>
[20]: <https://img.shields.io/github/v/tag/prrvchr/OAuth2OOo?label=latest#right>
[21]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[22]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[23]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[24]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[25]: <img/mContactOOo.svg#middle>
[26]: <https://github.com/prrvchr/mContactOOo/releases/latest/download/mContactOOo.oxt>
[27]: <https://img.shields.io/github/downloads/prrvchr/mContactOOo/latest/total?label=v1.2.1#right>
[28]: <img/mContactOOo-1_fr.png>
[29]: <img/mContactOOo-2_fr.png>
[30]: <img/mContactOOo-3_fr.png>
[31]: <img/mContactOOo-4_fr.png>
[32]: <img/mContactOOo-5_fr.png>
[33]: <img/mContactOOo-6_fr.png>
[34]: <img/mContactOOo-7_fr.png>
[35]: <img/mContactOOo-8_fr.png>
[36]: <img/mContactOOo-9_fr.png>
[37]: <https://bz.apache.org/ooo/show_bug.cgi?id=128569>
[38]: <https://prrvchr.github.io/eMailerOOo/README_fr>
[39]: <https://fr.wikipedia.org/wiki/Publipostage>
[40]: <https://github.com/prrvchr/mContactOOo/releases/latest/download/requirements.txt>
[41]: <https://peps.python.org/pep-0508/>
[42]: <https://prrvchr.github.io/mContactOOo/README_fr#pr%C3%A9requis>
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
