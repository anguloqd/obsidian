## 07 // algo : arbres de classification

[lecture_random_forest.pdf](ressources/07_algo_arbres_de_classification_lecture_random_forest.pdf)

## Arbres de Classification et Forêts Aléatoires

### Principe Fondamental des Arbres de Décision

#### Définition et Approche Conceptuelle

Les arbres de décision constituent une approche d'apprentissage supervisé qui divise récursivement l'espace des caractéristiques en sous-ensembles selon des règles linéaires appliquées aux variables, dans le but de segmenter la population cible en classes homogènes. Cette méthode tire son nom de sa représentation graphique arborescente, où chaque nœud terminal correspond à une décision de classification et le processus décisionnel consiste à parcourir l'arbre de la racine vers les feuilles.

Les arbres de décision s'inscrivent généralement dans la famille des algorithmes CART (Classification and Regression Trees), introduite par Breiman et ses collaborateurs en 1984. Plusieurs variantes algorithmiques ont été développées, notamment CART, ID3, C4.5 et C5.0, chacune avec ses spécificités en termes de critères de division et de gestion des données.

#### Structure et Représentation

La structure arborescente présente une hiérarchie claire où chaque nœud interne représente un test sur une caractéristique, chaque branche correspond au résultat de ce test, et chaque feuille constitue une décision finale. Cette représentation offre une interprétabilité remarquable, permettant de suivre facilement le cheminement logique menant à chaque prédiction.

La construction de l'arbre repose sur une division récursive de l'espace, effectuée par une recherche gloutonne visant à identifier la division optimale qui maximise l'information obtenue à chaque étape, jusqu'à ce qu'un critère d'arrêt soit atteint.

#### Exemple Illustratif : Dataset Titanic

Dans le contexte du célèbre dataset Titanic, un arbre de décision pourrait structurer les règles de survie selon des critères comme le sexe, l'âge et le nombre de conjoints. Par exemple :

- Pour Rose (femme, 20 ans, 1 conjoint) : le parcours dans l'arbre conduirait à une prédiction de survie
- Pour Jack (homme, 23 ans, sans frère/sœur à bord) : le cheminement mènerait à une prédiction de non-survie

### Algorithme de Construction

#### Cadre Mathématique Général

L'algorithme procède récursivement jusqu'à satisfaction du critère d'arrêt en :

1. Calculant le gain d'information pour chaque caractéristique et chaque division possible
2. Sélectionnant la division qui minimise le critère choisi (impureté du nœud)

Formellement, étant donnés des vecteurs d'entraînement $x_i \in \mathbb{R}^n$ et les labels correspondants $y_i \in \mathbb{R}^l$, pour des données au nœud $Q_m$ avec $n_m$ échantillons, soit $\theta = (j, t_m)$ une division candidate sur la caractéristique $j$ avec le seuil $t_m$.

L'impureté de la division utilisant $H$ comme fonction de perte s'exprime :

$$
G(Q_m, \theta) = \frac{n_m^{left}}{n_m}H(Q_m^{left}(\theta)) + \frac{n_m^{right}}{n_m}H(Q_m^{right}(\theta))
$$

L'algorithme sélectionne alors $\theta^*$ qui minimise cette impureté.

#### Critères d'Arrêt

Les critères d'arrêt couramment utilisés incluent :

- **Nombre de nœuds terminaux** : limitation de la taille de l'arbre
- **Nombre minimum d'individus par nœud** : assurer une représentativité statistique
- **Seuil de mesure optimale** : arrêt lorsque l'amélioration devient négligeable
- **Épuisement des caractéristiques** : toutes les variables ont été utilisées ou tous les individus appartiennent à la même classe

Il convient de noter que les arbres présentent une sensibilité particulière au sur-apprentissage, nécessitant une attention particulière aux critères d'arrêt.

### Critères de Division

#### Indice de Gini

L'indice de Gini mesure la fréquence à laquelle un élément choisi aléatoirement dans l'ensemble serait incorrectement étiqueté s'il était classé aléatoirement selon la distribution des étiquettes dans le sous-ensemble. L'objectif consiste à minimiser cet indice, idéalement jusqu'à zéro.

Pour un problème de classification avec $J$ classes et des probabilités $p_i$, l'indice de Gini pour le nœud $m$ s'exprime :

