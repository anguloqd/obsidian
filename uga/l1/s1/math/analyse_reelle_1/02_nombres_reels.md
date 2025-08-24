## 02 // les nombres réels (propriétés et partie entière)

[02_les_nombres_reels_(proprietes_et_partie_enti_chap2.pdf](ressources/02_les_nombres_reels_(proprietes_et_partie_enti_chap2.pdf)

## Les nombres réels

### Bornes inférieures et supérieures

#### Maximum et majorant (resp. minimum et minorant)

On dit que $a \in E$ majore $b \in E$ si $a \geq b$. En plus, si $a$ majore tout $b \in E$, alors $a$ est un **maximum** de $E$ (ou plus grand élément de $E$). Dans ce cas, il est unique, noté $\max E$.

Soit $A \subset E$ une partie de $E$. On dit que $M \in E$ est un **majorant** de $A$ s'il majore tous les éléments de $A$. Dans ce cas, on dit que $A$ est majoré par $M$.

On définit de même la minoration, le minimum (noté $\min E$) et le minorant.

#### Bornes

Une partie $A \subset E$ admettant un minorant et un majorant est dite **bornée**.

- On dit que $A$ admet une borne supérieure s'il est majoré et possède un **majorant plus petit** que tous les autres. Dans ce cas, on note $\sup A$ la borne supérieure de $A$.
- On dit que $A$ admet une borne inférieure s'il est minoré et possède un **minorant plus grand** que tous les autres. Dans ce cas, on note $\inf A$ la borne inférieure de $A$.

### Le corps des nombres réels

#### Propriété de la borne supérieure

On dit qu'un ensemble de nombres $E$ satisfait la propriété de la borne supérieure si toute partie $A \subset E$ non vide et majorée admet une borne supérieure dans $E$. L'ensemble des réels comble cette lacune de $\mathbb{Q}$.

#### Axiomes des nombres réels

On dit qu'un ensemble $E$ muni d'opérations $+$, $\times$ et de la relation d'ordre $\leq$ vérifie les axiomes des nombres réels si :

- $E$ muni de $+$, $\times$ et $\leq$ est un corps totalement ordonné,
- $E$ satisfait la propriété de la borne supérieure.

Il existe un ensemble vérifiant les axiomes des nombres réels. Cet ensemble est noté $\mathbb{R}$ et appelé corps des réels.

### Propriétés de $\mathbb{R}$

#### Borne supérieure et inférieure

Par définition, $\mathbb{R}$ possède la propriété de la borne supérieure (toute partie non vide majorée possède une borne supérieure). $x$ est la borne supérieure de $A$, une partie non-vide de $\mathbb{R}$, si :

- $\forall a \in A, a \leq x$
- $\forall \varepsilon > 0, \exists a \in A : a > x-\varepsilon$

Par passage à l'opposé, il possède aussi la "propriété de la borne inférieure" (toute partie non vide minorée possède une borne inférieure). $x$ est la borne inférieure de $A$, une partie non-vide de $\mathbb{R}$, si :

- $\forall a \in A, x \leq a$
- $\forall \varepsilon > 0, \exists a \in A, a < x + \varepsilon$

#### Autres propriétés

>[!theorem] Propriété des segments emboîtés
>Soit, pour tout $n \in \mathbb{N}$, $S_n = \{x \in \mathbb{R} : a_n \leq x \leq b_n\}$, avec
>$a_n, b_n \in \mathbb{R}$ vérifiant $a_n \leq a_{n+1} \leq b_{n+1} \leq b_n$.
>Alors $\displaystyle\bigcap_{n\in\mathbb{N}} S_n \neq \emptyset$.

>[!theorem] Propriété d'Archimède
>Pour tout $x, y \in \mathbb{R}$ avec $y > 0$, il existe $n \in \mathbb{N}$ tel que $n \cdot y > x$.

>[!theorem] Propriété de l'existence d'une partie entière
>Pour tout $x \in \mathbb{R}$, il existe un unique entier $n \in \mathbb{Z}$ tel que $n \leq x < n + 1$.
>Cet entier $n$ s'appelle la partie entière de $x$, notée $E(x)$ ou $\lfloor x\rfloor$.
