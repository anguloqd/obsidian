## 01 // mini-cours sur les séries

## Définition et notation

### Une suite *accrochée* à une autre suite

Une série est une **suite**. C’est une suite accrochée a une autre suite de base.

Particulièrement, est la somme partielle des premiers $n$ termes de la suite de base $(u_n)$.

Par rapport à la notation, et pour éviter de confusions :

- La ***série*** d’une suite $(u_n)$ est notée comme $\Sigma u_n$.
- La ***somme partielle*** des $n$ premiers termes de $(u_n)$ est noté $\Sigma_{k=0}^n u_k$. C’est un nombre réel et un terme de la suite $\Sigma u_n$.
- La ***limite*** de la série est $\Sigma_{k=0}^{\infty} u_n  := \lim_{n \rightarrow \infty} \Sigma_{k=0}^n u_n$. C’est un nombre réel.

## Suites, fonctions et quelques limites

### Dériver une suite à partir d’une fonction $f$ sur $\mathbb{R}$

Il est possible d’extraire une suite d’une fonction définie sur les réels. À partir de là, la limite de la fonction serait aussi la limite de la suite.

$$
\lim(u_n) = u, u\in\mathbb{R}; \text{ et } f \text{ continue en } u,
\\[0.1in] \text{donc } \lim f(u_n) = f(u)
$$

### Limites de séries notables

Par rapport à quelques limites :

1. La fonction exponentielle domine la potentiel ou polynomiale, en croissance et décroissance.

    $$
    \lim_{x \rightarrow \infty} \frac{a^x}{x^m} \rightarrow \infty\text{, avec } a>1 \text{ et } m>0;
    \\[0.1in]
    \text{et } \lim_{x \rightarrow \infty} a^xx^m=0, \text{ avec } 0 < a < 1\text{ et } m>0.

$$

    
2. Analogiquement, la fonction logarithmique est dominée par les polynômes, en croissance et décroissance.
    
    $$
    \lim_{x \rightarrow \infty} \frac{x^m}{\ln{x}} \rightarrow \infty\text{, avec } m>0;
    \\[0.1in]
    \text{et } \lim_{x \rightarrow \infty} x^m\ln{x}=0, \text{ avec } m<0.
    
$$

Autres séries importantes :  série géométrique, série exponentielle (expansion de Taylor de $e^x$), série harmonique alternante (converge à $\ln2$).

## Convergence et opérations de séries

### La convergence comme le terme limite de la suite : $“u_\infty”$

Si la suite des sommes partielles $\Sigma u_n$ converge, donc la limite existe. Il se peut que la limite n’existe pas, et donc elle ne converge pas !

**Condition nécessaire de convergence d’une série**. Si $\Sigma u_n$ converge $\implies$ $u_n \rightarrow 0$. Réciproque fausse.

### Opérations entre séries et propriétés

Avant de rentrer sur les sommes des séries, il est à note que la série d’une suite peut être vu comme un opérateur linéaire :

$$
\sum_{n=0}^\infty(u_n + v_n) = \sum_{n=0}^\infty(u_n) + \sum_{n=0}^\infty(v_n)
\hspace{8pt}\text{ et }\hspace{8pt}\sum_{n=0}^\infty (\alpha u_n) = \alpha \sum_{n=0}^\infty (u_n)
$$

- L’addition de séries $\sum(u_n)$ et $\sum(v_n)$…
    - Converge si les deux convergent.
    - Diverge si l’une converge et l’autre diverge.
    - Inconclusif si les deux divergent. Peut-être l’un ou l’autre.
- On ne modifie pas la nature convergente ou divergente d’une série modifiant une nombre **fini** de termes, mais on modifie sa limite !

## Séries à termes positifs

### Des séries pratiques pour travailler avec

Une série $\Sigma u_n$ est à termes positifs si pour tout $n ≥ 0$, $u_n ≥ 0$. Donc,

- La suite $\Sigma u_n$ est forcément croissante (pas confondre avec la suite de base $(u_n)$ !)
- La série $\Sigma u_n$ converge $\iff$ la suite de base $(u_n)$ est majorée.

