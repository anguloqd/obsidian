# 03 // non respect des hypothèses

[Économetrie 1 - Chap. #4.1](ressources/03_non_respect_des_hypotheses_4_chapitre4_partie41_econometrie1_202232024.pdf)

[Économetrie 1 - Chap. #4.2](ressources/03_non_respect_des_hypotheses_5_chapitre4_partie42_econometrie1_20232024.pdf)

[Économetrie 1 - Chap. #4.3](ressources/03_non_respect_des_hypotheses_6_chapitre4_partie43_econometrie1_20232024.pdf)

# Outils importants

## Rappel : hypothèses fondamentales

Les cinq hypothèses du cas linéaire simple sont légèrement changées dans le cas général :

- $H_1$ : $\mathbb{E} [u_i] = 0$
- $H_2$, variance constante : $\text{Var}(\mathbf{u})=\mathbb{E}[\mathbf{u}\mathbf{u}^T]=\sigma^2_u I_n$.
- $H_3$ : la matrice $\mathbf{X}$ est non aléatoire.
- $H_4$, spécificité : le modèle est correctement spécifié.
Dans ce cas c'est linéaire, donc $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \mathbf{u}$.
- $H_5$, non colinéarité: la matrice $\mathbf{X}$ est de plein rang, càd $k+1 < n$.
Comme rappel, $\mathbf{X}$ est de dimension $(n, k+1)$.

## Implications de $H_2$ et non respect

De la forme plus générale, càd. sans savoir si $H_2$ est respectée ou non, on peut écrire la variance des estimateurs comme :

$$
V(\hat{\boldsymbol{\beta}})=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbb{E}[\mathbf{u}\mathbf{u}^T]\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}
$$

- Si $H_2$ est respectée, cette expression devient donc :
    
    $$
    V(\hat{\boldsymbol{\beta}})=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\underbrace{\mathbb{E}[\mathbf{u}\mathbf{u}^T]}_{\sigma^2_u I_n}\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}=\sigma^2_u(\mathbf{X}^T\mathbf{X})^{-1}
    $$
    
- Si, par contre, $H_2$ n'est pas respectée :

$$
V(\mathbf{u})= \mathbb{E}[\mathbf{u}\mathbf{u}^T]=\sigma^2_u\Omega \neq \sigma^2_u I_n

\\[10pt]

\implies V(\hat{\boldsymbol{\beta}})=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\underbrace{\mathbb{E}[\mathbf{u}\mathbf{u}^T]}_{\sigma^2_u \Omega}\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}
$$

La variance des perturbations $\mathbf{u}$ prend une forme différente dans les deux cas :

$$
\begin{aligned}
V(\mathbf{u}) = E\left[\mathbf{u} \mathbf{u}^T\right] &=\begin{bmatrix}
\sigma_u^2 & 0 & 0 & 0 & 0 \\
0 & \sigma_u^2 & 0 & \cdots & 0 \\
0 & 0 & \sigma_u^2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \sigma_u^2
\end{bmatrix}

\\[30pt]

&= \sigma_u^2 \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{bmatrix}

= \sigma_u^2 I_N 

\end{aligned}

\\[10pt]

\text{Hétéroscédasticité : } V(\mathbf{u}) = \begin{bmatrix}
\omega_{11} & 0 & 0 & \cdots & 0 \\
0 & \omega_{22} & 0 & \cdots & 0 \\
0 & 0 & \omega_{33} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \omega_{NN}
\end{bmatrix}

\\[10pt]

\text{Autocorrelation : } V(\mathbf{u}) = \begin{bmatrix}
1 & \omega_{12} & \omega_{13} & \cdots & \omega_{1N} \\
\omega_{21} & 1 & \omega_{31} & \cdots & \omega_{2N} \\
\omega_{31} & \omega_{32} & 1 & \cdots & \omega_{3N} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\omega_{N1} & \omega_{N2} & \omega_{N3} & \cdots & 1
\end{bmatrix}

$$

# Hétéroscédasticité $(H_2)$

## Définition

$H_2$, l'hypothèse de variance constante ou homoscédasticité, nous assure que la variance des perturbations est constante pour toute valeur réalisée de $\mathbf{X}$. Justement, quand ce n'est plus le cas, on parle d'hétéroscédasticité.

