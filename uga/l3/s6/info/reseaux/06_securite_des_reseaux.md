## 06 // sécurité des réseaux

[06_securite_des_reseaux_6_securite_des_reseaux.pdf](ressources/06_securite_des_reseaux_6_securite_des_reseaux.pdf)

[06_securite_des_reseaux_transparents_securite_reseaux.pdf](ressources/06_securite_des_reseaux_transparents_securite_reseaux.pdf)

## Sécurité des réseaux

### Introduction à la sécurité informatique

La sécurité informatique vise à assurer que les ressources matérielles ou logicielles d'une organisation sont uniquement utilisées dans le cadre prévu. Cette discipline englobe trois domaines fondamentaux qui forment le socle de toute stratégie de sécurisation.

#### Domaines de la sécurité

La **fiabilité de fonctionnement** constitue le premier pilier et s'exprime en termes de disponibilité. Elle garantit que les systèmes restent opérationnels et accessibles aux utilisateurs autorisés.

La **confidentialité de l'information** assure que seules les personnes autorisées ont accès aux ressources sensibles. Ce domaine nécessite des mécanismes de contrôle d'accès rigoureux.

L'**intégrité des données** protège contre toute modification non autorisée des informations. La confidentialité et l'intégrité font appel aux techniques de la cryptographie pour leur mise en œuvre.

#### Politique de sécurité

Une politique de sécurité représente l'ensemble des orientations suivies par une organisation en matière de protection. Son élaboration relève de la direction et doit adopter une approche globale intégrant plusieurs niveaux :

- Sensibilisation des utilisateurs aux problèmes de sécurité
- Sécurisation des applications
- Protection des données
- Sécurité des télécommunications
- Renforcement des infrastructures matérielles

La sécurité repose sur trois piliers interconnectés : la technologie, l'individu et les procédures. Cette approche holistique reconnaît que la sécurité ne peut être assurée par la seule technologie.

### Fiabilité et disponibilité

La fiabilité de fonctionnement s'appuie principalement sur la redondance à différents niveaux. Au niveau du câblage, une topologie en étoile présente une meilleure résistance aux pannes qu'une architecture en bus.

Pour les équipements, la mise en place de plusieurs alimentations électriques et l'utilisation d'éléments *hot swap* (remplaçables à chaud) garantissent la continuité de service même en cas de défaillance matérielle.

### Confidentialité des communications

#### Mesures préventives

La confidentialité des communications nécessite plusieurs mesures techniques. Le remplacement des concentrateurs (hubs) par des commutateurs (switches) limite la diffusion des trames à l'ensemble du réseau.

Le paramétrage des équipements réseau permet d'implémenter des alertes automatiques lors de changements d'état de liaison ou de détection de nouvelles adresses MAC Ethernet sur un port. La désactivation automatique des ports face à des stations inconnues renforce ce dispositif.

#### Solutions d'authentification

Les solutions d'authentification comme IEEE 802.1X contrôlent l'accès au réseau au niveau des ports des commutateurs. Cette norme définit un mécanisme d'authentification des utilisateurs avant l'obtention d'un accès réseau.

#### Chiffrement et VPN

L'utilisation du chiffrement, notamment par les réseaux privés virtuels (VPN), protège les données en transit. Un VPN crée un tunnel sécurisé entre deux réseaux physiques via une infrastructure non fiable comme Internet.

### Réseaux privés virtuels (VPN)

Un VPN combine les notions de virtualité et de confidentialité. Il est virtuel car il relie deux réseaux physiques par une liaison non fiable, et privé car seuls les ordinateurs autorisés peuvent accéder aux données transitant dans le tunnel.

Le fonctionnement repose sur un protocole d'encapsulation (*tunneling*) où les données sont chiffrées entre l'entrée et la sortie du VPN. IPSec constitue le protocole d'encapsulation standard pour les réseaux IP, assurant l'authentification, l'intégrité et la confidentialité des communications.

### Cryptographie et chiffrement

#### Terminologie et concepts

