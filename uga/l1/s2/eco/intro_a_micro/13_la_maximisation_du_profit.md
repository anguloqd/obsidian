## 13 // la maximisation du profit

### Introduction

On va modéliser le comportement d'une firme avec le modèle de maximisation du profit. C'est-à-dire, la firme choisit le plan de production ou couple de facteurs de production $(x_1, x_2)$ qui maximise ses profits.

### Les profits

**Profits** : Différence entre recettes et coûts.

>[!important]
>La définition économique du profit exige d'évaluer tous les inputs et outputs à leur coût d'opportunité.

#### Coût d'opportunité

Le coût d'opportunité d'un facteur de production est la valeur de son meilleur usage alternatif.

### L'organisation des entreprises

Formes d'organisation :

- **Propriété individuelle** : elle appartient à un seul individu
- **Partenariat** : elle appartient à plusieurs personnes. Sa vie dure pendant que ses partenaires sont en vie
- **Société** : elle appartient à plusieurs personnes. Sa vie est indépendante de celles des partenaires

### Profits et valeur boursière de l'entreprise

**Valeur présente de la firme** : Valeur présente de tous les profits futurs.

Le prix d'une action représente la valeur présente du flux de dividendes que les investisseurs s'attendent à recevoir de la société.

#### Calcul de la valeur présente

Pour un flux de profits $\pi_t$ sur T périodes avec un taux d'actualisation $r$ :

$$V = \sum_{t=1}^T \frac{\pi_t}{(1+r)^t}$$

### Facteurs fixes et facteurs variables

**Facteurs fixes** : Facteurs de production qui doivent être rémunérés même si l'entreprise décide de ne rien produire. (ex.: bâtiment loué)

**Facteurs quasi-fixes** : Facteurs qui ne doivent être rémunérés que si l'entreprise décide de produire une quantité positive d'output. (ex.: électricité pour l'éclairage)

### La maximisation du profit à court terme

Cadre d'analyse :

- Soit $f(x_1, x_2)$ la fonction de production, où $x_1$ et $x_2$ sont des facteurs de production
- $w_1$ et $w_2$ sont leurs prix respectifs
- Les profits sont donc $\pi = pq - (w_1x_1 + w_2x_2)$ où $q = f(x_1, x_2)$

#### Condition de premier ordre

L'optimisation de $\pi$ par rapport à $x_1$ donne la valeur de $x_1$ telle que :

$$p \cdot Pm_1 = w_1$$

Où $Pm_1$ est le produit marginal du facteur 1.

#### Interprétation géométrique

On cherche la droite d'isoprofit la plus élevée qui croise l'isoquante de production.

On peut réécrire le profit comme :

$$\pi = pq - w_1x_1 - w_2x_2$$

Et en isolant $x_2$ :

$$x_2 = \frac{pq - w_1x_1 - \pi}{w_2}$$

Ceci est l'équation d'une droite d'isoprofit à un niveau constant $\pi$.

La condition d'optimisation devient :

$$Pm_1 = \frac{w_1}{p}$$

### Statique comparative

Effets des variations de prix :

- Il existe une relation inverse entre $w_1$ et $q$ (si le prix d'un facteur augmente, la production diminue)
- Il existe une relation directe entre $p$ et $q$ (loi de l'offre classique)

### La maximisation du profit à long terme

On applique la condition d'optimisation à tous les facteurs de production :

$$p \cdot Pm_1 = w_1$$

$$p \cdot Pm_2 = w_2$$

#### Cas de la fonction Cobb-Douglas

Pour une fonction Cobb-Douglas $q = x_1^a x_2^b$ :

En multipliant (1) par $x_1$ et (2) par $x_2$, puis en isolant $x_1$ et $x_2$ :

$$x_1 = \frac{ap}{w_1} \cdot q$$

$$x_2 = \frac{bp}{w_2} \cdot q$$

En remplaçant dans la fonction de production :

$$q = \left(\frac{ap}{w_1}\right)^a \left(\frac{bp}{w_2}\right)^b q^{a+b}$$

D'où l'on déduit le $q$ optimal si $a+b \neq 1$.

### Les courbes de demande de facteurs inverses

Les courbes de demande de facteurs inverses s'obtiennent en représentant la relation $p \cdot Pm_1 = w_1$, avec $w_1$ comme variable indépendante et $x_1$ comme fonction de $w_1$.

### La maximisation du profit et les rendements d'échelle

>[!theorem]
>Si une firme a des rendements d'échelle constants à long terme, son profit est forcément nul.

Preuve :

- Supposons une firme qui cherche à maximiser son profit avec des rendements d'échelle constants
- Elle a déjà trouvé son couple de production $(x_1,x_2)$ optimal
- Si elle augmente sa production d'un facteur positif, sa production augmentera du même facteur
- Donc, son couple de production initial n'était pas optimal (contradiction !)
- Cette contradiction disparaît si les profits sont nuls

Implications :

- Si une firme a des rendements d'échelle constants à long terme, son profit est forcément 0
- Si elle a des rendements d'échelle décroissants à long terme, elle sortira du marché
- Si elle a des rendements d'échelle croissants, elle cherchera à s'accroître indéfiniment

#### Limites à la croissance infinie

1. La firme pourrait croître au point de devenir inefficace (rendements d'échelle décroissants à partir d'un certain niveau)
2. Elle pourrait acquérir un pouvoir de marché pour manipuler le prix (le modèle n'est plus valable)
3. Toute entreprise ayant accès à la technologie pour obtenir des rendements d'échelle constants va l'utiliser, augmentant l'offre générale et faisant baisser le prix
