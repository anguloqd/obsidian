## 04 // apprentissage supervisé

[lecture_supervised_learning.pdf](ressources/04_apprentissage_supervise_lecture_supervised_learning.pdf)

[lecture_sklearn.pdf](ressources/04_apprentissage_supervise_lecture_sklearn.pdf)

[survey_ml_algorithms.pdf](ressources/04_apprentissage_supervise_survey_ml_algorithms.pdf)

[survey_hyperparameters.pdf](ressources/04_apprentissage_supervise_survey_hyperparameters.pdf)

## Apprentissage supervisé - Méthodologie et outils

### Introduction

L'apprentissage supervisé constitue une approche fondamentale de l'intelligence artificielle qui vise à identifier une fonction capable de projeter des vecteurs d'entrée vers des étiquettes en se basant sur des paires d'exemples entrée-sortie. Cette méthode s'oppose aux approches expertes traditionnelles en adoptant une démarche automatique de découverte de motifs au sein des données pour prendre des décisions concernant de nouvelles observations.

Dans le cadre de ce cours, l'accent porte sur les problèmes discrets de prédiction de variables catégorielles, communément appelés **problèmes de classification**. Ces problèmes consistent à assigner chaque observation à une classe prédéfinie parmi un ensemble fini de catégories possibles.

### Contexte et approches

#### Approches de résolution

Deux approches principales permettent de résoudre les problèmes de prédiction. L'**approche experte** s'appuie sur les connaissances du domaine pour construire manuellement des règles de décision. L'**approche automatique** identifie des motifs dans les données et utilise ces motifs pour prendre des décisions concernant de nouvelles observations.

L'apprentissage supervisé s'inscrit dans cette seconde approche en recherchant une fonction qui projette des vecteurs d'entrée vers des étiquettes basées sur des paires d'exemples entrée-sortie observées.

### Méthodologie de l'apprentissage supervisé

#### Formalisation mathématique

La méthodologie de l'apprentissage supervisé suit une approche formalisée. Chaque individu $i$ est représenté par un tuple $(X_i, y_i)$, où $X_i \in \mathbb{R}^d$ correspond au vecteur de caractéristiques et $y_i \in Y = \{1, …, K\}$ représente l'étiquette de classe.

L'objectif consiste à définir une fonction $f$ associant chaque $X_i$ à une étiquette : $f(X_i) \in Y$.

#### Processus d'apprentissage

Le processus d'apprentissage supervisé comprend trois étapes fondamentales :

1. **Construction d'un ensemble d'exemples** : Cette étape consiste à rassembler les données décrivant les individus (variables explicatives) et leurs étiquettes correspondantes (variable cible) qui constituent la vérité terrain.

2. **Construction d'une fonction de projection** : L'algorithme identifie une fonction capable de projeter ces données vers la vérité terrain en découvrant les relations sous-jacentes.

3. **Évaluation des performances** : La qualité de la méthode est mesurée soit sur l'ensemble d'exemples d'apprentissage, soit sur des données distinctes (ensemble de test).

#### Exemple d'application

L'illustration de cette méthodologie peut s'appuyer sur la prédiction du caractère légendaire des Pokémon. Les variables explicatives incluent les statistiques de combat, les types, et autres caractéristiques mesurables, tandis que la variable cible binaire indique si le Pokémon est légendaire ou non.

### Évaluation des modèles

#### Métriques d'évaluation

L'évaluation objective de la qualité des modèles d'apprentissage nécessite des métriques standardisées. Ces métriques s'appuient généralement sur la **matrice de confusion**, un tableau spécifique permettant de visualiser les performances d'un algorithme de classification.

#### Matrice de confusion

La matrice de confusion organise les résultats où chaque ligne représente les instances de la classe prédite tandis que chaque colonne représente les instances de la classe réelle. Cette représentation facilite l'identification des erreurs de classification et révèle quand l'algorithme est "confus" entre certaines classes.

Pour un problème de classification binaire, la matrice de confusion se décompose en quatre catégories :

