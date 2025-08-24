## 01 // intro aux réseaux

[01_intro_aux_reseaux_1_introduction_aux_reseaux.pdf](ressources/01_intro_aux_reseaux_1_introduction_aux_reseaux.pdf)

## Introduction aux réseaux

### Histoire et évolution des réseaux informatiques

Les premiers essais de transmission de données entre ordinateurs remontent aux années 1960. À la fin des années 1970, les premiers réseaux de terminaux et d'ordinateurs voient le jour, révolutionnant la façon dont les systèmes informatiques interagissent.

Ces réseaux permettent de partager des ressources coûteuses (programmes, équipements), d'échanger des données, d'améliorer la fiabilité grâce à la tolérance aux pannes, et de créer des systèmes distribués complexes.

### Concepts fondamentaux

#### Définitions et terminologie

La **téléinformatique** combine le traitement de l'information (domaine informatique) avec le transport de l'information (télécommunications). Un système téléinformatique désigne un ensemble d'équipements informatiques reliés par des voies de communication.

Le terme **réseau** désigne l'organisation des connexions entre les différents nœuds d'un système téléinformatique. Ces nœuds se divisent en deux catégories :

- Les ordinateurs au sens large
- Les équipements spécialisés dans les fonctions réseau

La **topologie du réseau** décrit la localisation des nœuds et l'agencement des liaisons entre eux. La connexion physique nécessite une carte réseau (NIC - Network Interface Card) ou coupleur.

#### Architectures réseau

Deux architectures principales coexistent :

**Architecture client-serveur** : Une machine (serveur) assume un rôle particulier dans la gestion des communications. Plusieurs serveurs peuvent coexister, chacun dédié à des applications spécifiques.

