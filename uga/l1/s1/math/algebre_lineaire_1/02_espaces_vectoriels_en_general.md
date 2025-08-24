## 02 // espaces vectoriels en général

## Espace vectoriel per se

### Définition

Un espace vectoriel est un ensemble formé de vecteurs ($E$), de sorte que :

- l’on puisse additionner (et soustraire) deux vecteurs $u$, $v$ pour en former un troisième $u + v$ (ou $u − v$) et que il reste dans $E$, appelé aussi **composition interne**
- l’on puisse multiplier chaque vecteur $u$ d’un facteur $λ$ pour obtenir un vecteur $λ \cdot u$ qui fait encore partie d'$E$, appelé aussi **composition externe**

Ces deux opérations **doivent** vérifier les huit propriétés montré du chapitre précèdent.

Ainsi, un ensemble de vecteurs que ne vérifie pas au moins l'une de telles propriétés, n'est pas un espace vectoriel, **spécialement, si ni vecteur nul ni l'opposé d'un vecteur ne sont pas inclus**.

### Définition de sous-espace vectoriel

Il est vite fatiguant de vérifier les huit axiomes qui font d’un ensemble un espace vectoriel. Heureusement, il existe une manière rapide et efficace de prouver qu’un ensemble est un espace vectoriel : grâce à la notion de sous-espace vectoriel.

Soit $E$ un $K$-espace vectoriel. Une partie $F$ de $E$ est appelée un sous-espace vectoriel si :

- $(0_F) ∈ F$ (le vecteur nul),
- $u + v ∈ F$ pour tous $u, v ∈ F$. ($(u + v)$ doit faire partie aussi de $F$)
(Propriété appelé “stabilité sous l’addition”)
- $λ \cdot u ∈ F$ pour tout $λ ∈ K$ et tout $u ∈ F$. ($λu$ doit faire partie aussi de $F$)
(Propriété appelé “stabilité sous la multiplication par scalaire”)
- **PENSE PLÛTOT À DES ÉLÉMENTS QU'À EXCLUSIVEMENT DES VECTEURS**.

On en déduit deux théorèmes, dont le premier est vraiment important :

1. Théorème : u**n sous-espace vectoriel est un espace vectoriel**
2. Théorème : soit $A ∈ M_{n,p}(R)$. Soit $AX = 0$ un système d’équations linéaires homogènes à $p$ variables. Alors l’ensemble des vecteurs solutions est un sous-espace vectoriel de $\mathbb{R}^p$.

> [!note]
> **Méthodologie**. Pour répondre à une question du type “L’ensemble $F$ est-il un espace vectoriel ?“, une façon efficace de procéder est de trouver un espace vectoriel $E$ qui contient $F$, puis prouver que $F$ est un sous-espace vectoriel de $E$. Il y a seulement trois propriétés à vérifier au lieu de huit !

## Combinaisons linéaires

### Définition et notes

Soit $n \ge 1$ un entier, soient $\{v_1 , v_2 , … , v_n\}$, $n$ vecteurs d’un espace vectoriel $E$. Alors, tout vecteur de la forme **$u = λ_1v_1 + λ_2v_2 + ··· + λ_nv_n$** (où $\{λ_1 ,λ_2 , … ,λ_n\}$ sont des éléments de $K$) est appelé combinaison linéaire des vecteurs $\{v_1, v_2, … , v_n\}$.

Les scalaires $\{λ_1, λ_2, … , λ_n\}$ sont appelés coefficients de la combinaison linéaire.

- Remarque : si $n = 1$, alors $u = λ_1v_1$ et on dit que $u$ est colinéaire à $v_1$ .
- Tout vecteur qui puisse être représenté comme la sommes des autres vecteurs escaladés, est aussi dit une combinaison linéaire de ces deux vecteurs.

## Sous-espace vectoriel

### Caractérisation d'un sous-espace vectoriel

**Théorème.** Soient $E$ un $K$-espace vectoriel et $F$ une partie non vide de $E$. $F$ est un sous-espace vectoriel de $E$ si et seulement si toute combinaison linéaire de deux éléments de $F$ appartient à $F$.

### Intersection de deux sous-espaces vectoriels

**Proposition :** intersection de deux sous-espaces. Soient $F,G$ deux sous-espaces vectoriels d’un $K$-espace vectoriel $E$. Donc, l’intersection $F ∩ G$ est un sous-espace vectoriel de $E$.

- **Remarque**: la **réunion (ne pas confondre avec intersection !)** de deux sous-espaces vectoriels de $E$ n’est pas en général un sous-espace vectoriel de $E$. C’est normalement un espace… moche et bizarre.

### Somme de deux sous-espaces vectoriels

Soient $F$ et $G$ deux sous-espaces vectoriels d’un $K$-espace vectoriel $E$. L’ensemble de tous les éléments $(u + v)$, où $u$ est un élément de $F$ et $v$ un élément de $G$, est appelé somme des sous-espaces vectoriels $F$ et $G$. Cette somme est notée $F + G$.

**Proposition #4.** Soient $F$ et $G$ deux sous-espaces vectoriels du $K$-espace vectoriel $E$. Donc

- 1. $F + G$ est un sous-espace vectoriel de $E$.
- 2. $F + G$ est le plus petit sous-espace vectoriel contenant à la fois $F$ et $G$.
- **NE PAS CONFONDRE LA SOMME AVEC L'UNION**.

### Sous-espaces vectoriels supplémentaires

Soient $F$ et $G$ deux sous-espaces vectoriels de $E$. $F$ et $G$ sont *en somme directe* dans $E$ si :