- **Vrais positifs (TP)** : Observations correctement classées comme positives
- **Vrais négatifs (TN)** : Observations correctement classées comme négatives
- **Faux positifs (FP)** : Observations incorrectement classées comme positives
- **Faux négatifs (FN)** : Observations incorrectement classées comme négatives

#### Métriques de performance

Plusieurs métriques standardisées découlent de la matrice de confusion :

**Exactitude (Accuracy)** : Proportion de résultats corrects parmi le nombre total de cas examinés.

$$
\text{Exactitude} = \frac{TP + TN}{TP + FP + FN + TN}
$$

**Précision** : Proportion de prédictions positives qui sont effectivement positives.

$$
\text{Précision} = \frac{TP}{TP + FP}
$$

**Rappel (Recall)** : Proportion de positifs réels correctement classifiés.

$$
\text{Rappel} = \frac{TP}{TP + FN}
$$

**Score F1** : Moyenne harmonique de la précision et du rappel.

$$
F_1 = 2 \times \frac{\text{précision} \times \text{rappel}}{\text{précision} + \text{rappel}}
$$

#### Choix des métriques

Le choix de la métrique appropriée dépend du contexte applicatif. Dans certaines situations, il peut être préférable de favoriser le rappel plutôt que la précision ou vice versa. Par exemple, en diagnostic médical, un rappel élevé peut être prioritaire pour éviter de manquer des cas positifs, même au prix de quelques faux positifs supplémentaires.

### Surapprentissage

#### Définition du surapprentissage

Le **surapprentissage** représente un phénomène où il est toujours possible de construire une fonction qui correspond exactement aux données d'apprentissage, mais cela ne garantit pas une bonne généralisation. Il n'est donc pas toujours souhaitable d'obtenir un ajustement parfait où $f(X_i) = y_i$ pour tous les $i$ de l'ensemble d'apprentissage.

Ce phénomène révèle une tension fondamentale entre la performance sur les données d'apprentissage et la capacité de généralisation à de nouvelles observations non vues durant l'apprentissage.

### Compromis biais-variance

#### Concepts fondamentaux

La sélection de l'algorithme approprié implique un **compromis biais-variance** qui influence directement les performances de généralisation.

L'**erreur de biais** provient d'hypothèses erronées dans l'algorithme d'apprentissage. Un biais élevé indique que l'algorithme n'apprend pas suffisamment à partir du jeu de données, conduisant à un sous-ajustement.

L'**erreur de variance** résulte de la sensibilité aux petites fluctuations dans l'ensemble d'apprentissage. Une variance élevée signifie que l'algorithme apprend le bruit présent dans les données, conduisant au surapprentissage.

#### Équilibrage du compromis

L'art de l'apprentissage supervisé réside dans l'identification de l'équilibre optimal entre ces deux sources d'erreur pour maximiser la performance de généralisation sur de nouvelles données.

### Ensembles d'apprentissage et de test

#### Principe de séparation

Puisqu'un ajustement parfait à 100% sur l'ensemble d'apprentissage n'est pas toujours le signe d'un bon modèle, la sélection du meilleur modèle nécessite une approche différente.

La solution standard consiste à diviser le jeu de données en deux ensembles distincts :

- **Ensemble d'apprentissage** : Utilisé pour construire le modèle
- **Ensemble de test** : Utilisé pour tester le modèle et calculer les métriques de performance

#### Considérations pratiques

Cette approche soulève des questions importantes concernant la représentativité de la division et la stratification des classes pour maintenir des proportions similaires dans les deux ensembles.

### Validation croisée

#### Principe de la validation croisée

La **validation croisée** constitue une méthode de rééchantillonnage qui utilise différentes portions des données pour tester et entraîner un modèle à travers différentes itérations, afin d'estimer la précision avec laquelle un modèle prédictif performera en pratique.

#### Validation croisée k-fold

