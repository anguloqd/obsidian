# 00 // tps

## Documents de TP

[00_tps_tp_ip1.pdf](ressources/00_tps_tp_ip1.pdf)

[00_tps_tp_ip2.pdf](ressources/00_tps_tp_ip2.pdf)

[00_tps_tp_ip3.pdf](ressources/00_tps_tp_ip3.pdf)

[00_tps_tp_routage1.pdf](ressources/00_tps_tp_routage1.pdf)

[00_tps_tp_routage2.pdf](ressources/00_tps_tp_routage2.pdf)

[00_tps_routage2_form.pdf](ressources/00_tps_routage2_form.pdf)

[00_tps_tp_firewall.pdf](ressources/00_tps_tp_firewall.pdf)

## TP1

- `ifconfig` pour trouver :
    - adresse Ethernet
    - adresse IP
- Câble droit et câble croisé :
    - Câble droit : connecte deux périph similaires
    - Câble croisé : connecte deux périph différents
- Pour changer d’adresse IP :
    - `ifconfig eth0 adresse_ip netmask 255.255.255.0 up`
- VLAN : sous-réseau d’un réseau local. Peut isoler les communications de deux machines qui appartiennent à deux VLAN différents
    - Pour se mettre à l’écoute de requêtes ICMP (comme `ping`, qui est un paquet unicast)
        - `tcpdump –e icmp`
    - Pour se mettre en écoute sur les paquets broadcast (adresse 255, puis port 8888)
        - `tcpdump –e port 8888`
    - Pour générer la requête en broadcast :
        - `echo "bonjour" | netcat –ub 192.168.55.255 8888`
    - Pour créer des domaines de broadcast : (dans la terminal du concentrateur switch)
        - `vlan/create 100`
        - `port/setvlan 1 100` pour affecter les ports des machines. Dans ce cas, affecte la machine connectée dans le port `1` dans la VLAN `100`
        - `vlan/print`

## TP2

- Noms de machines symboliques sans passer par les DNS :
    - Modifier `/etc/hosts/` avec un éditeur de texte. La syntaxe est :
     `<IP> <NOM1> <NOM2> … <NOM_FINAL>`
- Ping de taille paramétrable : `ping ip -s size`
    - MTU : limite de taille de paquets. Si un message ICMP atteint cette taille, il se fragmente.
    - Pour modifier MTU : `ifconfig eth0 mtu 1000`
- Commande traceroute : envoie des messages ICMP et permet de connaitre la route des datagrammes. Pour chaque router entre m1 et m2, la commande enverra un message ICMP de portée 1 (ie. durée de vie ou TTL, time to live), puis cette portée augmente de 1 jusqu’à que elle ne trouve plus de routers.
    - Définition formelle : “Comme la commande ping, la commande traceroute utilise également des messages ICMP ; elle permet de connaître la route exacte empruntée par les datagrammes. traceroute envoie 3 paquets UDP avec un TTL égal à 1 puis recommence en augmentant le TTL de 1 à chaque envoi. A chaque fois que le TTL arrive à 0, le routeur renvoie un message ICMP d’erreur.”
        
        ![untitled](ressources/00_tps_untitled.png)
        
        Les nuages sont des réseaux, les cercles avec des flèches sont des routers.
        
- ARP : address resolution protocol. C’est une table de correspondance adresse IP avec adresse MAC. `arp -n`.
    - La table montre la correspondance IP-MAC d’une machine si et seulement si :
        - On a fait `ping` à telle machine au moins une fois
        - La machine fait partie du réseau local (à travers un hub H1, et tel hub à une passerelle G1).
- Filtres de capture :
    - Sur m12 se mettre à l’écoute de messages UDP avec :
    `tcpdump -i any ‘udp and port 53’`. Attention, c’est `tcpdump`, pas `tcp` !
    - On peut le faire plus simplement avec Wireshark en écrivant comme filtre “`udp`”. On peut faire de même avec “`tcp`”.

## TP3

### DHCP

DHCP : protocole d’assignation d’adresse IP d’une machine dans un réseau local. Il est différent de l’affectation statique. On commence avec :

```bash
auto eth0 # demarrer l'interface eth0 automatiquement au démarrage du systeme
iface eth0 inet dhcp  # que l'interface eth0 maintenant affecte
											# des adresse ip à travers le protocole dhcp
```

Activer les interfaces réseau des m2 et m3 avec les commandes : `ifup eth0`. La réponse sur la console dira quelle adresse IP été afectée aux machines. Pour déactiver l’interface eth0, faire `ifdown eth0`.

La procédure donnera une adresse IP différente si l’adresse MAC de la carte réseau de la machine est différente. Si on change manuellement l’adresse MAC avec `ifconfig eth0 hw ether 02:03:04:05:06:07`, on aura un résultat différent.

Important. Le fait de affecter une IP dynamiquement est que la machine garde aussi l’adresse de la passerelle dans son tableau de routage. Si m2 fait `route -n` :

```bash
Destination   Gateway      Genmask        Flag   Metric   Ref   Use   Iface
192.168.2.0   0.0.0.0      255.255.255.0  U      1        0     0     eth0
0.0.0.0       192.168.2.2  0.0.0.0        UG     1        0     0     eth0
```

La première ligne est le routage du réseau local :

- Cette ligne indique que pour atteindre le réseau `192.168.2.0`, les paquets doivent être envoyés directement (pas de passerelle, donc `0.0.0.0`) via l’interface `eth0`.

La deuxième ligne est le routage extérieur :

- Cette ligne est la route par défaut. Elle indique que tous les paquets destinés à des réseaux pour lesquels il n’y a pas de route spécifique doivent être envoyés à la passerelle `192.168.2.2` via l’interface `eth0`.

### TCP et HTTP

![untitled](ressources/00_tps_untitled_1.png)

- Processus netcat qui permettra de recevoir la requête d’un client HTTP
lancé sur m2 (sans cependant y répondre):
    - `netcat ‐l ‐p 80` (`-l` : listen, `-p` : port)
- Simuler un dysfonctionnement du réseau :
    - En cliquant sur l’onglet “Anomalie” de Marionnet
    - Indiquer un taux de perte de 50 en entrée (inward) sur le port du hub H1 sur
    lequel est branché m1
- Initier une connexion HTTP depuis m2 vers m1 :
    - `lynx [http://192.168.2.254](http://192.168.2.254/)`