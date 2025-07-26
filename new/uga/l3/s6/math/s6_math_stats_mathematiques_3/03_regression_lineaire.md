# 03 // régression linéaire

Date de création: March 9, 2024 10:40 PM
Modifié: May 9, 2025 11:32 AM

[slides intro reglin stat3 annote.pdf](slides_intro_reglin_stat3_annote.pdf)

[slides reglin inf annote.pdf](slides_reglin_inf_annote.pdf)

# Régression linéaire - point de vue descriptif

Dans certaines situations, on est amené à étudier deux caractères distincts d'une même population. On peut par exemple considérer la taille ($x$) et le poids ($y$) d'un ensemble d'individus. L'objectif principal de l'étude est de déterminer l'éventuel lien entre les deux variables $x$ et $y$.

## Nuage de points

On relève le couple (taille, poids) de 8 individus. On résume les données dans le tableau suivant.

| taille x | 150 | 155 | 155 | 150 | 165 | 175 | 170 | 180 |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| poids y  | 50  | 55  | 60  | 62  | 65  | 70  | 70  | 90  |

**Definition.** Soit une population de $N$ individus. Le graphe des $N$ points $(x_i, y_i)$ est appelé nuage de points de la série.

**Definition.** Le point ayant pour coordonnées les moyennes $(\bar{x}, \bar{y})$ est appelé le *point moyen*.

Par rapport à la forme de la nuage de points, d'une manière générale, trois cas peuvent se présenter en ce qui concerne le profil du nuage :

- forme allongée et rectiligne : les points sont plus ou moins alignés
- forme allongée mais non rectiligne : les points ne sont pas alignés mais ont un profil ordonné
- forme quelconque

## Ajustement affine (droite de régression linéaire)

On s'intéresse plus particulièrement au premier cas. Procéder à un ajustement affine revient à chercher une droite $D$ d'équation

$$
y = \beta_1 x + \beta_0
$$

qui passe au plus proche des points du nuage de points. Cette droite nous servira donc d'approximation. Bien évidemment, suivant la méthode utilisée pour la construire, on peut obtenir différentes droites. La méthode la plus utilisée car donnant la meilleure approximation est la méthode des moindres carrés.

## La méthode des moindres carrés

L'idée de cette méthode est de chercher la droite qui minimise la somme des carrés des écarts verticaux entre la droite et les points du nuage, les résidus.

En pratique, on détermine les coefficients de la droite D : $y = \beta_1 x + \beta_0$ à l'aide de R ou d'un tableur. La droite ainsi obtenue est unique. Cette droite s'appelle la droite de régression linéaire de y en x par la méthode des moindres carrés. On note

$$
\sigma_{xy} = Cov(x, y) = \frac{1}{N}\sum(x_i - \bar{x})(y_i - \bar{y}).
$$

On a

$$
\beta_1 = cov(x, y)/\sigma^2_x,
$$

$$
\beta_0 = \bar{y} - \beta_1 \bar{x}.
$$

Preuve. On pose la somme des carrés des résidus :

$$
M(\beta_1, \beta_0) = \sum_{i=1}^n (y_i - \beta_1 x_i - \beta_0)^2.
$$

Le minimum de $M(\beta_1, \beta_0)$ s'obtient en annulant les dérivées partielles par rapport à $\beta_1$ et $\beta_0$.

## Coefficient de corrélation linéaire

Notons que la méthode des moindres carrés peut être utilisée pour n'importe quelle série double. On peut tout à fait obtenir une droite de régression dans le premier cas. Pour s'assurer de façon objective (et non purement visuelle) que l'ajustement est valide, on considère un autre paramètre de la série : le coefficient de corrélation $r$

$$
r = \frac{cov(x, y)}{\sigma_x \sigma_y}
$$

**Proposition.** On a les propriétés suivantes :

- on a toujours $-1 \leq r \leq 1$ ;
- le coefficient directeur de la droite de régression et le coefficient de corrélation sont de même signe ;
- le degré de corrélation est d'autant plus fort que r est proche de $1$ ou $−1$.

