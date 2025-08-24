## 04 // systèmes d’équations simultanées

[04_systemes_d'equations_simultanees_l4_equations_simultanees.pdf](ressources/04_systemes_d'equations_simultanees_l4_equations_simultanees.pdf)

## Systèmes d'équations simultanées

### Motivation et fondements historiques

L'économétrie moderne trouve ses racines dans l'étude des systèmes d'équations simultanées, développés initialement pour résoudre les problèmes d'endogénéité liés à la simultanéité des prix et des quantités échangées sur les marchés en équilibre. Ces problèmes constituent les premières manifestations identifiées de l'endogénéité en économétrie, discipline qui s'est ainsi distinguée comme une branche spécifique de la statistique.

L'approche par systèmes d'équations simultanées offre un cadre général pour traiter tout problème d'endogénéité. Elle se caractérise par une perspective d'information complète où chaque variable endogène du système fait l'objet d'une modélisation causale explicite. Cette approche se distingue des techniques de variables instrumentales présentées précédemment par sa nature systémique et sa capacité à exploiter simultanément l'ensemble des relations causales du modèle.

### Exemple illustratif : délinquance économique et chômage

L'interaction entre délinquance économique et chômage fournit un exemple paradigmatique des relations causales bidirectionnelles. Cette étude, inspirée des travaux de Fougère, Kramarz et Pouget (2007), utilise des données départementales françaises pour la période 1990-2000 et illustre parfaitement la complexité des systèmes d'équations simultanées.

#### Mécanismes causaux bidirectionnels

La relation causale du chômage vers la délinquance économique opère principalement par le mécanisme des opportunités légales et illégales. L'absence d'opportunités légales de revenu favorise le recours aux activités illégales, particulièrement pour les cambriolages, vols et trafic de stupéfiants. Cette relation est modulée par plusieurs facteurs : la présence policière, les aides aux chômeurs et la densité du tissu économique l'atténuent, tandis que la densité de population, les inégalités de revenu et l'implantation du crime organisé l'accentuent.

Réciproquement, la délinquance économique influence le chômage par son impact sur les décisions de localisation des entreprises. À moyen terme, la délinquance décourage l'implantation d'entreprises dans les zones affectées, contribuant ainsi à la persistance du chômage local. L'éducation, les aides à l'implantation d'entreprises et la densité de population peuvent atténuer cet effet.

#### Formalisation mathématique

Cette double causalité se traduit par le système d'équations simultanées suivant :

$$
\begin{cases}
\text{déli}_i = a_0 + b_0 \times \text{chom}_i + e_i \\
\text{chom}_i = \alpha_0 + \beta_0 \times \text{déli}_i + \varepsilon_i
\end{cases}
$$

où $E[e_i] = E[\varepsilon_i] = 0$, mais cruciale ment :

$$
\text{Cov}(\text{chom}_i, e_i) \neq 0 \quad \text{et} \quad \text{Cov}(\text{déli}_i, \varepsilon_i) \neq 0
$$

Cette structure révèle le problème fondamental : les variables explicatives sont endogènes dans chaque équation, rendant impossible l'estimation directe des paramètres causaux $b_0$ et $\beta_0$ par les moindres carrés ordinaires.

### Définitions et concepts fondamentaux

Un **système d'équations simultanées** se caractérise par deux propriétés essentielles : premièrement, au moins une équation contient une variable explicative endogène ; deuxièmement, chaque variable endogène possède "son" équation structurelle. Cette définition se distingue d'un **système de régressions empilées**, qui consiste simplement en un empilement de modèles de régression sans variables explicatives endogènes.

Le système précédent illustre parfaitement cette définition : chaque équation contient la variable endogène de l'autre comme variable explicative, créant une interdépendance qui ne peut être résolue par des techniques d'estimation conventionnelles.

#### Problème d'identification

Le défi central réside dans le problème d'identification, qui manifeste un déficit d'information fondamental. Contrairement aux techniques précédentes utilisant des variables instrumentales externes ou des variables de contrôle, l'approche par systèmes d'équations simultanées utilise conjointement ces deux solutions dans un cadre d'information complète.

Le modèle structurel complet incorpore l'ensemble des déterminants des variables endogènes :

**Équation de délinquance :**

$$
\text{déli}_i = a_0 + b_0 \times \text{chom}_i + \mathbf{d}_0' \mathbf{q}_{d,i} + \mathbf{r}_0' \mathbf{q}_{i} + u_{d,i}
$$

**Équation de chômage :**

