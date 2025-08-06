# 04 // ANOVA

[slides anova1 stat3 annote.pdf](ressources/04_anova_slides_anova1_stat3_annote.pdf)

[slides anova 2 stat 3 annote.pdf](ressources/04_anova_slides_anova_2_stat_3_annote.pdf)

# ANOVA à un facteur

## Motivation

Nous avons utilisé l'ANOVA dans l'étude du modèle linéaire $Y = β₁ξ + β₀ + ε$, avec certaines hypothèses sur $ξ$, $Y$, $ε$ de normalité et de non corrélation des termes d'erreur. Nous avions utilisé les tests de Student et de Fisher afin de vérifier la non nullité de $β₁$, ce qui entraînerait l'absence d'effet de $ξ$ sur $Y$, par l'étude des moyennes ou des variances.

La variable explicative $ξ$ était alors quantitative. Il n'est cependant pas rare de rencontrer une variable explicative qualitative. Le passage par une régression linéaire n'a plus de sens dès que la multiplication $β₁ξ$ n'en a plus. Prenons par exemple la variable $ξ$ à deux modalités :

La variable $ξ$ s'appelle le facteur. On pourra chercher à expliquer une variable réponse $X$, par exemple le taux d'une hormone. Pour chaque valeur $ξᵢ$, on obtient un échantillon indépendant $Xᵢ$. Dans le premier cas :

- $ξ = ξ₁$ : "placébo", d’échantillon $X_{1,1}, X_{1,2}, ···, X_{1,{n_1}}$
- $ξ = ξ₂$ : "traitement expérimental", d’échantillon $X_{2,1}, X_{2,2}, ···, X_{2,{n_2}}$

Ou dans le deuxième cas :

- $ξ = ξ₁$ : "placébo", d’échantillon $X_{1,1}, X_{1,2}, ···, X_{1,{n_1}}$
- $ξ = ξ₂$ : "traitement expérimental", d’échantillon $X_{2,1}, X_{2,2}, ···, X_{2,{n_2}}$
- ξ = ξ₃ : "traitement expérimental à forte dose" d’échantillon $X_{3,1}, X_{3,2}, ···, X_{3,{n_3}}$

On considère le modèle $Xᵢ = E[Xᵢ] + ε$ᵢ. La question est de savoir si les $μᵢ = E[Xᵢ]$ sont identiques ($ξ$ n'a pas d'effet sur $X$) ou différents selon les valeurs $ξᵢ$. Dans ce cas, $ξ$ influence $X$.

## Facteur à deux valeurs

### Le modèle

On considère deux échantillons indépendants de tailles n₁ et n₂, respectivement :

$$
X_{1,1}, X_{1,2}, ···, X_{1,{n_1}}
\\
X_{2,1}, X_{2,2}, ···, X_{1,{n_2}}
$$

Donc, l'estimateur de la variance est $s^2 = \frac{\sum_{j=1}^{n_1} (X_{1,j} - \bar{X}1)^2 + \sum{j=1}^{n_2} (X_{2,j} - \bar{X}_2)^2}{n_1 + n_2 - 2}$

On note que $(n_1 + n_2 - 2)s^2/\sigma^2$ suit une loi $\chi^2(n_1 + n_2 - 2)$.

Notre but est de tester l'hypothèse $H_0 = \text{"}\mu_1 = \mu_2\text{"}$, équivalente à "Le facteur n'a pas d'effet sur la variable $X$", ou encore "les deux échantillons sont issus de la même population". Nous allons donc étudier l'estimateur de la différence des moyennes $\bar{X}_1 - \bar{X}_2$, de moyenne nulle par hypothèse nulle, et de variance :

$$
\text{Var}(\bar{X}_1 - \bar{X}_2) = \text{Var}\left(\frac{1}{n_1}\sum_{j=1}^{n_1} X_{1,j} - \frac{1}{n_2}\sum_{j=1}^{n_2} X_{2,j}\right) = \frac{1}{n_1^2}\text{Var}\left(\sum_{j=1}^{n_1} X_{1,j}\right) + \frac{1}{n_2^2}\text{Var}\left(\sum_{j=1}^{n_2} X_{2,j}\right)
$$

