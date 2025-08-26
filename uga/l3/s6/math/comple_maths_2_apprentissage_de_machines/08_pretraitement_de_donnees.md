## 08 //  prétraitement de données

[lecture_extra_preprocessing.pdf](ressources/08_pretraitement_de_donnees_lecture_extra_preprocessing.pdf)

## Préprocessing des données

### Introduction

Le préprocessing des données constitue une étape fondamentale dans tout projet d'apprentissage automatique. En pratique, la majeure partie du travail en science des données consiste à nettoyer et préparer les jeux de données. Cette phase va au-delà de la simple exploration visuelle et des estimateurs statistiques pour optimiser les performances des modèles.

Trois problématiques principales nécessitent un préprocessing avancé : la gestion des valeurs manquantes, la mise à l'échelle des variables (feature scaling), et la suppression des valeurs aberrantes. Chacune de ces étapes peut significativement impacter la qualité et la robustesse des modèles d'apprentissage automatique.

### Gestion des valeurs manquantes

#### Classification des valeurs manquantes

La typologie des valeurs manquantes, établie par Rubin en 1976, distingue trois catégories fondamentales qui déterminent la stratégie de traitement appropriée.

##### Données manquantes complètement aléatoirement (MCAR)

Les données sont considérées comme Missing Completely at Random (MCAR) lorsque la probabilité qu'une observation soit manquante reste identique pour l'ensemble des observations du jeu de données. Cette situation se produit typiquement lors de dysfonctionnements d'instruments de mesure, où l'absence de données résulte d'un problème technique indépendant de la nature des observations.

##### Données manquantes aléatoirement (MAR)

Le mécanisme Missing at Random (MAR) caractérise les situations où la probabilité de valeurs manquantes dépend de variables observées dans le jeu de données. Par exemple, dans une enquête, un participant peut être moins susceptible de répondre à la question 2 s'il n'a pas répondu à la question 1. De même, certaines mesures peuvent être absentes en fonction de variables socio-économiques observables.

##### Données manquantes non aléatoirement (MNAR)

Les données Missing Not at Random (MNAR) présentent une probabilité de valeurs manquantes qui dépend de variables non observées. Cette situation complexifie considérablement le traitement car le processus génératif des valeurs manquantes demeure inconnu. L'exemple typique concerne un participant à une enquête qui refuse de répondre à une question en raison de son genre, information qui n'est pas collectée dans l'étude.

#### Stratégies de traitement des valeurs manquantes

##### Suppression des valeurs manquantes

La suppression pure et simple des observations ou des variables présentant des valeurs manquantes constitue l'approche la plus directe. Cette méthode présente des implications différentes selon le type de mécanisme sous-jacent :

Pour les données MCAR, la suppression de valeurs aléatoires n'introduit aucun biais dans l'analyse. Cependant, elle peut réduire la qualité du modèle si une proportion importante de données est éliminée.

Dans le cas des données MAR, la suppression introduit un biais systématique car les observations manquantes ne sont pas distribuées aléatoirement. L'imputation devient alors nécessaire pour préserver la validité statistique.

Pour les données MNAR, la suppression génère également un biais, mais l'imputation s'avère plus complexe en l'absence d'informations sur le processus génératif des valeurs manquantes.

##### Imputation par valeur unique

Cette méthode attribue une valeur constante à l'ensemble des observations manquantes d'une variable donnée. Pour les variables quantitatives, les choix incluent la moyenne (sensible aux valeurs extrêmes), la médiane ou le mode. Pour les variables qualitatives, l'imputation peut utiliser une catégorie distincte ou la classe la plus fréquente.

L'imputation par valeur unique présente l'avantage de sa simplicité conceptuelle et computationnelle. Néanmoins, elle montre des limites importantes : lorsque de nombreuses valeurs sont manquantes, la variable peut devenir inutilisable car artificiellement concentrée sur une seule valeur. Cette approche s'avère également inadaptée aux données MAR car elle ignore les dépendances entre variables.

##### Imputation par k plus proches voisins

L'algorithme des k-nearest neighbors (KNN) pour l'imputation estime les valeurs manquantes en utilisant les valeurs des k observations les plus similaires qui possèdent une mesure pour la variable concernée. Cette approche présente l'avantage significatif de prendre en compte les dépendances entre variables, ce qui la rend particulièrement adaptée aux données MAR.

La méthode introduit cependant un hyperparamètre k supplémentaire dont l'optimisation peut s'avérer délicate. Le choix de k influence directement la qualité de l'imputation : une valeur trop faible peut conduire à une imputation instable, tandis qu'une valeur trop élevée peut lisser excessivement les données.

##### Exemple d'application

Considérons le jeu de données suivant :

| ID  | Taille | Poids |
|-----|--------|-------|
| ID1 | 10     | 1     |
| ID2 | 12     | 2.5   |
| ID3 | 14     | 3     |
| ID4 | 9      | 2     |
| ID5 | N/A    | 1     |

Pour l'imputation par valeur unique, la moyenne des tailles observées (11.25) ou la médiane (11) peuvent être utilisées. Avec k=1, l'algorithme KNN sélectionnerait l'observation la plus proche de ID5 basée sur le poids (ID1 avec un poids de 1), donnant une taille imputée de 10. Avec k=3, la moyenne des trois plus proches voisins serait calculée.

### Mise à l'échelle des variables

#### Motivation

La mise à l'échelle des variables (feature scaling) constitue une méthode de normalisation de l'amplitude des différentes caractéristiques d'un jeu de données. Cette étape devient cruciale pour plusieurs catégories d'algorithmes :

