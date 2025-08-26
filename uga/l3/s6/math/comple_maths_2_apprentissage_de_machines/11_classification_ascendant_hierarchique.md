## 11 // classification ascendant hiérarchique

[lecture_hac.pdf](ressources/11_classification_ascendant_hierarchique_lecture_hac.pdf)

## Classification ascendante hiérarchique

### Introduction au clustering hiérarchique

#### Définition du clustering hiérarchique

Le clustering hiérarchique constitue une méthode de classification qui vise à construire une hiérarchie de clusters, organisant les données selon une structure arborescente de clusters imbriqués. Cette approche diffère fondamentalement des méthodes de partitionnement comme k-means en produisant une représentation multi-échelle des groupements naturels présents dans les données.

#### Approches méthodologiques

Deux stratégies principales caractérisent le clustering hiérarchique, chacune procédant selon une logique inverse :

L'**approche ascendante (agglomérative)** débute avec chaque observation constituant son propre cluster individuel, puis fusionne progressivement les paires de clusters les plus similaires en remontant la hiérarchie. Cette méthode nécessite de définir un critère pour décider quand fusionner les clusters.

L'**approche descendante (divisive)** commence avec l'ensemble des observations dans un unique cluster global, puis effectue des divisions récursives en descendant la hiérarchie. Cette stratégie requiert un critère pour déterminer quand subdiviser les clusters existants.

### Critères de liaison entre clusters

#### Fondements théoriques

La construction d'une hiérarchie de clusters nécessite deux composants essentiels : une mesure de dissimilarité entre observations individuelles et une mesure de dissimilarité entre ensembles d'observations. Cette seconde mesure, appelée critère de liaison, détermine la manière dont les distances entre clusters sont calculées.

#### Définition du critère de liaison

Un critère de liaison constitue une fonction des distances pairwise entre observations, permettant de mesurer la dissimilarité entre ensemble de points. Le choix de ce critère influence profondément la forme et la qualité des clusters obtenus.

#### Critère de liaison de Ward

Le critère de Ward minimise la somme des différences quadratiques à l'intérieur de tous les clusters. Il mesure l'augmentation de variance qui résulterait de la fusion de deux clusters donnés.

Formellement, pour deux clusters A et B, le critère de Ward se calcule :

$$W(A,B) = \sum_{x \in A \cup B} ||x - \mu_{A \cup B}||^2 - \sum_{x \in A} ||x - \mu_A||^2 - \sum_{x \in B} ||x - \mu_B||^2$$

Cette formule peut être simplifiée sous la forme :

$$W(A,B) = \frac{|A| \times |B|}{|A \cup B|} ||\mu_A - \mu_B||^2$$

où $\mu_A$ et $\mu_B$ représentent respectivement les centroïdes des clusters A et B.

#### Critère de liaison complète

La liaison complète minimise la distance maximale entre observations de paires de clusters. Cette approche conservatrice tend à produire des clusters compacts et de taille similaire.

Étant donnée une mesure de dissimilarité d et deux ensembles A et B :

$$C(A,B) = \max_{a \in A, b \in B} d(a,b)$$

Cette méthode garantit que tous les points d'un cluster sont relativement proches les uns des autres, mais peut être sensible aux valeurs aberrantes.

#### Critère de liaison simple

La liaison simple minimise la distance entre les observations les plus proches de paires de clusters. Cette approche permissive peut produire des clusters de forme allongée.

$$S(A,B) = \min_{a \in A, b \in B} d(a,b)$$

Cette méthode favorise la formation de chaînes d'observations et peut être sensible au phénomène de chaînage (chaining effect) où des clusters s'étendent de manière artificielle.

#### Critère de liaison moyenne

La liaison moyenne minimise la moyenne des distances entre toutes les observations de paires de clusters, offrant un compromis entre les approches simple et complète.

$$A(A,B) = \frac{1}{|A| \times |B|} \sum_{a \in A} \sum_{b \in B} d(a,b)$$

Cette méthode considère l'ensemble des relations entre points des deux clusters, produisant généralement des résultats équilibrés.

#### Exemple d'application des critères

Considérons deux ensembles de vecteurs dans $\mathbb{R}^2$ avec la distance de Manhattan :

- A = {[1,2], [2,3], [4,5]}
- B = {[3,1], [4,5], [1,5]}

L'application des différents critères de liaison révèle leurs caractéristiques distinctives :

- Ward nécessite le calcul des centroïdes et de l'augmentation de variance
- Complete identifie la paire de points la plus éloignée entre les deux ensembles
- Simple trouve la paire de points la plus proche
- Average calcule la moyenne de toutes les distances pairwise

### Algorithme de clustering agglomératif

#### Description de l'algorithme

