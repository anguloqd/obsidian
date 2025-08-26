## 01 // éléments de logique (preuves)

[Slides d’éléments de logique](ressources/01_elements_de_logique_(preuves)_chap1.pdf)

## Elements de logique

### Introduction

#### Démarche hypothético-déductive

La démarche mathématique permet de **garantir qu'une affirmation soit vraie** sans avoir recours à la mesure expérimentale. Par exemple, on peut affirmer que dans le plan, la somme des angles de tout triangle est égale à 180 degrés.

Cette garantie repose sur la **rédaction d'un raisonnement** qui explicite une raison à la véracité de l'énoncé.

#### Principe fondamental

Un raisonnement établit la véracité d'une affirmation (théorème, lemme, propriété, corollaire) à partir de :

- Sa formulation en propositions plus élémentaires
- Le calcul du résultat de cette "formule"
- Des opérations sur les valeurs "vrai" et "faux"

##### Exemple : somme de deux nombres impairs

L'affirmation "la somme de 2 nombres impairs est paire" se décompose formellement en une conjonction infinie d'alternatives.

**Reformulation avec définitions :**
- Un nombre $n \in \mathbb{N}$ est pair s'il existe $k \in \mathbb{N}$ tel que $n = 2k$
- Un nombre $n \in \mathbb{N}$ est impair s'il existe $k \in \mathbb{N}$ tel que $n = 2k + 1$

L'affirmation devient : "Quel que soit $n \in \mathbb{N}$ tel qu'il existe $k \in \mathbb{N}$ tel que $n = 2k + 1$, quel que soit $n' \in \mathbb{N}$ tel qu'il existe $k' \in \mathbb{N}$ tel que $n' = 2k' + 1$, il existe $K \in \mathbb{N}$ tel que $n' + n = 2K$."

>[!example]- Démonstration
>Soient $n, n' \in \mathbb{N}$ deux nombres impairs.
>Alors par définition, il existe $k, k' \in \mathbb{N}$ tels que $n = 2k + 1$ et $n' = 2k' + 1$.
>Alors $n + n' = 2k + 1 + 2k' + 1 = 2(k + k' + 1)$.
>Je pose $K = k + k' + 1$.
>Alors $K \in \mathbb{N}$ et $n + n' = 2K$.
>Ainsi, par définition, $n + n'$ est pair.

### Calcul propositionnel

#### Définition - Proposition

Une **proposition** est une formulation dont on peut dire qu'elle est vraie ou fausse.

>[!example]+ Exemples
>- "$3 > 0$" est une proposition vraie
>- "$x > 0$" n'est pas une proposition (ne connaissant pas $x$)
>- Sachant que $x = 2$, "$x > 0$" est une proposition vraie
>- "Il existe $x \in [-1, 1]$ tel que $x > 0$" est une proposition vraie
>- "Quel que soit $x \in \mathbb{R}$, $x^2 \geq 0$" est une proposition vraie
>- "Si $x = 2$ alors $x > 0$" n'est pas une proposition (ne connaissant pas $x$)
>- "Quel que soit $x \in \mathbb{R}$, si $x = 2$ alors $x > 0$" est une proposition vraie

#### Construction de propositions

À partir de propositions dont on connaît la valeur de vérité, on peut construire d'autres propositions à l'aide de **connecteurs** (donc, et, ou, …).

La valeur de vérité de la proposition construite se calcule à partir des **tables de vérité** des connecteurs.

#### Négation

**Table de vérité du connecteur "non" :**

| P | (non P) |
|:-:|:-------:|
| V | F       |
| F | V       |

>[!important]
>**Principe de non-contradiction :** Une proposition et sa négation ne sont jamais simultanément vraies.
>
>**Principe du tiers exclu :** Une proposition est ou bien vraie ou bien fausse.

##### Définition - Contradiction

Une **contradiction** est une proposition $P$ telle que $P$ est vraie et $(non~P)$ est vraie. Une contradiction n'existe pas.

>[!example]- Exemple d'utilisation du tiers exclu
>**Théorème :** Il existe des irrationnels $a$ et $b$ tels que $a^b$ est rationnel.
>
>**Démonstration :**
>Considérons la proposition $P$ : $\sqrt{2}^{\sqrt{2}} \in \mathbb{Q}$.
>D'après le tiers exclu, ou bien $P$ est vraie, ou bien $(non~P)$ est vraie.
>
>- Si $P$ est vraie, et sachant que $\sqrt{2}$ est irrationnel, le résultat $a^b \in \mathbb{Q}$ est obtenu avec $a = b = \sqrt{2}$.
>- Si $(non~P)$ est vraie, alors $\sqrt{2}^{\sqrt{2}}$ est irrationnel.
>  Dans ce cas, en posant $a = \sqrt{2}^{\sqrt{2}}$ et $b = \sqrt{2}$, on obtient :
>
>  $$
>  a^b = (\sqrt{2}^{\sqrt{2}})^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \times \sqrt{2}} = \sqrt{2}^2 = 2 \in \mathbb{Q}
>
>
$$
#### Disjonction

