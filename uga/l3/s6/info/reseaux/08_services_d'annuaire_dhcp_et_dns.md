# 08 // services d'annuaire dhcp et dns

[08_services_annuaire.pdf](ressources/08_services_annuaire.pdf)

# Les services d'annuaire DHCP et DNS

## Notion d'annuaire

Les services d'annuaire constituent l'ensemble des services permettant d'obtenir des informations à partir d'une base de données, qu'elle soit centrale ou répartie. Ces services apportent un confort considérable tant aux utilisateurs finaux qu'aux administrateurs réseau.

Les annuaires peuvent généralement être gérés selon deux approches principales : soit par plusieurs serveurs fonctionnant simultanément, soit par un serveur principal accompagné d'un ou plusieurs serveurs secondaires qui prennent le relais en cas de défaillance du serveur principal. Cette redondance assure la continuité de service et la haute disponibilité des informations d'annuaire.

Les services d'annuaire les plus répandus dans l'environnement réseau sont le DNS (Domain Name System) qui facilite la navigation des utilisateurs, et le DHCP (Dynamic Host Configuration Protocol) qui simplifie considérablement la tâche des administrateurs réseau.

## Le protocole DHCP

### Présentation générale

Le Dynamic Host Configuration Protocol (DHCP), défini par la RFC 2131, a été conçu comme une extension du protocole BOOTP (Bootstrap Protocol). Ce protocole fonctionne selon un modèle client/serveur et s'appuie sur le protocole UDP en utilisant les ports 67 et 68.

DHCP permet la configuration automatique des paramètres TCP/IP des différents hôtes du réseau, incluant l'adresse IP, le masque de sous-réseau, la passerelle par défaut, ainsi que d'autres paramètres réseau essentiels. Cette automatisation élimine la nécessité de configurer manuellement chaque poste de travail, réduisant considérablement les erreurs de configuration et la charge administrative.

### Méthodes d'allocation des adresses

DHCP propose trois méthodes distinctes d'allocation d'adresses IP, chacune répondant à des besoins spécifiques :

**Allocation manuelle** : Le serveur DHCP attribue une adresse IP spécifique définie préalablement par l'administrateur. Cette méthode garantit qu'un client particulier recevra toujours la même adresse IP, basée généralement sur son adresse MAC.

**Allocation automatique** : Le serveur DHCP attribue automatiquement une adresse IP disponible dans un pool d'adresses prédéfinies. Une fois attribuée, l'adresse reste associée au client de manière permanente.

**Allocation dynamique** : Le serveur DHCP attribue une adresse IP issue d'un pool d'adresses définies pour une durée limitée appelée bail (lease). Cette méthode optimise l'utilisation des adresses disponibles en permettant leur réutilisation après expiration du bail.

### Processus de configuration d'un client DHCP

Le processus de configuration d'un client DHCP suit un échange de messages en quatre étapes distinctes :

**DHCPDISCOVER** : Le client, ne possédant aucune adresse IP (0.0.0.0), envoie une requête en broadcast (255.255.255.255) dans laquelle il insère son adresse MAC. Cette requête permet d'identifier les serveurs DHCP disponibles sur le réseau.

**DHCPOFFER** : Les serveurs DHCP présents sur le réseau répondent en proposant chacun une adresse IP accompagnée d'une durée de bail et de leur propre adresse IP. Chaque serveur réserve temporairement l'adresse proposée.

**DHCPREQUEST** : Le client sélectionne généralement la première adresse IP reçue et envoie en broadcast une demande d'utilisation de cette adresse au serveur DHCP correspondant. Ce message comporte l'identification du serveur sélectionné, informant ainsi tous les serveurs de la décision du client.

**DHCPACK** : Le serveur DHCP sélectionné accuse réception de la demande et accorde l'adresse en bail. Simultanément, tous les autres serveurs DHCP retirent leurs offres et les adresses proposées redeviennent disponibles pour d'autres clients.

### Relais DHCP