La cryptologie englobe la cryptographie (science du chiffrement) et la cryptanalyse (science du décryptage). Le processus transforme un texte en clair en cryptogramme par chiffrement, puis retrouve le texte original par déchiffrement avec la clé appropriée. Le décryptage désigne le processus inverse réalisé sans connaître la clé.

#### Fonctions de la cryptographie

La cryptographie remplit quatre fonctions essentielles :

L'**authentification** vérifie l'identité revendiquée par une entité, garantissant que chaque correspondant est bien celui qu'il prétend être.

L'**intégrité** détecte toute altération des données durant la communication, qu'elle soit fortuite ou intentionnelle.

La **confidentialité** rend l'information inintelligible aux personnes non autorisées.

La **non-répudiation** prouve la participation d'une entité dans un échange de données, empêchant tout déni ultérieur.

#### Méthodes d'authentification

L'authentification s'appuie sur plusieurs classes de méthodes. La catégorie "je connais" utilise des éléments comme les mots de passe, nécessitant une identification préalable (login). La classe "je possède" exploite des objets physiques comme les cartes magnétiques. L'approche "je suis" recourt à la biométrie (empreintes digitales). Enfin, "je sais faire" comprend des compétences comme la signature manuscrite.

#### Intégrité par fonctions de hachage

Les fonctions de hachage convertissent une chaîne de longueur quelconque en une empreinte de taille fixe. Elles présentent des propriétés cryptographiques importantes : facilité de calcul dans un sens, difficulté d'inversion, et résistance aux collisions.

MD5 génère des empreintes de 128 bits, tandis que SHA-1 produit des condensats de 160 bits. Ces algorithmes détectent toute modification, même minime, du message original.

### Types de cryptosystèmes

#### Cryptosystèmes à usage restreint

Ces systèmes basent leur sécurité sur la confidentialité des algorithmes de chiffrement. Cette approche devient inutilisable avec de nombreux utilisateurs car elle ne peut garantir la confidentialité des méthodes.

#### Cryptosystèmes à usage général

Ces systèmes utilisent des algorithmes potentiellement publics mais s'appuient sur des clés secrètes pour assurer la sécurité. Le grand nombre de clés possibles rend la recherche exhaustive impraticable.

### Chiffrement symétrique

#### Principe de base

Le chiffrement symétrique utilise une même clé secrète pour chiffrer et déchiffrer les messages. Pour une sécurité optimale, la longueur de la clé doit égaler celle du message à protéger.

Cette approche présente des défis logistiques : elle nécessite un canal sûr pour transmettre la clé, et avec N utilisateurs, le système requiert N² clés secrètes pour que chaque paire puisse communiquer.

#### Exemple de fonctionnement

L'opération XOR illustre le principe du chiffrement symétrique. Alice et Bernard conviennent d'une clé secrète ("CHAMPIGNON"). Alice applique cette clé à son message ("JE VOUS AIME") par opération XOR bit à bit. Bernard utilise la même clé pour retrouver le message original.

#### Problème de l'échange des clés

Le paradoxe fondamental du chiffrement symétrique réside dans la nécessité de partager un secret pour communiquer secrètement. Cette contrainte devient critique lorsque les clés doivent être changées fréquemment ou que le nombre de participants augmente.

L'exemple du facteur illustre ce problème : comment Bernard peut-il envoyer un colis secret à Alice si leur facteur Charlie intercepte toute correspondance non sécurisée ? La solution implique un échange préalable de secrets par additions/soustractions successives.

### Chiffrement asymétrique

#### Fondements mathématiques

La cryptographie asymétrique exploite des fonctions mathématiques agissant comme des cadenas : faciles à utiliser dans un sens, très difficiles à inverser sans connaître un paramètre secret.

La factorisation des nombres premiers illustre ce principe. Multiplier deux nombres premiers (13×17 = 221) reste simple, mais retrouver les facteurs premiers d'un grand nombre (7 321 010 267 = 55 487×131 941) devient computationnellement très difficile.