L'hétéroscédasticité a une conséquence importante : on n'a plus de variance minimale sur les estimateurs $\hat{\boldsymbol{\beta}}$ de $\boldsymbol{\beta}$ ! $\hat{\boldsymbol{\beta}}$ n'est donc plus un estimateur efficace. Les estimateurs $\hat{\boldsymbol{\beta}}$ peuvent rester quand même des estimateurs **sans biais** et **convergents** si les autres hypothèses sont vérifiées.

![untitled](ressources/03_non_respect_des_hypotheses_untitled.png)

![untitled](ressources/03_non_respect_des_hypotheses_untitled_1.png)

En termes rigoureux, $H_2$ n'est pas respectée quand :

$$
\text{Var}(\mathbf{u})=\mathbb{E}[\mathbf{u}\mathbf{u}^T]=\sigma^2_u\Omega \neq \sigma^2_u I_n
$$

Ici, $\Omega$ est une matrice qui est différente de la matrice identité $I_n$. On expliquera l'aspect de cette matrice $\Omega$ plus tard. 

## Contexte

Le plus souvent, on retrouve les problèmes d’hétéroscédasticité avec des données en coupe transversale. Ceci est expliqué par les situations suivantes :

- Mauvaise spécification, i.e. $H_4$ non respectée
- Présence de valeurs extrêmes
- Même variable expliquée est répétée pour des valeurs différentes d’une variable explicative
- Observations représentent des moyennes calculées sur des échantillons de taille différentes
- Taille des erreurs est liée, de façon proportionnelle, aux valeurs prises par une variable explicative dans le modèle

## Identifier l’hétéroscédasticité : stats. descriptives

Une première manière d’identifier l’hétéroscédasticité c’est de voir les statistiques descriptives : voir des graphiques, mais aussi de voir des gros différence entre deux sous-échantillons de l’échantillon. **C’est une méthode informelle car nous ne savons pas si cette différence est statistiquement significative**.

![untitled](ressources/03_non_respect_des_hypotheses_untitled_2.png)

![“restaurn” est 0 si la zone n’applique pas des restrictions pour fumer dans les restaurants, et 1 sinon. “cigs” est la quantité de cigarettes fumées. Si on voit seulement les zones où restaurn=0 (un sous-échantillon), on voit que la variance est différente de si restaurn=1 (un autre sous-echantillon).](ressources/03_non_respect_des_hypotheses_untitled_3.png)

“restaurn” est 0 si la zone n’applique pas des restrictions pour fumer dans les restaurants, et 1 sinon. “cigs” est la quantité de cigarettes fumées. Si on voit seulement les zones où restaurn=0 (un sous-échantillon), on voit que la variance est différente de si restaurn=1 (un autre sous-échantillon).

## Identifier l’hétéroscédasticité : tests

Une deuxième manière c’est d’estimer les MCO, puis vois le graphique des résidus au carré vs. $\hat y$. Encore une autre manière c’est de lancer des tests d’hétéroscédasticité : test de Breuch-Pagan, ou le test de White qui est plus général.

### Test de Breuch-Pagan

Ça commence par estimer le modèle par les MCO. On obtient donc le vecteur colonne $\hat{\mathbf{u}}$ qui contient dans la ligne $i$ l'estimateur $\hat{u}_i$.

Ce test donne un résultat individuel d'hétéroscédasticité pour un niveau de variable $\mathbf{X}$ et non pas tous les niveaux de variables. Donc, pour chaque erreur $\hat{u}_i$, on calcule la statistique $g_i = \frac{(\hat{u}_i)^2}{\hat{\sigma^2_u}}$.

Après, on monte une autre régression linéaire, appelée "régression auxiliaire", dont les variables explicatives sont typiquement les mêmes que dans la régression originale (mais pas forcément).

$$
g_i = \frac{(\hat{u}_i)^2}{\hat{\sigma^2_u}}=a_0+a_1Z_1+a_2Z_2+\cdots+a_pZ_{pi}+\eta_i
$$

Ainsi, on crée une statistique de test et une région critique :

