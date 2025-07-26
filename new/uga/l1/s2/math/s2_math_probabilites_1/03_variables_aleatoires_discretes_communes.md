# 03 // variables aléatoires discrètes communes

Date de création: May 6, 2022 7:49 PM
Modifié: November 8, 2023 10:46 PM

# Paramètres descriptifs d’une distribution discrète

## Mode

C'est tout simplement la valeur la plus fréquente dans la population.

Pour définir une mode dans une population, il faut vérifier quelques conditions :

- La population est non-vide.
- La population doit avoir au moins une valeur différente des autres.
Ceci implique qu’une population de la forme $\{x,x,\dots,x\}$ n’a pas de mode, même si la valeur $x$ se repète.

**Note pratique**. Il est possible d'avoir plus d'une mode si elles ont la même fréquence.

## Espérance : $\mathbb E[X]$

### Définition

Mathématiquement, c’est la moyenne pondérée des résultats de la V.A $X$. Intuitivement, c'est la moyenne des résultats qu'on observerait si on pouvait répéter l’expérience une infinité de fois. Elle seulement existe si la série $\sum (x \cdot \mathbb P(X=x)$ est absolument convergente, sinon on dit que $X$ ne possède pas une espérance.

$$
\mathbb{E}(X) = \sum_{x \in \Omega_X} (x\cdot \mathbb P(X=x))
$$

### Propriétés

**Linéarité de l’espérance**. L’espérance de la somme est la somme des espérances, même si elles sont dépendantes.

$$
\mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y]
\newline
\mathbb{E}[\alpha X] = \alpha \mathbb{E}[X]  
$$

**Produit des espérances**. Si deux V.A. sont **forcément indépendantes**  $\implies$ l’espérance du produit égal le produit des espérances. **Réciproque fausse**.

$$
\mathbb{E}[XY] =\mathbb{E}[X]\mathbb{E}[Y] 
$$

**Espérance d’une V.A. fonction d’autre V.A**. Supposons une fonction réelle $f(x)$ et une VA définie sur une VA comme $Y=f(X)$. Donc, si la série $\sum(f(X) \cdot \mathbb P(X=x))$ est absolument convergente, donc on peut parler de l’espérance de $f(X)$ (ou de $Y$ aussi).

$$
\mathbb{E}[\overbrace{f(X)}^Y] = \sum_{x\in\Omega_X} (\overbrace{f(X)}^Y\cdot \mathbb P(X=x) )
$$

## Variance et écart-type : $\text{Var}(X)\text{ et }\sigma$

### Définition de variance et théorèmes

Un moment est une notion sortie de la physique. Si $n \in \N$ et $X$ est une V.A. avec espérance finie, donc $\mathbb{E}[X^n]$ est le moment d’ordre $n$ de $X$. Encore plus, $\mathbb{E}[(X-\mathbb{E}[X])^n]$ est le moment *centré* d’ordre $n$ de $X$. “Centré” veut dire centré autour de la moyenne, car à chaque valeur de $X$ on soustrait la moyenne, donc l’ensemble qui en ressort a comme nouveau centre $0$.

La variance est le moment d’ordre $2$ de $X$, c’est-à,dire, la valeur espérée du carré de la somme des écarts de chaque observation par rapport à la moyenne. Intuitivement, elle est simplement une mesure de dispersion de la moyenne, exprimée en unités carrées. **La variance est toujours positive !**

$$
\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}[X])^2] =\sum_{x\in\Omega_X}( (x-\mathbb{E}[X])^2\cdot \mathbb P(X=x))
$$

- **Théorème de König-Huygens**. $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$
Cette relation rend plus confortable le calcul de la variance.
- **Inégalité de Cauchy-Schwarz**. $|\mathbb{E}(XY)| \le \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}$

### L’écart type

La racine carré de la variance est connue comme l’écart-type, noté comme $\sigma = \sqrt{\text{Var}(X)}$. Elle est exprimé en unités de la V.A., tant que la variance est en unités carrées.

# Variables discrètes les plus communes

## Loi discrète uniforme : $U(a,b)$