C'est cette dernière assertion qui nous permet de dire si la droite de régression est proche des points. En pratique, une régression linéaire est légitime si $r > 0.9$ ou si $r < -0.9$.

# Régression linéaire - point de vue inférentiel

## Introduction

### Somme des carrés des écarts

On peut supposer que $x$ et $y$ sont les observations d'un échantillon des variables $X$ et $Y$. On écrit donc le modèle

$$
Y = \beta_1 X + \beta_0 + \varepsilon
$$

Les valeurs $β₁$ et $β₀$ calculées ci-dessus sont en réalité les estimations $β̂₁$ et $β̂₀$ par la méthode des moindres carrés, i.e. minimisant la somme des carrés des écarts (par rapport à la droite)

$$
SCE = \sum_i \varepsilon_i^2
$$

On a alors

$$
\hat{\beta}_1 = \frac{\sum_i (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_i (X_i - \bar{X})^2}
$$

et

$$
\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}
$$

On notera alors les valeurs prédites

$$
\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X
$$

et $Ŷᵢ$ est la valeur associée à $Xᵢ$ par la droite de régression (dite empirique). Il vient que

$$
SCE = \sum_i (\hat{Y}_i - Y_i)^2
$$

### Hypothèses sur les termes d'erreur $ε$

- Indépendance des erreurs : les $ε₁, ε₂, ⋯, εₙ$ sont indépendants.
- Exogénéité : les variables explicatives $(X₁, ⋯ Xₙ)$ ne sont pas corrélées au terme d'erreur. De plus, les erreurs sont centrées $E(εᵢ) = 0$
- Homoscédasticité : les termes d'erreurs sont supposés de variance constante.
- Normalité des termes d'erreur : les termes d'erreurs suivent une loi normale, centrées, de variance σ²

Lemme. Les hypothèses du modèle montrent que $Yᵢ = β₁X + β₀ + εᵢ$ suit une loi normale $N(β₁Xᵢ + β₀, σ²)$. De plus, les $Yᵢ$ sont indépendants.

### Équation de la variance

D'après les hypothèses précédentes, il vient que

$$
Var(Y) = Var(\hat{Y}) + Var(\varepsilon)
$$

grâce à l'exogénéité. Il vient que

$$
\sum_i (Y_i - \bar{Y})^2 = \sum_i (\hat{Y}_i - \bar{Y})^2 + \sum_i (Y_i - \hat{Y}_i)^2
$$

Cette équation a une signification intéressante.

- Le terme $∑ᵢ(Yᵢ - Ȳ)²$ représente la variation totale des valeurs des $Yᵢ$ par rapport à leur moyenne $Ȳ$. On notera cette quantité SCT : Somme des Carrés Totale.
- Puisque le terme $∑ᵢ(Ŷ - Ȳ)²$ est l'écart de la valeur prédite par rapport à la moyenne, nous dirons que ce terme est la Somme des Carrés due au Modèle, notée SCM.

On a donc

$$
SCT = SCM + SCE
$$

### Coefficient de détermination

Le coefficient de détermination est le rapport de variance de $Y$ expliquée par la régression :

$$
R^2 = \frac{Var(\hat{Y})}{Var(Y)}
$$

Le coefficient $R²$ est donc la proportion de variance de $Y$ expliquée par le modèle.

### Distribution de $β̂₁$

La méthode des moindres carrés prend le parti de ne pas considérer d'erreur sur les valeurs $xᵢ$ prises par $X$. Il vient qu'on peut considérer l'ensemble de valeurs $Xᵢ = xᵢ$ qui seront non aléatoires et le modèle équivalent :

$$
Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i
$$

Les termes $εᵢ$ sont des variables aléatoires normales identiques et indépendantes de moyenne nulle et variance $σ²ε$, quelque soit la valeur $Xᵢ$. On en déduit le théorème suivant qui donne la distribution de $β̂₁$.

Théorème. Sous les hypothèses du modèle de régression linéaire simple, $β̂₁$ suit une loi normale d'espérance $β₁$ et de variance :

