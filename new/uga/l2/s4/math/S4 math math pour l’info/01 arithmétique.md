# 01 // arithmétique

Date de création: January 15, 2023 11:26 PM
Modifié: June 9, 2023 5:40 PM

# Division euclidienne

## Définition

Diviser un nombre naturel $A$ (strictement naturel !) par un autre naturel $B$ est de trouver $Q,R\in\N$ qui vérifient l’équation suivante :

$$
A=BQ+R
$$

Dessus, le nombre $Q$ est le quotient et $R$ est le reste, où $0 \le R < B$. Notons qu’ici on parle de la division entière et pas de la division rationnelle.

<aside>
✏️ À partir d’ici, on note la division euclidienne de $a$ et $b$ comme $a/b$, on ne parle jamais ici de la division rationnelle ou réelle.

</aside>

# Numération en base $b$

[Slides de numération annotés.pdf](slides_bases_annote.pdf)

## Définition et notation

Il existent trois bases de numération relevantes dans la pratique : base $2$, base $10$ et base $16$.

- La base $2$ est utilisée comme la base principale dans l’informatique.
- La base $10$ est la manière naturelle de compter pour les humains.
- La base $16$ est une base très utile dans l’informatique pour compter de manière compacte.

Quand on parle des différents bases dans un même contexte, on adopte la notation $(n)_p$. Ici, $n$ est une quantité exprimée en chiffres dans une base et $p$ est la base concernée. Par exemple, toutes ces expressions qui suivent veulent exprimer le nombre $23$ :

$$
(23)_{10}=(10111)_2=(17)_{16}
$$

Notons que si on écrit un nombre sans spécifier la base, on parle implicitement de la base $10$.

**Proposition.** L’écriture d’un nombre entier en base $2$, $10$ ou $16$ est unique.

## Conversion

Il est plus facile de parle d’une conversion quand on applique l’expansion en base $p$ d’un nombre $(a_n\dots a_2 a_1 a_0)_p$, càd. un nombre dont la première chiffre est $a_0$, la deuxième est $a_1$, etc. :

$$
(a_n\dots a_2 a_1 a_0)_p = a_n \times p^n + \dots + a_2 \times p^2 + a_1 \times p + a_0
$$

### Base $p$ $\rightarrow$ Base 
$10$

C’est la plus faciles des conversions. Il faut juste utiliser l’expansion de base $p$.

$$
\text{Ex. }1 : (11011)_2=1\times 2^4+1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 = (27)_{10}

\newline

\text{Ex. }2 : (5C8)_{16}=5\times 16^2 + \underbrace{C}_{12} \times 16^1 + 8 = (1480)_{10}
$$

### Base $10$ $\rightarrow$ Base $p$

On effectue une division euclidienne récursivement de chaque quotient et **on inverse l’ordre des restes obtenus, càd. du bas en haut !!!**

$$
\left.
\begin{align*}
75 = 2 \times 37 + 1 \\
37 = 2 \times 18 + 1 \\
18 = 2 \times 9 + 0 \\
9 = 2 \times 4 + 1 \\
4 = 2 \times 2 + 0 \\
2 = 2 \times 1 + 0 \\
1 = 2 \times 0 + 1
\end{align*}
\right\}

\\
\text{}
\\

\implies (75)_{10}=(1001011)_2

$$

$$
\left.
\begin{align*}
2014 = 16 \times 125 + \underbrace{14}_E\\
125 = 16 \times 7 + \underbrace{13}_D \\
7 = 16 \times 0 + 7 \\

\end{align*}
\right\}

\\
\text{}
\\

\implies (2014)_{10}=(7DE)_{16}

$$

### Base $2$ $\rightarrow$ Base $16$ (ou viceversa)

On va utiliser ce tableau utile pour chaque chiffre “base” d’une base vers l’autre.

![Untitled](new/uga/l2/s4/math/S4%20math%20math%20pour%20l’info/01%20arithmétique/Untitled.png)