**Table de vérité du connecteur "ou" :**

| P | Q | (P ou Q) |
|:-:|:-:|:--------:|
| V | V | V        |
| V | F | V        |
| F | V | V        |
| F | F | F        |

#### Conjonction

**Table de vérité du connecteur "et" :**

| P | Q | (P et Q) |
|:-:|:-:|:--------:|
| V | V | V        |
| V | F | F        |
| F | V | F        |
| F | F | F        |

>[!exercise] Exercice fondamental
>Vérifier que les propositions $(P \text{ et } Q)$ et $(\text{non}((\text{non }P) \text{ ou } (\text{non }Q)))$ ont même table de vérité.
>
>**Conséquence :** La négation de $(P \text{ et } Q)$ est $((\text{non }P) \text{ ou } (\text{non }Q))$.

#### Implication

**Table de vérité du connecteur "$\Rightarrow$" :**

| P | Q | (P $\Rightarrow$ Q) |
|:-:|:-:|:-------------------:|
| V | V | V                   |
| V | F | F                   |
| F | V | V                   |
| F | F | V                   |

##### Formulations équivalentes de $(P \Rightarrow Q)$

- $P$ implique $Q$
- Si $P$ est vraie, alors $Q$ est vraie
- Pour que $P$ soit vraie, il faut que $Q$ soit vraie
- $Q$ est une **condition nécessaire** de $P$
- Pour que $Q$ soit vraie, il suffit que $P$ soit vraie
- $P$ est une **condition suffisante** de $Q$

>[!exercise]
>Vérifier que $(P \Rightarrow Q)$ et $((\text{non }P) \text{ ou } Q)$ ont même table de vérité.

#### Réciproque

La proposition $(Q \Rightarrow P)$ est appelée **réciproque** de $(P \Rightarrow Q)$.

>[!warning]
>Les propositions $(P \Rightarrow Q)$ et $(Q \Rightarrow P)$ peuvent avoir des valeurs différentes.
>
>**Exemple :** Si $P$ est fausse et $Q$ est vraie, alors $(P \Rightarrow Q)$ est vraie, tandis que $(Q \Rightarrow P)$ est fausse.

#### Contraposée

La proposition $((\text{non }Q) \Rightarrow (\text{non }P))$ est appelée **contraposée** de $(P \Rightarrow Q)$.

**Propriété fondamentale :** Une implication $(P \Rightarrow Q)$ et sa contraposée $((\text{non }Q) \Rightarrow (\text{non }P))$ ont toujours même valeur.

