## 03 // métriques et distances

[lecture_distance.pdf](ressources/03_metriques_et_distances_lecture_distance.pdf)

> [!note]
> [https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise)

## Métriques et distances

### Introduction

Les distances constituent un concept fondamental en apprentissage automatique et représentent le premier outil essentiel de tout scientifique des données. Elles permettent de quantifier numériquement à quel point deux individus ou objets sont "proches" ou "éloignés" dans un espace donné.

Cette mesure de similarité ou de dissimilarité entre points de données s'avère cruciale pour de nombreux algorithmes d'apprentissage automatique, notamment pour les techniques de classification, de clustering et de recherche de voisinage.

### Définition mathématique d'une distance

#### Définition formelle

Une distance est une mesure numérique qui quantifie l'éloignement entre des objets ou des points dans un espace. Pour qu'une fonction $d : X^2 \rightarrow \mathbb{R}$ soit considérée comme une distance au sens mathématique du terme, elle doit satisfaire quatre propriétés fondamentales :

1. **Propriété d'identité** : $\forall x, y \in X^2, d(x, y) = 0 \Leftrightarrow x = y$
2. **Positivité** : $\forall x, y \in X^2, x \neq y, d(x, y) > 0$
3. **Symétrie** : $\forall x, y \in X^2, d(x, y) = d(y, x)$
4. **Inégalité triangulaire** : $\forall x, y, z \in X^3, d(x, y) + d(y, z) \geq d(x, z)$

#### Interprétation des propriétés

Ces quatre axiomes garantissent la cohérence mathématique de la notion de distance :

- La propriété d'identité assure que seuls les objets identiques ont une distance nulle entre eux
- La positivité impose que la distance entre deux objets distincts soit toujours strictement positive
- La symétrie reflète l'intuition que la distance de A vers B égale celle de B vers A
- L'inégalité triangulaire établit qu'il n'existe pas de "raccourci" : le chemin direct entre deux points est toujours plus court que tout chemin passant par un point intermédiaire

### Distances populaires

#### Distance de Minkowski

La distance de Minkowski constitue une famille générale de distances paramétrée par un ordre $p \geq 1$. Pour deux vecteurs $x = (x_1, x_2, \ldots, x_n) \in \mathbb{R}^n$ et $y = (y_1, y_2, \ldots, y_n) \in \mathbb{R}^n$, elle se définit par :

$$d(x, y) = \left(\sum_{i=1}^{n} |x_i - y_i|^p\right)^{\frac{1}{p}}$$

Cette formulation engendre plusieurs distances classiques selon la valeur du paramètre $p$ :

##### Distance de Manhattan ($p = 1$)

Lorsque $p = 1$, la distance de Minkowski devient la distance de Manhattan, également appelée distance $L_1$ :

$$d(x, y) = \sum_{i=1}^{n} |x_i - y_i|$$

Cette distance correspond à la somme des valeurs absolues des différences entre coordonnées correspondantes.

##### Distance euclidienne ($p = 2$)

Pour $p = 2$, on obtient la distance euclidienne classique, ou distance $L_2$ :

$$d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$

Il s'agit de la distance "intuitive" correspondant à la longueur du segment reliant deux points dans l'espace euclidien.

##### Distance de Chebyshev ($p \rightarrow \infty$)

À la limite quand $p$ tend vers l'infini, la distance de Minkowski converge vers la distance de Chebyshev, ou distance $L_\infty$ :

$$d(x, y) = \max_{i=1,\ldots,n} |x_i - y_i|$$

Cette distance correspond à la plus grande différence absolue entre les coordonnées correspondantes.

#### Exemple de calcul

Pour illustrer ces concepts, considérons deux vecteurs $x = [1, 2, 4, 5]$ et $y = [0, 4, 3, 6]$ :

- **Distance de Manhattan** ($p = 1$) :
  $d(x, y) = |1-0| + |2-4| + |4-3| + |5-6| = 1 + 2 + 1 + 1 = 5$