Et, par indépendance des échantillons. Il en suit :

$$
\text{Var}(\bar{X}_1 - \bar{X}_2) = \frac{n_1}{n_1^2}\sigma^2 + \frac{n_2}{n_2^2}\sigma^2 = \sigma^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)
$$

### Le test de Student

Cette quantité sera estimée par $s^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)$.

Le test est basé sur la variable :

$$
T = \frac{\bar{X}_1 - \bar{X}_2}{s\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)
$$

On rejettera donc $H_0$ au seuil $\alpha$ si $|T| \geq q^t_{1-\alpha/2}(n_1+n_2-2)$

Le numérateur de la statistique $T$ est une mesure de l'écart entre les moyennes échantillonnales, alors qu'au dénominateur figure l'écart type s qui est une mesure de la dispersion à l'intérieur des échantillons. Nous rejetons $H_0$ lorsque $|T|$ prend une valeur trop grande, c'est-à-dire lorsque l'écart entre les échantillons est trop grand comparé à la dispersion à l'intérieur des échantillons. Nous utiliserons le même principe maintenant dans le cas de plus de deux échantillons.

## Facteur à $m$ modalités

### Le modèle

Supposons donc qu'on prélève $m$ échantillons indépendants :

$$
X_{1,1}, X_{1,2}, \cdots, X_{1,n_1}
\\
X_{2,1}, X_{2,2}, \cdots, X_{2,n_2}
\\
\vdots
\\
X_{a,1}, X_{a,2}, \cdots, X_{a,n_a}
$$

### Le test de Fisher

L'hypothèse à tester est $H_0$ : "$\mu_1 = \mu_2 = \cdots = \mu_a = \mu'$".

On observe que :

$$
\bar{X}_i - \bar{X} = \sum_{j=1}^{n_i} \frac{1}{n_i}(X_{ij} - \bar{X}) = \sum_{j=1}^{n_i} \frac{1}{n_i}\varepsilon_{ij} = \bar{\varepsilon}_i
$$

dont la variance est $\sigma^2/n_i$. Par conséquent :

$$
\sum_{i=1}^{a} n_i(\bar{X}_i - \bar{X})^2 / \sigma^2 = SCM/\sigma^2 \sim \chi^2(a-1)
$$

On pose :

$$
SCE = \sum_{i=1}^{a} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2
$$

Puisque $\sum_{i=1}^{a} (n_i - 1) = n - a$, on estime $\sigma^2$ par $SCE/(n-a)$ et :
$SCE/\sigma^2 \sim \chi^2(n-a)$, la variable du test est donc :

$$
F = \frac{SCM/(a-1)}{SCE/(n-a)} \sim F_{a-1,n-a}
$$

Nous rejetons $H_0$ au seuil $\alpha$ si :

$$
F = \frac{CMM}{CME} = \frac{SCM/(a-1)}{SCE/(n-a)} \geq q^{F_{a-1,n-a}}_{1-\alpha}
$$

où $q$ est le quantile d'ordre $1-\alpha$ de la dite loi.

Remarquons que nous rejetons $H_0$ seulement si $F$ est trop grand et non si $F$ est trop petit car un $F$ grand signifie que les $\bar{X}_i$ sont trop dispersées, et donc que les $\mu_i$ ne semblent pas être tous égaux.

### Equation de la variance

Posons de plus :

$$
SCT = \sum_{i=1}^{a} \sum_{j=1}^{n_i} (X_{ij} - \bar{X})^2
$$

pour la dispersion totale. On peut aisément établir l'équation de la variance suivante :

$$
SCT = SCM + SCE
$$

Où :

- $SCM = \sum_{i=1}^{m} n_i\bar{X}_i^2 - n\bar{X}^2$
- $SCT = \sum_{i=1}^{m} \sum_{j=1}^{n_i} X_{ij}^2 - n\bar{X}^2$
- $SCE = \sum_{i=1}^{m} \sum_{j=1}^{n_i} X_{ij}^2 - \sum_{i=1}^{m} n_i\bar{X}_i^2$

Les résultats d'une analyse de variance sont habituellement présentés sous la forme d'un tableau comme le suivant :