>[!example]- Démonstration par table de vérité
>
>| P | Q | $(P \Rightarrow Q)$ | non P | non Q | $((non~Q) \Rightarrow (non~P))$ |
>|:-:|:-:|:-------------------:|:-----:|:-----:|:-------------------------------:|
>| V | V | V                   | F     | F     | V                                |
>| V | F | F                   | F     | V     | F                                |
>| F | V | V                   | V     | F     | V                                |
>| F | F | V                   | V     | V     | V                                |

**Conséquence pratique :** Pour montrer qu'une implication est vraie, il est possible de montrer que sa contraposée l'est.

#### Équivalence

**Table de vérité du connecteur "$\Leftrightarrow$" :**

| P | Q | $(P \Leftrightarrow Q)$ |
|:-:|:-:|:-----------------------:|
| V | V | V                       |
| V | F | F                       |
| F | V | F                       |
| F | F | V                       |

##### Formulations équivalentes de $(P \Leftrightarrow Q)$

- $P$ est équivalente à $Q$
- $P$ est vraie si et seulement si $Q$ est vraie
- Pour que $P$ soit vraie, il faut et il suffit que $Q$ soit vraie
- $P$ est une **condition nécessaire et suffisante** de $Q$

>[!exercise]
>Justifier que $(P \Leftrightarrow Q)$ et $((P \Rightarrow Q) \text{ et } (Q \Rightarrow P))$ ont même table de vérité.

#### Propriétés des connecteurs logiques

**Équivalences fondamentales :**

| Proposition 1 | Proposition 2 |
|:--------------|:--------------|
| $(\text{non}(\text{non}~P))$ | $P$ |
| $(P \text{ ou } Q)$ | $(Q \text{ ou } P)$ |
| $(P \text{ et } Q)$ | $(Q \text{ et } P)$ |
| $((P \text{ ou } Q) \text{ ou } R)$ | $(P \text{ ou } (Q \text{ ou } R))$ |
| $((P \text{ et } Q) \text{ et } R)$ | $(P \text{ et } (Q \text{ et } R))$ |
| $(P \text{ et } (Q \text{ ou } R))$ | $((P \text{ et } Q) \text{ ou } (P \text{ et } R))$ |
| $(P \text{ ou } (Q \text{ et } R))$ | $((P \text{ ou } Q) \text{ et } (P \text{ ou } R))$ |
| $(\text{non}(P \text{ ou } Q))$ | $((\text{non}~P) \text{ et } (\text{non}~Q))$ |
| $(\text{non}(P \text{ et } Q))$ | $((\text{non}~P) \text{ ou } (\text{non}~Q))$ |

>[!tip]
>Dans un raisonnement, on peut remplacer la proposition 1 par la proposition 2 et réciproquement.

### Prédicats et quantificateurs

#### Motivation

De nombreuses propositions prennent la forme :

- De résultats d'existence : "Pour tout $x \in [0, +\infty[$, il existe un unique $y \in [0, +\infty[$ tel que $y^2 = x$"
- De propriétés universelles : "Pour tout triangle ABC rectangle en A, $AB^2 + AC^2 = BC^2$"

Les expressions "Pour tout […]" et "Il existe […]" sont centrales dans l'argumentation mathématique.

#### Définition - Prédicat

Un **prédicat** $P(x, y, …)$ est une formulation qui peut être vraie ou fausse selon les valeurs des variables $x, y, …$ fixées à l'extérieur de l'expression du prédicat.

>[!example]+ Exemples
>- "$x > 2$" est un prédicat. Il est vrai pour tout $x > 2$, et faux sinon.
>- "Il existe $x \in \mathbb{R}$ tel que $x \times a = 1$" est un prédicat. Il est vrai lorsque $a \neq 0$, et faux lorsque $a = 0$. Noter que la valeur de vérité ne dépend pas de $x$, qui est une **variable muette**.
>- "Pour tout $x \in \mathbb{R}$, $x^2 \geq 0$" n'est pas un prédicat. C'est une proposition vraie, où $x$ est une variable muette.

#### Quantificateur universel

##### Définition

