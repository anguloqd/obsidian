## 03 // cas dénombrable : fonctions génératrices, inégalités et loi des grands nombres

## Fonctions génératrices

### Définition générale

> *Une fonction génératrice est un dispositif quelque peu similaire à un sac. Au lieu de transporter de manière détachée de nombreux petits objets, ce qui pourrait être gênant, on les met tous dans un sac, et on n'a alors qu'un seul objet à transporter, le sac.

—* George Pólya

> *Une fonction génératrice est une corde à linge sur laquelle on accroche une séquence de nombres à afficher.

—* Hebert Wilf

Une *fonction génératrice d’une suite* est juste une manière de codifier une **suite** dans une **série**, prenants les valeurs de la première et les mettant comme des coefficients dans la deuxième. Par exemple :

$$
(a_n) = \{a_0, a_1, \dots, a_n\}\text{ suite de base.}

\newline

(a_0 + a_1x+a_2x^2+\dots+a_nx^n)  \text{ fonction génératrice de la suite.}
$$

Il n’existe pas une seule forme propre des fonction génératrices. Celle en-dessus est une fonction génératrice appelée une *série formelle*, qui est une généralisation des polynômes mais avec une infinité de termes. Ce type de série particulière est définie de telle manière que son convergence n’est pas importante ni nécessaire pour faire des manipulations algébriques communes (addition, multiplication, sommes partielles, etc.).

En réalité, on ne s’intéresse pas à voir la fonction comme une “fonction”. Elle n’est même pas une fonction dans le sens où elle établit une correspondance d’un ensemble de nombres à un autre. Aussi, la variable $x$ reste indéterminée, on ne s’intéresse pas non plus aux valeurs qu’elle pourrait prendre.

### Définition en théorie des probabilités

Maintenant, on peut parler d’une fonction génératrice d’une variable aléatoire. Toute variable aléatoire $X$ associe ses résultats — l’univers — à des probabilités — la loi de la VA — dont la somme fait $1$.  Puisque une suite est un ensemble indexé, on suppose que $X$ peut prendre que des valeurs en $\mathbb{N}$, et puis on indexe l’univers, pour finalement pouvoir appliquer un fonction génératrice.

Pensons le cas fini en premier et supposons que $X$ est une pièce **pipée** montrant pile avec $\mathbb P(X=0)=0.9$ et face avec $\mathbb P(X=1)=0.1$. Donc, la fonction génératrice $f$ de $X$ serait :

$$
f(z)=\mathbb{E}[z^X]=\sum_{k=0}^1 (z^k \cdot \mathbb P(X=k)) = 0.9+0.1z
$$

Maintenant dans le cas générale, la définition d’une *fonction génératrice de probabilités* $f$ d’une V.A $X \in\mathbb{N}$ est la suivante. Notons qu’on peut le faire même avec une infinité de valeurs possibles pour la V.A. $X$ !

$$
f(z)=\mathbb{E}[z^X]=\sum_{k=0}^\infty (z^k \cdot 
\mathbb P(X=k)) = 
\newline
\text{}
\newline
\mathbb P(X=0)+\mathbb P(X=1)z+\mathbb P(X=2)z^2+\mathbb P(X=3)z^3 \dots
$$

Notons que $f(1) = \sum_{k=0}^\infty \mathbb P(X=k) = 1$. C’est simplement la somme des probabilités.

Il y a deux propriétés importantes si on vérifie que $|z| ≤ 1$ :

- $f(z)$ est bien définie, càd. $f(z)\in\mathbb{R}$, car elle serait inférieur ou égale à la série $\sum(\mathbb P(X=k))$ qui on sait que converge à $1$. Ceci découle des propriétés des séries géométriques (on pourrait voir quelques polynômes comme des suites géométriques).
- La fonction est croissante et $0 \le f(z) \le 1$.

### Propriétés

#### Applications sur les lois de Bernoulli et binomiale

Toujours avec $|z| ≤ 1$, si un ensemble de V.A. $\{X_1, \dots, X_n\}$ sont indépendantes entre elles du début, leurs fonctions génératrices les sont aussi.

$$
\mathbb{E}[z^{\sum_{i=1}^n X_i}] = \prod_{i=1}^n \mathbb{E}[z^{X_i}]
$$

Encore plus, si la famille de V.A. $X_i$ sont indépendantes et identiquement distribués, — comme c’est le cas dans une loi binomiale, qui est une collection de V.A. de Bernoulli — alors :

$$
\mathbb{E}[z^{\sum_{i=1}^n X_i}] = (\mathbb{E}[z^{X_k}])^n \text{, où } k \in \mathbb{N} \text{ et } 1 \le k \le n
$$

#### Applications sur les dérivées, l’espérance et la variance

Puisque la fonction génératrice a la forme d’un polynôme, la $k$-ième dérivée de la fonction génératrice vérifie l’égalité suivante :

$$
f^{(k)}(0) = k!\cdot \mathbb P(X=k)
$$

#### Fonctions génératrices pour construire l’espérance et variance

Les fonctions génératrices de probabilités nous permet facilement de trouver l’espérance et la variance. Notons que si $f$ est dérivable en $1$, donc :

