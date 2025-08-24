## 09 // le surplus du consommateur

### La demande pour un bien discret

**Prix de réserve** : Niveau de prix où le consommateur est indifférent entre acheter un bien et garder son argent.

On suppose que la fonction d'utilité prend une forme quasi-linéaire :

$$
U(x,y) = v(x) + y
$$

- $y$ représente la quantité d'euros dédiée aux autres produits
- On définit $v(0) = 0$

- $r_1$ (prix de réserve pour une unité de bien $x$) est le prix maximum que le consommateur payerait pour en acheter
- $r_2$ pour deux unités, etc.

La fonction d'utilité doit respecter la propriété suivante :

$$
U(0, m) = U(1, m - r_1)
$$

Ce qui devient :

$$
v(0) + m = v(1) + (m - r_1)
$$

On en déduit :

$$
v(1) = r_1
$$

### Estimer l'utilité à partir de la demande

Par récurrence, on dérive que :

$$
r_n = v(n) - v(n - 1)
$$

Aussi :

$$
\sum_{i=1}^n r_i = v(n)
$$

- Puisque $n$ est naturel, cette expression a la forme d'une "dérivée discrète"
- Elle est décroissante par rapport à $n$
- La deuxième dérivée de $v(n)$ est négative

#### Surplus et utilité

- **Surplus brut (SB)** : utilité totale d'acheter $n$ unités
- **Surplus net (SN)** : surplus brut - $n \cdot p$

L'utilité totale est donc : $SB + (m - n \cdot p) = SN + m$

### Autres interprétations du surplus du consommateur

**Surplus du consommateur** : $SC(n) = v(n) - pn$

Le surplus du consommateur mesure la somme que le consommateur exigerait pour renoncer à l'ensemble de sa consommation d'un bien.

### Du surplus du consommateur au surplus des consommateurs

La somme des surplus individuels nous mène au surplus collectif.

### Approximation d'une demande continue

On peut approximer la demande d'un bien disponible en quantités continues avec une fonction "en escalier".

#### Représentation graphique

Pour un bien continu, le surplus du consommateur est représenté par l'aire sous la courbe de demande et au-dessus du prix de marché.

### L'utilité quasi-linéaire

Différence avec les préférences normales :

- Pour les préférences "normales" ou convexes, la quantité demandée de bien 1 dépend de la consommation possible des autres biens
- Pour les préférences quasi-linéaires par rapport à un bien, la quantité demandée de bien 1 ne dépend pas de la quantité consommée des autres biens

>[!important]
>Étant donné que le bien 2, dans ce cas, serait le revenu $m$, on pourrait dire qu'**il n'y a pas d'effet de revenu**.

Mesurer l'utilité par la surface située en-dessous de la courbe de demande n'est parfaitement correct que quand la fonction d'utilité est quasi-linéaire. Par contre, si l'effet revenu sur un bien est presque nul, cette méthode reste une bonne approximation.

### L'interprétation de la variation du surplus du consommateur

En général, le niveau absolu du surplus du consommateur ne suscite pas grand intérêt.

Dans le cas d'une augmentation de prix :

- **R** mesure la perte correspondant au fait de devoir payer davantage pour les unités encore achetées
- **T** mesure la perte correspondant à la réduction de sa consommation

### Le surplus du producteur

**Surplus du producteur** : Mesure la différence entre le montant que les producteurs reçoivent effectivement et le montant minimum qu'ils seraient prêts à accepter pour vendre leur production.

#### Représentation graphique

Le surplus du producteur est l'aire au-dessus de la courbe d'offre et en-dessous du prix de marché.

### L'analyse coût-bénéfice

**Analyse coût-bénéfice** : Méthodologie qui évalue les projets en comparant leurs avantages et leurs coûts sociaux totaux.

Cette analyse utilise souvent le concept de surplus du consommateur pour mesurer les bénéfices d'un projet.