<aside>
⛑️ Aide : la somme des entiers dans l’intervalle $[a,b]$ inclus est $\frac{n(a+b)}{2}$, où $n=(b-a+1)$ est la quantité d’entiers dans l’intervalle.

</aside>

$$
X\sim U(a,b)\iff\mathbb P(X=x)=\frac{1}{\underbrace{(b-a+1)}_n},\hspace{4pt}\forall x\in[a,b]
$$

C'est une distribution telle que toutes les valeurs possibles de $X$ ont la même probabilité d'être observées.

- **Espérance** : $\mathbb E[X] = \frac{a+b}{2}$.
- **Espérance de $X^2$**: $\mathbb E[X^2]=(b-a+1)(\frac{a+b}{2})^2=(b-a+1)\mathbb E[X]^2$
- **Variance** : $\text{Var}(X)=(b-a)(\frac{a+b}{2})^2=(b-a)\mathbb E[X]^2$
- **Mode** : la mode est égale à chaque élément.

## Loi de Bernoulli ou variable indicatrice : $\text{Bernoulli}(p)$

$$
X\sim\text{Bernoulli}(p) \iff \mathbb P (X=x) =
\begin{cases}
1,\text{ prob. } p \\
0,\text{ prob. } (1-p)
\end{cases}
$$

C'est une variable aléatoire $X$ que seulement prend deux valeurs : $0$ et $1$. Elle prend $1$ si le résultat de l’expérience est considéré un " succès ", et $0$ si on considère le résultat comme " échec ".

- **Espérance** : $\mathbb E[X] = p$.
- **Espérance de $X^2$** : $\mathbb E[X^2]=p$.
- **Variance** : $\text{Var}(X) = p(1-p)$.
- **Mode** : $M=
\begin{cases}
1,\text{ si }p>\frac{1}{2}\\
0,\text{ si }p<\frac{1}{2}\\

\end{cases}$. Elle n’est pas définie si $p=\frac{1}{2}$.

## Loi binomiale : $\mathcal B(n,p)$

$$
X\sim\mathcal B(n,p) \iff \mathbb P(X=k)=C^k_np^k(1-p)^{n-k}
$$

C'est la probabilité, avec remise, dans une suite de $n$ essais de Bernoulli identiques et indépendantes (iid.), d'avoir $k$ succès et $(n-k)$ échecs.

- **Espérance** : $\mathbb E[X]=np$.
- **Variance** : $\text{Var}(X) = np(1-p)$.
- Notons aussi que $\mathcal{B}(1,p)=\text{Bernoulli}(p)$

## Loi géométrique : $\text{Geo}(p)$

$$
X\sim\text{Geo}(p)\iff\mathbb P(X=k)=(1-p)^{k-1}p
$$

C'est la probabilité, dans une suite de $k$ expériences, d'observer en premier lieu $k-1$ échecs, puis le premier succès. À différence de la loi binomiale, notons qu'on ne multiplie pas par $C^k_n$. Donc, l'ordre ici est important, le succès doit être le dernier résultat.

- **Espérance** : $\mathbb E[X] = \frac{1}{p}$.
- **Variance** : $\text{Var}(X)=\frac{(1-p)}{p^2}$.

## Loi de Poisson : $\text{Poisson}(\lambda)\text{ ou }\mathcal P(\lambda)$

C’est la probabilité d’observer une quantité k de événements dans une unité de temps de référence. Le paramètre $\lambda$ représente la quantité moyenne d’événements dans une unité de temps.

$$
X\sim\text{Poisson}(\lambda) \iff \mathbb P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}, \text{ où } \lambda\in[0,\infin) \text{ et } k\in\N
$$

- **Espérance** : $E[X]=λ$
- **Variance** : $E[X]=λ$
- **Mode** : $M=n$, où $n \in [λ-1, λ]$
Basiquement, l’entier ou les deux entiers dans l’intervalle inclus.
- Identité utile pour des calculs par récurrence :
    
    $$
    \mathbb P(X=k+1)=\mathbb P(X=k)\frac{\lambda}{k+1}
    $$
    

