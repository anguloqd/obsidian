# 03 // suites réelles

Date de création: November 22, 2021 10:59 AM
Modifié: June 10, 2023 9:57 PM

[Slides des suites réelles](chap3.pdf)

# Généralités sur les suites réelles

1. Une suite réelle est une application de $\N$, ou d'une partie de $\N$, dans $\R$.
2. L'image d'un $n ∈ \N$ se note $u_n$ et s'appelle le terme de rang $n$ de la suite.
3. La suite est désignée par l'ensemble de ses termes via la notation $(u_n)$ ou $(u_n)_{n∈\N}$.

## Distinction entre ensemble et suite

Donnons un exemple :

- l'ensemble des entiers pairs, désigné par $\{2n : n ∈ \N\}$, et
- la suite des entiers pairs, désigné par $(u_n)_{n∈\N}$, avec, pour tout $n ∈ \N, u_n = 2n$.

La suite attribue un indice (et donc un certain ordre) à chaque entier pair : $u_0 = 0, u_1 = 2, u_2 = 4$, $...$ ce que ne fait pas l'ensemble.

## Définition par terme général ou par récurrence

- **Définition par terme général** : une expression de $u_n$ en fonction de $n$.
- **Définition par récurrence** : on définit le premier terme ou les premiers termes et on explicite une dépendance du terme de rang $n$ aux termes de rang inférieurs à $n$.
    
    ![image (41).png](image_(41).png)
    

# **Propriétés des suites**

## **Axiome de récurrence**

Soit $P_n$ une propriété indexée par $n ∈ \N$. Si les propriétés suivantes sont vraies : 

1. **Initialisation** : $P_0$ vraie.
2. **Hérédité** : $∀n ∈ \N, P_n ⇒ P_{n+1}$

… alors $∀n ∈ \N, P_n$ est vraie.

## A**utres propriétés**

- Une suite est majorée (resp. minorée, bornée) si et seulement si elle l'est à partir d'un certain rang.
- Une suite $(u_n)_{n∈N}$ est bornée si, et seulement si, la suite $(|u_n|)_{n∈\N}$ est majorée.

# **Suites classiques**

## **Suite arithmétique : $u_{n+1}=u_n+r$**

Soit $r ∈ \R$. Toute suite vérifiant la relation de récurrence $u_{n+1} = u_n + r$ est appelée suite arithmétique de raison $r$. Si $(u_n)_{n∈N}$ est arithmétique de premier terme $u_0 = a$ et de raison $r$, alors son terme général est $u_n = a + nr$.

Une suite arithmétique est entièrement déterminée (et caractérisée) par ses deux premiers termes (car $r = u_1 − u_0$).

On peut calculer la somme des éléments d’une suite arithmétique $S_n$ comme suit :

$$
S_n=\sum_{i=0}^nu_i=u_0+u_1+\dots+u_n=(n+1)\times\frac{u_0+u_n}{2}

\\[8pt]

S_n=\text{ nb de termes } \times \frac{\text{premier terme}+ n\text{-ième terme}}{2}
$$

## **Suite géométrique : $u_{n+1}=q\times u_n$**

Soit $q ∈ \R$. Toute suite vérifiant la relation de récurrence $u_{n+1} = q × u_n$ est appelée suite géométrique de raison $q$. Si $(u_n)_{n∈N}$ est géométrique de premier terme $u_0 = a$ et de raison $q$, alors son terme général est $u_n = a × q_n$.

Une suite géométrique est entièrement déterminée par ses deux premiers termes (car $q = \frac{u_1}{u_0}$ si $u_0 \ne 0$, et sinon $(u_n)$ est entièrement nulle).

On peut calculer la somme des éléments d’une suite arithmétique $S_n$ comme suit :

$$
S_n=\sum_{i=0}^nu_i=u_0+u_1+\dots+u_n=u_0\times\frac{q^{n+1}-1}{q-1}

\\[8pt]

S_n=\text{ premier terme } \times \frac{\text{raison}^\text{nb de termes}-1}{\text{raison}-1}
$$

## **Suite arithmético-géométrique : $u_{n+1} = au_n + b$**

Soit $a, b ∈ \R$. Toute suite vérifiant la relation de récurrence $u_{n+1} = au_n + b$ est appelée suite arithmético-géométrique.

- Une suite arithmético-géométrique vérifiant $u_{n+1} = au_n + b$ est arithmétique si $a = 1$, et géométrique si $b = 0$.
- Une suite arithmético-géométrique non stationnaire est entièrement déterminée par ses trois premiers termes.
- De $u_n \ne u_0$, en retranchant $u_2 = au_1 + b$ à $u_1 = au_0 + b$, on obtient $a = \frac{(u_2−u_1)}{(u_1−u_0)}$, et alors $b = u_1 − au_0$.

Si $a \ne 1$, le calcul du terme général d'une suite arithmético-géométrique vérifiant $u_{n+1} = au_n + b$ se ramène à celui d'une suite géométrique.

- On cherche un $x$ tel que $ax + b = x$. C'est à dire, $x = \frac{b}{(1-a)}$.
- On pose une nouvelle suite, $(v_n)$, comme $v_n = u_n - a$.
- Ceci vérifie que :
    
    $$
    \begin{align*}
    v_{n+1} &= u_{n+1} − x 
    \newline &= au_n + b − x
    \newline &= au_n + b − (ax + b)
    \newline &= a(u_n − x)
    \newline &= av_n
    \end{align*}
    $$
    
- Donc, $(v_n)$ est géométrique de raison $a$.
- Par conséquent $∀n ∈ \N, v_n = v_0 \cdot a_n$ , avec $v_0 = u_0 - x = u_0 - \frac{b}{(1−a)}$
Finalement, $u_n = v_n + x$.