Après, la chose à garder en tête c’est que chaque chiffre en base $16$ correspond à quatre chiffres en base $2$. Ceci rend la conversion beaucoup plus facile pour la relation spéciale entre $2$ et $16$ ($16$ est une puissance de $2$, finalement). Voyons deux exemples :

$$
(\underbrace{0100}_4 \space \underbrace{1011}_B)_2=(4B)_{16}

\\
\text{}
\\

(F9)_{16}=(\underbrace{1111}_F \space \underbrace{1001}_9)_2
$$

### Numération des réels

La définition qu’on avait présentée pour l’expansion en base $p$ d’un nombre naturel peut être étendue pour inclure les nombres réels. Pour un nombre réel qui a pour chiffres $(a_n \dots a_1 a_0 , b_1 \dots b_m)_p$, son expansion est :

$$
(a_n \dots a_1 a_0 , b_1 \dots b_m)_p = a_np^n + \dots +a_1p + a_0 + b_1p^{-1}\dots+b_mp^{-m}

\\
\text{}
\\

(7.25)_{10}=7 + 2 \times10^{-1}+5 \times10^{-2}
$$

Pour convertir $7.25$ en base $2$, on découpe le nombre en partie entière et partie rationnelle. On sait bien convertir $7$ en base $2$, c’est $(111)_2$, et donc on s’occupe de la partie rationnelle. On utilise le même raisonnement : si une puissance négative de p dépasse le nombre $n$, on laisse $0$ et on passe à la puissance suivante. **On tente place rationnelle par place rationnelle, toujours mettant la plus grande chiffre possible dans chaque place sans dépasser le nombre objectif**.

$$
(111.1)_2 = 7.5 > 7.25 \longrightarrow (111.01)_2=7.25
$$

Une application particulière est que $(0.\bar{1})_2=(0.111\dots)_2=(1)_{10}$. C’est une analogie des “les nombres avec période $9$ n’existent pas” et “$0.\bar{9} = 1$”.

## Opérations

Les opérations élémentaires sont analogues à celles qu’on sait faire en base $10$.

### L’addition

“On pose une retenue quand on arrive à $p$”.

![Untitled](new/uga/l2/s4/math/S4%20math%20math%20pour%20l’info/01%20arithmétique/Untitled%201.png)

### La soustraction

![Untitled](new/uga/l2/s4/math/S4%20math%20math%20pour%20l’info/01%20arithmétique/Untitled%202.png)

### Le produit

![Untitled](new/uga/l2/s4/math/S4%20math%20math%20pour%20l’info/01%20arithmétique/Untitled%203.png)

### La division euclidienne

Le prof. n’as pas donné un exemple de comment faire. Il faut juste reprende ce qu’on fait en base $10$ et pense en termes généraux de base $p$ pour toute autre base.

# Arithmétique élémentaire

[Slides d’arithmétique élémentaire](slides_arithmetique_minfo_annote.pdf)

## Multiples et diviseur

Si $a$ est un nombre entier, $c$ est un multiple de $a$ s’il existe $b$ tel que $a \cdot b = c$. Notons que $c$ est aussi multiple de $b$.

Pour les diviseurs, $b$ est un diviseur (ou facteur) de $a$ s’il existe $c$ tel que $a = b \cdot c$, c’est-à-dire, si a est multiple de $b$. Notons que $c$ est aussi diviseur ou facteur de $a$.

**Proposition**. Les assertions suivantes sont vraies :

- Si $a$ divise $b$, alors $a$ divise tout multiple de $b$.
- Si $a$ divise $b$ et $b$ divise $c$, alors $a$ divise $c$.
- Si $a$ et $b$ sont divisibles par $c$, alors $c$ divise $ax+by, \forall x,y \in \mathbb{Z}$.
    - En particulier, $c$ divise $a+b$ et $a-b$.

## Nombres premiers

Un nombre premier est un nombre naturel qui a seulement deux diviseurs distinctes : $1$ et lui-même.

**Théorème de caractérisation**. Soit $n$ un nombre naturel. Si $n$ n’est pas premier, il admet au moins un diviseur égal ou inférieur à $\sqrt{n}$.

