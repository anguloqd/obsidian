## 00 // tps

### Documents de TP

[00_tps_tp_ip1.pdf](ressources/00_tps_tp_ip1.pdf)

[00_tps_tp_ip2.pdf](ressources/00_tps_tp_ip2.pdf)

[00_tps_tp_ip3.pdf](ressources/00_tps_tp_ip3.pdf)

[00_tps_tp_routage1.pdf](ressources/00_tps_tp_routage1.pdf)

[00_tps_tp_routage2.pdf](ressources/00_tps_tp_routage2.pdf)

[00_tps_routage2_form.pdf](ressources/00_tps_routage2_form.pdf)

[00_tps_tp_firewall.pdf](ressources/00_tps_tp_firewall.pdf)

### TP1 - Introduction au protocole IP

#### Adresses et identificateurs réseau

- `ifconfig` pour trouver :
    - adresse Ethernet (MAC)
    - adresse IP
- Câble droit et câble croisé :
    - Câble droit : connecte deux périphériques similaires
    - Câble croisé : connecte deux périphériques différents
- Pour changer d'adresse IP :
    - `ifconfig eth0 adresse_ip netmask 255.255.255.0 up`

#### Adressage dans TCP/IP

- Chaque machine identifiée par une adresse IP (32 bits, notation décimale pointée) : `192.168.20.25`
- Chaque carte réseau dispose d'une adresse MAC (48 bits, notation hexadécimale) : `00:11:11:80:FB:3C`
- Protocole ARP fait la correspondance IP ↔ MAC
- DNS associe noms symboliques aux adresses IP : `miashs-www.u-ga.fr` ↔ `129.88.230.12`

#### Protocole ICMP et commande ping

