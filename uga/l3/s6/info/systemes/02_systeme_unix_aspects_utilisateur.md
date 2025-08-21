# 02 // système unix - aspects utilisateur

[systemes_cours2_2324.pdf](ressources/02_systeme_unix_aspects_utilisateur_systemes_cours2_2324.pdf)

# Les systèmes UNIX - Aspects utilisateurs en ligne de commande

## Historique et évolution d'UNIX

UNIX fut conçu au début des années 1970 chez Bell pour répondre aux besoins des mini-ordinateurs de l'époque. Développé par des informaticiens pour des informaticiens, ce système d'exploitation privilégiait l'évolutivité et l'ouverture dès sa conception. Cette philosophie a permis une diffusion remarquable, s'étendant des gros systèmes aux plateformes personnelles modernes comme Linux, macOS et Android.

L'écosystème UNIX présente plusieurs branches distinctes. Les versions constructeurs incluent IBM-AIX, HP-UX et Ultrix, chacune adaptée aux spécificités matérielles de son fabricant. La famille BSD (Berkeley Software Distribution) et ses dérivées comme SunOS représentent une autre lignée importante. Linux constitue aujourd'hui l'implémentation la plus répandue d'un système de type UNIX.

La norme POSIX (Portable Operating System Interface) standardise l'interface de programmation des systèmes UNIX, garantissant une portabilité des applications entre différentes implémentations.

## Architecture générale d'UNIX

UNIX présente une architecture modulaire centrée autour du noyau (kernel) qui gère les ressources matérielles fondamentales. Cette conception multi-tâches et multi-utilisateurs permet l'exécution simultanée de plusieurs processus par différents utilisateurs sur une même machine.

### Composants architecturaux

Le **système de gestion de fichiers (SGF)** organise le stockage des données selon une structure arborescente unifiée. Les **outils de développement** fournissent l'environnement nécessaire à la création et à la maintenance des programmes. La **gestion du système** supervise l'allocation des ressources et l'administration des utilisateurs.

Le module de **communications** assure l'intégration réseau, facilitant les échanges de données entre machines distantes. L'**interpréteur du langage de commandes (shell)** constitue l'interface principale entre l'utilisateur et le système, permettant l'exécution interactive des programmes.

Le système supporte indifféremment les interfaces textuelles et graphiques, s'adaptant aux besoins spécifiques de chaque contexte d'utilisation.

## Système de gestion de fichiers

### Structure arborescente

Les données s'organisent dans des fichiers possédant chacun un nom unique et un contenu spécifique. Les répertoires constituent un type particulier de fichiers regroupant plusieurs autres fichiers selon une logique fonctionnelle ou thématique.

L'architecture adopte une vue arborescente avec une racine unique notée "/" (root). Les répertoires forment les nœuds internes de cette structure tandis que les fichiers ordinaires constituent les feuilles terminales.

La norme FHS (Filesystem Hierarchy Standard) définit l'organisation standard de cette hiérarchie sur les systèmes Linux modernes.

### Organisation standard Linux

Le répertoire **/bin** contient les binaires essentiels des commandes utilisateur comme `bash`, `cat`, `chmod`, `cp`, `ls` et `mkdir`. Le répertoire **/dev** regroupe les fichiers de périphériques, incluant `/dev/null` pour les opérations de redirection.

Le répertoire **/etc** centralise les fichiers de configuration système tels que `passwd`, `hosts`, `fstab` et les scripts d'initialisation. Le répertoire **/home** héberge les répertoires personnels des utilisateurs.

Le répertoire **/usr** rassemble les applications et données utilisateur en lecture seule. Sa sous-structure inclut **/usr/bin** pour la plupart des commandes utilisateur, **/usr/lib** pour les bibliothèques, et **/usr/share** pour les données statiques partagées.

Le répertoire **/var** stocke les données variables comme les journaux système (**/var/log**), les files d'attente (**/var/spool**) et les caches applicatifs (**/var/cache**).

### Points de montage

UNIX permet d'attacher différents périphériques de stockage à divers endroits de la hiérarchie de fichiers. Cette capacité de montage unifie l'accès aux données indépendamment de leur localisation physique sur différents disques ou partitions.

## Navigation dans le système de fichiers

### Notion de chemin

Chaque fichier s'identifie par son chemin complet dans l'arborescence. Le caractère "/" sépare les différents niveaux de répertoires. Par exemple, `/home/bob/monFichier.txt` désigne le fichier `monFichier.txt` situé dans le répertoire `bob` lui-même contenu dans `/home`.

