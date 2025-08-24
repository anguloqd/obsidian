## 01 // introduction

[systemes_cours1_2324.pdf](ressources/01_introduction_systemes_cours1_2324.pdf)

[systemes_cours1_bis_2223.pdf](ressources/01_introduction_systemes_cours1_bis_2223.pdf)

## Systèmes d'exploitation des ordinateurs

### Introduction aux ordinateurs

L'ordinateur constitue un système de traitement d'information programmable dont le fonctionnement repose sur la lecture séquentielle d'instructions. Ces instructions permettent d'exécuter des opérations logiques et arithmétiques, et leur ensemble forme ce que l'on appelle un programme.

### Architecture de von Neumann

L'architecture de von Neumann représente le modèle fondamental sur lequel reposent la plupart des ordinateurs modernes. Cette architecture se compose de quatre éléments principaux interconnectés par des bus de communication.

#### Composants de l'architecture

L'**Unité Arithmétique et Logique (UAL)** assure les traitements de base en effectuant les opérations arithmétiques, les lectures et écritures de données. L'**Unité de Contrôle (UC)** coordonne le séquencement des opérations et décode les instructions à exécuter.

La **mémoire** stocke simultanément le programme et les données, constituant une caractéristique distinctive de cette architecture. Les **entrées/sorties** permettent la communication avec l'environnement externe par l'intermédiaire de périphériques tels que l'écran, le clavier ou l'imprimante.

Le **processeur** regroupe l'UAL et l'UC, formant l'unité centrale de traitement de l'ordinateur.

### Système de mémoire

Le système de mémoire d'un ordinateur présente une hiérarchie complexe adaptée aux différents besoins de stockage et de vitesse d'accès.

#### Types de mémoire

Les **mémoires volatiles** perdent leur contenu lors de la coupure d'alimentation. Cette catégorie comprend les registres du processeur, la mémoire cache et la mémoire vive (RAM). À l'inverse, les **mémoires persistantes** ou **mémoires de masse** conservent les données de manière permanente et incluent les disques durs, les SSD et les dispositifs de stockage amovibles.

La représentation conceptuelle de la mémoire s'apparente à une commode où chaque tiroir, identifié par une adresse unique, contient des données sous forme binaire (0 et 1).

### Architecture du microprocesseur

Le **CPU (Central Processing Unit)** constitue un composant électronique intégrant plusieurs millions de transistors. Sa structure comprend plusieurs éléments essentiels au traitement des instructions.

#### Composants internes

L'**horloge** fournit le signal de synchronisation qui rythme l'ensemble des opérations, agissant comme un métronome électronique. L'**unité de contrôle** coordonne l'exécution des instructions tandis que l'**unité arithmétique et logique** effectue les calculs nécessaires.

Les **registres** représentent des mémoires spécialisées internes au processeur. L'**accumulateur (AC)** stocke les résultats des opérations de l'UAL. Le **compteur de programme (PC)** contient l'adresse de la prochaine instruction à exécuter. Le **registre d'instruction courante** mémorise l'instruction en cours de traitement.

#### Mécanisme d'interruption

Les interruptions constituent un mécanisme fondamental permettant d'interrompre temporairement l'exécution normale du processeur. Les périphériques utilisent ce système pour signaler l'achèvement d'une opération, comme une lecture de disque. Les interruptions servent également à annoncer les erreurs matérielles et permettent aux systèmes d'exploitation de partager le processeur entre plusieurs tâches simultanées.

### Langages de programmation et compilation

La programmation informatique s'articule autour de différents niveaux d'abstraction, depuis le langage machine jusqu'aux langages de haut niveau.

#### Langages de bas niveau

Le **langage machine** correspond au code binaire directement exécutable par le processeur. L'**assembleur** offre une version lisible du langage machine en remplaçant les codes binaires par des mnémoniques compréhensibles. Ces langages ne contiennent que les instructions natives du processeur et nécessitent une connaissance approfondie de l'architecture matérielle.

#### Langages de haut niveau

Les langages de haut niveau se rapprochent du langage naturel et de la démarche de résolution de problème plutôt que du fonctionnement interne de la machine. Cette abstraction facilite considérablement le développement d'applications complexes. Il existe plusieurs centaines de langages de haut niveau, chacun adapté à des domaines d'application spécifiques.

#### Processus de compilation

