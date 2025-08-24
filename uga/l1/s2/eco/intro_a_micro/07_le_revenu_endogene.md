# 07 // le revenu endogène

## Introduction

Jusqu'ici, nous avons considéré que le revenu du consommateur était fixe et "exogène". En réalité, on gagne son revenu en vendant les biens que nous possédons.

## Demandes nettes et demandes brutes

On suppose que le consommateur dispose au départ d'une dotation des deux biens qu'on va noter $(\omega_1, \omega_2)$.
- Le consommateur va demander un panier $(x_1, x_2)$
- $x_1$ et $\omega_1$ sont le même produit, mais $x_1$ est la quantité demandée et $\omega_1$ la quantité offerte

>[!important] Types de demande
>- **Demande brute** : demande reflétée dans le panier de consommation $(x_1, x_2)$
>- **Demande nette** : quantité demandée moins quantité offerte de chaque bien $(x_1 - \omega_1, x_2 - \omega_2)$
>  - Une demande nette négative indique que le consommateur consomme moins que ce qu'il offre
>  - Une demande nette négative est donc une quantité offerte

## La contrainte budgétaire

Ancienne formulation : La contrainte budgétaire était exprimée comme $m = p_1x_1 + p_2x_2$

Nouvelle formulation avec dotation : Ce qu'on gagne dépend de notre offre (combien on offre et à quel prix) :
$$m = p_1\omega_1 + p_2\omega_2$$

La contrainte budgétaire devient donc :
$$p_1x_1 + p_2x_2 = p_1\omega_1 + p_2\omega_2$$

Ou sous forme simplifiée :
$$p_1(x_1 - \omega_1) + p_2(x_2 - \omega_2) = 0$$

### Représentation graphique

La droite de contrainte budgétaire peut être tracée de deux façons :
- Auparavant : équation point-point d'une droite passant par $m/p_1$ et $m/p_2$
- Maintenant : équation pente-point, avec pente $(-p_1/p_2)$ et passant par le point $(x_1 = \omega_1, x_2 = \omega_2)$, car on peut consommer tout ce qu'on offre

## Modification de la dotation initiale

Effets d'une modification de dotation :
- Si la dotation initiale augmente de $(\omega_1, \omega_2)$ à $(\omega'_1, \omega'_2)$, cela signifie que $m$ augmente aussi (prix fixes), donc la droite de budget se déplace vers l'extérieur
- Si elle décroît, la droite se déplace vers l'intérieur
- Si une modification à $(\omega'_1, \omega'_2)$ ne change pas l'égalité $p_1x_1 + p_2x_2 = p_1\omega_1 + p_2\omega_2$, la nouvelle dotation reste sur la même droite, avec un simple déplacement le long de celle-ci

## Les variations de prix

| Si $p_1$ augmente | Si $p_1$ diminue |
|-------------------|------------------|
| Acheteur net de bien $x_1$: Satisfaction décroît | Acheteur net de bien $x_1$: Satisfaction augmente |
| Vendeur net de bien $x_1$: Satisfaction augmente | Vendeur net de bien $x_1$: Satisfaction décroît |

- Un consommateur vendeur d'un bien $x_1$ peut devenir acheteur du même bien lors d'une variation du prix, ou inversement
- Un vendeur ou acheteur "définitif" est celui qui reste vendeur ou acheteur après la variation

## Chemins d'expansion et courbes de demande

- On commence depuis le point de dotation
- Il existe une certaine combinaison de prix où le consommateur ni vend ni achète, c'est le point de dotation
- Si le prix du bien $x_1$ monte, la droite de budget se rétrécit vers la gauche et vers le haut
- $x_1$ suit la loi de la demande : si le prix augmente, la quantité demandée diminue
- La courbe de demande du bien $x_1$ passe par le point de dotation $\omega_1$

### Demande brute et demande nette

Demande brute :
- Elle passe par le point de dotation
- Si le prix diminue, le consommateur voudra rester acheteur net
- Si le prix augmente, le consommateur voudra rester vendeur net

## Un réexamen de l'équation de Slutsky

Slutsky permettait de voir l'effet total sur la quantité demandée suite à une variation du prix, supposant que le revenu restait constant. Maintenant que le revenu dépend aussi des prix, il ne peut plus rester constant.

>[!important] Décomposition étendue
>Variation totale de la demande = variation due à l'effet de substitution + variation due à l'effet de revenu ordinaire + variation due à l'effet de revenu de la dotation

### Effets de revenu distingués

Dans le cas d'une diminution des prix :

**Effet de revenu ordinaire** : Indique qu'on peut acheter la même quantité du bien en gardant une partie du revenu.
- Si le bien est normal, la quantité demandée augmente
- Si le bien est inférieur, la quantité demandée diminue

**Effet de revenu de la dotation** : Indique l'effet de la variation de prix sur notre revenu.
- Si on est vendeur net de ce bien, une baisse de prix diminue notre revenu

### Équation de Slutsky modifiée

On réécrit l'équation de Slutsky en termes de variation du prix :

$$\frac{\Delta x_1}{\Delta p_1} = \frac{\Delta x_1^s}{\Delta p_1} + \frac{\Delta x_1^m}{\Delta p_1}$$