$$
\text{chom}_i = \alpha_0 + \beta_0 \times \text{déli}_i + \boldsymbol{\delta}_0' \mathbf{q}_{i} + \boldsymbol{\rho}_0' \mathbf{q}_{c,i} + u_{c,i}
$$

où :

- $\mathbf{q}_{d,i}$ : variables spécifiques à l'équation de délinquance (éducation, inégalités, criminalité organisée, police, aides aux chômeurs)
- $\mathbf{q}_{c,i}$ : variables spécifiques à l'équation de chômage (prévisions de croissance)
- $\mathbf{q}_i$ : variables communes (densité de population, tissu économique)

### Formes structurelle et réduite

#### Forme structurelle

La **forme structurelle** du système d'équations simultanées décrit les relations causales d'intérêt dans leur forme naturelle. Pour le modèle général, elle s'écrit :

$$
\begin{cases}
y_{d,i} = a_0 + b_0 y_{c,i} + \mathbf{d}_0' \mathbf{q}_{d,i} + \mathbf{r}_0' \mathbf{q}_i + u_{d,i} \\
y_{c,i} = \alpha_0 + \beta_0 y_{d,i} + \boldsymbol{\delta}_0' \mathbf{q}_i + \boldsymbol{\rho}_0' \mathbf{q}_{c,i} + u_{c,i}
\end{cases}
$$

avec $E[\mathbf{u}_i|\mathbf{z}_i] = \mathbf{0}$ où $\mathbf{u}_i = (u_{d,i}, u_{c,i})'$ et $\mathbf{z}_i = (1, \mathbf{q}_i', \mathbf{q}_{d,i}', \mathbf{q}_{c,i}')$ représente l'ensemble des variables exogènes du système.

Sous forme matricielle compacte :

$$
\begin{pmatrix}
1 & -b_0 \\
-\beta_0 & 1
\end{pmatrix}
\begin{pmatrix}
y_{d,i} \\
y_{c,i}
\end{pmatrix} = 
\begin{pmatrix}
a_0 & \mathbf{d}_0' & \mathbf{r}_0' & \mathbf{0}' \\
\alpha_0 & \boldsymbol{\delta}_0' & \mathbf{0}' & \boldsymbol{\rho}_0'
\end{pmatrix}
\begin{pmatrix}
1 \\
\mathbf{q}_i \\
\mathbf{q}_{d,i} \\
\mathbf{q}_{c,i}
\end{pmatrix} + 
\begin{pmatrix}
u_{d,i} \\
u_{c,i}
\end{pmatrix}
$$

#### Forme réduite

La **forme réduite** exprime chaque variable endogène comme une fonction linéaire exclusive des variables exogènes du système. Sa dérivation procède par substitution algébrique, éliminant les variables endogènes du côté droit des équations.

En résolvant le système matriciel précédent, on obtient :

$$
\begin{pmatrix}
y_{d,i} \\
y_{c,i}
\end{pmatrix} = 
\frac{1}{\Delta}
\begin{pmatrix}
1 & b_0 \\
\beta_0 & 1
\end{pmatrix}
\begin{pmatrix}
a_0 & \mathbf{d}_0' & \mathbf{r}_0' & \mathbf{0}' \\
\alpha_0 & \boldsymbol{\delta}_0' & \mathbf{0}' & \boldsymbol{\rho}_0'
\end{pmatrix}
\begin{pmatrix}
1 \\
\mathbf{q}_i \\
\mathbf{q}_{d,i} \\
\mathbf{q}_{c,i}
\end{pmatrix} + \mathbf{v}_i
$$

où $\Delta = 1 - b_0\beta_0$ représente le déterminant du système (supposé non nul pour l'existence d'un équilibre) et $\mathbf{v}_i$ les termes d'erreur de la forme réduite.

La forme réduite finale s'écrit :

$$
\begin{cases}
y_{d,i} = \pi_{d,1} + \pi_{d,2}' \mathbf{q}_i + \pi_{d,3}' \mathbf{q}_{d,i} + \pi_{d,4}' \mathbf{q}_{c,i} + v_{d,i} \\
y_{c,i} = \pi_{c,1} + \pi_{c,2}' \mathbf{q}_i + \pi_{c,3}' \mathbf{q}_{d,i} + \pi_{c,4}' \mathbf{q}_{c,i} + v_{c,i}
\end{cases}
$$

Les paramètres de forme réduite $\boldsymbol{\pi}_d$ et $\boldsymbol{\pi}_c$ s'expriment en fonction des paramètres structurels selon :