Les chemins relatifs permettent de référencer un fichier par rapport à la position courante. Le symbole ".." désigne le répertoire parent, permettant la remontée dans la hiérarchie. Ainsi, depuis `/home/bob`, le fichier `/home/lili/chose.txt` peut être référencé par `../lili/chose.txt`.

### Répertoire personnel (home directory)

UNIX gérant plusieurs utilisateurs simultanément, chaque utilisateur dispose de son répertoire personnel appelé "home". Ce répertoire, généralement situé sous `/home/nom_utilisateur`, constitue l'espace de travail privé de l'utilisateur.

L'ouverture d'un terminal positionne automatiquement l'utilisateur dans son répertoire personnel, servant de point de départ pour la navigation dans le système.

## Interface en ligne de commande

### Terminal et shell

L'**interpréteur de commande** ou **shell** permet le dialogue direct avec le système d'exploitation. Plusieurs implémentations coexistent : bash, sh, ksh, csh, chacune offrant des fonctionnalités spécifiques.

Le **terminal** constitue le logiciel hébergeant l'interpréteur de commande. Les implémentations courantes incluent Konsole (KDE), Terminal (macOS), et Gnome-terminal (GNOME).

### Syntaxe des commandes

La syntaxe générale suit le pattern : `nom-de-la-commande -options --options-longues parametre1 parametre2`

Le shell lit, interprète et exécute chaque commande saisie par l'utilisateur, affichant éventuellement les résultats à l'écran. Les options peuvent nécessiter des arguments complémentaires. Généralement, le nom de commande référence un fichier exécutable stocké dans les répertoires système.

### Commandes de navigation essentielles

La commande `pwd` (Print Working Directory) affiche le répertoire de travail courant. L'exécution `pwd` depuis le répertoire personnel renvoie par exemple `/home/utilisateur`.

La commande `ls` (list) liste le contenu d'un répertoire. `ls` seul affiche le contenu du répertoire courant, tandis que `ls /bin` liste spécifiquement le contenu de `/bin`.

La commande `cd` (change directory) modifie le répertoire de travail. `cd /bin` déplace vers `/bin`, tandis que `cd` sans argument ramène au répertoire personnel.

### Caractères spéciaux et chemins

Les **chemins spéciaux** s'évaluent dynamiquement : `~` représente le répertoire personnel, `.` le répertoire courant, `..` le répertoire parent.

Les **caractères jokers** facilitent la sélection de fichiers : `?` remplace un caractère quelconque, `*` remplace une séquence de caractères (y compris vide), `[abcd]` correspond à l'un des caractères listés, `[!efg]` exclut les caractères spécifiés.

### Fichiers cachés

Les fichiers dont le nom commence par un point restent masqués lors des listages standard. Le répertoire `~/.ssh` stocke typiquement les clés de chiffrement SSH. L'option `ls -a` révèle tous les fichiers, y compris les fichiers cachés.

## Manipulation de fichiers

### Création d'éléments

La commande `mkdir DIRECTORY` crée un nouveau répertoire. La commande `touch FILE` génère un fichier vide ou met à jour la date de modification d'un fichier existant. La commande `ln -s TARGET LINKNAME` établit un lien symbolique (raccourci) vers un fichier ou répertoire cible.

### Opérations de copie et déplacement

La commande `cp SOURCE DEST` copie le fichier source vers la destination spécifiée. La variante `cp SOURCE DIRECTORY` place la copie dans le répertoire de destination en conservant le nom original.

La commande `mv SOURCE DEST` déplace ou renomme un fichier selon le contexte. `mv SOURCE DIRECTORY` déplace le fichier dans le répertoire spécifié.

### Suppression d'éléments

La commande `rm FILE...` supprime les fichiers listés en paramètres. La commande `rmdir DIRECTORY...` supprime les répertoires vides spécifiés. Pour les répertoires contenant des fichiers, `rm -rf` force la suppression récursive.

### Affichage du contenu

La commande `cat` affiche intégralement le contenu d'un fichier texte. Les commandes `more` et `less` proposent un affichage paginé pour les fichiers volumineux, `less` offrant des fonctionnalités de navigation supérieures.

## Gestion des utilisateurs et groupes

### Structure des utilisateurs

Le fichier `/etc/passwd` répertorie tous les utilisateurs système. Chaque utilisateur se caractérise par un identifiant numérique unique (uid), un nom d'utilisateur (username), un groupe principal (gid), un champ d'information personnelle (gecos), son répertoire personnel et le programme de connexion (généralement le shell).

