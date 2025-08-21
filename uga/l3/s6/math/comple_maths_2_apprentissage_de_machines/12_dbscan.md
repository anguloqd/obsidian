# 12 // dbscan

[lecture_dbscan_3.pdf](ressources/12_dbscan_lecture_dbscan_3.pdf)
[Papier d’origine 1996_DBSCAN_KDD.pdf](ressources/12_dbscan_1996_dbscan_kdd.pdf)
[DBSCAN avec des paramètres adaptatifs : OPTICS.pdf](ressources/12_dbscan_optics.pdf)

# DBSCAN - Clustering par densité

## Introduction

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) est un algorithme de clustering non-paramétrique basé sur la densité. Contrairement aux méthodes traditionnelles comme k-means qui nécessitent de spécifier à l'avance le nombre de clusters, DBSCAN identifie automatiquement les groupes de points en se basant sur leur densité locale dans l'espace des données.

L'approche fondamentale de DBSCAN consiste à regrouper les points qui sont étroitement espacés (possédant de nombreux voisins proches) tout en marquant comme valeurs aberrantes les points isolés dans des régions de faible densité (dont les plus proches voisins sont éloignés).

## Principe de fonctionnement

### Définitions fondamentales

DBSCAN repose sur trois concepts clés définis à partir d'un rayon $\epsilon$ et d'un seuil minimal de points $n_{points}$ :

**Points centraux (core points)** : Un point est considéré comme central si au moins $n_{points}$ autres points se trouvent dans un rayon de distance $\epsilon$ autour de lui. Ces points forment le cœur des clusters et constituent les régions de haute densité.

**Accessibilité directe** : Un point $q$ est directement accessible depuis un point $p$ si $p$ est un point central et que $q$ se trouve dans la zone de rayon $\epsilon$ autour de $p$. Cette relation n'est pas nécessairement symétrique.

**Accessibilité** : Un point $q$ est accessible depuis un point $p$ s'il existe un chemin $p_0, p_1, \ldots, p_n, q$ où chaque $p_i$ est directement accessible depuis $p_{i-1}$. Cette propriété permet de connecter des points à travers une chaîne de points centraux.

**Points aberrants (outliers)** : Les points qui ne sont accessibles depuis aucun autre point sont considérés comme des valeurs aberrantes ou du bruit.

### Formation des clusters

Une fois que chaque point a été correctement classifié selon les définitions précédentes, la formation des clusters suit une règle simple : un cluster est constitué de tous les points (centraux ou non-centraux) qui sont accessibles depuis un point central donné. Les points non-accessibles ne sont affectés à aucun cluster et sont considérés comme du bruit.

Cette approche permet de découvrir des clusters de formes arbitraires, contrairement aux méthodes basées sur des prototypes qui tendent à produire des clusters sphériques.

## Algorithme

L'implémentation de DBSCAN suit une procédure systématique en trois étapes principales :

1. **Identification des voisinages** : Pour chaque point du jeu de données, l'algorithme détermine ses $\epsilon$-voisins (tous les points situés dans un rayon $\epsilon$) et identifie les points centraux ayant plus de $n_{points}$ voisins.

2. **Connexion des points centraux** : L'algorithme trouve tous les points centraux connectés, c'est-à-dire ceux qui sont mutuellement accessibles, pour former les structures de base des clusters.

3. **Affectation des points non-centraux** : Chaque point non-central est affecté au cluster le plus proche si celui-ci se trouve dans un rayon $\epsilon$, sinon il est classé comme bruit.

Cette approche garantit que tous les points d'un même cluster sont connectés par des chemins de haute densité, préservant ainsi la structure naturelle des données.

## Hyperparamètres

DBSCAN nécessite la configuration de trois hyperparamètres principaux :

- **$n_{points}$** : Le nombre minimum de points requis pour qu'un point soit considéré comme central. Ce paramètre contrôle la densité minimale requise pour former un cluster.

- **$\epsilon$** : Le rayon du voisinage utilisé pour définir la proximité entre les points. Il détermine la portée locale de l'analyse de densité.

- **Métrique de distance** : La fonction de distance utilisée pour calculer la proximité entre les points (euclidienne, Manhattan, etc.).

Le choix de ces paramètres influence fortement les résultats de l'algorithme et nécessite souvent une expertise du domaine ou une analyse exploratoire des données.

## Avantages et limites

### Avantages

DBSCAN présente plusieurs avantages significatifs par rapport aux méthodes de clustering traditionnelles :

**Découverte automatique du nombre de clusters** : L'algorithme détermine naturellement le nombre de clusters présents dans les données sans nécessiter de spécification préalable.

**Clusters de formes arbitraires** : Contrairement aux méthodes basées sur des centres (comme k-means), DBSCAN peut identifier des clusters de formes complexes et non-convexes.

**Robustesse au bruit** : L'intégration native du concept de bruit permet à l'algorithme d'identifier et d'isoler les valeurs aberrantes plutôt que de les forcer dans des clusters existants.

**Simplicité paramétrique** : Avec seulement trois hyperparamètres, l'algorithme reste relativement simple à configurer, particulièrement lorsque des experts du domaine peuvent guider le choix des paramètres.

### Limites

Malgré ses avantages, DBSCAN présente certaines limitations :

**Sensibilité aux variations de densité** : L'algorithme ne fonctionne pas de manière optimale avec des données présentant des densités très variables à travers l'espace paramétrique, car les mêmes paramètres $\epsilon$ et $n_{points}$ peuvent ne pas convenir à toutes les régions.

**Sélection des hyperparamètres** : Le choix approprié des paramètres $\epsilon$ et $n_{points}$ peut être difficile et nécessite souvent une analyse préalable des données ou des connaissances expertes du domaine d'application.

Ces caractéristiques font de DBSCAN un algorithme particulièrement adapté aux données présentant des clusters bien séparés de densité relativement homogène, tout en offrant une approche robuste pour la détection d'anomalies.