$$
\boldsymbol{\pi}_d = \frac{1}{\Delta}\begin{pmatrix}
a_0 + b_0\alpha_0 \\
\mathbf{d}_0 + b_0\boldsymbol{\delta}_0 \\
\mathbf{r}_0 \\
b_0\boldsymbol{\rho}_0
\end{pmatrix}, \quad
\boldsymbol{\pi}_c = \frac{1}{\Delta}\begin{pmatrix}
\alpha_0 + \beta_0 a_0 \\
\boldsymbol{\delta}_0 + \beta_0 \mathbf{d}_0 \\
\beta_0 \mathbf{r}_0 \\
\boldsymbol{\rho}_0
\end{pmatrix}
$$

Cette forme réduite constitue un système de régressions empilées où les conditions d'exogénéité $E[\mathbf{v}_i|\mathbf{z}_i] = \mathbf{0}$ sont satisfaites par construction.

### Estimation par les moindres carrés indirects (MCI)

#### Principe de l'estimateur des MCI

L'approche par les moindres carrés indirects exploite la structure du système pour décomposer l'estimation en quatre étapes séquentielles. Premièrement, la définition des variables endogènes sous forme de modèles de régression donne la forme réduite. Deuxièmement, l'établissement des relations entre paramètres structurels et réduits. Troisièmement, l'estimation des paramètres réduits par moindres carrés ordinaires sur chaque équation de la forme réduite. Quatrièmement, le calcul des paramètres structurels par inversion des relations précédentes.

#### Cas juste-identifié

Dans le cas juste-identifié, le nombre de paramètres réduits égale le nombre de paramètres structurels, permettant une bijection exacte. Pour le modèle simplifié avec huit paramètres structurels et huit paramètres réduits, le système d'inversion s'écrit :

$$
\begin{cases}
b_0 = \frac{\pi_{d,4}}{\pi_{c,4}}, \quad a_0 = \pi_{d,1} - b_0\pi_{c,1}, \quad d_0 = \pi_{d,2} - b_0\pi_{c,2}, \quad r_0 = \frac{\pi_{d,3}}{\Delta} \\
\beta_0 = \frac{\pi_{c,3}}{\pi_{d,3}}, \quad \alpha_0 = \pi_{c,1} - \beta_0\pi_{d,1}, \quad \delta_0 = \pi_{c,2} - \beta_0\pi_{d,2}, \quad \rho_0 = \frac{\pi_{c,4}}{\Delta}
\end{cases}
$$

Les **estimateurs des MCI** se définissent alors comme :

$$
\hat{\mathbf{g}}_N^{MCI} = \mathbf{g}(\hat{\boldsymbol{\pi}}_{d,N}^{MCO}, \hat{\boldsymbol{\pi}}_{c,N}^{MCO}) \quad \text{et} \quad \hat{\boldsymbol{\gamma}}_N^{MCI} = \boldsymbol{\gamma}(\hat{\boldsymbol{\pi}}_{d,N}^{MCO}, \hat{\boldsymbol{\pi}}_{c,N}^{MCO})
$$

#### Propriétés de convergence

La convergence des estimateurs des MCI découle directement de la convergence en probabilité des estimateurs de la forme réduite :

$$
\hat{\boldsymbol{\pi}}_{d,N}^{MCO} \xrightarrow{p} \boldsymbol{\pi}_d \quad \text{et} \quad \hat{\boldsymbol{\pi}}_{c,N}^{MCO} \xrightarrow{p} \boldsymbol{\pi}_c
$$

Par continuité des fonctions $\mathbf{g}(\cdot)$ et $\boldsymbol{\gamma}(\cdot)$, on obtient :

$$
\hat{\mathbf{g}}_N^{MCI} \xrightarrow{p} \mathbf{g}_0 \quad \text{et} \quad \hat{\boldsymbol{\gamma}}_N^{MCI} \xrightarrow{p} \boldsymbol{\gamma}_0
$$

## Conditions d'identification

### Identification dans le cas juste-identifié

L'identification des paramètres structurels nécessite des conditions spécifiques sur les paramètres réduits. Les paramètres $\mathbf{g}_0$ ne sont identifiables que si $\pi_{c,4} \neq 0$ (équivalent à $\rho_0 \neq 0$), tandis que $\boldsymbol{\gamma}_0$ nécessite $\pi_{d,3} \neq 0$ (équivalent à $r_0 \neq 0$).

Ces conditions révèlent le rôle fondamental des **variables exogènes spécifiques**. La variable $\mathbf{q}_{c,i}$ doit avoir un effet direct non nul sur $y_{c,i}$ pour servir d'instrument valide à $y_{c,i}$ dans l'équation de $y_{d,i}$. Symétriquement, $\mathbf{q}_{d,i}$ doit affecter directement $y_{d,i}$ pour instrumenter cette variable dans l'équation de $y_{c,i}$.

