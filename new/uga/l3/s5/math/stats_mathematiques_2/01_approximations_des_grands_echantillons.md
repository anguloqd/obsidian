# 01 // approximations des grands échantillons

# Convergence, grands échantillons, approx. gaussiennes

## Inégalités : Markov et Bienaymé-Tchebychev

### Markov

L’inégalité de Markov est une majoration d’une V.A. réelle (y incluse V.A entière). Soit $*X*$une variable aléatoire réelle, supposée presque sûrement positive ou nulle, et avec une espérance définie. La première formulation est la plus commune. Si $a>0$ :

$$
\space \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} \text{\hspace{8pt}ou\hspace{8pt}} \mathbb P(X\ge\varepsilon\mathbb E[X])\le\frac{1}{\varepsilon}
$$

Dans le matériel du cours, on l’a vue de manière un peu différente, et introduisant une fonction $f$ tel que l’espérance de $f(|X|)$ et $f(a)$ sont aussi bien définies :

$$
\mathbb{P}(|X| \ge a) \le \frac{\mathbb{E}[f(|X|)]}{f(a)}
$$

### Bienaymé-Tchebychev

Celle-ci est juste un conséquence de l’inégalité de Markov, sous condition que $X$ ait une variance. Prenons la version du cours de l’inégalité de Markov, fixons une autre V.A. réelle $Y = (X - \mathbb{E}[X])$ et $f(x) = x^2$. Notons que le $(X-\mathbb{E}[X])$ est mis au carré à droite de l’inégalité mais pas à gauche. Donc : 

$$
\begin{align*}
\mathbb{P}(|Y| \ge a) \le \frac{\mathbb{E}[|Y|^2]}{a^2}

&\iff

\mathbb{P}(|X-\mathbb{E}[X]| \ge a) \le \frac{\mathbb{E}[\left(|X-\mathbb{E}[X]|\right)^2]}{a^2}

\\ &\iff
\mathbb{P}(|X-\mathbb{E}[X]| \ge a) \le \frac{\text{Var}(X)}{a^2}
\end{align*}
$$

Par contre, la version suivante est plus intuitive, où $a > 1$. Elle s’interprète comme la probabilité que la valeur de $X$ soit à $a$ écart-types ou plus de la moyenne est plus petit que $1/a^2$. Encore plus intuitive, la probabilité que la valeur de $X$ soit éloignée de la moyenne devient de plus en plus petite. Il convient imaginer une loi normale sur $X$, par exemple.

$$
\mathbb{P}(|X - \mathbb{E}[X]| \ge a\sigma) \le \frac{1}{a^2} \iff \mathbb{P}(|X - \mathbb{E}[X]| \le a\sigma) \ge 1- \frac{1}{a^2}
$$

## Différent types de convergence

Pour toutes les types de convergence qui suit, on parlera d’une suite $(X_n)$ de variables aléatoires.

### Convergence en loi vers $X$

C’est le cas si la suite des répartitions de $X$, $\big(F_{X_n}\big)$, converge à une fonction existante, appelée $F_{X_\infty}$ ou tout simplement $F_X$. Notons que les propositions avec les fonctions génératrice $\mathcal{G}_{X_n}$ et $\mathbb E[f(X_n)]$ sont analogiques.

$$
\begin{array}{lc}
\lim_{n\rightarrow\infty} F_{X_n}(x)=F_X(x) &\iff \\[3pt] \lim_{n\rightarrow\infty} \mathcal G_{X_n}(x)=\mathcal G_X(x) &\iff\\[4pt] \lim_{n\rightarrow\infty} \mathbb E[f(X_n)]=\mathbb E[f(X)]
\end{array}
$$

### Convergence en probabilité vers $X$

C’est le cas si la différence entre $X_n$ et $X$ devient arbitrairement petite le plus $n$ se rapproche de l’infini (1ère proposition).