| Source | Somme des carrés | Degrés de liberté | Moyenne des carrés | $F$ |
| --- | --- | --- | --- | --- |
| Modèle | $SCM = \sum_{i=1}^{m} n_i\bar{X}_i^2 - n\bar{X}^2$ | $m-1$ | $\frac{SCM}{m-1}$ | $F = \frac{CMM}{CME}$ |
| Erreur | $SCT = \sum_{i=1}^{m} \sum_{j=1}^{n_i} X_{ij}^2 - n\bar{X}^2$ | $n-m$ | $\frac{SCE}{n-m}$ |  |
| Total | $SCE = \sum_{i=1}^{m} \sum_{j=1}^{n_i} X_{ij}^2 - \sum_{i=1}^{m} n_i\bar{X}_i^2$ | $m-1$ | $\frac{SCT}{n-1}$ |  |

### Contrastes (rejet de l’hypothèse d’égalité des moyennes)

La table d'analyse de variance nous permet de tester l'hypothèse que les moyennes des populations sont toutes égales. Dans la plupart des cas, le rejet de l'hypothèse soulève de nouvelles questions : si les moyennes ne sont pas toutes égales, où sont les différences? Nous étudions ici le cas où l'expérimentateur a formulé certaines questions (formulé certaines hypothèses) à priori.

Supposons, par exemple, qu'un expérimentateur veuille comparer trois traitements pour la culture des betteraves:

(i) Un engrais minéral appliqué en avril avant l'ensemencement;

(ii) Le même engrais appliqué en décembre avant le labourage;

(iii) Pas de minéraux.

On suppose qu'on rejette significativement l'égalité des moyennes par l'ANOVA. Le type d'engrais et son application.

Pb. Est-ce la nature de l'engrais qui a un effet? Les 2 premiers sont le même engrais.

Les données portent sur la récolte obtenue dans chacune de ces trois conditions. En supposant que l'hypothèse $\mu_1 = \mu_2 = \mu_3$ sera rejetée, l'expérimentateur sait qu'il voudra ensuite tester l'hypothèse :

$$
\frac{\mu_1 + \mu_2}{2} = \mu_3 \Longleftrightarrow \frac{\mu_1}{2} + \frac{\mu_2}{2} - \mu_3 = \sum_i \lambda_i \mu_i
$$

Où,

- $\lambda_1 = \frac{1}{2}$
- $\lambda_2 = \frac{1}{2}$
- $\lambda_3 = -1$

c'est l'hypothèse qu'en moyenne, les minéraux n'ont pas d'effet. Plus généralement, supposons qu'on veuille tester une hypothèse de la forme :

$$
H_0 = "\varphi = \sum_{i=1}^{a} \lambda_i \mu_i = 0"
$$

où $\lambda_i$ sont des constantes données. la fonction linéaire $\varphi = \sum_i \lambda_i \mu_i$ sera estimée par

$$
\hat{\varphi} = \sum_{i=1}^{n} \lambda_i \bar{X}_i
$$

Les $X_{ij} \sim \mathcal{N}(\mu_i, \sigma^2)$ i.i.d. Les $\bar{X}_i = \frac{1}{n_i} \sum_j X_{ij}$ sont des normales en tant que combinaisons linéaires de normales indépendantes

$$
E\bar{X}_i = \frac{1}{n_i} \sum_j EX_{ij} = \frac{1}{n_i} \sum_{j=1}^{n_i} \mu_i = \frac{n_i}{n_i} \mu_i
$$

$$
Var(\bar{X}i) = Var\left(\frac{1}{n_i} \sum_j X{ij}\right) = \frac{1}{n_i^2} \sum_{j=1}^{n_i} Var(X_{ij}) = \frac{n_i}{n_i^2}\sigma^2 = \frac{\sigma^2}{n_i}
$$

avec les $X_{ij}$ indépendants. Notons que les $\bar{X}_i$ sont indépendants et suivent $\mathcal{N}\left(\mu_i, \frac{\sigma}{\sqrt{n_i}}\right)$

Maintenant pour l’estimateur du contraste $\hat{\varphi}$,

