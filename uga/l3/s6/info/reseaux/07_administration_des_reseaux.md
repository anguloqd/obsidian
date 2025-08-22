# 07 // administration des réseaux

[07_administration_des_reseaux_transparents_administration_reseaux.pdf](ressources/07_administration_des_reseaux_transparents_administration_reseaux.pdf)

# Administration des réseaux

## Introduction générale

L'administration des réseaux constitue l'ensemble des moyens mis en œuvre pour garantir l'efficacité du système informatique et sa disponibilité continue. Cette discipline englobe également la surveillance des coûts et la planification des évolutions nécessaires à l'infrastructure réseau.

L'administration d'un réseau suppose l'existence d'une base d'information décrivant l'ensemble des objets administrés. Cette approche systématique devient essentielle compte tenu du grand nombre d'objets concernés et nécessite un dialogue permanent entre les différents composants du réseau.

## Les cinq domaines d'administration selon l'ISO

L'Organisation internationale de normalisation (ISO) définit cinq domaines fondamentaux pour l'administration des réseaux, chacun répondant à des besoins spécifiques de gestion et de maintenance.

### Gestion des configurations

La gestion des configurations consiste à maintenir un inventaire précis des ressources matérielles et logicielles du réseau. Cette discipline inclut le paramétrage des équipements et de la topologie réseau.

Les éléments surveillés comprennent :
- Le type et les caractéristiques des équipements
- Les versions et fonctions des logiciels
- La répartition géographique des équipements gérés

Cette approche systématique permet aux administrateurs de connaître précisément l'état de leur infrastructure à tout moment.

### Gestion des performances

La gestion des performances met en œuvre des moyens permettant d'évaluer le comportement des objets gérés et de déterminer si la qualité de service (QoS) requise est effectivement rendue aux utilisateurs.

Les activités principales incluent :
- La collecte d'informations par audit régulier
- La mesure du trafic réseau
- L'évaluation des temps de réponse
- Le calcul des taux d'erreurs
- Le stockage et l'archivage des données
- L'interprétation des mesures pour calculer la charge système

Ces mesures permettent d'identifier les goulots d'étranglement et d'optimiser les performances globales du réseau.

### Gestion des pannes

La gestion des pannes vise l'optimisation des ressources et des moyens disponibles pour assurer un diagnostic rapide de toute défaillance, qu'elle soit externe (coupure d'un lien public) ou interne (panne d'un routeur).

Les fonctionnalités essentielles comprennent :
- La surveillance et le traitement des alarmes
- La localisation et le diagnostic des incidents
- La mémorisation des anomalies par journalisation
- La définition des opérations curatives

Cette approche proactive permet de minimiser l'impact des pannes sur les utilisateurs finaux.

### Gestion de la comptabilité

La fonction comptabilité permet d'imputer les coûts du réseau à ses utilisateurs selon l'usage réel des moyens, constituant ainsi une comptabilité analytique précise.

Les éléments gérés incluent :
- La définition des centres de coût
- La mesure des dépenses structurelles et leur répartition
- La mesure des consommations par service
- L'imputation des coûts aux utilisateurs concernés

Cette approche favorise une utilisation responsable des ressources réseau.

### Gestion de la sécurité

La gestion de la sécurité regroupe tous les domaines nécessaires pour assurer l'intégrité des informations traitées et des objets administrés.

Les aspects couverts comprennent :
- Le contrôle d'accès au réseau
- La confidentialité des données
- L'intégrité des données
- L'authentification des utilisateurs
- La non-répudiation des transactions

## Le protocole SNMP

### Présentation générale

SNMP (Simple Network Management Protocol) constitue un protocole créé en 1988 par l'IETF (Internet Engineering Task Force) pour répondre aux besoins d'administration du réseau Internet. Les objectifs principaux de SNMP visent à fédérer en un standard unique des protocoles multiples liés aux équipementiers, tout en permettant un déploiement rapide et à moindre coût.

Ce protocole permet aux administrateurs réseau de gérer les équipements du réseau et de surveiller leur comportement de manière centralisée et standardisée.

### Architecture SNMP

Chaque élément potentiellement administrable dispose d'un agent, programme fonctionnant sur les éléments réseau (commutateurs, routeurs) et les stations de travail ou serveurs. Tous les agents sont contrôlés par une ou plusieurs stations d'administration appelées stations maîtresses (NMS : Network Management System).

Les informations d'administration d'un élément du réseau sont stockées dans une structure arborescente appelée MIB (Management Information Base), qui constitue la base de données des objets administrables.

