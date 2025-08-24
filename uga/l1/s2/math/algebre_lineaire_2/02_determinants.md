# 02 // déterminants

# Déterminants élémentaires : dimension $2$ et $3$

## Matrice $2\times2$

$$
\det\left(
\begin{bmatrix}
a&b\\c&d
\end{bmatrix}
\right)=ad-bc
$$

$$
\begin{array}{ccc}
a & \rightarrow & d \\
\downarrow & & \downarrow \\
c & \rightarrow & b
\end{array}
$$

Petit astuce pour bien rappeler : on descend par la ligne bleue en multipliant, puis par la ligne orange en multiplient.

## Matrice $3 \times 3$

$$
A=\begin{bmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{bmatrix} \implies \begin{align*}\det(A)&=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}
\\&-(a_{31}a_{22}a_{13}-a_{32}a_{23}a_{11}-a_{33}a_{21}a_{12})\end{align*}
$$

- Règle de Sarrus :
    $$
    \begin{array}{|ccc|cc}
    a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\
    a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\
    a_{31} & a_{32} & a_{33} & a_{31} & a_{32} \\
    \end{array}
    $$
    
    - On recopie les deux premières colonnes à droite de la matrice (colonnes grisées)
    - On additionne les produits de trois termes en les regroupant selon la direction de la diagonale descendante (à gauche)
    - On soustrait ensuite les produits de trois termes regroupés selon la direction de la diagonale montante (à droite)

# Expliquant le déterminant

## Définition et interprétation

Le déterminant est finalement le coefficient par lequel les aires sont multiplies passant de la base canonique a une autre base.

On caractérise le déterminant comme une fonction ou application d'une matrice à une coefficient réel.

$$
\det:M_n(\mathbb{K})\mapsto \mathbb{K}
$$

### Premières propriétés

### Optionnel : clarification de la propriété #1

- Prenons deux matrices, $A$ et $B$, de la même taille et dont ses colonnes sont les mêmes à exception d'une : la colonne $j$.
- Les coefficients de $A$ dans la colonne $j$ sont $\{a_{1j}, a_{2j}, ... , a_{ij}\}$. Respectivement pour la matrice $B$.
- Imaginons une troisième matrice, $C$, égale à $A$ et $B$ à exception de la colonne $j$, où dans chaque ligne $i$, on va prendre une combinaison linéaire des coefficients $a_{ij}$ et $b_{ij}$, avec coefficients $λ$ et $µ$.
- Finalement, $\text{det}(C) = λ \cdot \text{det}(A) + µ \cdot \text{det}(B)$.
    
    $$
    \begin{vmatrix} 
    a_{11} & \cdots & \lambda a_{1j} + \mu b_{1j} & \cdots & a_{1n} \\
    a_{21} & \cdots & \lambda a_{2j} + \mu b_{2j} & \cdots & a_{2n} \\
    \vdots & \ddots & \vdots & \ddots & \vdots \\
    a_{n1} & \cdots & \lambda a_{nj} + \mu b_{nj} & \cdots & a_{nn}
    \end{vmatrix} = \lambda
    \begin{vmatrix} 
    a_{11} & \cdots & a_{1j} & \cdots & a_{1n} \\
    a_{21} & \cdots & a_{2j} & \cdots & a_{2n} \\
    \vdots & \ddots & \vdots & \ddots & \vdots \\
    a_{n1} & \cdots & a_{nj} & \cdots & a_{nn}
    \end{vmatrix} + \mu
    \begin{vmatrix} 
    a_{11} & \cdots & b_{1j} & \cdots & a_{1n} \\
    a_{21} & \cdots & b_{2j} & \cdots & a_{2n} \\
    \vdots & \ddots & \vdots & \ddots & \vdots \\
    a_{n1} & \cdots & b_{nj} & \cdots & a_{nn}
    \end{vmatrix}
    $$
    
    - (Les barres de valeur abs. ici signifie le det.)