L'algorithme de clustering agglomératif procède selon une logique itérative simple mais efficace. Pour un critère de liaison L et une mesure de dissimilarité d sélectionnés :

1. **Initialisation** : Chaque individu est placé dans son propre cluster
2. **Fusion initiale** : Les éléments les plus proches sont fusionnés
3. **Itérations** : Jusqu'à ce que tous les éléments appartiennent au même cluster, fusionner récursivement les ensembles d'éléments qui minimisent le critère de liaison

L'assignation finale des clusters s'effectue en coupant l'algorithme à une valeur sélectionnée du critère de liaison, déterminant ainsi le niveau de granularité souhaité.

#### Exemple pratique

L'application de l'algorithme avec le critère de liaison simple et la distance de Manhattan sur le jeu de données suivant illustre le processus :

| Longueur sépale | Largeur sépale | Longueur pétale |
|-----------------|----------------|------------------|
| 5               | 2              | 1                |
| 4               | 3              | 1                |
| 6               | 5              | 4                |
| 7               | 1              | 5                |

L'algorithme calcule progressivement les distances entre tous les clusters, identifie les fusions optimales, et construit la hiérarchie complète. Différentes valeurs de seuil permettent d'obtenir différents nombres de clusters finaux.

### Dendrogrammes et interprétation

#### Définition et utilisation des dendrogrammes

Un dendrogramme constitue un diagramme arborescent représentant graphiquement la hiérarchie de clusters et leurs critères de liaison respectifs. Cette visualisation offre une représentation intuitive du processus de clustering et facilite l'analyse des résultats.

#### Avantages interprétatifs des dendrogrammes

Les dendrogrammes fournissent plusieurs avantages pour l'interprétation des résultats :

La **visualisation claire des groupements** permet d'identifier facilement quels éléments sont regroupés ensemble et à quel niveau de la hiérarchie ces regroupements se forment.

La **sélection flexible du nombre de clusters** s'effectue en définissant un seuil de coupure sur le dendrogramme, permettant d'explorer différentes granularités sans recalculer l'algorithme.

La **compréhension de la structure hiérarchique** révèle les relations d'inclusion entre clusters et met en évidence les sous-groupes naturels présents dans les données.

### Sélection du nombre optimal de clusters

#### Défis de la sélection

La détermination du nombre optimal de clusters demeure un défi fondamental du clustering hiérarchique. Cette problématique nécessite une approche multifacette combinant analyse visuelle et critères quantitatifs.

#### Approches de sélection

Plusieurs stratégies facilitent la sélection du nombre de clusters :

L'**analyse visuelle du dendrogramme** permet d'identifier les divisions qui "font sens" du point de vue métier ou scientifique. Les grandes différences dans les hauteurs de fusion indiquent souvent des séparations naturelles importantes.

L'**évaluation des scores de qualité** en fonction du nombre de clusters offre une validation quantitative. Les métriques comme le score de silhouette ou l'indice de Davies-Bouldin peuvent guider la sélection optimale.

La **validation par domaine d'expertise** reste essentielle pour confirmer que les clusters identifiés correspondent à des groupes significatifs dans le contexte applicatif.

### Avantages et limitations

#### Avantages du clustering hiérarchique

Le clustering hiérarchique présente plusieurs atouts distinctifs :

La **facilité d'interprétation** constitue un avantage majeur, rendant les résultats accessibles même à des utilisateurs non-spécialistes. La représentation arborescente correspond à des modes de pensée naturels pour l'organisation des connaissances.

L'**efficacité computationnelle pour l'exploration** permet de changer le nombre de clusters sans recalculer l'intégralité de l'algorithme. Une seule exécution produit toutes les configurations possibles de clustering.

La **révélation de structures multi-échelles** offre une compréhension approfondie de l'organisation des données à différents niveaux de granularité.

#### Limitations de l'approche

Plusieurs contraintes limitent l'applicabilité du clustering hiérarchique :

La **nécessité d'inférer le nombre de clusters** demeure un défi, malgré les outils d'aide à la décision disponibles. Cette sélection requiert souvent une expertise métier significative.

La **sensibilité au critère de liaison** peut produire des résultats très différents selon le choix effectué, nécessitant une compréhension approfondie des implications de chaque méthode.

La **complexité computationnelle** peut devenir prohibitive pour de très grandes bases de données, limitant l'applicabilité pratique de la méthode.

### Conclusion

La classification ascendante hiérarchique constitue un outil puissant pour l'exploration et la compréhension de structures complexes dans les données. Sa capacité à révéler des organisations multi-échelles et sa facilité d'interprétation en font une méthode de choix pour de nombreuses applications. La maîtrise des différents critères de liaison et l'analyse appropriée des dendrogrammes permettent d'exploiter pleinement le potentiel de cette approche pour révéler les patterns cachés dans les données.
