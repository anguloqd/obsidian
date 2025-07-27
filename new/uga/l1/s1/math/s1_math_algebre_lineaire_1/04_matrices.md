# 04 // matrices

# Opérations basiques entre deux matrices

## Addition de matrices

<aside>
🤷‍♂️ En vrai, je connaissais déjà que c’est la somme entrée par entrée entre deux matrices.

</aside>

## Multiplication de matrices

<aside>
🤷‍♂️ Pareil, je savais déjà que le produit entre deux matrices est le produit matriciel ou produit *point* de chaque ligne de la matrice gauche avec chaque colonne de la matrice droite.

</aside>

<aside>
💡 Pièges communes :

- Le produit n'est pas commutatif en général. Juste avec une matrice et son inverse, et aussi une matrice et l'identité.
- $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.
- $AB = AB$ n'implique pas $B = C$. On peut avoir $AB = AC$ et $B \ne C$.
</aside>

Propriétés :

- Associativité : $A(BC) = (AB)C$
- Distributivité : $A(B + C) = AB + AC \text{ et } (B + C)A = BA+ CA$.
- $A \cdot 0 = 0 \text{ et } 0 \cdot A = 0$.

# **Formule du binôme**

## Lorsque $AB=BA$…

Comme la multiplication n’est pas commutative, les identités binomiales usuelles sont fausses. En particulier, $(A + B)^2$ ne vaut en général pas $A^2 + 2AB + B^2$, mais on sait seulement que $(A+B)^2 = A^2 + AB + BA+ B^2$.

Si $AB = BA$ (si $A$ et $B$ commuent sous la multiplication), alors la formule du binôme applique. Dans la pratique, l’une des deux matrices est souvent la matrice identité qui commute avec tout.

# **Inverse d'une matrice**

## $A^{-1}$ telle que $A A^{-1}=I$

Plus généralement, quand $A$ est inversible, pour tout $p ∈ N$, on note $A^{-p} = (A^{-1})^p$.

- L’ensemble des matrices inversibles de $M_n(K)$ est noté $G L_n (K)$.

**Simplification par une matrice inversible.** Soient $A$ et $B$ deux matrices de $M_n(K)$ et $C$ une matrice inversible de $M_n(K)$. Alors l’égalité $AC = BC$ implique l’égalité $A = B$ (on multiplie par la droite par $C^{-1}$ aux deux côtés). 

- Pour les matrices 2x2, la formule est :

$$
A = \begin{pmatrix} a &b \\ c & d \end{pmatrix} \iff A^{-1}=\frac{1}{ad-bc} \begin{pmatrix} d &-b \\ -c & a \end{pmatrix}
$$

- Pour tout autre matrice, fais la méthode de Gauss-Jordan.

# **Types de matrices**

Avant de les présenter, on devrait connaître l’équivalence par lignes. Deux matrices $A$ et $B$ sont dites ***équivalentes par lignes*** si l’une peut être obtenue à partir de l’autre par une suite d’opérations élémentaires sur les lignes. On note $A ∼ B$.

- Les **opérations élémentaires** sont : escalader une ligne, sommer une autre ligne escaladée et déplacer deux lignes.

## Matrices échelonnées

**Matrices échelonnées** : le nombre de zéros commençant une ligne croît strictement ligne par ligne jusqu’à ce qu’il ne reste plus que des zéros (si c'est le cas, mais il peut se passer que il n'y a pas des lignes purement des zéros). Par exemple :

$$
\begin{bmatrix}
1&a_0&a_1&a_2&a_3 \\
0&0&2&a_4&a_5 \\
0&0&0&1&a_6
\end{bmatrix}
$$

**Matrices échelonnées réduites** : est une matrice échelonnée tel que

- le premier coefficient non nul d’une ligne (non nulle) vaut $1$
- et c’est le seul élément non nul de sa colonne.

$$
\begin{bmatrix}
1&0&a_1&0&b_1 \\
0&1&a_2&0&b_2 \\
0&0&0&1&b_3
\end{bmatrix}
$$

- Soit $A ∈ M_n (K)$. La matrice $A$ est inversible si et seulement si sa forme échelonnée réduite est la matrice identité $I_n$.
    
    ![untitled](new/uga/l1/s1/math/s1_math_algebre_lineaire_1/ressources/04_matrices_untitled.png)
    

## Matrices triangulaires

Les m**atrices triangulaires supérieures** sont celles dont leur coefficients strictement au dessous de la diagonal sont $0$. La définition est analogue pour les matrices triangulaires inférieures, juste que dans ce cas-ci au-dessous de la diagonale principale.

Un type de matrice intéressant sont les m**atrices diagonales,** qui sont des matrices qui ont des $0$ dans toutes les entrées hors de la diagonale. Notons que par conséquence, elles sont triangulaires supérieures et inférieures simultanément. Par exemple :

$$
\begin{bmatrix}
2&0&0 \\
0&3&0\\
0&0&5
\end{bmatrix}, \begin{bmatrix}
1&0&0 \\
0&0&0\\
0&0&1
\end{bmatrix} \text{et}
\begin{bmatrix}
0&0&0 \\
0&0&0\\
0&0&0
\end{bmatrix}
$$

Si $D$ est une matrice diagonale, il est très facile de calculer ses puissances $D^p$ (par récurrence sur $p$) :

$$
D = \begin{bmatrix}
a_1&0&0 \\
0&a_2&0\\
0&0&a_3
\end{bmatrix}
\implies
D^p = \begin{bmatrix}
a_1^p&0&0 \\
0&a_2^p&0\\
0&0&a_3^p
\end{bmatrix}
$$

Une matrice $A$ de taille $n × n$, triangulaire, est inversible si et seulement si ses éléments diagonaux sont tous non nuls.

# Opérations d’une seule matrice

## **Transposition : $A^T$**

C'est juste inverser les indices $i$ et $j$ de chaque entrée. La matrice $n \times p$ va se transformer à $p \times n$.

![untitled](new/uga/l1/s1/math/s1_math_algebre_lineaire_1/ressources/04_matrices_untitled_1.png)

## **Trace d’une matrice : $\text{tr}(A)$**

C'est la somme des entrées de la diagonal principale d'une matrice.

![untitled](new/uga/l1/s1/math/s1_math_algebre_lineaire_1/ressources/04_matrices_untitled_2.png)

## Notion de m**atrice symétrique et antisymétrique**

Une matrice symétrique est une matrice $A$ telle que $A = A^T$ , et une matrice antisymétrique est telle que $-A = A^T$ Les deux (symétriques et antisymétriques) sont forcément carrés.

**Théorème intéressant**. Toute matrice est la somme d’une matrice symétrique et d’une matrice antisymétrique.

![untitled](new/uga/l1/s1/math/s1_math_algebre_lineaire_1/ressources/04_matrices_untitled_3.png)