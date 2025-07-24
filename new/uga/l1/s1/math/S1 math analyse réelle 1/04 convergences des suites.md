# 04 // convergences des suites

Date de création: November 22, 2021 10:59 AM
Modifié: June 10, 2023 9:57 PM

[Slides de convergences](Chap4_(4).pdf)

# Limite d'une suite

## Définition et convergence

La définition formelle de la limite $\ell$ d’une suite $\{u_i\}$ est comme suit :

$$
∀ε > 0, ∃N ∈ \N, ∀n ≥ N, |u_n − \ell| ≤ ε
$$

En français, cette définition peut se lire comme…

- pour $n$ suffisamment grand (si $n ≥ N$, pour un certain $N$)…
- la distance entre $u_n$ et $\ell$ (mesurée par $|u_n − \ell|$)…
- est arbitrairement petite ($≤ ε$, quel que soit $ε > 0$).

On dit qu'une suite $(u_n)$ est ***convergente*** si elle admet une limite $\ell ∈ \R$. Dans le cas contraire, on dit que $(u_n)$ est ***divergente***. Quand la limite est "l'infini", on utilise la définition de inexistence d'une borne (supérieur ou inférieur).

- Pour $\infin$ : $∀M ∈ \R, ∃N ∈ \N, ∀n ≥ N,  u_n ≥ M$
- Pour $-\infin$ : $∀M ∈ \R, ∃N ∈ \N, ∀n ≥ N, u_n ≤ M$

## Propriétés

- Si $(u_n)$ admet une limite $\ell ∈ \R$, alors cette limite est unique.
- Soit $(u_n)$ une suite. Alors $(u_n)$ converge vers $\ell ∈ \R$ si et seulement si la suite $(u_n − \ell)$ converge vers $0$.
- Soit $(u_n)$ une suite et soit $\ell ∈ \R$...
    - S'il existe une suite $(v_n)$ convergeant vers $0$ et si $∀n ∈ \R, |u_n − \ell| ≤ v_n$, alors $(u_n)$ converge vers $\ell$.
- Toute suite convergente est bornée.
    - Attention : bornée n'implique pas convergente
- Soit $(u_n)$ une suite bornée (non nécessairement convergente), et soit $(v_n)$ une suite convergeant vers $0$...
    - Alors $(u_n \cdot v_n)$ converge vers $0$.

## **Passage à la limite d'une inégalité**

Soient $(u_n)$ et $(v_n)$ des suites convergentes vérifiant $u_n ≥ v_n$ à partir d'un certain rang. Alors $\lim u_n ≥ \lim v_n$.

Attention : la propriété précédente n'est pas vraie si on considère des inégalités strictes. $u_n > v_n \implies \lim u_n > \lim v_n$ est faux !

## Théorèmes notables

### Théorème de convergence monotone

C’est un théorème très utile et on le voit de deux manières :

- Si $(u_n)$ est croissante et majorée (pas forcément bornée inf.), alors elle converge.
- Si $(u_n)$ est décroissante et minorée (pas forcément bornée sup.), alors elle converge.

### **Théorème des "gendarmes"**

Soient $(u_n)$ et $(w_n)$ des suites convergeant vers la même limite $\ell ∈ \R$, Si $(v_n)$ est une suite vérifiant $u_n ≤ v_n ≤ w_n$ à partir d'un certain rang, alors $(v_n)$ est convergente et $\lim v_n = \ell$.

### Théorème de Bolzano-Weierstrass

Toute suite bornée possède au moins une suite extraite convergente.

## Suites dérivées d’une suite de base

### Suites adjacentes

Soit $∀n ∈ N, u_n ≤ v_n$, $(u_n)$ est une suite croissante et $(v_n)$ est décroissante. En plus, $\lim(u_n − v_n) = 0$.

Sous toutes ces conditions, elles convergent vers la même limite $\ell ∈ \R$, qui, de plus, vérifie ce qui suit : $∀n ∈ \N, u_n ≤ \ell ≤ v_n$.

### Suite extraite

Prenons comme base une suite de termes de la suite $(u_n)$. Formellement, c'est la donnée d'une suite $(u_{k_n}), n∈\N$ pour des indices ${k_n} ∈ \N$ vérifiant $k_0 < k_1 < . . .$

# Suites satisfaisant $u_{n+1} = f(u_n)$

![Représentation graphique. (Comportements de suites définies par $u_0$ et $u_{n+1} = f(u_n)$)](image_(39).png)

Représentation graphique. (Comportements de suites définies par $u_0$ et $u_{n+1} = f(u_n)$)

## Application contractante

Soit $I$ un intervalle fermé et borné de $\R$ et soit $f : I → I$. On dit que $f$ est *contractante* sur $I$ si :

$$
∃k ∈ [0, 1[, ∀x, y ∈ I, |f(x) − f(y)| < k|x − y|
$$

En plus, si $f$ est contractante, alors $f$ est continue (admis) et possède un unique point fixe $\ell ∈ \R$ (ceci découle du théorème du point fixe de Banach). De plus, pour tout $u_0 ∈ I$, la suite définie par $u_0$ et $u_{n+1} = f(u_n)$ converge vers $\ell$.

## Point fixe d’une fonction contractante

Soit $f$ une fonction réelle définie sur un intervalle $I$. On peut dire que $x ∈ I$ est un point fixe de $f$ si $f(x) = x$.

La preuve est comme suit : si $(u_n)_{n≥0}$ est une suite définie par une relation de récurrence de la forme $u_{n+1} = f(u_n)$ alors la suite des images de $f$ est $(f(u_n))_{n≥0}$.

Si de plus $(u_n)_{n≥0}$ converge vers $\ell$, et $f$ est continue, alors par composition $(f(u_n))_{n≥0})$ converge vers $f(\ell)$.

Or $(f(u_n))_{n≥0}$ peut aussi s'écrire $(u_{n+1})_{n≥0}$. C'est donc la suite $(u_n)_{n≥0}$ tronquée de son premier terme. Si $(u_n)_{n≥0}$ converge vers $\ell$, alors $(u_n)_{n≥1}$ aussi. Ainsi $f(\ell) = \ell$.