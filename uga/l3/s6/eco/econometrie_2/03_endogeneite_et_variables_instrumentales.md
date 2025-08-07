# 03 // endogénéité et variables instrumentales

[03_endogeneite_et_variables_instrumentales_l3_endogeneite_et_vis.pdf](ressources/03_endogeneite_et_variables_instrumentales_l3_endogeneite_et_vis.pdf)

# Endogénéité et variables instrumentales

L'endogénéité constitue l'une des violations les plus critiques des hypothèses de base de la régression linéaire classique. Ce phénomène survient lorsqu'une ou plusieurs variables explicatives sont corrélées avec le terme d'erreur du modèle, compromettant ainsi la validité des estimations obtenues par les moindres carrés ordinaires (MCO). La méthode des variables instrumentales représente l'approche privilégiée pour résoudre ces problèmes d'identification causale.

## Types fondamentaux d'endogénéité

L'endogénéité peut se manifester sous trois formes principales, chacune ayant des implications distinctes pour l'estimation économétrique et nécessitant des stratégies d'identification spécifiques.

### Variables explicatives pertinentes omises

Le premier type d'endogénéité résulte de l'omission de variables explicatives pertinentes. Cette situation est particulièrement fréquente en sciences sociales où de nombreux facteurs inobservables peuvent simultanément influencer la variable dépendante et les variables explicatives observées.

L'exemple classique de l'effet de la taille des classes sur les résultats scolaires illustre parfaitement ce problème. Considérons le modèle suivant où l'on souhaite estimer l'impact de la taille des classes de CE1 ($\text{tailclas}_i$) sur les résultats des élèves aux tests de mathématiques ou de français ($\text{score}_i$) :

$$\text{score}_i = \alpha_0 + b_{1,0} \text{tailclas}_i + \mathbf{b}_{-1,0}' \mathbf{c}_i + u_i \quad \text{avec } E[u_i] = 0$$

L'effet causal d'intérêt est $b_{1,0}$, qui mesure l'impact d'une augmentation d'une unité de la taille de classe sur le score. Intuitivement, on s'attend à ce que $b_{1,0} < 0$, reflétant l'hypothèse qu'une réduction de la taille des classes améliore les performances scolaires.

Le vecteur $\mathbf{c}_i$ contient les caractéristiques observables de l'élève (âge, sexe), de sa famille (situation professionnelle, composition du ménage) et de l'école (localisation, taille, statut ZEP). Cependant, de nombreux facteurs cruciaux demeurent inobservés : l'origine des parents et leur maîtrise de la langue, les aptitudes scolaires naturelles de l'élève (mesurables par le QI), ou encore son comportement en classe (calme ou turbulent).

Ces éléments inobservés, regroupés dans le vecteur $\tilde{\mathbf{q}}_i$, influencent à la fois les résultats scolaires et l'affectation aux classes. Si le "vrai" modèle incluait ces variables :

$$\text{score}_i = \delta_0 + b_{1,0} \text{tailclas}_i + \mathbf{b}_{-1,0}' \mathbf{c}_i + \boldsymbol{\lambda}' \tilde{\mathbf{q}}_i + v_i \quad \text{avec } E[v_i] = 0$$

Alors le modèle estimé relie ces deux spécifications par :

$$\alpha_0 = \delta_0 + E[\boldsymbol{\lambda}' \tilde{\mathbf{q}}_i]$$

et 

$$u_i = v_i + (\boldsymbol{\lambda}' \tilde{\mathbf{q}}_i - E[\boldsymbol{\lambda}' \tilde{\mathbf{q}}_i])$$

Les effets moyens des variables omises s'incorporent dans la constante du modèle, tandis que leurs déviations par rapport à cette moyenne contaminent le terme d'erreur.

L'endogénéité émerge du fait que l'affectation des élèves aux classes n'est pas aléatoire. Les élèves en difficulté sont généralement placés dans les classes plus petites pour bénéficier d'un suivi personnalisé, créant une corrélation positive entre la taille de classe et les caractéristiques inobservées : $\text{Cov}(\text{tailclas}_i, u_i) > 0$. Cette corrélation biaise l'estimateur MCO vers zéro, masquant l'effet réellement négatif de la taille de classe sur les performances.

### Simultanéité

La simultanéité constitue le deuxième type d'endogénéité majeur, survenant lorsque les variables explicatives et la variable dépendante se déterminent conjointement. Cette situation est courante en économie où les agents prennent simultanément des décisions interdépendantes.

L'étude de l'impact de la maternité sur le salaire des femmes par Angrist et Evans exemplifie ce problème. Le modèle d'intérêt s'écrit :

$$\text{salaire}_i = \alpha_0 + b_{1,0} \text{nbenf}_i + \mathbf{b}_{-1,0}' \mathbf{c}_i + u_i \quad \text{avec } E[u_i] = 0$$

où $\text{nbenf}_i$ représente le nombre d'enfants et $\mathbf{c}_i$ les variables de contrôle démographiques et socioéconomiques.

La simultanéité provient du fait que les choix de maternité et les décisions professionnelles sont pris de manière conjointe. D'une part, le salaire influence le nombre d'enfants par un double effet : les ressources disponibles pour élever les enfants et le coût d'opportunité du temps consacré à la maternité. D'autre part, le nombre d'enfants affecte le salaire par les contraintes temporelles qu'il impose sur la carrière professionnelle et les modifications de productivité qui peuvent en résulter.

Cette interdépendance rend $\text{nbenf}_i$ endogène car cette variable devient fonction du salaire et donc du terme d'erreur $u_i$. L'estimateur MCO produit empiriquement des coefficients proches de zéro, reflétant cette confusion entre les effets causaux bidirectionnels.

### Erreurs de mesure sur les variables explicatives

Le troisième type d'endogénéité, souvent négligé en pratique, résulte des erreurs de mesure affectant les variables explicatives. Bien que ce problème soit essentiellement technique, il a des implications profondes pour l'identification causale.

Considérons le modèle d'intérêt :

$$y_i = \alpha_0 + b_0 \tilde{x}_i + u_i \quad \text{avec } E[u_i] = E[u_i | \tilde{x}_i] = 0$$

où $\tilde{x}_i$ représente la vraie valeur de la variable explicative, qui n'est pas directement observée. Nous disposons seulement d'une mesure bruitée :

$$x_i^e = \tilde{x}_i + e_i$$

où $e_i$ constitue l'erreur de mesure, supposée satisfaire $E[e_i] = E[e_i | \tilde{x}_i] = E[u_i | e_i] = 0$.

Par substitution, le modèle observable devient :

$$y_i = \alpha_0 + b_0 x_i^e + v_i$$

avec $v_i = u_i - b_0 e_i$ et $E[v_i] = 0$.

L'endogénéité apparaît mécaniquement car :

$$\text{Cov}(x_i^e, v_i) = \text{Cov}(x_i^e, u_i - b_0 e_i) = -b_0 V(e_i)$$

La variable explicative mesurée avec erreur est par construction corrélée avec le terme d'erreur du modèle observable.

Cette corrélation induit un biais d'atténuation. L'estimateur MCO converge vers :

$$\text{plim}_{N \to +\infty} \hat{b}_{MCO,N} = b_0 \times \frac{V(\tilde{x}_i)}{V(\tilde{x}_i) + V(e_i)} < b_0$$

L'erreur de mesure atténue systématiquement l'effet estimé en valeur absolue, d'autant plus que la variance de l'erreur est importante relativement à la variance de la vraie variable.

## Biais d'endogénéité de l'estimateur des moindres carrés ordinaires

Le biais d'endogénéité représente une propriété générale de l'estimateur MCO lorsque la condition d'exogénéité stricte $E[\mathbf{x}_i u_i] = \mathbf{0}$ est violée. Dans le modèle linéaire général :

$$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i \quad \text{avec } E[u_i] = 0$$

ce biais peut être formalisé à partir de l'équation de l'estimateur MCO :

$$\hat{\boldsymbol{\alpha}}_{MCO,N} = \boldsymbol{\alpha}_0 + \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{x}_i u_i$$

L'application de la loi des grands nombres aux suites convergeant en probabilité permet de montrer que :

