# 01 // introduction à ML

[lecture_general_introduction_2.pdf](ressources/01_introduction_a_ml_lecture_general_introduction_2.pdf)
[lecture_intro_python_2.pdf](ressources/01_introduction_a_ml_lecture_intro_python_2.pdf)

# Introduction à l'apprentissage automatique et environnement Python

## Vue d'ensemble de l'apprentissage automatique

### Définition fondamentale

L'apprentissage automatique (machine learning) désigne une famille d'algorithmes capables d'apprendre et de s'adapter sans suivre d'instructions explicites, en tirant des inférences à partir de motifs présents dans les données. Cette approche révolutionnaire permet aux systèmes informatiques d'acquérir des connaissances et d'améliorer leurs performances par l'expérience plutôt que par la programmation directe.

À partir d'un dataset d'entraînement, les algorithmes d'apprentissage automatique identifient des patterns dans les données pour prédire ou inférer des informations sur de nouvelles données non vues précédemment. Cette capacité d'extrapolation constitue le cœur de l'intelligence artificielle moderne.

### Typologie des problèmes d'apprentissage automatique

#### Apprentissage supervisé

L'apprentissage supervisé constitue une catégorie où l'algorithme apprend à partir de données d'exemple pour prédire des valeurs sur des données inconnues. Cette approche se subdivise en deux types principaux de problèmes :

**Problèmes de classification** : l'objectif consiste à prédire une classe, c'est-à-dire une variable catégorielle. Les exemples classiques incluent :

- **Reconnaissance de caractères manuscrits** : à partir de la répartition des pixels, l'algorithme apprend à associer les chiffres manuscrits à leur valeur réelle
- **Reconnaissance d'espèces de fleurs** : en utilisant les caractéristiques morphologiques des fleurs, le système prédit leur espèce d'appartenance
- **Diagnostic médical** : à partir des dossiers médicaux (poids, âge, taille, statut tabagique), prédiction de la présence de diabète chez les patients
- **Détection de tumeurs** : analyse des caractéristiques tumorales (taille, hauteur, largeur, couleur) pour déterminer leur nature cancéreuse

**Problèmes de régression** : l'objectif vise à prédire une métrique, c'est-à-dire une variable numérique. Les applications typiques comprennent :

- **Prédiction de prix immobiliers** : estimation du prix de vente d'une maison basée sur ses caractéristiques (superficie, localisation, nombre de chambres)
- **Prévision de performances sportives** : prédiction du temps d'un athlète en course à partir de ses résultats antérieurs (nombre de victoires, temps précédents, temps d'entraînement total)
- **Estimation de croissance** : prédiction du poids adulte de baleineaux à partir de leurs caractéristiques (espèce, localisation, parents)

#### Apprentissage non supervisé

L'apprentissage non supervisé se caractérise par la recherche de patterns dans les données pour fournir une meilleure compréhension de leur structure, sans variable cible prédéfinie.

**Problèmes de clustering** : regroupement des données en sous-ensembles homogènes. Les exemples incluent :

- **Analyse comportementale Netflix** : regroupement des utilisateurs selon leurs caractéristiques d'usage (temps quotidien, nombre d'éléments visionnés, répartition séries/films)
- **Segmentation client** : identification de différents comportements d'achat à partir des habitudes de consommation (nombre d'articles achetés, montant total dépensé)

## Environnement de développement Python

### Présentation de Python

Python constitue un langage de programmation de haut niveau, généraliste, qui privilégie la lisibilité du code. Ce langage interprété nécessite un interpréteur pour s'exécuter sur le système cible, contrairement aux langages compilés qui génèrent du code machine directement à partir du code source.

### Avantages de Python pour l'apprentissage automatique

Python domine le domaine de la science des données et de l'apprentissage automatique pour plusieurs raisons stratégiques :

- **Simplicité d'apprentissage** : syntaxe intuitive et lisible facilitant la prise en main
- **Flexibilité de déploiement** : possibilité d'utilisation en scripts ou en packages structurés prêts pour la production
- **Écosystème riche** : nombreuses bibliothèques spécialisées disponibles pour la science des données
- **Portabilité** : compilation possible pour améliorer les performances et la portabilité
- **Polyvalence** : applications étendues au-delà de la science des données (applications web, systèmes client-serveur)

### Installation et configuration de Python

#### Téléchargement et installation

L'installation de Python s'effectue via le site officiel https://www.python.org. La sélection de la version appropriée selon le système d'exploitation (Windows, macOS, Linux) garantit une compatibilité optimale. La vigilance s'impose concernant la compatibilité des bibliothèques avec chaque version de Python.

**Installation Windows** : l'exécutable d'installation doit être configuré avec l'option "Add Python x.x to PATH" pour permettre l'utilisation en ligne de commande.

**Installation macOS** : bien que Python soit préinstallé sur la plupart des versions macOS, l'utilisation du package d'installation officiel assure l'accès à la version la plus récente.

**Installation Linux** : Python s'avère souvent préinstallé. La vérification s'effectue via `python3 --version`. L'installation via le gestionnaire de packages (`sudo apt-get install python3` pour Debian ou `sudo yum install python3` pour Red Hat) complète l'installation si nécessaire.