Les clients DHCP communiquant par broadcast, la présence de sous-réseaux routés pose un problème technique majeur. En théorie, un serveur DHCP devrait être installé dans chaque sous-réseau pour pouvoir répondre aux requêtes locales.

Cependant, un routeur compatible avec la RFC 1542 peut faire office d'agent de relais DHCP, relayant les messages broadcast entre les différents sous-réseaux. Cette fonctionnalité évite la nécessité de déployer un serveur DHCP dans chaque segment du réseau.

Alternativement, une machine serveur peut être configurée comme agent de relais DHCP. Cet agent doit connaître l'adresse du serveur DHCP central mais ne peut pas être lui-même client DHCP. L'agent relaye les demandes des clients DHCP vers le serveur central et transmet les offres aux clients concernés.

## Le système DNS

### Présentation générale

Le Domain Name System (DNS) constitue l'annuaire le plus ancien et certainement le plus utilisé d'Internet. Conçu en 1983 à la demande de la DARPA (Defense Advanced Research Projects Agency), le DNS permet de traduire un nom de domaine en informations de plusieurs types qui y sont associées, notamment en adresse IP.

Le système DNS est construit sous la forme d'une structure arborescente hiérarchique, permettant une organisation logique et scalable de l'espace de nommage Internet. Cette architecture distribuée assure la robustesse et les performances du système à l'échelle mondiale.

### Notion de domaine

Un domaine représente un sous-arbre de l'espace de nommage DNS. La racine de cet arbre, appelée domaine racine, est symboliquement représentée par un point (.). Cette racine constitue le point de départ de toute résolution DNS.

Un domaine peut être organisé en sous-domaines, créant une hiérarchie arborescente. Par exemple, le domaine ".fr" peut contenir des sous-domaines comme ".a.fr" et ".b.fr", chacun pouvant à son tour contenir ses propres sous-domaines.

### Infrastructure des serveurs racine

Les treize serveurs racine DNS sont gérés par des organisations différentes réparties géographiquement : deux européennes, une japonaise et dix américaines. Cette distribution géographique assure la redondance et la performance du système DNS mondial.

Certains serveurs DNS racine utilisent en réalité des grappes de serveurs (clusters) utilisant la technique anycast. Cette technique d'adressage et de routage permet de rediriger automatiquement les données vers le serveur le plus proche ou le plus efficace selon la politique de routage en vigueur.

### Domaines de premier niveau

Les domaines se trouvant immédiatement sous la racine sont appelés domaines de premier niveau (TLD : Top Level Domain). Ces TLD se divisent en deux catégories principales :

**Domaines génériques (generic TLD)** : Les noms de domaines ne correspondant pas à une extension de pays, tels que ".org", ".com", ".net", ".edu", etc.

**Domaines de code pays (ccTLD : country code TLD)** : Les noms correspondant aux codes de pays selon la norme ISO 3166, comme ".fr" pour la France, ".be" pour la Belgique, ".ch" pour la Suisse.

### Notion de zone et délégation

Une zone constitue une organisation logique et administrative des domaines DNS. Le rôle principal d'une zone consiste à simplifier l'administration des domaines en permettant une gestion décentralisée.

La délégation de zones permet de déléguer l'administration d'une zone ou d'une sous-zone aux administrateurs locaux de cette zone. Cette approche simplifie la gestion globale du domaine en distribuant les responsabilités administratives.

Les serveurs de noms d'une zone disposent de toutes les informations concernant cette zone et font autorité sur une ou plusieurs zones. Cette autorité signifie que les réponses fournies sont considérées comme faisant foi pour les domaines de la zone.

### Organisation des domaines et zones

L'organisation de l'espace de nommage DNS reste complètement indépendante de l'implantation géographique d'un réseau ou de son organisation physique. Cette séparation permet une grande flexibilité dans la gestion des noms de domaine.