La **compilation** transforme un code source écrit dans un langage de haut niveau en code machine exécutable. Le **compilateur** effectue cette transformation en plusieurs étapes successives.

L'**analyse lexicale** découpe le texte source en unités lexicales (mots-clés, identificateurs, opérateurs). L'**analyse syntaxique** vérifie la conformité grammaticale du code selon les règles du langage de programmation. L'**analyse sémantique** contrôle la cohérence des types de données et des portées des variables, construisant la table des symboles. Enfin, la **génération de code machine** produit le code exécutable final.

#### Interprétation

L'**interpréteur** analyse et exécute directement le code source sans génération préalable de code machine. Cette approche diffère de la compilation par l'exécution immédiate des instructions plutôt que leur traduction préalable.

Les langages compilés incluent C, C++ et Java, tandis que Python et JavaScript sont généralement interprétés. Les interpréteurs trouvent également leur utilité dans les langages de commande permettant le dialogue interactif avec l'ordinateur.

### Composants matériels d'un PC

L'architecture matérielle d'un ordinateur personnel intègre plusieurs composants spécialisés interconnectés par la carte mère.

#### Alimentation et carte mère

L'**alimentation électrique** convertit le courant alternatif en tensions continues adaptées aux besoins spécifiques de chaque composant. La **carte mère** constitue le support principal où s'interconnectent tous les autres éléments. Elle intègre souvent des composants intégrés pour l'audio, le réseau (Wi-Fi, Ethernet), l'affichage de base et la connectivité USB.

#### Mémoire vive (RAM)

La **mémoire vive** ou **RAM (Random Access Memory)** fournit un espace de travail rapide pour les applications en cours d'exécution. Cette mémoire volatile perd son contenu lors de l'extinction de l'ordinateur.

Les caractéristiques principales incluent la capacité (généralement entre 8 et 32 Go), le type de technologie (DDR-SDRAM avec les standards DDR4 et DDR5), et le format physique (DIMM pour les ordinateurs de bureau, SO-DIMM pour les portables). La latence CAS (environ 10 nanosecondes) et la fréquence de fonctionnement (200 à 400 MHz) déterminent les performances d'accès. Le débit, exprimé en transferts par seconde (1600 à 3200 MT/s), dépend de la fréquence et du type de mémoire.

#### Mémoires de masse

Les **mémoires de masse** assurent le stockage permanent des données avec des capacités importantes, mesurées en téraoctets. Deux technologies principales coexistent actuellement.

Les **disques durs magnétiques** utilisent un support magnétique pour stocker l'information avec un temps d'accès d'environ 5 millisecondes. Les **SSD (Solid State Drive)** emploient une technologie de mémoire flash électronique offrant un temps d'accès considérablement réduit (0,05 milliseconde) mais à un coût supérieur.

Les formats physiques varient selon l'usage : 2,5 pouces et 3,5 pouces pour les disques traditionnels, M.2 pour les SSD compacts. Le choix entre ces technologies implique un arbitrage entre coût, performance, capacité et durée de vie.

#### Carte graphique

La **carte graphique** gère l'affichage et effectue les calculs vectoriels nécessaires aux applications 3D et aux jeux. Elle peut être intégrée au processeur pour les besoins basiques ou constituer un composant indépendant avec sa propre mémoire dédiée pour les applications exigeantes.

### Caractéristiques des microprocesseurs PC

Les microprocesseurs modernes se distinguent par plusieurs caractéristiques techniques déterminant leurs performances.

#### Spécifications techniques

La **fréquence d'horloge** s'exprime en gigahertz (1 GHz équivaut à un milliard de cycles par seconde). Le **nombre de cœurs** indique la capacité de traitement parallèle, avec généralement quatre cœurs ou plus dans les processeurs contemporains.

La **mémoire cache** représente une mémoire interne ultra-rapide dont la capacité minimale recommandée atteint 10 mégaoctets (capable de stocker 80 millions de bits). L'**architecture** définit le jeu d'instructions supporté, avec x64 pour les PC et ARM pour les smartphones.

#### Fabricants principaux

**Intel** domine le marché des processeurs PC avec plusieurs gammes : Atom pour les appareils mobiles, Celeron et Pentium pour l'entrée de gamme, Core (i3, i5, i7, i9) pour les utilisateurs particuliers et professionnels, et Xeon pour les serveurs.

