# 05 // cadre général : théorème centrale de la limite

Date de création: November 10, 2022 12:58 AM
Modifié: July 27, 2023 5:47 PM

# Fonction caractéristique : $\mathbb E[e^{iXt}]$

## Plus puissante que la fonction génératrice

La fonction caractéristique, de la même manière que la fonction de répartition, ***détermine* *le* *comportement et propriétés*** de la distribution de probabilité de $X$.

Tant que la fonction génératrice n’est pas toujours définie, la fonction caractéristique existe toujours, d’où son utilité. La fonction caractéristique d’une V.A. $X$, pour  $t\in\R$, est donc :

$$
\varphi(t)=\mathbb{E}[e^{iXt}]
$$

# Convergence de variables aléatoires

## L’existence de $“F_\infin(x)”$ notée tout simplement $F(x)$

La notion de convergence d’une V.A. n’est pas unique. Ici, on va discuter trois notions de convergence, dont une sera essentielle pour le reste des contenus : **la convergence en loi**.

Soit $\{X_1, \dots, X_n\}$ une suite des V.A. réelles, $\{F_1, \dots, F_n\}$ leur fonctions de répartition et $X$ une V.A. de fonction de répartition $F$. Donc, la suite est dite “convergente en loi” à $X$ si :

$$
\lim_{n\rightarrow\infin} F_n(x)=F(x), \space\forall x\in\R \text{ et }F \text{ continue en }x.
$$

Il existe un théorème essentiel pour le TLC qui a besoin de la notion de convergence en loi, le théorème de continuité de Lévy :

> **Théorème de continuité de Lévy**. La suite $(X_n)$ est convergente à $X$ si et seulement si leur fonctions caractéristique $(\varphi_n)$ convergent vers une fonction $\varphi$. En plus, $\varphi(t)$ serait la fonction caractéristique et continue de $X$.
> 

# Théorème centrale de la limite

## “Une somme de VAs converge à une courbe normale”

### Motivation et dérivation

La loi des grands nombres énonce qu’une somme de V.A. iid se rapproche de son espérance quand le nombre de V.A. tend vers l’infini, mais ce théorème ne nous dit pas à quelle "vitesse". C’est ici où le théorème central de la limite est utile, car il nous permet de parler sur cette vitesse.

Soit $\{X_1, \dots, X_n\}$ une suite des V.A. telles que $\mathbb{E}[X_i]=0$, $\text{Var}(X_i)=1$ et $\bar{X}_n$ leur moyenne empirique. D’après la loi des grands nombres, la distance entre $\bar{X}_n$ et $\mathbb{E}[X]$ tend vers $0$.

On sait aussi que la variance de $\bar{X}_n$ est $\frac{\sigma^2}{n}$. Donc, notons que la variance tend vers $0$ aussi si $n$ tend vers l’infini. Ceci est problématique, car la variance par définition est plus grand que $0$ mais on veut aussi qu’elle soit finie ! 

On peut penser alors à modifier la statistique $\bar{X}_n$ pour que sa variance dans ce cas soit plus grand que $0$. On arrive à la modification suivante : on crée une suite $(a_n)$ et une autre suite $(a_n\bar{X}_n)$, ce qui nous donne la variance suivante :

$$
\text{Var}(a_n\bar{X}_n) = \frac{a_n^2}{n}\cdot\text{Var}(X_i)=\frac{a_n^2}{n}
$$

Si $a_n = \sqrt n$, la variance de la modification serait égale à $1$. Donc, on le définit comme cela.

### Finalement, le théorème

Il en résulte du **théorème de continuité de Lévy** que la variable $\sqrt{n}(\bar{X}_n-\mathbb{E}[X_i])$ converge en loi vers $\mathcal{N}(0,\sigma^2)$. Finalement, on peut énoncer le théorème centrale de la limite :

$$
\lim_{n \longrightarrow \infin} \mathbb{P}(\sqrt{n}(\bar{X}_n-\mathbb{E}[X])\in[a,b])=\frac{1}{\sigma\sqrt{2\pi}}\int_a^be^{-\frac{x^2}{2\sigma^2}}\space dx
$$

Notons qu’on peut diviser les termes de la suite $(a_n)$ par $\sigma$ pour que la variance soit réduite (càd. égale à $1$) et distribution finale soit normalisée, càd. $\mathcal{N}(0,1)$.

Le théorème de la limite centrale assume que deux conditions essentielles soient vérifiées :

- Les variables $X_i$ sont iid. : indépendantes et identiquement distribuées, ce dernier signifiant que toutes les $X_i$ suivent la même loi, qui n’est pas forcément normale.
- La variance est finie.

## Théorème de De Moivre-Laplace

<aside>
🗺️ La première foi que le TLC a été énoncé a été sous la forme du théorème de De Moivre-Laplace, d’où son importance historique.

</aside>

Le théorème de De Moivre-Laplace est juste un cas du théorème central de la limite : le cas où les VA iid. $(X_i)$ qui sont sommées suivent chacune une loi de Bernoulli. Notons que le TLC n’est pas limité à que les $(X_i)$ suivent cette loi.

