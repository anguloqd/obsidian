## 05 // cadre général : théorème central de la limite

## Fonction caractéristique : $\mathbb E[e^{iXt}]$

### Existence universelle contrairement à la fonction génératrice

La fonction caractéristique, de la même manière que la fonction de répartition, ***détermine uniquement*** la distribution de probabilité de $X$.

La fonction caractéristique existe toujours pour toute variable aléatoire (car $|e^{iXt}| = 1$), contrairement à la fonction génératrice des moments qui peut ne pas être définie. La fonction caractéristique d'une V.A. $X$, pour $t\in\mathbb{R}$, est :

$$\varphi_X(t)=E(e^{iXt})$$

## Convergence de variables aléatoires

### Convergence en loi

La notion de convergence d'une V.A. n'est pas unique. Ici, nous étudions principalement **la convergence en loi** (ou convergence en distribution).

Soit $(X_n)_{n \geq 1}$ une suite de V.A. réelles, $(F_n)_{n \geq 1}$ leurs fonctions de répartition et $X$ une V.A. de fonction de répartition $F$. La suite $(X_n)$ **converge en loi** vers $X$ (noté $X_n \stackrel{d}{\rightarrow} X$) si :

$$\lim_{n\rightarrow\infty} F_n(x) = F(x), \quad \forall x \in \mathbb{R} \text{ où } F \text{ est continue}$$

**Théorème de continuité de Lévy** : La suite $(X_n)$ converge en loi vers $X$ si et seulement si leurs fonctions caractéristiques $(\varphi_n)$ convergent ponctuellement vers une fonction $\varphi$ continue en $0$. De plus, $\varphi$ est alors la fonction caractéristique de $X$.

## Théorème central de la limite

### "Une somme normalisée de VAs converge vers une loi normale"

#### Motivation et dérivation

La loi des grands nombres énonce qu'une moyenne de V.A. iid se rapproche de l'espérance, mais ne quantifie pas la vitesse de convergence. Le théorème central de la limite (TCL) caractérise cette vitesse.

Soit $(X_i)_{i \geq 1}$ une suite de V.A. iid avec $\mathbb{E}[X_i] = \mu$ et $\text{Var}(X_i) = \sigma^2 < \infty$. Soit $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ la moyenne empirique.

D'après la LGN : $\bar{X}_n \stackrel{P}{\rightarrow} \mu$ quand $n \rightarrow \infty$.

La variance de $\bar{X}_n$ est $\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n} \rightarrow 0$ quand $n \rightarrow \infty$.

Pour obtenir une limite non dégénérée, nous normalisons par $\sqrt{n}$ :

$$Z_n = \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} = \frac{\sum_{i=1}^n (X_i - \mu)}{\sigma\sqrt{n}}$$

Cette normalisation garantit que $\text{Var}(Z_n) = 1$ pour tout $n$.

#### Énoncé du théorème central de la limite

**Théorème (TCL de Lindeberg-Lévy)** : Soit $(X_i)_{i \geq 1}$ une suite de V.A. iid avec $\mathbb{E}[X_i] = \mu$ et $\text{Var}(X_i) = \sigma^2 < \infty$. Alors :

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \stackrel{d}{\rightarrow} \mathcal{N}(0,1) \quad \text{quand } n \rightarrow \infty$$

**Équivalence** : Pour tout $a, b \in \mathbb{R}$ avec $a < b$ :

$$\lim_{n \rightarrow \infty} \mathbb{P}\left(a \leq \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \leq b\right) = \frac{1}{\sqrt{2\pi}}\int_a^b e^{-\frac{x^2}{2}} dx$$

**Conditions du TCL** :
1. Les variables $X_i$ sont **iid** (indépendantes et identiquement distribuées)
2. La variance $\sigma^2$ est **finie**

**Note** : La loi des $X_i$ peut être quelconque (pas nécessairement normale).

### Théorème de De Moivre-Laplace

Le théorème de De Moivre-Laplace est un cas particulier historique du TCL pour les variables de Bernoulli.

