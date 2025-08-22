# 09 // services d'intranet

[09_services_intranet.pdf](ressources/09_services_intranet.pdf)

# Services d'intranet

## Introduction

Les services d'intranet constituent l'épine dorsale des communications internes d'une organisation. Ces services comprennent principalement la messagerie électronique, les services d'annuaire et diverses autres services comme HTTP et NTP qui permettent le fonctionnement harmonieux des réseaux internes.

## La messagerie électronique

### Concept fondamental

La messagerie électronique représente un service d'échange de messages textuels initialement conçu pour transférer des fichiers de caractères ASCII. Ce système a évolué pour permettre la transmission de fichiers de tout type, avec des limitations de taille et un encodage spécifique en format caractères. La transmission s'effectue de manière asynchrone, ce qui signifie que l'émetteur et le récepteur n'ont pas besoin d'être connectés simultanément.

### Fonctionnalités principales

Un service de messagerie moderne offre plusieurs fonctionnalités essentielles. Le système d'adressage permet l'envoi vers un destinataire unique ou multiple. Les utilisateurs peuvent composer des messages et y attacher des pièces jointes. La gestion des files d'attente, appelées boîtes aux lettres, assure le stockage temporaire des messages. Enfin, un système d'archivage permet de classer les courriers selon différents critères dans des boîtes distinctes.

### Distinction entre types de communication

| Caractéristique | Messagerie électronique | Transfert de fichiers | Messagerie instantanée |
|----------------|-------------------------|----------------------|----------------------|
| Mode de transmission | Asynchrone | Synchrone | Synchrone |
| Type de données | Texte uniquement | Texte et binaire | Texte |
| Taille des fichiers | Limitée | Non limitée | Généralement limitée |
| Stockage | Message dans une boîte | Fichier dans une arborescence | Message dans une file de discussion |

## Architecture de messagerie

### Modèle de stockage et retransmission

L'architecture de stockage et retransmission utilise un réseau maillé d'agents de transfert de messages (MTA - Mail Transfer Agent). Ce système fonctionne de manière similaire à un réseau à commutation de paquets, où chaque MTA peut recevoir, stocker temporairement et retransmettre les messages vers leur destination. Les utilisateurs interagissent avec le système via des agents utilisateur de messagerie (MUA - Mail User Agent).

### Modèle d'acheminement de bout en bout

Dans le modèle de bout en bout, le serveur de messagerie achemine directement un message entre un émetteur et un destinataire en utilisant un service de transport existant, typiquement TCP. Un courrier est ainsi transmis comme une série de segments TCP, à l'image de la messagerie Internet SMTP.

### Architecture modulaire moderne

L'architecture moderne de messagerie comprend plusieurs composants spécialisés :

1. **MUA émetteur** : Composition du message
2. **MTA émetteur** : Envoi du message via SMTP
3. **MTA destinataire** : Réception du message
4. **MDA (Mail Delivery Agent)** : Stockage du message
5. **MAA (Mail Access Agent)** : Accès aux messages via POP/IMAP
6. **MUA destinataire** : Lecture des messages

### Cheminement des messages

Le processus de transmission d'un message suit une séquence précise. L'utilisateur compose son message avec son client de messagerie, qui peut le stocker temporairement si l'expédition immédiate n'est pas possible. Le message est ensuite transmis au MTA local en SMTP, puis acheminé vers le MTA du destinataire. En cas d'échec, un système de file d'attente permet la réémission. Le MDA stocke finalement le courrier dans la boîte aux lettres du destinataire, utilisant généralement les formats mbox ou maildir. Le destinataire peut ensuite récupérer ses messages via les protocoles POP ou IMAP.

## Protocoles de messagerie Internet

### Protocoles d'émission et de transfert

Le **Simple Mail Transfer Protocol (SMTP)**, défini par la RFC 821, constitue le protocole de base pour les échanges entre serveurs de messagerie. Il utilise des messages au format texte pour définir les communications. L'**Extended Simple Mail Transfer Protocol (ESMTP)**, défini par la RFC 1869, étend SMTP avec des commandes supplémentaires.

### Protocoles de relève

Le **Post Office Protocol (POP)** assure le dialogue de base entre un client de messagerie et un serveur pour la récupération du courrier. L'**Internet Message Access Protocol (IMAP)** offre des possibilités plus étendues, notamment la gestion des archives de courrier et la limitation des volumes de données échangées.

