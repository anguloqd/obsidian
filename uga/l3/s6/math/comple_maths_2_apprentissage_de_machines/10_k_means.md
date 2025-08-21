# 10 // k-means

[lecture_kmeans_3.pdf](ressources/10_k_means_lecture_kmeans_3.pdf)

# L'algorithme k-means

## Principe fondamental

### Définition de l'algorithme k-means

L'algorithme k-means, développé par MacQueen en 1967, constitue une méthode de clustering qui partitionne l'espace en k clusters en minimisant la variance intra-cluster. Cette approche vise à identifier des groupements naturels dans les données en optimisant un critère mathématique précis.

Formellement, étant donné un ensemble d'individus décrits par leurs caractéristiques $(X_1, \ldots, X_n)$, l'algorithme cherche à identifier k ensembles qui partitionnent les données en minimisant la variance intra-cluster :

$$\sum_{i=1}^{k} \sum_{X \in S_i} ||X - \mu_i||^2$$

où $\mu_i = \frac{1}{|S_i|} \sum_{X \in S_i} X$ représente le centroïde du cluster i.

### Distinction entre centroïdes et médoïdes

La compréhension des concepts de centroïde et de médoïde s'avère essentielle pour saisir les nuances entre différentes approches de clustering.

Le **centroïde** correspond à la moyenne arithmétique d'un cluster. Il s'agit d'un point calculé qui, dans la plupart des cas, n'appartient pas au jeu de données original. Cette caractéristique peut compliquer l'interprétation des résultats dans certains contextes applicatifs.

Le **médoïde** désigne un membre effectif du jeu de données dont la somme des dissimilarités avec tous les autres objets du cluster est minimale. Contrairement au centroïde, le médoïde existe réellement dans les données, facilitant ainsi l'interprétation des clusters.

## Algorithme k-means : implémentation

### Complexité algorithmique et approche pratique

Le problème d'optimisation sous-jacent au k-means s'avère NP-difficile, rendant impossible la recherche exhaustive de la solution optimale pour des jeux de données de taille réaliste. En pratique, l'algorithme itératif de Lloyd fournit une approximation efficace qui converge vers un optimum local.

### Description de l'algorithme de Lloyd

L'algorithme de Lloyd procède par itérations en alternant deux étapes fondamentales jusqu'à convergence :

**Étape d'assignation** : Chaque observation est assignée au cluster dont le centroïde est le plus proche selon la distance euclidienne. Cette étape utilise un critère de proximité simple mais efficace pour déterminer l'appartenance de chaque point.

**Étape de mise à jour** : Les centroïdes de chaque cluster sont recalculés comme la moyenne arithmétique de toutes les observations qui lui ont été assignées. Cette étape garantit que les centroïdes reflètent fidèlement la distribution des points dans chaque cluster.

L'algorithme s'arrête lorsque les assignations ne changent plus d'une itération à l'autre, indiquant que la configuration de clustering a atteint un état stable.

### Stratégies d'initialisation

L'initialisation des centroïdes influence significativement la qualité de la solution finale et la vitesse de convergence. Plusieurs stratégies d'initialisation sont couramment utilisées :

L'**approche complètement aléatoire** choisit k vecteurs aléatoirement dans l'espace des caractéristiques. Cette méthode simple peut parfois conduire à des solutions sous-optimales si les centroïdes initiaux sont mal positionnés.

La **partition de Forgy** sélectionne aléatoirement k observations du jeu de données comme centroïdes initiaux. Cette approche garantit que les centroïdes de départ correspondent à des points réels des données.

La **partition aléatoire** assigne aléatoirement chaque observation à un cluster, puis calcule les centroïdes correspondants. Cette méthode peut produire des clusters initiaux plus équilibrés.

### Exemple d'application

Considérons le jeu de données suivant pour illustrer l'application de l'algorithme k-means avec k=2 :

| ID | Longueur sépale | Largeur sépale |
|----|-----------------|----------------|
| 1  | 5               | 2              |
| 2  | 5               | 3              |
| 3  | 4               | 3              |
| 4  | 7               | 4              |
| 5  | 6               | 5              |

L'application de l'algorithme nécessite d'initialiser deux centroïdes, d'assigner chaque point au centroïde le plus proche, puis de recalculer les centroïdes jusqu'à convergence. L'interprétation des résultats révèle la formation de deux groupes distincts basés sur les caractéristiques morphologiques.

## Sélection du nombre optimal de clusters

### Identification des hyperparamètres

L'algorithme k-means présente un hyperparamètre principal : le nombre de clusters k. Cette valeur doit être spécifiée avant l'exécution de l'algorithme, ce qui constitue l'un des défis majeurs de cette approche.

### Méthode du coude (elbow method)

La méthode du coude fournit une approche visuelle pour sélectionner le nombre optimal de clusters. Cette technique consiste à tracer la variance intra-cluster en fonction du nombre de clusters et à identifier le point où la courbe s'aplatit significativement.

Le principe repose sur l'observation que l'ajout de clusters supplémentaires réduit mécaniquement la variance intra-cluster, mais avec des gains décroissants. Le "coude" de la courbe indique le point au-delà duquel l'amélioration devient marginale, suggérant le nombre optimal de clusters.