### Caractéristiques techniques

SNMP est défini par trois principaux RFC (1157, 1213 et 1155). Le protocole repose sur l'échange de messages (requêtes et réponses) entre l'élément réseau à surveiller et la station d'administration.

Les messages SNMP sont encapsulés dans des paquets UDP utilisant les numéros de port 161 et 162. Cette approche présente l'avantage de la simplicité et nécessite peu de puissance pour faire fonctionner l'agent. L'inconvénient réside dans le caractère non fiable du protocole UDP : une écriture sera suivie d'une lecture de la valeur pour vérification, et en cas de non-réponse, la requête est réitérée.

### Types de messages SNMP

Cinq types de messages ou requêtes SNMP peuvent être échangés (SNMPv1) entre agent et manager :

- **Get Request** : demande de la valeur courante de la variable indiquée
- **Get Next Request** : demande de la valeur "suivante" dans l'arborescence
- **Get Response** : envoi de la valeur demandée
- **Set Request** : configuration d'une variable à la valeur indiquée
- **Trap** : indication autonome de l'agent

### Fonctionnement des composants

La station maîtresse (manager) est chargée d'interroger régulièrement les agents et constitue également la destinataire des alertes (traps) générées spontanément par les agents. Plus la fréquence d'interrogation est élevée, plus les informations remontées seront détaillées, mais plus le trafic sera important.

Les agents répondent aux requêtes de la station maîtresse en renvoyant la valeur du paramètre recherché, positionnent des variables aux valeurs qui leur sont envoyées, et émettent spontanément une alarme lors d'un événement critique. Ces agents ne peuvent fonctionner que sur un CPU ou avec des extensions dédiées et possèdent des noms de communauté ("public" par défaut) pour se protéger des requêtes de lecture ou d'écriture indésirables.

## Les MIB (Management Information Base)

### Structure générale

Les MIB stockent les informations d'administration d'un élément du réseau sous forme arborescente. Chaque objet de la MIB possède un identificateur unique appelé OID (Object ID) et se conforme au codage ASN.1 (Abstract Syntax Notation) de l'ISO. Les objets peuvent être de différents formats : numérique entier, suite de bits, suite d'octets, nul, identificateur d'objet, ou séquence.

### Types de MIB

Une partie de la MIB, la MIB-II, doit toujours être présente sur tous les équipements compatibles SNMP. De multiples MIB ont été définies en complément selon différents critères :

- **Par technologies** : Ethernet, Token-Ring, FDDI, 100VG-AnyLan, X.25
- **Par équipements** : répéteur Ethernet, Bridge, Source-Route bridge, sonde
- **Par protocole** : BGP-4, PPP, RIP-2, OSPF, DNS, AppleTalk, DECnet

### Structure hiérarchique

La structure de la MIB se compose d'une racine non nommée à partir de laquelle sont référencés de façon absolue les objets (nœuds de l'arbre). Chaque nœud de l'arbre possède un nom symbolique, et chaque objet peut être identifié de façon symbolique ou en utilisant son OID numérique.

Par exemple, l'objet `iso.org.dod.internet.mgmt.mib.system.sysDescr.0` correspond à l'OID `1.3.6.1.2.1.1.1.0`.

## Logiciels de supervision

### Fonctionnalités génériques

Les logiciels de supervision ont pour tâche de mettre en œuvre tous les mécanismes génériques autour de SNMP. Ces outils proposent plusieurs fonctionnalités essentielles :

- L'enregistrement (log) avec filtrage divers et déclenchement d'actions sur événement (trap reçu)
- La découverte du réseau (IP) et le maintien d'une base de données des éléments découverts (adresses MAC, adresses IP, type d'équipements)
- La surveillance minimale de la présence de ces éléments par polling périodique
- L'aide à la construction de graphes par interrogation de variables spécifiques
- La mise en œuvre de scripts combinant polling, conditions et actions

### Auto-découverte

L'auto-découverte ne consiste pas à localiser physiquement les machines, mais à connaître leur existence par plusieurs méthodes :

- L'écoute des adresses réseau qui communiquent
- L'interrogation des adresses potentielles à l'aide de ping
- L'interrogation SNMP par requête Get sur une valeur élémentaire de la MIB II

Ce processus fonctionne en permanence en tâche de fond et prend en compte dynamiquement l'apparition de nouveaux nœuds dans le réseau ainsi que la disparition temporaire ou définitive de certains autres, signalée par une alarme.