$$
\forall\varepsilon >0, \lim_{n\rightarrow\infty} \mathbb P(|X_n-X| < \varepsilon)=1 \iff \lim_{n\rightarrow\infty}\mathbb P(|X_n-X|>\varepsilon)=0
$$

La différence avec la convergence en loi est que, pour la conv. en loi il se peut que la proba de la différence entre suite-limite ne soit pas plus petite qu’un epsilon particulier. 

### Convergence en moyenne d’ordre $p$ vers $X$

C’est le cas si le moment d’ordre $p$ de $X_n$ existe pour tout $n$, et le moment centré d’ordre $p$ devient $0$ à la limite.

$$
\mathbb E[X_n^p] \in \mathbb{R}\text{\hspace{6pt} et } \lim _{n\rightarrow \infty} \mathbb E[|X_n-X|^p]=0
$$

### Convergence *presque-sûrement* vers $X$

$$
\begin{array}{lc}
\mathbb P\left(\lim _{n\rightarrow \infty} X_n=X\right) = 1 &\iff\\[4pt]
\mathbb P \left( \sup_{m\ge n}|X_m-X|<\varepsilon\right)=1 &\iff\\[6pt]
\sum_{n=1}^\infty \mathbb P (|X_n-X|>\varepsilon) < \infty
\end{array}
$$

