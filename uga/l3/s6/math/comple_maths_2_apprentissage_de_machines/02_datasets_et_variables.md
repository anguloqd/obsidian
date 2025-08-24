## 02 // datasets et variables

[lecture_datasets_variables_4.pdf](ressources/02_datasets_et_variables_lecture_datasets_variables_4.pdf)

## Datasets et variables

### Introduction

L'apprentissage automatique repose fondamentalement sur l'exploitation de données structurées. Les algorithmes d'apprentissage automatique acquièrent leur capacité d'apprentissage, d'inférence et de prédiction grâce à l'analyse de datasets, qui constituent la matière première de tout système d'intelligence artificielle. La compréhension approfondie de la structure et des propriétés des datasets s'avère donc essentielle pour tout praticien de la science des données.

### Définition et structure des datasets

#### Représentation matricielle

Un dataset se conceptualise mathématiquement comme une matrice $M = (x_{i,j})_{1 \leq i \leq n, 1 \leq j \leq m}$, où $n$ représente le nombre d'individus dans la population étudiée et $m$ le nombre de variables observées. Cette structure bidimensionnelle organise l'information de manière systématique : chaque colonne correspond à une variable particulière (également appelée caractéristique ou feature), tandis que chaque ligne représente un enregistrement complet concernant un individu spécifique du dataset.

#### Organisation des données

La notation $x_{i,j}$ désigne la valeur de la variable $j$ pour l'individu $i$. Cette indexation permet de localiser précisément toute information au sein du dataset. Par exemple, dans un tableau simple :

| Individu | Variable 1 | Variable 2 | Variable 3 |
|----------|------------|------------|------------|
| ID1      | 5          | 4          | 1          |
| ID2      | 2          | 3          | 1          |

L'élément $x_{1,3} = 1$ correspond à la valeur de la troisième variable pour le premier individu, tandis que $x_{2,1} = 2$ représente la valeur de la première variable pour le second individu.

#### Exemple historique : le dataset Iris

Le dataset Iris constitue l'un des exemples les plus célèbres en apprentissage automatique. Introduit par le statisticien et biologiste britannique Ronald Fisher dans son article de 1936 "The use of multiple measurements in taxonomic problems", ce dataset illustre parfaitement les concepts fondamentaux de l'analyse de données.

| ID | Longueur sépale | Largeur sépale | Longueur pétale | Espèce     |
|----|-----------------|----------------|-----------------|------------|
| 1  | 2.1             | 3.1            | 4.1             | Setosa     |
| 2  | 3.1             | 1.1            | 2.1             | Setosa     |
| 3  | 4.1             | 5.1            | 3.1             | Versicolor |
| 4  | 1.1             | 2.1            | 2.1             | Virginica  |