### Équivalence avec l'estimation par variables instrumentales

L'approche par MCI révèle une équivalence fondamentale avec l'estimation par variables instrumentales appliquée équation par équation. Chaque équation du système structurel constitue un modèle à variables instrumentales où les variables endogènes explicatives sont instrumentées par les variables exogènes spécifiques de l'autre équation.

Pour l'équation de $y_{d,i}$ :

$$
y_{d,i} = \mathbf{g}_0' \mathbf{x}_{d,i} + u_{d,i}
$$

avec $\mathbf{x}_{d,i} = (1, y_{c,i}, \mathbf{q}_{d,i}', \mathbf{q}_i')'$ et le vecteur d'instruments $\mathbf{z}_i = (1, \mathbf{q}_i', \mathbf{q}_{d,i}', \mathbf{q}_{c,i})'$.

L'estimateur par variables instrumentales s'écrit :

$$
\hat{\mathbf{g}}_N^{VI} = \left(\sum_{i=1}^N \mathbf{x}_{d,i} \mathbf{z}_i' \right)^{-1} \left(\sum_{i=1}^N \mathbf{z}_i \mathbf{z}_i' \right)^{-1} \sum_{i=1}^N \mathbf{z}_i y_{d,i}
$$

Dans le cas juste-identifié, on démontre l'égalité $\hat{\mathbf{g}}_N^{MCI} = \hat{\mathbf{g}}_N^{VI}$, établissant l'équivalence conceptuelle entre les deux approches.

## Estimation par doubles moindres carrés et conditions générales

### Extension au cas sur-identifié

Pour le modèle général non nécessairement juste-identifié, la forme réduite devient :

$$
\begin{cases}
y_{d,i} = \boldsymbol{\pi}_d' \mathbf{z}_i + v_{d,i} \\
y_{c,i} = \boldsymbol{\pi}_c' \mathbf{z}_i + v_{c,i}
\end{cases}
$$

Le système d'inversion des paramètres réduits en paramètres structurels compte désormais $2 \times \dim(\mathbf{z}_i)$ équations pour $2 \times (2 + \dim(\mathbf{q}_{d,i}) + \dim(\mathbf{q}_{c,i}))$ inconnues.

Dans le cas sur-identifié où $\dim(\mathbf{q}_{d,i}) + \dim(\mathbf{q}_{c,i}) - 2 > 0$, le système est sur-déterminé, rendant impossible l'application directe des MCI. L'estimation par **doubles moindres carrés** (2MC) équation par équation devient alors la méthode privilégiée.

### Conditions d'ordre et de rang

#### Condition d'ordre

Pour l'équation $m$ du système général :

$$
y_{m,i} = a_{m,0} + \mathbf{b}_{m,0}' \mathbf{y}_{m,i} + \mathbf{d}_{m,0}' \mathbf{q}_{m,i} + \mathbf{r}_{m,0}' \mathbf{q}_{m,i}^s + u_{m,i}
$$

la condition d'ordre s'énonce :

$$
\dim(\mathbf{z}_i) \geq 1 + \dim(\mathbf{y}_{m,i}) + \dim(\mathbf{q}_{m,i}) + \dim(\mathbf{q}_{m,i}^s)
$$

Cette condition exprime que le nombre de variables exogènes du système doit au moins égaler le nombre de variables explicatives de l'équation considérée.

#### Condition de rang (version simplifiée)

Une condition presque suffisante pour la condition de rang exige que $\dim(\mathbf{q}_{m,i}^s) > 0$ pour tout $m$, c'est-à-dire que chaque variable endogène possède des variables explicatives qui lui sont spécifiques et n'apparaissent pas dans les autres équations.

Cette condition garantit l'existence d'instruments valides pour chaque variable endogène explicative, bien qu'elle ne soit ni nécessaire ni suffisante dans le cas général.

## Estimation en système versus équation par équation

### Estimateur des triples moindres carrés

Pour les systèmes sur-identifiés, l'estimateur des **triples moindres carrés** (3MC) constitue l'extension naturelle des MCI. Cet estimateur exploite pleinement la structure du système en tenant compte des corrélations contemporaines entre les termes d'erreur des différentes équations.

L'estimateur 3MC améliore généralement l'efficacité asymptotique par rapport à l'approche équation par équation, mais au prix d'une plus grande fragilité : une mauvaise spécification d'une seule équation compromet l'estimation de l'ensemble des paramètres du système.

### Arbitrage efficacité-robustesse