L'approche populaire de **validation croisée k-fold** divise le jeu de données en $k$ sous-ensembles, entraîne sur $k-1$ sous-ensembles, évalue sur le $k$-ième sous-ensemble, répète ce processus pour tous les sous-ensembles, puis agrège les scores de performance.

Cette méthode fournit une estimation plus robuste des performances du modèle en réduisant la dépendance à une division particulière des données.

### Sélection des hyperparamètres

#### Définition des hyperparamètres

La plupart des algorithmes possèdent des **hyperparamètres**, qui sont des paramètres conditionnant le comportement des algorithmes. Ces paramètres doivent être optimisés pour chaque cas d'usage spécifique.

#### Méthodes d'optimisation

L'approche simpliste utilise un plan factoriel complet avec validation croisée k-fold pour tester toutes les combinaisons possibles d'hyperparamètres. D'autres solutions plus sophistiquées incluent les algorithmes génétiques et le recuit simulé.

Il est crucial de rester vigilant concernant le surapprentissage lors de l'optimisation des hyperparamètres, car une optimisation excessive peut conduire à des modèles qui performent bien sur les données de validation mais généralisent mal.

### Algorithmes d'apprentissage supervisé

#### Diversité algorithmique

La littérature propose de nombreux algorithmes d'apprentissage supervisé, chacun avec ses avantages et inconvénients selon le contexte applicatif. Les algorithmes principaux étudiés dans ce cours incluent :

- **k-plus proches voisins** : Algorithme basé sur l'instance qui classifie selon la majorité des k voisins les plus proches
- **Naïve Bayes** : Méthode probabiliste basée sur le théorème de Bayes avec l'hypothèse d'indépendance conditionnelle
- **Arbres de classification** : Méthodes hiérarchiques qui divisent récursivement l'espace des variables

## Introduction à Scikit-learn

### Présentation de la bibliothèque

#### Scikit-learn : référence en apprentissage automatique

**Scikit-learn**, communément appelé **sklearn**, constitue une bibliothèque incontournable pour l'apprentissage automatique en Python. Cette bibliothèque fournit une large gamme d'outils pour diverses tâches d'apprentissage automatique, incluant la classification, la régression, le clustering, et bien d'autres applications.

#### Historique et développement

Scikit-learn trouve ses origines dans le projet Google Summer of Code de 2007. La bibliothèque est développée et maintenue par une communauté diverse de contributeurs à travers le monde, avec un développement actif sur GitHub et des contributions continues de chercheurs, développeurs et data scientists.

#### Fonctionnalités principales

La bibliothèque propose deux éléments fondamentaux : une **API standard facile à utiliser** et l'**implémentation de la plupart des algorithmes d'apprentissage automatique**. Cette combinaison en fait un outil de référence pour les praticiens du domaine.

### Avantages de Scikit-learn

#### Documentation et accessibilité

Scikit-learn se distingue par sa **documentation extensive** avec des guides complets et des exemples pour une utilisation efficace. Cette richesse documentaire facilite l'adoption par les nouveaux utilisateurs et sert de référence pour les praticiens expérimentés.

#### Diversité algorithmique

La bibliothèque supporte une **large gamme d'algorithmes** couvrant diverses tâches d'apprentissage automatique : classification, régression, clustering, et réduction de dimensionnalité. Cette diversité permet de répondre à la plupart des besoins pratiques avec un seul outil.

#### API cohérente

L'**API cohérente** de Scikit-learn facilite la transition entre différents algorithmes avec un workflow uniforme. Cette standardisation permet aux utilisateurs de se concentrer sur l'expérimentation algorithmique plutôt que sur l'apprentissage de multiples interfaces.

#### Communauté active

La **communauté active** de développeurs, chercheurs et data scientists contribue régulièrement, maintenant la bibliothèque à l'état de l'art des développements récents en apprentissage automatique.

#### Intégration écosystémique

L'**intégration avec d'autres bibliothèques** assure une interaction fluide avec NumPy, SciPy, et matplotlib, s'inscrivant naturellement dans l'écosystème PyData.

#### Optimisation des performances

