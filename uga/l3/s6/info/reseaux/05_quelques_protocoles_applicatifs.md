## 05 // quelques protocoles applicatifs

[05_quelques_protocoles_applicatifs_5_protocoles_applicatifs.pdf](ressources/05_quelques_protocoles_applicatifs_5_protocoles_applicatifs.pdf)

## Protocoles applicatifs

Les protocoles applicatifs constituent la couche supérieure de l'architecture TCP/IP, fournissant des services directement utilisables par les applications et les utilisateurs finaux. Ces protocoles s'appuient sur les services de transport fiables ou non-fiables fournis par TCP et UDP.

### DNS - Domain Name System

Le système DNS permet d'associer des noms symboliques lisibles par l'homme à des adresses IP numériques. Cette traduction bidirectionnelle constitue l'un des services fondamentaux d'Internet, rendant la navigation intuitive tout en préservant l'efficacité du routage numérique.

#### Structure hiérarchique

Les noms DNS s'organisent selon une structure hiérarchique similaire aux adresses IP. Chaque nom complet comprend deux composantes principales :

- Le nom de la machine (hostname) qui identifie un équipement spécifique
- Le nom de domaine (domain name) qui situe cette machine dans l'organisation hiérarchique globale

Par exemple, dans `prevert.upmf-grenoble.fr` :

- `prevert` représente le nom de la machine
- `upmf-grenoble.fr` constitue le domaine d'appartenance

#### Fonctionnement client-serveur

Dans chaque domaine, un serveur de noms (serveur DNS) maintient un annuaire local associant les noms aux adresses IP. Ce serveur traite les requêtes provenant tant des clients internes au domaine que des clients externes nécessitant une résolution de noms.

Le processus de résolution s'effectue selon un échange simple :

1. Le client envoie une requête contenant le nom à résoudre
2. Le serveur DNS consulte son annuaire local
3. Le serveur retourne l'adresse IP correspondante ou redirige vers un autre serveur

Le protocole DNS utilise UDP sur le port 53, privilégiant la rapidité pour ces échanges généralement courts et fréquents.

### FTP - File Transfer Protocol

Le protocole FTP, défini par la RFC 959, standardise le transfert de fichiers sur les réseaux TCP/IP. Ce protocole vise trois objectifs principaux :

- Permettre le partage de fichiers entre machines distantes
- Assurer l'indépendance vis-à-vis des systèmes de fichiers locaux
- Optimiser l'efficacité des transferts de données

#### Architecture à double canal

FTP implémente un modèle client-serveur utilisant deux canaux TCP distincts :

- **Canal de contrôle (port 21)** : transporte les commandes et les réponses de statut
- **Canal de données (port 20)** : assure le transfert effectif des fichiers

Cette séparation permet un contrôle fin des opérations tout en optimisant les performances des transferts volumineux. Le canal de contrôle reste actif durant toute la session, tandis que le canal de données s'ouvre uniquement lors des transferts.

### Telnet et SSH - Accès distant

#### Telnet - Terminal Network Protocol

Telnet émule une connexion de terminal vers un hôte distant, permettant l'exécution de commandes à distance comme si l'utilisateur était physiquement présent sur la machine cible. Le protocole utilise TCP pour garantir la fiabilité des échanges entre le clavier local et l'hôte distant.

L'architecture client-serveur de Telnet place :

- Le client sur la station de travail de l'utilisateur
- Le serveur sur l'hôte distant, écoutant sur le port TCP 23

Cependant, Telnet présente une vulnérabilité majeure : les identifiants (login et mot de passe) transitent en clair sur le réseau, exposant les sessions aux interceptions malveillantes.

#### SSH - Secure Shell

SSH constitue l'évolution sécurisée de Telnet, offrant :

- Des sessions interactives chiffrées entre client et serveur distant
- Le transfert sécurisé de fichiers
- L'authentification mutuelle par clés cryptographiques

SSH remplace avavantageusement les utilitaires non-chiffrés comme rlogin, rcp, rsh et telnet. Le serveur SSH écoute sur le port TCP 22, et toutes les communications bénéficient d'un chiffrement robuste protégeant contre l'écoute et la modification des données.

### DHCP - Dynamic Host Configuration Protocol

DHCP, défini par la RFC 2131, automatise la configuration des paramètres réseau TCP/IP. Ce protocole constitue une extension de BOOTP (Bootstrap Protocol) et simplifie considérablement l'administration des réseaux en attribuant automatiquement adresses IP, masques de sous-réseau, passerelles par défaut et autres paramètres réseau.

#### Méthodes d'allocation

DHCP propose trois méthodes d'attribution des adresses IP :

**Allocation manuelle** : L'administrateur préassigne des adresses IP spécifiques à des clients identifiés par leur adresse MAC.

**Allocation automatique** : Le serveur attribue automatiquement une adresse IP disponible de manière permanente.

**Allocation dynamique** : Le serveur concède une adresse IP pour une durée limitée (bail), permettant la réutilisation des adresses libérées.

#### Protocole d'échange

Le processus DHCP utilise UDP sur les ports 67 (serveur) et 68 (client) et suit une séquence en quatre étapes :

1. **DHCPDISCOVER** : Le client (0.0.0.0) diffuse une requête en broadcast (255.255.255.255) incluant son adresse MAC. Une temporisation aléatoire (1-10 secondes) évite la congestion lors de redémarrages simultanés.

2. **DHCPOFFER** : Le serveur répond en broadcast avec l'adresse MAC du client, une proposition d'adresse IP, la durée du bail et l'adresse du serveur.

3. **DHCPREQUEST** : Le client confirme son choix parmi les offres reçues (plusieurs serveurs DHCP peuvent coexister).

4. **DHCPACK** : Le serveur confirme l'attribution et transmet les paramètres complets.

Après réception du DHCPACK, le client peut vérifier la disponibilité de l'adresse attribuée via une requête ARP en diffusion. Si l'adresse s'avère déjà utilisée, il envoie un message DHCPDECLINE et relance le processus.

### Évaluation de TCP/IP

#### Avantages

L'adoption massive de TCP/IP résulte de nombreux atouts :

- **Gratuité et ouverture** : Aucun coût de licence et spécifications publiques
- **Indépendance constructeur** : Interopérabilité entre équipements hétérogènes
- **Universalité** : Support sur tous types de matériel, des microcontrôleurs aux supercalculateurs
- **Facilité d'installation** : Procédures standardisées et bien documentées
- **Maturité** : Protocoles éprouvés dans des environnements complexes depuis des décennies
- **Richesse applicative** : Vaste écosystème d'applications et services
- **Standardisation** : Documentation exhaustive et spécifications claires
- **Efficacité** : Conception simple mais performante

#### Limitations

TCP/IP présente néanmoins certaines contraintes :

- **Gouvernance américaine** : Standards émis aux États-Unis sans normalisation internationale formelle
- **Épuisement IPv4** : La plage d'adresses IPv4 a été entièrement allouée en février 2011
- **Complexité de gestion** : La facilité de déploiement peut conduire à des architectures ingérables
- **Absence de routage par source** : Impossibilité de router selon l'adresse d'origine
- **Sécurité** : Conception initiale sans considération sécuritaire, vulnérabilités intrinsèques du mode non-connecté

Ces limitations ont motivé le développement d'IPv6 et l'intégration de mécanismes de sécurité dans les protocoles modernes.
