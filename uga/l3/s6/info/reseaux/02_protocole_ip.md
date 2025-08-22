# 02 // protocole IP

[02_protocole_ip_2_le_protocole_ip.pdf](ressources/02_protocole_ip_2_le_protocole_ip.pdf)

# Le protocole IP

## Introduction à TCP/IP

Le protocole TCP/IP constitue l'épine dorsale des communications réseau modernes. Au sens strict, TCP/IP désigne un ensemble de deux protocoles complémentaires : IP (Internet Protocol), qui opère au niveau 3 (réseau) du modèle OSI, et TCP (Transmission Control Protocol), qui fonctionne au niveau 4 (transport). Dans la pratique, cette appellation recouvre une famille complète de protocoles interconnectés, formant ce qu'on appelle une pile de protocoles.

L'adoption quasi universelle de TCP/IP s'explique par sa capacité à unifier les communications, que ce soit sur des réseaux locaux (LAN) ou sur l'Internet global. Cette technologie trouve ses racines dans les recherches menées par le DARPA (Defense Advanced Research Projects Agency) dès la fin des années 1960.

### Contexte historique

En 1969, le projet ARPAnet (Advanced Research Projects Agency Network) concrétise les premières expérimentations en reliant quatre sites informatiques. Cette initiative marque le début d'une révolution technologique qui transformera radicalement les communications mondiales.

Les protocoles TCP/IP deviennent des standards militaires en 1983, période où le réseau ARPAnet cède progressivement la place à l'Internet. Cette transition coïncide avec l'extension du réseau au-delà du domaine universitaire vers le secteur commercial.

L'intégration précoce de TCP/IP dans le système Unix, notamment dans le noyau BSD (Berkeley Software Distribution), contribue significativement à sa popularité et à son adoption massive.

Depuis 1990, l'Europe connaît une explosion de l'utilisation d'IP dans le secteur non académique. Trois facteurs principaux expliquent cette montée en puissance :

- **L'interopérabilité** : un protocole commun permet la communication entre équipements de constructeurs différents
- **L'attrait commercial de l'Internet** : l'Internet repose entièrement sur les protocoles et services TCP/IP
- **La prolifération des outils de gestion** : le protocole SNMP (Simple Network Management Protocol) devient la référence en matière de gestion de réseau

## Architecture TCP/IP

Les protocoles TCP/IP s'organisent selon une architecture à quatre couches, souvent désignée sous le nom de modèle DoD (Department of Defense), en référence à ses origines militaires américaines.

### Couche accès réseau

Cette couche la plus basse gère la connexion physique avec les infrastructures matérielles : câbles, circuits d'interfaces électriques (transceivers), cartes réseau et protocoles d'accès au support physique. Elle intègre généralement les fonctionnalités des couches physique et liaison de données du modèle OSI.

Les utilisateurs interagissent rarement directement avec cette couche, car TCP/IP masque volontairement ces aspects techniques. Dans les systèmes Unix, ces protocoles apparaissent sous forme de pilotes de périphériques (drivers) et de programmes associés.

### Couche Internet

La couche Internet fournit l'adressage logique nécessaire aux interfaces physiques. Le protocole IP (Internet Protocol) constitue l'implémentation de référence de cette couche dans le modèle DoD.

Cette couche établit la correspondance entre adresses logiques et adresses physiques grâce aux protocoles ARP (Address Resolution Protocol – RFC 826) et RARP (Reverse Address Resolution Protocol). Le protocole ICMP (Internet Control Message Protocol) gère les incidents, diagnostics et conditions particulières liés au fonctionnement d'IP.

La fonction de routage des datagrammes entre hôtes distants relève également de cette couche, qui sert d'interface aux couches supérieures du modèle.

### Couche transport hôte à hôte

Cette couche définit les connexions entre hôtes du réseau. Le modèle DoD comprend deux protocoles principaux :

**TCP (Transmission Control Protocol)** assure un service de transmission fiable avec détection et correction d'erreurs. Il supporte les connexions simultanées et full-duplex, permettant l'établissement de multiples connexions sur un même hôte avec transmission simultanée des données.