#### Principe de fonctionnement

Le chiffrement asymétrique utilise une paire de clés : une clé publique pour chiffrer et une clé privée pour déchiffrer. Le message chiffré avec la clé publique du destinataire ne peut être déchiffré qu'avec sa clé privée correspondante.

Cette approche résout le problème de distribution des clés : la clé publique peut être transmise sans protection sur le réseau, tandis que seul le destinataire possède et connaît la clé privée. Il est computationnellement impossible de calculer la clé privée à partir de la clé publique.

#### Algorithme RSA

L'algorithme RSA, développé par Rivest, Shamir et Adleman en 1977, constitue le premier protocole de cryptographie à clé publique pratique. Il s'appuie sur la difficulté de factoriser de grands nombres.

Le processus génère deux grands nombres premiers p et q, calcule leur produit n = pq, choisit un exposant e premier avec (p-1)(q-1), puis détermine l'exposant de déchiffrement d tel que ed ≡ 1 mod((p-1)(q-1)).

Le chiffrement d'un bloc B s'effectue par B^e mod n, tandis que le déchiffrement utilise C^d mod n.

#### Défi RSA

En 1977, les inventeurs de RSA proposèrent un défi de factorisation avec une récompense de 100 dollars. Il fallut 17 ans et une équipe de 600 personnes pour factoriser le nombre de 129 chiffres proposé, démontrant la robustesse de l'algorithme pour des clés suffisamment longues.

### Gestion des clés publiques

#### Problématique de distribution

L'échange de clés publiques entre entités inconnues pose des défis pratiques. La diffusion sur des sites web reste vulnérable à la falsification, tandis que l'utilisation de centres de distribution soulève des questions de disponibilité et de surcharge.

#### Infrastructure de certification

La solution adoptée repose sur des autorités de certification (CA) qui certifient l'appartenance des clés à leurs légitimes propriétaires. Ces organismes tiers de confiance créent des certificats équivalents à des cartes d'identité numériques.

#### Certificats X.509

Les certificats suivent la norme X.509 standardisée par l'UIT. Ils établissent un lien entre une clé publique et son détenteur. La signature numérique de l'autorité de certification, appliquée au condensat des informations du certificat, garantit l'authenticité.

Les navigateurs web intègrent une liste prédéfinie d'autorités de certification reconnues (Thawte, VeriSign, GlobalSign). Les certificats n'étant ni secrets ni protégés, ils peuvent circuler librement.

### Cryptographie mixte et clés de session

#### Optimisation des performances

La cryptographie mixte combine les avantages du chiffrement symétrique (rapidité) et asymétrique (facilité de distribution des clés). Les algorithmes asymétriques, bien que sûrs, restent généralement lents pour le chiffrement de gros volumes de données.

#### Mécanisme de fonctionnement

Une clé de session symétrique de taille raisonnable est générée aléatoirement puis chiffrée avec la clé publique du destinataire. Celui-ci déchiffre la clé de session avec sa clé privée. Les deux parties possèdent alors la même clé symétrique pour chiffrer et déchiffrer les messages de la session.

À la fin de la session, la clé symétrique est détruite, assurant la confidentialité persistante même en cas de compromission ultérieure des clés.

### Signature numérique

#### Principe et objectifs

La signature numérique prouve qu'une transaction a eu lieu et garantit la non-répudiation. Elle inverse l'usage des clés asymétriques : le chiffrement s'effectue avec la clé privée, permettant la vérification par tous avec la clé publique correspondante.

#### Processus de signature

