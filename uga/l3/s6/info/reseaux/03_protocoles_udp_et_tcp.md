## 03 // protocoles UDP et TCP

[03_protocoles_udp_et_tcp_3_les_protocoles_udp_tcp.pdf](ressources/03_protocoles_udp_et_tcp_3_les_protocoles_udp_tcp.pdf)

## Les protocoles UDP et TCP

Les protocoles de transport UDP (User Datagram Protocol) et TCP (Transport Control Protocol) constituent la couche de transport du modèle OSI. Ces deux protocoles s'exécutent au-dessus du protocole IP et utilisent les services qu'il fournit pour assurer la communication entre processus distants.

TCP garantit un service de transmission fiable avec détection et correction d'erreurs de bout en bout, tandis qu'UDP offre un service de transmission de datagrammes sans connexion. Cette différence fondamentale détermine leurs domaines d'application respectifs.

### Architecture et adressage

#### Concept de socket

Un socket représente un point de communication permettant à un processus d'émettre et de recevoir des informations. Il combine une adresse IP et un numéro de port, créant ainsi un identifiant unique pour un processus sur une machine donnée. La combinaison de deux sockets définit complètement une connexion TCP ou un échange UDP.

#### Numéros de port standard

La RFC 1060 établit les ports prédéfinis pour les services réseau courants :

| Port | Service |
|------|---------|
| 20   | FTP     |
| 23   | Telnet  |
| 25   | SMTP    |
| 53   | DNS     |
| 69   | TFTP    |
| 80   | HTTP    |

### Protocole UDP

Le protocole UDP permet aux applications d'accéder directement à un service de transmission de datagrammes, similaire au service offert par IP mais avec des fonctionnalités supplémentaires au niveau transport.

#### Caractéristiques principales

UDP implémente un mécanisme d'identification des processus d'application via les numéros de port. Son approche orientée datagrammes évite les complexités liées à la gestion des connexions (ouverture, maintien, fermeture).

Le protocole excelle dans les applications de diffusion et multidiffusion. Les applications suivant un modèle interrogation-réponse peuvent utiliser UDP efficacement, la réponse servant d'accusé de réception positif. Si aucune réponse n'arrive dans le délai imparti, l'application retransmet simplement la requête.

UDP ne séquence pas les données et ne garantit pas leur remise conforme. Il peut optionnellement vérifier l'intégrité des données uniquement via un total de contrôle. Cette simplicité rend UDP plus rapide et efficace que TCP, mais moins robuste.

#### Applications utilisant UDP

Malgré l'absence de sécurité intégrée, de nombreuses applications reposent sur UDP :

- TFTP (Trivial File Transfer Protocol)
- DNS (Domain Name System)
- NFS (Network File System)
- SNMP (Simple Network Management Protocol)
- RIP (Routing Information Protocol)

#### Structure de l'en-tête UDP

L'en-tête UDP possède une taille fixe de 8 octets :

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Length             |           Checksum            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Le champ Source Port (16 bits) indique le numéro de port du processus émetteur et l'adresse pour les réponses. Une valeur de 0 signifie qu'aucun port n'est attribué.

Le champ Destination Port identifie le processus destinataire. UDP utilise ce champ pour le démultiplexage des données. Si UDP reçoit un datagramme sans numéro de port valide, il génère un message d'erreur ICMP et rejette le datagramme.

Le champ Length contient la longueur totale du paquet UDP en octets (en-tête + données). La valeur minimale est 8, correspondant à un paquet sans données.

Le pseudo en-tête contient l'adresse source, l'adresse destination, le protocole (UDP = 17) et la longueur UDP. Ces informations préviennent les erreurs de routage.

### Protocole TCP

TCP garantit une transmission fiable des données grâce à un protocole orienté connexion et à flot d'octets. Cette fiabilité repose sur plusieurs mécanismes sophistiqués.

#### Mécanisme de fiabilité

TCP utilise le mécanisme PAR (Positive Acknowledgment with Retransmission) pour garantir des transmissions fiables. Un système PAR retransmet les données jusqu'à recevoir un accusé de réception confirmant leur arrivée correcte.