$$
\frac{\sigma^2_\varepsilon}{\sum^n_{i=1} (X_i - \bar{X})^2}
$$

Lemme. On pose

$$
a_i = \frac{X_i - \bar{X}}{\sum^n_{i=1} (X_i - \bar{X})^2}
$$

Nous avons

$$
\hat{\beta}_1 = \sum^n_{i=1} a_i Y_i
$$

et

$$
\sum^n_{i=1} a_i = 0, \sum^n_{i=1} a^2_i = \frac{1}{\sum^n_{i=1} (X_i - \bar{X})^2}, \sum^n_{i=1} a_i X_i = 1
$$

On fait les remarques suivantes.

- Ce théorème montre que $β̂₁$ est sans biais pour $β₁$. Cela signifie que d'un échantillon à l'autre, la valeur de $β̂₁$ oscille autour de la valeur théorique $β₁$.
- Ces écarts par rapport à la moyenne $β₁$ sont distribuées selon une loi normale dont la variance est

$$
\sigma^2_{\hat{\beta}_1} = \frac{\sigma^2_\varepsilon}{\sum^n_{i=1} (X_i - \bar{X})^2}
$$

On note, donc, que la variance de $β̂₁$ croît avec $σ²ε$, mais qu'elle décroît lorsque $∑ⁿᵢ₌₁(Xᵢ - X̄)²$ croît. Ainsi, plus les $Xᵢ$ sont nombreux et dispersés, plus notre estimation sera fiable.

- On acceptera que la distribution de $β̂₀$ est normale et suit la loi

$$
N\left(\beta_0, \sigma^2_\varepsilon\left(\frac{1}{n} + \frac{\bar{X}^2}{\sum^n_{i=1} (X_i - \bar{X})^2}\right)\right)
$$

En pratique nous ne connaissons pas $σ²_ε$, la variance de la variable $ε$, qui est nécessaire dans le calcul de $σβ̂₁$. Cependant, nous disposons d'une estimation de celle-ci, à savoir :

$$
s^2_\varepsilon = \frac{1}{n-2}\sum^n_{i=1}\varepsilon^2_i = \frac{SCE}{n-2}
$$

Il vient que

$$
(n-2) \frac{s^2_\varepsilon}{\sigma^2_\varepsilon} \sim \chi^2_{n-2}
$$

On en conclut que le rapport $(β̂₁ - β₁)/sβ̂₁$ n'est pas distribuée selon une loi $N(0, 1)$, mais plutôt selon une loi $t$ de Student ayant $n - 2$ degrés de liberté. On a donc les distributions suivantes.

Théorème. En estimant $σ_ε$ par $s_ε$, on obtient les distributions des estimateurs suivantes

$$
(\hat{\beta}_0 - \beta_0)/s_{\hat{\beta}_0} \sim t_{n-2}, (\hat{\beta}_1 - \beta_1)/s_{\hat{\beta}_1} \sim t_{n-2}
$$

avec

$$
s^2_{\hat{\beta}_1} = \frac{SCE}{(n-2)\sum^n_{i=1}(X_i - \bar{X})^2}
$$

et

$$
s^2_{\hat{\beta}_0} = \frac{SCE}{(n-2)}\left(\frac{1}{n} + \frac{\bar{X}^2}{\sum^n_{i=1}(X_i - \bar{X})^2}\right)
$$

Si le nombre de degrés de liberté est assez élevé (plus de trente), on peut faire une approximation de la loi $t$ de Student par une loi $\mathcal N(0, 1)$.

## Intervalles de confiance

### Intervalles de confiances des coefficients de la régression

Le dernier théorème de la section précédente, donne les distributions suivantes.

$$
(\hat{\beta}_0 - \beta_0)/s_{\hat{\beta}_0} \sim t_{n-2}, (\hat{\beta}_1 - \beta_1)/s_{\hat{\beta}_1} \sim t_{n-2}, (n-2)\frac{s^2_\varepsilon}{\sigma^2_\varepsilon} \sim \chi^2_{n-2}
$$