Les **optimisations de performance** via des implémentations C et Cython garantissent des calculs efficaces même sur de grands jeux de données.

#### Fonctionnalités complètes

Scikit-learn inclut **toutes les étapes usuelles de la science des données** : support intégré pour la validation croisée et l'évaluation de modèles, sélection de variables et prétraitement des données, facilitant le workflow complet d'un projet d'apprentissage automatique.

#### Nature open source

Le caractère **open source** rend la bibliothèque librement disponible et modifiable, encourageant la collaboration et l'innovation dans la communauté.

### Workflow standard

#### Processus Créer, Entraîner, Évaluer, Prédire

Le workflow typique de Scikit-learn suit quatre étapes standardisées :

**Constructeur** : Initialisation du modèle avec les hyperparamètres souhaités. Cette étape configure les paramètres qui contrôlent le comportement de l'algorithme.

**Fit** : Entraînement du modèle sur les données d'apprentissage. Cette phase ajuste les paramètres du modèle en utilisant les données d'entraînement fournies.

**Evaluate** : Évaluation des performances du modèle sur l'ensemble d'entraînement. Cette étape évalue la qualité de l'apprentissage réalisé par le modèle.

**Predict** : Application du modèle entraîné pour faire des prédictions sur de nouvelles données. Cette phase utilise les motifs appris pour prédire les résultats sur des instances non vues.

#### Exemple pratique

```python
# Créer le modèle
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer sur l'ensemble d'entraînement
training_accuracy = model.score(X_train, y_train)

# Prédire sur de nouvelles données
predictions = model.predict(X_test)
```

### Catalogue des modèles disponibles

#### Modèles linéaires

Les **modèles linéaires** forment une famille fondamentale d'algorithmes incluant :

- **LinearRegression** : Régression linéaire classique
- **Ridge** : Régression avec régularisation L2
- **Lasso** : Régression avec régularisation L1
- **ElasticNet** : Régression avec régularisation mixte L1/L2
- **LogisticRegression** : Régression logistique pour la classification
- **SGDClassifier** : Classification par descente de gradient stochastique

#### k-plus proches voisins

Les algorithmes de **k-plus proches voisins** comprennent :

- **KNeighborsClassifier** : Classification par k-NN
- **KNeighborsRegressor** : Régression par k-NN

#### Machines à vecteurs de support

Les **machines à vecteurs de support** offrent :

- **SVC** : Classification par vecteurs de support
- **NuSVC** : Variante Nu-SVM pour la classification
- **SVR** : Régression par vecteurs de support
- **NuSVR** : Variante Nu-SVM pour la régression

#### Modèles basés sur les arbres

Les **modèles basés sur les arbres** incluent :

- **DecisionTreeClassifier** : Arbre de décision pour la classification
- **DecisionTreeRegressor** : Arbre de décision pour la régression
- **RandomForestClassifier** : Forêt aléatoire pour la classification
- **RandomForestRegressor** : Forêt aléatoire pour la régression

#### Clustering

Les algorithmes de **clustering** proposent :

- **KMeans** : Clustering k-moyennes
- **MiniBatchKMeans** : Version mini-batch de k-moyennes
- **DBSCAN** : Clustering basé sur la densité
- **AgglomerativeClustering** : Clustering hiérarchique agglomératif

#### Réduction de dimensionnalité

La **réduction de dimensionnalité** est supportée par :

- **PCA** : Analyse en composantes principales
- **TruncatedSVD** : Décomposition en valeurs singulières tronquée

#### Méthodes d'ensemble

Les **méthodes d'ensemble** combinent plusieurs modèles :

- **VotingClassifier** : Classification par vote
- **VotingRegressor** : Régression par vote
- **BaggingClassifier** : Classification par bagging
- **BaggingRegressor** : Régression par bagging

Cette richesse algorithmique fait de Scikit-learn un outil complet pour la plupart des tâches d'apprentissage automatique, avec une interface unifiée facilitant l'expérimentation et la comparaison de différentes approches.