L'unité d'échange entre modules TCP coopérants s'appelle un segment. Chaque segment contient un total de contrôle permettant au destinataire de vérifier l'intégrité des données. Si le segment arrive en parfait état, le récepteur envoie un accusé de réception positif. Dans le cas contraire, il élimine le segment. Après un délai déterminé, le module TCP émetteur retransmet les segments non acquittés.

#### Établissement de connexion

TCP établit une connexion logique de bout en bout entre machines communicantes via un échange de contrôle appelé handshake (poignée de main). Ce processus utilise un mécanisme à trois étapes appelé "three-way handshake".

La machine A initie la connexion en envoyant à B un segment contenant le bit SYN et un numéro de séquence d'initialisation. Ce segment indique à B que A souhaite établir une connexion et précise le numéro de séquence initial pour la transmission.

La machine B répond par un segment contenant les bits ACK et SYN, accusant réception du segment de A et transmettant son propre numéro de séquence initial.

Enfin, A envoie un segment ACK confirmant la réception du segment de B. Une fois cet échange terminé, les données peuvent être transmises.

La fermeture de connexion utilise également un handshake impliquant des segments contenant le bit FIN (plus aucune donnée à transmettre).

#### Structure de l'en-tête TCP

L'en-tête TCP contient plusieurs champs essentiels :

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Data  |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

#### Transfert de données et numérotation

TCP traite les données comme un flot continu d'octets plutôt que comme des paquets indépendants. Il maintient l'ordre des octets transmis et reçus grâce aux champs Sequence Number et Acknowledgment Number.

Chaque système choisit son numéro de séquence initial (ISN). Les segments SYN échangés pendant la poignée de main synchronisent les systèmes de numérotation. Le champ Sequence Number du segment SYN contient l'ISN, généralement égal à 0.

Chaque octet de données reçoit un numéro séquentiel à partir de l'ISN, de sorte que le premier octet de données porte le numéro ISN + 1.

Le numéro de séquence dans l'en-tête identifie la position du premier octet de données du segment dans le flot. Par exemple, si l'ISN vaut 0 et que 4000 octets ont été transférés, le prochain segment commence au numéro de séquence 4001.

L'accusé de réception remplit deux fonctions : confirmation de réception et contrôle de flux. Le numéro d'accusé de réception correspond au numéro de séquence du prochain octet attendu. Si 2000 octets ont été reçus correctement à partir du numéro 1, l'accusé de réception vaut 2001.

#### Contrôle de flux

Les machines émettant et recevant des segments TCP ne travaillent pas toujours au même rythme. TCP implémente donc un mécanisme de contrôle de flux via le champ Window.

Ce champ indique le nombre d'octets que le récepteur peut encore accepter. Si le récepteur peut recevoir 6000 octets supplémentaires, le champ Window vaut 6000. Cela informe l'émetteur qu'il peut continuer l'envoi tant que le nombre total d'octets en transit reste inférieur à cette limite.

Le récepteur contrôle le flux en modifiant la taille de fenêtre. Une fenêtre nulle ordonne à l'émetteur d'interrompre la transmission jusqu'à recevoir une valeur non nulle.

Exemple de fonctionnement : l'émetteur commence avec l'ISN = 0, le récepteur a reçu 2000 octets (accusé de réception = 2001) et dispose d'un espace tampon pour 6000 octets supplémentaires. L'émetteur peut transmettre des segments tant que la fenêtre n'est pas saturée. Si aucun accusé de réception n'arrive et que la fenêtre se remplit, l'émetteur retransmet après un délai les données non acquittées.

#### Multiplexage et communication bidirectionnelle

TCP sert simultanément plusieurs processus sur la même machine par multiplexage. Ces processus partagent l'interface réseau et donc l'adresse IP, mais TCP leur associe des numéros de port distincts.

Une connexion s'établit entre le port émetteur et le port récepteur, définissant les extrémités (endpoints) de la connexion. Chaque extrémité se caractérise par une paire adresse IP/numéro de port.

TCP supporte la communication bidirectionnelle simultanée (full duplex), permettant la transmission de données dans les deux sens sur une même connexion.

Les numéros de port sont décrits périodiquement dans des RFC. Les numéros 0 à 1023 sont réservés aux services système standard.
