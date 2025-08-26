## 12 // la technologie

- L'output d'un processus de production est, en principe, observable
- L'output de la consommation, c'est-à-dire l'utilité, n'est pas directement observable

### Inputs et outputs

**Types d'inputs** :
- **Biens de capital** : inputs qui sont eux-mêmes des biens produits (outputs)
  - Ce sont des machines : tracteur, bâtiment, ordinateur…
- **Capital financier** : argent utilisé pour démarrer ou faire tourner une affaire
- **Capital physique** : terme alternatif pour les biens de capital traditionnels

### La description des contraintes techniques

**Ensemble de production** : Toutes les combinaisons de facteurs et de produit qui correspondent à un processus de production techniquement réalisable.

**Isoquantes** : Combinaison de deux facteurs de production, $x_1$ et $x_2$, qui permettraient de produire une quantité constante $q$. Graphiquement représentée par une courbe convexe.
- Le niveau des isoquantes est déterminé par la technologie
- Le niveau des courbes d'indifférences est déterminé par des règles peu arbitraires comme dans le cas de l'utilité

**Fonction de production** : $q = f(x_1, x_2)$ indique la quantité maximale d'output qu'on peut produire avec les quantités d'inputs $x_1$ et $x_2$

### Exemples de technologies

#### Proportions fixes

Il existe une proportion entre $x_1$ et $x_2$ où avoir des unités supplémentaires d'un bien ou l'autre n'augmente pas l'output.

- Analogie des compléments parfaits
- Forme mathématique : $f(x_1, x_2) = \min\{ax_1, bx_2\}$

#### Substituts parfaits

On peut remplacer une unité de $x_2$ avec $x_1$ et la production reste inchangée.

- Même principe que les substituts parfaits pour les consommateurs
- Forme mathématique : $f(x_1, x_2) = x_1 + x_2$

#### Fonction Cobb-Douglas

On prioritise des couples d'inputs "balancés", tenant aussi en considération l'impact individuel de chaque input sur l'output.

- Forme mathématique : $f(x_1, x_2) = A \cdot x_1^a x_2^b$

### Les propriétés de la technologie

>[!important] Propriétés fondamentales
>- **Monotonie** : si on laisse le facteur $x_2$ fixe et on augmente $x_1$, la production augmente
>- **Convexité** : pour deux couples dans une isoquante, $(a_1,b_1)$ et $(a_2,b_2)$, leur moyenne doit être égale ou supérieure à $q$

### Le produit marginal

**Produit marginal** : Variation de la production suite à une variation marginale d'un facteur de production :
- $Pm_1 = \frac{\partial f(x_1,x_2)}{\partial x_1}$
- $Pm_2 = \frac{\partial f(x_1,x_2)}{\partial x_2}$

### Le taux marginal de substitution technique : TST

**Taux marginal de substitution technique** :

$$TST = -\frac{\partial x_2}{\partial x_1} = \frac{Pm_1}{Pm_2}$$

- C'est la pente de l'isoquante au point considéré
- Représente le taux auquel une entreprise peut substituer un facteur à un autre sans changer son niveau de production

### La décroissance du produit marginal

**Loi du produit marginal décroissant** : La dérivée seconde de $f$ par rapport à un facteur est négative.

Il ne s'agit pas réellement d'une loi, mais d'une caractéristique habituelle de la plupart des processus de production. Cette loi s'applique uniquement lorsque tous les autres inputs sont maintenus fixes.

### La décroissance du taux de substitution technique

Il y a une étroite relation entre l'hypothèse de décroissance du taux de substitution technique et celle de décroissance du produit marginal, mais elles restent différentes.

La décroissance du TST concerne la variation du rapport des produits marginaux quand nous augmentons la quantité d'un facteur et que nous réduisons celle de l'autre facteur de façon à rester sur la même isoquante.

### Le court terme et le long terme

- **Court terme** : certains facteurs de production sont fixés à des niveaux prédéterminés
- **Long terme** : tous les facteurs peuvent être modifiés

Si on décide de considérer un facteur fixe pour l'instant, on le note $\bar{x}_2$

### Les rendements d'échelle

**Types de rendements d'échelle** :
- **Rendements d'échelle constants** : $f(\lambda x_1, \lambda x_2) = \lambda f(x_1, x_2)$
- **Rendements d'échelle croissants** : $f(\lambda x_1, \lambda x_2) > \lambda f(x_1, x_2)$
- **Rendements d'échelle décroissants** : $f(\lambda x_1, \lambda x_2) < \lambda f(x_1, x_2)$

Pour une fonction Cobb-Douglas $f(x_1, x_2) = A x_1^a x_2^b$ :

- Si $a + b = 1$ : rendements constants
- Si $a + b > 1$ : rendements croissants
- Si $a + b < 1$ : rendements décroissants
