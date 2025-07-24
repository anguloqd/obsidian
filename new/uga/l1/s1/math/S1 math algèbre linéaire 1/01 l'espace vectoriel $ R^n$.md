# 01 // l'espace vectoriel $\R^n$

Date de création: September 19, 2021 8:26 PM
Modifié: May 30, 2023 12:25 AM

# Les bases, venant de l'algèbre abstraite

## Définition

De manière abstraite, pour expliquer ce qui est un espace vectoriel, il faut expliquer ce qui est une tuple et une structure algébrique.

- Une **tuple** est une séquence ordonnée finie d'éléments.
- Une **structure algébrique** est une tuple $(a_1, a_2, ..., a_n)$ où $*a_1*$ est un ensemble non-vide est $(a_2, ..., a_n)$ sont des opérations applicables aux éléments de $*a_1*$.

Finalement, un **espace vectoriel** est une structure algébrique crée d'un ensemble non-vide et deux opérations: l'addition (opération interne) et le produit scalaire (opération externe). Ces deux opérations satisfont huit propriétés fondamentales.

### Les huit propriétés fondamentales

Les propriétés qui suivent découlent de la définition de la somme et multiplication par un scalaire.

- 4 propriétés de l'addition :
    - **Commutativité** : $\forall u,v \in E: u + v = v + u$
    - **Associativité** : $\forall u,v,w \in E : u + (v + w) = (u + v) + w$
    - **Neutralité** : $\exists0_E\in E: u + 0 = 0 + u = u$
    (Existence du vecteur nul ou élément nul)
    - **Opposition** : $\forall u\exists (-u)\in E:u + (-u) = 0$
    (Existence de l’inverse additif)
- 4 propriétés du scalaire :
    - **Neutralité** : $\forall u \in E :1 \cdot u = u$
    - **Associativité** : $\forall u \in E, \text{ où } \lambda,\mu \in \R. : λ \cdot (µ \cdot u) = (λµ) \cdot u,$
    - **Distribution d'un scalaire** : $\forall u,v \in E, \text{ où } \lambda\in \R :λ \cdot (u + v) = λ \cdot u + λ \cdot v$
    (Distribution valide pour la droite et pour la gauche)
    - **Distribution d'un vecteur** : $\forall u \in E, \text{ où } \lambda,\mu \in \R : (λ + µ) \cdot u = λ \cdot u + µ \cdot u$

## Quelques extras

<aside>
1️⃣ **Extra**: la différence entre une tuple et un ensemble.

- **Répétition**: un tuple peut contenir plusieurs instances du même élément.
    - Alors la tuple $(1,2,2,3) \ne (1,2,3)$, mais l'ensemble $\{1,2,2,3\} = \{1,2,3\}$.
- **Ordre**: Les éléments de tuple sont ordonnés.
    - Alors la tuple $(1,2,3) \ne (3,2,1)$, mais l'ensemble $\{1,2,3\}$ = $\{3,2,1\}$.
- **Finitude**: un tuple a un nombre fini d'éléments, tandis qu'un ensemble ou un multi-ensemble peut avoir un nombre infini d'éléments.
</aside>

<aside>
2️⃣ **Extra**: sur les structures algébriques...

- Les arguments des opérations doivent être finis.
- Elles doivent aussi contenir des identités, propriétés et axiomes dérivées des opérations.
</aside>

# $\R^n$ vu comme un espace vectoriel

## En dimension 1 et au-delà

L’ensemble des nombres réels $\R$ est souvent représenté par une droite (penser à la droite numérique normale). C’est un espace de dimension 1.

De même, on peut commencer à définir des tuples de nombres réels.

- Le plan est formé des couples $(x_1, x_2)$ de nombres réels. Il est noté $\R^2$. C’est un espace à deux dimensions.
- L’espace de dimension 3 est constitué des triplets de nombres réels $(x_1,x_2, x_3)$. Il est noté $\R^3$.

Dès ici, on défini: la **somme** de deux vecteurs, le **produit** par un scalaire, le **vecteur nul** et **l'opposé** d'un vecteur.