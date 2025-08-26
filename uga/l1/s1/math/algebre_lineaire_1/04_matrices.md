## 04 // matrices

## Opérations basiques entre deux matrices

### Addition de matrices

L'addition de matrices se fait entrée par entrée. Pour deux matrices $A$ et $B$ de même taille $m \times n$, on a :

$$(A + B)_{ij} = A_{ij} + B_{ij}$$

**Exemple :**

$$\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix} + \begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix} = \begin{pmatrix}
6 & 8 \\
10 & 12
\end{pmatrix}$$

**Propriétés :**
- Associativité : $(A + B) + C = A + (B + C)$
- Commutativité : $A + B = B + A$
- Élément neutre : $A + 0 = A$ (où $0$ est la matrice nulle)
- Élément opposé : $A + (-A) = 0$

### Multiplication de matrices

Le produit matriciel $AB$ n'est défini que si le nombre de colonnes de $A$ égale le nombre de lignes de $B$. Si $A$ est de taille $m \times p$ et $B$ de taille $p \times n$, alors $AB$ est de taille $m \times n$ et :

$$(AB)_{ij} = \sum_{k=1}^{p} A_{ik} B_{kj}$$

**Exemple :**

$$\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix} \begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix} = \begin{pmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{pmatrix} = \begin{pmatrix}
19 & 22 \\
43 & 50
\end{pmatrix}$$

> [!note]
> Pièges communes :
>
> - Le produit n'est pas commutatif en général. Juste avec une matrice et son inverse, et aussi une matrice et l'identité.
> - $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.
> - $AB = AC$ n'implique pas $B = C$. On peut avoir $AB = AC$ et $B \ne C$.

Propriétés :

- Associativité : $A(BC) = (AB)C$
- Distributivité : $A(B + C) = AB + AC \text{ et } (B + C)A = BA+ CA$.
- $A \cdot 0 = 0 \text{ et } 0 \cdot A = 0$.

### Multiplication par un scalaire

Pour une matrice $A$ et un scalaire $\lambda \in \mathbb{K}$, la multiplication scalaire est définie par :

$$(\lambda A)_{ij} = \lambda A_{ij}$$

**Propriétés :**
- $(\lambda + \mu)A = \lambda A + \mu A$
- $\lambda(A + B) = \lambda A + \lambda B$
- $\lambda(\mu A) = (\lambda \mu)A$
- $(\lambda A)B = A(\lambda B) = \lambda(AB)$

## **Formule du binôme**

### Lorsque $AB=BA$…

Comme la multiplication n'est pas commutative, les identités binomiales usuelles sont fausses. En particulier, $(A + B)^2$ ne vaut en général pas $A^2 + 2AB + B^2$, mais on sait seulement que $(A+B)^2 = A^2 + AB + BA+ B^2$.

Si $AB = BA$ (si $A$ et $B$ commuent sous la multiplication), alors la formule du binôme s'applique :

$$(A + B)^n = \sum_{k=0}^{n} \binom{n}{k} A^{n-k} B^k$$

Dans la pratique, l'une des deux matrices est souvent la matrice identité qui commute avec toute matrice.

**Cas particuliers importants :**
- $(A + I)^2 = A^2 + 2A + I$
- $(A - I)^2 = A^2 - 2A + I$
- $A^n = (A + I - I)^n$ peut être développé si nécessaire

## **Inverse d'une matrice**

### $A^{-1}$ telle que $A A^{-1}=I$

Une matrice carrée $A$ est inversible (ou régulière) s'il existe une matrice $A^{-1}$ telle que :

$$AA^{-1} = A^{-1}A = I$$

La matrice $A^{-1}$ est appelée l'inverse de $A$ et est unique si elle existe.

Plus généralement, quand $A$ est inversible, pour tout $p ∈ \mathbb{N}$, on note $A^{-p} = (A^{-1})^p$.

- L'ensemble des matrices inversibles de $M_n(\mathbb{K})$ est noté $GL_n(\mathbb{K})$ (groupe linéaire).

**Propriétés de l'inverse :**
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$ (attention à l'ordre !)
- $(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}$ pour $\lambda \neq 0$

**Simplification par une matrice inversible.** Soient $A$ et $B$ deux matrices de $M_n(\mathbb{K})$ et $C$ une matrice inversible de $M_n(\mathbb{K})$. Alors l'égalité $AC = BC$ implique l'égalité $A = B$ (on multiplie par la droite par $C^{-1}$ aux deux côtés).

- Pour les matrices 2x2, la formule est :

$$A = \begin{pmatrix} a &b \\ c & d \end{pmatrix} \iff A^{-1}=\frac{1}{ad-bc} \begin{pmatrix} d &-b \\ -c & a \end{pmatrix}$$

Le déterminant $ad - bc$ doit être non nul pour que l'inverse existe.

- Pour toute autre matrice, utilise la méthode de Gauss-Jordan.

### Méthode de Gauss-Jordan pour calculer l'inverse

Pour calculer $A^{-1}$, on forme la matrice augmentée $(A | I)$ et on applique les opérations élémentaires sur les lignes jusqu'à obtenir $(I | A^{-1})$.

**Exemple :**

$$\begin{pmatrix}
2 & 1 & | & 1 & 0 \\
1 & 1 & | & 0 & 1
\end{pmatrix} \rightarrow \begin{pmatrix}
1 & 0 & | & 1 & -1 \\
0 & 1 & | & -1 & 2
\end{pmatrix}$$

Donc $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.

## **Types de matrices**

Avant de les présenter, on devrait connaître l'équivalence par lignes. Deux matrices $A$ et $B$ sont dites ***équivalentes par lignes*** si l'une peut être obtenue à partir de l'autre par une suite d'opérations élémentaires sur les lignes. On note $A ∼ B$.

- Les **opérations élémentaires** sont :
  1. Multiplier une ligne par un scalaire non nul
  2. Ajouter un multiple d'une ligne à une autre ligne
  3. Échanger deux lignes

### Matrices échelonnées

**Matrices échelonnées** : le nombre de zéros commençant une ligne croît strictement ligne par ligne jusqu'à ce qu'il ne reste plus que des zéros (si c'est le cas, mais il peut se passer qu'il n'y ait pas de lignes purement des zéros). Par exemple :

$$\begin{bmatrix}
1&a_0&a_1&a_2&a_3 \\
0&0&2&a_4&a_5 \\
0&0&0&1&a_6
\end{bmatrix}$$

**Critères pour une matrice échelonnée :**
1. Toutes les lignes non nulles sont au-dessus des lignes nulles
2. Le premier élément non nul d'une ligne (appelé pivot) est à droite du pivot de la ligne précédente
3. Tous les éléments sous un pivot sont nuls

**Matrices échelonnées réduites** : est une matrice échelonnée telle que

- le premier coefficient non nul d'une ligne (non nulle) vaut $1$
- et c'est le seul élément non nul de sa colonne.

$$\begin{bmatrix}
1&0&a_1&0&b_1 \\
0&1&a_2&0&b_2 \\
0&0&0&1&b_3
\end{bmatrix}$$

**Théorème :** Toute matrice peut être transformée en une unique matrice échelonnée réduite par des opérations élémentaires sur les lignes.

- Soit $A ∈ M_n(\mathbb{K})$. La matrice $A$ est inversible si et seulement si sa forme échelonnée réduite est la matrice identité $I_n$.
	- Corollaire. Les assertions suivantes sont équivalentes :
		- La matrice $A$ est inversible
		- Le système linéaire $AX = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$ a une unique solution $X = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$
		- Pour tout second membre $B$, le système linéaire $AX = B$ a une unique solution $X$.

### Matrices triangulaires

Les **matrices triangulaires supérieures** sont celles dont les coefficients strictement au-dessous de la diagonale sont $0$. La définition est analogue pour les matrices triangulaires inférieures, juste que dans ce cas-ci les coefficients au-dessus de la diagonale principale sont nuls.

**Exemples :**
- Triangulaire supérieure : $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$
- Triangulaire inférieure : $\begin{pmatrix} 1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix}$

**Propriétés importantes :**
- Le produit de deux matrices triangulaires supérieures est triangulaire supérieure
- Le déterminant d'une matrice triangulaire est le produit de ses éléments diagonaux
- L'inverse d'une matrice triangulaire (si elle existe) est aussi triangulaire du même type

Un type de matrice intéressant sont les **matrices diagonales,** qui sont des matrices qui ont des $0$ dans toutes les entrées hors de la diagonale. Notons que par conséquent, elles sont triangulaires supérieures et inférieures simultanément. Par exemple :

$$\begin{bmatrix}
2&0&0 \\
0&3&0\\
0&0&5
\end{bmatrix}, \begin{bmatrix}
1&0&0 \\
0&0&0\\
0&0&1
\end{bmatrix} \text{ et}
\begin{bmatrix}
0&0&0 \\
0&0&0\\
0&0&0
\end{bmatrix}$$

Si $D$ est une matrice diagonale, il est très facile de calculer ses puissances $D^p$ (par récurrence sur $p$) :

$$D = \begin{bmatrix}
a_1&0&0 \\
0&a_2&0\\
0&0&a_3
\end{bmatrix}
\implies
D^p = \begin{bmatrix}
a_1^p&0&0 \\
0&a_2^p&0\\
0&0&a_3^p
\end{bmatrix}$$

**Propriétés des matrices diagonales :**
- Elles commutent entre elles : $D_1 D_2 = D_2 D_1$
- L'inverse d'une matrice diagonale (si elle existe) s'obtient en inversant chaque élément diagonal
- Elles sont très utiles pour la diagonalisation

Une matrice $A$ de taille $n × n$, triangulaire, est inversible si et seulement si ses éléments diagonaux sont tous non nuls.

### Autres types de matrices importantes

**Matrice identité :** $I_n$ est la matrice diagonale avec des $1$ sur la diagonale :

$$I_3 = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

**Matrice nulle :** Toutes les entrées sont $0$.

**Matrice élémentaire :** Matrice obtenue en appliquant une seule opération élémentaire à la matrice identité.

## Opérations d'une seule matrice

### Transposition : $A^T$

C'est juste inverser les indices $i$ et $j$ de chaque entrée : $(A^T)_{ij} = A_{ji}$. Une matrice $n \times p$ va se transformer en $p \times n$.

**Exemple :**

$$\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{pmatrix}$$

**Théorème.**
1. $(A + B)^T = A^T + B^T$
2. $(\lambda A)^T = \lambda A^T$
3. $(A^T)^T = A$
4. $(AB)^T = B^T A^T$
5. Si $A$ est inversible, alors $A^T$ l'est aussi et on a $(A^T)^{-1} = (A^{-1})^T$.

**Noter bien l'inversion :** $(AB)^T = B^T A^T$, comme pour $(AB)^{-1} = B^{-1} A^{-1}$.

### Trace d'une matrice : $\text{tr}(A)$

C'est la somme des entrées de la diagonale principale d'une matrice carrée :

$$\text{tr}(A) = \sum_{i=1}^{n} A_{ii} = A_{11} + A_{22} + \cdots + A_{nn}$$

**Exemple :**

$$\text{tr}\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix} = 1 + 5 + 9 = 15$$

**Théorème.** Soient $A$ et $B$ deux matrices $n \times n$. Alors :
1. $\text{tr}(A + B) = \text{tr}A + \text{tr}B$
2. $\text{tr}(\lambda A) = \lambda \text{tr}A$ pour tout $\lambda \in \mathbb{K}$
3. $\text{tr}(A^T) = \text{tr}A$
4. $\text{tr}(AB) = \text{tr}(BA)$

La propriété 4 est particulièrement importante : la trace est invariante par permutation cyclique des matrices dans un produit.

### Notion de matrice symétrique et antisymétrique

Une matrice **symétrique** est une matrice $A$ telle que $A = A^T$, et une matrice **antisymétrique** est telle que $A^T = -A$. Les deux (symétriques et antisymétriques) sont forcément carrées.

**Exemples :**
- Symétrique : $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}$
- Antisymétrique : $\begin{pmatrix} 0 & 1 & -2 \\ -1 & 0 & 3 \\ 2 & -3 & 0 \end{pmatrix}$

**Propriétés importantes :**
- Une matrice antisymétrique a nécessairement des zéros sur sa diagonale principale
- L'ensemble des matrices symétriques forme un espace vectoriel
- L'ensemble des matrices antisymétriques forme aussi un espace vectoriel
- Ces deux espaces sont supplémentaires dans $M_n(\mathbb{K})$

**Théorème intéressant**. Toute matrice est la somme d'une matrice symétrique et d'une matrice antisymétrique.

**Preuve**. Soit $A$ une matrice. Définissons $B = \frac{1}{2}(A + A^T)$ et $C = \frac{1}{2}(A - A^T)$. Alors d'une part $A = B + C$; d'autre part $B$ est symétrique, car $B^T = \frac{1}{2}(A^T + (A^T)^T) = \frac{1}{2}(A^T + A) = B$; et enfin $C$ est antisymétrique, car $C^T = \frac{1}{2}(A^T - (A^T)^T) = -C$.

Cette décomposition est unique et s'appelle la **décomposition symétrique-antisymétrique** d'une matrice.
