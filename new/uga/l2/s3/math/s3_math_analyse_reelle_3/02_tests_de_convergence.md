# 02 // tests de convergence

# Comparaison à une série géométrique

## Règle de d’Alembert et Critère de d’Alembert

### Règle de d’Alembert

Soit $\Sigma u_n$ une série à termes réels ou complexes. Supposons que $k \in [0, 1[$ et $N \in \N$ tel que si $n ≥ N, |u_{n+1}| ≤ k|u_n|$. Alors la série $\Sigma u_n$ converge.

### Critère de d’Alembert

C’est un corollaire de la règle d’Alembert. Soit $\Sigma u_n$ à termes strictement positifs et supposons qu’il existe $\ell$ tel que $\lim_{n\rightarrow \infin} |\frac{u_{n+1}}{u_n}| = \ell$
.

- si $\ell < 1$$\implies$ $\Sigma u_n$ converge.
- si $\ell >1 \implies \Sigma u_n$ ne converge pas.
- si $\ell = 1$, elle peut converger ou diverger. On ne peut rien conclure.
**De même si la limite n’existe pas !**

Il est à noter que c’est plus facile d’utiliser d’Alembert avec des séries à termes positifs.

**Note pratique.** On peut écrire le quotient $\frac{u_{n+1}}{u_n}$ comme $|\frac{u_{n+1}}{u_n}|$, et si ce dernier converge, le premier converge aussi.

Après, encore si $(u_n)$ série a termes positifs, et supposant que $\Sigma u_n$ converge, on peut sommer $\Sigma u_n$ dans n’importe quel ordre. On ne change pas ni la nature ni la somme de $\Sigma u_n$. (on peut appliquer les propriétés commutative, associative et distributive !)

## Règle de Cauchy et Critère de Cauchy

### Règle de Cauchy

Soit $\Sigma u_n$ une série à termes réels ou complexes. Supposons que $k \in [0, 1[$ et $N \in \N$ tel que si $n ≥ N, \sqrt[n]{|u_n|} \le k$. Alors, la série $\Sigma u_n$ converge.

### Critère de Cauchy

C’est un corollaire de la règle d’Alembert. Soit $\Sigma u_n$ à termes strictement positifs et supposons qu’il existe $l$ tel que $\lim_{n\rightarrow \infin} \sqrt[n]{|u_n|} = \ell$
.

- si $\ell < 1$$\implies$ $\Sigma u_n$ converge.
- si $\ell >1 \implies \Sigma u_n$ ne converge pas.
- si $\ell = 1$, elle peut converger ou diverger. On ne peut rien conclure.

# Comparaison a une série de Riemann

## Particulièrement, domination par une série de Riemann

On part d’une série $\sum u_n$ à termes réels ou complexes.

1. S’il existe $\alpha > 1$ tel que $n^\alpha |u_n| \longrightarrow \ell\in \R \implies \sum u_n$ converge.
2. Su $n|u_n| \longrightarrow \ell\ne 0 \implies \sum |u_n|$ diverge (elle ne converge pas **absolument**, mais il se peut qu’elle converge ! C’est la notion de semi-convergence). 

# Utilisation d’une intégrale

## “Si l’intégrale converge, la série aussi”

Soit $f : [1, \infin] \mapsto \R^+$ et décroissante.
Donc $\sum f(n)$  converge $\iff \int_0^\infin f(t)dt$ converge et finie.
Si l’un diverge, l’autre aussi !

# Les séries alternées

## Séries de la forme $\sum (-1)^n u_n$

Une série alternée est une série dont les termes sont alternativement positifs et négatifs.

Si $(u_n)$ est positif, décroissante et convergeant vers $0$, la série $\sum(-1)^nu_n$ converge.
De plus, sa somme partielle $S_n = \sum_i^n (-1)^n u_n$ vérifie que $|S_\infin-S_n| \le u_{n+1}$.

# Utilisation d’un développement limité

## Remplacer une expr. par une autre similaire et plus simple

On peut utiliser juste les premiers termes du développement limité d’une expression/fonction pour trouver une équivalence (au sens de convergence) entre deux fonctions. Par exemple :

$$
\text{Autour de 0, }\ln(1+x)=\sum_{n=1}^\infin \frac{(-1)^{n+1}x^n}{n}=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}\dots
\newline
\text{ }
\newline
\implies \ln(1+x) \sim x \text{ quand } x\longrightarrow 0 
$$

Cette dernière similitude nous permet de remplacer, dans une certaine expression, $\ln(1+x)$ par $x$, et voir si tel remplacement nous mène à conclure une convergence ou divergence. Notons que $x$ est le premier terme du DL de $\ln(1+x)$. Autour de $0$, $\ln(1+x) \simeq x$.

**Note pratique**. L’approximation la plus simple serait de garder juste **le premier terme non nul** du développement.

# Critère d’Abel

## Utile quand $\sum u_n$ pas absolument convergente

Soit la suite $(u_n)$ positive, décroissante et convergente vers $0$ ; et la suite $(v_n)$ bornée.
Donc $\sum u_nv_n$ converge est la somme partielle $S_n$ vérifie $|S_\infin-S_n| \le 2Mu_n$, où $M$ est un majorant quelconque de $(|v_n|)$.

Ce critère est principalement pertinent si $\sum u_n$ n’est pas absolument convergente. Si $\sum u_n$, le critère est vrai mais trop évident et pas trop utile.