Soit $P(x)$ un prédicat dépendant de $x$. Soit $E$ un ensemble. La proposition $(\forall x \in E, P(x))$ :

- est **vraie** lorsque $P(x)$ est vraie pour tous les éléments $x$ de $E$
- est **fausse** lorsque $P(x)$ est fausse pour au moins un élément $x$ de $E$

**Lecture :** "Pour tout $x \in E$, $P(x)$" ou "Quel que soit $x \in E$, $P(x)$"

**Notation :** Le symbole $\forall$ s'appelle le **quantificateur universel**.

##### Interprétation logique

La proposition $\forall x \in E, P(x)$ est la **conjonction** de l'ensemble des propositions $P(e)$ lorsque $e$ parcourt l'ensemble $E$.

Si $E$ est un ensemble fini avec éléments $e_1, e_2, e_3, …$, alors :
$$
\forall x \in E, P(x) \equiv P(e_1) \text{ et } P(e_2) \text{ et } P(e_3) \text{ et } ...
$$
#### Quantificateur existentiel

##### Définition

Soit $P(x)$ un prédicat dépendant de $x$. Soit $E$ un ensemble. La proposition $(\exists x \in E, P(x))$ :

- est **vraie** lorsque $P(x)$ est vraie pour au moins un élément $x$ de $E$
- est **fausse** lorsque $P(x)$ est fausse pour tous les éléments $x$ de $E$

**Lecture :** "Il existe $x \in E$, $P(x)$"

**Notation :** Le symbole $\exists$ s'appelle le **quantificateur existentiel**.

##### Interprétation logique

La proposition $\exists x \in E, P(x)$ est la **disjonction** de l'ensemble des propositions $P(e)$ lorsque $e$ parcourt l'ensemble $E$.

Si $E$ est un ensemble fini avec éléments $e_1, e_2, e_3, …$, alors :
$$
\exists x \in E, P(x) \equiv P(e_1) \text{ ou } P(e_2) \text{ ou } P(e_3) \text{ ou } ...
$$
>[!example]+ Exemples d'application
>- $(\forall x \in \mathbb{R}, x^2 \geq 0)$ est une proposition vraie
>- $(\exists x \in \mathbb{R}, x^2 > 0)$ est une proposition vraie
>- $(\forall x \in \mathbb{R}, x^2 > x)$ est une proposition fausse
>
>Pour la dernière : il existe $x \in \mathbb{R}$ tel que $x^2 \leq x$, par exemple $x = 1$ ou $x = \frac{1}{2}$.

#### Négation des quantificateurs

##### Propriété 1

**La négation de $(\forall x \in E, P(x))$ est $(\exists x \in E, (\text{non}~P(x)))$.**

>[!example]- Démonstration
>Rappelons :
>- $(\forall x \in E, P(x))$ est vraie lorsque $P(x)$ est vraie pour tous les éléments $x$ de $E$
>- $(\forall x \in E, P(x))$ est fausse lorsque $P(x)$ est fausse pour au moins un élément $x$ de $E$
>
>Par négation :
>- $(\text{non}(\forall x \in E, P(x)))$ est fausse lorsque $P(x)$ est vraie pour tous les éléments $x$ de $E$
>- $(\text{non}(\forall x \in E, P(x)))$ est vraie lorsque $P(x)$ est fausse pour au moins un élément $x$ de $E$
>
>Autrement dit :
>- $(\text{non}(\forall x \in E, P(x)))$ est fausse lorsque $(\text{non}~P(x))$ est fausse pour tous les éléments $x$ de $E$
>- $(\text{non}(\forall x \in E, P(x)))$ est vraie lorsque $(\text{non}~P(x))$ est vraie pour au moins un élément $x$ de $E$
>
>Ce qui correspond exactement à : $(\exists x \in E, (\text{non}~P(x)))$.

##### Propriété 2

**La négation de $(\exists x \in E, P(x))$ est $(\forall x \in E, (\text{non}~P(x)))$.**