Ce dataset comprend 4 individus (fleurs d'iris) et 4 variables (longueur des sépales, largeur des sépales, longueur des pétales, et espèce). Il s'agit d'un problème de classification supervisée où l'objectif consiste à prédire l'espèce d'une fleur d'iris à partir de ses caractéristiques morphologiques.

### Types de variables

#### Classification générale

Dans un dataset $M = (x_{i,j})_{1 \leq i \leq n, 1 \leq j \leq m}$ comportant $n$ individus et $m$ variables, chaque variable $j$ peut appartenir à l'une des catégories suivantes :

##### Variables numériques

Les variables numériques vérifient $(x_{i,j})_{1 \leq i \leq n} \in \mathbb{R}^n$, c'est-à-dire que leurs valeurs appartiennent à l'ensemble des nombres réels. Ces variables permettent des opérations arithmétiques et des comparaisons d'ordre. La largeur des pétales dans le dataset Iris exemplifie ce type de variable, où des valeurs comme 2.1, 3.1, ou 4.1 centimètres peuvent être additionnées, soustraites ou comparées de manière significative.

##### Variables catégorielles

Les variables catégorielles satisfont $(x_{i,j})_{1 \leq i \leq n} \in X^n$, où $X$ représente un ensemble de valeurs distinctes sans ordre intrinsèque. L'espèce de fleur dans le dataset Iris illustre cette catégorie : les valeurs "Setosa", "Versicolor" et "Virginica" constituent des étiquettes distinctes sans relation d'ordre naturelle entre elles.

##### Variables ordinales

Les variables ordinales constituent un cas particulier des variables catégorielles où $(x_{i,j})_{1 \leq i \leq n} \in X^n$, avec $X$ un ensemble de valeurs distinctes ordonnées. Une variable de performance évaluée selon les niveaux "faible", "moyen", "élevé" exemplifie cette catégorie, car elle combine l'aspect catégoriel avec une relation d'ordre significative.

### Analyse des datasets

#### Approches d'analyse

L'analyse d'un dataset s'articule autour de deux approches complémentaires :

- **Analyse visuelle** : exploitation de représentations graphiques pour comprendre intuitivement la structure et les propriétés des données
- **Analyse statistique** : utilisation d'estimateurs statistiques pour quantifier les caractéristiques des données

L'efficacité de l'analyse dépend crucially du type de variables concernées. Une analyse inappropriée peut conduire à des interprétations erronées des données, compromettant ainsi la qualité des modèles d'apprentissage automatique développés.

#### Analyse des variables numériques

##### Indicateurs statistiques fondamentaux

Les variables numériques bénéficient d'un arsenal riche d'indicateurs statistiques :

**Moyenne arithmétique** : synthétise la tendance centrale des données

$$
\bar{X} = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

**Variance et écart-type** : quantifient la dispersion des données autour de la moyenne

$$
\text{var}(X) = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{X})^2
$$

$$
\sigma(X) = \sqrt{\text{var}(X)}
$$

**Quantiles** : divisent la distribution ordonnée en parties égales. Les quartiles (quantiles d'ordre 1/4) et la médiane s'avèrent particulièrement utiles pour les datasets contenant de nombreuses valeurs aberrantes (outliers), car ces indicateurs résistent mieux à l'influence de valeurs extrêmes que la moyenne arithmétique.

##### Représentations graphiques

**Histogrammes** : construits en divisant l'espace numérique en intervalles de longueur régulière puis en calculant la fréquence des valeurs par intervalle. Cette représentation révèle la forme de la distribution des données et permet d'identifier d'éventuelles multimodalités ou asymétries.

**Boîtes à moustaches (boxplots) et graphiques en violon** : représentent simultanément toutes les valeurs de la variable ainsi que leurs indicateurs statistiques, notamment les quantiles et la médiane. Ces visualisations facilitent l'identification des valeurs aberrantes et la comparaison de distributions entre différents groupes.

#### Analyse des variables catégorielles

##### Défis spécifiques

Les variables catégorielles présentent des défis analytiques particuliers car elles ne supportent pas les opérations arithmétiques classiques. L'analyse se concentre donc sur l'étude des patterns de distribution et des associations entre catégories.

##### Indicateurs statistiques

Les indicateurs principaux pour les variables catégorielles incluent :

- **Comptages** : nombre d'occurrences de chaque catégorie
- **Fréquences** : proportions relatives de chaque catégorie par rapport au total

##### Représentations graphiques

Les **graphiques en barres** constituent la représentation visuelle standard pour les variables catégorielles. Ils permettent de comparer visuellement les fréquences des différentes catégories et d'identifier les modalités dominantes ou rares dans le dataset.

### Importance de l'analyse préliminaire

La qualité de l'analyse préliminaire des variables conditionne directement la pertinence des algorithmes d'apprentissage automatique appliqués ultérieurement. Une compréhension approfondie de la nature et des propriétés des variables permet de :

- Choisir les algorithmes les mieux adaptés aux types de données disponibles
- Détecter et traiter les valeurs manquantes ou aberrantes
- Identifier les transformations nécessaires avant l'application des modèles
- Évaluer la qualité et la complétude du dataset

Cette étape d'exploration et d'analyse constitue donc un préalable indispensable à tout projet d'apprentissage automatique réussi.
