# 03 // séries entières

# Définitions : série entière et rayon de convergence

## Pourquoi série “entière” ?

Une série entière est une série de la forme $\sum u_n x^n$, où $(u_n)$ suite réelle et $x \in \mathbb{C}$ (mais on se limitera aux réels). Elle est dite *entière* car l’exposant de $x$ est entier.

## Rayon et domaine de convergence : les valeurs de $x$ tels que $\sum u_n x^n$ converge

On définit $E = \{ x :  (|u_n|x^n) \text{ bornée}\}$. Notons qu’il peuvent avoir plusieurs $x$ qui vérifient cette condition. Finalement, le rayon de convergence de la série entière $\sum u_n x^n$ est dénoté $R$ :

$$
R=
\begin{cases}
\sup E, \text{ si } E \text{ est borné} \\
+\infin, \text{ sinon}
\end{cases}
$$

On a construit tout cela pour déterminer finalement la nature de $\sum u_n x^n$ :

- Si $|x| < R$, la série converge
    - **Corollaire**. Si $\sum u_n x^n$ converge en $x=x_0$, donc $|x_0| \le R$.
- Si $|x| > R$, la série diverge
    - **Corollaire**. Si $\sum u_n x^n$ diverge en $x=x_0$, donc $|x_0| \ge R$.
- Si $|x| = R$, on ne peut rien conclure.
Elle peut converger ou diverger sur les bornes.

L’ensemble de valeurs de $x=\{x_0, \dots, x_n\}$ où la série $\sum u_n x^n$ converge est appelé le domaine de convergence $D$ : $D = \{ x : \sum u_n x^n \text{ converge}\}$ .

# Détermination du rayon de convergence

## Règle de d’Alembert

Supposons une suite réelle $(u_n)$ tel que $u_n \ne 0$ et $\lim_{n\rightarrow \infin} |\frac{u_{n+1}}{u_n}| = \ell$. Donc :

$$
R =
\begin{cases}
\frac{1}{\ell}, \text{ si }  \ell > 0\\
+\infin, \text{ si } \ell=0 \\
0, \text{ si }  \ell\longrightarrow+\infin
\end{cases}
$$

## Règle de Cauchy

Supposons une suite réelle $(u_n)$ tel que $\lim_{n\rightarrow \infin} \sqrt[n]{|u_n|} = \ell$. Donc :

$$
R =
\begin{cases}
\frac{1}{\ell}, \text{ si }  \ell > 0\\
+\infin, \text{ si } \ell=0 \\
0, \text{ si }  \ell\longrightarrow+\infin
\end{cases}
$$

## “Somme” des séries

Soient $\sum u_n x^n$ et $\sum v_n x^n$ deux séries entières avec rayons de convergence $R_1$ et $R_2$, respectivement. Donc, si on crée la série “somme” $\sum (u_n+v_n)x^n$ avec rayon de convergence $R$ :

- $R \ge \min(R_1,R_2)$
- $R_1 \ne R_2 \implies R = \min(R_1,R_2)$

# Séries entières d’une variable réelle

## Intervalle de convergence $]R,R[$ et la fonction $S$

Tout ce qu’on a présenté avant peut s’appliquer aussi aux nombres complexes, mais maintenant on se limite aux réels.

L’intervalle de convergence est juste une idée dérivée du rayon de convergence. Si $R$ est le rayon de convergence, donc $]-R, R[$ est l’intervalle de convergence. En plus, on peut définir une fonction $S$ qui correspond chaque point de l’intervalle à sa limite :

$$
\begin{gather*}
\begin{align*}
S :
\space\space
&]-R,R[
\space\space
\mapsto
\space
\R \\
&{x}
\space\space
=
\space
\sum_{n=0}^{+\infin} u_nx^n
\end{align*}
\end{gather*}
$$

Cette fonction $S$ est intégrable sous Riemann et aussi dérivable. Dans le cas de l’intégrale, l’intervalle d’intégration est dès $0$ à $x$ ou dès $x$ à $0$, pour $x \in ]-R,R[$. 

$$
\int_0^xS(t)dt = \sum_{n=0}^{+\infin}u_n\frac{x^{n+1}}{n+1}
\space\space\space
\text{ et }
\space\space\space S'(x)=\sum_{n=1}^{+\infin}nu_nx^{n-1}
$$

# Développement en série entière

## Série de Taylor : la connexion série entières et dev. limités

Finalement, on connecte les séries entières avec les développements limités. Avec $r >0$, on prend une fonction $f : \space ]-r, r[ \space \mapsto \R$.

Cette fonction est dite “développable en $0$” s’il existe une série $\sum u_nx^n$ de rayon de convergence $R \ge r$ tel que $f(x) = \sum_{n=0}^{+\infin}u_nx^n$, pour tout $x \in \space ]-r,r[$.

En particulier, la série que permet de réécrire $f(x)$ sous forme de série entière est la série de Taylor. À savoir : $f(x) = \sum_{n=0}^{+\infin} \frac{f^{(n)}(0)}{n!}x^n$.

## Développements limités usuels

> [!note]
> Mnéumonique TEBG : trigo, exponentiel, binôme et géométrique.

## Formule de binôme généralisée

Rappelons la formule du binôme, pour $n\in\mathbb{N}$ :

$$
(a+b)^n=\sum_{k=0}^n C^n_k a^k b^{n-k}, \text{ où } C^n_k = \frac{n!}{k!(n-k)!}
$$

Donc, soit $\alpha \in \R \setminus \Z$ et $|x| < 1$, alors :

$$
(1+x)^\alpha=1+\sum_{n=1}^{+\infin}\frac{\alpha(\alpha-1)\dots(\alpha-n+1)}{n!}x^n
$$