- **Propriété #1** : le déterminant est linéaire par rapport à chaque vecteur colonne, les autres étant fixés
- **Propriété #2** : si une matrice $A$ a deux colonnes identiques, alors son déterminant est nul
- **Propriété #3** : le déterminant de la matrice identité $I_n$ vaut $1$, pour tout $n$ naturel

### Remarque : ce qui rend le $\det$ "spéciale"

Ils existent des fonctions/applications comme $M_n(\mathbb{K}) \mapsto \mathbb{K}$ qui ne sont pas le déterminant, mais le $\det$ en est une.

- Une application de $M_n(\mathbb{K}) \rightarrow \mathbb{K}$ qui satisfait la propriété #1 est appelée forme multilinéaire.
- Si elle satisfait la propriété #2, elle est appelée alternée.
- Le déterminant est donc la seule forme multilinéaire alternée qui prend comme valeur 1 sur la matrice $I_n$.

## Propriétés et opérations élémentaires

### Matrices $0_n$ et $I_n$

Reprenant les premières propriétés de la section précédente, on peut déduire deux faits importants :

- le déterminant de la matrice nulle $0_n$ vaut 0 (par la propriété (ii))
- le déterminant de la matrice identité $I_n$ vaut 1 (par la propriété (iii))

### Effets des opérations élémentaires sur le déterminant

Soit $A'$ une matrice $A$ à laquelle on à appliqué une opération élémentaire sur la colonne $i$.