Soit $\{X_1, \dots, X_n\}$ une suite des V.A. Bernoulli de paramètre $p$. Donc la suite de terme générale$\sqrt{n}(\bar{X}_n-p)$ converge en loi quand $n \rightarrow \infin$ vers une distribution normale de moyenne $0$ et variance $p(1-p)$.

$$
Z_n = \frac{X_n - np}{\sqrt{np(1-p)}} = \frac{X_n - \mu}{\sigma} \implies \left(\lim_{n\rightarrow\infin} Z_n\right)\sim\mathcal N(0,1)
$$

Quand $n$ tend vers l’infini, $\left(\lim_{n\rightarrow \infin} Z_n \right) = \mathcal N(0,1)$, c’est une égalité stricte. Par contre, quand $n$ est fini, on parle juste d’une approximation, donc $Z_n \approx \mathcal N(0,1)$. Cette approximation est acceptée si les conditions suivantes sont vérifiés :

- $np \ge 10$.
- $n(1-p) \ge 10$.

## Formulation plus pratique du TLC et sa relation avec la LGN

Soit $\bar{X}_n$ la moyenne empirique de $n$ V.A. iid. Donc :

- Loi des Grands Nombres : tant que $n \rightarrow \infin$, la distance entre $\bar{X}_n$ et $\mathbb{E}[X]$ devient plus petite que tout nombre réel $a>0$ avec probabilité $1$.
- Théorème Centrale de la Limite : tant que $n \rightarrow \infin$, la V.A. $\bar{X}_n$ converge en loi vers $\mathcal{N}(0, \frac{\sigma^2}{n})$.

Il faut laisser clair une chose : la moyenne empirique toujours va converger vers la moyenne théorique. Toujours. On peut réécrire les deux théorèmes comme suite, $a > 0$ :

$$
\begin{align*}

\text{LGN :} & \lim_{n\rightarrow\infin} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = 1

\\

\text{TCL :} & \lim_{n\rightarrow\infin} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx \space (*)

\end{align*}

\\
\\[8pt]
(*): \text{cette dernière formulation du TCL est incorrecte ! voir note dessous.}
$$

D’un côté, il semble que $(\bar{X}_n-\mathbb{E}[X])$  tend vers $0$. Au même temps, il semble que c’est égale à l’intégrale. Donc, lequel des deux ? La première.

Il existe un problème avec la deuxième : si $n \rightarrow \infin$, la variance devient $0$, et la variance comme telle n’est pas utile
$$. Imaginons la courbe qui viendrait si la variance était $0$ : il n’existe pas de dispersion autour de la moyenne et $\bar{X}_n$ serait toujours égal à $\mathbb{E}[X]$, càd. $(\bar{X}_n-\mathbb{E}[X])$ serait toujours égal à $0$.

![Untitled](new/uga/l2/s3/math/S3%20math%20probabilités%202/05%20cadre%20général%20théorème%20centrale%20de%20la%20limit/Untitled.png)

$$
F(x)=
\begin{cases}
0, x < 0 \\
1, x \ge 0
\end{cases}
$$

![Untitled](new/uga/l2/s3/math/S3%20math%20probabilités%202/05%20cadre%20général%20théorème%20centrale%20de%20la%20limit/Untitled%201.png)

$$
"f(x)"=
\begin{cases}
1, x=0 \\
0, x \ne 0
\end{cases}
$$

Il est correct de construire une fonction de répartition qui représenterait la fonction de répartition de $(\bar{X}_n-\mathbb{E}[X])$. En fait, une variable aléatoire avec telle fonction de répartition est appelée une **variable aléatoire dégénérée**.

Par contre, il n’est pas possible de construire une densité, car il devrait avoir une aire sous la courbe égale à $1$ quand $x=0$, mais ce n’est pas possible, car le “rectangle” sous $f(x)$ n’as pas de ampleur, donc son aire est toujours $0$.

Le choix de multiplier $(\bar{X}_n-\mathbb{E}[X])$ par $\sqrt{n}$ permet de laisser tendre $n$ vers l’infini et que la variance ne soit pas nulle. Particulièrement, on garanti l’existence d’une variance non-nulle, mais aussi non-infinie, c’est qui nous est utile.

<aside>
💡 On pourrait concevoir deux formes de présenter le TCL : la réelle et la pratique.

$$
\begin{align*}

\text{TCL réel : }
\lim_{n\rightarrow\infin} \mathbb{P}(-a\le\sqrt{n}(\bar{X}_n-\mathbb{E}[X]) \le a) &= \int_{-a}^a \mathcal{N}\left(0,\sigma^2\right)dx

\\

\text{TCL pratique : }
\mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) &\approx \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx

\end{align*}
$$

Il ne faut absolument pas appliquer une limite $\lim_{n \rightarrow \infin}$ dans la formulation pratique. Il sert comme une bonne approximation à partir de $n \ge 30$, mais **il ne fait objectivement plus de sens si on laisse $n$ tendre vers l’infini !** Je l’avais fais en dessus pour expliquer le besoin d’ajouter le facteur $\sqrt{n}$.

</aside>