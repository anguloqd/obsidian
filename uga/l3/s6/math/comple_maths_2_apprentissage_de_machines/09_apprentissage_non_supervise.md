# 09 // apprentissage non-supervisé

[lecture_unsupervised_learning_2024.pdf](ressources/09_apprentissage_non_supervise_lecture_unsupervised_learning_2024.pdf)

# Apprentissage non supervisé

## Définitions fondamentales

### Apprentissage non supervisé

L'apprentissage non supervisé constitue une famille d'algorithmes qui apprennent des motifs à partir de données non étiquetées. Contrairement à l'apprentissage supervisé qui vise à prédire des actions sur des données inconnues, l'apprentissage non supervisé cherche à améliorer la compréhension de données existantes. Les algorithmes construisent une représentation concise des données en exploitant les relations de similarité pour générer du contenu informatif ou révéler des structures cachées.

Cette approche méthodologique se distingue par l'absence de variable cible prédéfinie. Les algorithmes explorent autonomement les données pour identifier des patterns naturels, des groupements ou des anomalies sans supervision externe.

### Taxonomie de l'apprentissage non supervisé

La littérature distingue plusieurs catégories d'apprentissage non supervisé, chacune répondant à des objectifs spécifiques :

Les **méthodes de clustering** regroupent les observations selon leur similarité, révélant des structures naturelles dans les données. Les **modèles latents** identifient des variables cachées qui expliquent les corrélations observées. La **détection d'anomalies** repère les observations atypiques qui s'écartent significativement du comportement général.

## Clustering : concepts et définition

### Principe du clustering

Le clustering consiste à regrouper un ensemble d'objets de sorte que les objets appartenant au même groupe (appelé cluster) soient plus "similaires" entre eux qu'aux objets des autres groupes. Cette similarité s'évalue selon des critères mathématiques spécifiques qui varient selon l'algorithme utilisé.

Formellement, étant donné un ensemble de j individus décrits par leurs caractéristiques $(x_{j,1}, \ldots, x_{j,n})$, l'objectif consiste à assigner chaque individu à un cluster i (où $1 \leq i \leq m$). L'algorithme optimal produit des groupes où la similarité intra-groupe est maximisée tandis que la similarité inter-groupes est minimisée.

### Diversité des approches de clustering

Les algorithmes de clustering se différencient par leur interprétation de la "similarité" et du concept de "cluster". Cette diversité méthodologique reflète l'absence d'une méthode universellement optimale : chaque jeu de données peut nécessiter une approche spécifique.

Les **modèles basés sur les centroïdes** (comme k-means) définissent les clusters autour de points centraux. Les **modèles de connectivité** (clustering hiérarchique) construisent des dendrogrammes basés sur la proximité entre observations. Les **approches basées sur la distribution** (modèles latents et mélanges gaussiens) supposent que les données proviennent de distributions statistiques sous-jacentes. Enfin, les **méthodes basées sur la densité** (DBSCAN) identifient les clusters comme des régions de forte densité séparées par des zones de faible densité.

### Types de clustering

Le clustering peut être catégorisé selon la nature de l'affectation des observations :

Le **clustering dur (hard clustering)** assigne chaque individu à un unique cluster, créant une partition nette des données. Le **clustering flou (soft clustering)** permet à un individu d'appartenir simultanément à plusieurs clusters avec des degrés d'appartenance variables, reflétant l'incertitude naturelle dans certaines affectations.

### Applications pratiques

Les applications du clustering couvrent de nombreux domaines. En marketing, la segmentation comportementale permet d'identifier des groupes de consommateurs aux habitudes similaires. En analyse de données, le clustering facilite la détection d'individus aberrants nécessitant une investigation approfondie. Dans l'apprentissage semi-supervisé, le clustering peut servir à mapper des échantillons vers des classes pour enrichir l'entraînement de modèles supervisés.

### Sélection du nombre de clusters

La détermination du nombre optimal de clusters constitue un défi majeur. Certains algorithmes intègrent nativement cette sélection, tandis que d'autres nécessitent une approche itérative : tester différents nombres de clusters, évaluer chaque configuration et sélectionner la meilleure selon des critères objectifs.

Le clustering demeure sensible au surapprentissage, et le compromis biais-variance s'applique également dans ce contexte. Un nombre de clusters trop élevé peut conduire à une sur-segmentation artificielle, tandis qu'un nombre insuffisant peut masquer des structures importantes.

## Évaluation des algorithmes de clustering

### Défis spécifiques à l'évaluation

L'absence de vérité terrain (ground truth) dans l'apprentissage non supervisé empêche l'utilisation directe des métriques d'apprentissage supervisé. Cette particularité nécessite le développement de métriques spécifiquement adaptées aux tâches non supervisées.

### Approches d'évaluation

Trois approches principales permettent d'évaluer la performance des algorithmes de clustering :

L'**évaluation interne** utilise des scores mathématiques décrivant la qualité du clustering basés uniquement sur les données et les résultats de l'algorithme. L'**évaluation manuelle** fait appel à des experts humains pour valider la cohérence et la signification des clusters. L'**évaluation empirique ou indirecte** mesure l'efficacité pratique du clustering dans des tâches applicatives spécifiques.

### Principe des scores de clustering

