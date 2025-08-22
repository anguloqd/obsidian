# 04 // routage IP

[04_routage_ip_4_le_routage_ip.pdf](ressources/04_routage_ip_4_le_routage_ip.pdf)

# Le routage IP

Le routage IP constitue le mécanisme fondamental permettant aux paquets de données de traverser les réseaux interconnectés pour atteindre leur destination. Ce processus repose sur une architecture décentralisée où chaque nœud prend des décisions de routage locales sans connaissance globale du réseau.

## Principe de fonctionnement

Le protocole IP détermine automatiquement le chemin optimal pour acheminer les paquets de données de proche en proche jusqu'au destinataire. Cette transmission s'effectue par l'intermédiaire de routeurs (également appelés gateways) qui constituent les relais successifs de la route.

Le processus de routage implique trois étapes principales :
1. L'ordinateur émetteur identifie le premier relais sur le chemin
2. Chaque routeur intermédiaire examine l'adresse de destination dans l'en-tête du paquet, consulte sa table de routage, et redirige le datagramme vers le saut suivant
3. Le dernier routeur remet le paquet sur le réseau local du destinataire

### Architecture décentralisée

Le routage IP fonctionne selon un modèle décentralisé où aucun nœud ne possède une vision complète du réseau. Cette approche présente plusieurs avantages : robustesse face aux pannes, évolutivité et distribution de la charge de traitement.

Le routage s'effectue de saut en saut (next hop) depuis la source jusqu'à la destination. Les services de niveau supérieur comme le contrôle de flux, la gestion d'erreurs et le contrôle de congestion sont gérés de bout en bout par des protocoles comme TCP, permettant à IP de se concentrer uniquement sur l'acheminement.

## Tables de routage

### Structure et contenu

La table de routage contient une liste structurée des réseaux et hôtes de destination avec les informations nécessaires pour les atteindre efficacement. Chaque entrée spécifie la destination et le routeur de prochain saut pour transmettre le datagramme.

Le concept de "saut" (hop) désigne le passage d'un datagramme à travers un routeur. Le routeur de prochain saut doit être connecté au même segment de réseau physique que le routeur courant, garantissant ainsi la connectivité directe.

### Optimisation et sélection de route

Le routeur de prochain saut se choisit comme la destination intermédiaire offrant le coût minimal pour atteindre la destination finale. Cette métrique de coût peut s'exprimer en termes de :
- Délais de transmission
- Charges financières
- Nombre de sauts
- Bande passante disponible

L'efficacité du routage IP repose sur une conception optimisée des tables : seul le numéro de réseau de destination nécessite un stockage, réduisant ainsi l'espace mémoire requis et accélérant les consultations.

### Mise à jour des tables

Les tables de routage peuvent être maintenues selon deux approches :

**Routage statique** : Les routes sont configurées manuellement et restent fixes. Cette méthode convient aux réseaux simples à topologie stable ou pour des interventions de dépannage nécessitant des corrections manuelles.

**Routage dynamique** : Les routes s'adaptent automatiquement aux changements du réseau grâce à des protocoles de routage comme RIP (Routing Information Protocol) ou OSPF (Open Shortest Path First). Les réseaux modernes privilégient cette approche pour sa flexibilité et sa capacité d'adaptation.

## Distribution des tables de routage

### Hôtes versus routeurs

Les tables de routage existent aussi bien dans les hôtes que dans les routeurs, mais leur utilisation diffère fondamentalement :

- Les hôtes utilisent leur table de routage uniquement pour les datagrammes qu'ils génèrent eux-mêmes
- Les routeurs traitent et retransmettent les datagrammes provenant d'autres nœuds du réseau

Cette distinction reflète les rôles différents : les hôtes agissent comme points terminaux de communication, tandis que les routeurs servent d'intermédiaires pour l'acheminement.

### Route par défaut

Dans les configurations réseau simples disposant d'un seul point de sortie, la spécification explicite de chaque destination devient superflue. La route par défaut offre une solution élégante en dirigeant automatiquement tout le trafic non local vers un routeur unique.

Cette route par défaut se représente dans la table de routage par l'adresse spéciale `0.0.0.0`, signifiant "toutes les destinations non spécifiement listées". Ce mécanisme simplifie considérablement la configuration des réseaux à topologie simple.

## Interconnexion de sous-réseaux

Lorsqu'un réseau se subdivise en sous-réseaux, l'interconnexion nécessite des routeurs dédiés pour assurer la communication entre segments. Cette segmentation permet :
- L'optimisation des performances en réduisant les domaines de collision
- L'amélioration de la sécurité par isolation des segments
- La simplification de l'administration réseau
- La flexibilité dans l'allocation des adresses IP

Chaque sous-réseau requiert une connectivité vers les autres segments via des routeurs spécialisés qui maintiennent la cohérence de l'adressage global tout en préservant l'indépendance locale des segments.