**UDP (User Datagram Protocol)** offre un service de transmission plus simple, sans garantie de fiabilité, adapté aux applications qui n'exigent pas les fonctionnalités avancées de TCP.

### Couche application

La couche application couronne l'architecture TCP/IP en permettant aux logiciels d'utiliser les services des protocoles de transport. Les protocoles d'application se divisent en deux catégories :

**Protocoles orientés utilisateurs** :
- TELNET : émulation de terminal pour sessions distantes
- FTP : transfert de fichiers (File Transfer Protocol)
- SMTP : transfert de courrier électronique (Simple Mail Transfer Protocol)

**Protocoles orientés administration** :
- DNS (Domain Name Service) : correspondance entre adresses IP et noms d'hôtes
- RIP (Routing Information Protocol) : gestion du routage
- NFS (Network File System) : partage de fichiers entre machines

## Comparaison avec le modèle OSI

Comme dans le modèle OSI, les données transitent de haut en bas lors de l'émission et de bas en haut lors de la réception. Chaque couche ajoute ses propres informations de contrôle sous forme d'en-têtes pour garantir une transmission correcte.

Les terminologies diffèrent entre les deux modèles. Le modèle OSI utilise le terme PDU (Protocol Data Unit) pour décrire les données de chaque couche. Le modèle DoD emploie une nomenclature spécifique :
- Messages et flots au niveau application
- Segments et paquets au niveau transport
- Datagrammes au niveau Internet
- Trames au niveau accès réseau

Le multiplexage/démultiplexage permet à plusieurs protocoles de couches supérieures d'utiliser un protocole commun de couche inférieure. Un réseau Ethernet supportant IP peut simultanément gérer d'autres protocoles comme IPX. Le champ EtherType identifie le protocole réseau destinataire, autorisant le multiplexage à la source et le démultiplexage à la destination.

| Type de réseau | EtherType |
|----------------|-----------|
| IP | 0x800 |
| ARP | 0x806 |
| Banyan Systems | 0xBAD |
| DEC LAT | 0x6004 |
| AT&T | 0x8008 |
| AppleTalk | 0x8069 |
| Novell | 0x8137-0x8138 |

Lorsque la couche IP reçoit un paquet Ethernet, elle identifie les paquets TCP ou UDP grâce à un champ de 8 bits dans l'en-tête IP.

## Fonctions du protocole IP

Le protocole Internet (RFC 791) fournit le service de transmission de paquets fondamental sur lequel reposent tous les réseaux TCP/IP. Tous les protocoles des couches adjacentes utilisent IP pour transmettre leurs données, faisant de ce protocole le point de passage obligé de toutes les communications TCP/IP.

IP fonctionne au-dessus de diverses technologies réseau : Ethernet, Token-Ring, FDDI, ATM, démontrant sa polyvalence et son indépendance vis-à-vis du matériel sous-jacent.

### Fonctions principales

Les fonctions essentielles d'IP comprennent :
- La définition du format des datagrammes
- L'établissement du plan d'adressage Internet
- L'interface entre les couches accès réseau et transport
- Le routage des datagrammes vers les destinations distantes
- La fragmentation et le réassemblage des datagrammes

IP constitue un protocole non orienté connexion, routant chaque datagramme indépendamment des autres. Il délègue aux protocoles des autres couches la responsabilité d'établir des connexions si nécessaire.

Le réseau IP emploie la méthode "Best Effort" (meilleur effort), garantissant une livraison optimale sans assurance absolue de réussite. IP ne contient qu'un total de contrôle d'en-tête (header checksum) sans mécanisme de vérification des données, laissant cette responsabilité aux protocoles des autres couches.

Les protocoles de couches supérieures peuvent spécifier des paramètres de qualité de service (QoS). La couche IP tente alors de faire correspondre ces exigences avec les services fournis par le matériel réseau sous-jacent.

### Format du datagramme

Le datagramme IP comprend un en-tête IP suivi des données provenant des protocoles supérieurs.