### Solutions disponibles

Plusieurs logiciels d'administration sont disponibles sur le marché :

**Solutions commerciales** :
- OpenView d'HP
- Tivoli Netview d'IBM
- PRTG de Paessler
- WhatsUp Gold d'Ipswich

**Solutions open source** :
- Zabbix
- Zenoss
- Nagios

## Sécurité SNMP

### Vulnérabilités des versions 1 et 2c

Les versions SNMP 1 et 2c ne sont pas sûres pour plusieurs raisons :

- Les trames circulent en clair sur le réseau, permettant la récupération facile du nom de communauté
- Même si l'agent est paramétré pour ne répondre qu'à certaines adresses IP, le spoofing d'adresse IP reste possible
- Il n'existe pas de notion d'"utilisateur authentifié"

### SNMP version 3 (SNMPv3)

La version 3 de SNMP a été créée pour résoudre ces problèmes de sécurité. Cette version comprend plusieurs composants :

- Un dispatcher (répartiteur)
- Un sous-système de traitement des messages
- Un sous-système de sécurité
- Un sous-système de contrôle d'accès

### Modèle de sécurité utilisateur

Le module le plus commun repose sur l'utilisateur ou un "modèle de sécurité utilisateur" qui apporte plusieurs améliorations :

**Authenticité et intégrité** :
- Des utilisateurs peuvent être créés, chacun disposant d'un identifiant et d'un mot de passe personnel
- Les messages ont une signature numérique générée par hachage (MD5 ou SHA)

**Confidentialité** :
- Les messages peuvent être chiffrés au moyen d'un algorithme (DES) à clé secrète

**Validité temporaire** :
- Utilise une horloge synchronisée avec une fenêtre de 150 secondes et un contrôle de séquence pour éviter les attaques par rejeu

### Niveaux de sécurité

SNMPv3 définit trois niveaux de sécurité :

- **noAuthPriv** : Pas d'authentification, pas de confidentialité
- **authNoPriv** : Authentification sans confidentialité  
- **authPriv** : Authentification avec confidentialité

## Métrologie réseau

### Définition et objectifs

La métrologie désigne par définition la science des mesures. Dans le cadre des réseaux informatiques, son objectif consiste à "connaître et comprendre le réseau" afin de pouvoir :

- Intervenir dans l'urgence en cas de problème
- Anticiper l'évolution du réseau
- Planifier l'introduction de nouvelles applications
- Améliorer les performances pour les utilisateurs

### Protocoles utilisés

**SNMP** :
- Récupération à intervalles réguliers des valeurs des compteurs sur les équipements actifs
- Mise à jour d'histogrammes à partir des données collectées

**NetFlow** :
- Protocole développé par Cisco permettant la comptabilisation de flux réseaux
- Supporté par la majorité des vendeurs d'équipements réseaux
- Des protocoles similaires existent : sFlow chez InMon, LFAP chez Riverstone

### Outils de visualisation

Le programme MRTG constitue un exemple d'outil de métrologie permettant de visualiser le trafic entrant et sortant des interfaces réseau sous forme de graphiques temporels.

## Autres outils d'administration

### Protocole HTTP

L'utilisation d'un navigateur Web comme outil d'interrogation présente certains avantages. L'agent devient plus autonome en intégrant un mini-serveur Web, mais doit prendre en charge une partie des fonctions de mise en forme des informations. Un protocole légèrement mieux adapté que HTTP, comme HTTPS, doit être adopté pour gérer plus complètement les aspects liés à la sécurité.

### Téléchargement et mise à jour

La mise à jour des systèmes d'exploitation et des fichiers de configuration s'effectue généralement par TFTP (Trivial File Transfer Protocol), protocole simple et léger adapté à ces tâches spécifiques.

### Telnet et SSH

Ces protocoles permettent d'accéder à l'interface de configuration des matériels réseau (switch, routeur). SSH offre une version sécurisée de Telnet avec chiffrement des communications.

### Analyseurs de protocoles

Les analyseurs de protocoles constituent des logiciels permettant d'intercepter et de décoder le trafic réseau. La connexion réseau est placée dans un mode d'opération "libéral" (promiscuous) où tous les paquets transitant par le segment du réseau sont acceptés, y compris ceux destinés aux autres nœuds.

Ces outils s'avèrent utiles pour comprendre les protocoles de réseau et corriger les dysfonctionnements, mais posent des problèmes de sécurité en raison de leur capacité d'interception du trafic.