La première affirmation est la présentation la plus populaire. Celle-ci signifie que les valeurs de $X_n$ se rapprochent de la valeur de $X$, au sens où les événements pour lesquels $X_n$ ne converge pas à $X$ ont probabilité $0$. C’est la convergence stochastique la plus similaire à [convergence simple ou ponctuelle d’Analyse Réelle](https://en.wikipedia.org/wiki/Pointwise_convergence). À savoir :

$$
\lim f_n=f \iff \lim f_n(x)=f(x) \text{ pour tout }x\text{ dans le domaine de }f.
$$

Deux théorèmes sur cette convergence sont à noter :

- **Théorème de Slutsky**.
Si $X_n → X$ presque sûrement et $g$ est une fonction continue sur $\mathbb{R}$, alors $g(X_n) → g(X)$ presque sûrement.
- **Théorème de Slutsky “en deux dimensions/variables”**.
Si $X_n → X$ presque sûrement et $Y_n → Y$ presque sûrement et $g$ est une fonction continue sur $\mathbb{R}^2$ alors $g(X_n, Y_n) → g(X, Y)$ presque sûrement.

### Relations entre les convergences

Ces quatre définitions de convergence ont une relation d’implication utile et intéressante :

- Convergence en probabilité $\implies$ Convergence en loi
- Convergence en moyenne d’ordre $p$ $\implies$ Convergence en probabilité
- Convergence presque-sûre $\implies$ Convergence en probabilité

$$
\begin{array}{lc}
&\text{Conv. presque-sûre} \Rightarrow\hspace{-6pt} &\text{Conv. en proba.}\hspace{-6pt} &\Leftarrow \text{Conv. } p \\
&&\Downarrow&\\
&&\text{Conv. en loi}&
\end{array}
$$

En outre, la convergence en probabilité est équivalente à la convergence en loi dans le cas de la convergence vers une constante. Notons aussi que, dans le cas général, il n’y a pas, entre convergence en m.q. et convergence p.s., de domination de l’une sur l’autre.

# Loi des grands nombres (faible et forte)

## Préparation et version faible

Pour montrer les deux versions de la loi des grands nombres, on aura besoin de ce qui suit :

1. On commence avec une suite de VAs iid $(X_i)_{i\le n}=\{X_1, \dots, X_n\}$ .
2. On définit sa moyenne empirique comme $\bar X_n=\frac{1}{n} \sum _{i=1}^n X_i$.
3. Finalement, on suppose que l’espérance de $X_i$ existe, donc $\mathbb E[X_i]$ existe, pour un $i$ n’importe quel.

La loi faible dit que la moyenne arithmétique d’une suite de V.A. iid **converge en loi** vers l’espérance de ces VA. Plus facilement, la moyenne empirique tend vers la moyenne théorique si les $n$ essaies tend vers l’infini.

$$
\forall \varepsilon >0,\lim_{n \rightarrow \infty} \mathbb{P} \left(\left|\bar{X}_n -\mathbb{E}[X_i] \right| \ge \epsilon \right) = 0
$$

Notons, on fixe $\varepsilon$ en premier lieu (à une valeur n’importe quelle, mais fixée), puis un calcule la différence entre la moyenne et l’espérance. **Cet ordre est vraiment important** pour comprendre l’équation précédente comme une proposition.

Parfois, on trouve plutôt la différence avec le signe que la différence en valeur absolue, càd $(\bar{X}_n -\mathbb{E}[X_i])$. Cela dit, on peut facilement voir qu’on arrive on même résultat. Notons que le fait que toute l’expression est dans valeur absolue signifie que cette limite est majorant de la $\mathbb{P}$ de la grande expression sans valeur absolue.

$$
0 \le \lim_{n \rightarrow \infty} \mathbb{P} \left(\bar{X}_n -\mathbb{E}[X_i]\ge \epsilon\right), \text{ par définition des probabilités.}

\\[06pt]

\text{En plus, }\lim_{n \rightarrow \infty} \mathbb{P} \left(\bar{X}_n -\mathbb{E}[X_i] \ge \epsilon \right)  \le \underbrace{\lim_{n \rightarrow \infty} \mathbb{P} \left(\left|\bar{X}_n -\mathbb{E}[X_i] \right| \ge \epsilon \right)}_0

\\[02pt]

\text{Finalement, } 0 \le \underbrace{\lim_{n \rightarrow \infty} \mathbb{P} \left(\bar{X}_n -\mathbb{E}[X_i]\ge \epsilon\right)}_0 \le 0.
$$

## Version forte et remarques

On reprend la même préparation pour cette version. La loi forte affirme que la moyenne empirique **converge presque sûrement** à l’espérance.

$$
\mathbb P \left(\lim_{n\rightarrow \infty} \bar X_n = \mathbb E[X] \right)=1
$$

La loi des grands nombres n’a pas d’intérêt pratique pour le calcul statistique, contrairement au théorème central limite qui vient préciser la façon dont la moyenne empirique $\bar X_n$ converge vers $\mathbb E[X]$. Ce théorème est à la base de nombreuses propriétés essentielles des échantillons en statistique.

# Théorème central de la limite

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
\lim_{n \longrightarrow \infty} \mathbb{P}(\sqrt{n}(\bar{X}_n-\mathbb{E}[X])\in[a,b])=\frac{1}{\sigma\sqrt{2\pi}}\int_a^be^{-\frac{x^2}{2\sigma^2}}\space dx
$$

Notons qu’on peut diviser les termes de la suite $(a_n)$ par $\sigma$ pour que la variance soit réduite (càd. égale à $1$) et distribution finale soit normalisée, càd. $\mathcal{N}(0,1)$.

Le théorème de la limite centrale assume que deux conditions essentielles soient vérifiées :

- Les variables $X_i$ sont iid. : indépendantes et identiquement distribuées, ce dernier signifiant que toutes les $X_i$ suivent la même loi, qui n’est pas forcément normale.
- La variance est finie.

## Théorème de De Moivre-Laplace

> [!note]
> La première foi que le TLC a été énoncé a été sous la forme du théorème de De Moivre-Laplace, d’où son importance historique.

Le théorème de De Moivre-Laplace est juste un cas du théorème central de la limite : le cas où les VA iid. $(X_i)$ qui sont sommées suivent chacune une loi de Bernoulli. Notons que le TLC n’est pas limité à que les $(X_i)$ suivent cette loi.

Soit $\{X_1, \dots, X_n\}$ une suite des V.A. Bernoulli de paramètre $p$. Donc la suite de terme générale$\sqrt{n}(\bar{X}_n-p)$ converge en loi quand $n \rightarrow \infty$ vers une distribution normale de moyenne $0$ et variance $p(1-p)$.

$$
Z_n = \frac{X_n - np}{\sqrt{np(1-p)}} = \frac{X_n - \mu}{\sigma} \implies \left(\lim_{n\rightarrow\infty} Z_n\right)\sim\mathcal N(0,1)
$$

Quand $n$ tend vers l’infini, $\left(\lim_{n\rightarrow \infty} Z_n \right) = \mathcal N(0,1)$, c’est une égalité stricte. Par contre, quand $n$ est fini, on parle juste d’une approximation, donc $Z_n \approx \mathcal N(0,1)$. Cette approximation est acceptée si les conditions suivantes sont vérifiés :

- $np \ge 10$.
- $n(1-p) \ge 10$.

## Formulation plus pratique du TLC et sa relation avec la LGN

Soit $\bar{X}_n$ la moyenne empirique de $n$ V.A. iid. Donc :

- Loi des Grands Nombres : tant que $n \rightarrow \infty$, la distance entre $\bar{X}_n$ et $\mathbb{E}[X]$ devient plus petite que tout nombre réel $a>0$ avec probabilité $1$.
- Théorème Centrale de la Limite : tant que $n \rightarrow \infty$, la V.A. $\bar{X}_n$ converge en loi vers $\mathcal{N}(0, \frac{\sigma^2}{n})$.

Il faut laisser clair une chose : la moyenne empirique toujours va converger vers la moyenne théorique. Toujours. On peut réécrire les deux théorèmes comme suite, $a > 0$ :

$$
\begin{align*}

\text{LGN :} & \lim_{n\rightarrow\infty} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = 1

\\

\text{TCL :} & \lim_{n\rightarrow\infty} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx \space (*)

\end{align*}

\\
\\[8pt]
(*): \text{cette dernière formulation du TCL est incorrecte ! voir note dessous.}
$$

D’un côté, il semble que $(\bar{X}_n-\mathbb{E}[X])$  tend vers $0$. Au même temps, il semble que c’est égale à l’intégrale. Donc, lequel des deux ? La première.

Il existe un problème avec la deuxième : si $n \rightarrow \infty$, la variance devient $0$, et la variance comme telle n’est pas utile
$$. Imaginons la courbe qui viendrait si la variance était $0$ : il n’existe pas de dispersion autour de la moyenne et $\bar{X}_n$ serait toujours égal à $\mathbb{E}[X]$, càd. $(\bar{X}_n-\mathbb{E}[X])$ serait toujours égal à $0$.

![untitled](new/uga/l2/s3/math/probabilites_2/05_cadre_general_theoreme_centrale_de_la_limit/untitled.png)

$$
F(x)=
\begin{cases}
0, x < 0 \\
1, x \ge 0
\end{cases}
$$

![untitled](new/uga/l2/s3/math/probabilites_2/05_cadre_general_theoreme_centrale_de_la_limit/untitled_1.png)

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

> [!note]
> On pourrait concevoir deux formes de présenter le TCL : la réelle et la pratique.
>
> $$
> \begin{align*}
>
> \text{TCL réel : }
> \lim_{n\rightarrow\infty} \mathbb{P}(-a\le\sqrt{n}(\bar{X}_n-\mathbb{E}[X]) \le a) &= \int_{-a}^a \mathcal{N}\left(0,\sigma^2\right)dx
>
> \\
>
> \text{TCL pratique : }
> \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) &\approx \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx
>
> \end{align*}
> $$
>
> Il ne faut absolument pas appliquer une limite $\lim_{n \rightarrow \infty}$ dans la formulation pratique. Il sert comme une bonne approximation à partir de $n \ge 30$, mais **il ne fait objectivement plus de sens si on laisse $n$ tendre vers l’infini !** Je l’avais fais en dessus pour expliquer le besoin d’ajouter le facteur $\sqrt{n}$.