Les scores de clustering attribuent les meilleures évaluations aux algorithmes produisant des clusters à forte similarité intra-groupe et faible similarité inter-groupes. Cette philosophie reflète l'objectif fondamental du clustering : maximiser la cohésion interne tout en maximisant la séparation externe.

## Score de silhouette

### Définition et formulation

Le score de silhouette mesure la similarité d'un objet à son propre cluster comparativement aux autres clusters. Pour une instance donnée, ce score se calcule selon la formule :

$$s = \frac{b - a}{\max(a, b)}$$

où :
- $a$ représente la distance intra-cluster moyenne (distance moyenne entre l'objet et tous les autres objets de son cluster)
- $b$ représente la distance moyenne au cluster voisin le plus proche (distance moyenne entre l'objet et tous les objets du cluster le plus proche)

### Interprétation des valeurs

Le score de silhouette évolue dans l'intervalle [-1, 1]. Une valeur élevée indique que l'objet est bien assigné à son cluster et mal adapté aux clusters voisins. Une valeur proche de 0 suggère que l'objet se situe à la frontière entre deux clusters. Une valeur négative signale une affectation probablement incorrecte.

### Diagnostic de la qualité du clustering

Lorsque la majorité des objets présentent des valeurs élevées, la configuration de clustering est appropriée. À l'inverse, de nombreuses valeurs faibles ou négatives indiquent soit que le jeu de données ne se prête pas au clustering, soit que le nombre de clusters est mal choisi.

### Représentation visuelle

Les scores de silhouette se représentent habituellement sous forme de graphique de silhouette, permettant une évaluation visuelle immédiate de la qualité du clustering. Cette représentation facilite l'identification des clusters problématiques et guide l'optimisation des paramètres.

### Exemple d'application

Considérons le jeu de données suivant avec clustering par distance de Manhattan :

| ID | Taille | Poids | Cluster |
|----|--------|-------|---------|
| 1  | 10     | 16    | 1       |
| 2  | 12     | 14    | 1       |
| 3  | 14     | 15    | 1       |
| 4  | 14     | 30    | 2       |
| 5  | 30     | 30    | 2       |

Pour chaque point, le calcul du score de silhouette nécessite de déterminer la distance intra-cluster moyenne et la distance moyenne au cluster voisin le plus proche, puis d'appliquer la formule de normalisation.

## Indice de Davies-Bouldin

### Principe de l'indice

L'indice de Davies-Bouldin mesure la similarité moyenne de chaque cluster avec son cluster le plus similaire. Cette similarité se définit comme le rapport entre les distances intra-cluster et les distances inter-clusters.

### Formulation mathématique

La similarité entre les clusters i et j se définit par :

$$R_{i,j} = \frac{s_i + s_j}{d_{i,j}}$$

où :
- $s_i$ représente la distance moyenne entre chaque point du cluster i et le centroïde de ce cluster
- $d_{i,j}$ représente la distance entre les centroïdes des clusters i et j

L'indice de Davies-Bouldin se calcule alors :

$$DB = \frac{1}{k} \sum_{i=1}^{k} \max_{i \neq j} R_{i,j}$$

où k désigne le nombre de clusters.

### Interprétation

Contrairement au score de silhouette, un indice de Davies-Bouldin faible indique un meilleur clustering. Cette métrique favorise les configurations où les clusters sont compacts (faibles distances intra-cluster) et bien séparés (grandes distances inter-clusters).

### Exemple d'application

Avec le même jeu de données que précédemment, l'utilisation de la distance euclidienne permet de calculer les centroïdes de chaque cluster, puis les distances moyennes intra-cluster et inter-clusters nécessaires à l'évaluation de l'indice.

## Interprétation des clusters

### Complexité de l'interprétation

L'interprétation des clusters s'avère souvent aussi complexe que la tâche de clustering elle-même. Cette étape critique détermine l'utilité pratique des résultats obtenus et guide les décisions business ou scientifiques.

### Stratégies d'interprétation

Plusieurs approches facilitent l'interprétation des clusters :

L'**analyse des scores de qualité** permet d'évaluer la pertinence globale du clustering et d'identifier les configurations problématiques. L'**examen des estimateurs statistiques** de chaque caractéristique au sein des clusters révèle les variables discriminantes. La **visualisation graphique** des clusters selon différentes dimensions aide à comprendre les critères de regroupement.

### Analyse des caractéristiques

L'interprétation passe par l'analyse comparative des valeurs moyennes, médianes et écarts-types de chaque caractéristique dans les différents clusters. Cette analyse statistique révèle les variables qui contribuent le plus à la différenciation entre groupes.

### Validation par domaine d'expertise

La validation par des experts du domaine demeure essentielle pour confirmer la cohérence métier des clusters identifiés. Cette validation humaine complète les métriques quantitatives en apportant une perspective sémantique indispensable.

## Conclusion

L'apprentissage non supervisé, et particulièrement le clustering, offre des outils puissants pour explorer et comprendre la structure cachée des données. Les métriques d'évaluation comme le score de silhouette et l'indice de Davies-Bouldin fournissent des guides objectifs pour optimiser les configurations de clustering, tandis que l'interprétation des résultats nécessite une approche multidisciplinaire combinant analyse statistique et expertise métier.

La réussite d'un projet de clustering dépend autant de la sélection appropriée de l'algorithme et de ses paramètres que de la capacité à interpréter et valider les résultats dans le contexte applicatif spécifique.