L'utilisateur **root** possède l'uid 0 et dispose des privilèges administrateur complets. Les utilisateurs avec uid inférieur à 1000 sont généralement réservés aux services système.

### Système de groupes

Chaque utilisateur appartient à un groupe principal unique et peut être membre de groupes secondaires additionnels. Le fichier `/etc/group` définit l'appartenance aux groupes selon le format : `groupname:x:gid:liste_utilisateurs_secondaires`.

### Administration des comptes

Les commandes `adduser`/`useradd` créent de nouveaux utilisateurs, `usermod` modifie les comptes existants, `deluser` les supprime. La commande `passwd` permet le changement de mot de passe. Les commandes `id` et `id USERNAME` affichent les informations d'appartenance aux groupes.

La gestion des utilisateurs et groupes nécessite les privilèges root, accessibles via `su -` ou par l'intermédiaire de `sudo`.

## Système de permissions

### Modèle de droits

UNIX implémente un système de permissions à trois niveaux : le propriétaire du fichier (u), le groupe propriétaire (g), et les autres utilisateurs (o). Trois types de droits s'appliquent : lecture (r), écriture (w), et exécution (x).

La commande `ls -l` révèle les permissions selon le format : type de fichier suivi de neuf caractères représentant les droits par catégorie d'utilisateur.

### Gestion des permissions

La commande `chmod` modifie les permissions selon la syntaxe : `chmod [qui][action][droits] fichier`

Les spécificateurs "qui" incluent (u)ser, (g)roup, (o)ther, (a)ll. Les actions comprennent + (ajouter), - (retirer), = (définir exactement). Les droits s'expriment par r, w, x.

## Gestion des processus

### Concept de processus

Un **processus** représente l'exécution d'un programme en mémoire. UNIX étant multitâche, plusieurs processus s'exécutent simultanément, chacun identifié par un numéro unique (PID - Process Identifier).

Chaque processus possède un processus parent (PPID - Parent Process Identifier), formant une hiérarchie. Le processus init ou systemd constitue l'ancêtre de tous les processus utilisateur.

### Hiérarchie des processus

Au démarrage, le noyau initialise le matériel puis lance le premier processus (init/systemd). Ce processus engendre tous les autres selon une structure arborescente visible via la commande `pstree`.

Les processus héritent des droits de l'utilisateur qui les a lancés, déterminant leurs capacités d'accès aux ressources système.

### Contrôle des processus

L'opérateur `&` lance un processus en arrière-plan, libérant le terminal pour d'autres commandes. La combinaison Ctrl+Z suspend un processus, `bg` le reprend en arrière-plan.

Les commandes `ps` et `ps aux` listent respectivement les processus du terminal courant et tous les processus système. Les outils `pstree` et `htop` offrent des vues alternatives de l'activité des processus.

### Signaux système

Les signaux permettent la communication avec les processus via `kill -SIGNAL PID`. Le signal SIGTERM (15) demande un arrêt propre du processus, SIGKILL (9) force sa terminaison immédiate.

## Redirections et tubes

### Flux standards

Chaque processus dispose de trois flux de communication standards : l'entrée standard (stdin, généralement le clavier), la sortie standard (stdout, l'écran), et la sortie d'erreur (stderr, également l'écran par défaut).

### Mécanismes de redirection

L'opérateur `<` redirige l'entrée standard depuis un fichier. L'opérateur `>` redirige la sortie standard vers un fichier (écrasement), `>>` effectue un ajout. L'opérateur `2>` redirige spécifiquement la sortie d'erreur.

La construction `2>&1` combine les sorties standard et d'erreur vers la même destination.

### Tubes (pipes)

L'opérateur `|` connecte la sortie standard d'un processus à l'entrée standard d'un autre, créant un pipeline de traitement. Cette fonctionnalité exploite une mémoire partagée entre processus.

L'exemple `ls -1 / | wc -l` illustre ce mécanisme : la liste des fichiers générée par `ls` alimente directement le compteur de lignes `wc`.

## Le shell BASH

### Présentation

BASH (Bourne Again Shell) constitue l'interpréteur de commande par défaut sur la plupart des systèmes Linux. Il combine les fonctionnalités d'exécution interactive des commandes et de programmation par scripts (mode batch).

### Système de variables

#### Définition et utilisation

L'affectation suit la syntaxe `maVariable=valeur` (sans espaces). La substitution s'effectue via `$maVariable` ou `${maVariable}` pour la concaténation dans des chaînes complexes.