$$
I_g(m) = \sum_{i=1}^{J} p_i(1-p_i) = 1 - \sum_{i=1}^{J} p_i^2
$$

**Classification binaire** : L'indice se simplifie à $I_g(m) = 1 - p_0^2 - p_1^2$

**Exemple pratique** :
- Pour $S_1 = \{\text{Légendaire, Non-légendaire, Non-légendaire}\}$ : $I_g = 1 - (\frac{1}{3})^2 - (\frac{2}{3})^2 = \frac{4}{9}$
- Pour $S_2 = \{\text{Non-légendaire, Non-légendaire, Non-légendaire, Non-légendaire}\}$ : $I_g = 0$ (pureté complète)

#### Entropie et Gain d'Information

L'entropie quantifie l'incertitude d'une distribution d'ensemble. Elle atteint son minimum (0) lorsque tous les individus sont correctement classifiés et son maximum lorsque les individus sont répartis équitablement entre les classes.

$$
\text{Entropie}(S) = -\sum_{i=1}^{J} p_i \times \log_2(p_i)
$$

avec la convention que $p_i \times \log_2(p_i) = 0$ lorsque $p_i = 0$.

**Classification binaire** : $\text{Entropie}(S) = -p_0 \times \log_2(p_0) - p_1 \times \log_2(p_1)$

Le **gain d'information** calcule le gain en entropie d'une nouvelle division par rapport à l'entropie actuelle, normalisé par le nombre d'éléments :

$$
\text{Gain}(S, \text{division}) = \text{entropie}(S) - \sum_{i=0}^{j} \frac{|S_i|}{|S|} \times \text{entropie}(S_i)
$$

#### Gestion des Variables Numériques

Les variables numériques requièrent un traitement particulier et plus coûteux computationnellement. Pour chaque division possible, l'indice choisi doit être calculé pour identifier la division optimale. Cela peut s'effectuer soit par un algorithme d'optimisation pour trouver la division, soit, si la plage de valeurs n'est pas trop large, en ordonnant les valeurs et en calculant le gain d'information à chaque étape.

### Exemple Pratique : Construction avec l'Indice de Gini

#### Dataset d'Entraînement

| Hauteur | Couleur | Label |
|---------|---------|-------|
| Court | Marron | Légendaire |
| Long | Noir | Légendaire |
| Court | Marron | Légendaire |
| Court | Noir | Non légendaire |
| Court | Marron | Non légendaire |
| Long | Noir | Non légendaire |

**Individu à classifier** : Hauteur = Court, Couleur = Noir

#### Étape 1 : Division sur la Hauteur

**Sous-ensemble "Court"** : $S_{\text{hauteur=court}} = \{\text{Légendaire, Légendaire, Non-légendaire, Non-légendaire}\}$

$$
I_g(S_{\text{hauteur=court}}) = 1 - \left(\frac{2}{4}\right)^2 - \left(\frac{2}{4}\right)^2 = \frac{1}{2}
$$

**Sous-ensemble "Long"** : $S_{\text{hauteur=long}} = \{\text{Légendaire, Non-légendaire}\}$

$$
I_g(S_{\text{hauteur=long}}) = 1 - \left(\frac{1}{2}\right)^2 - \left(\frac{1}{2}\right)^2 = \frac{1}{2}
$$

**Indice de Gini total pour la division sur hauteur** : $\frac{4}{6} \times \frac{1}{2} + \frac{2}{6} \times \frac{1}{2} = \frac{1}{2}$

#### Étape 2 : Division sur la Couleur

**Sous-ensemble "Marron"** : $S_{\text{couleur=marron}} = \{\text{Légendaire, Légendaire, Non-légendaire}\}$

$$
I_g(S_{\text{couleur=marron}}) = 1 - \left(\frac{2}{3}\right)^2 - \left(\frac{1}{3}\right)^2 = \frac{4}{9}
$$

**Sous-ensemble "Noir"** : $S_{\text{couleur=noir}} = \{\text{Légendaire, Non-légendaire, Non-légendaire}\}$

$$
I_g(S_{\text{couleur=noir}}) = 1 - \left(\frac{1}{3}\right)^2 - \left(\frac{2}{3}\right)^2 = \frac{4}{9}
$$

**Indice de Gini total pour la division sur couleur** : $\frac{3}{6} \times \frac{4}{9} + \frac{3}{6} \times \frac{4}{9} = \frac{4}{9}$