**Extra**. Un calcul intéressant est la somme de des probabilités de chaque résultat possible, c’est-à-dire de chaque $k$ possible :

$$
\begin{align*}\mathbb P(X=0)+\mathbb P(X=1)+\mathbb P(X=2)+\dots &= \sum_{k=0}^\infin\mathbb P(X=k)
\\[11pt] &=\sum_{k=0}^\infin e^{-\lambda}\frac{\lambda^k}{k!}
\\[11pt] &= e^{-\lambda}\sum_{k=0}^\infin\frac{\lambda^k}{k!}
\\[14pt] &=e^{-\lambda}(e^\lambda)
\\[5pt] &= 1
\end{align*}
$$

Trivial : si on somme toute les possibilités, c'est sûr qu'on arrive à $1$. **Ce qui est intéressant ce que il apparaît l'expansion de Taylor de $e^x$ dans $\sum_{k=0}^\infin\frac{\lambda^k}{k!}$, si on suppose que $x=\lambda$**.

### Approximation d’une loi binomiale avec la loi de Poisson

On peut approximer une loi binomiale avec une loi de Poisson si et seulement si :

- $n$ est très grand : $n \ge 30$ (ou $n\ge 100$ pour le matériel du cours),
- $p$ est très petit : $p \le 0.1$, et
- $np \le 15$

Dans ce cas, on pose $λ = np$ et on a finalement ce qui suit :

$$
\mathcal B(n,p) \approx \text{Poisson}(np), \text{ ou } \mathbb P(X_\mathcal{B}=k)\approx\mathbb P(X_\mathcal{P}=k)=e^{-np}\frac{(np)^k}{k!}
$$

## Loi hypergéométrique : $\text{Hypergeo}(N,K,n)$

$$
X\sim\text{Hypergeo}(N,K,n) \iff \mathbb P(X=k)=\frac{C^k_KC^{n-k}_{N-K}}{C^n_N}
$$

C'est la probabilité, sans remise, de tirer $k$ succès (de $K$ possibles) et $(n-k)$ échecs (de $(N-K)$ possibles) d'un échantillon de taille $n$ d'une population de taille $N$.

En d'autres termes, c'est la probabilité, sans remise, dans une suite de $n$ expériences, d'observer $k$ succès (de $K$ possibles succès dans $N$) et $(n-k)$ échecs (de $(N-K)$ possibles dans $N$). Un tel schéma est utilisé dans les sondages.

Particulièrement, les paramètres sont la taille de la population $N$, la taille de l’échantillon $n$ et les états de succès possibles $K$. La variable indépendante $k$ est la quantité d’états de succès dans l’échantillon (observés).

- **Espérance** : $\mathbb E[X]=\frac{kn}{N}$
- **Variance** : $\text{Var}(X)=n \cdot \frac{k}{N} \cdot \frac{N-k}{N} \cdot \frac{(N-n)}{N-1}$

### Quelques notes à faire

- Chaque échantillon possible peut être classifié comme succès/échec (ou deux catégories mutuellement exclusives)
- La probabilité de succès change avec chaque sélection, car chaque sélection réduit la population dont on sélectionne.
- **Conséquence** : si $X$ suit une loi hypergéométrique, **$X$ n'est pas une iid. (indépendante et identique)**.

### Exemple

Il y a $10$ boules : $4$ rouges et $6$ bleues. Je fixe la taille des échantillons de boules à $6$. Quelle est la probabilité que tel échantillon contiennent $2$ boules rouges et $4$ bleues ?

- [(Manières de prendre $2$ boules rouges des $4$ totales) * (Manières de prendre $4$ boules bleues des $6$ totales)]/(Manières de prendre $6$ boules quelles conques de $10$ totales).

### Approximer une hypergéométrique avec une binomiale

Si $N\longrightarrow\infin$ et $\lim_{N\rightarrow\infin} \frac K N = p$, on peut donc établir l’approximation qui suit :

$$
\lim_{N\rightarrow\infin}\frac{C^k_KC^{n-k}_{N-K}}{C^n_N}=C^k_np^k(1-p)^{n-k}
$$