**AMD** propose des alternatives avec les gammes Athlon, Ryzen pour les particuliers, et Epyc pour les serveurs. AMD développe également des processeurs graphiques haut de gamme.

### Logiciels de base

Le fonctionnement d'un ordinateur repose sur plusieurs couches logicielles essentielles qui s'exécutent avant les applications utilisateur.

#### BIOS

Le **BIOS (Basic Input Output System)** constitue un ensemble de programmes fondamentaux permettant l'initialisation de base lors de l'allumage de l'ordinateur. Stocké dans une mémoire flash non volatile sur la carte mère, le BIOS effectue les vérifications matérielles initiales et lance le processus d'amorçage du système d'exploitation.

#### Système d'exploitation

Le **système d'exploitation (OS - Operating System)** représente un ensemble de programmes dirigeant l'utilisation des ressources informatiques par les applications. Ses objectifs principaux consistent à faciliter la programmation et l'utilisation de la machine en fournissant une abstraction du matériel, tout en gérant efficacement les ressources disponibles.

### Systèmes d'exploitation contemporains

#### Classification par famille

Les systèmes d'exploitation actuels se répartissent en plusieurs catégories selon leur origine et leur licence. **Windows** de Microsoft adopte un modèle propriétaire, tandis que **macOS** d'Apple combine éléments propriétaires et libres. **GNU/Linux** respecte les principes du logiciel libre sous licence GNU GPL.

Pour les appareils mobiles, **iOS** d'Apple utilise un modèle propriétaire, alors qu'**Android** de Google s'appuie sur des licences libres (Apache v2 et GNU GPL v2).

On distingue traditionnellement deux familles principales : les systèmes de type UNIX (macOS, GNU/Linux) et les systèmes Windows.

#### Architecture système

L'organisation d'un système informatique présente une structure en couches hiérarchiques. Le **matériel** constitue la base physique, sur laquelle s'appuie le **système d'exploitation** qui fournit une interface standardisée. Les **applications** utilisent cette interface pour accéder aux ressources matérielles de manière abstraite.

Le système distingue deux modes d'exécution : le **mode noyau** offre un accès complet au matériel, tandis que le **mode utilisateur** limite l'accès aux ressources par l'intermédiaire d'abstractions sécurisées.

### Fonctionnalités des systèmes d'exploitation

#### Gestion des périphériques

La gestion des périphériques ou des entrées/sorties abstrait la communication avec les équipements externes (écran, clavier, webcam, imprimante, réseau) par l'intermédiaire de pilotes logiciels spécialisés. Cette abstraction permet aux applications d'utiliser les périphériques sans connaître leurs spécificités techniques.

#### Système de fichiers

La gestion des données s'organise autour d'un système de fichiers offrant une vue unifiée de l'accès aux informations stockées. Le système d'exploitation contrôle les autorisations d'accès aux fichiers et gère leur organisation logique indépendamment du support physique de stockage.

#### Gestion des ressources

La **gestion du processeur** utilise des stratégies d'ordonnancement pour partager le temps de calcul entre plusieurs applications simultanées (multiplexage temporel). La **gestion de la mémoire vive** répartit l'espace mémoire entre les différents programmes (multiplexage spatial).

#### Gestion des processus

Le système d'exploitation supervise l'exécution des applications sous forme de processus en affectant et partageant les ressources nécessaires. Il gère le cycle de vie complet des applications : démarrage, exécution, suspension et terminaison.

#### Interface utilisateur

Le système fournit des interfaces de commande et de programmation multiples. L'**interface de programmation** expose un ensemble d'appels système que les développeurs peuvent utiliser. La norme **POSIX** standardise cette interface pour les systèmes de type UNIX.

L'**interpréteur de commande (shell)** permet aux utilisateurs de dialoguer avec le système en mode textuel, bien qu'il ne fasse pas partie intégrante du système d'exploitation. L'**interface graphique** offre une alternative intuitive basée sur la manipulation d'éléments visuels à la souris.

#### Exemples d'utilisation

Une même opération, comme la copie d'un fichier, peut s'effectuer de trois manières différentes. En ligne de commande avec l'instruction `cp chose.txt truc.txt`, par programmation en langage C utilisant les fonctions `fopen()`, `getc()`, `putc()` et `fclose()`, ou graphiquement par glisser-déposer dans l'explorateur de fichiers.
