## 02 // les préférences

### Hypothèses de préférences

>[!important] Axiomes des préférences
>- **Complétude** : deux paniers peuvent toujours être comparés
>- **Réflexivité** : si deux paniers sont égaux, nécessairement les deux paniers sont aussi désirables
>- **Transitivité** : si le panier A est préféré à B et B est préféré à C, alors A est préféré à C

Propriétés additionnelles (si les deux biens sont non-substituts ni non-compléments) :

- **Monotonie** : le plus, le mieux
- **Convexité** : les paniers balancés sont plus préférables que les paniers "extrêmes"

### Représentation des préférences

**Courbes d'indifférence** : ensemble des paniers procurant le même niveau de satisfaction.

Propriétés des courbes d'indifférence :

- Ne se croisent jamais (due à la transitivité)
- Sont continues (due à la complétude)
- Ont une pente négative (due à la monotonie)
- Sont convexes vers l'origine (due à la convexité des préférences)

### Formes des courbes d'indifférence

#### Préférences "normales" (Cobb-Douglas)

- Équation : $y = \frac{\text{cte}}{x}$
- Hyperbole classique
- Forme générale : $U(x,y) = x^a y^b$ où $a, b > 0$

#### Préférences quasilinéaires

- Équation : $\text{cte} = f(x) + y$
- Courbes verticalement parallèles

#### Préférences substituts

- Équation : $ax + by = \text{cte}$
- Droite vers le bas
- Pente : $-\frac{a}{b}$
- Forme générale : $U(x,y) = ax + by$ où $a, b > 0$

#### Préférences complémentaires

- Équation : $\text{cte} = \min\{ax, by\}$
- Forme de "L" avec le coin étant $\frac{y}{x}=\frac{a}{b}$
- Forme générale : $U(x,y) = \min\{ax, by\}$ où $a, b > 0$

### Taux marginal de substitution

Le TMS est la dérivée dans un point en particulier sur une courbe d'indifférence :

$$\text{TMS} = -\frac{dy}{dx}$$

Il est toujours négatif et mesure la propension marginale à payer.

**Interprétation économique** : quantité du bien y à laquelle le consommateur est prêt à renoncer pour obtenir une unité supplémentaire du bien x.

Valeurs particulières :

- Pour Cobb-Douglas : $\text{TMS} = -\frac{ay}{bx}$
- Pour substituts parfaits : $\text{TMS} = -\frac{a}{b}$ (constant)
- Pour compléments parfaits : $\text{TMS} = 0$ ou $\infty$ (selon le segment)