$$
E\hat{\varphi} = E\left[\sum_i \lambda_i \bar{X}_i\right] = \sum_i \lambda_i E\bar{X}_i = \sum_i \lambda_i \mu_i = \varphi = 0 \text{ sous } H_0
$$

$$
⁍
$$

avec les $\bar X_i$ indépendants.

Donc, sous $H_0$, $\frac{\hat{\varphi}}{\sigma\sqrt{\sum_i \frac{\lambda_i^2}{n_i}}} \sim \mathcal{N}(0,1)$ et $\sigma^2$ est estimé par $\sqrt{\frac{SCE}{n-a}}$.

$$
⁍
$$

Donc $\frac{{\hat{\varphi}}/{\sigma\sqrt{\frac{\sum \lambda_i^2}{n_i}}}}{{\sqrt{\frac{(n-a)}{n-a}\frac{SCE/n-a}{\sigma^2}}}} \sim t_{n-a}$, qui simplifie à $\frac{\hat{\varphi}}{\sqrt{\frac{SCE}{n-a}}\sqrt{\sum_i \frac{\lambda_i^2}{n_i}}} \sim t_{n-a}$. À comparer au quantile théorique de $t_{n-a}$

# ANOVA à deux facteurs

## Généralisation

La généralisation de l'ANOVA à une voie à des plans d'expérience plus complexes est assez intuitive. Cet exemple suivant utilise deux facteurs.

Le loyer moyen dans une grande ville française, en fonction de deux facteurs : date de construction $A$ et nombre de pièces $B$ est donné par :

|  | $A = 1$
$< 1981$ | $A = 2$

$1981-1990$ | $A = 3$
$1991-2001$ | $A = 4$
$> 2001$ |
| --- | --- | --- | --- | --- |
| $B = 1$
$1$ pièce | 509 | 503 | 521 | 795 |
| $B = 2$
$2$ pièces | 596 | 661 | 814 | 1138 |
| $B = 3$
$3$ pièces | 684 | 791 | 1071 | 1503 |
| $B = 4$
$4$ pièces | 808 | 960 | 1259 | 1741 |
| $B = 5$
$5$ pièces | 1075 | 1216 | 1604 | 2131 |

L'analyse d'un tel jeu de données à pour objectif d'expliquer et de quantifier l'influence des deux facteurs sur la variable réponse (le loyer). Le plan d'expérience employé est complet, en ce sens que, pour chaque combinaison des deux facteurs, on dispose d'une observation.

## Position du problème

On veut mesurer maintenant le rôle conjoint de deux facteurs $A$ et $B$ sur la variable dépendante (réponse). Trois effets sont à mesurer :

- Effet de $A$
- Effet de $B$
- Interaction entre $A$ et $B$

Les deux premiers seront les effets principaux.

### Description des données

La population est notée $P$, $X$ est la variable d'intérêt de moyenne globale $μ$. On étudie le rôle de deux facteurs $A$ et $B$, le facteur $A$ ayant $p$ modalités $(A_1, · · ·, A_p)$, le facteur $B$ ayant $q$ modalités $(B_1, · · ·, B_q)$.

- Les facteurs $A$ et $B$ définissent $p × q$ sous population P_{ij}, sur laquelle la sous-variable X_{ij} de X prend les observations x_{i,j,k} (pour k ≤n_{ij}) et a pour moyenne μ_{ij}.
- On note P_i. les individus correspondants à A = A_i, la sous variable X_i. de X est observée par la concaténation sur j des x_{i,j,k}. La variable X_i. a pour moyenne μ_i. et effectif n_i. = $\sum_{j=1}^{q} n_{ij}$
- On note $P_{\circ,j}$ les individus correspondants à $B = B_j$, la sous variable $X_{\circ,j}$ de $X$ est observée par la concaténation sur $j$ des $x_{i,j,k}$. La variable $X_j$ a pour moyenne $μ_{\circ,j}$ et effectif $n_{j,\circ} = \sum_{i=1}^{p} n_{ij}$

On suppose que dans chaque sous-population $P_{ij}$, les observations $x_{i,j,k}$ forme un échantillon $E_{ij}$.

Note. Pour simplifier l'exposé, dans tout ce qui suit, on considère que le plan d'expériences est équilibré, $\text{card}(E_{ij}) = n_{ij} = n$. Cela n'est pas gênant, en effet, en passant par un plan équilibré, on améliore la robustesse du test.

