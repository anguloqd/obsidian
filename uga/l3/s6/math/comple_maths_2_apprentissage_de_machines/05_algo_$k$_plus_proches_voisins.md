# 05 // algo : $k$ plus proches voisins

[lecture_knn (2).pdf](lecture_knn_(2).pdf)
[knearest_neighbors.pdf](ressources/05_algo_$k$_plus_proches_voisins_knearest_neighbors.pdf)
[knn_papers.pdf](ressources/05_algo_$k$_plus_proches_voisins_knn_papers.pdf)

# Algorithme des k Plus Proches Voisins (k-NN)

## Introduction et contexte

L'algorithme des k plus proches voisins (k-Nearest Neighbors ou k-NN en anglais) constitue l'une des méthodes fondamentales de l'apprentissage automatique supervisé. Cette approche se distingue par sa simplicité conceptuelle et sa capacité à résoudre des problèmes de classification sans nécessiter d'hypothèses préalables sur la distribution des données.

Dans le cadre de l'apprentissage supervisé, l'objectif consiste à apprendre une fonction de prédiction à partir d'un ensemble de données d'entraînement composé de paires (entrée, sortie). L'apprentissage supervisé permet de résoudre diverses catégories de problèmes, notamment :
- La classification : prédiction d'étiquettes catégorielles (spam/non-spam, type de cancer, reconnaissance d'images)
- La régression : prédiction de valeurs numériques continues (prix immobilier, température, cours boursiers)

## Principe fondamental de l'algorithme k-NN

### Définition et concept de base

L'algorithme des k plus proches voisins est une méthode d'apprentissage supervisé non-paramétrique qui effectue la classification d'un nouvel échantillon en se basant sur le vote majoritaire de ses k voisins les plus proches dans l'espace des caractéristiques.

Le terme "non-paramétrique" signifie que l'algorithme ne fait aucune hypothèse préalable concernant la forme ou la distribution des données sous-jacentes. Cette propriété lui confère une grande flexibilité d'adaptation à différents types de problèmes.

### Mécanisme de fonctionnement

Le processus de classification par k-NN suit une séquence d'étapes bien définie :

1. **Calcul des distances** : Pour un nouvel échantillon à classifier, l'algorithme calcule la distance entre cet échantillon et tous les points du jeu d'entraînement
2. **Identification des voisins** : Les k échantillons d'entraînement les plus proches sont identifiés selon la métrique de distance choisie
3. **Vote majoritaire** : L'étiquette de classe est déterminée par le vote majoritaire parmi ces k voisins les plus proches

Cette approche repose sur l'hypothèse fondamentale que des échantillons similaires dans l'espace des caractéristiques appartiennent probablement à la même classe.

## Exemple pratique : Classification de types de Pokémon

### Présentation du problème

Considérons un exemple concret de classification où l'objectif est de prédire le type d'un Pokémon (Eau ou Plante) en fonction de ses caractéristiques physiques : taille et poids.

**Jeu d'entraînement :**

| Taille | Poids | Type   |
|--------|-------|--------|
| 45     | 30    | Eau    |
| 30     | 25    | Eau    |
| 40     | 35    | Eau    |
| 20     | 15    | Plante |
| 22     | 18    | Plante |
| 25     | 20    | Plante |

**Échantillon à classifier :**

| Taille | Poids | Type |
|--------|-------|------|
| 25     | 31    | ?    |

### Application avec la distance euclidienne

La distance euclidienne entre deux points $(x_1, y_1)$ et $(x_2, y_2)$ est calculée selon la formule :

$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$

**Calcul des distances pour l'échantillon (25, 31) :**

| Distance calculée | Type correspondant |
| ----------------- | ------------------ |
| 20,02             | Eau                |
| 7,81              | Eau                |
| 15,52             | Eau                |
| 16,76             | Plante             |
| 13,34             | Plante             |
| 11,0              | Plante             |

### Analyse comparative selon la valeur de k

**Classification avec k=1 (1 plus proche voisin) :**
- Le voisin le plus proche est à une distance de 7,81 et appartient à la classe "Eau"
- **Prédiction : Eau**

**Classification avec k=3 (3 plus proches voisins) :**
- Les trois voisins les plus proches sont aux distances : 7,81 (Eau), 11,0 (Plante), 13,34 (Plante)
- Vote majoritaire : 2 votes pour "Plante" contre 1 vote pour "Eau"
- **Prédiction : Plante**

