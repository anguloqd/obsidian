# 03 // l'utilité

## Concept d'utilité

L'utilité est une représentation mathématique des préférences. Une fonction d'utilité $U(x,y)$ attribue des valeurs numériques aux paniers de biens.

Si panier A est préféré à B, alors $U(\text{panier A}) > U(\text{panier B})$.

## Propriétés des fonctions d'utilité

>[!important] Caractéristiques fondamentales
>- **Ordinalité** : seul l'ordre des niveaux d'utilité compte, pas les valeurs absolues
>- **Transformations monotones** : si $V = f(U)$ où $f'(U) > 0$, alors V représente les mêmes préférences que U

### Utilité marginale

L'utilité marginale est la variation d'utilité suite à un changement marginal dans la consommation d'un bien :
- $Um_1 = \frac{\partial U}{\partial x}$ ou $\frac{\Delta U}{\Delta x}$
- $Um_2 = \frac{\partial U}{\partial y}$ ou $\frac{\Delta U}{\Delta y}$

### Taux Marginal de Substitution (TMS)

$$\text{TMS} = \frac{Um_1}{Um_2}$$

## Fonctions d'utilité courantes

### Cobb-Douglas
$$U(x,y) = x^a y^b$$

Propriétés :
- TMS = $-\frac{a}{b} \cdot \frac{y}{x}$
- Utilité marginale de x : $Um_x = a \cdot x^{a-1} \cdot y^b$
- Utilité marginale de y : $Um_y = b \cdot x^a \cdot y^{b-1}$

### Substituts parfaits 
$$U(x,y) = ax + by$$

Propriétés :
- TMS = $-\frac{a}{b}$ (constant)
- $Um_x = a$, $Um_y = b$ (constants)

### Compléments parfaits 
$$U(x,y) = \min\{ax, by\}$$

Propriétés :
- TMS = 0 ou $\infty$ selon le segment
- Utilité marginale : discontinue aux points d'égalité $ax = by$

### Fonctions quasi-linéaires 
$$U(x,y) = f(x) + y$$

Propriétés :
- TMS = $-f'(x)$ (dépend uniquement de x)
- $Um_x = f'(x)$, $Um_y = 1$ (constante)
- Exemples : $\sqrt{x} + y$, $\ln(x) + y$
- Les courbes d'indifférence sont verticalement parallèles
- L'effet revenu est nul pour le bien x

## Importance de l'utilité en microéconomie

- L'utilité est un concept ordinal plutôt que cardinal
- La fonction d'utilité sert uniquement à mettre en ordre les paniers
- L'écart numérique entre utilités n'a pas d'interprétation directe
- Les préférences "normales" sont généralement monotones et convexes