## Tableau des moyennes

Ce tableau est dérivé et est préféré pour des raisons pratiques que le tableau de données original.

| **Aspiration (X) / Carburant (Y)** | **Atmo**                 | **Turbo**                | **Total**                |
| ---------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| **Diesel**                         | $\bar X_{1,1}=58.1$      | $\bar X_{1,2}=98.6$      | $\bar X_{1,\circ}=78.35$ |
| **Essence**                        | $\bar X_{2,1}=101.6$     | $\bar X_{2,2}=138.4$     | $\bar X_{2,\circ}=120$   |
| **Total**                          | $\bar X_{\circ,1}=79.85$ | $\bar X_{\circ,2}=118.5$ | $\bar X = 112.1$         |

## Graphique des intersections

Ce graphe permet de distinguer les interactions lorsque les lignes se croisent.

![image.png](ressources/04_anova_image.png)

Dans ce cas particulier, lorsque les lignes sont parallèles, il n’y a pas d’effet de l’intersection. Par contre, il y a d’autres patterns qui rendent compte d’un effet de l’intersection.

![image.png](ressources/04_anova_image_1.png)

## Hypothèses statistiques

Ce sont les mêmes que pour l'ANOVA à 1 facteur : normalité de la variable dépendante, indépendance des observations inter et intra groupes, variance homogène dans les groupes.

## Hypothèses soumises au test

Il y en a trois :

$$
\begin{cases}H_0 : \mu_i = \mu, \quad \forall i & \text{absence d'effet de } A \\H_0 : \mu_j = \mu, \quad \forall j & \text{absence d'effet de } B \\H_0 : \mu_{ij} = \mu, \quad \forall i,j & \text{absence d'effet de l'interaction.}\end{cases}
$$

## Equation de la variance

$$
x_{i,j,k} - \bar{X} = \underbrace{(\bar{X}_{i\cdot} - \bar{X}) + (\bar{X}_{\cdot j} - \bar{X})}_{\text{Effet des facteurs principaux}} + \underbrace{(\bar{X}_{ij} - \bar{X}_{i\cdot} - \bar{X}_{\cdot j} + \bar{X})}_{\text{Effet de l'interaction}} + \underbrace{(x_{i,j,k} - \bar{X}_{ij})}_{\text{Erreur résiduelle}}
$$

À partir de laquelle on extrait l'équation d'ANOVA :

$$
\underbrace{SCT}_{\text{Variabilité totale}} = \quad \underbrace{SCM_{A} + SCM_{B} + SCM_{AB}}_{\text{Variabilité expliquée}} \quad + \underbrace{SCE}_{\text{Variabilité résiduelle}}
$$

Où les termes sont :

- $SCT = \sum (x_{ijk} -\bar{X})^2$
- $SCM_A = nq \sum_{i=1}^p (\bar{X}_{i,\circ} -\bar{X})^2$
- $*SCM_B = np \sum_{j=1}^q (\bar{X}_{\circ,j} -\bar{X})^2*$
- $*SCE = \sum (x_{ijk} - \bar{X}_{ij})^2*$
- $*SCM_{AB} = SCT - SCM_A -SCM_B - SCE*$

On calcule les carrés moyens :

- $CMT = \frac{SCT}{pqn-1}$
- $CMM_A = \frac{SCM_A}{p-1}$
- $CMM_B = \frac{SCM_B}{q-1}$
- $CMM_{AB} = \frac{SCM_{AB}}{(p-1)(q-1)}$
- $CME = \frac{SCE}{pq(n-1)}$

Voici les rapports de carrés moyens pour construire les statistiques de Fisher utilisées pour mettre à jour les effets (principaux et interactions).

- Effet de $A$ : $F_A = \frac{CMM_A}{CME}$
- Effet de $B$ : $F_B = \frac{CMM_B}{CME}$
- Effet de l'interaction de $A$ et de $B$ : $F_{AB} = \frac{CMM_{AB}}{CME}$

Ces quantités suivent une loi de Fischer, les degrés de libertés sont lus dans les dénominateurs des carrés moyens associés.