$$
f'(1)=\sum_{k=0}^\infty (k\cdot \mathbb P(X=k))=\mathbb{E}[X] \text{, et}

\newline
\text{}
\newline

f''(1)= \sum_{k=0}^\infty((k)(k-1)\cdot \mathbb P(X=k)) \implies f'(1) + f''(1) = \mathbb{E}[X^2]
$$

Finalement, on se rend compte de que on peut trouver et exprimer l’espérance et même la variance d’une variable aléatoire à partir de la fonction génératrice.

$$
\mathbb{E}[X] = f'(1) \hspace{8pt}\text{ et\hspace{8pt} Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = [f'(1)+f''(1)]-[f'(1)]^2
$$

#### Approximation poissonienne d’une binomiale

Soit $(X_n)$ une suite des VA entières non-négatives représentés chacune par la fonction génératrice $f_n$, et $X$ une VA entière non-négative de fonction génératrice $f$. Les deux propositions sont équivalentes, avec $k\in\mathbb{N}$ et $0 \le z \le 1$ :

$$
\lim_{n \rightarrow \infty} \mathbb{P}(X_n=k) = \hspace{-1pt}\overbrace{\mathbb{P}(X=k)}^\text{si l'une existe...} \iff \lim_{n \rightarrow \infty} f_n(z) = \hspace{-8pt}\overbrace{f(z)}^\text{l'autre aussi}
$$

> **Théorème de continuité de Lévy**. La suite $(X_n)$ est convergente à $X$ si et seulement si leur fonctions caractéristique $(\varphi_n)$ convergent vers une fonction $\varphi$. En plus, $\varphi(t)$ serait la fonction caractéristique et continue de $X$.

Cette propriété est utile pour construire une approximation entre la loi de Poisson et la loi Binomiale. Supposons que les VA dans $(X_n)$ sont des loi binomiales, avec $n$ le nombre de essais de Bernoulli de la VA et $p_n$ la probabilité de succès de chaque essai individuel.

On sait que l’espérance de la loi Binomiale est $np_n$, **on veut donc définir $p_n$ en termes de $n$** tel que $\lim_{n \rightarrow \infty} np_n$ converge vers un nombre $\lambda$, respectant toujours que la somme des toute probabilité égal 1. Cela implique que, quand $n$ augmente, $p_n$ diminue. Une telle définition de $p_n$ pourrait être $p_n = \frac{\lambda}{n}$, et on voit clairement que $\lim_{n\rightarrow\infty} np_n = \lim_{n\rightarrow\infty}n\left(\frac{\lambda}{n}\right) = \lambda$, mais $p_n$ peut prendre n’importe quelle forme arbitraire telle que elle converge vers un réel $\lambda$, comme par exemple $\lim_{n\rightarrow\infty} np_n = \lim_{n\rightarrow\infty}n\left(\frac{\lambda}{n + \frac{1}{n}}\right) = \lambda$.

Notons que la fonction génératrice $f_n(z)$ de un loi binomial $X_n$ est $(1-p_n+zp_n)^n$. Donc, si on fait $n \rightarrow \infty$ :

$$
f_n(z)=e^{n\ln(1-p_n+zp_n)}=e^{n\ln(1+p_n(z-1))}
$$

Ici, on est algébriquement bloqués, on ne peut plus continuer (c’est trop compliqué). Cela dit, on sait que le polynôme de Taylor de première degré de $\ln(1+x)$ correspond à $x$, pour $x$ petit et autour de $0$, ce qui est le cas de $p_n(z-1)$. C’est-à-dire, $\ln(1+p_n(z-1)) \simeq p_n(z-1)$. On remplace sur la dernière expression :

$$
f_n(z)=e^{n\ln(1+p_n(z-1))}\approx e^{np_n(z-1)}=e^{\lambda(z-1)}
$$

Ici, on a démontré qu’il existe effective la limite quand $n \rightarrow \infty$ de $f_n(z)$, laquelle on va appeler tout simplement $f(z)$. Donc, par l’équivalence de propositions précédente, on a démontré aussi qu’il existe aussi la limite de la loi de probabilités $\mathbb{P}(X_n=k)$ quand $n \rightarrow \infty$, sans besoin d’expliciter son expression mathématique.

## Inégalités notables

### Inégalité de Markov

L’inégalité de Markov est une majoration d’une V.A. réelle (y incluse V.A entière). Soit $*X*$une variable aléatoire réelle, supposée presque sûrement positive ou nulle, et avec une espérance définie. La première formulation est la plus commune. Si $a>0$ :

$$
\space \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} \text{\hspace{8pt}ou\hspace{8pt}} \mathbb P(X\ge\varepsilon\mathbb E[X])\le\frac{1}{\varepsilon}
$$

Dans le matériel du cours, on l’a vue de manière un peu différente, et introduisant une fonction $f$ tel que l’espérance de $f(|X|)$ et $f(a)$ sont aussi bien définies :

$$
\mathbb{P}(|X| \ge a) \le \frac{\mathbb{E}[f(|X|)]}{f(a)}
$$

### Inégalité de Bienaymé-Tchebicheff

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

## Loi faible des grands nombres

### “La moyenne empirique tend vers la moyenne théorique”

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