- ICMP gère les erreurs au niveau IP
- `ping` utilise deux types de messages ICMP :
    - Type 8 : echo request (demande d'écho)
    - Type 0 : echo reply (réponse d'écho)
- Informations fournies : machine active/inactive, temps de propagation, pertes de paquets

#### VLAN : sous-réseaux virtuels

VLAN : sous-réseau d'un réseau local. Peut isoler les communications de deux machines qui appartiennent à deux VLAN différents

- Pour se mettre à l'écoute de requêtes ICMP (comme `ping`, qui est un paquet unicast)
    - `tcpdump –e icmp`
- Pour se mettre en écoute sur les paquets broadcast (adresse 255, puis port 8888)
    - `tcpdump –e port 8888`
- Pour générer la requête en broadcast :
    - `echo "bonjour" | netcat –ub 192.168.55.255 8888`
- Pour créer des domaines de broadcast : (dans la terminal du concentrateur switch)
    - `vlan/create 100`
    - `port/setvlan 1 100` pour affecter les ports des machines. Dans ce cas, affecte la machine connectée dans le port `1` dans la VLAN `100`
    - `vlan/print`

#### Capture de trames avec Wireshark

- Trois zones d'interface :
    - Liste des paquets capturés (synthèse)
    - Décodage détaillé du paquet sélectionné
    - Affichage hexadécimal et ASCII
- Filtres d'affichage pour analyser le trafic spécifique

### TP2 - Protocoles avancés

#### Résolution de noms sans DNS

Noms de machines symboliques sans passer par les DNS :

- Modifier `/etc/hosts/` avec un éditeur de texte. La syntaxe est :
    `<IP> <NOM1> <NOM2> … <NOM_FINAL>`

#### Fragmentation IP et MTU

Ping de taille paramétrable : `ping ip -s size`

- MTU : limite de taille de paquets. Si un message ICMP atteint cette taille, il se fragmente.
- Pour modifier MTU : `ifconfig eth0 mtu 1000`

#### Commande traceroute

Commande traceroute : envoie des messages ICMP et permet de connaitre la route des datagrammes. Pour chaque router entre m1 et m2, la commande enverra un message ICMP de portée 1 (ie. durée de vie ou TTL, time to live), puis cette portée augmente de 1 jusqu'à que elle ne trouve plus de routers.

Définition formelle : "Comme la commande ping, la commande traceroute utilise également des messages ICMP ; elle permet de connaître la route exacte empruntée par les datagrammes. traceroute envoie 3 paquets UDP avec un TTL égal à 1 puis recommence en augmentant le TTL de 1 à chaque envoi. A chaque fois que le TTL arrive à 0, le routeur renvoie un message ICMP d'erreur."

![untitled](ressources/00_tps_untitled.png)

Les nuages sont des réseaux, les cercles avec des flèches sont des routers.

#### Protocole ARP (Address Resolution Protocol)

ARP : address resolution protocol. C'est une table de correspondance adresse IP avec adresse MAC. `arp -n`.

La table montre la correspondance IP-MAC d'une machine si et seulement si :

- On a fait `ping` à telle machine au moins une fois
- La machine fait partie du réseau local (à travers un hub H1, et tel hub à une passerelle G1).

##### Fonctionnement d'ARP

1. Hôte A veut communiquer avec hôte B (connaît IP de B)
2. A envoie requête ARP en broadcast : "Qui a l'IP X ? Répondez à mon IP Y"
3. Toutes les machines reçoivent la requête
4. Seul B répond : "Je suis X, mon MAC est Z"
5. A met à jour sa table cache ARP
6. Les entrées expirent après temporisation

#### Protocoles de transport et applications

##### Notion de ports

- Ports 0-1023 : ports réservés (services standards)
    - SMTP : port 25
    - HTTP : port 80
    - DNS : port 53
    - SSH : port 22
- Ports > 1024 : ports utilisateurs
- Correspondance nom/numéro dans `/etc/services`

##### Analyse DNS (protocole UDP)

Filtres de capture :

- Sur m12 se mettre à l'écoute de messages UDP avec :
    `tcpdump -i any 'udp and port 53'`. Attention, c'est `tcpdump`, pas `tcp` !
- On peut le faire plus simplement avec Wireshark en écrivant comme filtre "ùdp". On peut faire de même avec "tcp".

### TP3 - DHCP et TCP

#### DHCP (Dynamic Host Configuration Protocol)

DHCP : protocole d'assignation d'adresse IP d'une machine dans un réseau local. Il est différent de l'affectation statique. On commence avec :

```bash
auto eth0 # demarrer l'interface eth0 automatiquement au démarrage du système
iface eth0 inet dhcp  # que l'interface eth0 maintenant affecte
                     # des adresse ip à travers le protocole dhcp
```

Activer les interfaces réseau des m2 et m3 avec les commandes : `ifup eth0`. La réponse sur la console dira quelle adresse IP été afectée aux machines. Pour désactiver l'interface eth0, faire `ifdown eth0`.

La procédure donnera une adresse IP différente si l'adresse MAC de la carte réseau de la machine est différente. Si on change manuellement l'adresse MAC avec `ifconfig eth0 hw ether 02:03:04:05:06:07`, on aura un résultat différent.

##### Effet sur le routage

Important. Le fait d'affecter une IP dynamiquement est que la machine garde aussi l'adresse de la passerelle dans son tableau de routage. Si m2 fait `route -n` :

```bash
Destination   Gateway      Genmask        Flag   Metric   Ref   Use   Iface
192.168.2.0   0.0.0.0      255.255.255.0  U      1        0     0     eth0
0.0.0.0       192.168.2.2  0.0.0.0        UG     1        0     0     eth0
```

La première ligne est le routage du réseau local :

- Cette ligne indique que pour atteindre le réseau `192.168.2.0`, les paquets doivent être envoyés directement (pas de passerelle, donc `0.0.0.0`) via l'interface `eth0`.

La deuxième ligne est le routage extérieur :

- Cette ligne est la route par défaut. Elle indique que tous les paquets destinés à des réseaux pour lesquels il n'y a pas de route spécifique doivent être envoyés à la passerelle `192.168.2.2` via l'interface `eth0`.

#### TCP et HTTP

![untitled](ressources/00_tps_untitled_1.png)

- Processus netcat qui permettra de recevoir la requête d'un client HTTP lancé sur m2 (sans cependant y répondre):
    - `netcat –l –p 80` (`-l` : listen, `-p` : port)
- Simuler un dysfonctionnement du réseau :
    - En cliquant sur l'onglet "Anomalie" de Marionnet
    - Indiquer un taux de perte de 50 en entrée (inward) sur le port du hub H1 sur lequel est branché m1
- Initier une connexion HTTP depuis m2 vers m1 :
    - `lynx http://192.168.2.254`

##### Analyse des sessions TCP

- Poignées de main : SYN, SYN-ACK, ACK (début)
- Fermeture : FIN-ACK, FIN-ACK, ACK
- Numéros de séquence relatifs dans Wireshark
- Flow Graph pour visualiser les échanges
- Mécanisme de retransmission en cas de perte

### TP Routage 1 - Configuration basique

#### Rappels sur le routage

- Deux machines sur le même segment communiquent directement (ARP)
- Pour atteindre un autre réseau : informations de routage (statiques/dynamiques)
- Chaque équipement possède une table de routage :
    - Adresse du réseau local
    - Adresses des réseaux distants autorisés
    - Entrée par défaut

##### Algorithme de routage

```
si (@IP_dest & masque == mon@IP & masque)
alors envoi_direct (datagramme, @IP_dest)
sinon
    envoi_indirect(datagramme, @IP_dest, routeur(@IP_dest & masque))
```

#### Commandes de routage

##### Configuration d'interfaces

```bash
# Afficher toutes les interfaces
ifconfig

# Configurer une interface
ifconfig eth0 192.168.10.1 netmask 255.255.255.0 up
```

##### Gestion des tables de routage

```bash
# Afficher la table de routage
route -n

# Ajouter une route vers un réseau
route add -net 192.168.100.0 netmask 255.255.255.0 gw 192.168.10.254

# Ajouter une route par défaut
route add default gw 192.168.10.2

# Supprimer une route
route del -net 192.168.10.0 netmask 255.255.255.0

# Supprimer la route par défaut
route del default
```

#### Étapes de configuration

##### Étape 1 : Configuration de base

- 4 hôtes (m1, m2, m3, m4) dans 4 réseaux :
    - N1 : 192.168.10.0
    - N2 : 192.168.110.0
    - N3 : 192.168.20.0
    - N4 : 192.168.120.0
- 2 routeurs R1 et R2
- Convention d'adressage : première IP pour hôte, dernière pour routeur

##### Étape 2 : Interconnexion des routeurs

- Réseau inter-routeurs : 192.168.200.0
- R1 : 192.168.200.1
- R2 : 192.168.200.2
- Configuration des tables pour communication complète

##### Étapes 3-4 : Extension et optimisation

- Ajout de 4 hôtes supplémentaires (m5-m8)
- Nouveaux réseaux N5-N8
- Routeurs R3 et R4
- Vérification avec `traceroute -n`

### TP Routage 2 - Routage avancé et sous-réseaux

#### Découpage en sous-réseaux

Objectif : découper le réseau 192.168.20.0 en trois sous-réseaux

##### Contraintes du découpage

- m1 (192.168.20.1) dans N1-1
- N1-1 : max 30 hôtes
- N1-2 : max 120 hôtes
- N1-3 : max 60 hôtes
- N2 : 172.20.0.0
- Utilisation possible du sous-réseau 0

##### Calcul des sous-réseaux

| Sous-réseau | Hôtes requis | Bits hôtes | Masque | Adresse réseau |
|-------------|--------------|------------|---------|----------------|
| N1-1 | 30 | 5 (/27) | 255.255.255.224 | 192.168.20.0/27 |
| N1-2 | 120 | 7 (/25) | 255.255.255.128 | 192.168.20.128/25 |
| N1-3 | 60 | 6 (/26) | 255.255.255.192 | 192.168.20.64/26 |
| N2 | - | - | 255.255.0.0 | 172.20.0.0/16 |

##### Plages d'adresses disponibles

| Sous-réseau | Adresse début | Adresse fin | Broadcast |
|-------------|---------------|-------------|-----------|
| N1-1 | 192.168.20.1 | 192.168.20.30 | 192.168.20.31 |
| N1-2 | 192.168.20.129 | 192.168.20.254 | 192.168.20.255 |
| N1-3 | 192.168.20.65 | 192.168.20.126 | 192.168.20.127 |
| N2 | 172.20.0.1 | 172.20.255.254 | 172.20.255.255 |

#### Configuration des tables de routage

##### Stations clientes

- Configuration minimale : réseaux directs + route par défaut
- Test de connectivité avec `ping`
- Optimisation des chemins avec `traceroute`

##### Routeurs

- Routes spécifiques vers chaque sous-réseau
- Possibilité d'utiliser une route par défaut
- Impact de la suppression de routes

#### Résolution de noms

Configuration du fichier `/etc/hosts` sur chaque machine :

```
192.168.20.1 m1
192.168.20.129 m2
# etc.
```

Test avec noms symboliques dans les commandes `ping` et affichage de `route` sans option `-n`.

### TP Firewall - Sécurité réseau

#### Concepts de base

##### IP Masquerading (camouflage IP)

- Les réseaux privés (RFC 1918) ne sont pas routables sur Internet :
    - 10.*.*.*
    - 172.16.*.*
    - 192.168.*.*
- Le masquerading réécrit les paquets pour qu'ils semblent provenir de la passerelle
- Réécrit ensuite les réponses pour la destination originale

##### iptables et netfilter

Programme `iptables` manipule les règles de filtrage du noyau Linux.

###### Tables et chaînes

**Table NAT (Network Address Translation) :**
- PREROUTING
- POSTROUTING

**Table FILTER (par défaut) :**
- INPUT : paquets destinés au firewall
- OUTPUT : paquets émis par le firewall
- FORWARD : paquets routés

###### Politiques de filtrage

- ACCEPT : paquets acceptés
- DROP : paquets refusés sans notification
- REJECT : paquets refusés avec notification

#### Commandes iptables essentielles

##### Gestion des chaînes

```bash
# Créer une chaîne utilisateur
iptables –N test

# Supprimer une chaîne vide
iptables –X test

# Changer la politique d'une chaîne
iptables -P FORWARD DROP

# Afficher les règles
iptables –L
iptables -nL  # format numérique

# Supprimer toutes les règles
iptables -F
```

##### Manipulation des règles

```bash
# Ajouter une règle
iptables –A INPUT –s 0/0 –j DENY

# Insérer une règle
iptables -I INPUT 1 -s 192.168.1.0/24 -j ACCEPT

# Supprimer une règle par position
iptables –D INPUT 1

# Supprimer une règle par critères
iptables –D INPUT –s 127.0.0.1 –p icmp –j DENY
```

##### Spécification des critères

**Adresses :**
- Nom complet : `prevert.upmf-grenoble.fr`
- Adresse IP : `195.221.42.159`
- Réseau : `195.221.42.0/24`
- Toute adresse : `0.0.0.0/0` ou `0/0`

**État des connexions :**
- ESTABLISHED : connexion établie
- NEW : nouvelle connexion
- INVALID : connexion inconnue
- RELATED : connexion liée

**Protocoles et ports :**

```bash
# Protocole
-p tcp/udp/icmp

# Ports
--sport 80          # port source
--dport 80          # port destination
--dport 1024:65535  # plage de ports
-m multiport --dport 137,139  # ports multiples

# Négation
! -p tcp
```

#### Configuration pratique

##### Étape 1 : Configuration de base

**Réseau privé :** 192.168.40.0/24
- m1 : 192.168.40.1 (client)
- proxy : 192.168.40.254 (firewall, 2 interfaces)

**Réseau public :** 195.83.80.0/24
- proxy : 195.83.80.254
- www : 195.83.80.10

**Sur le firewall :**

```bash
# Activer le routage
echo 1 > /proc/sys/net/ipv4/ip_forward

# Désactiver les redirections ICMP
echo 0 > /proc/sys/net/ipv4/conf/all/send_redirects
echo 0 > /proc/sys/net/ipv4/conf/eth0/send_redirects

# Activer le masquerading
iptables -A POSTROUTING -t nat -j MASQUERADE

# Autoriser le routage depuis le réseau privé
iptables -A FORWARD -s 192.168.40.0/24 -j ACCEPT
```

##### Étape 2 : Filtrage simple

Création d'une chaîne pour journalisation :

```bash
# Créer chaîne LOG_DROP
iptables –N LOG_DROP
iptables –A LOG_DROP –j LOG
iptables –A LOG_DROP –j DROP

# Bloquer ping sur loopback
iptables –A INPUT –p icmp –s 127.0.0.1 –j LOG_DROP

# Observer les logs
tail –f /var/log/messages
```

##### Étape 3 : Filtrage HTTP

Bloquer les connexions HTTP (port 80) :

```bash
iptables -A FORWARD -p tcp --sport 80 -m state --state ESTABLISHED -j LOG_DROP
iptables -A FORWARD -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j LOG_DROP
```

**Approche inverse - tout interdire sauf HTTP :**

```bash
# Politique restrictive
iptables -P FORWARD DROP

# Autoriser DNS (UDP et TCP)
iptables -A FORWARD -p udp -s 0/0 -d 192.168.40.0/24 --sport 53 -j ACCEPT
iptables -A FORWARD -p udp -s 192.168.40.0/24 -d 0/0 --dport 53 -j ACCEPT
iptables -A FORWARD -p tcp -s 0/0 -d 192.168.40.0/24 --sport 53 -j ACCEPT
iptables -A FORWARD -p tcp -s 192.168.40.0/24 -d 0/0 --dport 53 -j ACCEPT

# Autoriser HTTP
iptables -A FORWARD -p tcp -s 0/0 -d 192.168.40.0/24 --sport 80 -m state --state ESTABLISHED -j ACCEPT
iptables -A FORWARD -p tcp -s 192.168.40.0/24 -d 0/0 --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
```

**Extension pour SSH :**

```bash
# Autoriser SSH sortant
iptables -A FORWARD -p tcp -s 192.168.40.0/24 -d 0/0 --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A FORWARD -p tcp -s 0/0 -d 192.168.40.0/24 --sport 22 -m state --state ESTABLISHED -j ACCEPT
```

#### Tests et validation

- Vérification avec `ping`, `epiphany`, `nslookup`
- Test de connectivité : `ssh miashs-dc.u-ga.fr`
- Observation des logs dans `/var/log/messages`
- Vérification des règles : `iptables -L` et `iptables -t nat -L`