On en déduit les intervalles de confiance à $100(1 - α\%)$ suivants.

$$
\frac{(n-2)s^2_\varepsilon}{q_{\chi^2_{(n-2)}}^{\alpha/2}} \geq \sigma^2_\varepsilon \geq \frac{(n-2)s^2_\varepsilon}{q_{\chi^2_{(n-2)}}^{1-\alpha/2}}
$$

$$
\hat{\beta}_0 - q_{t_{n-2}}^{1-\alpha/2}s_{\hat{\beta}_0} \leq \beta_0 \leq \hat{\beta}_0 + q_{t_{n-2}}^{1-\alpha/2}s_{\hat{\beta}_0}
$$

$$
\hat{\beta}_1 - q_{t_{n-2}}^{1-\alpha/2}s_{\hat{\beta}_1} \leq \beta_1 \leq \hat{\beta}_1 + q_{t_{n-2}}^{1-\alpha/2}s_{\hat{\beta}_1}
$$

où la valeur $q_{t_{n-2}}^{1-\alpha/2}$ est le quantile d'ordre $1 - α/2$ d'une loi de Student à $n - 2$ degrés de liberté (obtenu de la table de la loi de Student).

### Intervalles pour les prévisions

Lorsque nous substituons dans l'équation de la droite de régression une valeur donnée de $X$, soit $X₀$, nous obtenons une certaine valeur que nous notons :

$$
\hat{Y}_0 = \hat{\beta}_0 + \hat{\beta}_1 X_0
$$

Cette valeur de $X₀$ peut être utilisée à deux fins, car elle estime deux choses :

- $E[Y₀] = β₀ + β₁X₀$, c'est-à-dire la moyenne de la variable $Y$ en $X = X₀$ ;
- $E[Y₀] + ε = β̂₀ + β̂₁X₀ + ε$, c'est-à-dire une observation de $Y$ pour un individu ayant en $X = X₀$.

Lorsque l'on fait de telles prévisions, on préfère accompagner celles-ci de limites de confiance.

1. Dans le premier cas, lorsque nous voulons estimer la moyenne de la variable $Y$ lorsque la valeur de $X$ demeure fixée à $X₀$, nous utilisons l'intervalle à $100α\%$ de confiance suivant :
    
    $$
    \hat{Y}_0 \pm q_{t_{n-2}}^{1-\alpha/2}\sqrt{s^2_\varepsilon\left(\frac{1}{n} + \frac{(X_0 - \bar{X})^2}{\sum(X_i - \bar{X})^2}\right)}
    $$
    
    où la valeur $q_{t_{n-2}}^{1-\alpha/2}$ est le quantile d’ordre $1 − α/2$ d’une loi de Student à $n − 2$ degrés de liberté.
    
    ### Preuve
    
    On utilisera les notations et les résultat d’un lemme précédent. Pour rappel,
    
    $$
    a_i = \frac{X_i - \bar{X}}{\sum_{i=1}^n (X_i - \bar{X})^2}
    $$
    
    Nous avons
    
    $$
    \hat{\beta}_1 = \sum_{i=1}^n a_i Y_i
    $$
    
    et
    
    $$
    \sum_{i=1}^n a_i = 0, \sum_{i=1}^n a_i^2 = \frac{1}{\sum_{i=1}^n (X_i - \bar{X})^2}, \sum_{i=1}^n a_i X_i = 1
    $$
    
    nous obtenons,
    
    $$
    \hat{Y}_0 = \bar{Y} + \hat{\beta}_1 (X_0 - \bar{X})
    $$
    
    Puisque
    
    $$
    \hat{\beta}_1 = \sum_{i=1}^n a_i Y_i
    $$
    
    nous avons,
    
    $$
    \hat{\beta}_1 = \sum_{i=1}^n a_i (\beta_1 X_i + \beta_0 + \varepsilon_i)
    $$
    
    Il suit des égalités sur les sommes des a_i que
    
    $$
    \hat{\beta}_1 = \beta_1 + \sum_{i=1}^n a_i \varepsilon_i
    $$
    
    Par conséquent,
    
    $$
    \begin{align} Var(\hat{Y}_0) &= Var(\bar{Y} + \hat{\beta}_1 (X_0 - \bar{X})) \\ &= Var(\beta_0 + \beta_1 \bar{X} + \bar{\varepsilon} + (X_0 - \bar{X})(\beta_1 + \sum_{i=1}^n a_i \varepsilon_i)) \\ &= Var(\bar{\varepsilon} + (X_0 - \bar{X})\sum_{i=1}^n a_i \varepsilon_i) \end{align}
    $$
    
    On voit alors que le coefficient de $ε_i$ est
    
    $$
    \frac{1}{n} + (X_0 - \bar{X})a_i
    $$
    