**Architecture sans serveur** : Toutes les stations possèdent le même rôle et communiquent directement entre elles. Cette approche reste limitée aux petits réseaux (moins d'une douzaine de postes) car la gestion devient complexe au-delà.

#### Débits de transmission

Les débits s'expriment en bits par seconde (bps) avec leurs multiples :

- Kilobit par seconde (Kbit/s)
- Mégabit par seconde (Mbit/s)
- Gigabit par seconde (Gb/s)
- Térabit par seconde (Tb/s)

Les réseaux locaux atteignent couramment 100 Mb/s à 1 Gb/s, tandis que les épines dorsales (backbones) peuvent atteindre 10 Gb/s.

**Note importante** : 1 Ko = 1024 × 8 bits = 8192 bits ≈ 8 Kb

### Transmission de l'information

#### Caractéristiques de transmission

La transmission entre deux entités se caractérise par plusieurs paramètres :

**Sens des échanges** :
- Unidirectionnel
- Bidirectionnel à l'alternat ou simultané

**Mode de transmission** :
- En série
- En parallèle

**Synchronisation** :
- Mode synchrone
- Mode asynchrone

Pour assurer le bon fonctionnement, un codage des signaux et des protocoles communs doivent être établis.

#### Supports physiques

Trois grandes catégories de supports existent :

**Supports filaires** : Circulation d'une grandeur électrique sur un câble métallique.

**Supports aériens** : Propagation d'ondes électromagnétiques ou radioélectriques dans l'air ou le vide (fréquences inférieures à 3000 GHz).

**Supports optiques** : Acheminement d'informations sous forme lumineuse.

#### Codage des signaux

La transmission en bande de base constitue la méthode la plus simple : un courant nul ou négatif représente un 0, un courant positif un 1. Ce signal carré présente l'avantage de la simplicité d'implémentation mais souffre d'une dégradation rapide avec la distance.

#### Sens de transmission

Trois modes de transmission existent :

**Mode simplex** : Transmission unidirectionnelle de l'émetteur vers le récepteur (radio, télévision).

**Mode semi-duplex (half duplex)** : Transmission bidirectionnelle alternée, jamais simultanée.

**Mode duplex (full duplex)** : Transmission bidirectionnelle simultanée.

#### Modes d'acheminement

##### Mode avec connexion

Le mode connecté exige une autorisation préalable avant tout échange. Il comprend trois phases :

1. Négociation et établissement de liaison
2. Transfert des données via un circuit virtuel
3. Libération de la connexion

**Avantages** : Sécurisation du transport, contrôle de l'activité réseau, négociation de la qualité de service (QoS).

**Inconvénients** : Lourdeur de mise en œuvre, difficulté pour les applications multipoints (nécessité d'ouvrir autant de connexions que de destinataires).

##### Mode sans connexion

Les données sont émises sans vérification préalable de la présence du destinataire. Chaque message contient les adresses d'émetteur et de destinataire, permettant un transport indépendant. Les messages peuvent arriver dans le désordre. Ce mode convient mieux aux messages courts.

### Classification des réseaux

#### Réseaux filaires

##### Réseaux locaux (LAN)

Les **Local Area Networks** connectent les ordinateurs d'un bâtiment ou d'un site. Propriété privée de l'organisation utilisatrice, ils offrent des débits de 100 Mb/s à 1 Gb/s. Ethernet (IEEE 802.3) domine ce marché, avec Token-Ring (IEEE 802.5) comme alternative.

##### Réseaux métropolitains (MAN)

Les **Metropolitan Area Networks** couvrent l'étendue d'une grande ville ou d'une région (environ 100 km). Ils interconnectent plusieurs LAN et utilisent les technologies FDDI et ATM, se situant entre secteurs privé et public.

##### Réseaux étendus (WAN)

Les **Wide Area Networks** s'étendent à l'échelle régionale, nationale ou planétaire. Terrestres (fibre optique) ou hertziens (satellite), ils sont systématiquement loués à des opérateurs spécialisés.

#### Réseaux sans fil

##### Réseaux personnels (WPAN)

Les **Wireless Personal Area Networks** offrent une portée d'une dizaine de mètres :

**Bluetooth (802.15.1)** : Faible consommation, 1 Mb/s, portée de 30 mètres, intégré dans de nombreux équipements.

**ZigBee (802.15.4)** : Alternative spécialisée pour les objets connectés.

##### Réseaux locaux sans fil (WLAN)

Les **Wireless Local Area Networks** couvrent plusieurs centaines de mètres avec des débits de plusieurs dizaines de Mb/s. Le standard dominant 802.11b (Wi-Fi) de l'IEEE offre :

- Mobilité des utilisateurs
- Simplicité d'installation
- Topologie flexible
- Coûts réduits
- Interconnectivité avec l'existant
- Fiabilité éprouvée

##### Réseaux métropolitains sans fil (WMAN)

Les **Wireless Metropolitan Area Networks** basés sur IEEE 802.16 (WiMax) couvrent quelques kilomètres avec des débits jusqu'à 1 Gb/s en fixe et 100 Mb/s en mobile (802.16m).

##### Réseaux étendus sans fil (WWAN)

Les **Wireless Wide Area Networks** s'étendent sur plusieurs centaines de kilomètres via un ensemble de cellules. Les technologies GSM, GPRS, 3G, 4G et 5G constituent les exemples les plus répandus.

### Normalisation

#### Organismes de normalisation

Les organismes établissent les cadres de développement technologique et garantissent la complétude des spécifications. On distingue les **normes** (établies par des organismes officiels) des **standards de fait** (définis par des entités non reconnues).

**ISO (International Standardization Organization)** : Organisation non gouvernementale regroupant les organismes nationaux (AFNOR en France).

**UIT-T (Union Internationale des Télécommunications)** : Organisation intergouvernementale responsable des télécommunications sur câbles.

**IEEE (Institute of Electrical and Electronics Engineers)** : Société internationale très active dans le domaine des réseaux locaux.

#### Modèle OSI

Le modèle **Open System Interconnection** (ISO 7498-1983) résulte de la stratification des systèmes de communication et de la volonté de normalisation face aux constructeurs indépendants.

Ses objectifs :

- Permettre la modification modulaire de l'infrastructure
- Autoriser l'approvisionnement multi-fournisseurs

Le modèle se divise en 7 couches, les quatre inférieures concernant le réseau proprement dit, les supérieures étant orientées utilisateur et applications.

##### Couche physique (1)

Spécifie les caractéristiques physiques de transmission : codage, détection de signal, synchronisation, paramètres électriques, optiques et mécaniques des liaisons.

##### Couche liaison de données (2)

Organise les données en trames avec en-tête et délimiteur. Gère les problèmes de trames endommagées, perdues ou dupliquées via les contrôles de redondance cyclique (CRC).

##### Couche réseau (3)

Achemine les données du système source au destinataire quelle que soit la topologie. Utilise soit les circuits virtuels (mode connecté) soit les datagrammes (mode sans connexion). Assure le routage et la traduction entre adresses physiques et logiques.

##### Couche transport (4)

Garantit la fiabilité du transfert de bout en bout, indépendamment des couches inférieures. Assure la qualité de service selon les possibilités des couches basses, en mode connecté ou non connecté.

##### Couche session (5)

Première couche établissant une communication formelle avec l'homologue distant. Peu utilisée dans les systèmes courants, notamment Internet.

##### Couche présentation (6)

Gère la représentation des données, la compression et le chiffrement. Le chiffrement peut s'effectuer aux niveaux physique, transport ou présentation avec des compromis sécurité/performance.

##### Couche application (7)

Interface utilisateur pour les fonctions de communication : transfert de fichiers (FTP), messagerie électronique, émulation de terminal virtuel.

#### Modèle TCP/IP

Développé par le département de la défense américain (DoD) dans le projet DARPA, ce modèle se concentre sur quatre couches principales, simplifiant l'architecture OSI tout en conservant l'essentiel des fonctionnalités.

#### Normes IEEE 802

L'IEEE et l'ECMA ont standardisé les réseaux locaux pour assurer la compatibilité inter-constructeurs. Le comité 802 (créé en 1980) a produit :

- 802.3 pour Ethernet
- 802.4 pour MAP
- 802.5 pour Token-Ring

Ces spécifications couvrent les couches 1 et 2 du modèle OSI.

### Topologies réseau

#### Topologie en étoile

Un élément central (hub ou concentrateur) relie N-1 chemins pour N équipements. Topologie dissymétrique mais offrant une bonne centralisation de la gestion, malgré un coût de câblage élevé.

#### Topologie en anneau

Les éléments se connectent sur un chemin bouclé avec circulation ordonnée des informations. L'ordre de circulation implique un accès séquentiel aux différents nœuds.

#### Topologie en bus

Tous les accès se connectent en parallèle sur un média unique partagé. L'absence d'ordre dans les éléments limite le débit global à la bande passante du média.

#### Topologie en chaîne

Un chemin relie successivement tous les accès avec séquencement implicite. Contrairement à l'anneau, la chaîne possède deux extrémités distinctes.

#### Topologie en arbre

Structure hiérarchique avec branches et subdivisions depuis une racine unique, sans création de boucles. Topologie riche permettant des niveaux hiérarchiques élaborés.

#### Topologie maillée

Liaisons point-à-point entre tous les éléments par paires. Topologie la plus coûteuse (N(N-1)/2 liens) mais offrant une redondance maximale.

| Topologie | Symétrie | Ordre | Directionnel | Brins | Confidentialité |
|-----------|----------|-------|--------------|-------|-----------------|
| Étoile | Non | Non | Non | N-1 | Oui |
| Anneau | Oui | Oui | À priori | N | Non |
| Bus | Oui | Non | Non | 1 | Non |
| Chaîne | Non | Oui | Non | N-1 | Non |
| Arbre | Non | Non | Non | N-1 | Possible |
| Maillage | Oui | Non | Non | N(N-1)/2 | Oui |

La distinction entre topologie physique (câblage) et topologie logique (circulation des données) reste essentielle pour la compréhension des architectures réseau.

### Composants physiques des réseaux

#### Éléments constitutifs

Un réseau comprend :

- **Support physique** : Acheminement des signaux
- **Prises (tap)** : Connexion au support
- **Adaptateurs (transceiver)** : Traitement des signaux
- **Coupleurs (NIC)** : Cartes réseau gérant les communications
- **Équipements spécialisés** : Répéteurs, hubs, switchs

#### Médias de transmission

##### Câbles métalliques

**Câble coaxial** : Âme en cuivre pour transmission, gaine conductrice pour retour, séparées par un isolant. Bonnes performances débit/distance et immunité electromagnétique, mais coût élevé et installation délicate.

**Paire torsadée** : Conducteurs groupés par paires et vrillés pour réduire les perturbations, l'atténuation et la paradiaphonie. Simple et économique, performances limitées en distance malgré les progrès technologiques permettant 100 Mb/s à 1 Gb/s.

Types de paires torsadées :

- **UTP** (Unshielded Twisted Pair) : Non blindées
- **STP** (Shielded Twisted Pair) : Blindées
- **FTP** (Foiled Twisted Pair) : Écrantées
- **SFTP** : Écrantées et blindées

| Vitesse | Câble compatible |
|---------|------------------|
| 100M | CAT5 (100 m) |
| 1G | CAT5e (100 m) |
| 10G | CAT6 (55 m), CAT6a (100 m), CAT7 (100 m) |
| 40G | CAT8.1 (30 m), CAT8.2 (30 m) |

##### Fibre optique

Transport par propagation d'ondes lumineuses dans une fibre de verre très fine. Une fibre par direction de transmission.

**Types d'émetteurs** :
- LED (850 nm)
- Diodes infrarouge (1300 nm)
- Lasers pour monomode (1300 ou 1550 nm)

**Catégories de fibres** :
- **Saut d'indice** (200/380 μm) : Grande dispersion, matériels économiques
- **Gradient d'indice** (62.5/125 μm) : Couches d'indices proches, distances jusqu'à 2 km
- **Monomode** (10 μm) : Propagation directe, nécessite des lasers coûteux, hauts débits longue distance

##### Supports sans fil

**Ondes radio** : Traversent les obstacles mais subissent absorption, atténuation et réflexion. Réglemention stricte des fréquences et puissances.

**Infrarouge** : Alternative aux ondes radio dans les environnements à fortes interférences, mais ne traverse pas les obstacles opaques. Réglementation moins stricte.

### Technologies Ethernet

#### Historique et normalisation

Développé par Digital, Intel et Xerox (DIX), Ethernet devient standard IEEE 802.3 en 1985, puis norme ISO 8802-3 en 1989. Le format de nommage IEEE : **XX TTT MM** avec XX (débit Mb/s), TTT (technique de codage), MM (identification média).

#### Ethernet 10 Mb/s

**10BASE5 (gros coaxial)** : 500 m par segment, 100 accès maximum, transceivers externes avec câbles AUI.

**10BASE2 (coaxial fin)** : 185 m par segment, 30 accès maximum, transceivers intégrés avec connecteurs BNC.

**10BASE-T (paires torsadées)** : UTP catégorie 3/4/5, 100 m maximum, topologie physique étoile avec fonctionnement logique en bus via concentrateur.

**10BASE-F (fibre optique)** : 500 m à 2 km selon le type, utilisée principalement pour les backbones.

#### Fast Ethernet (100 Mb/s)

**100BASE-T4** : 4 paires UTP catégorie 3/4/5, 3 paires à 33 Mb/s plus détection d'erreur.

**100BASE-TX** : 2 paires UTP/STP catégorie 5, 100 m maximum, meilleur rapport qualité/prix.

**100BASE-FX** : 2 brins fibre multimode 62.5/125 μm, seule solution au-delà de 100 m.

#### Gigabit Ethernet

**1000BASE-CX** : Paire torsadée blindée cuivre
**1000BASE-SX** : Fibre optique courte longueur d'onde (850 nm)
**1000BASE-LX** : Fibre optique longue longueur d'onde (1300 nm)
**1000BASE-T** : 4 paires UTP catégorie 5, 250 Mb/s par paire, 100 m maximum

#### 10 Gigabit Ethernet et au-delà

Solutions commercialisées depuis 2002, fonctionnement uniquement en commutation, distances de 2 m à 40 km sur fibre optique. La norme 10GBase-T (2006) nécessite des câbles catégorie 6a ou 7 pour atteindre 100 m.

Standards 25G et 40G (802.3bq, 2016) utilisent 4 paires torsadées sur 30 m pour datacenters.

### Wi-Fi et réseaux sans fil 802.11

#### Standards concurrents

**HiperLAN (ETSI)** : Bande 5 GHz, 24 Mb/s (version 1) à 54 Mb/s (version 2).

**802.11 (IEEE)** : Bande 2,4 GHz (ISM), 14 canaux avec chevauchement limitant à 3 réseaux coexistants.

#### Évolutions 802.11

- **802.11b (Wi-Fi)** : 11 Mb/s, comparable à Ethernet 10BASE-T
- **802.11g** : 54 Mb/s
- **802.11n** : 100 Mb/s sur 90 m, technologie MIMO, bandes 2,4 et 5 GHz
- **802.11ac (Wi-Fi 5)** : 1,3 Gb/s jusqu'à 7 Gb/s, bande 5-6 GHz exclusivement
- **802.11ad** : 6,75 Gb/s à 60 GHz, portée limitée à 10 m
- **802.11ah** : 8 Mb/s à 0,9 GHz, portée 100 m
- **802.11ax (Wi-Fi 6)** : 1,2 Gb/s par flux, consommation réduite, gestion améliorée des interférences

#### Modes de fonctionnement

**Mode infrastructure** : Points d'accès (AP) centralisent les communications, jusqu'à 100 stations par AP. Cellules avec recouvrement possible.

**Mode ad-hoc** : Communication directe entre stations sans point d'accès central. Simplicité de mise en œuvre mais limitations fonctionnelles.

### Équipements réseau spécialisés

#### Répéteur

Régénère les signaux affaiblis selon les distances maximales :

- 100 m pour paire torsadée
- 185 m pour coaxial fin
- 500 m pour gros coaxial

Formes : répéteur bi-port, concentrateur (hub), étoile optique.

#### Pont

Répéteur filtrant reliant deux segments. Transmet uniquement les trames destinées à l'autre segment, réduisant l'encombrement réseau.

#### Commutateur (switch)

Pont multi-ports performant distribuant les trames uniquement sur les ports concernés. Améliore la confidentialité et multiplie la bande passante totale par le nombre de ports.

#### Réseaux locaux virtuels (VLAN)

Segmentation logicielle des grands réseaux d'entreprise. Un VLAN constitue un domaine de broadcast regroupant les stations selon des critères organisationnels.

**Types de VLAN** :
- **Niveau 1 (physique)** : Regroupement par ports
- **Niveau 2 (MAC)** : Regroupement par adresses MAC
- **Niveau 3 (paquet)** : Regroupement par adresses IP

### Adressage et format des trames

#### Adressage MAC

Identification unique de chaque interface réseau via une adresse de 6 octets :

- 3 premiers octets : Numéro constructeur (OUI - Organizationally Unique Identifier)
- 3 derniers octets : Numéro de série

**Bits spéciaux** :
- Premier bit à 1 : Adresse multicast (groupe)
- Tous bits à 1 : Broadcast (diffusion générale)

#### Principe Ethernet CSMA/CD

**Carrier Sense Multiple Access with Collision Detection** : Écoute du média avant émission, détection des collisions, algorithme de récupération (back-off) avec attente aléatoire exponentielle.

Délai inter-trames minimum : 96 bits-times (9,6 μs à 10 Mb/s, 0,96 μs à 100 Mb/s).

#### Format des trames Ethernet

Longueur totale : 64 à 1518 octets (sans préambule).

**Champs constitutifs** :
- **Préambule** : 48 bits de synchronisation + SFD (10101011)
- **Adresses** : 6 octets source et destination
- **Type/Longueur** : Protocole supérieur (Ethernet V2) ou longueur données (IEEE 802.3)
- **Données** : 46 à 1500 octets (complétés par PAD si nécessaire)
- **FCS** : Contrôle d'intégrité CRC-32

Le Frame Check Sequence permet la détection d'erreurs sur 1, 2 ou un nombre impair de bits, ainsi que la majorité des rafales d'erreurs.