>[!example]- Démonstration
>La propriété précédente, appliquée à $(\text{non}~P)$ au lieu de $P$, dit :
>"la négation de $(\forall x \in E, (\text{non}~P(x)))$ est $(\exists x \in E, P(x))$."
>
>Par double négation, j'obtiens :
>"la proposition $(\forall x \in E, (\text{non}~P(x)))$ est la négation de $(\exists x \in E, P(x))$."

### Exemples de raisonnements

#### Raisonnement général

>[!example]- Exemple
>**Théorème :** $\forall x \in \mathbb{R}, \exists y \in \mathbb{R}, y > x$.
>
>**Méthode :**
>- Pour montrer une proposition de la forme $(\forall x \in E, P(x))$, on commence par : "Soit $x \in E$. Alors […]"
>- Pour montrer une proposition de la forme $(\exists x \in E, P(x))$, on utilise ses connaissances ou on exhibe un exemple $x = …$ tel que $P(x)$ soit vraie. Dans ce cas, on écrit : "Je pose $x = …$. [calculs]… Donc $P(x)$."
>
>**Démonstration :**
>Soit $x \in \mathbb{R}$.
>Je pose $y = x + 1$.
>De $1 > 0$, je déduis, en ajoutant $x$ : $x + 1 > x + 0$.
>Ainsi $y > x$.

#### Raisonnement par l'absurde

>[!example]- Exemple
>**Théorème :** $\forall x \in \mathbb{R} \setminus \{1\}, \frac{2x+2}{x-1} \neq 2$.
>
>**Méthode :** Pour montrer une propriété par l'absurde, je suppose que sa négation est vraie, et j'en déduis une contradiction.
>
>**Démonstration :**
>Je suppose, par l'absurde, qu'il existe $x \in \mathbb{R} \setminus \{1\}$ tel que $\frac{2x+2}{x-1} = 2$.
>Alors, en multipliant par $x - 1$ (non nul), j'obtiens :
>
>
$$
>2x + 2 = 2(x - 1)
>
>
$$
>J'en déduis $2x + 2 = 2x - 2$, et donc $2 = -2$.
>Or $2 \neq -2$. Contradiction.

#### Disjonction de cas

>[!example]- Exemple
>**Théorème :** $\forall x \in \mathbb{R}, |x| \geq x$.
>
>**Méthode :** Je décompose la proposition à montrer en plusieurs cas, et je montre chacun des cas.
>
>**Démonstration :**
>Soit $x \in \mathbb{R}$.
>Alors $x \geq 0$ ou $x < 0$.
>
>**Cas 1 :** Je suppose $x \geq 0$. Je sais que dans ce cas $|x| = x$.
>Or $x \geq x$, donc $|x| \geq x$.
>
>**Cas 2 :** Je suppose $x < 0$. Je sais que quel que soit $x \in \mathbb{R}$, $|x| \geq 0$.
>Ainsi $|x| \geq 0 > x$. Donc $|x| > x$, et donc $|x| \geq x$.

#### Raisonnement par contraposée

>[!example]- Exemple
>**Théorème :** $\forall n \in \mathbb{N}$, si $n^2$ est pair, alors $n$ est pair.
>
>**Méthode :** On raisonne par contraposée lorsqu'on montre $(\text{non}~Q) \Rightarrow (\text{non}~P)$ au lieu de $(P \Rightarrow Q)$.
>
>**Démonstration :**
>Soit $n \in \mathbb{N}$.
>Je suppose que $n$ est impair.
>Alors il existe $k \in \mathbb{N}$ tel que $n = 2k + 1$.
>Alors :
>
>
$$
>n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 = 2K + 1
>
>
$$

>avec $K = 2k^2 + 2k \in \mathbb{N}$.
>Donc $n^2$ est impair.
>Par contraposée, si $n^2$ est pair, alors $n$ est pair.