> [!note]
> La chose qui tombe bien des séries à termes positifs, c’est que pour montre qu’elle converge, on doit seulement démontrer qu’elle est majoré.
> Soit elle et majoré et converge, ou soit elle diverge vers l’infini. **Évidemment, une série à termes positifs est toujours croissante**.

### Règle de d’Alembert et Critère de d’Alembert

#### Règle de d’Alembert

Soit $\Sigma u_n$ une série à termes réels ou complexes. Supposons que $k \in [0, 1[$ et $N \in \mathbb{N}$ tel que si $n ≥ N, |u_{n+1}| ≤ k|u_n|$. Alors la série $\Sigma u_n$ converge.

#### Critère de d’Alembert

C’est un corollaire de la règle d’Alembert. Soit $\Sigma u_n$ à termes strictement positifs et supposons qu’il existe $\ell$ tel que $\lim_{n\rightarrow \infty} |\frac{u_{n+1}}{u_n}| = \ell$

.

- si $\ell < 1$$\implies$ $\Sigma u_n$ converge.
- si $\ell >1 \implies \Sigma u_n$ ne converge pas.
- si $\ell = 1$, elle peut converger ou diverger. On ne peut rien conclure.
**De même si la limite n’existe pas !**

Il est à noter que c’est plus facile d’utiliser d’Alembert avec des séries à termes positifs.

**Note pratique.** On peut écrire le quotient $\frac{u_{n+1}}{u_n}$ comme $|\frac{u_{n+1}}{u_n}|$, et si ce dernier converge, le premier converge aussi.

Après, encore si $(u_n)$ série a termes positifs, et supposant que $\Sigma u_n$ converge, on peut sommer $\Sigma u_n$ dans n’importe quel ordre. On ne change pas ni la nature ni la somme de $\Sigma u_n$. (on peut appliquer les propriétés commutative, associative et distributive !)

### Domination et théorème de comparaison

**Domination**. Une série $\Sigma v_n$ domine une autre $\Sigma u_n$ si, à partir d’un certain rang $N$, il existe $n ≥ N$ tel que $u_n ≤ v_n$.
Supposons les deux sont à termes positifs.

**Théorème de comparaison** :

- si $\Sigma v_n$ domine $\Sigma u_n$ et $\Sigma v_n$ converge $\implies$ $\Sigma u_n$ converge aussi. Réciproque fausse.
- si $\Sigma v_n$ domine $\Sigma u_n$ et $\Sigma u_n$ diverge $\implies$ $\Sigma v_n$ diverge aussi. Réciproque fausse.
- Corollaire : si $\lim_{n→\infty} \frac{u_n}{v_n}$ = $\ell,\text{ } \ell \in \mathbb{R}$, donc $\Sigma u_n$ et $\Sigma v_n$ sont de même nature (conv./div.).
- Corollaire : si on a deux séries $(u_n)$ et $(v_n)$, si le quotient $\lim_{n \rightarrow \infty} \frac{u_n}{v_n} = 1$, on dit que le séries sont *équivalentes.*
On note $u_n \sim_{n\rightarrow \infty} v_n$.

## D’autres séries notables

### Séries de Riemann

Les séries de Riemann sont les séries de la forme $\Sigma \frac{1}{n^p}$, avec $p \in \mathbb{R}$.

- Si $\Sigma \frac{1}{n^p}$ converge $\iff p > 1$.

### Séries absolument convergentes

Une série $\Sigma u_n$ est absolument convergente si $\Sigma |u_n|$ converge. Notons que, évidemment, $\Sigma |u_n|$ est une série à termes positifs, on peut donc utiliser les outils qu’on connaît des séries à termes positifs.

- Si une série $\Sigma u_n$ converge absolument $\implies \Sigma u_n$ converge “normalement”. Réciproque fausse.
    - Les séries qui convergent mais divergent absolument sont appelés séries *semi-convergentes*.
- La somme de deux séries absolument convergentes est aussi absolument convergente.