2. Dans le second cas, il s'agit de prévoir, pour un individu donné, la valeur de $Y$ qui lui est propre, sachant que sa valeur en $X$ est $X₀$. L'intervalle est
    
    $$
    \hat{Y}_0 \pm q_{t_{n-2}^{1-\alpha/2}}\sqrt{s^2_\varepsilon\left(1 + \frac{1}{n} + \frac{(X_0 - \bar{X})^2}{\sum_i(X_i - \bar{X})^2}\right)}
    $$
    
    ### Preuve
    
     Il s'agit maintenant de trouver la variance de β̂₀ + β̂₁X₀ + ε. On note que ε est une réplication du terme d'erreur indépendante des autres. Il suit
    
    $$
    Var(\hat{\beta}_0 + \hat{\beta}_1 X_0 + \varepsilon) = Var(\hat{\beta}_0 + \hat{\beta}_1 X_0) + Var(\varepsilon)
    $$
    
    De manière analogue à la preuve précédente,
    
    $$
    Var(\hat{\beta}_0 + \hat{\beta}_1 X_0 + \varepsilon) = \sigma^2_\varepsilon\left(1 + \frac{1}{n} + \frac{(X_0 - \bar{X})^2}{\sum(X_i - \bar{X})^2}\right)
    $$
    
    qui peut être estimée par
    
    $$
    s^2_\varepsilon\left(1 + \frac{1}{n} + \frac{(X_0 - \bar{X})^2}{\sum(X_i - \bar{X})^2}\right)
    $$
    

## Tests sur la pente de la droite

Pour faire simple, les tests $F$ de Fischer et $t$ de Student testent l'hypothèse $H₀$ sous laquelle le coefficient $β₁$ est nul, contre $β₁$ est non nul (ce qui permet d'affirmer que $X$ explique $Y$, au moins en partie).

### Test de Student

Notons l'hypothèse nulle

$$
H_0 = "\beta_1 = 0"
$$

autrement formulée, $H₀$ est équivalente à "$X$ n'explique pas $Y$". L'estimation de $β₁$ dans le théorème précédent, montre que

$$
\frac{\hat{\beta}_1 - \beta_1}{s_{\hat{\beta}_1}} \sim t_{n-2}
$$

et sous $H₀$, nous garderons

$$
\frac{\hat{\beta}_1}{s_{\hat{\beta}_1}} \sim t_{n-2}
$$

Rappelons l'estimation

$$
s_{\hat{\beta}_1} = \sqrt{\frac{SCE}{(n-2)\sum(X_i - \bar{X})^2}}
$$

Nous ferons donc un test (bilatéral) de Student sur la statistique de test $β̂₁/s_{β̂₁}$. On rejettera $H₀$ au seuil $α$ si

$$
\frac{|\hat{\beta}_1|}{s_{\hat{\beta}_1}} \geq q_{t_{n-2}^{1-\alpha/2}}
$$

### Table d'ANOVA

L'analyse de la variance, souvent présentée sous forme d'un tableau, permet d'éclairer sur l'influence de la variable $X$ sur la variable $Y$ grâce à l'étude de la décomposition de la variance. Notons, encore, l'hypothèse nulle

$$
H_0 = "\beta_1 = 0"
$$

On note que $SCM = β̂₁²∑_i(X_i - X̄)²$. On a vu que

