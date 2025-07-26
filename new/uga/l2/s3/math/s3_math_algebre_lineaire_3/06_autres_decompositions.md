# 06 // autres décompositions

Date de création: December 12, 2022 1:40 PM
Modifié: June 10, 2023 9:30 PM

# Qu’est-ce une décomposition ?

## Définition

Une *décomposition* est une manière de réécrire une matrice $A$ comme l’opération de différentes matrices. La diagonalisation est la décomposition qu’on a vu jusqu’à ce moment : $A =PDP^{-1}$. 

Pareil, la trigonalisation est une autre décomposition : $A = PTP^{-1}$, où $T$ matrice triangulaire.

# Décomposition LU

## Matrice de permutation

Avant d’aborder la décomposition, il faut expliquer qu’est-ce qu’une **matrice de permutation**. Elle est simplement une matrice $P$ tel que chaque ligne et colonne à un seul $1$ et des $0$ partout. La matrice identité est une **matrice de permutation**, par exemple, mais aussi si on inverse les lignes ou colonnes de l’identité. 

## Décomposition LU : $P^{-1}A=LU$

Soit $A$ une matrice **inversible**. Donc, on peut réécrire $A$ comme : 

$$
P^{-1}A=LU \space \text{ou} \space A=PLU
$$

où $P$ est une matrice de permutation, $L$ est une matrice triangulaire inférieure ($L$ de “lower”) et $U$ est une matrice triangulaire supérieure ($U$ de “upper”). Parfois, on peut ramener la matrice de permutation $P$ à la matrice identité.

# Matrices orthogonales et décomposition QR

## Matrice orthogonale : $Q$

Une matrice orthogonale est une matrice $Q$ telle qu’elle vérifie deux conditions :

1. La norme ou magnitude des vecteurs colonne vaut $1$
2. Le produit scalaire des vecteurs colonnes différents vaut $0$
Ceci implique que les vecteurs sont deux à deux orthogonaux.

### Propriétés

- $Q^{T}Q=I$
- $\det(Q)=\pm 1$,
- $Q^{-1}=Q^T$
- Si $Q$ est une matrice de passage de une base $B_1$ à une base $B_2$, donc la matrice de passage de $B_2$ à $B_1$ est $Q^{T}$.

## Décomposition QR : $A=QR$

Pour une matrice $A$, 

$$
A=QR
$$

Où $Q$ est une matrice orthogonale et $R$  est une matrice triangulaire supérieure.

En plus, si $A$ est inversible, il existe une unique décomposition QR tel que les coefficients de $R$ soient strictement positifs. Telle décomposition est **unique**.

# Matrice de covariance et ACP

## Avant, matrice symétriques : $M=M^T$

Une matrice symétrique est une matrice $M$ telle que $M = M^T$. Une propriété est que **toute matrice symétrique réelle est diagonalisable** : il existe $Q$ orthogonale tel que $M=QD^TQ$.

## Matrice de covariance : $M=\big[m_{i,j}\big],\hspace{4pt} m_{i,j}=\text{Cov}(i,j)$

Une matrice de covariance est une matrice $M$ qui contient la covariances de deux coordonnés $i,j$ d’un vecteur aléatoire (càd. un vecteur qui contient des variables aléatoires ou variables statistiques) dans le coefficient $(i,j)$ de la matrice. 

Par exemple, supposons des variables statistiques d’un vin : prix $X_1$, dégrées d’alcool $X_2$ et âge $X_3$. Alors le vecteur colonne aléatoire qui leur représentent est $\bold{X} = (X_1,X_2,X_3)^T$.

On construit alors une matrice de covariance à partir du vecteur aléatoire $\bold{X}$ :

$$
M=
\begin{bmatrix}
\text{var}(X_1) & \text{cov}(X_1,X_2) & \text{cov}(X_1,X_3) \\
\text{cov}(X_2,X_1) & \text{var}(X_2) & \text{cov}(X_2,X_3) \\
\text{cov}(X_3,X_1) & \text{cov}(X_3,X_2) & \text{var}(X_3)
\end{bmatrix}
$$

## ACP : Analyse en composantes principales

Avant d’expliquer qu’est-ce que l’analyse en composantes principales, il faut rappeler un peu de statistique. Supposons deux vecteurs aléatoires : l’un avec deux composants, et l’autre avec huit composants. Cela veut dire qu’on a besoin de deux vecteurs de **base** (canonique) pour représenter chaque entrée du premier vecteur aléatoire. Analogiquement, huit vecteurs de base pour le deuxième vecteur aléatoire.