- **Distance euclidienne** ($p = 2$) :
  $d(x, y) = \sqrt{(1-0)^2 + (2-4)^2 + (4-3)^2 + (5-6)^2} = \sqrt{1 + 4 + 1 + 1} = \sqrt{7}$

- **Distance de Minkowski d'ordre 3** ($p = 3$) :
  $d(x, y) = (|1-0|^3 + |2-4|^3 + |4-3|^3 + |5-6|^3)^{1/3} = (1 + 8 + 1 + 1)^{1/3} = \sqrt[3]{11}$

### Similarité et dissimilarité cosinus

#### Concept de similarité cosinus

La similarité cosinus mesure l'angle entre deux vecteurs plutôt que leur distance euclidienne. Elle s'appuie sur le produit scalaire normalisé et exploite la relation géométrique $x \cdot y = ||x|| \times ||y|| \times \cos(\theta)$, où $\theta$ représente l'angle entre les vecteurs $x$ et $y$.

#### Dissimilarité cosinus

La dissimilarité cosinus se définit comme le complément à 1 de la similarité cosinus. Pour deux vecteurs $x = (x_1, x_2, \ldots, x_n) \in \mathbb{R}^n$ et $y = (y_1, y_2, \ldots, y_n) \in \mathbb{R}^n$, elle s'exprime par :

$$d(x, y) = 1 - \frac{x \cdot y}{||x|| \times ||y||} = 1 - \frac{\sum_{i=1}^{n} x_i \times y_i}{\sqrt{\sum_{i=1}^{n} x_i^2} \times \sqrt{\sum_{i=1}^{n} y_i^2}}$$

#### Exemple de calcul

Pour les vecteurs $x = [1, 2, 4, 5]$ et $y = [0, 4, 3, 6]$ :

- Produit scalaire : $x \cdot y = 1 \times 0 + 2 \times 4 + 4 \times 3 + 5 \times 6 = 0 + 8 + 12 + 30 = 50$
- Norme de $x$ : $||x|| = \sqrt{1^2 + 2^2 + 4^2 + 5^2} = \sqrt{46}$
- Norme de $y$ : $||y|| = \sqrt{0^2 + 4^2 + 3^2 + 6^2} = \sqrt{61}$
- Dissimilarité cosinus : $d(x, y) = 1 - \frac{50}{\sqrt{46} \times \sqrt{61}}$

#### Limitation mathématique

La dissimilarité cosinus ne satisfait pas tous les axiomes d'une distance mathématique stricte. En particulier, l'inégalité triangulaire n'est pas toujours vérifiée, ce qui explique pourquoi cette mesure ne peut être considérée comme une distance au sens mathématique du terme.

### Distance versus dissimilarité

#### Distinction terminologique

Dans la pratique de l'informatique et de l'apprentissage automatique, il existe un abus de langage courant entre informaticiens et mathématiciens. De nombreuses mesures appelées "distances" dans les bibliothèques logicielles ne respectent pas rigoureusement tous les axiomes mathématiques d'une distance.

#### Relaxation des propriétés

Ces mesures, plus précisément appelées similarités ou dissimilarités, relaxent certaines contraintes :

- La propriété de séparation se limite souvent à $\forall x \in X, d(x, x) = 0$ (un objet a une distance nulle avec lui-même)
- L'inégalité triangulaire n'est pas toujours vérifiée

Malgré ces limitations théoriques, ces mesures conservent leur utilité pratique et restent désignées comme "distances" dans la documentation des bibliothèques logicielles.

### Ressources complémentaires

Pour approfondir l'étude des distances et explorer d'autres mesures de similarité utilisées en apprentissage automatique, la fonction `pairwise_distances` du module `sklearn.metrics` de scikit-learn propose une large gamme d'implémentations. Cette ressource s'avère particulièrement utile pour les travaux pratiques et l'application concrète de ces concepts.

La compréhension approfondie de ces différentes mesures de distance constitue un prérequis essentiel pour maîtriser de nombreux algorithmes d'apprentissage automatique, depuis les méthodes de classification par k-plus proches voisins jusqu'aux techniques de clustering hiérarchique.