```
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

La longueur standard de l'en-tête est de 20 octets (5 mots de 32 bits), le sixième mot étant optionnel. Le champ IHL (Internet Header Length) indique la longueur variable de l'en-tête en mots de 32 bits.

Le champ Version (4 bits) identifie le format de l'en-tête IP. La version actuelle IPv4 utilise la valeur 4, tandis qu'IPv6 utilise la valeur 6 et supporte des adresses de 128 bits.

Le champ Type of Service (TOS) informe les réseaux de la qualité de service désirée, spécifiant la priorité, les délais, le débit et la fiabilité. Bien que souvent ignoré par les implémentations actuelles, ce champ gagnera probablement en importance.

Le champ Total Length contient la longueur totale du datagramme (en-tête + données) en octets. L'Internet suggère que les réseaux supportent des datagrammes de 576 octets sans fragmentation, bien que la plupart des implémentations gèrent des tailles bien supérieures.

Le champ Time To Live (TTL) représente la durée de vie maximale du datagramme en secondes, décrémentée à chaque routeur. Quand le TTL atteint zéro, le datagramme est détruit et un message ICMP informe l'expéditeur. Cette mécanisme limite la durée de vie des segments TCP et élimine les boucles de routage. Les valeurs initiales communes sont 32 ou 64 secondes.

L'adresse de destination (32 bits) identifie le réseau et l'hôte destinataires. Si cette adresse correspond au réseau local, le paquet est transmis directement ; sinon, il est envoyé vers une passerelle pour routage.

### Routage des datagrammes

Les passerelles Internet, plus précisément appelées routeurs IP, acheminent les paquets entre réseaux en utilisant le protocole Internet. La terminologie TCP/IP traditionnelle distingue deux types d'équipements réseau : les passerelles, qui transmettent les paquets entre réseaux, et les hôtes, qui ne le font pas.

Une machine multiconnectée (connectée à plusieurs réseaux) peut transmettre des paquets et fonctionne alors comme une passerelle.

### Fragmentation des datagrammes

Lorsqu'une passerelle interconnecte des réseaux physiques différents, la division des datagrammes peut s'avérer nécessaire. Chaque type de réseau définit une unité de transfert maximale (MTU), correspondant à la taille maximale des paquets transmissibles.

| Type de réseau | MTU (octets) |
|----------------|--------------|
| Ethernet | 1 500 |
| IEEE 802.3 | 1 492 |
| Token-Ring | 4 440 à 17 940 |
| FDDI | 4 352 |
| IEEE 802.4 | 8 166 |

Si un datagramme dépasse la MTU du réseau de destination, la fragmentation divise le datagramme en fragments plus petits. Chaque fragment conserve le format d'un datagramme normal.

Le deuxième mot de l'en-tête contient les informations de fragmentation :
- Le champ Identification indique le datagramme d'origine
- Le champ Fragment Offset (multiple de 8 octets) précise la position du fragment
- Le bit More Fragments (MF) dans le champ Flags indique s'il reste des fragments (MF=1) ou si c'est le dernier (MF=0)

Le réassemblage s'effectue uniquement par l'hôte de destination, jamais par les routeurs intermédiaires.

### Transmission vers la couche transport

Le champ Protocol identifie le protocole de couche supérieure destinataire des données IP, permettant le multiplexage/démultiplexage vers les protocoles appropriés.

Valeurs courantes :
- TCP : 6
- UDP : 17  
- ICMP : 1

Sous Unix, ces valeurs sont stockées dans le fichier `/etc/protocols`.

## Adressage IP

### L'adresse IP

TCP/IP offre une vision logique du réseau, indépendante de la technologie matérielle sous-jacente. Les nœuds du réseau sont identifiés par une adresse logique de 32 bits : l'adresse IP (IPv4).

Cette adresse comporte deux parties : l'identifiant de réseau (netid) et l'identifiant d'hôte (hostid). Un masque de sous-réseau (netmask) permet au logiciel IP de déterminer la partie réseau en effectuant un ET logique.

Historiquement, l'Internet était organisé en classes d'adresses, le nombre de bits dédiés au réseau et à l'hôte variant selon la classe.

```
Classe A : 0xxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (0.0.0.0 à 127.255.255.255)
Classe B : 10xxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (128.0.0.0 à 191.255.255.255)  
Classe C : 110xxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (192.0.0.0 à 223.255.255.255)
Classe D : 1110xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (224.0.0.0 à 239.255.255.255)
Classe E : 1111xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (240.0.0.0 à 247.255.255.255)
```

Les classes A, B et C étaient destinées aux adresses d'hôtes, la classe D à la multidiffusion (multicasting) et la classe E réservée pour un usage ultérieur.

- **Classe A** : 7 bits de réseau, 24 bits d'hôte (moins de 128 réseaux, millions d'hôtes par réseau)
- **Classe B** : 14 bits de réseau, 16 bits d'hôte (milliers de réseaux, milliers d'hôtes par réseau)
- **Classe C** : 21 bits de réseau, 8 bits d'hôte (millions de réseaux, moins de 254 hôtes par réseau)

### CIDR et adressage sans classe

La notion de classes d'adresses est devenue obsolète avec l'introduction du CIDR (Classless Internet Domain Routing) en 1993 (RFC 1518 et 1519). Ce système permet l'utilisation de masques arbitraires appliqués à n'importe quelle adresse, organisant le regroupement géographique des adresses pour optimiser les tables de routage.

Les adresses IP s'expriment en notation décimale pointée (quatre nombres décimaux séparés par des points). Le masque peut être spécifié en notation décimale pointée ou en notation CIDR (nombre de bits à 1) :

```
192.168.200.254/255.255.255.0  (notation classique)
192.168.200.254/24             (notation CIDR)
```

### Adresses IP spéciales

Plusieurs adresses IP ont des significations particulières :

- **Adresse réseau** : hostid = 0 (exemple : 192.168.1.0)
- **Diffusion dirigée** : tous les bits hostid à 1 (exemple : 192.168.1.255 pour un réseau de classe C)
- **Diffusion limitée** : 255.255.255.255 (atteint tous les nœuds du réseau local)
- **Adresse nulle** : 0.0.0.0 (utilisée lors de la détermination d'adresse IP ou comme route par défaut)
- **Adresse de bouclage** : 127.x.x.x (renvoi vers l'application locale, généralement 127.0.0.1)

### Types de transmission

**Unicast** : transmission vers une adresse IP individuelle, utilisée pour la communication entre deux nœuds.

**Broadcast** : transmission vers tous les nœuds d'un réseau spécifique.

**Multicast** : transmission vers un groupe de destinataires utilisant une adresse de classe D. Les hôtes du groupe conservent leur adresse IP normale (classe A, B ou C) et peuvent recevoir des données soit individuellement soit via l'adresse de groupe.

Pour que la multidiffusion fonctionne, les hôtes doivent pouvoir rejoindre et quitter dynamiquement les groupes. Cette fonctionnalité n'est pas disponible dans les anciennes implémentations d'IP.

### Attribution des adresses IP

Pour les réseaux connectés à Internet, l'obtention d'un identifiant de réseau unique est obligatoire. L'IANA (Internet Address Network Authority) constitue l'autorité suprême, ayant délégué la zone européenne au RIPE NCC (Réseaux IP Européens - Network Coordination Centre).

Pour réduire les besoins en nouvelles adresses, la RFC 1918 définit des plages d'adresses privées :
- Classe A : 10.0.0.0 à 10.255.255.255
- Classe B : 172.16.0.0 à 172.31.255.255  
- Classe C : 192.168.0.0 à 192.168.255.255

Ces adresses, destinées aux réseaux privés, nécessitent des mécanismes de translation (NAT) pour accéder à Internet.

### Sous-réseaux

Le sous-adressage (subnetting) divise une plage d'adresses en sous-réseaux IP grâce à un masque de sous-réseau. Ce masque étend la partie réseau en empruntant des bits à la partie hôte.

Règles du masque :
- Bit à 1 : bit de réseau
- Bit à 0 : bit d'hôte

Le sous-réseau n'est reconnu qu'localement. Depuis Internet, l'adresse reste interprétée comme une adresse IP standard.

La RFC 950 déconseille l'utilisation de sous-réseaux dont tous les bits sont à 0 ou à 1 pour éviter les ambiguïtés.

### Sur-réseaux (supernets)

Le sur-adressage, conçu en 1985, consiste à regrouper plusieurs adresses de classe C pour créer une classe virtuelle intermédiaire entre les classes B et C.

Cette technique, principalement destinée aux fournisseurs d'accès Internet (FAI), utilise le CIDR pour résumer un bloc d'adresses en une seule entrée de table de routage : (adresse de base, masque de sur-réseau).

Exemple :
```
Bloc : (192.55.16.0, 255.255.240.0)
Notation CIDR : 192.55.16.0/20
```

Ce bloc contient 16 adresses de classe C (2^4 = 16), déterminées par les 4 bits variables du masque.

### Protocoles de résolution d'adresse

#### ARP (Address Resolution Protocol)

ARP établit la correspondance dynamique entre adresses IP (32 bits) et adresses MAC physiques nécessaires à la transmission sur les réseaux de couche 2.

Processus ARP :
1. L'hôte A envoie une requête ARP en diffusion contenant son adresse IP/MAC et l'IP de B
2. Seul l'hôte B répond en incluant son adresse MAC
3. A met à jour son cache ARP avec cette information
4. Les entrées du cache expirent après un délai configurable (généralement 15 minutes)

Le paquet ARP utilise la valeur EtherType 0x806. Le protocole suppose que le réseau physique supporte la diffusion.

#### RARP (Reverse ARP)

RARP permet aux stations sans disque d'obtenir leur adresse IP auprès d'un serveur distant. Le client diffuse une requête RARP (EtherType 0x8035) et accepte la première réponse reçue.

Le serveur RARP maintient une table des adresses IP indexée par les adresses matérielles. Contrairement à ARP, RARP nécessite généralement un processus dédié (démon) sur le serveur.

## Le protocole ICMP

ICMP (Internet Control Message Protocol, RFC 792) constitue une partie intégrante d'IP, gérant le contrôle, la détection d'erreurs et la transmission d'informations pour TCP/IP.

Toutes les implémentations IP peuvent générer des messages ICMP, encapsulés dans des datagrammes IP (champ Protocol = 1). Les messages ICMP ne génèrent jamais de réponses (sauf echo request) pour éviter les cascades de messages.

### Types de messages ICMP

**Contrôle de flux** : message de congestion envoyé à la source pour suspendre temporairement l'envoi de datagrammes.

**Destination inaccessible** : signale qu'une destination (réseau, hôte ou port) n'est pas joignable.

**Redirection de route** : indique à un hôte d'utiliser une passerelle différente, plus appropriée.

**Vérification d'hôtes distants** : 
- Echo request (type 8) et echo reply (type 0) permettent de tester la connectivité
- La commande `ping` utilise ces messages et mesure la latence
- La commande `traceroute` utilise des paquets UDP avec TTL croissant pour découvrir la route

## IPv6

IPv6 succède à IPv4 en conservant ses meilleures fonctionnalités tout en corrigeant ses limitations. Les principales améliorations incluent :

**Adressage étendu** : adresses de 128 bits (16 octets) offrant un espace d'adressage de 3,4×10^38 adresses, notées en 8 groupes de 4 chiffres hexadécimaux séparés par des deux-points.

Exemple : `8000:0000:0000:0000:0123:4567:89AB:CDEF`

**En-tête simplifié** : réduction de 14 à 7 champs pour accélérer le traitement par les routeurs et améliorer le débit global.

**Flexibilité des options** : les champs obligatoires deviennent optionnels, permettant aux routeurs d'ignorer plus facilement les options non pertinentes.

**Sécurité renforcée** : mécanismes d'authentification et de confidentialité intégrés.

**Qualité de service améliorée** : attention accrue aux différents types de services et à leurs exigences spécifiques.