Le processus combine le calcul d'un condensat du message (pour l'intégrité) et son chiffrement avec la clé privée (pour l'authentification). Le destinataire déchiffre la signature avec la clé publique de l'émetteur et compare le condensat obtenu avec celui qu'il calcule du message reçu.

### Tailles et sécurité des clés

#### Clés symétriques

La sûreté d'une clé secrète dépend exponentiellement de sa longueur. Chaque bit supplémentaire double le nombre de combinaisons possibles. Une clé de 56 bits offre 2^56 possibilités, mais l'augmentation de la puissance de calcul rend cette taille insuffisante.

Les recommandations actuelles préconisent des clés de 256 bits pour AES. La France limitait les clés à 40 bits jusqu'en 1998, année où les clés de 56 bits furent cassées.

#### Clés asymétriques

Les clés asymétriques nécessitent des tailles plus importantes car leur sécurité repose sur la difficulté de factorisation. La recherche des facteurs premiers d'un grand nombre devient impraticable dans un temps raisonnable avec des clés suffisamment longues.

Les recommandations actuelles préconisent des clés de 3072 bits pour RSA, reflétant l'évolution des capacités de calcul et des techniques de factorisation.

### Protocoles de sécurisation

#### SSH (Secure Shell)

SSH définit à la fois un protocole et un ensemble de programmes pour des sessions interactives et des transferts de fichiers sécurisés. Il remplace les utilitaires classiques non chiffrés comme rlogin, rcp, rsh et telnet.

Le protocole propose deux modes d'authentification : l'authentification traditionnelle par mot de passe (protégé par le chiffrement du canal) et l'authentification forte basée sur la cryptographie asymétrique avec des paires de clés publique/privée.

#### SSL/TLS (Socket Secure Layer/Transport Layer Security)

SSL, initialement développé par Netscape puis standardisé par l'IETF sous le nom TLS, sécurise les communications réseau. Il offre la confidentialité des données et l'authentification des interlocuteurs via des certificats électroniques.

Ce protocole sécurise les services web (HTTPS) et les protocoles de messagerie (POPS, IMAPS), transformant des communications en clair en échanges chiffrés.

#### Systèmes OTP (One Time Password)

Les mots de passe uniques génèrent un nouveau mot de passe à chaque connexion, rendant inutile leur capture sur le réseau. Le système s'initialise avec un mot de passe secret sur le serveur, puis utilise un challenge pour calculer l'OTP sans utiliser le réseau.

### Pare-feu et filtrage

#### Rôles et objectifs

Un pare-feu (firewall) contrôle et restreint l'accès au réseau en un point précis. Il centralise les décisions de sécurité, renforce la protection des services, détermine les règles d'accès, isole des portions du réseau et enregistre l'activité.

Cependant, il ne peut protéger contre les connexions qui le contournent, les menaces totalement nouvelles, les virus applicatifs, ou les utilisateurs internes malveillants.

#### Classifications

Les pare-feu se déclinent en plateformes logicielles (implémentées sur des ordinateurs standards avec des logiciels spécialisés comme Netfilter) et en équipements matériels dédiés (boîtiers spécialisés ou routeurs avec des listes de contrôle d'accès).

#### Filtrage IP

Le filtrage examine les en-têtes des paquets IP pour prendre des décisions. Chaque paquet peut être accepté (ACCEPT), rejeté silencieusement (DROP), ou rejeté avec notification (REJECT).

Deux politiques s'opposent : "ce qui n'est pas interdit est autorisé" versus "ce qui n'est pas autorisé est interdit". La politique restrictive offre une meilleure sécurité.

#### Filtrage stateless et stateful

Le filtrage stateless examine chaque paquet indépendamment selon des critères statiques (adresses, ports, protocoles). Le filtrage stateful maintient un état des connexions et adapte son comportement selon le contexte (ESTABLISHED, NEW, INVALID, RELATED).

#### Pare-feu nouvelle génération

Les Next Generation Firewalls (NGFW) intègrent l'identification des applications et des utilisateurs. Ils reconnaissent plus de 800 protocoles et des milliers d'applications web, permettant des politiques granulaires comme "autoriser le web mais interdire Facebook".

### Architectures de pare-feu

#### Routeur écran

L'architecture la plus simple place un routeur filtrant entre le réseau interne et Internet. Il route ou bloque les paquets selon la politique de sécurité définie.

#### Translation d'adresses (NAT)

Le NAT permet aux réseaux privés (RFC 1918 : 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) de communiquer avec Internet. La passerelle réécrit les paquets pour masquer les adresses internes, agissant comme un proxy au niveau IP.

#### Pare-feu à proxy

Cette architecture utilise des serveurs mandataires qui traitent les requêtes des clients internes vers les serveurs externes. Elle offre un contrôle fin des applications mais peut introduire des latences.

#### Zone démilitarisée (DMZ)

La DMZ place les serveurs publics (web, mail, DNS) dans un segment réseau distinct, protégé par deux pare-feu. Cette architecture isole les services publics du réseau interne tout en maintenant leur accessibilité depuis Internet.

#### Architectures hiérarchiques

Les organisations complexes peuvent déployer plusieurs niveaux de pare-feu, créant des périmètres de sécurité emboîtés pour différents niveaux de sensibilité.

### Sécurité des réseaux sans fil

#### Principes de gestion

La sécurisation des réseaux sans fil (WLAN) nécessite une gestion par des équipes formées, des audits réguliers, une surveillance du trafic et la recherche de réseaux sauvages non autorisés.

Les bornes sans fil doivent être traitées comme des équipements sensibles : protection de l'accès physique, intégration dans la politique de sécurité, sensibilisation des utilisateurs.

#### Configuration sécurisée

L'administration des bornes doit s'effectuer uniquement par l'interface filaire, avec désactivation de tous les services d'administration sur l'interface sans fil (web, SNMP, TFTP).

La modification des paramètres par défaut (SSID, clés, communautés SNMP) et l'utilisation de mots de passe robustes renforcent la sécurité de base.

#### Filtrage MAC et limitations

Le filtrage par adresse MAC autorise uniquement les cartes réseau enregistrées. Cependant, cette protection présente des faiblesses : gestion administrative lourde, visibilité des adresses MAC dans toutes les trames, et possibilité d'usurpation par écoute du trafic.

### Protocoles de chiffrement Wi-Fi

#### WEP (Wired Equivalent Privacy)

WEP, introduit en 1999 avec la norme 802.11, utilise des clés partagées de 64 ou 128 bits avec l'algorithme RC4. Ce protocole présente des faiblesses majeures : problèmes d'initialisation, absence de gestion des clés, et vulnérabilité aux attaques de cryptanalyse.

#### WPA (Wi-Fi Protected Access)

WPA améliore WEP en introduisant le protocole TKIP (Temporal Key Integrity Protocol). Bien que toujours basé sur RC4, TKIP modifie dynamiquement les clés de chiffrement (tous les 10 Ko), corriger les défauts de WEP. Cependant, l'attaque d'Erik Tews et Martin Beck en 2008 a compromis la sécurité de TKIP.

#### WPA2

WPA2 adopte l'algorithme AES (Advanced Encryption Standard), résultat d'un concours du NIST lancé en 1997. Il remplace TKIP par CCMP (Counter Mode with Cipher Block Chaining Message Authentication Code Protocol), offrant une sécurité significativement renforcée.

WPA2 fonctionne selon deux modes : Enterprise (avec serveur d'authentification RADIUS selon 802.1X) pour les grandes organisations, et Personal (PSK - Pre-Shared Key) pour les PME/PMI.

La découverte de la faille KRACK en 2017 a révélé des vulnérabilités dans WPA2, contraignant la Wi-Fi Alliance à développer WPA3.

#### Architecture réseau sans fil

Les bornes 802.11 doivent être considérées comme des équipements sensibles avec firmware mis à jour régulièrement. Le placement géographique et le réglage de puissance minimisent la propagation des ondes hors périmètre.

Les flux sans fil doivent être traités comme du trafic externe, nécessitant un filtrage au niveau de passerelles dédiées et une authentification des utilisateurs.

### Attaques et vulnérabilités

#### Cadre légal

Le Code pénal français sanctionne les atteintes aux Systèmes de Traitement Automatisé de Données (STAD). L'article 323-1 condamne l'accès frauduleux (3 ans de prison, 100 000 € d'amende), l'article 323-2 l'entrave au fonctionnement (5 ans, 150 000 €), et l'article 323-3 la modification de données (5 ans, 150 000 €).

#### Types de risques

Les risques se classent en trois catégories : accidentels (incendie, panne, erreur humaine), erreurs (saisie, exploitation, conception), et malveillance (fraude, sabotage, espionnage industriel).

Les attaques visent le vol d'informations (écoute passive, ingénierie sociale), l'intrusion (prise de contrôle partielle ou totale), et le déni de service (saturation des ressources).

#### Dénis de service (DoS)

Les attaques par déni de service rendent indisponibles les services ou machines ciblés. Elles exploitent soit les vulnérabilités applicatives (débordement de buffer), soit les faiblesses protocolaires ou d'implémentation.

#### Méthodologie d'attaque

Une attaque type suit plusieurs phases : recherche d'informations (topologie, services), identification des vulnérabilités, exploitation, installation de portes dérobées et systèmes d'écoute, suppression des traces, puis éventuellement déni de service.

### Techniques de reconnaissance

#### Collecte d'informations

La reconnaissance utilise des sources publiques (DNS, whois, moteurs de recherche) et des outils de découverte (traceroute, ping, hping) pour cartographier la topologie et identifier les systèmes.

La prise d'empreinte (fingerprinting) avec des outils comme nmap révèle les systèmes d'exploitation et versions logicielles. Le scan de ports détecte les services ouverts sur les machines cibles.

#### Techniques de scan de ports

Le scan TCP SYN (Half Open) envoie uniquement un segment SYN et analyse la réponse pour déduire l'état du port. Rapide mais potentiellement détectable par les systèmes de surveillance.

Le scan TCP Connect établit des connexions complètes, ressemblant à des accès légitimes mais consommant plus de ressources.

Les scans furtifs (FIN, XMAS, Null) exploitent des comportements protocolaires spécifiques pour déjouer certains systèmes de filtrage.

Le scan ACK détecte la présence de pare-feu sans déterminer l'état des ports.

Le scan UDP présente des défis d'interprétation dus au caractère sans connexion du protocole.

### Attaques sur réseaux locaux

#### Écoute réseau (sniffing)

L'écoute nécessite un accès physique au réseau et exploite la nature broadcast des réseaux partagés. Les commutateurs modernes limitent cette technique en créant des domaines de collision séparés.

#### Techniques de redirection

L'usurpation d'adresses (spoofing) falsifie les identifiants réseau. L'ARP poisoning corrompt les caches ARP pour rediriger le trafic vers la machine de l'attaquant, même sur des réseaux commutés.

L'IP spoofing falsifie l'adresse source des paquets, empêchant la réception des réponses mais permettant des attaques asymétriques.

#### Attaques par inondation

Le SYN flooding sature les ressources de connexion en envoyant massivement des demandes de connexion avec des adresses sources aléatoires. La machine cible maintient des connexions semi-ouvertes jusqu'à épuisement des ressources.

L'UDP flooding génère des tempêtes de paquets UDP pour saturer la bande passante et les ressources des hôtes. L'attaque Chargen exploit illustre cette technique en faisant communiquer les services chargen et echo.

#### Attaques sans fil spécialisées

Le wardriving détecte et localise les réseaux sans fil dont les ondes se propagent hors périmètre. Cette technique permet l'utilisation non autorisée de connexions ou l'interception de communications.

Les attaques KRACK exploitent des faiblesses dans le processus de renégociation des clés WPA2, permettant à un attaquant de se faire passer pour un point d'accès légitime et de forcer l'utilisation d'une clé connue.

#### Attaques distribuées

Les attaques distribuées utilisent des réseaux de machines compromises (botnets) pour amplifier leur impact. Ces agents reçoivent des ordres d'un contrôleur central et lancent simultanément des attaques coordonnées contre les cibles désignées.

Cette approche démultiplie la puissance d'attaque et complique la traçabilité, rendant les défenses traditionnelles moins efficaces face à ces menaces distribuées.