#### Vérification de l'installation

La validation de l'installation s'effectue en ouvrant un terminal et en tapant `python3` pour démarrer l'interpréteur Python. L'apparition de l'invite Python (`>>>`) confirme l'installation correcte.

### Gestion des packages avec pip

#### Présentation de pip

pip constitue le gestionnaire de packages par défaut de Python, utilisé pour installer, gérer et distribuer les packages Python. Inclus dans les installations Python depuis la version 3.4, pip facilite considérablement la gestion des dépendances.

#### Utilisation de pip

Les **packages Python** regroupent des modules connexes organisés dans une hiérarchie de répertoires, fournissant des ensembles de fonctions, classes et variables. Cette organisation permet de bénéficier du travail d'autres développeurs sans redévelopper les fonctionnalités de base.

**Installation de packages** : `pip install <nom_package>`
**Liste des packages installés** : `pip list`
**Désinstallation** : `pip uninstall <nom_package>`

#### Fichiers de requirements

Les fichiers de requirements (`requirements.txt`) listent tous les packages nécessaires à un projet. L'installation groupée s'effectue via `pip install -r requirements.txt`, facilitant la reproduction d'environnements de développement identiques.

### Environnements virtuels Python

#### Concept et utilité

Un environnement virtuel Python constitue un répertoire autonome contenant une installation Python et son propre ensemble de packages. Cette isolation permet de gérer plusieurs environnements Python isolés sur le même système, évitant les conflits entre projets aux dépendances différentes.

#### Avantages des environnements virtuels

L'utilisation d'environnements virtuels s'avère **indispensable** en Python pour plusieurs raisons :

- **Isolation** : prévention des conflits entre dépendances de projets
- **Reproductibilité** : partage facile des spécifications d'environnement pour des configurations cohérentes
- **Nettoyage simple** : suppression de l'environnement virtuel pour éliminer tous les packages associés
- **Compatibilité de versions** : maintenance de différentes versions Python pour différents projets

#### Création et gestion d'environnements virtuels

**Création** : `python3 -m venv <chemin/vers/venv>`
**Activation** :
- Windows : `<chemin/vers/venv>/Scripts/activate`
- macOS/Linux : `source <chemin/vers/venv>/bin/activate`
**Désactivation** : `deactivate`

Une fois activé, l'environnement virtuel prend la priorité sur l'installation Python système, permettant une gestion isolée des packages.

### Modes d'exécution de Python

Python offre plusieurs modalités d'exécution adaptées à différents contextes :

- **Exécution interactive** : via terminal, iPython ou Jupyter Notebook
- **Exécution de scripts** : fichiers `.py` exécutés via l'interpréteur
- **Packages structurés** : code organisé en modules avec points d'entrée définis

#### Scripts Python

Un script Python consiste en un fichier d'extension `.py` exécutable via l'interpréteur. L'exemple basique d'un fichier contenant `print("I love learning Python!")` sauvegardé sous `test.py` s'exécute via `python test.py`.

## Jupyter Notebook : environnement de développement interactif

### Présentation de Jupyter

Jupyter Notebook constitue un environnement interactif basé sur le web permettant de créer et partager des documents contenant du code exécutable, des équations, des visualisations et du texte narratif. Largement adopté pour l'analyse de données, le calcul scientifique et l'apprentissage automatique, Jupyter fournit également un environnement d'apprentissage idéal pour Python.

### Installation et utilisation

L'installation s'effectue dans un environnement virtuel via `pip install jupyter`. Le démarrage se fait par `jupyter notebook` dans le répertoire de travail souhaité, ouvrant l'interface dans le navigateur web.

#### Interface et fonctionnalités

L'interface Jupyter s'organise autour de **cellules** pouvant contenir du code ou du texte (Markdown). L'exécution individuelle des cellules de code via `Shift + Enter` permet un développement itératif. Les variables et sorties persistent entre les cellules au sein du même notebook.

**Cellules Markdown** : permettent l'inclusion de texte formaté, titres, listes, liens, images et équations LaTeX, fournissant des capacités narratives riches pour documenter le code et l'analyse.

#### Partage et exportation

Les notebooks Jupyter se sauvegardent au format `.ipynb` et se partagent facilement via des plateformes comme GitHub, Jupyter Notebook Viewer ou Jupyter Hub. L'exportation vers divers formats (HTML, PDF, LaTeX, diapositives) facilite la diffusion des résultats.

## Ressources et matériel pédagogique

L'ensemble du matériel pédagogique reste accessible sur le dépôt GitHub du cours : https://github.com/SphRbtHyk/miashs_introduction_ml/tree/main. L'accès s'effectue soit par clonage du dépôt Git pour les utilisateurs familiers avec cet outil, soit par téléchargement direct avant chaque session.

L'utilisation conjointe de Jupyter et Python tout au long du semestre garantit un apprentissage pratique et interactif de l'apprentissage automatique, combinant théorie et mise en application immédiate.