Cette différence de résultat illustre l'impact significatif du choix de la valeur k sur les performances de classification.

## Hyperparamètres de l'algorithme k-NN

### Paramètres principaux

L'algorithme k-NN nécessite la configuration de plusieurs hyperparamètres critiques :

1. **La valeur de k** : le nombre de voisins à considérer pour la classification
2. **La métrique de distance** : euclidienne, Manhattan, Minkowski, etc.
3. **Le système de pondération** : uniforme ou basé sur la distance

### Problématiques liées au choix de k

Le choix de la valeur k présente plusieurs défis :

- **k trop petit (k=1)** : L'algorithme devient très sensible au bruit et aux valeurs aberrantes, pouvant conduire à un sur-apprentissage
- **k trop grand** : L'algorithme peut perdre en précision locale et tendre vers une classification basée sur la classe majoritaire globale
- **k pair** : Risque d'égalité lors du vote, nécessitant une règle de départage

### Sélection optimale des hyperparamètres

La méthode recommandée pour déterminer les hyperparamètres optimaux consiste à utiliser la **validation croisée k-fold**. Cette technique divise le jeu de données en k sous-ensembles, utilise k-1 sous-ensembles pour l'entraînement et le sous-ensemble restant pour la validation, puis répète le processus k fois.

Dans sa version la plus simple, on procède par **plan factoriel complet** en testant toutes les combinaisons possibles des différents hyperparamètres et en sélectionnant celle qui maximise le score de validation.

## Avantages et limites de l'algorithme k-NN

### Avantages principaux

L'algorithme k-NN présente plusieurs atouts significatifs :

**Simplicité conceptuelle** : L'algorithme est intuitivement compréhensible et ne nécessite pas de connaissances mathématiques avancées pour être appréhendé.

**Extension multi-classes naturelle** : Contrairement à certains algorithmes binaires, k-NN gère nativement les problèmes de classification à plus de deux classes sans modification particulière.

**Approche non-paramétrique** : L'absence d'hypothèses sur la distribution des données confère à l'algorithme une grande flexibilité d'adaptation à divers contextes.

**Absence de phase d'entraînement** : L'algorithme ne nécessite pas de phase d'apprentissage préalable, ce qui le rend particulièrement adapté aux situations où les données évoluent fréquemment.

### Limites et défis

Malgré ses avantages, l'algorithme k-NN présente également des limitations importantes :

**Sensibilité à l'hyperparamétrisation** : Les performances de l'algorithme dépendent fortement du choix des hyperparamètres, nécessitant une phase de réglage minutieuse.

**Vulnérabilité au bruit** : La présence de caractéristiques non informatives ou de valeurs aberrantes peut significativement dégrader les performances de classification.

**Coût computationnel élevé** : Pour chaque nouvelle prédiction, l'algorithme doit calculer la distance avec tous les échantillons d'entraînement, ce qui peut devenir prohibitif pour de grandes bases de données.

**Difficulté d'interprétation** : Contrairement aux arbres de décision ou à la régression linéaire, k-NN ne fournit pas de modèle explicite permettant de comprendre les relations entre les variables.

**Sensibilité à la dimension** : Dans des espaces de haute dimension, la notion de "proximité" devient moins discriminante (fléau de la dimensionnalité), réduisant l'efficacité de l'algorithme.

## Considérations pratiques et extensions

### Métriques de distance alternatives

Au-delà de la distance euclidienne, plusieurs métriques peuvent être utilisées selon la nature des données :

- **Distance de Manhattan** : $d = |x_1-x_2| + |y_1-y_2|$
- **Distance de Minkowski** : généralisation des distances euclidienne et Manhattan
- **Distance de Hamming** : pour les variables catégorielles
- **Distances personnalisées** : adaptées à des domaines spécifiques

### Pondération par distance

Une variante de l'algorithme consiste à pondérer les votes des voisins en fonction de leur distance : les voisins plus proches ont un poids plus important dans la décision finale. Cette approche peut améliorer les performances dans certains contextes.

L'algorithme des k plus proches voisins demeure ainsi un outil fondamental de l'apprentissage automatique, offrant un équilibre entre simplicité d'implémentation et efficacité pratique, tout en nécessitant une attention particulière aux choix des hyperparamètres et à la qualité des données.