**Propriété #1**. Tout nombre entier peut se d´ecomposer en produit de facteurs premiers. Cette
décomposition est unique.

**Propriété #2**. Si $p$ est un nombre premier et divise un produit $ab$, alors il divise au moins un
des termes.

## PGCD et PPCM

Le plus grand commun diviseur $PGCD(a,b)$ est une fonction qui prend deux nombres naturels et retourne un nombre $d$ tel qu’il est plus grand que tous les diviseurs communs de $a$ et $b$.

Similairement, le plus petit commun multiple $PPCM(a,b)$ est une fonction qui retourne le naturel $d$ tel qu’il est plus petit que tous les multiples communs de $a$ et $b$. Une propriété est que $PPCM(a,b) \le ab$.

Pour calculer le PGCD, on utilise l’algorithme d’Euclide, lequel est basée sur la propriété $PGCD(a,b) = PGCD(b, r_{a/b})$, où $r$ est le reste de la division euclidienne de $a/b$.

### Algorithme d’Euclide

1. Pour trouver $PGCD(a,b)$, $a > b$, on pose la division euclidienne tel que $a = bq_1+r_1$.
2. On divise récursivement le quotient et reste, $q_i/r_i$ obtenus jusqu’à que $r_n = 0$.
3. On déduit que $q_n=r_{n-1}=PGCD(a,b)$.

$$
\begin{array}{c}
495 = 210 \times 2 + 75 \\
210 = 75 \times 2 + 60 \\
75 = 60 \times 1 + 15 \\
60 = 15 \times 4 + 0
\end{array} \longrightarrow 
\begin{array}{c}
\text{Le PGCD est le dernier reste non nul :}\\
PGCD(495,210)=15
\end{array}
$$

### Propriétés de PGCD et PPCM

<aside>
✏️ Notation. $a \mid b$ signifie $a$ divise $b$. C’est-à-dire, $\exists a\in \N : \exists k \in \N, a = kb$.

</aside>

- $PGCD(a,b) \times PPCM(a,b)=ab$
- Les diviseurs communs à deux nombres sont les diviseurs de leur PGCD.
- $PGCD(ca, cb) = c\cdot PGCD(a, b)$
- Si $c$ est un diviseur commun de $a$ et $b \implies PGCD(a/c, b/c) = PGCD(a, b)/c$.
- $PGCD(a, b)\mid PGCD(ac, bd)$.
- Si $c$ est un diviseur commun de $a$ et $b \implies c = PGCD(a, b)$ si et seulement si $a/c$ et $b/c$ sont premiers entre eux.

## Nombre copremiers : premiers entre eux

Deux nombres a et b sont premiers entre eux ou *copremiers* si leur seul diviseur commun est $1$. Une implication naturelle est que $PGCD(a,b) = 1$.

Notons que $a$ et $b$ ne sont forcément pas premiers. Cela dit, un nombre premier $p$ est un nombre copremier à tous les nombres strictement inférieurs à $p$.

### PGCD et décomposition en nombres premiers

On peut déduire si $a$ et $b$ sont copremiers en regardant leur décomposition en nombre premiers : leur PPCM est le produit de tous les nombres premiers qui apparaissent dans les deux décompositions en facteurs premiers de ces deux entiers, chacun affecté du plus petit exposant qui apparait dans celles-ci.

$$
\begin{array}{c}
4950= 2 \times3^2 \times5^2 \times 11 \\
4875=3 \times 5^3 \times 13
\end{array} \longrightarrow 
PGCD(4950, 4875) = 3 \times 5^2 = 75
$$

### PPCM et décomposition en nombres premiers

Dans le cas du PPCM, leur PPCM est le produit de tous les nombres premiers qui apparaissent dans au moins une des décompositions en facteurs premiers de ces deux entiers, chacun affecté du plus grand exposant qui apparait dans celles-ci.