On sait qu’on peut observer le vecteur de deux composants avec une nuage de points, et il reste facilement interprétable. D’autre part, on ne peut pas observer une nuage de points en huit dimensions. Cela serait idéel si on pourrait l’observer en deux dimensions ou trois, c’est ici l’intérêt de l’ACP : **on réduira la dimension de nos données essayant de conserver leur aspects les plus “importants”**.

Ici, “réduire la dimension” veut dire réduire la quantité de vecteurs nécessaires pour représenter une entrée de données. En résumé, on le fera à travers des éléments qui apportent le plus de variance totale à nos donnés.

(Dans ce contexte, la variance “totale” de l’ensemble de données ou nuage des points multidimensionnel est simplement la somme des variances de chaque élément)

### Étape #1 : standardiser les données, matrice de covariance

Ayant clarifier l’objectif, la première chose à faire est de standardiser les données, càd. on centre les données autour de $0$ et on réduit la variance à $1$. Ceci est un pas super important !

Supposons qu’on un vecteur aléatoire qui représente un couple de prix en dollars et mètres carrés des maisons sur un district. Normalement, le prix en dollars sera exprimé dans un ordre de magnitude beaucoup plus grand que la taille en mètres carrés. En 2022, le prix moyenne par pied carré est $\$244$ aux États-Unis, donc pensons que une maison de $1.000$ mètres carrés vaut en moyenne $\$244.000$ ! La différence d’ordre de magnitude est significative, et elle sera encore plus significative dans le calcule des variance de chaque élément.

Cette différence ordre de magnitude nous féra penser, lors de regarder l’ordre de magnitude de la variance, que le prix apporte plus à la variance totale que les mètre carrés (ce qui n’est pas forcément vrai). Par contre, si on standardise les données, on parlera du même ordre de magnitude pour les variances aussi.

Une fois les données standardisées, on calcule la matrice de covariance des données standardisées, comme ci-dessous. On note que la diagonale ne porte que des $1$.

![On reprend ici l’exemple des bouteilles de vin.](new/uga/l2/s3/math/s3_math_algebre_lineaire_3/06_autres_decompositions/untitled.png)

On reprend ici l’exemple des bouteilles de vin.

### Étape #2 : diagonalisation de la matrice de covariance

Regardons à nouveau notre matrice de covariance. On voit que pour chaque élément, il existe une entrée qui représente sa relation de variance par rapport aux autres éléments. Donc, on pourrait interpréter chaque colonne comme un vecteur aussi ! Particulièrement, pour la colonne prix, l’interprétation serait “les **unités de covariance** entre le prix et l’élément $i$”, et comme ça pour les autres.

Qu’est-ce qui ce passe si on tente de diagonaliser cette matrice ? Si $A$ est notre matrice de covariance, donc $A=PDP^{-1}$  sera sa diagonalisation, avec $D$ qui portera les valeurs propres et $P$ les vecteur propres.

Ici, il faudrait bien s’arrêter pour interpréter ce qu’on a. Si on voit la matrice de covariance $A$ comme une transformation linéaire, les vecteur propres sont ces vecteurs qui sont seulement escaladées par un coefficient et qui gardent la même direction. En plus, les valeurs propres nous diront combien de chaque vecteur propre est nécessaire pour reconstruire les covariances $A$.

Du départ, notre base était la base canonique : chaque vecteur de la base canonique ajoute une unité de chaque élément qui compose un vin, et on reconstruit tous les éléments du vin avec la somme escaladée de chaque vecteur.

Maintenant, avec la vecteurs propres comme base, chaque vecteur représente un “mélange” de chaque élément (prix, dégrées d’alcool…) et pour reconstruire un vin on prendra une certaine quantité $\lambda_i$ de chaque vecteur. Ceci est simplement l’interprétation de la partie $PD$ de la diagonalisation $A=PDP^{-1}$ .

Si on prend un vin (une donnée) et on fait une combinaison linéaire avec un vecteur propre (cette “mélange” d’éléments), on obtient ce qu’on appelle un “facteur” ou “composant”. 

> Jusqu’ici, un **détail important** à retenir ce que la trace est une invariante de similitude, donc $\text{Tr}(A) = \text{Tr}(D)$. En plus, la trace de $A$ est la variance total de l’ensemble de données standardisées.

