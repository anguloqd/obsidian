# 02 // régression linéaire multiple

[Économétrie 1 - Chap. #2](ressources/02_regression_lineaire_multiple_2_chapitre2_econometrie1_20232024.pdf)

# Le modèle

## Rappel : les cinq hypothèses fondamentales

Par la suite, on va supposer les cinq hypothèses ”fondamentales” qui suivent :

- $H_1$ : $\mathbb E [u_i] = 0$
- $H_2$, la homoscédasticité ou variance constante : $\text{Var}(u_i)=\mathbb E[u_i^2]=\sigma^2_u$
- $H_3$,: la variable explicative $x_i$ est non aléatoire
- $H_4$, spécificité : le modèle est correctement spécifié.
Dans ce cas c’est linéaire, donc $y_i = \beta_0+\beta_1x_i+u_i$.
- $H_5$, non colinéarité: la variable explicative $x_i$ n’est pas constante pour toutes les observations.

> [!note]
> Les estimateurs $\hat \beta_0$ et $\hat \beta_1$ peuvent être biaisés. La source normalement vient du non respect du modèle spécifie (utiliser $\ln x$ quand ça devrait être $x$, ou vice-versa) ou de H3 : $\mathbb E [\bold x u] \ne 0$ donc $\text{Cov}(\bold x, u) \ne 0$.

Sous ces hypothèses, il découle que : 

- Les estimateurs $\hat β_0$ et $\hat β_1$ des MCO sont **sans biais et a variance minimale**, aussi appelés les estimateurs de Gauss-Markov**.** Donc :
    
    $$
    \mathbb E[\hat\beta_0]=\beta_0 \text{\hspace{8pt}et\hspace{8pt}}\mathbb E[\hat\beta_1]=\beta_1 
    $$
    
- Les variances sont les suivantes, mais il nous manque un paramètre $\sigma^2_u$.
    
    $$
    \text{Var}(\beta_1)=\frac{\sigma^2_u}{\sum_{i=1}^N(x_i-\bar x)^2}
    
    \text{\hspace{8pt}et\hspace{8pt}}
    
    \text{Var}(\beta_0)=\frac{\sigma^2_u}{n}\frac{\sum_{i=1}^Nx_i^2}{\sum_{i=1}^N(x_i-\bar x)^2}
    $$
    
- Si on prend la variances des résidus, ce serait un estimateur biaisé de $\sigma^2_u$.
Néanmoins, Il existe un estimateur sans biais de $\sigma^2_u$, où $k$ le nombre de var. explicatives. Dans ce cas, $k=1$.
    
    $$
    \hat\sigma^2_u=\frac{\sum_{i=1}^n\hat u_i^2}{N-(k+1)} \implies \mathbb E[\hat\sigma^2_u]=\sigma^2_u
    $$
    

## Généralisation à $n$ variables explicatives, changement des $H_i$

C’est juste l’inclusion de plus de variables explicatives dans le modèle :

$$
y_i=\beta_0+\beta_1x_{i1}+\beta_2 x_{i2}+\cdots+\beta_k x_{ik}+u_i
$$

- $y_i$ : observation individuelle de la variable à expliquer pour l’individu $i$
- $k$ : le nombre de variables explicatives du modèle
- $x_{ik}$ : les $k$ variables explicatives qui correspondent à l’individu $i$
- $N$ : nombre d’observations
- Indice $i$ : pour les individus.
Fixer un $i$ est de se fixer sur un individu (coupe transversale)
- Indice $t$ : pour les périodes temporelles.
Fixer un $t$ est de voir une photographie des individus au moment $t$.

Pour écrire l’équation qui tient en compte de tous les individus $i$, on écrit sous forme matricielle :

$$
\bold y=\bold X\beta+\bold u

\\[10pt]

\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}

=

\begin{bmatrix}
1&x_{11}&x_{12}& \cdots &x_{1k} \\
1&x_{21}&x_{22}& \cdots &x_{2k} \\
\vdots&\vdots&\vdots&\ddots&\vdots \\
1&x_{N1}&x_{N2}& \cdots &x_{Nk} \\
\end{bmatrix}
\begin{bmatrix}
\beta_0 \\
\beta _1 \\
\vdots \\
\beta_k
\end{bmatrix}
+
\begin{bmatrix}
u_1 \\
u_2 \\
\vdots \\
u_n
\end{bmatrix}
$$

