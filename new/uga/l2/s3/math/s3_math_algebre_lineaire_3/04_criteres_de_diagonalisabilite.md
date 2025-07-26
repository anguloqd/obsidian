# 04 // critères de diagonalisabilité

# Vocabulaire

## Multiplicité algébrique $\alpha_\lambda$ et géométrique

La **multiplicité algébrique** d’un valeur propre $\lambda$ est la quantité de polynômes dont le valeur propre est racine des facteurs polynomiaux du polynôme caractéristique, **comptant les facteurs répétés**. Par exemple, dans $(\lambda-1)(\lambda-3)^2$, $\lambda=3$ a une multiplicité algébrique de $2$.

**Théorème**. Soit $\alpha_\lambda$ la multiplicité de $\lambda$, donc $1 \le \dim E_\lambda \le \alpha_\lambda$. ($E_\lambda=\text{Ker}(A-\lambda I)$)

- Si $\alpha_\lambda = 1$ pour tout $\lambda$, tous les $\lambda$ ont un seul $v_\lambda$ associé.
- Si $\alpha_\lambda > 1$, il y a ***au moins*** un $v_\lambda$ associé par $\lambda$. Normalement c’est plus d’un $v_\lambda$ associé.

La **multiplicité géométrique** d’un valeur propre $\lambda$ est la dimension son sous-espace propre $E_\lambda$.
Un règle plus facile aussi c’est qui mult. alg. $\alpha_\lambda$ $≠$ mult. géo. $\dim E_\lambda$, donc $M$ pas diagonalisable.

**Théorème**. Soit $f$ endomorphe sur $\R^n$. Les quatre propositions suivantes sont équivalentes :

- On peut trouver une base de vecteurs propres $\{e_i\}$.
- Dans la base de vecteurs propres $\{e_i\}$, la matrice $M$ de $f$ est diagonale.
- $\R^n=\oplus_i E_{\lambda_i}$
- $\alpha_\lambda=\dim E_\lambda$, pour tout valeur propre $\lambda$.

## Polynôme scindé

Un polynôme *scindé* est un polynôme factorisable en facteurs polynomiaux de degré $1$ sur $\R$. En plus, si chaque facteur polynomiaux de degré $1$ est unique, il est *simplement scindé*. 

$$
(x^2+x+1) : \text{racines non-réelles, non-scindé.}
\\
(x-1)(x-2)^2 : \text{scindé, pas simplement scindé.}
\\
(x-1)(x-2)(x-3) : \text{simplement scindé.}
$$

**Théorème**. Si le polynôme caractéristique est scindé, la matrice est trigonalisable (possiblement diagonalisable). En plus, s’il est simplement scindé, il est forcément diagonalisable. Par conséquence, **s’il n’est pas scindé, il n’est pas ni trigonalisable ni diagonalisable**.

# Polynôme minimal : $P_{M,M}(X)$

## Déduire diagonalisabilité sans la lancer

Le polynôme minimal $P_{M,M}(X)$ d’une matrice $M$ est le polynôme annulateur de $M$ de plus petit degré ayant les mêmes racines du polynôme caractéristique $P_{M,C}(X)$. Par exemple :

$$
M =
\begin{pmatrix}
5 &-7 & 6 \\
0 & 1 & 0 \\
-3 & 5 & -1
\end{pmatrix}
\implies P_{M,C}(X)=(X-1)(X-2)^2

\\
\text{}
\\

\text{Donc, } P_{M,M}(X) = (X-1)(X-2)  \text{ ou } P_{M,M}(X)=P_{M,C}(X)=(X-1)(X-2)^2

\\
\text{}
\\

P_{M,C}(M)=(M-I)(M-2I)^2 =
\begin{pmatrix}
4&-7&3\\
0&0&0\\
-3&5&-2
\end{pmatrix}
\begin{pmatrix}
3&-7&3\\
0&-1&0\\
-3&5&-3
\end{pmatrix}^2=0
$$

Dans le cas précédent, $P_{M,M}(X) = P_{M,C}(X)$, car l’autre polynôme n’est pas annulateur. 

Note : la matrice identité $I$ est l’unité dans le monde des matrices.

**Théorème**. $M$ diagonalisable $\iff$ Polynôme minimal $P_{M,M}(M)$ simplement scindé.
Dans l’exemple précédent donc, il ne faut aller plus loin, car $P_M(M)$ non simpl. scindé.