Les algorithmes formulant des hypothèses sur la distribution des variables nécessitent souvent une normalisation préalable. Les méthodes basées sur la distance, comme les k-moyennes ou les k plus proches voisins, sont particulièrement sensibles aux différences d'échelle entre variables. Sans normalisation, une variable avec une amplitude importante peut dominer artificiellement le calcul de distance.

Les algorithmes utilisant la descente de gradient bénéficient également de la mise à l'échelle car elle accélère la convergence et stabilise l'optimisation. Enfin, certaines transformations de variables et techniques comme l'analyse en composantes principales (ACP) requièrent une normalisation pour produire des résultats interprétables.

#### Min-max scaling

La normalisation min-max (rescaling) transforme l'amplitude des variables pour les faire évoluer dans l'intervalle [0, 1]. La formule de transformation s'écrit :

$$x' = \frac{x - \min(x)}{\max(x) - \min(x)}$$

Cette méthode préserve la distribution relative des données tout en harmonisant les échelles. Pour le vecteur [1, 3, 4, 2], la transformation min-max donne :

- min(x) = 1, max(x) = 4
- Résultat : [0, 0.67, 1, 0.33]

#### Standardisation

La standardisation transforme les variables pour qu'elles présentent une moyenne nulle et une variance unitaire. Cette transformation suit la formule :

$$x' = \frac{x - \bar{x}}{\sigma}$$

où $\bar{x}$ représente la moyenne et $\sigma$ l'écart-type de la variable.

Pour le vecteur [1, 3, 4, 2] :

- Moyenne : $\bar{x} = 2.5$
- Écart-type : $\sigma = 1.29$
- Résultat standardisé : [-1.16, 0.39, 1.16, -0.39]

#### Problématique de fuite de données

La mise à l'échelle peut introduire une fuite de données (data leakage) entre les ensembles d'entraînement et de test, compromettant la validité des résultats. Cette fuite se produit lorsque les statistiques (moyenne, écart-type, minimum, maximum) calculées sur l'ensemble complet des données sont utilisées pour normaliser à la fois l'entraînement et le test.

Pour éviter cette problématique, la normalisation doit être effectuée exclusivement sur l'ensemble d'entraînement, puis les paramètres obtenus sont appliqués à l'ensemble de test. Cette précaution garantit que l'ensemble de test ne contribue pas à la définition de la transformation.

#### Cas d'usage

##### Situations nécessitant une mise à l'échelle

La normalisation s'avère indispensable pour les modèles sensibles à l'amplitude des variables, notamment les algorithmes basés sur la distance. Les méthodes d'optimisation par descente de gradient tirent également profit de la mise à l'échelle car elle réduit le temps d'entraînement et améliore la stabilité numérique.

Lors de transformations de variables ou d'application de l'analyse en composantes principales, la normalisation devient essentielle pour obtenir des résultats cohérents et interprétables.

##### Situations déconseillant la mise à l'échelle

Certains contextes rendent la normalisation contre-productive. Les modèles nécessitant une interprétation directe des coefficients peuvent voir leur lisibilité compromise par la mise à l'échelle. De plus, certains algorithmes, notamment les méthodes basées sur les arbres de décision, ne sont sensibles qu'aux relations de proportionnalité et ne bénéficient pas de la normalisation.

### Suppression des valeurs aberrantes

#### Définition et origine des valeurs aberrantes

Une valeur aberrante (outlier) correspond à une observation qui diffère significativement des autres points de données. Ces anomalies peuvent résulter de plusieurs phénomènes : des erreurs de mesure, de la variabilité naturelle dans le processus de mesure, ou l'émergence de comportements nouveaux et inattendus.

#### Stratégies de gestion

La présence de valeurs aberrantes soulève une question fondamentale : certaines résultent d'erreurs de mesure et doivent être corrigées, tandis que d'autres portent une information légitime, comme dans le cas de distributions non gaussiennes.

Plusieurs approches permettent de traiter les valeurs aberrantes : leur suppression du jeu de données, leur remplacement par imputation, l'utilisation de métriques robustes (médiane plutôt que moyenne), ou l'adaptation des modèles pour les prendre en compte. La prudence s'impose avant toute suppression car les valeurs aberrantes peuvent contenir des informations précieuses.

#### Méthode de Tukey

La méthode de Tukey (Tukey's fence) constitue une approche standard pour la détection de valeurs aberrantes. Elle considère comme aberrantes les observations situées en dehors de l'intervalle :

$$[Q_1 - k(Q_3 - Q_1), Q_3 + k(Q_3 - Q_1)]$$

où $Q_1$ et $Q_3$ représentent respectivement les premier et troisième quartiles.

Tukey suggère d'utiliser k = 1.5 pour identifier les valeurs aberrantes modérées et k = 3 pour les valeurs extrêmes. Cette méthode s'appuie sur l'écart interquartile, une mesure robuste de la dispersion qui résiste mieux à l'influence des valeurs extrêmes que l'écart-type.

### Conclusion

Le préprocessing des données représente une étape cruciale qui conditionne largement la réussite d'un projet d'apprentissage automatique. La gestion appropriée des valeurs manquantes, la mise à l'échelle des variables et le traitement des valeurs aberrantes nécessitent une compréhension approfondie des mécanismes sous-jacents et des implications de chaque choix méthodologique.

L'efficacité du préprocessing repose sur l'adaptation des techniques aux caractéristiques spécifiques du jeu de données et aux exigences de l'algorithme d'apprentissage utilisé. Une approche réfléchie et systématique dans cette phase préparatoire constitue un investissement essentiel pour la qualité finale des modèles développés.