$$\text{plim}_{N \to +\infty} \hat{\boldsymbol{\alpha}}_{MCO,N} = \boldsymbol{\alpha}_0 + [E(\mathbf{x}_i \mathbf{x}_i')]^{-1} E[\mathbf{x}_i u_i]$$

Le terme $[E(\mathbf{x}_i \mathbf{x}_i')]^{-1} E[\mathbf{x}_i u_i]$ constitue le biais asymptotique d'endogénéité de $\hat{\boldsymbol{\alpha}}_{MCO,N}$ pour $\boldsymbol{\alpha}_0$ si $E[\mathbf{x}_i u_i] \neq \mathbf{0}$.

Une propriété cruciale de ce biais est sa nature systémique : même si une seule variable explicative est endogène, tous les coefficients du modèle sont potentiellement biaisés. Considérons le cas où seul le K-ième élément $x_{K,i}$ est endogène :

$$E[x_{k,i} u_i] = 0 \text{ pour } k = 1, ..., K-1$$
$$E[x_{K,i} u_i] \neq 0$$

Dans le modèle partitionné :

$$y_i = \boldsymbol{\alpha}_{-K,0}' \mathbf{x}_{-K,i} + \alpha_{K,0} x_{K,i} + u_i \quad \text{avec } E[u_i] = E[u_i | \mathbf{x}_{-K,i}] = 0$$

le biais de l'estimateur MCO $\hat{\boldsymbol{\alpha}}_{MCO,N} = (\hat{\boldsymbol{\alpha}}_{-K,N}^{MCO}, \hat{\alpha}_{K,N}^{MCO})'$ de $\boldsymbol{\alpha}_0 = (\boldsymbol{\alpha}_{-K,0}, \alpha_{K,0})'$ s'exprime par :

$$\text{plim}_{N \to +\infty} \hat{\boldsymbol{\alpha}}_{MCO,N} = \boldsymbol{\alpha}_0 + \begin{pmatrix} \boldsymbol{\gamma} \\ 1 \end{pmatrix} \times \text{Cov}(x_{K,i}, u_i) \times \frac{1}{V(e_{K,i})}$$

où $e_{K,i} = x_{K,i} - EL(x_{K,i} | \mathbf{x}_{-K,i})$ représente la partie de $x_{K,i}$ non expliquée par $\mathbf{x}_{-K,i}$, et $\boldsymbol{\gamma} = E[\mathbf{x}_{-K,i} e_{K,i}]/V(e_{K,i})$.

Ainsi, l'endogénéité d'une seule variable "contamine" l'ensemble des estimateurs du modèle. Seront biaisés : le coefficient de la variable endogène elle-même, les coefficients des variables exogènes corrélées avec la variable endogène, et la constante du modèle.

## La notion de variable instrumentale

Face aux limitations des MCO en présence d'endogénéité, la méthode des variables instrumentales offre une approche alternative pour l'identification causale. Cette méthode repose sur l'exploitation de sources de variation exogène pour isoler les effets causaux d'intérêt.

### Intuition fondamentale

L'intuition sous-jacente à l'utilisation des variables instrumentales part du constat suivant : lorsque $\tilde{x}_i$ est endogène, la covariance $\text{Cov}(\tilde{x}_i, y_i)$ ne permet pas d'identifier $b_0$ car :

$$\text{Cov}(\tilde{x}_i, y_i) = b_0 V(\tilde{x}_i) + \text{Cov}(\tilde{x}_i, u_i)$$

Cette équation contient deux inconnues : le paramètre d'intérêt $b_0$ et le terme de biais $\text{Cov}(\tilde{x}_i, u_i)$.

La stratégie instrumentale consiste à identifier une variable $\tilde{z}_i$ telle que $\text{Cov}(\tilde{z}_i, y_i)$ fournisse une équation permettant d'identifier $b_0$. Dans le modèle :

$$y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$$

nous avons :

$$\text{Cov}(\tilde{z}_i, y_i) = \text{Cov}(\tilde{z}_i, \alpha_0 + b_0 \tilde{x}_i + u_i) = b_0 \text{Cov}(\tilde{z}_i, \tilde{x}_i) + \text{Cov}(\tilde{z}_i, u_i)$$

Pour que $\tilde{z}_i$ soit utile à l'identification de $b_0$, deux conditions doivent être satisfaites :

**Condition d'exogénéité** : $\text{Cov}(\tilde{z}_i, u_i) = 0$, signifiant que $\tilde{z}_i$ est exogène par rapport au terme d'erreur.

**Condition de pertinence** : $\text{Cov}(\tilde{z}_i, \tilde{x}_i) \neq 0$, impliquant que $\tilde{z}_i$ est linéairement liée à la variable explicative endogène.

Sous ces conditions, nous obtenons :

$$b_0 = \frac{\text{Cov}(\tilde{z}_i, y_i)}{\text{Cov}(\tilde{z}_i, \tilde{x}_i)}$$

Cette relation permet de construire un estimateur convergent de $b_0$ :

$$\hat{b}_{N} = \frac{\sum_{i=1}^N (z_i - \bar{z}_N)(y_i - \bar{y}_N)}{\sum_{i=1}^N (z_i - \bar{z}_N)(x_i - \bar{x}_N)} \xrightarrow{p} b_0$$

### Définition formelle et conditions de validité

Une variable instrumentale $\tilde{z}_i$ de $\tilde{x}_i$ dans le modèle $y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$ avec $E[u_i] = 0$ est valide si et seulement si :

1. **Condition d'exogénéité** : $\text{Cov}(\tilde{z}_i, u_i) = 0$, garantissant que $\tilde{z}_i$ est exogène par rapport au terme d'erreur.

2. **Condition de pertinence** : $\text{Cov}(\tilde{z}_i, \tilde{x}_i) \neq 0$, assurant que $\tilde{z}_i$ est linéairement liée à la variable explicative endogène.

Ces conditions doivent être évaluées tant par l'analyse théorique du processus générateur des données que par des tests empiriques appropriés.

L'identification par variables instrumentales repose sur le principe que $\tilde{z}_i$ n'influence $y_i$ qu'indirectement, par son effet sur $\tilde{x}_i$. Cette **relation d'exclusion** implique que la variable instrumentale n'apparaît pas directement dans l'équation structurelle d'intérêt, mais seulement dans l'équation de la variable explicative endogène.

Le schéma causal peut être représenté par : $\tilde{z}_i \to \tilde{x}_i \to y_i$, où l'effet de $\tilde{z}_i$ sur $y_i$ "transite" exclusivement via $\tilde{x}_i$.

Les variations de $\tilde{z}_i$ sont qualifiées de **variations exogènes** car elles ne sont pas corrélées avec $u_i$. Ce sont précisément ces variations exogènes qui permettent l'identification de $b_0$, indépendamment de la nature causale ou simplement corrélationnelle de la relation entre $\tilde{z}_i$ et $\tilde{x}_i$.

### Exemples de variables instrumentales

L'application pratique de la méthode des variables instrumentales nécessite l'identification de sources de variation exogène pertinentes pour chaque contexte d'étude.

**Effet de la taille des classes sur les résultats scolaires**

Pour instrumenter $\text{tailclas}_i$, Angrist et Lavy proposent d'utiliser $\text{tailclas\_moy}_i$, la taille moyenne des classes de CE1 dans l'école de l'élève $i$.

Cette variable satisfait la condition d'exogénéité car elle dépend principalement du nombre total d'élèves de CE1 dans l'école et de la règle institutionnelle limitant la taille maximale des classes à 25 élèves. Ces facteurs sont largement indépendants des caractéristiques individuelles inobservées des élèves.

La condition de pertinence est vérifiée empiriquement : la taille moyenne des classes dans l'école est fortement corrélée avec la taille de la classe spécifique de chaque élève, tout en présentant une variation suffisante pour l'identification.

Les résultats obtenus par Angrist et Lavy (1999) et Piketty (2004) révèlent que $\hat{b}_{1,N} < 0$, contrairement aux estimations MCO qui donnent $\hat{b}_{1,N}^{MCO} \approx 0$. Cette différence confirme l'importance de traiter l'endogénéité pour révéler l'effet réellement négatif de la taille des classes.

**Effet de la maternité sur le salaire des femmes**

Angrist et Evans se concentrent sur l'effet marginal du troisième enfant en définissant :

$$\text{trois\_enf}_i = \begin{cases} 1 & \text{si la femme } i \text{ a 3 enfants ou plus} \\ 0 & \text{si la femme } i \text{ a exactement 2 enfants} \end{cases}$$

Leur instrument $\text{meme\_sexe}_i$ prend la valeur 1 si les deux premiers enfants ont le même sexe, et 0 sinon.

L'exogénéité de cet instrument repose sur le caractère aléatoire de la détermination du sexe des enfants. La pertinence provient du fait que les parents dont les deux premiers enfants sont de même sexe ont une probabilité significativement plus élevée d'avoir un troisième enfant, reflétant une préférence pour la diversité des sexes.

Cette stratégie d'identification révèle un effet négatif significatif du troisième enfant sur le salaire maternel, masqué dans les estimations MCO par les biais de simultanéité.

**Traitement des erreurs de mesure**

Dans le contexte des erreurs de mesure, une approche instrumentale efficace consiste à utiliser une **mesure alternative** de la même variable sous-jacente. Si $x_i^e = \tilde{x}_i + e_i$ représente la première mesure et $z_i = \tilde{x}_i + \varepsilon_i$ une seconde mesure, alors $z_i$ constitue un instrument valide pour $x_i^e$ sous les conditions :

- $\text{Cov}(e_i, \varepsilon_i) = 0$ (indépendance des erreurs de mesure)
- $\text{Cov}(\varepsilon_i, u_i) = 0$ (exogénéité de la seconde erreur de mesure)

Cette technique de la "double-proxy" permet de surmonter le biais d'atténuation en exploitant la corrélation entre les deux mesures imparfaites de la même variable latente.

## L'estimateur des variables instrumentales

La généralisation de l'approche instrumentale à des modèles multivariés nécessite le développement d'un cadre méthodologique rigoureux pour la construction et l'analyse des propriétés de l'estimateur des variables instrumentales.

### Construction générale

Considérons le modèle linéaire général :

$$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i \quad \text{avec } E[u_i] = 0$$

où certaines variables explicatives sont potentiellement endogènes. Partitionnons le vecteur $\mathbf{x}_i$ en :

$$\mathbf{x}_i = \begin{pmatrix} \mathbf{x}_i^x \\ \mathbf{x}_i^e \end{pmatrix}$$

où $\mathbf{x}_i^x$ contient les $M$ variables exogènes (incluant la constante) et $\mathbf{x}_i^e$ les $(K-M)$ variables endogènes.

Pour chaque variable endogène, nous supposons disposer d'une variable instrumentale. Le vecteur d'instruments $\mathbf{z}_i$ se construit par :

$$\mathbf{z}_i = \begin{pmatrix} \mathbf{x}_i^x \\ \mathbf{z}_i^e \end{pmatrix}$$

où $\mathbf{z}_i^e$ représente le vecteur des variables instrumentales pour $\mathbf{x}_i^e$.

Une variable $z_{k,i}$ est un instrument valide pour $x_{k,i}$ dans le modèle linéaire si :

1. **Condition d'exogénéité** : $\text{Cov}(z_{k,i}, u_i) = 0$
2. **Condition de pertinence** : $z_{k,i}$ est "suffisamment" liée à $x_{k,i}$

La condition de pertinence sera formalisée ultérieurement en termes de conditions de rang pour assurer l'identification du modèle.

### Conditions d'orthogonalité et méthode des moments

L'estimateur des variables instrumentales se fonde sur un système de **conditions d'orthogonalité** dérivées de l'exogénéité du vecteur d'instruments. Le modèle peut s'écrire sous la forme :

$$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i \quad \text{avec } E[u_i | \mathbf{z}_i] = 0$$

Cette condition d'exogénéité conditionelle implique la condition de moment :

$$E[\mathbf{z}_i u_i] = E[\mathbf{z}_i (y_i - \boldsymbol{\alpha}_0' \mathbf{x}_i)] = \mathbf{0}$$

Le vecteur $\mathbf{z}_i$ est parfois appelé **vecteur d'instruments** ou **ensemble d'information du modèle**, car il contient toutes les variables utilisées pour construire des conditions de moment estimantes.

L'application du **principe d'analogie** de la méthode des moments définit l'estimateur des variables instrumentales $\hat{\boldsymbol{\alpha}}_{VI,N}$ comme la solution du système :

$$\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i (y_i - \hat{\boldsymbol{\alpha}}_{VI,N}' \mathbf{x}_i) = \mathbf{0}$$

Ce système de $K$ équations à $K$ inconnues admet une solution explicite sous la condition d'identification :

$$\text{rang}[E(\mathbf{z}_i \mathbf{x}_i')] = K = \dim(\mathbf{x}_i)$$

La résolution du système donne :

$$\hat{\boldsymbol{\alpha}}_{VI,N} = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i y_i$$

### Définition formelle

**Définition** : Dans le modèle à variables instrumentales $y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i$ avec $E[u_i | \mathbf{z}_i] = 0$, l'**estimateur des variables instrumentales** de $\boldsymbol{\alpha}_0$ est défini par :

$$\hat{\boldsymbol{\alpha}}_{VI,N} = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i y_i$$

L'estimateur des VI est également connu sous le nom d'**estimateur des moindres carrés indirects** (MCI), soulignant le fait que l'identification se fait indirectement par l'intermédiaire des variables instrumentales plutôt que directement par la corrélation entre variables explicatives et variable dépendante.

## Propriétés asymptotiques de l'estimateur des variables instrumentales

L'analyse des propriétés statistiques de l'estimateur des variables instrumentales nécessite l'établissement de conditions régulières et l'application des théorèmes limites classiques.

### Convergence

**Propriété (Convergence de l'estimateur VI)** : Soit $\{(y_i, \mathbf{x}_i, \mathbf{z}_i) ; i = 1, 2, ..., N\}$ un échantillon de variables aléatoires tel que :

$$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i \quad \text{avec } E[u_i | \mathbf{z}_i] = 0$$

L'estimateur des VI de $\boldsymbol{\alpha}_0$ :

$$\hat{\boldsymbol{\alpha}}_{VI,N} = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i y_i$$

1. **existe** avec une probabilité approchant 1 quand $N \to +\infty$
2. **est convergent** : $\hat{\boldsymbol{\alpha}}_{VI,N} \xrightarrow{p} \boldsymbol{\alpha}_0$ quand $N \to +\infty$

**Démonstration** : En substituant l'expression du modèle $y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i$ dans la définition de l'estimateur :

$$\hat{\boldsymbol{\alpha}}_{VI,N} = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i (\boldsymbol{\alpha}_0' \mathbf{x}_i + u_i)$$

$$= \boldsymbol{\alpha}_0 + \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i u_i$$

Par la loi des grands nombres :

$$\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i' \xrightarrow{p} E[\mathbf{z}_i \mathbf{x}_i']$$

$$\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i u_i \xrightarrow{p} E[\mathbf{z}_i u_i] = \mathbf{0}$$

La dernière égalité utilise la condition d'exogénéité $E[u_i | \mathbf{z}_i] = 0$. Par conséquent :

$\left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i u_i \xrightarrow{p} [E(\mathbf{z}_i \mathbf{x}_i')]^{-1} \times \mathbf{0} = \mathbf{0}$

D'où finalement : $\hat{\boldsymbol{\alpha}}_{VI,N} \xrightarrow{p} \boldsymbol{\alpha}_0 + \mathbf{0} = \boldsymbol{\alpha}_0$.

### Normalité asymptotique

**Propriété (Normalité asymptotique de l'estimateur VI)** : Sous les conditions de régularité appropriées, l'estimateur des variables instrumentales vérifie :

$\sqrt{N}(\hat{\boldsymbol{\alpha}}_{VI,N} - \boldsymbol{\alpha}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_0)$

où la matrice de variance-covariance asymptotique est donnée par :

$\boldsymbol{\Sigma}_0 = [E(\mathbf{z}_i \mathbf{x}_i')]^{-1} E[u_i^2 \mathbf{z}_i \mathbf{z}_i'] [E(\mathbf{z}_i \mathbf{x}_i')]^{-1}$

**Démonstration** : À partir de la décomposition établie précédemment :

$\sqrt{N}(\hat{\boldsymbol{\alpha}}_{VI,N} - \boldsymbol{\alpha}_0) = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{\sqrt{N}}\sum_{i=1}^N \mathbf{z}_i u_i$

La loi des grands nombres assure que :

$\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i' \xrightarrow{p} E[\mathbf{z}_i \mathbf{x}_i']$

Le théorème central limite implique que :

$\frac{1}{\sqrt{N}}\sum_{i=1}^N \mathbf{z}_i u_i \xrightarrow{d} \mathcal{N}(\mathbf{0}, E[u_i^2 \mathbf{z}_i \mathbf{z}_i'])$

En utilisant $E[u_i | \mathbf{z}_i] = 0$, nous avons $E[\mathbf{z}_i u_i] = \mathbf{0}$. La combinaison de ces résultats par le théorème de Slutsky donne :

$\sqrt{N}(\hat{\boldsymbol{\alpha}}_{VI,N} - \boldsymbol{\alpha}_0) \xrightarrow{d} [E(\mathbf{z}_i \mathbf{x}_i')]^{-1} \times \mathcal{N}(\mathbf{0}, E[u_i^2 \mathbf{z}_i \mathbf{z}_i'])$

ce qui établit la normalité asymptotique avec la matrice de variance-covariance annoncée.

### Estimation de la matrice de variance-covariance

L'inférence statistique nécessite un estimateur convergent de la matrice de variance-covariance $\boldsymbol{\Sigma}_0$. Nous distinguons deux cas selon les hypothèses sur la structure des erreurs.

**Cas homoscédastique**

Sous l'hypothèse d'homoscédasticité conditionnelle $E[u_i^2 | \mathbf{z}_i] = \sigma_0^2$, la loi des espérances itérées donne :

$E[u_i^2 \mathbf{z}_i \mathbf{z}_i'] = E[E[u_i^2 | \mathbf{z}_i] \mathbf{z}_i \mathbf{z}_i'] = \sigma_0^2 E[\mathbf{z}_i \mathbf{z}_i']$

La matrice de variance-covariance se simplifie en :

$\boldsymbol{\Sigma}_0 = \sigma_0^2 [E(\mathbf{z}_i \mathbf{x}_i')]^{-1} E[\mathbf{z}_i \mathbf{z}_i'] [E(\mathbf{z}_i \mathbf{x}_i')]^{-1}$

L'estimateur convergent s'obtient par substitution des moyennes empiriques et du paramètre inconnu par ses estimateurs convergents :

$\hat{\boldsymbol{\Sigma}}_N = \hat{\sigma}_N^2 \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{z}_i' \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1}$

où $\hat{\sigma}_N^2 = \frac{1}{N}\sum_{i=1}^N (y_i - \hat{\boldsymbol{\alpha}}_{VI,N}' \mathbf{x}_i)^2$ constitue un estimateur convergent de $\sigma_0^2$.

**Cas hétéroscédastique**

En l'absence d'hypothèse d'homoscédasticité, l'estimateur robuste de White s'applique directement :

$\hat{\boldsymbol{\Sigma}}_N = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N (y_i - \hat{\boldsymbol{\alpha}}_{VI,N}' \mathbf{x}_i)^2 \mathbf{z}_i \mathbf{z}_i' \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \mathbf{x}_i'\right)^{-1}$

Cet estimateur demeure convergent sous des conditions de régularité générales, sans nécessiter d'hypothèses spécifiques sur la structure de l'hétéroscédasticité.

## L'estimateur des doubles moindres carrés

L'estimateur des doubles moindres carrés (2MC) représente une interprétation alternative de l'estimateur des variables instrumentales qui met en évidence la structure en deux étapes de la procédure d'estimation. Cette approche facilite l'intuition économétrique et fournit un cadre naturel pour l'analyse des conditions d'identification.

### Construction et interprétation

L'estimateur 2MC procède conceptuellement en deux étapes, d'où son nom. Considérons le modèle structurel :

$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i$

où le vecteur $\mathbf{x}_i$ contient à la fois des variables exogènes $\mathbf{x}_i^x$ et des variables endogènes $\mathbf{x}_i^e$.

**Première étape** : Projection des variables explicatives sur l'espace engendré par les instruments. Pour chaque variable explicative $x_{k,i}$, nous estimons la régression auxiliaire :

$x_{k,i} = \boldsymbol{\pi}_k' \mathbf{z}_i + v_{k,i}$

où $\mathbf{z}_i$ représente le vecteur d'instruments (incluant les variables exogènes). Cette étape génère les valeurs prédites $\hat{x}_{k,i} = \hat{\boldsymbol{\pi}}_k' \mathbf{z}_i$ pour chaque variable explicative.

**Deuxième étape** : Régression de la variable dépendante sur les valeurs prédites de l'étape précédente :

$y_i = \boldsymbol{\alpha}_0' \hat{\mathbf{x}}_i + \eta_i$

où $\hat{\mathbf{x}}_i$ désigne le vecteur des valeurs prédites de toutes les variables explicatives.

Cette procédure en deux étapes produit exactement le même estimateur que la formule directe des variables instrumentales. En effet, nous pouvons montrer que :

$\hat{\boldsymbol{\alpha}}_{2MC,N} = \left(\frac{1}{N}\sum_{i=1}^N \hat{\mathbf{x}}_i \mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \hat{\mathbf{x}}_i y_i = \hat{\boldsymbol{\alpha}}_{VI,N}$

### Intuition économétrique

L'approche 2MC révèle l'intuition fondamentale de la méthode des variables instrumentales. La première étape "nettoie" les variables explicatives de leur corrélation avec le terme d'erreur en ne conservant que la variation expliquée par les instruments exogènes. La deuxième étape utilise cette variation purifiée pour estimer les paramètres structurels.

Cette interprétation géométrique montre que l'estimateur VI utilise uniquement la composante des variables explicatives qui est orthogonale au terme d'erreur, éliminant ainsi le biais d'endogénéité au prix d'une perte d'efficacité lorsque les instruments ne sont pas parfaitement corrélés avec les variables explicatives.

## Conditions d'identification et choix des variables instrumentales

L'identification des paramètres structurels par la méthode des variables instrumentales nécessite la vérification de conditions algébriques précises et le choix judicieux des instruments. Cette section développe les conditions nécessaires et suffisantes pour l'identification, ainsi que les critères pratiques de sélection des variables instrumentales.

### Conditions de rang et d'ordre

L'identification du vecteur de paramètres $\boldsymbol{\alpha}_0$ dans le modèle :

$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i \quad \text{avec } E[u_i | \mathbf{z}_i] = 0$

requiert que le système de conditions d'orthogonalité $E[\mathbf{z}_i (y_i - \boldsymbol{\alpha}_0' \mathbf{x}_i)] = \mathbf{0}$ admette une solution unique.

**Condition d'ordre** : Le nombre d'instruments doit être au moins égal au nombre de paramètres à estimer. Formellement :

$\dim(\mathbf{z}_i) \geq \dim(\mathbf{x}_i) = K$

Cette condition nécessaire assure que nous disposons d'au moins autant d'équations que d'inconnues dans le système de conditions d'orthogonalité.

**Condition de rang** : La matrice $E[\mathbf{z}_i \mathbf{x}_i']$ doit être de rang plein. Formellement :

$\text{rang}[E(\mathbf{z}_i \mathbf{x}_i')] = K$

Cette condition assure l'inversibilité de la matrice $E[\mathbf{z}_i \mathbf{x}_i']$ et donc l'existence d'une solution unique au système d'identification.

Lorsque $\dim(\mathbf{z}_i) = \dim(\mathbf{x}_i) = K$, le modèle est dit **exactement identifié**. Dans ce cas, la condition de rang équivaut à la non-singularité de la matrice carrée $E[\mathbf{z}_i \mathbf{x}_i']$.

Lorsque $\dim(\mathbf{z}_i) > \dim(\mathbf{x}_i) = K$, le modèle est **sur-identifié**. Cette situation offre des possibilités de tests de validité des restrictions sur-identifiantes et généralement une meilleure efficacité asymptotique des estimateurs.

### Pertinence des instruments et instruments faibles

La condition de rang, bien qu'algébriquement nécessaire, ne capture pas pleinement les enjeux statistiques liés à la qualité des instruments. La **pertinence des instruments** constitue un aspect crucial pour les propriétés en échantillon fini de l'estimateur VI.

Un instrument est qualifié de **faible** lorsque sa corrélation avec la variable explicative endogène est statistiquement significative mais numériquement faible. Cette situation engendre plusieurs problèmes :

1. **Biais en échantillon fini** : Même si l'estimateur VI est asymptotiquement non biaisé, il peut présenter un biais substantiel en échantillon fini lorsque les instruments sont faibles.

2. **Variance élevée** : La variance de l'estimateur VI est inversement proportionnelle à la force de la corrélation entre instruments et variables explicatives. Des instruments faibles conduisent à des estimateurs très imprécis.

3. **Distorsion des tests** : Les tests de Student standard peuvent présenter des distorsions de taille importantes en présence d'instruments faibles.

### Critères de choix des instruments

Le choix optimal des variables instrumentales nécessite un équilibre délicat entre plusieurs critères parfois conflictuels.

**Exogénéité théorique** : L'instrument ne doit pas être corrélé avec les facteurs inobservés qui affectent la variable dépendante. Cette condition, généralement non testable, doit être établie par des arguments économiques, institutionnels ou expérimentaux.

**Pertinence empirique** : L'instrument doit présenter une corrélation suffisamment forte avec la variable explicative endogène. Cette condition se vérifie empiriquement par l'examen des statistiques de Fisher dans les régressions auxiliaires de première étape.

**Indépendance conditionnelle** : Idéalement, l'instrument ne devrait être corrélé avec la variable explicative endogène qu'à travers le mécanisme d'intérêt, et non par des canaux alternatifs qui violeraient la restriction d'exclusion.

**Monotonie** : Dans les modèles d'effets de traitement, la condition de monotonie requiert que l'instrument affecte la probabilité de traitement dans la même direction pour tous les individus.

### Tests de validité des instruments

Plusieurs tests statistiques permettent d'évaluer empiriquement la qualité des instruments, bien que certaines conditions ne soient pas directement testables.

**Test de pertinence des instruments** : La pertinence se teste par l'examen des statistiques de Fisher dans les régressions auxiliaires de première étape. Une règle empirique courante suggère que la statistique F doit excéder 10 pour écarter les problèmes d'instruments faibles.

**Test de sur-identification de Sargan-Hansen** : Lorsque le modèle est sur-identifié, ce test examine la compatibilité entre les différentes conditions d'orthogonalité. Sous l'hypothèse nulle de validité des instruments, la statistique :

$J_N = N \times \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \hat{u}_i\right)' \left[\frac{1}{N}\sum_{i=1}^N \hat{u}_i^2 \mathbf{z}_i \mathbf{z}_i'\right]^{-1} \left(\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \hat{u}_i\right)$

suit asymptotiquement une distribution du chi-deux à $(\dim(\mathbf{z}_i) - \dim(\mathbf{x}_i))$ degrés de liberté.

**Test d'exogénéité** : Ce test compare les estimateurs VI et MCO pour déterminer si le traitement de l'endogénéité est nécessaire. Sous l'hypothèse nulle d'exogénéité, les deux estimateurs sont convergents, mais l'estimateur MCO est plus efficace.

## Fonctions de contrôle et test d'exogénéité

Les fonctions de contrôle constituent une approche alternative à la méthode des variables instrumentales pour traiter l'endogénéité. Cette méthode, également connue sous le nom de **régression augmentée**, repose sur l'inclusion explicite de termes de correction du biais d'endogénéité dans l'équation structurelle.

### Principe des fonctions de contrôle

L'intuition fondamentale des fonctions de contrôle consiste à modéliser explicitement la source d'endogénéité pour ensuite la contrôler directement dans l'estimation. Considérons le modèle structurel :

$y_i = \boldsymbol{\alpha}_0' \mathbf{x}_i + u_i$

où certaines variables de $\mathbf{x}_i$ sont endogènes. L'endogénéité provient de la corrélation $E[\mathbf{x}_i u_i] \neq \mathbf{0}$.

L'approche par fonctions de contrôle suppose que cette corrélation peut être modélisée par une fonction des instruments disponibles. Plus précisément, si nous disposons d'instruments $\mathbf{z}_i$, nous pouvons écrire :

$E[u_i | \mathbf{x}_i, \mathbf{z}_i] = E[u_i | \mathbf{x}_i - E[\mathbf{x}_i | \mathbf{z}_i]]$

Cette condition, appelée **condition de moyenne conditionnelle**, stipule que la corrélation entre $u_i$ et $\mathbf{x}_i$ s'explique entièrement par la déviation de $\mathbf{x}_i$ par rapport à sa prédiction basée sur les instruments.

### Procédure d'estimation

La méthode des fonctions de contrôle procède en deux étapes similaires à l'approche 2MC, mais avec une interprétation différente :

**Première étape** : Estimation des équations de forme réduite pour les variables explicatives endogènes :

$\mathbf{x}_i^e = \boldsymbol{\Pi}' \mathbf{z}_i + \mathbf{v}_i$

Cette étape génère les résidus $\hat{\mathbf{v}}_i = \mathbf{x}_i^e - \hat{\boldsymbol{\Pi}}' \mathbf{z}_i$ qui constituent les **fonctions de contrôle**.

**Deuxième étape** : Estimation de l'équation structurelle augmentée par les fonctions de contrôle :

$y_i = \boldsymbol{\alpha}' \mathbf{x}_i + \boldsymbol{\lambda}' \hat{\mathbf{v}}_i + \varepsilon_i$

Sous des conditions de régularité, l'estimateur MCO de cette équation augmentée est convergent et asymptotiquement normal.

### Test d'exogénéité par régression augmentée

L'approche par fonctions de contrôle fournit un cadre naturel pour tester l'hypothèse d'exogénéité des variables explicatives. Le **test d'exogénéité par régression augmentée** examine la significativité statistique des coefficients des fonctions de contrôle dans l'équation structurelle augmentée.

L'hypothèse nulle d'exogénéité s'exprime par :

$H_0 : \boldsymbol{\lambda} = \mathbf{0}$

Sous cette hypothèse, les fonctions de contrôle ne devraient pas avoir de pouvoir explicatif dans l'équation structurelle, et l'estimateur MCO standard serait approprié.

Le test se réalise par un test de Fisher standard sur la significativité jointe des coefficients des fonctions de contrôle :

$F = \frac{(SCR_0 - SCR_1)/q}{SCR_1/(N-K)} \sim F_{q,N-K}$

où $SCR_0$ et $SCR_1$ désignent respectivement les sommes des carrés des résidus sous l'hypothèse nulle (modèle sans fonctions de contrôle) et alternative (modèle avec fonctions de contrôle), et $q$ représente le nombre de fonctions de contrôle.

Ce test présente l'avantage d'être applicable même lorsque les instruments sont faibles, contrairement à certains tests alternatifs basés sur la comparaison des estimateurs VI et MCO.

## Variables de contrôle et hétérogénéité non observée

Les variables de contrôle représentent une stratégie complémentaire aux variables instrumentales pour traiter l'endogénéité causée par l'omission de variables pertinentes. Cette approche, particulièrement adaptée aux données de panel et aux études longitudinales, exploite les variations temporelles ou cross-sectionnelles pour identifier les effets causaux.

### Principe fondamental

L'approche par variables de contrôle part de la reconnaissance que l'endogénéité résulte souvent de facteurs inobservés qui affectent simultanément les variables explicatives et la variable dépendante. Plutôt que de chercher des instruments externes, cette méthode tente de contrôler directement ces facteurs par l'inclusion de variables observables appropriées ou l'exploitation de structures particulières des données.

Considérons le modèle général :

$y_i = \boldsymbol{\alpha}' \mathbf{x}_i + \boldsymbol{\beta}' \mathbf{w}_i + u_i$

où $\mathbf{x}_i$ contient les variables d'intérêt potentiellement endogènes et $\mathbf{w}_i$ représente les variables de contrôle. L'objectif est de choisir $\mathbf{w}_i$ de manière à assurer $E[u_i | \mathbf{x}_i, \mathbf{w}_i] = 0$.

### Applications aux données de panel

Dans le contexte des données de panel, la décomposition du terme d'erreur permet de distinguer les effets fixes individuels des chocs transitoires :

$u_{it} = \mu_i + \varepsilon_{it}$

où $\mu_i$ capture l'hétérogénéité non observée invariante dans le temps (talent individuel, préférences stables) et $\varepsilon_{it}$ représente les chocs idiosyncratiques.

**Estimateur à effets fixes** : Cette approche élimine les effets fixes individuels par la transformation en déviations par rapport aux moyennes individuelles :

$y_{it} - \bar{y}_i = \boldsymbol{\alpha}' (\mathbf{x}_{it} - \bar{\mathbf{x}}_i) + (\varepsilon_{it} - \bar{\varepsilon}_i)$

L'estimateur MCO appliqué aux données transformées est convergent sous la condition $E[\varepsilon_{it} | \mathbf{x}_{it}, \mu_i] = 0$.

**Estimateur en premières différences** : Alternativement, la différenciation première élimine les effets fixes :

$\Delta y_{it} = \boldsymbol{\alpha}' \Delta \mathbf{x}_{it} + \Delta \varepsilon_{it}$

Cette approche est particulièrement appropriée lorsque les erreurs $\varepsilon_{it}$ suivent une marche aléatoire.

### Stratégies d'identification causale

Les variables de contrôle s'intègrent dans des stratégies d'identification causale plus larges qui exploitent des sources de variation exogène ou quasi-expérimentale.

**Expériences naturelles** : L'identification repose sur des événements exogènes qui affectent différentiellement les unités d'observation. Les variables de contrôle permettent d'isoler l'effet de ces chocs en contrôlant pour les caractéristiques observables des unités.

**Discontinuités de régression** : Cette approche exploite les discontinuités arbitraires dans les règles d'attribution des traitements. Les variables de contrôle, typiquement des fonctions flexibles de la variable de seuil, permettent de contrôler les tendances sous-jacentes.

**Différences de différences** : Cette méthode compare l'évolution des groupes traités et de contrôle avant et après l'intervention. Les variables de contrôle temporelles et cross-sectionnelles permettent de contrôler les tendances différentielles préexistantes.

### Limites et précautions

L'efficacité de l'approche par variables de contrôle dépend crucialement de la capacité à identifier et mesurer les sources pertinentes d'hétérogénéité non observée. Plusieurs limites doivent être considérées :

**Problème de sélection sur les inobservables** : Les variables de contrôle ne peuvent traiter que l'endogénéité provenant de facteurs observables ou proxifiables par des variables disponibles.

**Malédiction de la dimensionnalité** : L'inclusion d'un grand nombre de variables de contrôle peut conduire à des problèmes de multicolinéarité et de sur-ajustement, particulièrement dans des échantillons de taille limitée.

**Contrôle excessif** : L'inclusion de variables qui sont elles-mêmes affectées par le traitement d'intérêt peut introduire un biais de variable intermédiaire (bad controls).

L'arbitrage entre variables instrumentales et variables de contrôle dépend de la nature spécifique du problème d'identification et de la disponibilité des données. Les variables instrumentales offrent une identification plus robuste lorsque des instruments valides sont disponibles, tandis que les variables de contrôle peuvent être plus efficaces lorsque les sources d'hétérogénéité non observée sont bien comprises et partiellement observables.

## Estimation de la variance asymptotique de l'estimateur des variables instrumentales

La variance asymptotique de l'estimateur des variables instrumentales $\hat{a}_{N}^{VI}$ dans un modèle à VI peut être estimée selon deux approches principales, selon que l'on suppose l'homoscédasticité ou l'hétéroscédasticité des termes d'erreur.

Dans le cas homoscédastique où $V[u_i|\mathbf{z}_i] = \sigma_0^2$, la variance asymptotique $\Sigma_0$ peut être estimée par $\hat{\Sigma}_N$ définie comme :

$\hat{\Sigma}_N \equiv \hat{\sigma}_N^2 \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{z}_i'\right) \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'\right)^{-1}$

Pour le cas général admettant l'hétéroscédasticité, l'estimateur robuste dit "de White" $\hat{\Sigma}_N^W$ s'écrit :

$\hat{\Sigma}_N^W \equiv \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{z}_i'\hat{u}_i^2\right) \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'\right)^{-1}$

où $\hat{\sigma}_N^2 \equiv \frac{1}{N-K}\sum_{i=1}^{N} \hat{u}_i^2$ avec $\hat{u}_i \equiv y_i - \mathbf{x}_i'\hat{\mathbf{a}}_N^{VI}$ représentant le résidu d'estimation.

L'estimateur $\hat{\Sigma}_N^W$ présente l'avantage d'être robuste à l'hétéroscédasticité, c'est-à-dire qu'il fournit des estimations cohérentes de la variance asymptotique même lorsque la variance conditionnelle des termes d'erreur n'est pas constante.

# L'estimateur des doubles moindres carrés (2MC)

## Contexte et motivation

L'estimateur des variables instrumentales présente une limitation importante lorsque plusieurs variables instrumentales sont disponibles pour instrumenter une seule variable explicative endogène, ou lorsque plusieurs variables explicatives sont simultanément endogènes. Dans le modèle linéaire général à variables instrumentales :

$$y_i = \boldsymbol{\alpha}_0'\mathbf{x}_i + u_i \text{ avec } E[u_i|\mathbf{z}_i] = 0$$

nous pouvons décomposer les variables explicatives en deux sous-ensembles : les variables exogènes $\mathbf{x}_i^x$ (de dimension $M \times 1$) et les variables endogènes $\tilde{\mathbf{x}}_i^e$ (de dimension $(K-M) \times 1$), de sorte que $\mathbf{x}_i = [\mathbf{x}_i^x, \tilde{\mathbf{x}}_i^e]'$.

Lorsque nous cherchons à instrumenter une variable explicative endogène $\tilde{x}_{k,i}$ (avec $k > M$), nous recherchons des variables exogènes par rapport à $u_i$ qui soient corrélées à $\tilde{x}_{k,i}$. La technique de recherche de variables instrumentales consiste à identifier les variables qui permettraient de prédire au mieux $\tilde{x}_{k,i}$, sous la contrainte que ces variables explicatives doivent être exogènes dans le modèle d'intérêt.

## Construction du vecteur d'instruments et problème de sur-identification

Le vecteur des variables instrumentales $\mathbf{z}_i$ se compose des variables exogènes $\mathbf{x}_i^x$ et des variables instrumentales externes $\tilde{\mathbf{z}}_i^e$ nécessaires pour instrumenter $\tilde{\mathbf{x}}_i^e$ :

$$\mathbf{z}_i = [\mathbf{x}_i^x, \tilde{\mathbf{z}}_i^e]'$$

La dimension de ce vecteur d'instruments vérifie $\dim(\mathbf{z}_i) = L = M + (L-M)$, où $(L-M)$ représente le nombre de variables instrumentales externes disponibles.

La relation entre le nombre de variables explicatives et le nombre de variables instrumentales détermine le statut d'identification du modèle. Lorsque $L = K$, le modèle est dit juste-identifié et l'estimateur des variables instrumentales peut être appliqué directement. Cependant, lorsque $L > K$, le modèle est sur-identifié, ce qui signifie qu'il existe plus d'équations de moment que de paramètres à estimer.

Dans ce cas de sur-identification, la condition d'orthogonalité $E[\mathbf{z}_i(y_i - \mathbf{x}_i'\boldsymbol{\alpha}_0)] = \mathbf{0}$ définit un système de $L$ équations à $K$ inconnues. La contrepartie empirique :

$$\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i(y_i - \mathbf{x}_i'\boldsymbol{\alpha}) = \mathbf{0}$$

n'admet généralement pas de solution unique, créant un problème de résolution.

## Solution par projection linéaire

L'estimateur des doubles moindres carrés résout ce problème en utilisant une astuce qui permet de réduire la dimension du vecteur de variables instrumentales sans perdre d'information. L'idée centrale consiste à définir un vecteur d'instruments $\mathbf{w}_i(\mathbf{z}_i)$ de dimension $K$ tel que :

$$E[\mathbf{w}_i(\mathbf{z}_i)(y_i - \mathbf{x}_i'\boldsymbol{\alpha}_0)] = \mathbf{0}$$

Un vecteur d'instruments optimal doit satisfaire deux conditions : être exogène par rapport à $u_i$ et permettre de bien prédire $\mathbf{x}_i$. La projection linéaire de $\mathbf{x}_i$ sur $\mathbf{z}_i$, notée $E_L[\mathbf{x}_i|\mathbf{z}_i]$, constitue un excellent candidat pour $\mathbf{w}_i(\mathbf{z}_i)$ car elle représente la meilleure combinaison linéaire des éléments de $\mathbf{z}_i$ pour prédire $\mathbf{x}_i$ au sens de l'erreur quadratique moyenne.

## Projection linéaire et ses propriétés

La projection linéaire de $\mathbf{x}_i$ sur $\mathbf{z}_i$ est définie comme :

$$E_L[\mathbf{x}_i|\mathbf{z}_i] \equiv \boldsymbol{\gamma}'\mathbf{z}_i$$

où $\boldsymbol{\gamma} = \arg\min_{\mathbf{g}} E[(\mathbf{x}_i - \mathbf{g}'\mathbf{z}_i)^2]$.

Cette projection permet de décomposer $\mathbf{x}_i$ en deux composantes : la partie prédite par $\mathbf{z}_i$ et le résidu de cette prédiction :

$$\mathbf{x}_i = \boldsymbol{\gamma}'\mathbf{z}_i + \mathbf{e}_i$$

où $\mathbf{e}_i \equiv \mathbf{x}_i - \boldsymbol{\gamma}'\mathbf{z}_i$ vérifie par construction $E[\mathbf{z}_i\mathbf{e}_i'] = \mathbf{0}$.

Lorsque $E[\mathbf{z}_i\mathbf{z}_i']$ est inversible, le paramètre de projection s'exprime comme :

$$\boldsymbol{\gamma} = (E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i\mathbf{x}_i']$$

Un estimateur convergent de $\boldsymbol{\gamma}$ peut être obtenu par la méthode des moindres carrés ordinaires dans l'équation $\mathbf{x}_i = \boldsymbol{\gamma}'\mathbf{z}_i + \mathbf{e}_i$ :

$$\hat{\boldsymbol{\gamma}}_N = \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{z}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{x}_i'\right)$$

Il convient de noter que cette équation ne définit pas un modèle causal de $\mathbf{x}_i$ mais constitue simplement un outil mathématique de décomposition. La régression de $\mathbf{x}_i$ sur $\mathbf{z}_i$ fournit par construction le meilleur prédicteur linéaire au sens des moindres carrés, dans une logique d'ajustement sans référence à un modèle causal.

## Cas multivarié et matrice de projection

Dans le cas multivarié où $\mathbf{x}_i$ est un vecteur de dimension $K$, la projection linéaire s'écrit :

$$E_L[\mathbf{x}_i|\mathbf{z}_i] \equiv \boldsymbol{\Gamma}\mathbf{z}_i$$

où $\boldsymbol{\Gamma}$ est une matrice $K \times L$ dont chaque ligne correspond à la projection d'un élément de $\mathbf{x}_i$ sur $\mathbf{z}_i$. Cette matrice vérifie :

$$\boldsymbol{\Gamma} = E[\mathbf{x}_i\mathbf{z}_i'](E[\mathbf{z}_i\mathbf{z}_i'])^{-1}$$

L'estimateur empirique de cette matrice de projection est donné par :

$$\hat{\boldsymbol{\Gamma}}_N = \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'\right) \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{z}_i'\right)^{-1}$$

Cette approche présente plusieurs avantages : $E_L[\mathbf{x}_i|\mathbf{z}_i]$ a la même dimension $K$ que $\mathbf{x}_i$, est exogène car fonction de variables exogènes, est bien corrélée à $\mathbf{x}_i$ par construction comme son meilleur prédicteur linéaire, et il est facile de construire un estimateur convergent de cette projection.

## Définition et calcul de l'estimateur des doubles moindres carrés

En utilisant la projection linéaire $\mathbf{w}_i(\mathbf{z}_i) \equiv E_L[\mathbf{x}_i|\mathbf{z}_i] = \boldsymbol{\Gamma}\mathbf{z}_i$, la condition d'orthogonalité modifiée devient :

$$E[\boldsymbol{\Gamma}\mathbf{z}_i(y_i - \mathbf{x}_i'\boldsymbol{\alpha}_0)] = \mathbf{0}$$

soit, en développant :

$$E[\mathbf{x}_i\mathbf{z}_i'](E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i(y_i - \mathbf{x}_i'\boldsymbol{\alpha}_0)] = \mathbf{0}$$

L'application du principe d'analogie conduit à l'estimateur des doubles moindres carrés :

$$\hat{\boldsymbol{\alpha}}_N^{2MC} = \left(\frac{1}{N}\sum_{i=1}^{N} \hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i y_i\right)$$

En substituant l'expression de $\hat{\boldsymbol{\Gamma}}_N$, cet estimateur peut s'écrire sous la forme compacte :

$$\hat{\boldsymbol{\alpha}}_N^{2MC} = (\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{y}$$

où $\mathbf{X}$, $\mathbf{Z}$ et $\mathbf{y}$ désignent respectivement les matrices empilées des observations $\mathbf{x}_i$, $\mathbf{z}_i$ et $y_i$.

## Interprétation en termes de variables instrumentales et moindres carrés

L'estimateur des doubles moindres carrés admet deux interprétations équivalentes qui éclairent sa structure :

**Interprétation en termes de variables instrumentales** : L'estimateur $\hat{\boldsymbol{\alpha}}_N^{2MC}$ a la structure d'un estimateur des variables instrumentales avec un vecteur d'instruments "estimés" $\hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i$, qui constitue un estimateur convergent de $E_L[\mathbf{x}_i|\mathbf{z}_i]$.

**Interprétation en termes de moindres carrés** : L'estimateur peut également être vu comme un estimateur des moindres carrés ordinaires avec des variables explicatives "estimées" $\hat{\mathbf{w}}_i \equiv \hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i$, qui sont les estimateurs convergents des régresseurs $\mathbf{w}_i(\mathbf{z}_i) \equiv E_L[\mathbf{x}_i|\mathbf{z}_i]$.

## Technique des moindres carrés successifs

L'estimateur des doubles moindres carrés tire son nom de la propriété qu'il peut être calculé en deux étapes successives de moindres carrés ordinaires :

**Première étape** : Le calcul de $\hat{\boldsymbol{\Gamma}}_N$ correspond en fait au calcul d'estimateurs des moindres carrés pour chaque équation :

$$x_{k,i} = \boldsymbol{\gamma}_k'\mathbf{z}_i + e_{k,i}$$

pour $k = 1, \ldots, K$, où $\hat{\boldsymbol{\gamma}}_{k,N}^{MCO} = \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i\mathbf{z}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{z}_i x_{k,i}\right)$.

**Deuxième étape** : L'estimation finale s'obtient par :

$$\hat{\boldsymbol{\alpha}}_N^{2MC} = \left(\frac{1}{N}\sum_{i=1}^{N} (\hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i)(\hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i)'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} (\hat{\boldsymbol{\Gamma}}_N\mathbf{z}_i) y_i\right)$$

Cette propriété était importante lorsque les moyens de calcul étaient limités, mais elle doit être utilisée avec précaution. L'utilisation de régresseurs estimés en deuxième étape peut être dangereuse, particulièrement dans le contexte des estimateurs non linéaires des doubles moindres carrés qui ne possèdent pas cette propriété des "moindres carrés successifs". L'utilisation d'instruments estimés ne pose en revanche pas de problème particulier.

## Relation avec l'estimateur des variables instrumentales

L'écriture matricielle compacte permet d'établir la relation entre l'estimateur des variables instrumentales et celui des doubles moindres carrés. En utilisant la matrice d'instruments $\mathbf{Z}$ de dimension $N \times L$, les estimateurs s'écrivent :

$$\hat{\boldsymbol{\alpha}}_N^{VI} = (\mathbf{Z}'\mathbf{X})^{-1}\mathbf{Z}'\mathbf{y}$$

$$\hat{\boldsymbol{\alpha}}_N^{2MC} = (\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{y}$$

Lorsque $K = L$, les matrices $\mathbf{X}'\mathbf{Z}$, $\mathbf{Z}'\mathbf{Z}$ et $\mathbf{Z}'\mathbf{X}$ sont carrées et de même dimension $K \times K$. En utilisant les propriétés des inverses de produits de matrices inversibles $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$, on obtient :

$$\hat{\boldsymbol{\alpha}}_N^{2MC} = (\mathbf{Z}'\mathbf{X})^{-1}\mathbf{Z}'\mathbf{Z}(\mathbf{X}'\mathbf{Z})^{-1}\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{y} = (\mathbf{Z}'\mathbf{X})^{-1}\mathbf{Z}'\mathbf{y} = \hat{\boldsymbol{\alpha}}_N^{VI}$$

Ainsi, l'estimateur des variables instrumentales constitue un cas particulier de l'estimateur des doubles moindres carrés. De même, l'estimateur des moindres carrés ordinaires est un cas particulier d'estimateur des variables instrumentales lorsque les variables explicatives peuvent être utilisées comme leurs propres instruments ($\mathbf{Z} = \mathbf{X}$).

En économétrie, l'estimateur des doubles moindres carrés constitue une référence essentielle pour le traitement de l'endogénéité dans les modèles linéaires.

# Propriétés asymptotiques de l'estimateur des doubles moindres carrés

## Convergence de l'estimateur

La convergence de l'estimateur des doubles moindres carrés repose sur les mêmes principes fondamentaux que ceux de l'estimateur des variables instrumentales. Considérons un échantillon $\{(y_i, \mathbf{x}_i, \mathbf{z}_i); i = 1,2,\ldots,N\}$ de variables aléatoires tel que :

$$y_i = \mathbf{a}_0'\mathbf{x}_i + u_i \text{ avec } E[u_i|\mathbf{z}_i] = 0$$

L'estimateur des doubles moindres carrés :

$$\hat{\mathbf{a}}_N^{2MC} = \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i y_i\right)$$

existe avec une probabilité approchant 1 et converge en probabilité vers le vrai paramètre : $\hat{\mathbf{a}}_N^{2MC} \xrightarrow{p} \mathbf{a}_0$ quand $N \to \infty$.

Cette propriété de convergence se démontre en utilisant les techniques habituelles à partir de l'équation :

$$\hat{\mathbf{a}}_N^{2MC} = \mathbf{a}_0 + \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i u_i\right)$$

obtenue en substituant $y_i = \mathbf{a}_0'\mathbf{x}_i + u_i$. Les résultats cruciaux pour la convergence sont l'application de la loi des grands nombres et la condition d'exogénéité $E[\mathbf{z}_i u_i] = \mathbf{0}$.

## Normalité asymptotique dans le cas homoscédastique

La distribution asymptotique de l'estimateur des doubles moindres carrés est particulièrement bien établie dans le cas où les termes d'erreur sont homoscédastiques. Dans le cadre d'un modèle à variables instrumentales avec $E[u_i^2|\mathbf{z}_i] = \sigma_0^2$, l'estimateur des doubles moindres carrés vérifie :

$$\sqrt{N}(\hat{\mathbf{a}}_N^{2MC} - \mathbf{a}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_0)$$

où la matrice de variance asymptotique est donnée par :

$$\boldsymbol{\Sigma}_0 = \sigma_0^2 (E[\mathbf{x}_i\mathbf{z}_i'](E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i\mathbf{x}_i'])^{-1}$$

Cette propriété se démontre en utilisant le théorème central limite appliqué à l'équation :

$$\sqrt{N}(\hat{\mathbf{a}}_N^{2MC} - \mathbf{a}_0) = \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{\sqrt{N}}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i u_i\right)$$

L'hypothèse d'homoscédasticité permet une simplification importante de l'expression de la variance asymptotique. Alors que dans le cas hétéroscédastique, l'expression de la variance asymptotique devient particulièrement complexe, l'homoscédasticité conduit à la forme simplifiée présentée ci-dessus.

Une seconde raison de privilégier le cas homoscédastique est que l'estimateur des doubles moindres carrés est asymptotiquement efficace dans ce contexte, c'est-à-dire qu'il n'existe pas de meilleur estimateur de la méthode des moments fondé sur la condition estimante considérée. Cette propriété d'efficacité ne se maintient pas en présence d'hétéroscédasticité.

La variance de la loi limite se simplifie grâce aux propriétés algébriques $(\mathbf{A}'\mathbf{B})' = \mathbf{B}'\mathbf{A}$ et $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$. Dans le cas hétéroscédastique, la variance asymptotique prend une forme beaucoup plus compliquée impliquant $E[\mathbf{x}_i\mathbf{z}_i'(E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i\mathbf{z}_i'u_i^2]E[\mathbf{z}_i\mathbf{x}_i'](E[\mathbf{x}_i\mathbf{z}_i'(E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i\mathbf{x}_i'])^{-1}$.

## Estimation de la variance asymptotique

Dans un modèle à variables instrumentales avec termes d'erreur homoscédastiques, la variance asymptotique $\boldsymbol{\Sigma}_0$ de l'estimateur des doubles moindres carrés peut être estimée par :

$$\hat{\boldsymbol{\Sigma}}_N = \hat{\sigma}_N^2 \left(\frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_i\mathbf{z}_i'(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{z}_i\mathbf{x}_i'\right)^{-1}$$

avec $\hat{\sigma}_N^2 = \frac{1}{N-K}\sum_{i=1}^{N} \hat{u}_{i,N}^2$ et $\hat{u}_{i,N} = y_i - \mathbf{x}_i'\hat{\mathbf{a}}_N^{2MC}$.

Cet estimateur $\hat{\boldsymbol{\Sigma}}_N$ constitue simplement la contrepartie empirique de $\boldsymbol{\Sigma}_0 = \sigma_0^2 (E[\mathbf{x}_i\mathbf{z}_i'](E[\mathbf{z}_i\mathbf{z}_i'])^{-1}E[\mathbf{z}_i\mathbf{x}_i'])^{-1}$, en notant que $\sigma_0^2 = E[(y_i - \mathbf{x}_i'\mathbf{a}_0)^2]$. Sa convergence découle de l'application de la loi des grands nombres et de la propriété de convergence de $\hat{\mathbf{a}}_N^{2MC}$.

# Considérations pratiques pour l'usage des variables instrumentales

## Terminologie et position dans la littérature économétrique

Le terme "modèle à variables instrumentales" est relativement peu utilisé dans la littérature économétrique, bien qu'il souligne une réalité importante : les variables instrumentales font partie intégrante de la spécification du modèle économétrique. Le choix des instruments $\mathbf{z}_i$ est aussi crucial que celui des variables explicatives $\mathbf{x}_i$ du modèle. Cette approche contraste avec une vision où les instruments seraient des outils techniques accessoires plutôt que des composantes structurelles de la modélisation.

Dans la pratique économétrique contemporaine, l'estimateur des variables instrumentales "n'existe pas" en tant que tel dans les logiciels d'économétrie et tend à disparaître des manuels. Cette évolution s'explique par le fait que l'estimateur des variables instrumentales constitue un cas particulier de l'estimateur des doubles moindres carrés, dont le calcul est programmé dans tous les logiciels spécialisés.

## Stratégies de choix des variables instrumentales

Le choix des variables instrumentales constitue l'aspect le plus délicat de cette méthodologie et doit résulter d'une analyse fine du processus générateur de données (PGD). L'exogénéité des variables instrumentales, condition fondamentale pour la validité de l'estimation, est quasiment impossible à tester dans l'absolu. Cette impossibilité de test direct de l'exogénéité rend le choix des instruments particulièrement critique.

En pratique, il est fortement recommandé de s'inspirer de la littérature existante. Dans la grande majorité des cas (probablement 99%), les problèmes rencontrés correspondent à des situations déjà analysées ou à des cas analogues à ceux qui ont été traités dans la littérature. Cette approche cumulative permet de bénéficier de l'expérience collective de la profession et de réduire les risques d'erreurs de spécification.

Les variables instrumentales développées par Angrist sont souvent citées comme exceptionnelles par leur simplicité et leur pertinence. Certains critiques, avec ironie, suggèrent qu'Angrist détermine ses problèmes de recherche en fonction des variables instrumentales qu'il a à disposition, soulignant ainsi l'importance centrale du choix des instruments dans la faisabilité d'une étude empirique.

## Arbitrage entre nombre de variables instrumentales et qualité

L'efficacité asymptotique de l'estimateur des doubles moindres carrés s'accroît théoriquement avec le nombre de variables instrumentales utilisées, de manière mécanique. Cette propriété théorique rend tentante la stratégie d'utiliser de nombreuses variables instrumentales. Cependant, plusieurs considérations pratiques invitent à la prudence :

**Risque de variables instrumentales non valides** : Plus le nombre d'instruments utilisés est élevé, plus le risque d'inclure de "mauvaises" variables instrumentales, c'est-à-dire des variables non exogènes, augmente. L'inclusion d'instruments invalides peut compromettre la cohérence de l'ensemble de l'estimation.

**Biais à distance finie** : L'utilisation de conditions estimantes trop nombreuses peut induire des biais dans l'estimateur des doubles moindres carrés lorsque la taille d'échantillon N n'est pas suffisamment grande. Ce problème devient particulièrement aigu lorsque le ratio N/L diminue.

**Problème des instruments faibles** : Les variables instrumentales ayant une faible corrélation avec les variables qu'elles sont censées instrumenter peuvent être à l'origine de biais importants lorsqu'elles sont "légèrement endogènes". Cette problématique, connue sous le nom de "weak instruments problem", constitue un défi majeur dans la pratique économétrique.

## Biais à distance finie et dimensionnalité

L'estimateur des doubles moindres carrés est convergent ($\hat{\mathbf{a}}_N^{2MC} \xrightarrow{p} \mathbf{a}_0$ quand $N \to \infty$) mais demeure biaisé à distance finie : $E[\hat{\mathbf{a}}_N^{2MC}|\mathbf{Z}] \neq \mathbf{a}_0$ en général.

Schématiquement, lorsque la dimension $L = \dim(\mathbf{z}_i)$ augmente, le ratio N/L diminue et il devient de plus en plus difficile de justifier l'utilisation des propriétés asymptotiques de $\hat{\mathbf{a}}_N^{2MC}$ pour approximer ses propriétés réelles avec N grand mais fini. 

C'est particulièrement le nombre de variables instrumentales "externes", $\dim(\tilde{\mathbf{z}}_i^e)$, qui importe dans cette analyse. Il est préférable de se contenter de quelques variables instrumentales "dont on est sûr" par variable explicative endogène plutôt que de tenter d'en utiliser un grand nombre, surtout si le ratio N/K n'est pas très grand.

## Le problème des instruments faibles

Dans le modèle simple $y_i = \alpha_0 + \beta_0 \tilde{x}_i + u_i$ avec $E[u_i] = 0$ et $\tilde{z}_i$ comme variable instrumentale pour $\tilde{x}_i$, l'estimateur des doubles moindres carrés vérifie :

$\hat{\beta}_N^{2MC} = \hat{\beta}_N^{VI} \xrightarrow{p} \beta_0 + \frac{\text{Cov}(\tilde{z}_i, u_i)}{\text{Cov}(\tilde{z}_i, \tilde{x}_i)}$

Une variable $\tilde{z}_i$ est considérée comme un instrument faible pour $\tilde{x}_i$ si $\text{Cov}(\tilde{z}_i, \tilde{x}_i) \equiv \varepsilon \approx 0$.

L'utilisation d'instruments faibles ne pose pas de problème si $\text{Cov}(\tilde{z}_i, u_i) = 0$, ce qui ne peut être réellement assuré qu'"en théorie". Le problème des instruments faibles réside dans le fait que si $\text{Cov}(\tilde{z}_i, u_i) = \varsigma$ avec $\varsigma \approx 0$ mais $\varsigma \neq 0$, alors $\frac{\text{Cov}(\tilde{z}_i, u_i)}{\text{Cov}(\tilde{z}_i, \tilde{x}_i)} = \frac{\varsigma}{\varepsilon}$ peut être grand en valeur absolue, impliquant un biais asymptotique significatif de $\hat{\beta}_N^{2MC}$.

Inversement, si $\tilde{z}_i$ est un instrument "fort" pour $\tilde{x}_i$, c'est-à-dire si $\text{Cov}(\tilde{z}_i, \tilde{x}_i)$ est grand, alors le biais asymptotique de $\hat{\beta}_N^{2MC}$ est nécessairement petit et peut être négligé.

# Choix des variables instrumentales et conditions d'identification

## Conditions d'exogénéité et d'identification

L'utilisation des estimateurs des variables instrumentales ou des doubles moindres carrés repose sur l'exogénéité des variables instrumentales, $E[u_i|\mathbf{z}_i] = 0$, pour définir la condition d'orthogonalité :

$E[\mathbf{z}_i(y_i - \mathbf{x}_i'\mathbf{a}_0)] = \mathbf{0}$

Cette condition d'exogénéité constitue une condition nécessaire mais non suffisante pour l'identification de $\mathbf{a}_0$. Il est également nécessaire que cette équation caractérise $\mathbf{a}_0$ de manière unique, c'est-à-dire que :

$E[\mathbf{z}_i(y_i - \mathbf{x}_i'\mathbf{a})] = \mathbf{0} \Leftrightarrow \mathbf{a} = \mathbf{a}_0$

## Condition de rang sur les variables instrumentales

L'analyse de l'unicité de la solution révèle que l'équation $E[\mathbf{z}_i\mathbf{x}_i']\mathbf{a} = E[\mathbf{z}_i y_i]$ admet une solution unique en $\mathbf{a}$ si et seulement si $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = \dim(\mathbf{a}) = K$.

**Propriété d'identification** : Le vecteur de paramètres $\mathbf{a}_0$ est identifiable par la condition $E[\mathbf{z}_i(y_i - \mathbf{x}_i'\mathbf{a}_0)] = \mathbf{0}$ si et seulement si $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$.

Cette condition d'identification est appelée condition de rang sur les variables instrumentales. Son interprétation n'est pas immédiate, mais certaines conditions nécessaires pour $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$ sont directement compréhensibles.

## Conditions nécessaires pour l'identification

Trois conditions nécessaires peuvent être identifiées :

**Condition d'ordre** : $\dim(\mathbf{z}_i) \geq \dim(\mathbf{x}_i)$, soit $L \geq K$. Il doit y avoir au moins autant de variables instrumentales que de variables explicatives, ou de manière équivalente, au moins autant de conditions de moment que de paramètres à estimer.

**Condition d'identification des effets** : $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$. Les éléments de $\mathbf{x}_i$ doivent être tels que $\mathbf{a}_0$ serait identifié si $y_i = \mathbf{x}_i'\mathbf{a}_0 + u_i$ était un modèle de régression ordinaire.

**Condition d'indépendance des instruments** : $\text{rang}(E[\mathbf{z}_i\mathbf{z}_i']) \geq K$. Au moins $K = \dim(\mathbf{a}_0) = \dim(\mathbf{x}_i)$ éléments de $\mathbf{z}_i$ doivent être linéairement indépendants, c'est-à-dire non redondants quant à leur apport d'information.

## Analyse des conditions de rang par projections linéaires

Pour examiner le contenu concret de la condition $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$, il convient d'utiliser les partitions habituelles et les projections linéaires. En décomposant les variables explicatives en variables exogènes $\mathbf{x}_i^x$ et endogènes $\tilde{\mathbf{x}}_i^e$, et les instruments en variables exogènes et variables instrumentales externes $\tilde{\mathbf{z}}_i^e$, nous pouvons définir les parties spécifiques de chaque variable.

Notons $\tilde{e}_{ℓ,i}$ le résidu de la projection du ℓ-ième élément de $\tilde{\mathbf{x}}_i^e$ sur $\mathbf{x}_{i,(−ℓ)}^x$, c'est-à-dire la partie spécifique de $\tilde{x}_{ℓ,i}$ dans $\tilde{\mathbf{x}}_i^e$ :

$\tilde{e}_{ℓ,i} \equiv \tilde{x}_{ℓ,i} - E_L[\tilde{x}_{ℓ,i}|\mathbf{x}_{i,(−ℓ)}^x]$

pour $ℓ = 1,\ldots,K-1$.

Le vecteur $\tilde{\mathbf{e}}_i^e$ est défini comme l'empilement des parties spécifiques des variables exogènes et endogènes, excluant la constante pour éviter les problèmes de colinéarité parfaite.

## Conditions équivalentes pour l'identification

Trois conditions équivalentes caractérisent l'identification :

**Condition (i)** : $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$

**Condition (ii)** : $\text{rang}(\text{Cov}(\mathbf{z}_i, \tilde{\mathbf{x}}_i)) = K-1$

**Condition (iii)** : $\text{rang}(V[\tilde{\mathbf{e}}_i^x]) = M-1$ et $\text{rang}(\text{Cov}(\tilde{\mathbf{z}}_i^e, \tilde{\mathbf{e}}_i^e)) = K-M$

L'analyse de la condition (iii) est particulièrement éclairante. La matrice $V[\tilde{\mathbf{e}}_i^x]$ étant diagonale, l'analyse de son rang est immédiate. Le défi réside dans l'examen de la condition $\text{rang}(\text{Cov}(\tilde{\mathbf{z}}_i^e, \tilde{\mathbf{e}}_i^e)) = K-M$, même lorsque les éléments de $\tilde{\mathbf{e}}_i^e$ ne sont pas corrélés entre eux.

## Condition suffisante et variables instrumentales spécifiques

Une condition suffisante simple peut être énoncée pour $\text{rang}(\text{Cov}(\tilde{\mathbf{z}}_i^e, \tilde{\mathbf{e}}_i^e)) = K-M$. En notant :

$E_L[\tilde{e}_{k,i}^e|\tilde{\mathbf{z}}_i^e] = \sum_{m=1}^{L-M} \gamma_{ℓ,m}^e \tilde{z}_{m,i}^e$

nous dirons que $\tilde{z}_{ℓ,i}^e$ est une variable instrumentale spécifique de $\tilde{x}_{k,i}^e$ si et seulement si $\gamma_{ℓ,k} \neq 0$ et $\gamma_{ℓ,m} = 0$ pour $m \in \{1,\ldots,K-M\}$ et $m \neq k$.

En termes de partie spécifique $\tilde{\varsigma}_{ℓ,i}^e \equiv \tilde{z}_{ℓ,i}^e - E_L[\tilde{z}_{ℓ,i}^e|\tilde{\mathbf{z}}_{i,(−ℓ)}^e]$, la variable $\tilde{z}_{ℓ,i}^e$ est spécifique de $\tilde{x}_{k,i}^e$ si et seulement si $\text{Cov}(\tilde{\varsigma}_{ℓ,i}^e, \tilde{e}_{k,i}^e) \neq 0$ et $\text{Cov}(\tilde{\varsigma}_{ℓ,i}^e, \tilde{e}_{m,i}^e) = 0$ pour $m \neq k$.

Si chaque élément de $\tilde{\mathbf{e}}_i^e$ possède une variable instrumentale externe qui lui est spécifique, alors $\text{rang}(\text{Cov}(\tilde{\mathbf{z}}_i^e, \tilde{\mathbf{e}}_i^e)) = K-M$. Cette condition suffisante peut être examinée empiriquement et fournit une guidance pratique pour l'évaluation de la validité des instruments.

## Implications pratiques pour l'identification

Pour que $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$, deux conditions principales doivent être satisfaites :

**Variabilité et indépendance des variables explicatives** : Les éléments de $\tilde{\mathbf{x}}_i$ doivent être suffisamment variables et suffisamment indépendants entre eux, générant ainsi de "grosses" parties spécifiques. Cette condition correspond à la condition de rang du modèle de régression standard. Si le modèle linéaire utilisé est problématique, de très bonnes variables instrumentales n'y changeront rien.

**Instrumentation adéquate des variables endogènes** : Chaque variable explicative endogène doit être "instrumentée" par au moins une variable instrumentale externe. Il ne sert à rien d'avoir beaucoup de variables instrumentales si une variable explicative endogène est abandonnée en termes d'instrumentation. Plus que les variables $\tilde{\mathbf{x}}_i^e$ elles-mêmes, ce sont leurs parties spécifiques $\tilde{\mathbf{e}}_i^e$ qui doivent être instrumentées par $\tilde{\mathbf{z}}_i^e$.

## Diagnostic pratique des problèmes d'identification

En pratique, l'examen de la condition $\text{rang}(\text{Cov}(\tilde{\mathbf{z}}_i^e, \tilde{\mathbf{e}}_i^e)) = K-M$ suit généralement cette séquence :

**Recherche de variables instrumentales spécifiques** : Lorsqu'on cherche des variables instrumentales pour $\tilde{\mathbf{x}}_i^e$, on privilégie des instruments aussi spécifiques que possible de chacun des éléments. Cette pratique se réfère à la condition suffisante pour la condition de rang.

**Calcul direct de l'estimateur** : La condition $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i']) = K$ étant difficile à examiner ex ante, on calcule directement l'estimateur des doubles moindres carrés en utilisant le vecteur de variables instrumentales $\mathbf{z}_i$.

**Diagnostic a posteriori** : On diagnostique un problème relatif à $\text{rang}(E[\mathbf{z}_i\mathbf{x}_i'])$ si le calcul de l'estimateur est impossible parce que certaines matrices ne peuvent être inversées (cas relativement rare) ou si les écarts-types estimés de l'estimateur sont "énormes" pour certains paramètres. Ces derniers correspondent généralement à des variables explicatives peu variables, très liées entre elles, ou à des variables explicatives endogènes mal instrumentées.

## Anatomie de l'estimateur des doubles moindres carrés

L'analyse des projections des parties spécifiques des variables explicatives endogènes sur le vecteur des instruments révèle la structure fondamentale de l'identification. Dans le modèle à variables instrumentales :

$y_i = \alpha_0 + \mathbf{b}_0'\tilde{\mathbf{x}}_i + u_i \text{ avec } E[u_i|\mathbf{z}_i] = 0$

si $\text{rang}(\text{Cov}(\mathbf{z}_i, \tilde{\mathbf{x}}_i)) = K-1$, alors :

Pour les variables exogènes : $b_{m,0} = (V[\tilde{e}_{m,i}^x])^{-1}\text{Cov}(\tilde{e}_{m,i}^x, y_i)$ pour $m = 1,\ldots,M-1$

Pour les variables endogènes : $b_{ℓ,0} = (V[E_L[\tilde{e}_{ℓ,i}^e|\tilde{\mathbf{z}}_i^e]])^{-1}\text{Cov}(E_L[\tilde{e}_{ℓ,i}^e|\tilde{\mathbf{z}}_i^e], y_i)$ pour $ℓ = 1,\ldots,K-M$

Cette décomposition peut également s'écrire :

$b_{ℓ,0} = (\text{Cov}(E_L[\tilde{e}_{ℓ,i}^e|\tilde{\mathbf{z}}_i^e], \tilde{e}_{ℓ,i}^e))^{-1}\text{Cov}(E_L[\tilde{e}_{ℓ,i}^e|\tilde{\mathbf{z}}_i^e], y_i)$

Cette "anatomie" de l'estimateur des doubles moindres carrés montre que ce sont effectivement les projections des parties spécifiques des variables explicatives endogènes sur le vecteur des instruments qui identifient les paramètres du modèle associés à ces variables. Cette perspective éclaire la logique profonde de l'instrumentation et guide le choix des variables instrumentales dans la pratique économétrique.

# Fonctions de contrôle et variables de contrôle de l'hétérogénéité

## Introduction aux fonctions de contrôle

Les techniques de variables instrumentales (VI) présentées précédemment constituent l'approche principale pour traiter les problèmes d'endogénéité des variables explicatives. L'estimateur des doubles moindres carrés (2MC) permet de contourner efficacement les problèmes de simultanéité, d'omission de variables explicatives pertinentes et d'erreurs de mesure sur les variables explicatives.

Cette section présente une approche alternative pour gérer les problèmes d'endogénéité : l'approche par les fonctions de contrôle. Cette méthode se distingue par sa capacité à "contrôler" directement le problème d'endogénéité plutôt que de le contourner comme le font les VI. Elle offre également une base théorique pour développer des tests d'exogénéité des variables explicatives et constitue une introduction naturelle aux variables de contrôle de l'hétérogénéité.

### Principe fondamental des fonctions de contrôle

Le principe des fonctions de contrôle repose sur une décomposition stratégique du terme d'erreur en deux composantes distinctes. Cette décomposition permet de transformer un modèle avec variables explicatives endogènes en un modèle de régression standard où les conditions d'orthogonalité sont respectées.

La première composante, appelée fonction de contrôle, capture spécifiquement la partie du terme d'erreur qui génère l'endogénéité de la variable explicative concernée. Cette fonction "contrôle" donc le problème d'endogénéité en l'isolant de manière explicite. La seconde composante correspond au résidu de cette décomposition, qui ne présente plus de corrélation problématique avec les variables explicatives.

## Développement théorique des fonctions de contrôle

### Le modèle de référence

Considérons le modèle linéaire général avec une variable explicative endogène :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + u_i$

où $E[u_i | \mathbf{x}_i] = E[u_i] = 0$ mais $E[u_i | x_i^e] \neq 0$, caractérisant ainsi l'endogénéité de $x_i^e$.

Pour traiter cette endogénéité, nous supposons disposer d'un vecteur de variables instrumentales "externes" $\mathbf{z}_i^e$ pour $x_i^e$, satisfaisant les conditions d'orthogonalité standard :

$E[u_i | \mathbf{x}_i, \mathbf{z}_i^e] = E[u_i | \mathbf{z}_i] = 0$

où $\mathbf{z}_i = (\mathbf{x}_i', \mathbf{z}_i^{e'})$ représente l'ensemble complet des instruments.

### Construction de la fonction de contrôle

Le problème d'endogénéité provient de la corrélation non nulle entre $x_i^e$ et $u_i$. Si nous connaissions la forme exacte de cette relation, nous pourrions l'exploiter pour éliminer l'endogénéité. Formellement, si nous connaissions $E[u_i | \mathbf{z}_i, x_i^e]$, nous pourrions écrire :

$E[u_i | \mathbf{z}_i, x_i^e] = \rho \times \lambda(\mathbf{z}_i, x_i^e)$

pour une fonction $\lambda$ appropriée. Cette relation permet une décomposition fondamentale :

$u_i = \rho \lambda(\mathbf{z}_i, x_i^e) + \varepsilon_i$

où $\varepsilon_i$ représente le résidu de cette espérance conditionnelle, satisfaisant par construction $E[\varepsilon_i | \mathbf{z}_i, x_i^e] = 0$.

### Mise en œuvre par projections linéaires

Dans le contexte linéaire, cette approche se concrétise par l'utilisation de deux projections linéaires successives. La première projection décompose la variable endogène $x_i^e$ :

$x_i^e = \mathbf{z}_i'\boldsymbol{\gamma} + e_i$

où $\boldsymbol{\gamma} = E[\mathbf{z}_i \mathbf{z}_i']^{-1} E[\mathbf{z}_i x_i^e]$ et $E[e_i | \mathbf{z}_i] = 0$ par construction.

Cette décomposition sépare $x_i^e$ en deux composantes : $\mathbf{z}_i'\boldsymbol{\gamma}$ qui est exogène par rapport à $u_i$ (puisque $\mathbf{z}_i$ est un vecteur d'instruments valides), et $e_i$ qui contient la source de l'endogénéité puisque $\text{Cov}(x_i^e, u_i) = \text{Cov}(e_i, u_i)$ étant donné que $E[e_i | \mathbf{z}_i] = 0$.

La seconde projection décompose le terme d'erreur $u_i$ :

$u_i = \rho e_i + \varepsilon_i$

où $\rho = E[e_i e_i]^{-1} E[e_i u_i]$ et $E[\varepsilon_i | e_i] = 0$ par construction.

### Le modèle de régression augmentée

En substituant ces décompositions dans le modèle original, nous obtenons :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \rho(x_i^e - \mathbf{z}_i'\boldsymbol{\gamma}) + \varepsilon_i$

Ce qui se réécrit comme :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \rho e_i + \varepsilon_i$

où $e_i = x_i^e - \mathbf{z}_i'\boldsymbol{\gamma}$ représente la fonction de contrôle.

Cette formulation révèle que le modèle augmenté est désormais un modèle de régression standard puisque $E[\varepsilon_i | \mathbf{x}_i, x_i^e, e_i] = 0$. La fonction de contrôle $e_i$ "capture" toute la corrélation problématique entre $x_i^e$ et le terme d'erreur original.

### Procédure d'estimation en deux étapes

L'estimation des paramètres du modèle augmenté peut s'effectuer selon une procédure en deux étapes :

**Première étape :** Estimation des paramètres de projection $\boldsymbol{\gamma}$ par moindres carrés ordinaires (MCO) dans la régression :

$x_i^e = \mathbf{z}_i'\boldsymbol{\gamma} + e_i$

Cette étape produit l'estimateur $\hat{\boldsymbol{\gamma}}_{MCO}$ et permet de calculer les résidus estimés $\hat{e}_{i,N} = x_i^e - \mathbf{z}_i'\hat{\boldsymbol{\gamma}}_{MCO}$.

**Seconde étape :** Estimation des paramètres $\alpha_0$, $\boldsymbol{\beta}_0$ et $\rho$ par MCO dans la régression augmentée :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \rho \hat{e}_{i,N} + \hat{\varepsilon}_{i,N}$

### Propriétés asymptotiques et limites

L'erreur de mesure introduite par le remplacement de $\boldsymbol{\gamma}$ par $\hat{\boldsymbol{\gamma}}_{MCO}$ dans la seconde étape est asymptotiquement négligeable. En effet, la convergence en probabilité $\hat{\boldsymbol{\gamma}}_{MCO} \xrightarrow{p} \boldsymbol{\gamma}$ implique que $\hat{e}_{i,N} - e_i \xrightarrow{p} 0$.

Cependant, cette erreur de mesure introduit un aléa supplémentaire qui modifie la distribution asymptotique de l'estimateur de la seconde étape. Les $\hat{e}_{i,N}$ constituent des "régresseurs estimés", ce qui complique l'inférence statistique. Cette caractéristique limite l'intérêt pratique des fonctions de contrôle pour l'estimation des modèles linéaires à VI, où l'estimateur des 2MC reste généralement préférable.

### Extension aux variables multiples

L'approche se généralise naturellement au cas de plusieurs variables endogènes. Pour le modèle :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + \mathbf{x}_i^{e'}\boldsymbol{\beta}_0^e + u_i$

il suffit d'utiliser les décompositions :

$\mathbf{x}_i^e = \mathbf{Z}_i \boldsymbol{\Gamma} + \mathbf{e}_i \quad \text{et} \quad u_i = \mathbf{e}_i'\boldsymbol{\rho} + \varepsilon_i$

où $\mathbf{Z}_i$ contient tous les instruments et $\boldsymbol{\Gamma}$ est la matrice des coefficients de projection.

## Test d'exogénéité par la régression augmentée

### Motivation et enjeux

L'endogénéité des variables explicatives constitue un problème fréquent et sérieux en économétrie. Face à ce défi, une stratégie pourrait consister à utiliser systématiquement des techniques à VI pour se prémunir contre tout problème d'endogénéité potentiel. Cependant, cet excès de prudence présente plusieurs inconvénients majeurs.

Premièrement, le choix de variables instrumentales appropriées s'avère souvent délicat et des VI ne sont pas toujours disponibles. Deuxièmement, si la variable explicative "instrumentée" est en réalité exogène, l'utilisation de l'estimateur des 2MC au lieu des MCO entraîne une perte d'efficacité d'estimation souvent substantielle en pratique. Troisièmement, il existe des moyens de tester l'exogénéité des variables explicatives, permettant ainsi un choix éclairé entre les différentes techniques d'estimation.

### Propriétés comparées des estimateurs selon l'exogénéité

Pour un modèle linéaire général $y_i = \mathbf{a}_0'\mathbf{x}_i + u_i$ avec $E[u_i] = 0$, les propriétés des estimateurs MCO et 2MC dépendent crucially du statut d'exogénéité des variables explicatives.

**Cas d'endogénéité :** Si $E[u_i | \mathbf{x}_i] \neq 0$, alors l'estimateur MCO $\hat{\mathbf{a}}_{MCO}$ converge vers une limite différente de $\mathbf{a}_0$ (biais de convergence), tandis que l'estimateur 2MC $\hat{\mathbf{a}}_{2MC}$ reste convergent vers $\mathbf{a}_0$ sous réserve de la validité des instruments.

**Cas d'exogénéité :** Si $E[u_i | \mathbf{x}_i] = 0$, les deux estimateurs sont convergents vers $\mathbf{a}_0$, mais l'estimateur MCO présente une matrice de variance-covariance asymptotique strictement plus petite que celle de l'estimateur 2MC.

Cette différence d'efficacité s'explique par la perte d'information inhérente à l'utilisation des VI. En effet, l'estimateur des 2MC "remplace" implicitement les $\mathbf{x}_i$ par leur projection $E[\mathbf{x}_i | \mathbf{z}_i]$ sur l'espace des instruments. Cette projection élimine une partie des variations de $\mathbf{x}_i$, celle décrite par $\mathbf{e}_i = \mathbf{x}_i - E[\mathbf{x}_i | \mathbf{z}_i]$, réduisant ainsi la précision de l'estimation.

### Fondement théorique du test d'Hausman

Ces propriétés comparées constituent le fondement des tests d'Hausman d'exogénéité des variables explicatives. Le principe statistique repose sur l'observation que, sous l'hypothèse nulle d'exogénéité, la différence entre les deux estimateurs converge en distribution vers une loi normale centrée :

$\sqrt{N}(\hat{\mathbf{a}}_{2MC} - \hat{\mathbf{a}}_{MCO}) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \boldsymbol{\Psi})$

où $\boldsymbol{\Psi}$ est une matrice définie positive. Cette convergence permet de construire une statistique de test basée sur la magnitude de la différence entre les estimateurs.

### Test de la régression augmentée

Le cadre des fonctions de contrôle offre une implémentation particulièrement élégante du test d'Hausman. Pour le modèle avec une variable endogène :

$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + u_i$

l'hypothèse d'exogénéité de $x_i^e$ équivaut à tester $\text{Cov}(x_i^e, u_i) = 0$.

En utilisant la décomposition par fonction de contrôle, nous avons :

$\text{Cov}(x_i^e, u_i) = \text{Cov}(e_i, u_i) = \rho \times V(e_i)$

Par conséquent, l'hypothèse d'exogénéité équivaut à tester $H_0: \rho = 0$.

### Procédure de test

Le test de la régression augmentée s'effectue selon la procédure suivante :

**Étape 1 :** Estimation de la projection $x_i^e = \mathbf{z}_i'\boldsymbol{\gamma} + e_i$ par MCO, produisant les résidus estimés $\hat{e}_{i,N}$.

**Étape 2 :** Estimation de la régression augmentée $y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \rho \hat{e}_{i,N} + \varepsilon_i$ par MCO.

**Étape 3 :** Test de l'hypothèse $H_0: \rho = 0$ à l'aide des tests standard (test de Student, test de Fisher), sans correction pour l'utilisation de régresseurs estimés.

Cette dernière simplification se justifie par le fait que, sous l'hypothèse nulle $\rho = 0$, les erreurs introduites par le remplacement de $\boldsymbol{\gamma}$ par $\hat{\boldsymbol{\gamma}}_{MCO}$ disparaissent du modèle, rendant la correction inutile.

### Interprétation et utilisation des résultats

**Non-rejet de $H_0$:** Si l'hypothèse $\rho = 0$ n'est pas rejetée, la variable $x_i^e$ peut être considérée comme exogène. Le modèle se réduit à un modèle de régression standard, et l'estimation par MCO est recommandée pour bénéficier du gain d'efficacité par rapport aux 2MC.

**Rejet de $H_0$:** Si l'hypothèse $\rho = 0$ est rejetée, la variable $x_i^e$ est endogène. Le modèle doit être traité comme un modèle à VI, et l'estimation par 2MC avec $\mathbf{z}_i$ comme instruments est appropriée. Bien que la régression augmentée fournisse les mêmes estimations ponctuelles des paramètres structurels, elle ne produit pas les écarts-types corrects, nécessitant une ré-estimation par 2MC pour l'inférence.

### Limites et considérations pratiques

Les tests d'exogénéité présentent certaines limites importantes. D'une part, ils ne sont réalisables que si l'on dispose de VI pour la variable dont l'exogénéité est testée. D'autre part, ces tests ne valident pas la spécification "complète" du modèle.

La validité du test repose sur deux conditions critiques : les VI utilisées doivent être elles-mêmes valides (ce qui ne peut être testé qu'avec d'autres VI, créant un problème de régression infinie), et les variables explicatives supposées exogènes doivent l'être réellement (ce qui ne peut également être testé qu'avec des VI supplémentaires).

En définitive, bien que les tests d'exogénéité soient utiles, ils ne peuvent remplacer le travail fondamental de l'économètre : la spécification de l'ensemble d'information du modèle, incluant ses variables explicatives exogènes et ses variables instrumentales. Ce travail requiert une analyse approfondie du processus générateur des données et suppose une connaissance substantielle du phénomène modélisé, confirmant l'adage selon lequel "l'économétrie, c'est d'abord de l'économie".

## Considérations sur les mesures d'ajustement

### Le $R^2$ dans les modèles à VI

Pour un modèle à VI général $y_i = \mathbf{a}_0'\mathbf{x}_i + u_i$ avec $E[u_i | \mathbf{z}_i] = 0$, les logiciels d'économétrie produisent généralement une mesure d'ajustement de type $R^2$ définie par :

$R_{2MC}^2 = 1 - \frac{\sum_{i=1}^N (\hat{u}_{i,N}^{2MC})^2}{\sum_{i=1}^N (y_i - \bar{y}_N)^2}$

où $\hat{u}_{i,N}^{2MC} = y_i - \mathbf{x}_i'\hat{\mathbf{a}}_{2MC}$.

### Propriétés particulières

Contrairement au $R^2$ des modèles de régression standard, cette mesure d'ajustement peut présenter des propriétés contre-intuitives. Premièrement, si $R_{2MC}^2 < 1$, il est possible d'obtenir $R_{2MC}^2 < 0$. Deuxièmement, on n'a généralement pas l'égalité habituelle entre la somme des carrés expliquée et totale moins résiduelle.

Ces particularités proviennent du fait que, dans le calcul de l'estimateur des 2MC, la somme des résidus n'est généralement pas nulle : $\sum_{i=1}^N \hat{u}_{i,N}^{2MC} \neq 0$. Cette propriété reflète la nature différente du critère d'optimisation des 2MC, qui est basé sur les conditions d'orthogonalité $\frac{1}{N}\sum_{i=1}^N \mathbf{z}_i \hat{u}_{i,N}^{2MC} = \mathbf{0}$ plutôt que sur la minimisation de la somme des carrés des résidus.

### Interprétation conceptuelle

Le critère du calcul de $\hat{\mathbf{a}}_{2MC}$ n'est pas un critère d'ajustement au sens traditionnel. L'estimateur des 2MC vise à satisfaire les conditions d'orthogonalité empiriques avec les instruments, non à minimiser l'erreur quadratique de prédiction. Si le terme d'erreur du modèle est très variable, les résidus 2MC prendront de "grosses" valeurs, mais cela ne remet pas en cause la validité de l'estimateur.

Cette différence conceptuelle explique pourquoi l'estimateur MCO produit toujours un meilleur ajustement que l'estimateur 2MC au sens de l'erreur quadratique moyenne, même lorsque le premier est biaisé. L'écart $R_{MCO}^2 - R_{2MC}^2$ sera d'autant plus important que les variables explicatives endogènes sont "fortement" corrélées au terme d'erreur.

### Perspective pratique

En microéconométrie appliquée, les $R^2$ obtenus dans les modèles à VI dépassent rarement 0,4, reflétant la nature complexe des phénomènes économiques et la difficulté de les modéliser exhaustivement. Cette observation souligne l'importance de distinguer entre la logique d'ajustement (maximiser le pouvoir prédictif) et la logique d'identification (estimer correctement les paramètres causaux d'intérêt).

# Les variables de contrôle de l'hétérogénéité

## Introduction et motivation

Les variables de contrôle de l'hétérogénéité représentent une approche alternative aux variables instrumentales pour traiter les problèmes d'endogénéité des variables explicatives. Cette méthode se distingue fondamentalement par sa philosophie : plutôt que de "contourner" le problème d'endogénéité comme le font les VI, elle vise à "éliminer" directement ce problème en contrôlant explicitement ses sources.

Cette approche ne s'applique spécifiquement qu'aux problèmes d'endogénéité causés par l'omission de variables explicatives pertinentes. Elle repose sur l'idée que les variables explicatives d'un modèle servent à réduire la variance du terme d'erreur en "contrôlant" une partie de l'hétérogénéité de la variable à expliquer. L'introduction judicieuse de ces variables permet de capter les effets de phénomènes qui rendent difficile l'identification de la relation d'intérêt dans une population hétérogène.

### Distinction conceptuelle avec les variables instrumentales

Les techniques de VI et l'approche par variables de contrôle de l'hétérogénéité représentent des philosophies très différentes. Les VI permettent de "contourner" le problème d'endogénéité en exploitant une variation exogène de la variable endogène. Les variables de contrôle, quant à elles, permettent de "contenir" et ultimement "éliminer" le problème en modélisant explicitement ses mécanismes générateurs.

Cette différence se reflète dans l'utilisation pratique : les deux approches sont souvent utilisées conjointement, les VI étant employées pour certaines variables endogènes et les variables de contrôle pour d'autres, selon la nature spécifique de chaque problème d'endogénéité.

## Cadre conceptuel des variables de contrôle

### Le rôle général des variables de contrôle

Dans la pratique économétrique, un économètre s'intéresse généralement à l'effet d'une variable spécifique (la variable explicative d'intérêt) sur une variable à expliquer. Cet effet constitue l'effet d'intérêt de l'étude. Cependant, l'estimation de cet effet nécessite souvent l'introduction de variables explicatives "supplémentaires", appelées variables de contrôle.

Considérons le modèle :

$$y_i = \alpha_0 + b_0 x_i + \boldsymbol{\beta}_0'\mathbf{c}_i + u_i$$

où $E[u_i] = 0$, $x_i$ représente la variable d'intérêt, $b_0$ l'effet d'intérêt, et $\mathbf{c}_i$ le vecteur des variables de contrôle.

L'introduction de $\mathbf{c}_i$ dans le modèle améliore systématiquement la précision de l'estimation de $b_0$. Dans le modèle "simplifié" sans contrôle :

$$y_i = \delta_0 + b_0 x_i + v_i$$

où $E[v_i] = 0$, le terme d'erreur $v_i$ contient l'essentiel des effets des variables $\mathbf{c}_i$, conservant ainsi une large part de l'hétérogénéité de $y_i$. Ceci implique $V(v_i) \geq V(u_i)$, rendant l'estimation de $b_0$ moins précise dans le modèle simplifié que dans le modèle complet.

### Contrôle de l'endogénéité par les variables de contrôle

Dans certaines configurations, la variable explicative d'intérêt $x_i$ peut être exogène par rapport à $u_i$ (dans le modèle complet avec $\mathbf{c}_i$) mais endogène par rapport à $v_i$ (dans le modèle simplifié sans $\mathbf{c}_i$). Dans ce cas, le terme $\boldsymbol{\beta}_0'\mathbf{c}_i$ "élimine" le problème d'endogénéité de $x_i$ en contrôlant l'hétérogénéité de $y_i$.

Cette situation se produit lorsque $x_i$ et $v_i$ sont liés par, et uniquement par, les variables $\mathbf{c}_i$. La transition du modèle complet au modèle simplifié implique une décomposition de $\boldsymbol{\beta}_0'\mathbf{c}_i$ :

$$\boldsymbol{\beta}_0'\mathbf{c}_i = E[\boldsymbol{\beta}_0'\mathbf{c}_i] + (\boldsymbol{\beta}_0'\mathbf{c}_i - E[\boldsymbol{\beta}_0'\mathbf{c}_i])$$

Cette décomposition sépare les effets "en moyenne" des effets "hors-moyenne", ces derniers constituant une source potentielle de corrélation entre $x_i$ et le nouveau terme d'erreur $v_i$.

La notion de "contrôle" est intimement liée à celle de "toutes choses égales par ailleurs" : si $x_i$ et $\mathbf{c}_i$ sont corrélés et $\boldsymbol{\beta}_0 \neq \mathbf{0}$, alors $x_i$ et $v_i$ varient nécessairement conjointement, créant l'endogénéité dans le modèle simplifié.

## Modélisation formelle du problème

### Le modèle de référence

Reprenons le modèle linéaire général avec une variable explicative endogène :

$$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + u_i$$

où $E[u_i | \mathbf{x}_i] = E[u_i] = 0$ mais $E[u_i | x_i^e] \neq 0$.

L'approche par variables de contrôle part du postulat qu'il existerait idéalement un modèle "latent" :

$$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \delta_0 q_i + v_i$$

où $E[v_i | \mathbf{x}_i, x_i^e, q_i] = E[v_i] = 0$, qui constituerait un modèle de régression parfait. Le problème pratique réside dans le fait que la variable $q_i$ n'est pas observée dans les données disponibles.

### Caractéristiques de la variable latente

La variable latente $q_i$ présente plusieurs propriétés importantes. Nous supposons que $\text{Cov}(q_i, \mathbf{x}_i) = \mathbf{0}$, signifiant que $\mathbf{x}_i$ ne fournit aucune information statistique sur $q_i$. Cette hypothèse permet de distinguer clairement les rôles de $\mathbf{x}_i$ et $q_i$ dans le modèle. Par simplification, nous posons également $E[q_i] = 0$, ce qui constitue une normalisation sans perte de généralité sur une variable non observée.

Le lien entre les modèles utilisé et latent s'établit par :

$$u_i = v_i + \delta_0 q_i$$

Cette relation montre que $u_i$ contient l'effet de $q_i$ sur $y_i$, représenté par $\delta_0 q_i$, qui constitue un effet de moyenne nulle accroissant l'hétérogénéité non contrôlée de $y_i$.

### Source de l'endogénéité

La variable $x_i^e$ est endogène dans le modèle utilisé si et seulement si $\text{Cov}(x_i^e, u_i) \neq 0$. En utilisant la relation entre les modèles, nous obtenons :

$$\text{Cov}(x_i^e, u_i) = \text{Cov}(x_i^e, v_i + \delta_0 q_i) = \delta_0 \times \text{Cov}(x_i^e, q_i)$$

La dernière égalité utilise le fait que $\text{Cov}(x_i^e, v_i) = 0$ dans le modèle latent.

Par conséquent, $x_i^e$ est endogène si et seulement si :
1. $q_i$ est une variable explicative pertinente de $y_i$ (i.e., $\delta_0 \neq 0$), et
2. La variable latente $q_i$ est corrélée à $x_i^e$ (i.e., $\text{Cov}(x_i^e, q_i) \neq 0$)

Cette situation génère le "biais de variable explicative pertinente omise". L'estimateur MCO de $\beta_0$ sera biaisé avec un biais positif si $\delta_0 \times \text{Cov}(x_i^e, q_i) > 0$ et négatif dans le cas contraire. Ce biais provient de la "confusion" entre les effets de $q_i$ et $x_i^e$ sur $y_i$ dans l'estimation par MCO.

### Illustration par l'équation de salaire

L'équation de salaire fournit une illustration classique de ces mécanismes. Supposons $y_i$ représente le salaire de l'individu $i$, $x_i^e$ son niveau d'éducation, $\mathbf{x}_i$ ses autres caractéristiques observées (expérience, âge, sexe), et $q_i$ ses aptitudes non observées ou son origine ethnique.

Cas des aptitudes scolaires : Si $q_i$ représente les aptitudes scolaires, nous avons généralement $\delta_0 > 0$ (les aptitudes "causent" un salaire plus élevé) et $\text{Cov}(x_i^e, q_i) > 0$ (les aptitudes aident à poursuivre des études). Ceci génère un biais positif sur $\beta_0$ : les individus les plus aptes font davantage d'études et obtiennent de meilleurs salaires, créant une surestimation de l'effet causal pur de l'éducation.

Cas de l'origine ethnique : Si $q_i$ représente l'origine ethnique (par exemple, appartenance à une minorité), nous pourrions avoir $\delta_0 \leq 0$ (effet potentiel de discrimination à l'emploi) et $\text{Cov}(x_i^e, q_i) < 0$ (corrélation entre origine minoritaire et difficultés d'accès à l'éducation). Ceci peut générer un biais positif ou négatif selon les magnitudes relatives, compliquant l'interprétation de l'effet causal de l'éducation.

## Principe des variables de contrôle de l'hétérogénéité

### Stratégie fondamentale

Il n'est pas nécessaire de mesurer directement $q_i$ pour résoudre le problème d'endogénéité. La stratégie consiste à identifier une variable ou un vecteur de variables $\mathbf{c}_i$ qui "capte" tout ce qui lie $q_i$ à $x_i^e$ tout en étant exogène par rapport au terme d'erreur $v_i$ du modèle latent.

L'idée repose sur une double observation. D'une part, nous ne pouvons rien faire contre le fait que $\delta_0 \neq 0$ : si $q_i$ est pertinente pour expliquer $y_i$, elle le restera indépendamment de nos efforts. D'autre part, nous pouvons parfois contrôler la "partie" de $q_i$ qui est liée à $x_i^e$, éliminant ainsi la source de l'endogénéité.

### Décomposition de la variable latente

Les variables de contrôle de l'endogénéité doivent permettre une décomposition de $q_i$ sous la forme :

$$q_i = \gamma + \boldsymbol{\rho}'\mathbf{c}_i + \varepsilon_i$$

où cette décomposition satisfait des propriétés essentielles :

1. $\text{Cov}(x_i^e, \varepsilon_i) = 0$ : la partie résiduelle $\varepsilon_i$ n'est pas corrélée à $x_i^e$
2. $\text{Cov}(\mathbf{c}_i, \varepsilon_i) = \mathbf{0}$ : les variables de contrôle ne sont pas corrélées au résidu
3. $\text{Cov}(\mathbf{c}_i, v_i) = \mathbf{0}$ : les variables de contrôle sont exogènes dans le modèle latent

Ces conditions garantissent que $\boldsymbol{\rho}'\mathbf{c}_i$ "capte" exactement ce qui lie $q_i$ à $x_i^e$, éliminant ainsi la source de l'endogénéité.

### Construction du modèle contrôlé

En substituant cette décomposition dans le modèle latent, nous obtenons :

$$y_i = \alpha_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \delta_0(\gamma + \boldsymbol{\rho}'\mathbf{c}_i + \varepsilon_i) + v_i$$

Ce qui se réécrit :

$$y_i = (\alpha_0 + \delta_0\gamma) + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + (\delta_0\boldsymbol{\rho})'\mathbf{c}_i + (v_i + \delta_0\varepsilon_i)$$

En définissant $\theta_0 = \alpha_0 + \delta_0\gamma$, $\boldsymbol{\pi}_0 = \delta_0\boldsymbol{\rho}$, et $\eta_i = v_i + \delta_0\varepsilon_i$, nous obtenons le modèle contrôlé :

$$y_i = \theta_0 + \mathbf{x}_i'\boldsymbol{\beta}_0 + x_i^e \beta_0 + \boldsymbol{\pi}_0'\mathbf{c}_i + \eta_i$$

### Propriétés du modèle contrôlé

Le modèle contrôlé constitue un modèle de régression linéaire standard. En effet, les propriétés de la décomposition de $q_i$ impliquent :

1. $\text{Cov}(\mathbf{x}_i, \eta_i) = \mathbf{0}$ : les variables $\mathbf{x}_i$ restent exogènes
2. $\text{Cov}(x_i^e, \eta_i) = 0$ : la variable $x_i^e$ devient exogène grâce au contrôle
3. $\text{Cov}(\mathbf{c}_i, \eta_i) = \mathbf{0}$ : les variables de contrôle sont exogènes par construction

Ces propriétés garantissent que l'estimateur MCO appliqué au modèle contrôlé est convergent pour tous les paramètres, y compris $\beta_0$ qui représente l'effet causal d'intérêt de $x_i^e$ sur $y_i$.

### Mécanisme d'action des variables de contrôle

L'équation $q_i = \gamma + \boldsymbol{\rho}'\mathbf{c}_i + \varepsilon_i$ révèle le mécanisme par lequel les variables de contrôle éliminent l'endogénéité. La variable latente $q_i$ se décompose en trois termes :

1. Une constante $\gamma$ dont l'effet se fond dans l'ordonnée à l'origine du modèle contrôlé
2. Un terme $\boldsymbol{\rho}'\mathbf{c}_i$ qui contrôle l'endogénéité de $x_i^e$ en captant ce qui lie $q_i$ à cette variable
3. Un terme résiduel $\varepsilon_i$ dont l'effet s'ajoute au terme d'erreur mais ne génère plus d'endogénéité

La transformation du modèle non contrôlé au modèle contrôlé élimine effectivement l'endogénéité : dans le premier, $x_i^e$ est corrélée à $u_i$ via $q_i$, tandis que dans le second, $x_i^e$ n'est plus corrélée à $\eta_i$ grâce au contrôle exercé par $\boldsymbol{\rho}'\mathbf{c}_i$.

## Applications et exemples

### Retour sur l'équation de salaire

Contrôle des aptitudes scolaires : Pour contrôler l'effet des aptitudes non observées, le choix usuel de $\mathbf{c}_i$ se limite souvent à des scores de tests standardisés comme le QI. Ces tests ne mesurent qu'une partie des aptitudes individuelles, principalement celles liées au raisonnement logique. Cependant, ces aptitudes constituent généralement les plus utiles pour les études et la carrière professionnelle, rendant le contrôle partiellement efficace.

Contrôle de l'origine : Dans le cas de l'origine ethnique, il n'existe généralement pas de variable de contrôle efficace autre que $q_i$ elle-même (l'origine). Cette situation nécessite soit une mesure directe de la variable (quand elle est légalement et éthiquement collectible), soit le recours aux techniques de VI. Sans mesure de $q_i$, il devient difficile, voire impossible, de mesurer statistiquement les phénomènes de discrimination.

### Problèmes de "mauvais contrôle"

L'utilisation inappropriée de variables de contrôle peut générer des biais supplémentaires. Deux exemples typiques illustrent ces écueils dans le contexte de l'équation de salaire :

Utilisation de la catégorie socioprofessionnelle (CSP) : Bien que la CSP soit liée aux aptitudes individuelles, elle constitue largement une conséquence du niveau d'éducation. Son introduction comme variable de contrôle capture certes l'effet des aptitudes, mais élimine simultanément l'essentiel de l'effet causal de l'éducation sur le salaire, sous-estimant ainsi le paramètre d'intérêt.

Utilisation des résultats de tests d'embauche : Si ces résultats dépendent des aptitudes individuelles, ils dépendent également du niveau d'éducation. Une partie de l'effet de l'éducation transite par la performance aux tests, créant un biais de sous-estimation lorsque ces résultats sont utilisés comme variables de contrôle.

Ces exemples soulignent l'importance de distinguer entre variables de contrôle appropriées (qui captent uniquement ce qui lie la variable latente à la variable d'intérêt) et variables de contrôle inappropriées (qui captent également une partie de l'effet causal d'intérêt).

## Propriétés théoriques et limites

### Flexibilité de la spécification

La forme linéaire de l'effet de $\mathbf{c}_i$ sur $q_i$ dans $q_i = \gamma + \boldsymbol{\rho}'\mathbf{c}_i + \varepsilon_i$ n'est pas véritablement restrictive. Les éléments de $\mathbf{c}_i$ peuvent être choisis de manière flexible, incluant des transformations non linéaires, des interactions, ou des fonctions des variables originales. Le terme $\boldsymbol{\rho}'\mathbf{c}_i$ peut être conceptualisé comme la projection linéaire optimale $E[q_i | \mathbf{c}_i]$.

### Hypothèses simplificatrices

La condition $\text{Cov}(q_i, \mathbf{x}_i) = \mathbf{0}$ utilisée dans le développement théorique visait principalement à distinguer clairement les rôles des vecteurs $\mathbf{x}_i$ et $\mathbf{c}_i$. Dans le modèle final, ces deux groupes de variables jouent des rôles à la fois similaires et distincts : tous améliorent la prédiction de $y_i$ et la précision des estimateurs, mais seul $\mathbf{c}_i$ contrôle l'endogénéité de $x_i^e$.

### Différences avec les variables instrumentales

Les variables instrumentales $\mathbf{z}_i$ et les variables de contrôle $\mathbf{c}_i$ présentent des natures fondamentalement différentes. Bien que les deux doivent être liées à $x_i^e$, leurs relations avec la variable latente $q_i$ sont opposées : $\mathbf{z}_i$ doit être non corrélé à $q_i$ (condition d'exclusion), tandis que $\mathbf{c}_i$ doit être le plus corrélé possible à $q_i$ pour maximiser l'efficacité du contrôle.

### Limitations de scope

L'approche par variables de contrôle ne peut traiter que l'endogénéité due à l'omission de variables explicatives pertinentes. Elle s'avère inefficace pour les problèmes de simultanéité ou d'erreurs de mesure.

Simultanéité : Si $x_i^e$ et $y_i$ sont simultanément déterminées, $\mathbf{c}_i$ devrait contrôler entièrement $u_i$ pour éliminer l'endogénéité, ce qui équivaudrait à disposer d'un modèle "parfait" - situation impossible en pratique.

Erreurs de mesure : Si $x_i^e$ est une mesure bruitée d'une variable d'intérêt, $\mathbf{c}_i$ devrait contrôler entièrement l'erreur de mesure concernée, impliquant une connaissance complète de cette erreur - situation également irréaliste.

### Considérations pratiques

En pratique, le raisonnement sous-jacent au choix des variables de contrôle est souvent moins formel que ne le suggère le développement théorique. Les économètres s'appuient généralement sur leur connaissance du domaine d'application et leur compréhension des mécanismes économiques pour identifier les variables susceptibles de contrôler efficacement l'hétérogénéité non observée.

La spécification de l'ensemble d'information du modèle - incluant ses variables explicatives exogènes, ses variables de contrôle de l'hétérogénéité, et ses variables instrumentales - constitue une phase essentielle du travail économétrique. Cette tâche requiert une analyse approfondie du processus générateur des données et suppose une connaissance substantielle du phénomène modélisé, confirmant une fois encore que "l'économétrie, c'est d'abord de l'économie".

## Synthèse et perspectives

L'approche par variables de contrôle de l'hétérogénéité offre un complément précieux aux techniques de variables instrumentales pour traiter les problèmes d'endogénéité. Sa force réside dans sa capacité à éliminer complètement certains types de problèmes d'endogénéité en modélisant explicitement leurs mécanismes générateurs.

Cette méthode trouve sa pertinence maximale lorsque l'endogénéité provient de l'omission de variables explicatives pertinentes et que des proxy appropriés de ces variables omises sont disponibles. Dans de telles situations, elle peut s'avérer plus efficace que les techniques de VI, particulièrement lorsque des instruments valides sont difficiles à identifier.

Cependant, le succès de cette approche dépend critiquement de la qualité des variables de contrôle utilisées. Le choix de ces variables requiert une compréhension approfondie des mécanismes économiques sous-jacents et des sources potentielles d'hétérogénéité non observée. Cette exigence souligne l'importance de l'expertise substantielle dans le domaine d'application, au-delà des seules considérations techniques économétriques.

En définitive, les variables de contrôle de l'hétérogénéité ne constituent ni une panacée ni un substitut universel aux variables instrumentales, mais plutôt un outil complémentaire dans l'arsenal de l'économètre pour identifier correctement les relations causales d'intérêt. Leur utilisation optimale s'inscrit dans une démarche plus large de spécification rigoureuse des modèles économétriques, guidée par la théorie économique et la connaissance institutionnelle du phénomène étudié.