## Adressage global

### Syntaxe des adresses

Les adresses de courrier électronique suivent la syntaxe résumée dans la RFC 3696, basée sur les RFC 2821 et 2822. Elles sont codées dans un sous-ensemble limité de caractères ASCII et prennent toujours la forme `identifiant@domaine`. Le DNS permet de déterminer les serveurs de courrier d'un domaine via les enregistrements de type MX.

### Formats d'adresses

Plusieurs formats d'adresses sont acceptés :

- `bob@gmail.com` : forme simple
- `"bob"@gmail.com` : avec guillemets délimitant l'identifiant
- `bob (Bob Morane) @gmail.com` : avec commentaire ignoré
- `Bob Morane <bob@gmail.com>` : seule la partie entre crochets est considérée
- `bob@136.173.24.11` : forme littérale avec adresse IP

## Protocole SMTP

Le protocole SMTP fonctionne selon un modèle client/serveur entre deux MTA, utilisant des commandes textuelles envoyées via TCP sur le port 25 par défaut. Chaque commande, terminée par la séquence ASCII CR LF, reçoit une réponse du serveur composée d'un numéro et d'un message descriptif. Les MTA gèrent des files d'attente pour les messages en émission et réception.

## Format des messages

### Format de base RFC 822

Un courrier électronique est structuré en lignes de caractères US-ASCII sur 7 bits, chaque ligne ne dépassant pas 1000 caractères et terminée par CR LF. Le message comprend deux parties distinctes séparées par une ligne vide : l'entête et le corps. L'entête contient une liste de lignes décrivant les caractéristiques du message sous la forme `Nom_de_zone: Valeur_de_zone`.

### Entêtes obligatoires et facultatives

Trois entêtes sont obligatoires :
- `From:` adresse de l'émetteur
- `To:` adresse du destinataire  
- `Date:` date de création du message

Les entêtes facultatives incluent `Received:` pour le chemin suivi, `Reply-To:` pour l'adresse de réponse, `Subject:` pour l'objet, et `Message-ID:` pour l'identifiant unique. Les entêtes privées doivent être préfixées par `X-`.

## Format MIME

### Objectifs et évolution

Le format MIME (Multipurpose Internet Mail Extensions) apparaît en juin 1992 avec les RFC 1341 et 1342 pour combler les lacunes du format de base. Il permet la transmission de messages utilisant des jeux de caractères autres que l'US-ASCII, définit un système de typage pour documents multimédia, et autorise les corps de message à parties multiples.

### Types de données MIME

MIME définit cinq types principaux :

- **Type texte** : données lisibles (text/plain, text/html)
- **Type image** : différents codages image (image/jpeg, image/gif)
- **Type son** : codages audio (audio/basic)
- **Type vidéo** : images animées (video/mpeg)
- **Type application** : autres données (application/octet-stream)

### Types composites multipart

Les données composites permettent de combiner plusieurs types en un seul corps :

- `multipart/mixed` : données indépendantes
- `multipart/alternative` : alternatives d'une même information
- `multipart/digest` : transfert de messages multiples
- `multipart/parallel` : données présentées en parallèle
- `multipart/related` : données reliées

## Formats de codage MIME

### Codage quoted-printable

Ce format code un texte d'alphabet 8 bits en US-ASCII 7 bits. Les caractères standards (codes 33 à 127 sauf =) sont codés normalement, tandis que les caractères spéciaux 8 bits sont représentés par `=NM` où N et M sont les chiffres hexadécimaux du code ASCII.

### Codage Base64

Le codage Base64 permet de représenter tout type de données 8 bits avec des caractères US-ASCII. Les données sont découpées en groupes de 3 octets, convertis en groupes de 24 bits, puis codés par 4 caractères US-ASCII. Ce codage augmente la taille du message d'environ 30%.

### Autres formats

Le format 8 bits permet de transporter directement des caractères 8 bits dans les corps de messages, nécessitant des modifications ESMTP. Le format binaire pose des problèmes avec les limitations standard de longueur de ligne et de délimiteurs.

## Protocoles de relève

### Post Office Protocol (POP)

POP, défini dans la RFC 1939, constitue le protocole de relève le plus simple. La version 3 utilise le port TCP 110. Les messages transférés sont généralement effacés du serveur, bien qu'une copie puisse être conservée temporairement. POP ne gère pas les archives sur serveur et convient à l'utilisation depuis un poste client unique.