L'effet revenu peut être divisé comme suit :

Effet de revenu = variation de la demande quand le revenu se modifie × modification du revenu quand le prix varie

- **Premier terme** : $\frac{\Delta x_1^m}{\Delta m}$ (impact d'un changement de revenu sur la demande)
- **Deuxième terme** : $\frac{\Delta m}{\Delta p_1} = \omega_1$ (impact d'un changement de prix sur le revenu)

L'effet de revenu dotation est donc : $\frac{\Delta x_1^m}{\Delta m} \cdot \omega_1$

L'équation finale de Slutsky devient :

$$\frac{\Delta x_1}{\Delta p_1} = \underbrace{\frac{\Delta x_1^s}{\Delta p_1}}_{\text{Effet substitution}} + \underbrace{\frac{\Delta x_1^m}{\Delta m} \cdot (x_1 - \omega_1)}_{\text{Effet revenu net}}$$

### Analyse des effets

Supposons une hausse du prix du bien $x_1$ :
- L'effet substitution entraînera une baisse de la quantité demandée
- Si le consommateur est demandeur net, la quantité demandée descendra davantage
- S'il est vendeur net, le résultat est incertain, car l'effet revenu dotation peut contrecarrer l'effet substitution

## L'offre de travail

### Modélisation de base

Variables du modèle :
- $p$ : prix unitaire de la consommation
- $C$ : quantité de consommation
- $w$ : taux de salaire
- $L$ : quantité de travail offerte
- $M$ : revenu non salarial (épargne, parents, allocations...)

On suppose que le consommateur consomme tout ce qu'il gagne en revenu (pas d'épargne).

La contrainte budgétaire s'écrit :
$$pC = M + wL$$

On peut aussi l'écrire :
$$pC - wL = M$$

$M$ peut être interprétée comme la dotation initiale de ressources.

### Ajustement pour le temps disponible

- On limite l'offre de travail à 24 heures par jour, 7 jours par semaine
- 24 heures * 7 jours = 168 heures, noté $\bar{L}$

On modifie l'équation en ajoutant $w\bar{L}$ aux deux côtés :

$$pC + w\bar{L} - wL = M + w\bar{L}$$
$$pC + w(\bar{L} - L) = M + w\bar{L}$$

- La limite de consommation si on ne travaillait pas serait $\bar{C} = M/p$
- On réécrit comme $p\bar{C} = M$ et on substitue
- $pC + w(\bar{L} - L) = p\bar{C} + w\bar{L}$

### Introduction du temps de loisir

Le temps de loisir $R = (\bar{L} - L)$ ("R" de relaxation)
- La limite des heures de loisirs serait $\bar{R} = \bar{L}$ (si on consacre toutes nos heures aux loisirs)

L'équation devient finalement :
$$pC + wR = p\bar{C} + w\bar{R}$$

Interprétation :
- Valeur de la consommation et loisir = valeur de la dotation en consommation et loisir
- La dotation en temps est évaluée sur la base du taux de salaire
- Le membre droit de l'équation devient une constante

### Analyse de l'équilibre

- Cette équation a une structure égale à la contrainte budgétaire avec un consommateur doté de biens
- La courbe de contrainte budgétaire passe par le point de dotation : ($\bar{C}$, $\bar{R}$)
- La courbe a une pente égale à $-\frac{w}{p}$
- Le point optimal est où $\frac{Um_R}{Um_C} = \frac{w}{p}$
- Le salaire réel $(w/p)$ est la quantité de consommation que l'individu gagne s'il renonce à une heure de loisir

### Variations sur les constantes

Effets de variations :
- Si les revenus non salariaux $(M)$ augmentent, l'offre de travail $(L)$ diminue (et $R$ augmente)
  - Donc, les loisirs sont des biens normaux et le travail est un bien inférieur

- Si $w$ augmente, $R$ peut augmenter ou diminuer
  - Si $w$ est faible, une augmentation fait augmenter $L$, donc $R$ diminue
  - Si $w$ est élevé, une augmentation fait diminuer $L$, donc $R$ augmente

### Décomposition de Slutsky pour l'offre de travail

- L'effet de substitution est toujours l'inverse de la variation de $w$ (toujours de signe négatif)
- Pour l'effet revenu (ordinaire et dotation), $(\bar{R} - R)$ est presque toujours positif et $\frac{\Delta R}{\Delta m}$ est toujours positif, donc ce terme est positif
- Avec une variation de $w$, l'effet sur $R$ n'est pas déterminé
  - L'effet revenu domine l'effet substitution quand $(\bar{R} - R)$ est grand, c'est-à-dire, quand l'offre de travail est grande ou $R$ est petit

Un tarif majoré pour heures supplémentaires implique nécessairement une augmentation de l'offre de travail, alors qu'une augmentation du taux de salaire pour toutes les heures travaillées a un effet indéterminé.

- Un tarif majoré pour heures supplémentaires correspond à un effet de substitution pur : rotation de la droite de budget autour d'un point choisi
- Une augmentation du salaire de base serait une rotation-translation (effet substitution + effet revenu)