Les seules machines connues au niveau de l'espace de nommage sont les serveurs de noms déclarés. Ces informations restent accessibles par des bases de données "whois" qui permettent d'identifier les responsables et les caractéristiques techniques d'un domaine.

### Résolution directe et inverse

Le principe fondamental de la résolution de noms consiste à associer un nom d'hôte à une adresse IP. Cette opération, appelée résolution de noms directe, constitue l'usage le plus courant du DNS.

Un Fully Qualified Domain Name (FQDN), ou nom de domaine pleinement qualifié, représente un nom de domaine écrit de façon absolue et ponctué par un point final, comme "miashs-www.u-ga.fr.".

### Le domaine in-addr.arpa

Le processus inverse de résolution existe également et permet, pour une adresse IP donnée, de fournir le nom correspondant. Cette résolution de noms inverse utilise une zone particulière appelée "in-addr.arpa".

Le mécanisme de résolution inverse transforme une adresse IP en nom de domaine dans l'arbre in-addr.arpa. Par exemple, l'adresse IP 129.88.230.12 correspond au sous-domaine "12.230.88.129.in-addr.arpa" qui peut renvoyer le nom qualifié "miashs-www.u-ga.fr".

Cette inversion de l'ordre des octets dans le domaine in-addr.arpa permet de maintenir la structure hiérarchique du DNS tout en permettant la résolution inverse des adresses.

### Cache DNS et optimisation

Quand un hôte doit résoudre un nom, il s'adresse à un ou plusieurs serveurs de noms dits récursifs. Ces serveurs parcourent la hiérarchie DNS et transmettent la requête à d'autres serveurs de noms pour fournir une réponse complète au client.

Pour optimiser les requêtes ultérieures, les serveurs DNS récursifs conservent en mémoire (cache) les réponses des résolutions de noms précédentes. Cette information reste conservée pendant une période déterminée appelée Time To Live (TTL) et associée à chaque nom de domaine.

Le cache DNS améliore considérablement les performances du système en évitant de répéter des requêtes identiques et en réduisant la charge sur les serveurs autoritaires.

### Serveurs primaires et secondaires

Un nom de domaine peut utiliser plusieurs serveurs DNS pour assurer la redondance et la haute disponibilité. L'architecture typique comprend généralement au moins deux serveurs : un primaire et un secondaire, avec la possibilité d'avoir plusieurs serveurs secondaires.

L'ensemble des serveurs primaires et secondaires font autorité pour un domaine, ce qui signifie que leur réponse ne fait pas appel à un autre serveur ou à un cache. Cette autorité garantit l'exactitude et la fiabilité des informations fournies.

En revanche, les serveurs récursifs fournissent des réponses qui ne sont pas nécessairement à jour à cause du cache mis en place. Ces réponses sont qualifiées de "non-authoritative answer" (réponse ne faisant pas autorité).

### Types d'enregistrement DNS

Le système DNS utilise différents types d'enregistrements pour stocker diverses informations :

**SOA (Start Of Authority)** : Indique l'autorité sur la zone et contient toutes les informations administratives sur le domaine, incluant les délais de mise à jour des bases de données entre serveurs primaires et secondaires, ainsi que le nom du responsable du site.

**NS (Name Server)** : Spécifie les adresses des serveurs de noms pour le domaine, permettant de déléguer l'autorité à des serveurs spécifiques.

**A (Address)** : Permet de faire correspondre un nom d'hôte à une adresse IPv4 de 32 bits distribuée sur quatre octets.

**AAAA** : Version IPv6 de l'enregistrement A, associant un nom d'hôte à une adresse IPv6 de 128 bits sur seize octets.

**MX (Mail eXchanger)** : Déclare les serveurs de messagerie responsables de la réception des emails pour un domaine donné.

**CNAME (Canonical Name)** : Permet de définir des alias sur des nœuds existants, créant des noms alternatifs pour un même hôte.

**PTR (Pointer)** : Utilisé pour la résolution de noms inverse dans le domaine in-addr.arpa, permettant d'associer une adresse IP à un nom de domaine.