## 13 // sélection de features : PCA et t-SNE

[feature_engineering.pdf](ressources/13_selection_de_features_pca_et_t_sne_feature_engineering.pdf)

[lecture_dimensionality_reduction.pdf](ressources/13_selection_de_features_pca_et_t_sne_lecture_dimensionality_reduction.pdf)

[lecture_feature_selection_2.pdf](ressources/13_selection_de_features_pca_et_t_sne_lecture_feature_selection_2.pdf)

[lecture_feature_projection.pdf](ressources/13_selection_de_features_pca_et_t_sne_lecture_feature_projection.pdf)

## Réduction de dimensionnalité et sélection de variables

### Introduction

La réduction de dimensionnalité constitue une transformation des données depuis un espace de grande dimension vers un espace de dimension inférieure, avec une perte d'information aussi faible que possible. Cette approche vise simultanément à réduire le nombre de variables tout en conservant autant d'information que possible des données originales.

Cette problématique s'impose naturellement dans de nombreux contextes d'apprentissage automatique où les jeux de données présentent un grand nombre de variables, rendant l'analyse et le traitement complexes tant d'un point de vue computationnel que conceptuel.

### Motivations pour la réduction de dimensionnalité

#### Problèmes liés à la haute dimensionnalité

Plusieurs facteurs justifient la nécessité de réduire la dimensionnalité des données. Le **temps de calcul** représente un enjeu majeur, car la complexité algorithmique croît généralement avec le nombre de dimensions, rendant les traitements prohibitifs sur de grands jeux de données.

La **visualisation des données** devient également problématique au-delà de trois dimensions, limitant les capacités d'exploration et de compréhension des structures sous-jacentes. Cette limitation entrave l'analyse exploratoire et l'interprétation des résultats.

Les **variables non pertinentes** peuvent agir comme du bruit, dégradant les performances des algorithmes d'apprentissage. De même, les **variables corrélées** n'apportent pas d'information nouvelle pour résoudre la tâche d'apprentissage, créant de la redondance sans valeur ajoutée.

#### Le fléau de la dimensionnalité

Le **fléau de la dimensionnalité** (curse of dimensionality) désigne divers phénomènes qui apparaissent lors de l'analyse de données dans un espace de grande dimension. Le problème principal réside dans le fait que le jeu de données devient sparse : il n'existe pas suffisamment de combinaisons de valeurs pour permettre un apprentissage efficace.

Ce phénomène se manifeste par une dégradation des performances des algorithmes, une augmentation des besoins en données pour maintenir une densité statistique suffisante, et une perte de discriminabilité entre les observations dans l'espace de grande dimension.

### Méthodes de réduction de dimensionnalité

Deux approches principales permettent de réduire le nombre de variables : l'**élimination directe de variables** (sélection de variables) et la **projection des variables** dans un espace de dimension inférieure (extraction de variables).

#### Sélection de variables

La sélection de variables consiste à identifier le sous-ensemble de variables qui porte le plus d'information pertinente pour la tâche d'apprentissage, puis à ne conserver que ces variables dans le jeu de données final. Cette approche préserve l'interprétabilité des variables originales puisqu'elle ne les transforme pas.

#### Extraction de variables par projection

L'extraction de variables, également appelée projection de variables, transforme les données depuis l'espace de grande dimension vers un espace de dimensions réduites. Cette transformation nécessite de projeter les données dans un nouvel espace qui constitue une combinaison des variables originales, avec une perte d'information minimale.

Les transformations peuvent être **linéaires** (comme l'Analyse en Composantes Principales, la Factorisation Matricielle Non-négative) ou **non-linéaires** (comme t-SNE ou UMAP). Le choix entre ces approches dépend de la nature des relations entre les variables et des objectifs de l'analyse.

## Sélection de variables

### Définition et approches

La sélection de variables consiste à identifier le sous-ensemble de variables qui porte le plus d'information pour la tâche d'apprentissage et à n'utiliser que celles-ci pour la résolution du problème. Cette approche peut s'appuyer sur plusieurs stratégies complémentaires.

Les **connaissances expertes du domaine** permettent d'identifier a priori les variables pertinentes en se basant sur la compréhension métier du problème. Les **règles automatiques basées sur des métriques objectives** offrent une approche systématique et reproductible. Enfin, l'**intégration dans l'algorithme lui-même** permet d'incorporer la sélection comme étape du processus de traitement des données.

#### Types de variables problématiques

Les variables peuvent présenter deux types de problèmes principaux. Les variables **redondantes** fournissent une information déjà donnée par d'autres variables en raison de corrélations élevées (par exemple, l'heure d'arrivée tardive et l'heure de départ tardive). Les variables **non pertinentes** n'apportent aucune information utile pour la tâche considérée (par exemple, les conditions météorologiques pour la reconnaissance d'images).

#### Classification des approches

Les approches de sélection se divisent en deux catégories principales. Les **méthodes basées sur des filtres** ignorent le modèle d'apprentissage et sélectionnent un sous-ensemble de variables selon des critères intrinsèques aux données. Les **méthodes basées sur des enveloppes** (wrapper methods) construisent itérativement un modèle avec un sous-ensemble de variables et sélectionnent celui présentant les meilleures performances selon un score d'apprentissage.