- $F ∩ G = \{0_E\}$,
- $F + G = E$.
- On note alors $F ⊕ G = E$.

**Proposition #5.** $F$ et $G$ sont supplémentaires dans $E$ si et seulement si tout élément de $E$ s’écrit d’une manière unique comme la somme d’un élément de $F$ et d’un élément de $G$.

### Sous-espace engendré

**Théorème #4** : soit $\{v_1, … , v_n\}$ un ensemble fini de vecteurs d’un $K$-espace vectoriel $E$. Alors :

- L’ensemble des combinaisons linéaires des vecteurs $\{v_1, … , v_n\}$ est un sous-espace vectoriel de $E$.
- C’est le plus petit sous-espace vectoriel de $E$ (au sens de l’inclusion) contenant les vecteurs $\{v_1 , … , v_n\}$.
- Ce sous-espace vectoriel est appelé sous-espace engendré par $\{v_1, … , v_n\}$ et est noté $\text{Vect}(v_1, … , v_n)$.

On a donc:

- $u ∈ \text{Vect}(v_1 , … , v_n) \iff$ il existe $\{λ_1, … ,λ_n\} ∈ K$ tels que $u = λ_1v_1 + ··· + λ_nv_n$.

## Applications linéaires

### Définition, corollaires et plus

Soient $E$ et $F$ deux $K$-espaces vectoriels. Une application $f$ de $E$ dans $F$ est une application linéaire si elle satisfait aux deux conditions suivantes :

- $f(u + v) = f(u) + f(v)$, pour tous $u, v ∈ E$ ;
- $f(λ \cdot u) = λ \cdot f(u)$, pour tout $u ∈ E$ et tout $λ ∈ K$.
- Corollaire :
    - $f(0_E)$ = $0_F$ (le vecteur normal ou nul de départ est celui de arrivée)
    - $f(−u)$ = $−f(u)$, pour tout $u ∈ E$.

**Caractérisation d'une application linéaire.** Soient $E$ et $F$ deux $K$-espaces vectoriels et $f$ une application de $E$ dans $F$. L’application $f$ est linéaire si et seulement si, pour tous vecteurs $u$ et $v$ de $E$ et pour tous scalaires $λ$ et $µ$ de $K$, on a que $f(λu + µv) = λf(u) + µf(v)$.

**Un peu de vocabulaire** :

- A.L. de $E \mapsto F$ : " **morphisme** " ou " **homomorphisme** ".
- A.L. de $E \mapsto E$ : " **endomorphisme** ".

### Applications linéaires notables

- **Homothétie** : $f_λ : E → E, u \mapsto λu$.
    - $λ = 1, f_λ$ est l’application identité ;
    - $λ = 0, f_λ$ est l’application nulle ;
    - $λ = −1$, on retrouve la symétrie centrale.
- **Projection** : la projection sur $F$ parallèlement à $G$ ($F//G$) est l’application $p : E → E$ définie par $p(u) = v$, por tout vecteur $u = v + w$, avec $v ∈ F$ et $w ∈ G$. Il faut dire aussi que $F$ et $G$ sont sev. supplémentaires de $E$.
    - Une projection $p$ vérifie l’égalité $p^2(u) = p(u)$. Ici, $p^2(u)$ signifie $p(u)\circ p(u)$.

### Image

Si $f : E → F$, l'image d'un ensemble contenu dans $E$ par $f$ **est un autre ensemble** contenu dans $F$. L'image du sous-ensemble initial, $A$, serait $\text{Im}(A)$, qui appartiendrait a $F$.

- Si $E'$ est un sous-espace vectoriel de $E$, alors $f(E')$ est un sous-espace vectoriel de $F$. En particulier, $\text{Im}(f)$ est un sous-espace vectoriel de $F$.
- $f$ est surjective si et seulement si $\text{Im}(f) = F$ (et pas $\text{Im}(f) ∈ F$).

### Noyau

Si $f : E → F$, le noyau de $E$, noté $\text{Ker}(E)$, serait l'ensemble de tous les éléments qui correspondraient à $0$, càd. l’ensemble d’éléments de $E$ tels que $f(u) = 0_F$.

- Le noyau est aussi un sous-espace vectoriel de $E$.
- Si $f$ injective, alors $\text{Ker}(f) = 0_E$ (le réciproque est aussi vrai).

### L'espace vectoriel $\mathcal{L}(E, F)$

Soit $\mathcal{F}(E, F)$ l'ensemble des applications ou fonctions de $E$ en $F$, pas forcément des applications linéaires. Si $\mathcal{F}$ est muni d'une loi de composition interne et externe, $\mathcal{F}$ devient $\mathcal{L}(E,F)$, où $\mathcal{L}$ est l'ensemble des A.L. de $E$ en $F$.

$\mathcal{L}$ est, lui même, un espace vectoriel. C'est, alors, l'espace vectoriel des applications linéaires de $E$ en $F$. $\mathcal{L}$ est aussi un sev. de $F$.

- Notation : $\mathcal{L}(E)$ est un sev. de $\mathcal{F}(E, E)$.

### Composition et inverse d'application linéaires

Si $f : E\mapsto F$ et $g : F \mapsto G$, alors $g \circ f : E\mapsto G$. $f$, $g$ et $g \circ f$ sont toutes des applications linéaires.

- **Vocabulaire** :
    - **Endomorphisme** ou **automorphisme** : A.L. de $E\mapsto E$.
    - **Homomorphisme** : A.L. de $E\mapsto F$.
    - **Isomorphisme** : A.L. de $E\mapsto F$, avec $f$ bijective.