- **Escalade** : $\text{det}(A') = λ \cdot \text{det}(A)$. (découle de propriété #1)
- **Somme escaladée** : $\text{det}(A') = \text{det}(A)$. Ça ne change pas.
- **Échange** : $\text{det}(A') = -\text{det}(A)$. Le signe du déterminant change.

**Corollaire.** Si une colonne $C_i$ de la matrice $A$ est une combinaison linéaire des autres colonnes, alors $\text{det}(A) = 0$.

## Opérations élémentaires $E$ comme un produit : $A' = A\cdot E$

Supposons une matrice quelle conque $A$, à la quelle on veut appliquer les trois opérations élémentaires. On va définir une matrice $E$, telle que, si on applique une certaine opération linéaire à $A$, ce serait le même que si on faisait $A \cdot E$. 

La matrice après l'opération élémentaire serait $A' = A \cdot E$, où **$E$ décrit donc l'opération élémentaire**.

### Qu'est-ce que $E$ pour chaque opération élémentaire

- **Escalade** : si on multiplie $C_i$ par $λ$, on peut la réécrire avec $E = \text{diag}(1, . . . ,1,λ,1, . . . ,1)$, qui est la matrice diagonal avec $λ$ en position $(i,i)$ et $1$ d'ailleurs.
- **Somme escaladée** : si on ajout $λ \cdot C_j$ à $C_i$, $E$ serait comme la matrice identité, mais avec $λ$ en position $(j, i)$. Fais attention à l'ordre de $j$ et $i$ !
- **Échange** : si on change $C_i$ par $C_j$, $E$ serait comme la matrice identité, mais avec des $0$ en $(i,i)$ et $(j,j)$, et avec des 1 en $(i,j)$ et $(j,i)$.

### Le déterminant de $E$

- Si $E$ représente une escalade : $\text{det}(E) = λ$.
- Si $E$  représente une somme escaladée : $\text{det}(E) = 1$.
- Si $E$ représente un échange : $\text{det}(E) = -1$.
- $\text{det}(A') = \text{det}(A \cdot E) = \text{det}(A) \cdot \text{det}(E)$, si $E$ représente une opération élémentaire.

**Note pratique**. On peut transformer une matrice $A$ avec un suite d'opérations élémentaires dans une matrice triangulaire (supérieure ou inférieure, peu importe) $A'$ et après multiplier $\text{det}(A')$ avec le $\det$ de tous les $E$ intermédiaires pour arriver à $\text{det}(A)$.

## Autres propriétés

### Déterminant d'autres opérations

- Déterminant d'un produit : $\text{det}(AB) = \text{det}(A)  \cdot \text{det}(B)$
- Déterminant des matrices inversibles : $\text{det}(A^{-1}) = 1/\text{det}(A)$.
    - Une matrice est inversible $\leftrightarrow$ son déterminant est non nul.
    - Aussi, deux matrices semblables ont le même déterminant.
- Déterminant de la transposée : $\text{det}(A^T)$ = $\text{det}(A)$.
    - Une conséquence du dernier résultat est que, par transposition, tout ce que l'on a dit des déterminants à propos des colonnes est vrai pour les lignes.

### Déterminants de matrices triangulaires

Le déterminant d'une matrice triangulaire de dimension $n \times n$, soit supérieure ou inférieure, est égal au produit des entrées diagonaux, peu importe les autres entrées.

$$
A_n^\text{inf}=\begin{bmatrix}
a_{11}&0&\cdots&0\\
a_{21}&a_{22}&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
a_{n1}&a_{n2}&\cdots&a_{nn}\end{bmatrix}

\text{ ou }

A_n^\text{sup}=\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
0&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&a_{nn}\end{bmatrix} 

\\[12pt]

\implies\det(A)=a_{11}a_{22}\dots a_{nn}
$$

# Calculs de déterminants de taille générale $n$

## Préparation

Soit $A$ une matrice carrée. On va appeler $A_{ij}$ à la matrice extraite qu'on obtient en effaçant la ligne $i$ et la colonne $j$. Voyons cet exemple :
$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix} \quad \Rightarrow \quad
A_{32} = \begin{bmatrix}
1 & 3 \\
4 & 6
\end{bmatrix} \quad \Rightarrow \quad
\det(A_{32}) = 1 \cdot 6 - 3 \cdot 4 = 6 - 12 = -6
$$

On introduit l'idée d'un *mineur* : un "mineur d'ordre $n-p$" est le déterminant d'une matrice extraite $A'$ d'une matrice de base $A$ à laquelle on a appliqué la suppression de lignes et colonnes $p$ fois. Ainsi et dans cet exemple, le $\text{det}(A_{ij})$ est un mineur d'ordre $n-1$ de la matrice $A$. 

Une autre idée importante pour la suite est le *cofacteur* : le "cofacteur de $A$ relatif au coefficient $a_{ij}$" est $C_{ij}$ = $(-1)^{i+j} \cdot \text{det}(A_{ij})$. Dans cette exemple, on a que :

$$
C_{32}=(-1)^{3+2}\det A_{32}=(-1)\times(-11)=11
$$

## Développement suivant une ligne ou une colonne

On reprend les idées de mineur et cofacteur pour présenter la méthode de calcul général d'un déterminant. Notamment, c'est la méthode de "développement d'une matrice", et on peut la faire par rapport aux lignes (indice $i$) ou colonnes (indice $j$).

$$
\text{Dev. par rapport aux lignes :} \det A=\sum_{i=1}^n(-1)^{i+j}a_{ij}\det A_{ij}=\sum_{i=1}^na_{ij}C_{ij}
$$$$
\text{Dev. par rapport aux colonnes :}\det A=\sum_{j=1}^n(-1)^{i+j}a_{ij}\det A_{ij}=\sum_{j=1}^na_{ij}C_{ij}
$$

Ceci est utile pour calculer le déterminant de matrices de grande taille par récurrence, jusqu'à ce qu'on arrive à des matrices de taille $3$ ou $2$, où on peut utiliser les méthodes élémentaires présentées au début de cours.

Le choix de développer par rapport aux lignes ou aux colonnes sera par convenance, particulièrement si on voit une ligne ou colonne qui contient plusieurs zéros, ce qui facilite le calcul. Voyons cet exemple :
$$
\begin{vmatrix}
2 & 0 & 0 \\
1 & 3 & 4 \\
0 & 2 & 1
\end{vmatrix} = 2 \cdot \begin{vmatrix}
3 & 4 \\
2 & 1
\end{vmatrix} = 2(3 \cdot 1 - 4 \cdot 2) = 2(3 - 8) = 2 \cdot (-5) = -10
$$

Finalement, si on développe par rapport aux lignes ou aux colonnes, il ne faut pas oublier de changer le signe du coefficient selon la "matrice de signes", qui est important pour le facteur $(-1)^{i+j}$ :

$$
\begin{bmatrix}
+ & - & + & \dots \\
- & + & - & \dots \\
+ & - & + & \dots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$

## **Inverse d'une matrice de taille générale $n$**

On parle des inverses de matrice ici car elle sont liées au déterminant. Si $A$ est une matrice carrée, on définit $\text{Com}(A)$ comme la comatrice de $A$, qui contient les cofacteurs $C_{ij}$ en l'entrée $(i,j)$ : 

$$
\text{Com}(A)=[C_{ij}]=
\begin{bmatrix}
C_{11}&C_{12}&\cdots&C_{1n}\\
C_{21}&C_{22}&\cdots&C_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
C_{n1}&C_{n2}&\cdots&C_{nn}
\end{bmatrix}
$$

Finalement, cette matrice nous aide à calculer l'inverse de $A$ comme suit :

$$
A^{-1}=\frac{1}{\det A}\text{Com}(A)^T
$$

# **Applications des déterminants**

## Règle **de Cramer : résoudre des syst. d'éq. lin. avec le $\det$**

La règle de Cramer permet de calculer le vecteur solution $[x_1,\dots,x_n]^T$ à un système d'équations linéaires (ayant autant d'équations que des inconnus) en se servant du déterminant de la matrice des coefficients $A$ (et supposant que $\det A \ne 0$, sinon la règle ne marche pas).

On commence par écrire le système comme $A\mathbf{X}=\mathbf{B}$.

$$
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2 \\
\vdots \\
b_n
\end{pmatrix}
$$

À partir de la matrice $A$, on définit la matrice $A_j$, qui est une matrice presque pareille à $A$ mais qui remplace la colonne $j$ par le vecteur colonne $B$.

$$
A_j = 
\begin{pmatrix}
a_{11} & \cdots & a_{1,j-1} & b_1 & a_{1,j+1} & \cdots & a_{1n} \\
a_{21} & \cdots & a_{2,j-1} & b_2 & a_{2,j+1} & \cdots & a_{2n} \\
\vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & \cdots & a_{n,j-1} & b_n & a_{n,j+1} & \cdots & a_{nn}
\end{pmatrix}
$$

Finalement, l'unique vecteur solution $[x_1,\dots,x_n]^T$ est donné par le calcul suivant :

$$
x_1=\frac{\det A_1}{\det A},\hspace{4pt}x_2=\frac{\det A_2}{\det A}, \hspace{4pt} \dots, \hspace{4pt}x_n=\frac{\det A_n}{\det A}
$$

## Relation avec les bases

On se donne une base $B$ de $E$ et on veut savoir si une famille de vecteurs $A$ est une base de $E$. On écrit chaque vecteur colonne dans une matrice, ou chaque vecteur est exprimé avec la base $B$.

$$
\begin{align*}
A=\{v_i,v_2,\dots,v_n\}\text{ est une base} &\iff \text{rg}(A)=n
\\ &\iff A \text{ est inversible}
\\ &\iff \det A \ne0
\end{align*}
$$

## Relation avec le rang

Le rang d'une matrice $A$ est le plus grand entier $r$ tel qu'il existe au moins un mineur d'ordre $r$ extrait de $A$ non nul.

$$
\text{rg}(A) = r \iff \text{tous les mineurs d'ordre } r+1 \text{ sont nuls et il existe au moins un mineur d'ordre } r \text{ non nul}
$$

$$
A \text{ est inversible } \iff \det A \neq 0 \iff \text{rg}(A) = n
$$