### Approches basées sur des filtres

#### Sélection par seuil de variance

La sélection par seuil de variance constitue une méthode simple consistant à éliminer les variables présentant une faible variance. En pratique, cette approche nécessite de définir un seuil minimal de variance (en gardant à l'esprit les biais potentiels) puis d'éliminer toutes les variables ne respectant pas ce critère.

Cette méthode présente l'avantage d'être **indépendante du modèle** et de présenter un **risque limité de surapprentissage**. Cependant, elle ne tient pas compte des **corrélations entre variables**, ce qui peut conduire à éliminer des variables individuellement peu informatives mais collectivement pertinentes.

### Approches basées sur des enveloppes

#### Principe des méthodes wrapper

La sélection basée sur des enveloppes, également appelée sélection basée sur un modèle, consiste à construire itérativement un modèle sur un sous-ensemble de variables et à sélectionner le sous-ensemble présentant les meilleures performances.

#### Stratégies de sélection

La sélection peut suivre deux stratégies principales. L'approche **progressive** (forward) démarre sans aucune variable et ajoute à chaque itération celle qui maximise le score de performance. L'approche **régressive** (backward) démarre avec l'ensemble complet des variables et retire à chaque itération celle qui maximise le score après suppression.

L'algorithme s'arrête lorsqu'un seuil de performance est atteint ou qu'aucune amélioration significative n'est observée lors des itérations suivantes.

#### Avantages et limites

Les méthodes wrapper présentent l'avantage de **prendre en compte la spécificité de la tâche d'apprentissage** et les **corrélations entre variables**. Elles sont cependant **dépendantes du modèle** utilisé et les corrélations identifiées **dépendent du sous-ensemble** considéré, ce qui peut conduire à des solutions sous-optimales selon le contexte.

## Extraction de variables

### Analyse en composantes principales (PCA)

#### Principe fondamental

L'Analyse en Composantes Principales constitue une méthode de projection de variables consistant à identifier un nouveau système de coordonnées comme combinaison linéaire des variables d'entrée. Ce système orthogonal représente une combinaison linéaire des variables qui maximise la variance des données projetées.

L'objectif de l'ACP vise à identifier de **nouveaux axes plus pertinents** pour représenter les données, à **quantifier l'importance** de chaque axe, et à **éliminer les axes peu importants** pour réduire la dimensionnalité.

#### Fondements mathématiques

La recherche de nouveaux axes maximisant la variance et non corrélés peut être formalisée mathématiquement. Il peut être démontré que ces composantes principales correspondent aux vecteurs propres de la **matrice de covariance** (ACP centrée) ou de la **matrice de corrélation** (ACP normée) des données.

#### Algorithme détaillé

L'algorithme de l'ACP suit plusieurs étapes systématiques, illustrées ici sur le jeu de données Iris :

##### Standardisation des données

Pour une ACP centrée, les données sont centrées autour de leur moyenne. Pour une ACP normée, les données sont standardisées (moyenne nulle et écart-type unitaire) pour obtenir la matrice $Z$.

##### Calcul de la matrice de corrélation

La matrice de corrélation $C$ est calculée selon la formule :

$$
C = \frac{1}{n} Z^t Z
$$

où $Z$ représente la matrice standardisée et $n$ le nombre d'individus dans le jeu de données.

Pour l'exemple du jeu de données Iris :

| Variable | Sepal length | Width | Petal length |
|----------|--------------|--------|--------------|
| Sepal length | 1.00 | 0.79 | 0.60 |
| Width | 0.79 | 1.00 | 0.52 |
| Petal length | 0.60 | 0.52 | 1.00 |

##### Calcul des valeurs et vecteurs propres

Les valeurs propres (triées par ordre décroissant) de la matrice de corrélation sont : $[2.27, 0.51, 0.20]$.

La matrice des vecteurs propres $P$ (triés selon les valeurs propres) est :

| Variable | Composante 0 | Composante 1 | Composante 2 |
|----------|--------------|--------------|--------------|
| S. length | 0.61 | -0.26 | 0.75 |
| Width | 0.59 | -0.48 | -0.65 |
| P. length | 0.53 | 0.84 | -0.14 |

##### Projection dans le nouvel espace

La projection des individus dans le nouvel espace s'obtient en multipliant la matrice standardisée $Z$ par la matrice des vecteurs propres : $Z^* = ZP$.

| ID | Composante 0 | Composante 1 | Composante 2 |
|----|--------------|--------------|--------------|
| 0 | 0.66 | -0.95 | 0.30 |
| 1 | -0.80 | 0.07 | 0.87 |
| 2 | -1.35 | -0.90 | 0.02 |
| 3 | -0.74 | 1.00 | -0.31 |
| 4 | 0.64 | -1.02 | -0.20 |
| 5 | 3.68 | 0.57 | -0.20 |
| 6 | -0.65 | -0.31 | -0.83 |
| 7 | 0.75 | 0.13 | 0.11 |
| 8 | -2.11 | 0.70 | -0.26 |
| 9 | -0.08 | 0.72 | 0.51 |

##### Sélection du nombre d'axes

L'importance de chaque axe correspond à sa valeur propre et permet de sélectionner le nombre d'axes à conserver selon le pourcentage de variance expliquée. La somme cumulée des rapports $\frac{\lambda_i}{\sum_{j=0}^{n} \lambda_j}$ pour la $i$-ème valeur propre $\lambda_i$ donne la variance totale expliquée.

Pour cet exemple, la somme cumulée est $[0.76, 0.93, 1]$, conduisant à sélectionner deux axes qui expliquent 93% de la variance.

##### Projection finale

La projection finale conserve uniquement les composantes sélectionnées :

| ID | Composante 0 | Composante 1 |
|----|--------------|--------------|
| 0 | 0.66 | -0.95 |
| 1 | -0.80 | 0.07 |
| 2 | -1.35 | -0.90 |
| 3 | -0.74 | 1.00 |
| 4 | 0.64 | -1.02 |
| 5 | 3.68 | 0.57 |
| 6 | -0.65 | -0.31 |
| 7 | 0.75 | 0.13 |
| 8 | -2.11 | 0.70 |
| 9 | -0.08 | 0.72 |

#### Interprétation des résultats

L'interprétation des résultats s'appuie sur le **cercle des corrélations**, qui consiste à calculer la corrélation des variables originales avec les nouvelles composantes pour déduire la contribution de chaque variable aux axes principaux.

#### Avantages et inconvénients

L'ACP présente l'avantage d'être **simple à implémenter** et de permettre une **évaluation aisée de la perte de données** due à la transformation. Cependant, les **variables transformées perdent leur interprétabilité** et la méthode est **sensible aux valeurs aberrantes**.

### t-SNE (t-distributed Stochastic Neighbor Embedding)

#### Principe fondamental

t-SNE constitue une méthode de réduction de dimensionnalité non-linéaire qui associe à chaque paire d'individus une probabilité d'être proches dans le nouvel espace en s'appuyant sur une distribution de probabilité dans l'espace original.

Étant donnée une matrice $X$ avec $k$ individus et $n$ variables, l'objectif consiste à identifier une matrice $Q$ avec $k$ individus et $d$ variables, où $d \ll n$.

#### Distributions de probabilité

La méthode nécessite deux distributions de probabilité complémentaires :

- $p_{ij}$ : mesure la similarité entre les individus dans l'espace initial
- $q_{ij}$ : mesure la similarité entre les individus dans le nouvel espace

L'objectif consiste à minimiser la divergence entre ces distributions de probabilité.

#### Divergence de Kullback-Leibler

La divergence de Kullback-Leibler constitue une mesure de similarité statistique qui quantifie la différence entre une distribution de probabilité $P$ et une distribution $Q$ :

$$
D_{KL}(P||Q) = \sum_{x \in X} P(x) \log \left( \frac{P(x)}{Q(x)} \right)
$$

Dans le cas de t-SNE, l'objectif consiste à minimiser :

$$
KL(P||Q) = \sum_{i \neq j} p_{ij} \log \left( \frac{p_{ij}}{q_{ij}} \right)
$$

#### Définition des distributions

Dans l'espace original, la probabilité conditionnelle que $j$ soit le voisin de $i$ suit une gaussienne centrée sur $x_i$ :

$$
p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}
$$