$$
\text{Pour } i \text{ fixé, } H_0:\sigma^2_i=\sigma_u^2 \text{ vs. }H_1:\sigma^2_i=h(Z_i a)
\\[10pt]
\tau=\left\{T=Q_{BP}=\frac{SCE_{\text{aux.}}}{2}, \mathcal{C}=\left\{Q_{BP}:Q_{BP}>\chi^2(p)\right\} \right\}
$$

### Test de White

La différence de ce test avec Breuch-Pagan c'est que ce test considère toutes les variances des perturbations pour chaque input des observations (vecteur des $x_i$ observés). Ça commence de la même manière : estimation par les MCO, estimation de $(\hat{u}_i)^2$, puis on lance une régression linéaire comme suit :

$$
\hat{u}^2_i=a_0+\sum_{j=1}^k a_jx_{ij}+\sum_{j=1}^k \sum_{\ell \geq j}^k a_{j\ell} x_{ij} x_{i\ell}+\varepsilon_i 
$$

Finalement, le test est donc

$$
H_0:\forall i, \sigma^2_i=\sigma_u^2 \text{ vs. }H_1:\exists i, \sigma^2_i\neq \sigma_u^2
\\[10pt]
\tau=\left\{T=Q_{W}=NR^2\approx \chi^2\left(\frac{(k+1)(k+2)}{2}-1 \right), \mathcal{C}=\left\{Q_{W}:Q_{W}>\chi^2_\text{th}\right\} \right\}
$$

## Corriger l'hétéroscédasticité

### Écarts-types robustes

Il existe une manière de corriger les écarts-types des estimateurs du MCO. L'intérêt c'est que les intervalles de confiance et les résultats de tests de significativité sont calculés avec l'écart-type de $\boldsymbol{\beta}$, donc si l'écart-type est biaisé à cause du non respect de $H_2$, nos intervalles et résultats de tests ne sont pas fiables. **Il est absolument nécessaire que l'échantillon soit de grande taille**.

La "bonne" matrice de covariance des MCO de White est :

$$
\hat{V}(\hat{\boldsymbol{\beta}}_{MCO})=(\mathbf{X}^T\mathbf{X})^{-1} \hat{V} (\mathbf{X}^T\mathbf{X})^{-1}, \text{ où } \hat{V}=\sum_{i=1}^N\hat{u}_i^2(\mathbf{X}_i^T\mathbf{X}_i)
$$

![IC calculé avec les écart-types originaux.](ressources/03_non_respect_des_hypotheses_untitled_4.png)

IC calculé avec les écart-types originaux.

![IC calculé avec les écart-types robustes.](ressources/03_non_respect_des_hypotheses_untitled_5.png)

IC calculé avec les écart-types robustes.

### Les moindres carrés (quasi-) généralisés

On voudrait transformer notre modèle original de $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \mathbf{u}$. On commence par une matrice $\Omega$ qui résulte d'une opération d'autre matrice $\Phi$ : $\Omega = \Phi^T\Phi$. Il faut signaler que $\Omega$ est une matrice non-singulière avec inverse connue.

Une fois déterminée $\Omega$, on transforme le modèle comme suit :

$$
\Phi \mathbf{y}= \Phi \mathbf{X} \boldsymbol{\beta} + \Phi \boldsymbol{\varepsilon} \iff \mathbf{y}^*= \mathbf{X}^* \boldsymbol{\beta} + \boldsymbol{\varepsilon}^*
$$

On peut montrer que $\Phi \boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}^*$ respecte les hypothèses de Gauss-Markov. L'application des MCO à ce modèle transformé donne l'estimateur des Moindres Carrés Généralisés (MCG), qui est aussi équivalent à l'estimateur des MCO sur le modèle suivant :

$$
\Omega^{-1/2}\mathbf{y}= \Omega^{-1/2}\mathbf{X} \boldsymbol{\beta}+ \Omega^{-1/2} \mathbf{u}
$$

Les estimateurs du MCG sont sans biais et plus efficients que ceux du MCO. Ceci pourrait suffire si on connaît la covariance des erreurs $\Omega$, mais notons que $\Omega$ est inconnue. Tout l'enjeu consiste alors à estimer correctement la matrice $\Omega$. On parle maintenant des Moindres Carrés Quasi-Généralisés : (on utilise le $\rho$ réel pour estimer $\Omega$, on utilise $\hat{\rho}$). On ne peut jamais savoir le $\Omega$ réel, donc puisqu'on utilise $\hat{\Omega}$, on parle plutôt de "Quasi-Généralisés".