Par défaut, les variables restent locales au shell courant. La commande `export` rend une variable accessible aux processus fils.

#### Variables prédéfinies

La variable `$PATH` définit les répertoires de recherche des commandes exécutables. `$HOME` contient le chemin du répertoire personnel. `$SHELL` indique l'interpréteur de commande actuel.

#### Variables spéciales

`$?` renvoie le code de retour de la dernière commande (0 pour succès). `$$` contient le PID du shell courant. `$!` stocke le PID de la dernière commande en arrière-plan.

Les variables `$0` à `$9` correspondent aux paramètres de ligne de commande d'un script. `$#` compte le nombre de paramètres, `$*` les concatène, `$@` les présente sous forme de tableau.

### Opérations avancées

#### Tableaux

La déclaration `montab=("un" "deux" "trois")` crée un tableau. L'accès s'effectue via `${montab[index]}`, l'affichage complet via `${montab[@]}`.

#### Évaluation arithmétique

Les expressions arithmétiques nécessitent `let a=3+4` ou `a=$((3+4))` pour l'évaluation numérique. Sans ces constructions, `a=3+4` traite l'expression comme une chaîne littérale.

#### Substitution de commandes

La syntaxe `$(commande)` ou `` `commande` `` remplace l'expression par le résultat de l'exécution de la commande spécifiée.

### Initialisation du shell

Les shells de connexion (login shells) exécutent successivement `/etc/profile` puis l'un des fichiers `~/.bash_profile`, `~/.bash_login`, ou `~/.profile`.

Les shells interactifs non-login exécutent `/etc/bash.bashrc` puis `~/.bashrc` pour l'initialisation des variables et alias.

## Composition et contrôle des commandes

### Opérateurs de séquencement

L'opérateur `;` permet l'exécution séquentielle de commandes indépendamment de leur succès. L'opérateur `&&` conditionne l'exécution de la seconde commande au succès de la première. L'opérateur `||` exécute la seconde commande uniquement en cas d'échec de la première.

## Programmation shell

### Structure des scripts

Les scripts BASH débutent par la ligne `#!/bin/bash` spécifiant l'interpréteur. Les commentaires commencent par `#`. La commande `exit N` termine l'exécution avec le code de retour N.

### Entrées/sorties

La commande `echo` affiche du texte, `echo -n` supprime le retour à la ligne final, `echo -e` interprète les séquences d'échappement. La commande `read` lit l'entrée utilisateur dans des variables spécifiées.

### Gestion des paramètres

Les paramètres de script s'accèdent via `$1` à `$9`. La commande `shift` décale les paramètres pour traiter plus de neuf arguments. Les variables `$#`, `$*`, et `$@` fournissent respectivement le nombre, la concaténation, et le tableau des paramètres.

### Structures conditionnelles

La structure `if/then/fi` évalue le code de retour d'une commande (0 pour vrai, non-zéro pour faux). Les variantes `if/then/else/fi` et `if/then/elif/then/else/fi` permettent des branchements complexes.

### Commande test

La commande `test` ou sa forme `[ ]` évalue des conditions sur les fichiers (`-r`, `-w`, `-x`, `-f`, `-d`), les chaînes (`=`, `!=`, `-z`, `-n`), et les nombres (`-eq`, `-lt`, `-gt`).

Les opérateurs logiques `-a` (et), `-o` (ou), et `!` (négation) composent des expressions complexes.

### Structures itératives

La boucle `while/do/done` répète tant que la condition reste vraie. La boucle `until/do/done` répète jusqu'à ce que la condition devienne vraie. La boucle `for/do/done` itère sur une liste d'éléments.

## Recherche et manipulation de données

### Recherche de fichiers

La commande `find` effectue des recherches récursives selon la syntaxe : `find chemin(s) critère(s) action(s)`

Les critères incluent `-name` pour le nom, `-size` pour la taille, `-mtime` pour la date de modification, `-user` pour le propriétaire. Les actions comprennent `-print`, `-ls`, `-exec`, et `-ok` pour l'exécution interactive.

### Recherche dans le contenu

La commande `grep` filtre les lignes correspondant à une expression régulière. Les options `-v` inverse la sélection, `-c` compte les correspondances, `-n` affiche les numéros de lignes, `-i` ignore la casse.

### Manipulation de texte

La commande `cut` extrait des colonnes spécifiques via `-f` (champs délimités) ou `-c` (positions de caractères). Les commandes `wc` compte les mots/lignes/caractères, `sort` trie les lignes, `uniq` élimine les doublons sur un fichier préalablement trié.