où $\sigma_i$ mesure la densité autour de $x_i$ et doit être estimé. La probabilité jointe est définie par :

$$
p_{ij} = \frac{p_{j|i} + p_{i|j}}{2N}
$$

Dans le nouvel espace dimensionnel, une loi de Student à queues lourdes est utilisée :

$$
q_{ij} = \frac{(1 + \|q_i - q_j\|^2)^{-1}}{\sum_k \sum_{l \neq k} (1 + \|q_k - q_l\|^2)^{-1}}
$$

L'optimisation utilise la descente de gradient pour minimiser la divergence KL.

#### Exemple d'application

L'application de t-SNE au jeu de données Iris démontre sa capacité à révéler des structures non-linéaires que l'ACP peut manquer. Les projections en 2D obtenues par t-SNE et PCA montrent des différences notables dans la séparation des classes et la préservation des structures locales.

#### Avantages et inconvénients

t-SNE présente plusieurs avantages significatifs : les visualisations sont **généralement plus esthétiques** que celles de l'ACP et la méthode peut **identifier des motifs non-linéaires** dans les données.

Cependant, elle présente des limitations importantes : elle nécessite de nombreux **hyperparamètres**, ne **préserve que la structure locale** des données, produit des **résultats stochastiques**, **ne passe pas à l'échelle** efficacement sur de grands jeux de données, est **difficile à interpréter** et **ne crée pas de nouvelles variables compréhensibles** pour les analyses ultérieures.

Ces caractéristiques font de t-SNE un outil principalement adapté à la visualisation exploratoire plutôt qu'à la transformation de données pour des tâches d'apprentissage automatique en aval.
