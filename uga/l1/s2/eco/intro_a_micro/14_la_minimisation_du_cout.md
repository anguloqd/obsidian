## 14 // la minimisation du coût

### La minimisation du coût

**Fonction de coût** : $C(w_1, w_2, q)$ représente le coût minimum nécessaire pour produire une quantité $q$ lorsque les prix des facteurs sont $w_1$ et $w_2$.

#### Les droites d'isocoût

À un certain niveau de coût $C$, on pose :

$$
C = w_1x_1 + w_2x_2
$$

On peut réécrire comme :

$$
x_2 = \frac{C - w_1x_1}{w_2}
$$

Pour différentes valeurs de $C$, on obtient différentes droites d'isocoût.

#### Le problème d'optimisation

Le processus d'optimisation consiste à chercher la plus basse droite d'isocoût possible qui soit tangente à l'isoquante correspondant à la production $q$.

>[!theorem] Condition d'optimalité
>Au point optimal, le taux marginal de substitution technique doit égaler le rapport des prix des facteurs :
>
>$$
>TST = \frac{Pm_1}{Pm_2} = \frac{w_1}{w_2}
>$$

### Fonctions de demande conditionnelle de facteurs

$x_1(w_1, w_2, q)$ exprime la quantité de $x_1$ demandée tenant compte des prix et avec un $q$ fixe.

Cette fonction est différente de la demande des facteurs pour la maximisation du profit :

- Pour la minimisation des coûts, on fixe $q$ et les prix des facteurs
- Pour la maximisation du profit, on ne fixe pas $q$ mais uniquement les prix des facteurs

### Cas particuliers

#### Facteurs compléments parfaits

Pour une fonction de production $f(x_1, x_2) = \min\{ax_1, bx_2\}$ :

$$
C(q) = (aw_1 + bw_2) \cdot q
$$

#### Facteurs substituts parfaits

Pour une fonction de production $f(x_1, x_2) = ax_1 + bx_2$ :

$$
C(q) = \min\{aw_1, bw_2\} \cdot q
$$

#### Facteurs Cobb-Douglas

Pour une fonction $f(x_1, x_2) = x_1^a x_2^b$ avec $a+b=1$ :

1. On part de la condition d'optimalité $TST = \frac{w_1}{w_2}$
2. On remplace le TST par $\frac{a}{b} \cdot \frac{x_2}{x_1}$, donc $\frac{a}{b} \cdot \frac{x_2}{x_1} = \frac{w_1}{w_2}$
3. On résout pour $x_2$ en fonction de $x_1$ : $x_2 = \frac{b \cdot w_1}{a \cdot w_2} \cdot x_1$
4. On substitue dans la fonction de production : $q = x_1^a \cdot \left(\frac{b \cdot w_1}{a \cdot w_2} \cdot x_1\right)^b$
5. On résout pour $x_1$ en fonction de $q$ et des prix des facteurs

### Les rendements d'échelle et la fonction de coût

**Fonction de coût moyen** :

$$
CM(q) = \frac{C(q)}{q}
$$

Relation avec les rendements d'échelle :

- Si la firme présente des rendements d'échelle constants, $CM$ est constant (indépendant de $q$)
- Pour des rendements d'échelle croissants, si $q$ augmente, $CM$ diminue
- Pour des rendements d'échelle décroissants, si $q$ augmente, $CM$ augmente

#### Représentation mathématique

Pour des rendements d'échelle homogènes de degré $r$ :

- Si $r = 1$ (constant) : $C(q) = c \cdot q$ et $CM(q) = c$
- Si $r > 1$ (croissant) : $C(q) = c \cdot q^{1/r}$ et $CM(q) = c \cdot q^{(1-r)/r}$ (décroissant)
- Si $r < 1$ (décroissant) : $C(q) = c \cdot q^{1/r}$ et $CM(q) = c \cdot q^{(1-r)/r}$ (croissant)

### Les coûts à long terme et à court terme

- **Court terme** : au moins un facteur est fixe
- **Long terme** : tous les facteurs sont variables

#### Coût à court terme

$$
CCT(q) = w_1x_1 + w_2\bar{x}_2
$$

Où la demande de $x_1$ dépend de $w_1$, $w_2$, $\bar{x}_2$ (fixé) et $q$.

#### Coût à long terme

$$
C(q) = w_1x_1 + w_2x_2
$$

Où $x_1$ et $x_2$ sont tous deux dépendants de $w_1$, $w_2$ et $q$.

>[!theorem] Relation entre coûts
>
>$$
>C(q) = CCT(q, x_2(q))
>$$
>
>Explication : le coût à long terme égale le coût à court terme quand le facteur $x_2$ est au niveau qui minimise le coût à long terme.
