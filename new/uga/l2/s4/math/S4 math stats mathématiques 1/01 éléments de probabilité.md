# 01 // éléments de probabilité

Date de création: January 15, 2023 11:25 PM
Modifié: June 9, 2023 5:41 PM

[Slides de rappels de proba](slides_rappels_proba_stat1_annote_2301.pdf)

# Rappels

| Statistiques | Probabilités |
| --- | --- |
| Observation | Réflexion (anticipation) |
| Moyenne empirique : $\sum_i x_if_i$ | Espérance : $\sum_i x_iP(X=x_i), \int_i xf_X(x)dx$ |
| Fréquence (relative, mais absolue aussi) | Probabilité |

Le passage de la statistique (pratique) pour déduire la probabilité (théorie) est une ***inférence***.

On rappellera juste quelques propriétés mathématiques très utilisées dans ce domaine :

- Linéarité de l’espérance : $E[aX+bY+c] = aE[X]+bE[Y]+c$, **sans cond. sur $X$ et $Y$**
- La variance est invariante sous translation et quadratique : $Var(aX+b) = a^2Var(X)$
- Si X et Y sont deux V.A. indépendantes, alors $Var(X+Y)=Var(X)+Var(Y)$
- La fonction de répartition d’une V.A. $X$ est $F_X(t) = P(X\le t)$

## Loi de Bernoulli

$X$ suit une loi de Bernoulli : $X  \sim \mathcal{B}(p)$. Elle modélise une expérience à deux issues : réussite ou échec. La réussite est de probabilité $p$ et l’échec de probabilité $1-p$.

- $E[X]=p$
- $Var(X)=p(1-p)$

## Loi binomiale

$X$ suit une loi binomiale : $X \sim \mathcal{B}(n,p)$. Elle modélise une suite de V.A. de Bernoullis identiques et indépendantes.

$$
P(X=k)= \binom{n}{k}p^k(1-p)^{n-k}, \text{où } \binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

- $E[X]=np$
- $Var(X)=np(1-p)$

## Loi normale

$X$ suit une loi normale : $X \sim \mathcal{N}(\mu,\sigma^2)$, où $\mu$ sa moyenne et $\sigma^2$ sa variance. Une somme de V.A. iid. converge en loi vers cette loi (peu importe la loi des V.A. de base !), selon le Théorème de la Limite Centrale, d’où son importance.

On utilise $\mathcal{N}(0,1)$ pour construire les autres lois normaux.

$$
\mathcal{N}(0,1)=\frac{1}{\sqrt{2\pi}}e^\frac{-x^2}{2} \implies \mathcal{N}(\mu,\sigma^2)=\sigma\mathcal{N}(0,1)+\mu
$$

**Théorème**. Soient $X,Y$ deux V.A. qui suivent une loi normale chacune. Si elles sont indépendantes, donc la nouvelle variable aléatoire $(X+Y)$ suit aussi une loi normale $\mathcal{N}(\mu_X+\mu_Y, \sigma^2_X + \sigma^2_Y)$. On peut généraliser à une somme de plus de deux V.A.

# Loi des statistiques

## Loi de $\chi^2$ (khi-deux)

$X$ suit une loi de khi-deux : $X \sim \chi^2(n)$, où $n$ les degrés de liberté. C’est une somme des carrés de n V.A. normaux standard.

$$
X_1^2+\dots+X_n^2,\space X_i\sim\mathcal{N}(0,1)
$$

- $E[X]=n$
- $Var(X)=2n$
- Si $X_1 \sim \chi^2(n_1)$ et $X_2 \sim \chi^2(n_2)$ et elles sont indépendantes,
donc $(X_1+X_2)\sim \chi^2(n_1+n_2)$

## Loi de Student

$X$ suit une loi de Student : $X \sim t(k)$, où $k$ les degrés de liberté. On suppose que $U$ et $V$ sont deux V.A indépendantes, $U$ est normale centrée-réduite et $V$ est khi-deux à $k$ degrés.

$$
X=\frac{U}{\sqrt{V/k}}
$$

- $E[X]=0$
- $Var(X)=\frac{k}{k-2}, k>2$

## Loi de Fisher

$X$ suit une loi de Fisher : $X \sim \mathcal{F}(d_1,d_2)$, où $d_1,d_2$ degrés de liberté. $U$ et $V$ sont indépendantes et chacune suit une loi de khi-deux à $d_1$ et $d_2$ degrés de liberté, respectivement.

$$
X=\frac{U/d_1}{V/d_2}
$$

- $E[X]=\frac{d_2}{d_2-1}, d_2>2$
- $Var(X)=\frac{2d_2^2(d_1+d_2-2)}{2d_1(d_2-2)(d_2-4)}, d_2>4$

## Propriétés entres ces lois

- Si $X\sim\mathcal{F}(d_1,d_2)$, donc $1/X \sim \mathcal{F}(d_2,d_1)$
- Si $X\sim t(k)$, alors $X^2 \sim \mathcal{F}(1,k)$
- Si $X\sim\mathcal{N}(0,1)$, alors $X^2\sim\mathcal{F}(1,\infin)$

# Théorèmes limites

## Convergence en loi

Soit $(X_n)$ une suite de variables aléatoires. On dit que $(X_n)$ converge en loi vers un certain $X$ si et seulement si…

$$
\lim_{x \rightarrow\infin}F_{X_n}(x)=F_X(x), \forall x \in \R
$$

Où $F_{X_i}(x)$ est la fonction de répartition de la V.A. $X_i$.

## Loi des grands nombres

Soit $(X_n)$ une suite de V.A. iid. qui admettent la même espérance $\mu$ et le même ecart-type $\sigma$ (déjà conséquence de iid). Alors, la moyenne empirique tend vers $\mu$ (la moyenne théorique) quand $n$ tend vers l’infini.

$$
\lim_{n\rightarrow\infin}\bar{X_n}=\lim_{n\rightarrow\infin}\frac{1}{n}\sum_{i=0}^nx_i=\mu
$$

## Théorème centrale de la limite

Soit $(X_n)$ une suite de V.A. iid. qui admettent la même espérance $\mu$ et le même ecart-type **fini $\sigma$** (déjà conséquence de iid). Alors, la moyenne de ces V.A tend vers une loi normale $\mathcal{N}(\mu,\sigma^2/n)$, mais plus formellement :

$$
\lim_{n\rightarrow\infin} \sqrt{n}(\bar{X}_n-\mu)=\mathcal{N}(0,\sigma^2)
$$

## Approximation d’une binomiale par une normale

Sous quelques conditions, on peux approximer une loi binomiale décemment avec une loi normale. Notamment, on a besoin de $n \ge 50$ et au moins une de ces conditions :

- $0.4 \le p \le 0.6$, ou
- $np(1-p) \ge 18$, ou
- $np>5$ et $n(1-p)>5$

Si l’une des ces conditions est vérifié, on peut dire que $\mathcal{B}(n,p) \simeq \mathcal{N}(np,np(1-p))$.

## Par rapport à $\chi^2$, Student et Fisher

- Si $X\sim\mathcal{F}(d_1,d_2)$, alors $\lim_{d_2\rightarrow\infin} d_1X =\chi^2(d_1)$
- Student converge à une normale centrée-réduite : $\lim_{k\rightarrow\infin} t(k) = \mathcal{N}(0,1)$