Soit $(X_i)_{i \geq 1}$ une suite de V.A. iid de Bernoulli de paramètre $p \in (0,1)$. Soit $S_n = \sum_{i=1}^n X_i$.

Alors : $\mathbb{E}[S_n] = np$ et $\text{Var}(S_n) = np(1-p)$.

**Théorème** :

$$Z_n = \frac{S_n - np}{\sqrt{np(1-p)}} \stackrel{d}{\rightarrow} \mathcal{N}(0,1) \quad \text{quand } n \rightarrow \infty$$

**Approximation pratique** : Pour $n$ fini, $Z_n \approx \mathcal{N}(0,1)$ si :
- $np \geq 10$
- $n(1-p) \geq 10$

Ces conditions garantissent une approximation acceptable de la loi binomiale par la loi normale.

### Formulations pratiques du TCL

#### Version asymptotique (exacte)

Pour $n$ grand, la variable normalisée suit exactement une loi normale :

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \stackrel{d}{\rightarrow} \mathcal{N}(0,1)$$

#### Version approximative (pratique)

Pour $n$ suffisamment grand (typiquement $n \geq 30$), on peut approximer :

$$\bar{X}_n \stackrel{approx}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

**Important** : Cette approximation est valide pour $n$ fini mais grand. Il ne faut **jamais** appliquer $\lim_{n \rightarrow \infty}$ à cette formulation car elle deviendrait dégénérée.

> [!warning]
> Si on laisse $n$ tendre vers l'infini dans la version pratique, la variance serait $0$ mais la variance ne peut pas être $0$ par définition ! On aurait pas une vraie densité mais une mesure de Dirac.

### Relation entre LGN et TCL

Soit $\bar{X}_n$ la moyenne empirique de $n$ V.A. iid avec $\mathbb{E}[X_i] = \mu$ et $\text{Var}(X_i) = \sigma^2$.

**Loi des Grands Nombres (LGN)** :

$$\lim_{n\rightarrow\infty} P(|\bar{X}_n - \mu| \leq \epsilon) = 1, \quad \forall \epsilon > 0$$

**Théorème Central de la Limite (TCL)** :

$$\lim_{n\rightarrow\infty} \mathbb{P}\left(\left|\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma}\right| \leq a\right) = \frac{2}{\sqrt{2\pi}}\int_0^a e^{-\frac{x^2}{2}} dx$$

#### Variables aléatoires dégénérées

Quand $n \rightarrow \infty$, la variable $(\bar{X}_n - \mu)$ converge vers $0$ (LGN). Sa fonction de répartition limite est :

$$F(x) = \begin{cases}
0, & x < 0 \\
1, & x \geq 0
\end{cases}$$

Cette fonction correspond à une **variable aléatoire dégénérée** concentrée en $0$, aussi appelée mesure de Dirac $\delta_0$.

Une telle variable n'admet pas de densité au sens usuel, car toute la masse de probabilité est concentrée en un point.

#### Pourquoi la normalisation par $\sqrt{n}$ ?

La normalisation $\sqrt{n}(\bar{X}_n - \mu)$ permet d'obtenir une limite non dégénérée :

- Elle compense exactement la décroissance en $1/\sqrt{n}$ de l'écart-type de $\bar{X}_n$
- Elle garantit une variance limite égale à $\sigma^2$ (ou $1$ après division par $\sigma$)
- Elle révèle la vitesse de convergence : l'erreur $|\bar{X}_n - \mu|$ est typiquement d'ordre $O(1/\sqrt{n})$

> [!note] **Résumé des formulations**
>
> **TCL exact (asymptotique)** :
>
> $$
> \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \stackrel{d}{\rightarrow} \mathcal{N}(0,1)
>
$$
>
> **Approximation pratique** (pour $n \geq 30$) :
>
>
$$
> \bar{X}_n \stackrel{approx}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
>
$$

>
> **Attention** : Ne jamais mélanger limite asymptotique et approximation finie !