$$
s^2_\varepsilon = \frac{1}{n-2}\sum_{i=1}^n \varepsilon_i^2 = \frac{SCE}{n-2}
$$

et on rappelle que sous $H₀$,  $(β₁ = 0), β̂₁/s_{β̂₁} ~ t_{n-2}$, avec

$$
s^2_{\hat{\beta}_1} = \frac{SCE}{(n-2)\sum(X_i - \bar{X})^2}
$$

Il vient que

$$
\left(\frac{\hat{\beta}_1}{s_{\hat{\beta}_1}}\right)^2 = \frac{\hat{\beta}_1^2 \sum(X_i - \bar{X})^2}{\frac{SCE}{n-2}} = \frac{SCM}{SCE/(n-2)}
$$

suit une loi de Fisher $F_{1,n-2}$ en tant que carré de la loi de Student. La variable du test est donc

$$
\frac{SCM}{SCE/(n-2)}
$$

et on observe son éloignement (à droite) de zéro. Ainsi, si la p-value dans la table d'ANOVA est proche de zéro (ou en dessous du seuil fixé), on rejettera la nullité de $β̂₁$.

Dans ce cadre, on voit qu'on peut utiliser le test de $t$ de Student pour le rapport $β̂₁/s_{β̂₁}$ ou $F$ de Fisher pour le carré de ce rapport, sans distinction. Il est totalement équivalent en cas de régression simple (ce n'est pas le cas sur une régression multiple). On note d'ailleurs que la statistique $F$ est le carré de la statistique $t$.

Dans le cadre d'une régression multiple (sur plusieurs variables explicatives), le test de Fischer teste l'effet global des variables sur la variable $Y$, les tests de Student testent l'effet de chaque variable explicative sur $Y$.

## Tests sur régression linéaire multiple

La question qu'on se pose est de savoir si la variable réponse est expliquée par les variables explicatives dans leur globalité, ou par telle ou telle variable explicative. Cela se traduit, mathématiquement, par la non nullité des coefficients de la régression. En effet, si le coefficient d'une des variable explicative est nul ou presque nul, cette variable explicative fait peu varier la régression linéaire, elle n'influence donc pas la variable réponse. Plaçons-nous dans le cadre de la régression linéaire multiple.

### Les tests $t$ de Student

Les tests de Student testent la nullité de chaque coefficient de la régression linéaire. Ainsi, on saura quelles variables explicatives ont un effet sur la variable expliquée.

L'hypothèse nulle de chaque test est $H₀ = "\text{La variable } X_i \text{ n'a pas d'effet sur la variable réponse}" = "β_i = 0"$.

Pour prendre une décision :

- Si la p-value est inférieure au un niveau $α$ choisi (en général $0.05$), alors on rejette l'hypothèse nulle et on considère que la variable $X_i$ a un effet sur la variable réponse.
- Si la p-value est supérieure au niveau $α$ choisi (en général $0.05$), alors on ne doit pas rejeter l'hypothèse nulle. La variable $X_i$ n'a pas d'effet sur la variable réponse.

### Les tests $F$ de Fisher - ANOVA

Le test de Fisher teste l'effet de l'ensemble des variables explicatives sur la variable réponse. Ainsi, on saura si la variable réponse est expliquée par les variables explicatives. On appelle cela une ANalyse de la (Of) VAriance.

L'hypothèse nulle du test est $H₀ = "\text{Les variables } X_i \text{ n'ont pas d'effet, dans leur globalité, sur la variable réponse}" = "\text{la variance de l'erreur est très forte face à la variance expliquée par le modèle}"$.

Pour prendre une décision :

- Si la p-value est inférieure au un niveau $α$ choisi (en général $0.05$), alors on rejette l'hypothèse nulle et on considère que les variable $X_i$ ont un effet global sur la variable réponse.
- Si la p-value est supérieure au niveau $α$ choisi (en général $0.05$), alors on ne doit pas rejeter l'hypothèse nulle. Les variables $X_i$ n'ont pas d'effet sur la variable réponse.