### Utilisation du score de silhouette

Le score de silhouette, présenté dans le cours précédent, atteint théoriquement son maximum global pour le nombre optimal de clusters. Cette propriété en fait un critère objectif pour la sélection de k.

L'approche consiste à calculer le score de silhouette moyen pour différentes valeurs de k et à sélectionner celle qui maximise ce score. Cette méthode offre une validation quantitative des résultats de clustering.

## Avantages et limitations

### Avantages de l'algorithme k-means

L'algorithme k-means présente plusieurs avantages qui expliquent sa popularité :

La **rapidité de calcul** constitue un atout majeur, particulièrement pour de grandes bases de données. L'algorithme présente une complexité temporelle raisonnable qui le rend applicable dans de nombreux contextes industriels.

La **simplicité conceptuelle** facilite la compréhension et l'implémentation de la méthode. Cette transparence algorithmique favorise l'adoption par des utilisateurs non-spécialistes.

L'**efficacité sur les clusters sphériques** représente un point fort notable. Lorsque les données présentent des groupements de forme approximativement circulaire, k-means produit des résultats de haute qualité.

### Limitations de l'approche

Plusieurs limitations inhérentes à l'algorithme doivent être prises en compte :

Le **caractère aléatoire de l'algorithme** introduit une variabilité dans les résultats. Différentes exécutions peuvent produire des solutions distinctes, nécessitant des stratégies de validation robustes.

L'**absence de garantie d'optimum global** constitue une limitation fondamentale. L'algorithme converge vers un optimum local qui peut différer significativement de la solution globale optimale.

La **spécification préalable de k** représente un défi pratique majeur. Cette contrainte nécessite une connaissance a priori de la structure des données ou l'utilisation de méthodes auxiliaires pour estimer k.

L'**inexistence des représentants de classe** complique l'interprétation des résultats. Les centroïdes calculés ne correspondent généralement pas à des observations réelles, rendant l'analyse métier plus complexe.

## Variante : algorithme PAM

### Principe du Partitioning Around Medoids

L'algorithme PAM (Partitioning Around Medoids), développé par Kaufman et Rousseeuw, constitue une variante du k-means qui utilise des médoïdes plutôt que des centroïdes. Cette approche vise à minimiser la distance entre les points d'un cluster et le point désigné comme centre de ce cluster.

L'utilisation de médoïdes résout l'un des problèmes majeurs du k-means : le représentant de chaque cluster existe effectivement dans le jeu de données, facilitant ainsi l'interprétation des résultats.

### Description de l'algorithme PAM

L'algorithme PAM procède par itérations selon le schéma suivant :

**Initialisation** : Sélection gloutonne de k points parmi les n observations pour minimiser la fonction de coût :

$$\sum_{i=1}^{k} \sum_{X \in S_i} d(X, x^{(i)})$$

où $x^{(i)}$ représente le médoïde du cluster i et d une mesure de dissimilarité.

**Itérations** jusqu'à stabilisation de la fonction de coût :

1. **Association** : Chaque point non-médoïde est associé au médoïde le plus proche
2. **Évaluation** : Pour chaque médoïde m et chaque point non-médoïde o :
   - Échange temporaire de m et o
   - Calcul du changement de coût induit
   - Stockage si le coût diminue
3. **Optimisation** : Réalisation de l'échange qui diminue le plus la fonction de coût

### Exemple d'application PAM

L'application de PAM au même jeu de données que précédemment illustre les différences avec k-means :

| ID | Longueur sépale | Largeur sépale |
|----|-----------------|----------------|
| 1  | 5               | 2              |
| 2  | 5               | 3              |
| 3  | 4               | 3              |
| 4  | 7               | 4              |
| 5  | 6               | 5              |

L'algorithme PAM identifie deux médoïdes réels parmi ces cinq observations, facilitant l'interprétation biologique des clusters obtenus.

### Avantages et limitations de PAM

**Avantages** :

L'**existence des médoïdes dans le jeu de données** facilite considérablement l'interprétation des clusters. Les représentants de classe correspondent à des observations réelles, permettant une analyse métier directe.

La **personnalisation de la mesure de dissimilarité** offre une flexibilité importante. L'algorithme peut s'adapter à différents types de données et contextes applicatifs en choisissant la métrique de distance appropriée.

**Limitations** :

La **nécessité de spécifier k** demeure un défi identique à k-means. Cette contrainte nécessite une expertise métier ou l'utilisation de méthodes de sélection automatique.

L'**initialisation aléatoire** peut conduire à des solutions sous-optimales, similairement à k-means. Cette limitation nécessite des stratégies de validation robustes.

## Conclusion

L'algorithme k-means et sa variante PAM constituent des outils fondamentaux pour le clustering de données. Leur simplicité conceptuelle et leur efficacité computationnelle en font des méthodes de choix pour de nombreuses applications. La compréhension de leurs avantages et limitations guide leur utilisation appropriée selon le contexte spécifique et les objectifs analytiques poursuivis.

Le choix entre k-means et PAM dépend principalement de l'importance accordée à l'interprétabilité des résultats et de la nature des données analysées. Ces deux approches offrent des perspectives complémentaires sur la structure cachée des données et constituent une base solide pour l'exploration de jeux de données complexes.