#### Décision de Division

Puisque $\frac{4}{9} < \frac{1}{2}$, l'algorithme sélectionne la division sur la couleur comme racine de l'arbre. Le processus continue récursivement avec la caractéristique restante (hauteur) sur chaque sous-ensemble jusqu'à satisfaction des critères d'arrêt.

### Élagage (Pruning)

#### Problématique du Sur-apprentissage

Les arbres de décision manifestent une tendance naturelle au sur-apprentissage, mémorisant les spécificités du jeu d'entraînement au détriment de la généralisation. L'élagage constitue une technique essentielle pour contrer ce phénomène en supprimant les sections de l'arbre considérées comme non-critiques ou redondantes.

#### Types d'Élagage

**Pré-élagage** : Établissement dès le départ de critères d'arrêt limitant la profondeur de l'arbre ou les métriques d'information.

**Post-élagage** : Après construction complète de l'arbre, suppression de nœuds et divisions n'apportant pas suffisamment d'information.

#### Élagage par Réduction d'Erreur

L'élagage par réduction d'erreur constitue l'algorithme le plus simple. Il procède de manière ascendante en supprimant chaque test individuellement. Si la précision demeure identique après suppression, le test est définitivement retiré de l'arbre.

### Hyperparamètres

Les principaux hyperparamètres des arbres de classification comprennent :

- **Critères d'arrêt** : profondeur maximale, nombre minimum d'échantillons par feuille, amélioration minimale requise
- **Critère d'information** : choix entre entropie, indice de Gini, ou autres mesures d'impureté
- **Stratégies d'élagage** : paramètres de régularisation pour contrôler la complexité de l'arbre

### Avantages et Inconvénients

#### Avantages

**Interprétabilité exceptionnelle** : La structure arborescente offre une compréhension intuitive du processus décisionnel, facilitant l'explication des prédictions aux utilisateurs non-techniques.

**Gestion naturelle des données catégorielles** : Contrairement à de nombreux algorithmes nécessitant un encodage préalable, les arbres traitent directement les variables catégorielles.

**Réduction automatique des caractéristiques** : L'algorithme sélectionne implicitement les variables les plus informatives, effectuant une sélection de caractéristiques intégrée.

**Efficacité computationnelle en prédiction** : Une fois construit, l'arbre permet des prédictions rapides sans calculs coûteux.

#### Inconvénients

**Tendance au sur-apprentissage** : Principal défaut des arbres, particulièrement problématique avec des datasets complexes ou bruités.

**Coût computationnel d'entraînement** : La construction peut être longue, spécialement avec des variables quantitatives nécessitant l'évaluation de nombreux seuils de division.

**Instabilité** : De petites modifications dans les données peuvent produire des arbres très différents.

### Forêts Aléatoires

#### Principe du Bagging

Pour contrer la tendance au sur-apprentissage des arbres individuels, la méthode des forêts aléatoires emploie une technique d'ensemble appelée bagging (bootstrap aggregating). Cette approche consiste à ré-échantillonner les données d'entraînement avec remise, construire plusieurs modèles sur ces données ré-échantillonnées, et combiner les prédictions par vote majoritaire.

#### Implémentation Pratique

Le processus de bagging s'articule autour des étapes suivantes, répétées $n$ fois :

1. **Ré-échantillonnage** : création d'un nouvel ensemble de données par tirage avec remise
2. **Construction** : entraînement d'un arbre sur ce dataset ré-échantillonné
3. **Prédiction** : pour un nouvel échantillon, interrogation des $n$ arbres différents et agrégation des réponses (possiblement pondérées selon les performances individuelles)

Cette approche d'ensemble améliore significativement la robustesse et la généralisation par rapport aux arbres individuels, tout en conservant une interprétabilité relative through l'analyse de l'importance des variables.

#### Avantages des Forêts Aléatoires

Les forêts aléatoires combinent la simplicité conceptuelle des arbres individuels avec une performance accrue grâce à l'effet d'ensemble. Elles réduisent la variance des prédictions, améliorent la généralisation, et fournissent des mesures d'importance des variables particulièrement utiles pour l'analyse exploratoire des données.

La randomisation introduite à deux niveaux (échantillonnage des observations et sélection aléatoire des variables à chaque nœud) contribue à diversifier les arbres individuels, maximisant ainsi les bénéfices de l'agrégation.