Un autre **détail important** est que les vecteurs propres dans $P$ doivent être orthogonaux deux à deux et de norme $1$, donc $P$ est une matrice orthogonale.
> 

### Étape #3 : réduction de dimension

Notons que dans $D$, il aura des valeurs propres plus grands qu’autres, ce qui signifie que il faudrait plus d’un vecteur propre que d’autre pour reconstruire les variances. C’est ici où on fait la réduction de dimension : si chaque vecteur représente une dimension, et on a besoin d’une quantité petite d’un certain vecteur propre pour reconstruire les covariances (càd. un valeur propre petit), **on pourrait juste négliger tel vecteur propre**. Particulièrement, on voit combien d’un vecteur propre (son valeur propre) fait comme proportion de la variance totale : $\frac{\lambda_i}{\text{Tr}(A)}$.

Il faut garder en tête que la plus de variance un vecteur garde du *dataset*, la plus d’information il en contient ! 

Chaque fois qu’on prend des vins (vecteurs ligne $\bold{x}_1, \dots, \bold{x}_n$) et on prend sa combinaison linéaire avec le vecteur de plus grand $\lambda$, $\bold{w}_1$, on obtient une constante résultat $(F_1)_i$ qui est le “facteur” du vin $i$ sous $\bold{w}_1$. Supposons qu’on garde tous les facteurs $(F_1, \dots, F_n)$ comme des données dans le vecteur ligne $\bold{F}_1$ associé au vecteur propre $\bold{w}_1$, alors il en résulte que $\bold{w}_1$ est tel vecteur colonne qui maximise la variance de $\bold{F}_1$. Formellement,

$$
\bold{w}_1=\argmax_{||\bold{w}||=1} \left\{ \sum_i(F_1)^2_i \right\}=\argmax_{||\bold{w}||=1} \left\{ \sum_i(\bold{x}_i \cdot \bold{w})^2 \right\}
$$

On pourra prendre un autre vecteur colonne $\bold{w}_i$ et faire la même opération avec chaque vin $\bold{x}_i$, et la variance des facteurs résultats dans $\bold{F}_i$ sera plus petite que $\bold{F}_1$. De même, le vecteur propre $\bold{w}_2$ est tel qui maximise la variance et est différent de $\bold{w}_1$, et comme ça successivement.

Normalement avec l’ACP, on veut avoir des données originalement dans beaucoup de dimensions représentables en un nombre de dimensions qu’on puisse voir, donc normalement on garde au maximum les trois vecteurs propres qui contiennent le plus de variance totale du *dataset* ou nuage de points original.

### Étape #4 : reconstruction des données réduites

Dans l’exemple du vin, on garde $\bold{w}_1$ et $\bold{w}_2$. Seulement avec eux deux, on peut reconstruire $86\%$ de la variance totale, c’est donc un sacrifice qui vaut le coup. Finalement, on détermine $F_1$ et $F_2$ de chaque vin et on graphique la nouvelle nuage en $2$ dimensions. Le résultat devrait semble quelque chose comme suit :

![Il faudrait dire que les vecteurs $\bold{w}_1$ et $\bold{w}_2$ font parties des lignes de meilleure régression linéaire tout au même temps qu’elle sont orthogonaux entre elles.](new/uga/l2/s3/math/s3_math_algebre_lineaire_3/06_autres_decompositions/untitled_1.png)

Il faudrait dire que les vecteurs $\bold{w}_1$ et $\bold{w}_2$ font parties des lignes de meilleure régression linéaire tout au même temps qu’elle sont orthogonaux entre elles.

![Un autre exemple sorti de Wikipédia d’un *dataset* de dimension réduite*.* Notons les clairs groupassions en vert et bleu des données après la transformation.](new/uga/l2/s3/math/s3_math_algebre_lineaire_3/06_autres_decompositions/untitled_2.png)

Un autre exemple sorti de Wikipédia d’un *dataset* de dimension réduite*.* Notons les clairs groupassions en vert et bleu des données après la transformation.

Alors, quand est l’ACP utile ? Déjà, pour pouvoir graphique les données dans une dimension humainement appréciable. Mais, aussi ce graphique nous permet de reconnaître des groupes (clusters) et des données (”vins”) qui sont proches l’une de l’autre.

[Principal component analysis - Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)

[](https://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-l-des-multi.pdf)