$$
\hat{\Omega}^{-1/2}\mathbf{y}= \hat{\Omega}^{-1/2}\mathbf{X} \boldsymbol{\beta}+ \hat{\Omega}^{-1/2} \mathbf{u}
$$

On verra donc le passage des MCG à MCQG pour $\hat{\boldsymbol{\beta}}$ et $V[\hat{\boldsymbol{\beta}}]$ : 

$$
\text{MCG : \hspace{5pt}}
\begin{align*}
&\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \Omega^{-1}\mathbf{X})^{-1}\mathbf{X}^T\Omega^{-1}\mathbf{y}
\\
&V(\hat{\boldsymbol{\beta}})=\sigma^2_u(\mathbf{X}^T\Omega^{-1}\mathbf{X})^{-1}
\end{align*}

\longrightarrow

\text{MCQG : \hspace{5pt}}
\begin{align*}
&\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \hat{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^T\hat{\Omega}^{-1}\mathbf{y}
\\
&V(\hat{\boldsymbol{\beta}})=\sigma^2_u(\mathbf{X}^T\hat{\Omega}^{-1}\mathbf{X})^{-1}
\end{align*}
$$

Alors que les MCG sont plus efficaces que les MCO en cas d'hétéroscédasticité ou d'autocorrélation, ce n'est pas le cas des MCQG. L'estimateur réalisable est asymptotiquement plus efficace, à condition que la matrice de covariance des erreurs soit estimée de manière cohérente, mais pour un échantillon de taille petite à moyenne, il peut être en fait moins efficace que les MCO.

On voit donc pourquoi certains auteurs préfèrent utiliser les MCO et reformulent leurs inférences en considérant simplement un estimateur alternatif pour la variance de l'estimateur robuste à l'hétéroscédasticité ou à l'autocorrélation sérielle.

### Preuve du biais de MCO et de la correction de biais du MCG

### → $\hat{\sigma}^2_{u,MCO}$ est biaisé

On commence par prouver que l'estimateur des MCO est biaisé si $H_2$ non respectée :

$$
\mathbb{E}(\hat{\sigma}^2_{u,MCO})=\frac{\hat{\mathbf{u}}^T \hat{\mathbf{u}}}{T-(k+1)}
$$

Dans le chapitre deux, on a prouvé que $\hat{\mathbf{u}}^T \hat{\mathbf{u}}= \mathbf{u}^T \mathbf{M} \mathbf{u}$. Donc, finalement :

![untitled](ressources/03_non_respect_des_hypotheses_untitled_6.png)

La suite est donc :

![untitled](ressources/03_non_respect_des_hypotheses_untitled_7.png)

On conclut que $\hat{\sigma}^2_{u,MCO}$ est biaisé.

### → $\hat{\sigma}^2_{u,MCG}$ est sans biais

On sait que

$$
\hat{\sigma}^2_{u,MCG}=\frac{\hat{\mathbf{u}^*}^T \hat{\mathbf{u}^*}}{T-(k+1)}, \text{ où } \mathbf{u}^*=\Omega^{-1/2}\mathbf{u} \text{ et } \hat{\mathbf{u}^*}=\mathbf{M}^*\mathbf{u}^*
$$

Donc, 

![untitled](ressources/03_non_respect_des_hypotheses_untitled_8.png)

Puis, finalement,

![untitled](ressources/03_non_respect_des_hypotheses_untitled_9.png)

On conclut que $\hat{\sigma}^2_{u,MCG}$ est donc sans biais.

### Les moindres carrés pondérés

Si la forme de l'hétéroscédasticité est connue, l'estimateur des MCQG peut être appliqué. Ceci prend le nom de "Moindres Carrés Pondérés" ou MCP, car la connaissance de la variance non-constante est incorporée dans la régression. **L'objectif est de transformer le modèle de sorte que la variance devienne constante.**

### → Variance de $u$ de la forme $\sigma^2z^2_t$

On commence par supposer que la variance de la vraie erreur peut s'écrire en fonction d'une autre variable $z_t$. Attention, ici on est dans des données de panel (coupe transversale et évolution dans le temps simultanément).

$$
V(u_t)=\sigma^2z_t^2, \text{ où }\sigma^2 \text{ constante inconnue}
$$

Pour supprimer l'hétéroscédasticité, il suffit de normaliser les variables par $z_t$.

$$
\frac{y_t}{z_t}=\beta_1\frac{1}{z_t}+\beta_2\frac{x_{2t}}{z_t}+\beta_3\frac{x_{3t}}{z_t}+v_t, \text{où }v_t=\frac{u_t}{z_t} \text{ est un terme d'erreur}
$$

Notons donc la conséquence de cette transformation pour tout $z_t$ :

$$
V(v_t)=V \left( \frac{u_t}{z_t} \right)=\frac{V(u_t)}{z_t^2}=\frac{\sigma^2 z_t^2}{z_t^2}=\sigma^2
$$

La variance de ce nouveau modèle devient donc constante. 

### → Variance de $u$ de la forme $\sigma^2_i \exp(Z_i a)$

Un autre cas c'est que la variance prenne une forme de type dit "multiplicatif".

$$
V(u_t)=\sigma^2_u=\sigma_i^2 \exp(Z_i a) \iff \sigma^2_i=\sigma^2_u\exp(Z_i a)
$$

On estime par les MCO, puis on calcule $\log(\hat{u}^2_i)$ pour tout $i$, puis on monte un modèle pour le $\log$ calculé :

$$
\log(\hat{u}^2_i)=\log(\sigma^2_u)+Z_i a+\varepsilon_i
$$

On revient sur $\sigma^2_i=\sigma^2_u\exp(Z_i a)$. Notons que l'estimation de $\sigma^2_i$ serait donc :

$$
\hat{\sigma}^2_i=\exp(Z_i \hat{a}) \iff \hat{\sigma}_i=\sqrt{\exp(Z_i\hat{a})}
$$

# Autocorrélation $(H_2)$

## Définition et illustration

Quand $H_2$ n'est pas respectée, le deuxième cas c'est l'autocorrélation. Quand elle est présente, la matrice des variances des perturbations est de la forme suivante, où les $\omega$ ne sont pas forcément égaux à $0$, donc $H_2$ n'est pas respectée.

$$
\text{Autocorrelation : } V(\mathbf{u}) = \begin{bmatrix}
1 & \omega_{12} & \omega_{13} & \cdots & \omega_{1N} \\
\omega_{21} & 1 & \omega_{31} & \cdots & \omega_{2N} \\
\omega_{31} & \omega_{32} & 1 & \cdots & \omega_{3N} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\omega_{N1} & \omega_{N2} & \omega_{N3} & \cdots & 1
\end{bmatrix}
$$

Ceci implique qu’il y a une dépendance temporelle entre les observations. 

Il est intéressant d’aller voir le graphique de $\hat u_{t+1}$ vs. $\hat u_t$. 

Un premier cas c’est quand la relation entre les perturbations adjacentes est **linéairement positive**. Dans ce cas, le graphique $\hat u_t$ vs. $t$ présente des “blocs” : quand $\hat u_t$ est positif, $\hat u_{t+1}$ est fréquemment positif aussi. Idem dans le cas négatif. Ça crée, dans l’exemple, un bloc des perturbations positifs, puis des perturbations négatives, puis positives de nouveau.

![untitled](ressources/03_non_respect_des_hypotheses_untitled_10.png)

Un deuxième cas c’est l’autocorrélation négative entre les erreurs adjacents : ici, les erreurs sont alternants. Si un erreur est positif, l’erreur suivant est fréquemment négatif, et vice-versa.

![untitled](ressources/03_non_respect_des_hypotheses_untitled_11.png)

Quand $H_2$ est respectée, l’erreur a plutôt une forme comme suit.

![untitled](ressources/03_non_respect_des_hypotheses_untitled_12.png)

## Conséquence pour les MCO

Les estimateurs des MCO restent sans biais et convergents. La seule chose qui change c’est qu’ils ne sont plus à variance minimale. Ils ne sont donc plus BLUE, ni des estimateurs de Gauss-Markov, ni efficients, etc.

Ceci donc signifie qu’on ne peut pas lancer des tests de significativité de l’effet une variable explicative sur une variable expliquée ! Il se peut que ce soit significatif, oui, **mais on ne peut pas lancer des tests car ce tests dépendent du respect des hypothèses, car les statistiques de Student ne suivront pas une loi de Student et pareil pour Fisher**. Toute inférence statistique faite avec ces estimateurs est donc invalide. **Il faudra “corriger” les estimateurs, mais on verra cela après**.

## Tests pour identifier

### Test de Durbin-Watson

Pour ce test, on devra :

1. Calculer les MCO d'un modèle
2. Calculer $\hat{\mathbf{u}}$
3. Monter une régression auxiliaire comme suit, où $v_t \sim \mathcal{N}(0, \sigma^2_v)$.
On estimera $\rho$ par $\hat{\rho}$ par les MCO.
Notons que la constante de ce modèle linéaire est égale à $0$.

$$
u_t=\rho u_{t-1}+v_t
$$

Ici, on peut finalement lancer le test. Les hypothèses seront $H_0 : \rho = 0$ et $H_1 : \rho \neq 0$. On commence par établir notre statistique DW. Dans ce cas, c'est comme suit.

$$
DW=\frac{\sum_{t=2}^T(\hat{u}_t-\hat{u}_{t-1})^2}{\sum_{t=1}^T \hat{u}_t^2} \approx 2(1-\hat{\rho})
$$

Le rapport de carrés est la définition formelle, mais on utilise plutôt l'approximation à droite.

Maintenant, pour la région de rejet et de non-rejet, elle prend la forme suivante. $d_\ell$ et $d_u$ sont des bornes inférieures et supérieures, respectivement, à lire d'une table de DW.

Si le $DW$ tombe sur une zone de rejet de $H_0$ ou inconclusive, on passe au MCQG. On s'arrête juste si on ne rejette pas $H_0$.

![untitled](ressources/03_non_respect_des_hypotheses_untitled_13.png)

![untitled](ressources/03_non_respect_des_hypotheses_untitled_14.png)

Le résultat de ce test est valide sous trois conditions : la matrice des $X$ n'est pas aléatoire $(H_3)$, il n'y a pas de termes de retard dans la régression originale, et la constante originale est différente de $0$.

### Test de Breuch-Godfrey

C'est un test plus général qui introduit des corrélations d'ordre $r$. À nouveau, il faut :

1. Estimation originale par les MCO
2. Calculer $\hat{\mathbf{u}}$
3. Monter la régression auxiliaire comme suit, où $v_t \sim \mathcal{N}(0, \sigma^2_v)$.
    
    $$
    u_t=\rho_1 u_{t-1}+\rho_2 u_{t-2}+\cdots+\rho_r u_{t-r}+v_t
    $$
    
4. Lancer le test, où $H_0$ : $\forall i\geq 1, \rho_i=0$, vs. $H_1 : \exists i \geq 1, \rho_i \neq 0$.
La statistique du test est donc $(T-r)R^2$.
La région critique est $(T-r)R^2 > \chi^2_r$. 

## Correction de l'autocorrélation

[T.2.4 - Examples of Applying Cochrane-Orcutt Procedure](https://online.stat.psu.edu/stat501/book/export/html/1003)

### MCQG : méthode de Prais-Winsten

Ceci exige la même préparation que les deux tests d'autocorrélation.

1. Estimation originale par les MCO
2. Calculer $\hat{\mathbf{u}}$
3. Monter une régression auxiliaire comme suit, où $v_t \sim \mathcal{N}(0, \sigma^2_v)$.
On estimera $\rho$ par $\hat{\rho}$ par les MCO.
Notons que la constante de ce modèle linéaire est égale à $0$.

$$
u_t=\rho u_{t-1}+v_t
$$

Une fois qu'on a calculé $\hat{\rho}$, on monte une autre régression auxiliaire. On fera la substitution $y^*_t = y_t - \hat{\rho} y_{t-1}$ et $X^*_t = X_t - \hat{\rho} X_{t-1}$. On finit par avoir ce qui suit :

$$
y^*_t = \alpha(1-\hat{\rho})+X^*_t\boldsymbol{\beta}+u_t
\\
y_t-\hat{\rho} y_{t-1}=\alpha(1-\hat{\rho})+(X_t-\hat{\rho} X_{t-1})\boldsymbol{\beta}+u_t
$$

Finalement, la "correction" des $\boldsymbol{\beta}$ se fait par réestimer ce nouveau modèle par les MCO. Les $\hat{\boldsymbol{\beta}}$ qui en résultent sont les MCO "corrigés par l'autocorrélation".

Dans le calcul de $V(\beta)$, on a que :

$$
\Omega = \begin{bmatrix}
\frac{1}{1-\rho^2} & \frac{\rho}{1-\rho^2} & \frac{\rho^2}{1-\rho^2} & \cdots & \frac{\rho^{T-1}}{1-\rho^2} \\
\frac{\rho}{1-\rho^2} & \frac{1}{1-\rho^2} & \frac{\rho}{1-\rho^2} & \cdots & \frac{\rho^{T-2}}{1-\rho^2} \\
\frac{\rho^2}{1-\rho^2} & \frac{\rho}{1-\rho^2} & \frac{1}{1-\rho^2} & \cdots & \frac{\rho^{T-3}}{1-\rho^2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{\rho^{T-1}}{1-\rho^2} & \frac{\rho^{T-2}}{1-\rho^2} & \frac{\rho^{T-3}}{1-\rho^2} & \cdots & \frac{1}{1-\rho^2}
\end{bmatrix}

$$

### MCQG : méthode de Cochrane-Orcutt

Cette méthode est identique à celle de Prais-Winsten, mais on laisse tomber l'observation en temps initial et on refait la procédure. $\Omega$ reste la même.

Une note intéressante c'est que la transformation de $y^*$ et $X^*$ est appelée "l'estimation de Cochrane-Orcutt". Cette méthode précède la méthode de Prais-Winsten.

### MCQG : méthode de Hildreth et Lu

Cette méthode est fondée sur le balayage et sur la répétition de l'estimation de Cochrane-Orcutt. Basiquement, on choisit plusieurs valeurs de $\rho \in [-1, 1]$ et on répète la méthode de Cochrane-Orcutt. On garde la valeur de $\hat{\rho}$ qui minimise la $SCR$ de l'estimation de Cochrane-Orcutt.

### Estimateur de maximum de vraisemblance

La log-vraisemblance s'écrit, sous $H_2^*$ :

$$
\begin{aligned}
\log L\left(\boldsymbol{\theta}^*\right) & =\log L\left(y_1, \ldots, y_T ; \mathbf{b}, \sigma_u^2, \Omega\right) \\
& =-\frac{T}{2} \log 2 \pi-\frac{T}{2} \log \sigma_u^2+\frac{1}{2} \log \left(1-\rho^2\right)-\frac{1}{2 \sigma_u^2}\left(\mathbf{y}^*-\mathbf{X}^* \mathbf{b}\right)^T\left(\mathbf{y}^*-\mathbf{X}^* \mathbf{b}\right)
\end{aligned}
$$

On cherche les valeurs de $\mathbf{b}$ qui maximisent la log-vraisemblance.

# Endogénéité $(H_3)$

[Causal Inference with Linear Regression: Endogeneity](https://towardsdatascience.com/causal-inference-with-linear-regression-endogeneity-9d9492663bac)

## Définition et sources

La définition est simplement quand une variable explicative est corrélée avec le terme d'erreur. Une telle variable est dite une variable endogène. Son estimateur par les MCO correspondant n'est plus BLUE, car il faut vérifier $H_3$ : "toutes les variables indépendantes sont non corrélées avec les termes d'erreurs".

Le problème de l'endogénéité est courant en sciences sociales et économie. Le problème se pose lorsque des variables individuelles importantes ne peuvent pas être observées. Celles-ci sont souvent corrélées avec les informations explicatives observées.

Les sources d'endogénéité sont souvent des variables omises, la simultanéité et les erreurs de mesure. Ce cours va plutôt se concentrer sur les erreurs de mesure.

## L'erreur de mesure

Dans un modèle de régression linéaire, on suppose que les observations sont mesurées correctement et sans erreur. Dans de nombreuses situations, cette hypothèse n'est pas respectée. Certaines variables (par exemple, la capacité et la volonté des gens de faire de l'exercice) peuvent ne pas être mesurables, et nous utilisons alors des variables de substitution (par exemple, les scores de QI des gens et le nombre d'heures passées dans la salle de sport) pour mesurer l'effet. Il est parfois difficile de faire des observations correctes.

Quelques définitions avant. On suppose un modèle linéaire simple temporel : $y_t = \beta_0 + \beta_1 x_t + u_t$.

- Une variable explicative est strictement exogène si : $\mathbb{E}(x_{jt} u_{t'})=0, \forall t,t'$
- Une variable explicative est exogène si : $\mathbb{E}(x_{jt} u_t)=0, \forall t$
- Une variable explicative est prédéterminée si : $\mathbb{E}(x_{jt} u_{t'})=0, \forall t' \geq t$

Si la valeur observée $x_t$ est mesurée avec erreur, on peut l'écrire comme : $x_t = \tilde{x_t} + v_t$, la vraie valeur plus une erreur de mesure.

Le vrai modèle serait donc : $y_t = \beta_1 \tilde{x_t}+\beta_0+u_t$. Mais on peut voir ce qui impliquerait pour $x_t$ :

$$
\begin{aligned}
y_t & =\beta_1 \tilde{x}_t+\beta_0+u_t \\
& =\beta_1\left(x_t-v_t\right)+\beta_0+u_t \\
& =\beta_1 x_t+\beta_0+w_t, \text{ avec } w_t=u_t-\beta_1 v_t
\end{aligned}
\\
\mathbb{E}\left[x_t w_t\right]=\mathbb{E}\left[\left(\tilde{x}_t+v_t\right) w_t\right]=\mathbb{E}\left[\left(\tilde{x}_t+v_t\right)\left(u_t-\beta_1 v_t\right)\right]=-\beta_1 \sigma_v^2 \neq 0
$$

L'estimateur des MCO de $\beta_1$ est donc biaisé et non convergent. On voit que $x_t$ est corrélée avec $w_t$ à travers $\beta_1$.

## Méthode des variables instrumentales

#TODO(À faire !)

## Tests

### Test de Hausman : vérifier l'exogénéité

Ce test s'applique à un estimateur dans deux cas :

- Quand il est convergent et asymptotiquement efficace sous $H_0$ (il n'y a pas de corrélation), mais non convergent sous $H_1$ (il y a de la corrélation)
- Quand il est convergent mais non efficace sous $H_0$ et $H_1$

Les hypothèses sont mathématiquement définies comme suit :

$$
H_0:\text{plim}_{T\to\infty} \frac{\mathbf{X}^T \mathbf{u}}{T}=0 \text{ vs. } H_1: \text{plim}_{T\to\infty} \frac{\mathbf{X}^T \mathbf{u}}{T}\neq0
$$

La statistique du test serait :

$$
Q_H=\left(\widehat{\boldsymbol{\beta}_{IV}}-\widehat{\boldsymbol{\beta}_{MCO}}\right)^T\left[\widehat{V}\left(\hat{\boldsymbol{\beta}}_{IV}\right)-\widehat{V}\left(\hat{\boldsymbol{\beta}}_{MCO}\right)\right]^{-1}\left(\widehat{\boldsymbol{\beta}_{IV}}-\widehat{\boldsymbol{\beta}_{MCO}}\right) \sim \chi^2(k+1)
$$

Et la région de rejet est donnée par $Q_H > Q_\text{th}$.

### Test de Sargan : valider le choix des instruments

$H_0$ devient "les VI sont de bons instruments" contre $H_1$ "les VI ne sont pas de bons instruments". Mathématiquement,

$$
H_0:\text{plim}_{T\to\infty} \frac{\mathbf{Z}^T \mathbf{u}}{T}=0 \text{ vs. } H_1: \text{plim}_{T\to\infty} \frac{\mathbf{Z}^T \mathbf{u}}{T}\neq0
$$

La statistique du test est donc

$$
Q_S=\frac{\bar{\mathbf{u}}^T {\mathbf{Z}}(\mathbf{Z}^T\mathbf{Z})^{-1}\mathbf{Z}^T\bar{\mathbf{u}}}{\hat{\sigma}^2_{\mathbf{u}, VI}}=TR^2\sim\chi^2(p-(k+1))
$$

Et, à nouveau, la région de rejet est donnée par $Q_S > Q_\text{th}$.