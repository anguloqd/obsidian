# 02 // les nombres réels (propriétés et partie entière)

[Slides des nombres réels](ressources/02_les_nombres_reels_(proprietes_et_partie_enti_chap2.pdf)

# Bornes inférieures et supérieures

## Maximum et majorant (resp. minimum et minorant)

On dit que $a ∈ E$ majore $b ∈ E$ si $a ≥ b$. En plus, si $a$ majore tout $b ∈ E$, alors $a$ est un **maximum** de $E$ (ou plus grand élément de $E$). Dans ce cas, il est unique, noté $\max E$.

Soit $A ⊂ E$ une partie de $E$. On dit que $M ∈ E$ est un **majorant** de $A$ s'il majore tous les éléments de $A$. Dans ce cas, on dit que $A$ est majoré par $M$.

On définit de même la minoration, le minimum (noté $\min E$) et le minorant.

## Bornes

Une partie $A ⊂ E$ admettant un minorant et un majorant est dite **bornée**.

- On dit que $A$ admet une borne supérieure s'il est majoré et possède un **majorant plus petit** que tous les autres. Dans ce cas, on note $\sup A$ la borne supérieure de $A$.
- On dit que $A$ admet une borne inférieure s'il est minoré et possède un **minorant plus grand** que tous les autres. Dans ce cas, on note $\inf A$ la borne inférieure de $A$.

# Le corps des nombres réels

## Propriété de la borne supérieure

On dit qu'un ensemble de nombres $E$ satisfait la propriété de la borne supérieure si toute partie $A ⊂ E$ non vide et majorée admet une borne supérieure dans $E$. L'ensemble des réels comble cette lacune de $\mathbb{Q}$.

## Axiomes des nombres réels

On dit qu'en ensemble $E$ muni d'opérations $+, ×$ et de la relation d'ordre $≤$ vérifie les axiomes des nombres réels si :

- $E$ muni de $+, ×$ et $≤$ est un corps totalement ordonné,
- $E$ satisfait la propriété de la borne supérieure.

Il existe un ensemble vérifiant les axiomes des nombres réels. Cet ensemble est noté $\mathbb{R}$ et appelé corps des réels.

# Propriétés de $\mathbb{R}$

## Borne supérieure et “inférieure”

Par définition, $\mathbb{R}$ possède la propriété de la borne supérieure (toute partie non vide majorée possède une borne supérieure). x est la borne supérieure de A, une partie non-vide de \mathbb{R}, si :

- $\forall a \in A, a \le x$
- $\forall \varepsilon > 0, \exists a \in A : a > x-\varepsilon$

Par passage à l'opposé, il possède aussi la " propriété de la borne inférieure " (toute partie non vide minorée possède une borne inférieure). x est la borne inférieure de A, une partie non-vide de \mathbb{R}, si :

- $\forall a \in A, x \le a$
- $\forall \varepsilon > 0, \exists a \in A, a < x + \varepsilon$

## Autres propriétés

- **Propriété des segments emboîtés** :
    
    ![image (48).png](ressources/02_les_nombres_reels_(proprietes_et_partie_enti_image_(48).png)
    
- **Propriété d’Archimède** : pour tout $x, y ∈ \mathbb{R}$ avec $y > 0$, il existe $n ∈ \mathbb{N}$ tel que $n \cdot y > x$.
- **Propriété de l'existence d'une partie entière** : pour tout $x ∈ \mathbb{R}$, il existe un unique entier $n ∈ \Z$ tel que $n ≤ x < n + 1$. Cet entier n s'appelle la partie entière de $x$, notée $E(x)$ ou $\lfloor x\rfloor$.