$$
\begin{array}{c}
4950= 2 \times3^2 \times5^2 \times 11 \\
4875=3 \times 5^3 \times 13
\end{array} \longrightarrow
\begin{array}{c} 
PPCM(4950, 4875) = \\
2 \times 3^2 \times 5^3 \times 11 \times 13  = 312750
\end{array}
$$

### Propriétés entre copremiers, PGCD et PPCM ($a$ et $b$ copremiers)

- Si $a$ divise $bc$ $\implies$ $a$ divise $c$.
- On a $PGCD(a, bc) = PGCD(a, c)$.
    - De plus, si $a$ et $c$ sont premiers entre eux, alors $PGCD(a, bc) = 1$.
- Soient $a,b \in \Z$, et $PGCD(a,b)=d$…
    - $\exists x,y \in \Z : ax+by=d$.
    - **Théorème de Bachet-Bezout**.
    $a$ et $b$ sont copremiers $\iff \exists x,y \in \Z : ax+by=1$.

### Algorithme d’Euclide généralisé

Pour trouver une solution à $ax+by=PGCD(a,b)$, on remonte dès la fin de l’algorithme d’Euclide.

$$
\begin{array}{c}
l_1 : 495 = 210 \times 2 + 75 \\
l_2 : 210 = 75 \times 2 + 60 \\
l_3 : 75 = 60 \times 1 + 15 \\
l_4 : 60 = 15 \times 4 + 0 \\ \\
PGCD(495,210)=15
\end{array} \\ 

$$

$$
\begin{array}{cl}
\text{On cherche }x,y
: & 495x+210y=15
\end{array}

\\
\text{}
\\