### Internet Message Access Protocol (IMAP)

IMAP, défini dans la RFC 2060, représente le protocole le plus complet. La version 4 utilise le port TCP 143 et gère le courrier directement sur le serveur, permettant la création de dossiers et le déplacement de messages. Il minimise les échanges de données et s'adapte à la consultation depuis différents postes clients.

## Implémentations logicielles

### MTA open source

Plusieurs solutions open source dominent le marché :

- **Sendmail** : existe depuis 1980, développé par Eric Allman
- **Postfix** : créé en 2001 par Vietse Venema
- **Exim** : développé depuis 1995 par Philippe Hazel
- **Qmail** : créé en 1997 par Dan Bernstein

Postfix et Qmail sont considérés comme les meilleures solutions actuelles.

### MTA propriétaires

Les solutions propriétaires incluent principalement des logiciels d'entreprise intégrés dans des suites bureautiques : Exchange/IIS (Microsoft), Zimbra (VMware), Lotus Notes/Domino (IBM), et IMAIL (Ipswitch).

## Service d'annuaire

### Concept et fonctionnalités

Les services d'annuaire assurent le stockage hiérarchique d'informations et permettent de modéliser différents objets : utilisateurs, machines, groupes, unités organisationnelles. Chaque objet possède des attributs associés sous forme de texte, données binaires ou listes. Le système intègre une gestion de droits d'accès et des mécanismes de sécurisation via TLS et authentification.

### Évolution vers LDAP

Avant LDAP, chaque annuaire possédait son propre protocole d'accès : NIS/YellowPages, Microsoft SAM, X.500 DAP. Le protocole X.500 DAP était jugé trop lourd pour l'implémentation. LDAP (Lightweight Directory Access Protocol) apporte une uniformisation protocolaire fonctionnant au-dessus de TCP/IP, permettant la communication avec tout service d'annuaire sans impact sur l'implémentation. Standardisé en 1993 (RFC 1487), révisé en 1995 (RFC 1777), LDAPv3 apparaît en 2002 et est révisé en 2006.

### Structure LDAP

Un annuaire LDAP forme un arbre d'entrées reflétant le modèle organisationnel, politique ou géographique de la structure. Chaque entrée comprend un ensemble d'attributs définis dans des schémas. Un attribut possède un nom, un type et une ou plusieurs valeurs. Le caractère multivalué constitue une différence majeure avec les SGBD. Chaque entrée possède un identifiant unique appelé Distinguished Name (DN).

### Communication LDAP

La communication suit un modèle client/serveur permettant aux applications de se connecter et s'authentifier auprès d'un serveur LDAP sur le port TCP 389. Le protocole supporte également les opérations d'import/export via le format LDIF (LDAP Data Interchange Format), particulièrement adapté à la sauvegarde et la réplication d'annuaires.

## Autres services

### HTTP (HyperText Transfer Protocol)

Les serveurs HTTP ou serveurs Web traitent les requêtes HTTP sur le port 80 et HTTPS sur le port 443. Apache, de la fondation Apache, reste populaire malgré la progression importante de Nginx. Apache, apparu en avril 1995, supporte de nombreux modules et la gestion de sites virtuels. Nginx, prononcé "engine-ex", utilise une architecture asynchrone et événementielle pour traiter efficacement de nombreuses connexions simultanées.

### NTP (Network Time Protocol)

NTP synchronise les horloges locales d'ordinateurs via le réseau sur une référence UTC. Cette synchronisation compense la dérive naturelle des horloges à quartz et s'avère indispensable pour certains protocoles réseau. Le protocole, ancien (version 0 en 1985), utilise UDP sur le port 123. La version 3 (RFC 1305) reste la plus répandue, tandis que la version 4 (RFC 5905, juin 2010) apporte des améliorations importantes.

### Architecture NTP

NTP utilise une structure hiérarchique de strates. La strate 0 comprend les horloges de référence (radios, satellites, horloges atomiques). Les serveurs de temps récupèrent l'heure auprès des récepteurs ou d'autres serveurs, tandis que les clients se synchronisent avec les serveurs de temps. Chaque client NTP peut également servir de serveur. La norme prévoit jusqu'à 16 strates, mais la plupart des clients se situent aux strates 3 ou 4. Cette organisation redondante permet une répartition efficace de la charge.