L'arbitrage entre estimation en système et équation par équation reflète un compromis fondamental entre efficacité et robustesse. L'estimation en système, plus efficace asymptotiquement, suppose une spécification correcte de l'ensemble du modèle. L'estimation équation par équation, bien que généralement moins efficace, offre une robustesse supérieure aux erreurs de spécification.

En pratique, cet arbitrage se résout généralement en faveur de la robustesse, particulièrement lorsque l'intérêt porte sur un sous-ensemble des paramètres structurels plutôt que sur l'ensemble du système.

### Inférence en information complète versus limitée

#### Inférence en information complète

L'approche en information complète, typique des estimateurs 3MC ou MCI, exploite l'ensemble de l'information contenue dans le système. Elle suppose :

1. La spécification correcte de toutes les équations du système
2. La linéarité de chaque équation en ses variables explicatives
3. L'exogénéité de l'ensemble des variables instrumentales par rapport à tous les termes d'erreur

Cette approche maximise l'efficacité asymptotique mais reste vulnérable aux erreurs de spécification.

#### Inférence en information limitée

L'approche en information limitée, illustrée par l'estimation 2MC équation par équation, ne requiert que :

1. La spécification correcte de l'équation d'intérêt
2. L'existence d'instruments valides pour les variables endogènes explicatives de cette équation
3. Les conditions de rang appropriées

Cette approche, bien que potentiellement moins efficace, offre une robustesse considérablement supérieure. Dans l'exemple de Fougère, Kramarz et Pouget, l'intérêt principal portant sur l'effet causal du chômage sur la délinquance, l'estimation de la seule équation de délinquance par 2MC suffit, sans nécessiter la spécification d'un modèle complet pour le chômage.

## Distribution asymptotique des estimateurs MCI

### Application de la méthode delta

La distribution asymptotique des estimateurs MCI découle de celle des estimateurs de la forme réduite via la méthode delta. Si :

$$
\sqrt{N}(\hat{\boldsymbol{\pi}}_N^{MCO} - \boldsymbol{\pi}_0) \xrightarrow{L} \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_0)
$$

alors :

$$
\sqrt{N}(\hat{\boldsymbol{\theta}}_N^{MCI} - \boldsymbol{\theta}_0) \xrightarrow{L} \mathcal{N}\left(\mathbf{0}, \frac{\partial \mathbf{h}(\boldsymbol{\pi}_0)}{\partial \boldsymbol{\pi}'} \boldsymbol{\Sigma}_0 \frac{\partial \mathbf{h}(\boldsymbol{\pi}_0)'}{\partial \boldsymbol{\pi}}\right)
$$

où $\boldsymbol{\theta}_0 = \mathbf{h}(\boldsymbol{\pi}_0)$ avec $\mathbf{h}(\cdot) = (\mathbf{g}(\cdot)', \boldsymbol{\gamma}(\cdot)')'$.

### Calcul de la matrice de variance-covariance

La matrice de variance-covariance asymptotique de l'estimateur de la forme réduite s'exprime, en utilisant les produits de Kronecker :

$$
\boldsymbol{\Sigma}_0 = E\left[\left(\mathbf{I}_2 \otimes \mathbf{z}_i\mathbf{z}_i'\right)^{-1} \left(\mathbf{I}_2 \otimes \mathbf{z}_i\right) \mathbf{v}_i\mathbf{v}_i' \left(\mathbf{I}_2 \otimes \mathbf{z}_i'\right) \left(\mathbf{I}_2 \otimes \mathbf{z}_i\mathbf{z}_i'\right)^{-1}\right]
$$

Dans le cas homoscédastique où $E[\mathbf{v}_i\mathbf{v}_i'|\mathbf{z}_i] = \boldsymbol{\Omega}_0$, cette expression se simplifie en :

$$
\boldsymbol{\Sigma}_0 = \boldsymbol{\Omega}_0 \otimes E[\mathbf{z}_i\mathbf{z}_i']^{-1}
$$

L'estimateur empirique de $\boldsymbol{\Sigma}_0$ s'obtient par substitution des estimateurs empiriques correspondants, permettant l'inférence statistique standard sur les paramètres structurels estimés par MCI.

### Efficacité asymptotique

Dans le cas juste-identifié, les estimateurs MCI atteignent l'efficacité asymptotique, égalisant les performances des estimateurs par variables instrumentales. Cette propriété découle de l'utilisation optimale de toute l'information disponible dans le système, sans perte due à la sur-identification.

L'équivalence entre estimateurs MCI et VI dans le cas juste-identifié illustre l'unité conceptuelle des approches d'estimation en présence d'endogénéité, malgré leurs formulations apparemment différentes.