\begin{array}{cl}
\text{D'après } l_3:
& 75 - 60 = 15\end{array} \\

\\
\text{}
\\

\begin{array}{cl}
\text{Injectant } l_2 \rightarrow l_3: &
75-(210-2\times 75)=15 \\
& 3 \times 75 - 210 = 15
\end{array} \\

\\
\text{}
\\

\begin{array}{cl}
\text{Injectant }:
&3\times(495-2\times210)-210=15 \\l_1 \rightarrow (l_2\rightarrow l_3)
&3 \times 495 - 7 \times 210 = 15
\end{array}

\\
\text{}
\\

\text{D'après la dernière ligne : } x=3,y=-7
$$

Quand on injecte, on voit que c’est pour pouvoir exprimer les choses en termes de $210$ et $495$. En $l_2 \rightarrow l_3$, on exprime $60$ en termes de $210$ et $75$ (on garde l’expression en $210$ et on remplace celle en $75$), puis en $l_1 \rightarrow (l_2 \rightarrow l_3)$, on exprime $75$ en termes de $495$ et $210$ (on garde les deux car ils sont les deux nombres qui nous intéressent).

# Congruences

[Slides de congruence](slides_congr_minfo_annote.pdf)

## Définition

Soit $n$ un entier naturel. On dit que les entiers $a$ et $b$ sont congrus modulo $n$ si et seulement si ils ont le même reste dans la division euclidienne par $n$. On note alors $a \equiv b[n]$.

Il est immédiat de voir que si $a=nq+r$, alors $a \equiv r[n]$  ou aussi $a \equiv r \text{ mod } n$. C’est ce reste $r$ qui représentera l’entier $a$ modulo $n$.

[Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence)

## Propriétés

Soient $a,b,c,d \in \N$ et $n \in \N^*$. Si $a \equiv c[n]$ et $b \equiv d[n]$ (càd. ils sont des restes de $n$), les propriétés suivantes sont vraies, pour tout $p \in \N$ :

$$
a+b \equiv (c+d)[n] \\
a-b \equiv (c-d)[n] \\
a\times b \equiv (c \times d)[n] \\
a^p \equiv c^p[n]
$$

On notera aussi que si $a \equiv b[n]$, alors $a-b \equiv 0[n]$ et $n$ divise $a - b$. Par exemple : $75 \equiv 5[7] \iff (75-5) \equiv 0[n]$ et donc $(75-5)$ est divisible par $7$.

Ces propriétés permet de creer une algèbre de groupe cyclique de $n$, ce qu’on explique dans la section “petit théorème de Fermat”.

**Théorème de l’inverse multiplicatif**. Soit $a \in \Z, n\in \N$. $x$ est l’inverse multiplicatif modulaire en $n$ de $a$ si et seulement si $ax \equiv 1[n]$. **$x$ existe si et seulement si $a$ est copremier avec $n$**.

[Modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

## Petit théorème de Fermat

Si $p$ est un nombre premier et $a$ est un entier non divisible par $p$ (non-multiple de $p$), alors :

$$
a^{p-1} \equiv 1[p] \text{ ou, de manière equivalente, } a^p \equiv a[p].
$$

Ce théorème est fondamental dans la cryptologie moderne industrielle qui a besoin d’entiers
naturels premiers à grands nombres de chiffres (codage RSA). Notons que si $p > a$ et $a\ne0$, la condition de $a$ non-divisible par $p$ est déjà vérifiée.

**Corollaire**. Soit $p$ et $q$ des nombres premiers distincts. On pose $n=pq$ et, pour tout $a$ copremier avec $n$, il est vrai que $a^{(p-1)(q-1)} \equiv 1[n]$. 

### Preuve du corollaire

**Preuve**. Montrons que pour $p$ et $q$ premiers, si $a \equiv b[p]$ et $a \equiv b[q]$, alors $a \equiv b[pq] \iff a \equiv b[n]$.

On a que $a-b=kp$ et $a-b = mq \implies kp = mq$, où $k,m \in \Z$, donc $p$ divise $mq$. Or, puisque $p$ et $q$ sont premiers ils sont copremiers, donc $p \nmid q$ et $p \mid m$.

Puisque $p \mid m$, on peut écrire $m = lp$ pour un certain $l \in \Z$ et $a-b=lpq \implies a \equiv b[pq]$.

Finalement, on applique le petit théorème de Fermat et on arrive à la conclusion :

$$
\begin{cases}
a^{p-1} \equiv 1[p] \implies {a^{p-1}}^{q-1}=a^{(p-1)(q-1)} \equiv 1^{q-1}[p]=1[p]
\\
a^{q-1} \equiv 1[q] \implies {a^{q-1}}^{p-1}=a^{(p-1)(q-1)} \equiv 1^{p-1}[q]=1[q]
\end{cases}
\\
\implies
a^{(p-1)(q-1)} \equiv1[n]
$$

## Groupe cyclique

Si on fixe un nombre naturel $n$, on peut classifier tous les nombres naturels selon leurs congruence modulo $n$. Par exemple, si on fixe $n=3$, on peut classifier les nombres $\bar1 \in \{1, 4, 7, \dots\}$ comme ceux qui sont congruents à $1[3]$. De même pour $\bar2 \in \{2,5,8,\dots\}$, et $\bar0 \in \{0,3,6, \dots\}$, ces derniers étant les multiples de $3$.

Ces agroupassions de naturels sont appelées “classes de congruences”. En plus, on peut regrouper les classes d’équivalences dans un ensemble partant d’un $n$ fixe pour créer l’ensemble $\Z/n\Z$, appelé “**l’anneau d’entiers modulo $n$**”.

$$
\Z/n\Z = \bigcup_{k=0}^{n-1}\overline{k}_n =\left\{\overline0_n,\overline1_n,\dots,\overline{n-2}_n,\overline{n-1}_n\right\},

\text{ où } \overline{k}_n=\left\{p\in\N:p \equiv k[n] \right\}

\\

\text{Par exemple : }\Z/3\Z = \{\bar0_3, \bar1_3, \bar2_3\} = \{\{0,3,6,\dots\}, \{1,4,7,\dots\}, \{2,5,8,\dots\}\}
$$

### $\Z/n\Z$ comme algèbre : opérations entre classes de congruences/résidus

On peut doter à $\Z/n\Z$ d’opérations analogues à celles vus pour les entiers modulés par $n$ :

- Addition : $\overline{a}_n + \overline{b}_n = \overline{(a+b)}_n$
- Soustraction : $\overline{a}_n - \overline{b}_n = \overline{(a-b)}_n$
- Multiplication : $\overline{a}_n \overline{b}_n = \overline{(ab)}_n$

Sous ces opérations, l’anneau $\Z/n\Z$ est fermé/stable et donc un **groupe algébrique**. En plus, le groupe est dit “cyclique” car si on additionne $1$ à chaque élément de $\overline{k}$ itérativement, on reviendra éventuellement à $\overline{k}$. Par exemple :

$$
\begin{align*}
\Z/3\Z = \{\overline0_3,\overline1_3,\overline2_3\}

\longrightarrow

\space &3 \equiv 0[3] \implies \overline3_3=\overline0_3 \\ &\overline{2}_3 + \overline{1}_3=\overline{3}_3=\overline0_3
\end{align*}
$$

### Classes d’équivalences spéciales

Soient $\overline{a}, \overline{b} \in \Z /n \Z$ alors on définit si pour $\overline{a}$, il existe $\overline{b}$ telle que :

- Inverse de $\overline{a}$ : $\overline{a}_n \overline{b}_n = \overline{1}_n$, alors $\overline{b}$ est l’inverse de $\overline{a}$ et viceversa.
**C’est une analogie de l’inverse multiplicatif modulaire d’entiers**.
- Diviseur de zéro : $\overline{a}_n \overline{b}_n = \overline0_n$, on dit que $\overline{a}_n$ et $\overline{b}_n$ sont des diviseurs de zéro.

Pour un certain $\overline{a}$ fixé, on utilise l’algorithme d’Euclide pour trouver son inverse multiplicative :

$$
PGCD(7,15)=1. \text{ On cherche } x,y :7x+15y=1

\\
\text{}
\\

\begin{align*}
\text{Avec l'algo. d'Euclide, on trouve : } &7\times(-2)+15(1)=1
\\ \implies &7\times(-2) = -15(1)+1 \\
\implies &7\times(-2)\equiv 1[15]

\end{align*}

\\
\text{}
\\

\text{Or, dans } \Z/15\Z : \overline{-2}=\overline{15-2}=\overline{13} \implies 
\begin{array}{c}
\overline{7}_{15} \times \overline{13}_{15} = \overline{1}_{15}
\\ 7 \times 13 \equiv 1[15]
\end{array}

\\
\text{}
\\

7[15],13[15] \text{ sont inverses, et aussi } \overline{7}_{15} , \overline{13}_{15}
$$

**Théorème**. Tout comme dans le cas des entiers, on énonce quelques analogies sur les clases :

- $\overline{a}_n$ est inversible si $a$ et $n$ sont copremiers ou $PGCD(a,n)=1$.
- $\overline{a}_n$ est un diviseur de zéro si $a$ et $n$ ne sont pas copremiers ou $PGCD(a,n) \ne 1$.
- Si $n$ est premier, seule $\overline0$ n’est pas inversible.

## Théorème chinois des restes

Soient $n_1$ et $n_2$ deux entiers plus grands que $1$ et copremiers, et $n = n_1 n_2$. On note $u_1$ et $u_2$ **tels que *$u_1n_1+u_2n_2 = 1$*, dont l’existence est assurée par le thm. de Bachet-Bezout. Il existe un **unique** $x[n]$ tel que $x \equiv r_1[n_1]$ et $x \equiv r_2[n_2]$. Particulièrement :

$$
\begin{cases}
x \equiv r_1[n_1] \\
x \equiv r_2[n_2]
\end{cases}
\iff
x \equiv \big(r_2(u_1n_1)+r_1(u_2n_2)\big)[n]
$$

**Exemple.** Disons qu’on cherche un $x$ qui vérifie le système de congruence suivant :

$$
\begin{cases}
x \equiv 1[3] \\
x \equiv 2[4] 
\end{cases}

\implies

\underbrace{12}_{n} =
\underbrace{3}_{n_1} \times \underbrace{4}_{n_2}

\implies \text{On cherche }r: x\equiv r[12]

\\
\text{}
\\

3u_1+4u_2=1 \implies 
\begin{cases}
u_1=-1 \\
u_2=1
\end{cases} \implies
\begin{array}{l}
x \equiv \big(2(-1\times3)+1(1\times4)\big)[12]\\x\equiv (-6+4)[12]\equiv(-2)[12]\equiv10[12]
\end{array}
$$

Il faut dire aussi que ce serait plus facile aussi si on le fait avec un tableau de cette manière :

| $\Z/12\Z$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | **10** | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\Z/4\Z$ | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | **2** | 3 |
| $\Z/3\Z$ | 0 | 1 | 2 | 0 | 1 | 2 | 0 | 1 | 2 | 0 | **1** | 2 |

On voit que $10$ a résidu $2$ divisé par $4$ ($10 \equiv 2[4]$) et résidu $1$ divisé par $3$  ($10 \equiv 1[3]$).

**Note**. On détermine $u_1$ et $u_2$ avec l’algorithme d’Euclide généralisé.

[Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)

## Codage RSA

Il s’agit d’un codage tres populaire, utilisé a une échelle industrielle, sur lequel ont travaillé Rivest, Shamir et Adleman, MIT (USA). R et S sont informaticiens, A est un matheux.

L’algorithme se divise en trois étapes : génération de clefs, chiffrement et déchiffrement. On imagine deux acteurs : Alice et Bob.

### Génération de clefs

On choisit deux grands nombres premiers distincts $p$ et $q$, puis on calcule $n=pq$. Il est à noter que, connaissant $n$, il est très difficile de trouver $p$ et $q$. Comme note pratique, $p$ et $q$ doivent être choisis de manière aléatoire et avoir une longueur en bits similaire. Après, on calcule $\varphi(n)=(p-1)(q-1)$.

<aside>
✏️ $\varphi(n)$ est la fonction indicatrice d’Euler, où elle prend un entier $n$ et retourne les nombres copremiers avec $n$ entre $1$ et $n$ inclus. En plus, elle a deux propriétés utilisées ici :

1. $\varphi(p) = p-1$, pour $p$ premier.
2. Si $m$ et $n$ sont copremiers, donc $\varphi(mn)=\varphi(m)\varphi(n)$.
</aside>

Ayant $\varphi(n)$, on choisit un entier positif $e < \varphi(n)$ et copremier avec $\varphi(n)$. On utiliser $e$ pour dire “encoding” en anglais. Puis, on définit $d$ (comme “decoding” en anglais) tel que $e \cdot d \equiv 1[\varphi(n)]$, càd. $d$ est l’inverse multiplicative modulaire de $e$ modulo $\varphi(n)$. Cette dernière opération on la fait avec l’algorithme d’Euclide généralisé.

Finalement, on appelle la “clef publique” l’ensemble $(n,e)$, càd. le module et l’exposant de chiffrement ; et la “clef privée” l’ensemble $(n,d)$, càd. le module et l’expose de déchiffrement. Bien évidemment, l’exposant de déchiffrement $d$ doit se maintenir en secret.

### Chiffrement

Bob souhaite transmettre un message $M$ à Alice. Alice lui donne sa clef publique $(n,e)$ pour que Bob puisse chiffrer le message à transmettre (mais ne lui donne pas sa clef privée $(n,d)$ !).

Bob prend son message $M$ et le transforme comme un nombre $m$ tel que $m < n$. Puis il obtient le message chiffre avec l’opération $c \equiv m^e[n]$. Finalement, Bob transmet $c$ à Alice.

### Déchiffrement

Maintenant, c’est à Alice de déchiffrer $c$. Elle doit faire le calcul suivant pour déterminer $m$ : $m \equiv c^d[n]$. Finalement, ayant $m$, elle doit invertir le padding scheme pour trouver $M$.

[RSA](https://es.wikipedia.org/wiki/RSA)