> [!note]
> Le vecteur $\hat\beta$ qui contient les estimateurs des MCO de $\beta$ et qui résous ce système d’équations linéaires utilise la [pseudo-inverse](https://en.wikipedia.org/wiki/Generalized_inverse) ou l’inverse de [Moore-Penrose](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) de $\bold X$ (une généralisation de l’inverse pour les matrices pas forcément carrés. Elle est égale à l’inverse régulière si la matrice est carré).
>
> $$
> \hat\beta=(\bold X^T \bold X)^{-1}\bold X^T\bold y
> $$

Les cinq hypothèses du cas linéaire simple sont légèrement changées dans le cas général :

- $H_1$ : $\mathbb E [u_i] = 0$
- $H_2$, variance constante : $\text{Var}(\bold u)=\mathbb E[\bold u\bold u ^T]=\sigma^2_u I_n$.
- $H_3$,: la matrice $\bold X$ est non aléatoire.
- $H_4$, spécificité : le modèle est correctement spécifié.
Dans ce cas c’est linéaire, donc $\bold y = \beta \bold X + \bold u$.
- $H_5$, non colinéarité: la matrice $\bold X$ est de plein rang, càd $k+1 < n$.
Comme rappel, $\bold X$ est de dimension $(n, k+1)$.

# L’estimateur des Moindres Carrés Ordinaires (MCO)

## Préparation : dérivées pour les vecteurs et scalaires

[Par rapport aux dérivés des vecteurs et matrices](https://en.wikipedia.org/wiki/Matrix_calculus#Layout_conventions), il existe trois présentations de dérivée avec vecteurs: la dérivé vecteur-par-scalaire, la dérivé scalaire-par-vecteur et la dérivé vecteur-par-vecteur. Les dérivés avec matrice découlent facilement à partir de celles avec vecteurs.

- Dans la suite, un vecteur contient plusieurs fonctions de x (y compris $\text{Id}(x)=x$ elle-même) et un scalaire est juste une fonction de x (qui peut être aussi ).
    - (En fait, un vecteur est une matrice colonne et un scalaire est un matrice ligne, mais pour le scalaire on suppose que il n’a qu’une seule entrée, donc c’est une matrice ligne $(1\times1)$ d’une seule entrée et donc une seule valeur)
- Le premier composant est la variable dépendante et la deuxième la variable indépendante, donc si on parle de la dérivé vecteur-par-scalaire, un vecteur est une variable dépendante et le scalaire la variable dépendante.

La dérivé d’un vecteur $\bold y$ par rapport à un scalaire $x$ est utilisé dans le cas où  contient à chaque entrée des fonctions de  différentes. On prend donc la dérivé partielle de chaque fonction par rapport à . Ceci nous donne aussi le “vecteur tangent”. Si on suppose qu’n est en physique, est  sont les coordonnés de position, le vecteur tangent montre la vitesse vers chaque direction.

$$
\frac{\partial \bold y}{\partial x}=
\begin{bmatrix}
\frac{\partial y_1}{\partial x}
\\[8pt]
\frac{\partial y_2}{\partial x}
\\[8pt]
\vdots
\\[8pt]
\frac{\partial y_m}{\partial x}
\end{bmatrix}
$$

![Pour chaque point de la position en 2 dimensions, on a le vecteur tangent (qui représente la vitesse) et un vecteur normal qui n’a pas d’importance ici.](new/uga/l3/s5/eco/s5_eco_econometrie_1/s5_eco_econometrie_1/02_regression_lineaire_multiple_acbe670dd69d4e1b83e97400c1e52272/untitled.png)

Pour chaque point de la position en 2 dimensions, on a le vecteur tangent (qui représente la vitesse) et un vecteur normal qui n’a pas d’importance ici.

Après, on a la dérivé d’un scalaire par rapport à un vecteur, où les entrées du vecteur sont les arguments du scalaire $y=f(x_1,\cdots, x_n)$. Le résultat prend la dérivé partielle du scalaire par rapport à chaque variable indépendante. On note que le gradient est un cas de dérive vecteur-par-scalaire.

$$
\frac{\partial y}{\partial \bold x}=
\begin{bmatrix}
\frac{\partial y}{\partial x_1}
\\[8pt]
\frac{\partial y}{\partial x_2}
\\[8pt]
\vdots
\\[8pt]
\frac{\partial y}{\partial x_n}
\end{bmatrix}
=\nabla y
$$

Finalement, la dérivé d’un vecteur $\bold y$ par rapport à autre vecteur $\bold x$ suppose que chaque entré de  est une fonction à plusieurs variables qui se trouvent dans . Pour chaque ligne, on dérive un fonction $y_i$ par rapport à toutes ses variables indépendantes dans  (càd, ligne $1$ contient le gradient de $y_1$, ligne $2$ le gradient de $y_2$, etc). Concrètement, l’entrée $ij$ est la dérivé de la fonction $i$ par rapport à la variable indépendante $j$.

$$
\frac{\partial \bold y}{\partial \bold x} =
\begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & 
\frac{\partial y_1}{\partial x_2} &
\cdots &
\frac{\partial y_1}{\partial x_n}

\\[8pt]

\frac{\partial y_2}{\partial x_1} & 
\frac{\partial y_2}{\partial x_2} &
\cdots &
\frac{\partial y_2}{\partial x_n}

\\[8pt]

\vdots & \vdots & \ddots & \vdots

\\[8pt]

\frac{\partial y_m}{\partial x_1} & 
\frac{\partial y_m}{\partial x_2} &
\cdots &
\frac{\partial y_m}{\partial x_n}
\end{bmatrix}
$$

## Comment calculer les MCO

Les MCO sont juste les coefficients d’une régression linéaire mais appliqué sur un échantillon, dans l’espoir que ces valeur seront pas si éloignées des vraies valeurs qu’on obtiendrait si on appliquait la régression linéaire sur toute la population.

Partons du terme SCE pour trouver ce qui nous intéresse :

$$
SCE=\sum_{i=1}^n (y_i-\hat y_i)^2= \sum_{i=1}^n û^2_i
$$

Voyons que maintenant on traite avec un vecteur d’erreurs $\bold u$. Pour que chaque entrée devienne $\hat u^2_i$ on peut écrire une opération avec $\bold u$ comme suit : 

$$
\bold u^T \bold u = \begin{bmatrix}
\hat u^2_1 \\
\hat u^2_2 \\
\vdots \\
\hat u^2_n
\end{bmatrix}
$$

Et finalement, on veut minimiser tel vecteur.

$$
\min_\beta(\bold u^T \bold u) 

\iff

\beta : \frac{\partial}{\partial \beta} (\bold u^T \bold u) = 0 

\text{ et }

\frac{\partial^2}{\partial \beta^2} (\bold u^T \bold u) > 0

\\[10pt]

\begin{align*}
\min_\beta (\bold u^T \bold u)
&=
\min_\beta (\bold y - \bold X\beta)^T(\bold y - \bold X\beta) 
\\
&=
\min_\beta (\bold y ^T \bold y - 2\bold y^T\bold X \beta+\beta^T\bold X^T\bold X \beta)

\end{align*}
$$

On applique la condition de premier ordre à l’expression pour arriver au résultat. On omet la condition de deuxième ordre.

$$
\begin{align*}
&\frac{\partial}{\partial\beta} (\bold y ^T \bold y - 2\bold y^T\bold X \beta+\beta^T\bold X^T\bold X \beta) = 0
\\
\iff
&-2\bold X^T\bold y + 2 \bold X^T \bold X\hat \beta =0
\\
\iff

&\bold X^T \bold X \hat\beta = \bold X^T \bold y
\\
\iff
&\hat \beta = (\bold X^T \bold X)^{-1}\bold X^T \bold y, \text{ sous } H_5
\end{align*}
$$

---

Pour faire le passage de la première ligne à la deuxième ligne, voici quelques opérations avec dérivées, vecteur et scalaires à savoir, sorti du PDF dessous, page 12/61.

[Ch3slides-multiple-linear-regression.pdf](ressources/02_regression_lineaire_multiple_ch3slides-multiple-linear-regression.pdf)

Pour ce premier, notons on fait une combinaison linéaire de coefficients $\bold a$. Le résultat final de l’opération $\bold a^T \bold x$ est juste $[a_{j=1}x_{i=1}+a_{j=2}x_{i=2}+\cdots+a_{j=m}x_{i=n}]$. Si on dérive cette expression par $\bold x$ (scalaire-par-vecteur), on devrait avoir de retour le vecteur avec les coefficients, donc $\bold a$.  

$$
\begin{align*}
&\frac{\partial}{\partial \bold x}(\bold x^T \bold a)= \frac{\partial}{\partial \bold x} (\bold a^T\bold x)=\bold a
\end{align*}
$$

Pour ce deuxième, notons que l’expression qui résulte de $\bold x^T \bold x$ (comb. lineaire) est égale à $[x_1^2+x_2^2+\cdots+x_n^2]$. La dérivé de cette expression devrait nous retourner $2x_i$ pour l’entrée $i$, donc $2\bold x$.

$$
\begin{align*}
&\frac{\partial}{\partial \bold x}(\bold x^T \bold x) = \frac{\partial}{\partial \bold x}(||\bold x||^2)=2\bold x
\end{align*}
$$

Pour ce troisième, la forme de chaque entrée de $\bold A \bold x$ tout seul est un vecteur colonne$(\sum_{i,j=1}^{i=n, j=m} a_{ij}x_i)$. Après, la forme de chaque entrée de $\bold x^T(\bold A \bold x)$ est donc $(\sum_{i,j=1}^{i=n, j=m} a_{ij}x_i^2)$. Si on dérive chaque terme par $x_i$, on finit avec le vecteur colonne $(\sum_{i,j=1}^{i=n, j=m} 2a_{ij}x_i)$, donc $2\bold A\bold x$.

$$
\begin{align*}
&\frac{\partial}{\partial \bold x}

(\bold x^T \bold A \bold x)=2\bold A\bold x
\end{align*}
$$

Finalement, on utilise un raisonnement pareil pour ce dernier.

$$
\begin{align*}
&\frac{\partial}{\partial \bold x}(\bold x^T \bold B^T \bold B \bold x)=\frac{\partial}{\partial \bold x}(||\bold B\bold x||^2)=2 \bold B^T \bold B \bold x
\end{align*}
$$

## Variance des MCO

La variance de la matrice des estimateurs $\hat B$ est égale à la matrice de covariance entre les estimateurs $\hat\beta_i$ et $\hat\beta_j$, pour $k$ variables explicative.

$$
\text{Var}(\hat\beta)=\hat{\sigma^2_u}(\bold X^T\bold X)^{-1}=
\begin{bmatrix}

\text{Var}(\hat \beta_0) & \text{Cov}(\hat\beta_0, \hat\beta_1) & \cdots & \text{Cov}(\hat\beta_0, \hat\beta_k)

\\

\text{Cov}(\hat\beta_1, \hat\beta_0) & \text{Var}(\hat \beta_1) & \cdots & \text{Cov}(\hat\beta_1, \hat\beta_k)

\\

\vdots&\vdots&\ddots&\vdots

\\

\text{Cov}(\hat\beta_k, \hat\beta_1) &\text{Cov}(\hat\beta_k, \hat\beta_2) &\cdots &\text{Var}(\hat \beta_k)

\end{bmatrix}
$$

Comme rappel, l’estimateur des écarts-types des perturbations $u$ est :

$$
\hat{\sigma^2_u}=\frac{\hat{\bold{u}}^T\hat{\bold{u}}}{n-(k+1)}=\frac{SCR}{n-(k+1)}
$$

# Hypothèses et propriétés

## Espérance et variance de $\hat \beta$

Preuve que $\hat \beta$ est un estimateur sans biais de $\beta$ :

![untitled](new/uga/l3/s5/eco/s5_eco_econometrie_1/ressources/02_regression_lineaire_multiple_untitled_1.png)

Calcul de la variance de $\hat \beta$ :

![untitled](new/uga/l3/s5/eco/s5_eco_econometrie_1/ressources/02_regression_lineaire_multiple_untitled_2.png)

## Estimation de la variance des perturbations $\sigma^2_u$

Tout comme dans le cas de régression simple, $\bold u$ n’est pas observable. Donc, on estime avec $\hat {\bold u}$. Avant, on se prépare avec le calcul d’une certaine matrice $\bold M$ telle que :

![untitled](new/uga/l3/s5/eco/s5_eco_econometrie_1/ressources/02_regression_lineaire_multiple_untitled_3.png)

Le $T$ dans $I_T$ est le $n$ dans les dimensions $(n, k+1)$ de la matrice $\beta$. Avec cette définition de M, on peut dire que :

- M est symétrique : $\bold M=\bold M^T$
- M est idempotente : $\bold M \bold M^T=\bold M^T \bold M$
- $\text{Rg}(\bold M)=\text{tr}(\bold M)=N-k$

Finalement, on peut calculer $\hat{\bold u}$ :

![untitled](new/uga/l3/s5/eco/s5_eco_econometrie_1/ressources/02_regression_lineaire_multiple_untitled_4.png)

Et donc, finalement :

$$
\hat {\bold u}^T \hat {\bold u}=\bold u^T \bold M^T \bold M \bold u=\bold u^T \bold M \bold u 
$$

# Qualité de l’ajustement

## Rappel : analyse de la variance et $R^2$

La populaire équation de la variance, qui décompose la variance comme la somme de deux termes, est la suivante :

$$
\underbrace{\sum_{i=1}^N(y_i-\bar y)^2}_{SCT}=\underbrace{{\sum_{i=1}^N(\hat y_i-\bar y)^2}}_{SCE}+\underbrace{\sum_{i=1}^N(y_i-\hat y_i)^2}_{SCR}

\\[8pt]

\text{Remarque : } \sum_{i=1}^N(y_i-\hat y_i)^2=\sum_{i=1}^N(\hat u_i - \cancel{\bar{\hat u}}^{\space0})^2
$$

Où $SCT$ est la somme des carrés totaux, $SCE$ est la somme des carrées expliques, et $SCR$ est la somme des carrés des résidus.

Avec cette terminologie, on rappelle le coefficient de détermination :

$$
R^2=\frac{SCE}{SCT}=1-\frac{SCR}{SCT}
$$

- $R^2 = 1$ : si tous les points correspondant aux données se trouvent sur la droite d’ajustement.
- $R^2 = 0$ : les variations entre les $\bar y_i$ ne capturent quasiment rien de la variation observée entre les $y_i$.
- Remarque : un faible $R^2$ n’implique pas forcément que la régression des MCO ne sert à rien, mais que d’autres “problèmes” peuvent expliquer ce résultat.

## Ajustement de $R^2$

Un fait important par rapport à $R^2$ est que sa valeur augmente si le nombre de variables explicatives augmente. Ceci ne nous est pas pratique, car on ne pourra pas savoir si l’une des variables explicatives a un impacte presque nul sur la variable à prédire.

Pour $R^2$, toute variable explicative nous rapproche de la meilleure prédiction, ce qui n’est pas désirable, car on veut distinguer entre les variables explicatives qui sont des bons prédicteurs et celles qui ne sont pas.

La manière populaire d’ajuster $R^2$ est comme $\bar{R^2}$, un $R^2$ ajusté aux degrés de liberté :

$$
\bar{R^2}=R^2-\frac{k-1}{n-k}(1-R^2)=1-\frac{SCR/(n-k)}{SCT/(k-1)}
$$

# Inférence statistique

## Test statistiques

La grande différence de ce cas avec le cas de regression simple c’est que un estimateur $\beta_i$ pourrait ne pas être significatif individuellement (sous un test de Student) mais le modèle en tout pourrait être significatif globalement (sous un test de Fisher).