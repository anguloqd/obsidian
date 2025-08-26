## 02 // rappels sur les matrices

## Règles générales sur le déterminant d’une matrice

### Linéarité du déterminant

Un déterminant est dit “linéaire” par rapport aux lignes et colonnes. C’est-à-dire, commençons avec une matrice écrite comme une liste de vecteurs colonnes $c_1, …, c_n$ :

$$\det(M)=\det(c_1,\dots,c_n)$$

Donc, escalader **UNE SEULE** colonne multiplie **TOUT** le déterminant de la matrice originale par $\lambda$. Similairement, additionner un vecteur colonne $\mathbf{x}$ de constantes à une colonne de la matrice $M$ nous donne le deuxième résultat.

$$\det(c_1,\dots, \lambda c_i,\dots, c_n)= \lambda\det(c_1,\dots,c_n)\text{, et}
\newline
\det(c_1+\mathbf{x}, \dots, c_n) = \det(c_1,\dots,c_n)+\det(\mathbf{x},\dots,c_n)$$

**Note** : le prof. a fait ça (factoriser un colonne) dans le 1er control, 2ème exo de diagonalisation.

On peut finalement écrire l’opération d’escalade et somme sur une même ligne de manière plus compacte comme suit :

$$\det(c_1,\dots,\lambda c_i + \mathbf{x}, \dots, c_n) = \lambda\det(c_1,\dots,c_i,\dots c_n) +\det(c_1,\dots,\mathbf{x},\dots,c_n)$$

On en déduit que si $M$ est une matrice carré de taille $n$, donc $\det(\lambda M) = \lambda^n \det(M)$.

### Alternance du déterminant

Si on change de position deux colonnes ou lignes quelles conques, le déterminant change de signe. Exemple : $\det(c_1, c_2, c_3) = -\det(c_1, c_3, c_2)$.

### Déterminant et inversibilité

Si $A$ et $B$ sont eux matrices carrés de même taille $n$, donc $\det(AB) = \det(A)\det(B)$.

En plus, $M$ est une matrice inversable $\iff \det(M) \ne 0$.

Finalement, on ne change pas la valeur d’un déterminant en ajoutant à une colonne ou ligne une combinaison linéaire des autres colonnes ou lignes. En fait, si on a une matrice avec un vecteur qui est combinaison linéaire des autres, on peut le barrer et garder le même déterminant de la matrice originale.

## Pivot de Gauss et les déterminants

### Astuce par rapport aux matrices triangulaires

La méthode de Pivot de Gauss nous est utile car on peut transformer des matrices quelles conques en triangulaires. Ce dernier nous permet facilement de calculer le déterminant d’une matrice car **ce serait seulement le produit des entrées diagonaux dans le cas d’une matrice triangulaire**.

## Calculs de déterminants de taille générale $n$

### Préparation

Soit $A$ une matrice carrée. On va appeler $A_{ij}$ à la matrice extraite qu'on obtient en effaçant la ligne $i$ et la colonne $j$. Voyons cet exemple :

![image (12).png](image_(12).png)

On introduit l’idée d’un *mineur* : un “mineur d’ordre $n-p$” est le déterminant d’une matrice extraite $A’$ d’une matrice de base $A$ à laquelle on a appliqué la suppression de lignes et colonnes $p$ fois. Ainsi et dans cet exemple, le $\text{det}(A_{ij})$ est un mineur d'ordre $n-1$ de la matrice $A$.

Une autre idée importante pour la suite est le *cofacteur* : le “cofacteur de $A$ relatif au coefficient $a_{ij}$” est $C_{ij}$ = $(-1)^{i+j} \cdot \text{det}(A_{ij})$. Dans cette exemple, on a que :

$$C_{32}=(-1)^{3+2}\det A_{32}=(-1)\times(-11)=11$$

### Développement suivant une ligne ou une colonne

On reprend les idées de mineur et cofacteur pour présenter la méthode de calcul général d’un déterminant. Notamment, c’est la méthode de “développement d’une matrice”, et on peut la faire par rapport aux lignes (indice $i$) ou colonnes (indice $j$).

$$\text{Dev. par rapport aux lignes :} \det A=\sum_{i=1}^n(-1)^{i+j}a_{ij}\det A_{ij}=\sum_{i=1}^na_{ij}C_{ij}

\\[8pt]

\text{Dev. par rapport aux colonnes :}\det A=\sum_{j=1}^n(-1)^{i+j}a_{ij}\det A_{ij}=\sum_{j=1}^na_{ij}C_{ij}$$

Ceci est utile pour calculer le déterminant de matrices de grande taille par récurrence, jusqu'à ce qu'on arrive à des matrices de taille $3$ ou $2$, où on peut utiliser les méthodes élémentaires présentées au début de cours.

Le choix de développer par rapport aux lignes ou aux colonnes sera par convenance, particulièrement si on voit une ligne ou colonne qui contient plusieurs zéros, ce qui facilite le calcul. Voyons cet exemple :

![image (16).png](image_(16).png)

Finalement, si on développe par rapport aux lignes ou aux colonnes, il ne faut pas oublier de changer le signe du coefficient selon la “matrice de signes“, qui est important pour le facteur $(-1)^{i+j}$ :

$$\begin{bmatrix}
+ & - & + & \dots \\
- & + & - & \dots \\
+ & - & + & \dots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}$$

### **Inverse d'une matrice de taille générale $n$**

On parle des inverses de matrice ici car elle sont liées au déterminant. Si $A$ est une matrice carrée, on définit $\text{Com}(A)$ comme la comatrice de $A$, qui contient les cofacteurs $C_{ij}$ en l’entrée $(i,j)$ :

$$\text{Com}(A)=[C_{ij}]=
\begin{bmatrix}
C_{11}&C_{12}&\cdots&C_{1n}\\
C_{21}&C_{22}&\cdots&C_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
C_{n1}&C_{n2}&\cdots&C_{nn}
\end{bmatrix}$$

Finalement, cette matrice nous aide à calculer l’inverse de $A$ comme suit :

$$A^{-1}=\frac{1}{\det A}\text{Com}(A)^T$$

## Matrice triangulaires par blocs

### Une idée seulement utile par rapport aux déterminants

**Attention !** Ceci est seulement et uniquement possible avec la notion de triangularité et quand un bloc est nul. Pour tous les autres cas, il n’existe pas de “calculs par blocs” possibles !

$$\left|
\begin{array}{c|c}
A & B \\ \hline
0 & D
\end{array}
\right|
= \det(A)\det(D) - \cancel{\det(B)\det(0)} = \det(A)\det(D)

\newline
\text{Par exemple, }

\left|
\begin{array}{cc|cc}
1&2&3&4\\
5&6&7&8\\ \hline
0&0&9&10\\
0&0&11&12\\
\end{array}
\right|
\text{ est triangulaire par blocs.}$$
