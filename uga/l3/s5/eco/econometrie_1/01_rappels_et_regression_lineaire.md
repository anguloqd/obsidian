## 01 // rappels et régression linéaire

[Économétrie - Chap #1](ressources/01_rappels_et_regression_lineaire_1_chapitre1_econometrie1_20232024.pdf)

## Les modèles linéaires déterministes

### Exemple d’une fonction de production

Prenons une fonction Cobb-Douglas, où $Q$ le niveau de production (endogène), A la technologie et K le capital (exogènes).

$$Q=AL^\alpha K^\beta$$

En fait, on pourrait linéariser cette fonction en appliquant un logarithme des deux côtés :

$$\log Q=\log A + \alpha \log L + \beta \log K$$

En généralisant à $N$ firmes $i$, chaque firme a la fonction de production qui suit :

$$\log Q_i = b_0 + b_1\log L_i + b_2 \log K_i$$

Avec cette forme fonctionnelle, on pourra parler de l’élasticité du facteur travail. Le “facteur travail” est $\log L$.

$$b_1=\frac{\partial\log Q}{\partial\log L}=\frac{\partial Q}{\partial L} \times \frac{L}{Q}$$

Et on sais aussi que la productivité marginal est $Pm_L=\frac{\partial Q}{\partial L}$. Donc, notons qu’on peut passer de $b_1$ à $Pm_L$ et vice-versa.

$$b_1=\frac{\partial\log Q}{\partial\log L}=\frac{\partial Q}{\partial L} \times \frac{L}{Q} \iff Pm_L=\frac{\partial Q}{\partial L}=\frac{Q}{L}\times b_1$$

Les deux élasticité et productivité marginale peuvent être estimés avec des données. Notons que c’est analogique pour le “facteur capital” $\log K$ et son élasticité.

$$b_2=\frac{\partial\log Q}{\partial\log L}=\frac{\partial Q}{\partial K} \times \frac{K}{Q} \iff Pm_L=\frac{\partial Q}{\partial K}=\frac{Q}{K}\times b_2$$

On peut voir que $b_0$ est donc “le log du niveau de production commun à toutes les observations, mais qui n’est expliqué ni par le travail, ni par le capital". Comment revenir au niveau de production ?

### Familles de formes fonctionnelles

Notons que les facteurs peuvent être en forme normale, appelé juste forme “niveau”, ou bien en forme log. Ici, $y$ est la production $Q$ et $x_i$ sont les facteurs comme $L$ ou $K$. Voyons :

- Modèle niveau-niveau : $y=b_0+b_1x_1+b_2x_2$
    - $b_i = \partial y / \partial x_i$. $b_i$ est donc un effet marginal.
    - Une augmentation de $1$ (unité) de $x_i$ cause une augmentation de $b_1$ unités de $y$.
    - **Il est possible de passe de l’élasticité à l’effet marginal et inversement**.
- Modèle log-log : $\log y = b_0+b_1\log x_1 + b_2\log x_2$
    - $b_i = \partial y / \partial x_i \times x_i/y$ est une élasticité.
    - Une augmentation de $1\%$ de $x_i$ cause une augmentation de $b_i\%$ de $y$.
- Modèle log-niveau : $\log y =b_0+b_1x_1+b_2x_2$
    - $b_i = \partial \log y / \partial x_i = \partial y/y \times \ 1/\partial x_i$. $b_i$ est une semi-élasticité.
    - Une augmentation de $x_i$ d’une unité augmente $y$ de $(b_i \times 100)\%$.
- Modèle niveau-log : $y = b_0+b_1\log x_1 + b_2x_2$
    - Pas tous les facteurs doivent être en $\log$. **Un seul suffit pour dire que il y a une spécification (forme du modèle) niveau-log**. On parlera de $x_1$ ici.
    - $b_1 = \partial y/\partial \log x_1=\partial y \times x_1/\partial x_1$. **Ceci n’est pas une semi-élasticité ! On dit “l’élasticité sans nom”.**
    - Une augmentation de $1\%$ de $x_1$ cause un augmentation de $b_1/100$ unités.

> [!note]
> Prenons $y_i = b_0 + b_1 x_{1i} + b_2 x_{1i}^2 + b_3 x_{2i} + u_i$.
> La dérivé partielle sur niveau-niveau est l’effet marginale : $\partial y_i /\partial x_1=b_1+2b_2x_1$
> La dérivé partielle sur log-log est l’élasticité.
> La dérivé partielle sur log-niveau est la semi-élasticité.
> Il se peut qu’on parle juste de “effet $x_1$” qui est juste le coefficient de $x_1$ : $\partial y_i / \partial “x_1” = b_1$. Ce n’est pas l’effet marginale totale de $x_1$. Parfois on veut juste se concentrer sur le coefficient direct isolé.

La question sur comment choisir la forme fonctionnelle adaptée dépend de la nature de chaque variable, ses graphiques et les statistique de relation entre les variables (covariance, corrélation).

## Modèles linéaires aléatoires

### Équations

Le modèle générale de régression linéaire est le suivant, avec $k$ l’indices des facteurs, $i$ l’indice de la firme ou individu en question et $u$ est le “terme de perturbation”, càd. l’erreur ou facteurs inobservés.

$$y_i=\beta_0+\beta_1x_{1i}+\beta_2x_{2i}+\cdots+\beta_kx_{ki}+u_i$$

Dans ce chapitre, on se limite à juste une variable explicative. Donc :

$$y_i=\beta_0+\beta_1x_{1i}+u_i$$

### L’erreur $u_i$ et l’espérance de $y$

Cette perturbation traduit principalement:

- Les facteurs inobservables, qui illustrent les comportements des individus;
- La forme fonctionnelle n’est pas forcément linéaire dans les paramètres;
- Le fait que cette fonction peut varier en fonction du temps ou des individus observés;
- L’omission de variables dans le modèle économique; des erreurs de mesure sur les variables, etc.

Supposons que **les autres facteurs compris dans $u$ sont maintenus constants**, alors s’il n’y a pas eu une changement/variation dans $u$, une variation de $y$ est due forcement à une variation de $x_1$, particulièrement comme suit :

$$\Delta u=0\implies \Delta y=\beta_1\Delta x$$

$\beta_1$ mesure l’effet de $x$ sur $y$ en supposant que tous les autres facteurs sont fixes, y compris $u$.  Il va falloir poser des hypothèses sur $x$, $u$ et leur lien.

En plus, on fait deux hypothèses sur u :

- $\mathbb E[u]=0$
**Ex.** : les facteurs autres que le niveau d’étude, ont un effet moyen nul dans la population.
- $\mathbb E[u|x]=\mathbb E[u]$. Meilleure écriture : $\mathbb E[u|x=c, c\in\Omega_x]=\mathbb E[u]$.
**À interpréter** : la valeur espérée de $u$ peut être décrite par la valeur de $x$ pour une partie de la population.
**Ex. :** Soit $u$ l’aptitude innée d’une personne. Le niveau moyen de l’aptitude est identique pour tout valeur possible de $x$.

Ces deux hypothèses permet de conclure $\mathbb E[u|x]=\mathbb E[u] = 0$. Ceci permet d’écrire la fonction de régression de la population $\mathbb E[y|x]$ (pourquoi pas “l’espérance”?) comme suit :

$$E(y|x)=E(\beta_0+\beta_1x+u)=\beta_0+\beta_1x$$

C’est donc la valeur moyenne de $y$ pour les différents niveaux de $x$. Notons que c’est l’espérance de y et non pas la valeur exacte de $y$ ! La valeur espérée annule l’erreur, mais en réalité la variable $y$ sera affecte par l’erreur $u$ !

![[ressources/01_rappels_et_regression_lineaire_untitled.png]]

Dispersion de la production ($Q$) et du travail ($L$), et fonction de régression de la population $\mathbb E[Q|L] = β_0 + β_1L$

On se souciera d’estimer $\beta_0$ et $\beta_1$ après avec un échantillon issu de la population.

### Dérivation de l’estimateur des MCO

Des hypothèses précédentes, on peut déduire ce qui suit :

$$\text{Cov}(x, u)=E(u|x)=0$$

Ce qui implique donc :

$$E(\underbrace{y-\beta_1x-\beta_0}_u)=0 \text{ et } \text{Cov}(x,u)=E(x,(y-\beta_1x-\beta_0)]=0$$

On voudra estimer $\beta_0$ et $\beta_1$ sous contrainte de minimiser la somme des erreurs au carré.  Les estimateurs seront notés $\hat \beta_0$ et $\hat \beta_1$. MCO signifie Moindres Carrés Ordinaires. L’objectif devient dériver les valeurs de $\beta_0$ et $\beta_1$, donc on fait ce qui suit. On commence avec deux faits :

$$\tag{1}\frac{1}n{}\sum_{i=1}^n(y_i-\hat\beta_0-\hat\beta_1x_i)=0$$

$$\tag{2}\frac{1}n{}\sum_{i=1}^nx_i(y_i-\hat\beta_0-\hat\beta_1x_i)=0$$

Notons que l’équation $(1)$ équivaut ce qui suit :

$$\frac{1}n{}\sum_{i=1}^n(y_i-\hat\beta_0-\hat\beta_1x_i)=0 \iff \bar y=\hat\beta_0+\hat\beta_1\bar x$$

Après, en isolant $\beta_0$ et en le remplaçant, notons que l’équation $(2)$ devient ce qui suit :

$$\begin{align*}
&\frac{1}n{}\sum_{i=1}^nx_i(y_i-\hat\beta_0-\hat\beta_1x_i)=0
\\
\iff &\frac{1}n{}\sum_{i=1}^nx_i(y_i-\bar y + \hat\beta_1\bar x-\hat\beta_1x_i)=0
\\
\iff
&\frac{1}{n}\sum_{i=1}^nx_i(y_i-\bar y)=\frac{1}{n}\sum_{i=1}^nx_i(-\hat\beta_1\bar x+\hat\beta_1 x_i)
\\
\iff
&\frac{1}{n}\sum_{i=1}^nx_i(y_i-\bar y) = \beta_1 \sum_{i=1}^nx_i(x_i-\bar x)
\end{align*}$$

Cette équation a une solution pour $\beta_1$ ssi. $\sum_{i=1}^nx_i(x_i-\bar x) \ne 0$. Alors :

$$\begin{align*}
&\hat \beta_1=\frac
{\sum_{i=1}^nx_i(y_i-\bar y)}
{\sum_{i=1}^nx_i(x_i-\bar x)}
=
\frac
{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}
{\sum_{i=1}^n(x_i-\bar x)^2}=\frac{\text{Cov}(x,y)}{V(x)}

\\[12pt]

&\hat\beta_0=\bar y - \hat\beta_1 \bar x
\end{align*}$$

On dit que $\hat\beta_0$ et $\hat\beta_1$ minimisent la somme des carrés des résidus (SCR), qui est la somme de la valeur ajustée par la droite de régression $(\hat y)$ et la valeur réelle observée $(y_i)$.

Notons que $\hat\beta_0$ et $\hat\beta_1$ changent en fonction de l’échantillon donné !

## Propriétés des MCO

### L’erreur $u_i$ et le résidu $\hat u_i$

Étant donné qu’on ne connaît pas toute la population pour en calculer la meilleure droite, on se contentera d’estimer $\beta_0$ et $\beta_1$ avec $\hat\beta_0$ et $\hat\beta_1$. Aussi, on va se contenter d’estimer $u_i$, le résidu de l’observation $i$ par rapport à la vraie droite $(\beta_0, \beta_1)$. Son estimateur sera $\hat u_i$. Quelques faits :

- La somme de résidus $\sum_{i=1}^N(y_i-\hat y_i)^2=\sum_{i=1}^N(\hat u_i - \cancel{\bar{\hat u}}^{\space0})^2$ est nulle $\iff$ la moyenne de résidus est nulle.
Ceci est naturel. La proposition à gauche vient de $\mathbb E[u]=0$ qu’on met en hypothèse.
- La covariance des variables explicatives et les résidus des MCO est nulle.
- Le point moyen $(\bar x, \bar y)$ est toujours sur la droite de régression.
Ceci est visible dans la définition de $\beta_0 = \bar y - \beta_1 \bar x$ et isolant $\bar y$.

### Analyse de la variance et $R^2$

La populaire équation de la variance, qui décompose la variance comme la somme de deux termes, est la suivante :

$$\underbrace{\sum_{i=1}^N(y_i-\bar y)^2}_{SCT}=\underbrace{{\sum_{i=1}^N(\hat y_i-\bar y)^2}}_{SCE}+\underbrace{\sum_{i=1}^N(y_i-\hat y_i)^2}_{SCR}

\\[8pt]

\text{Remarque : } \sum_{i=1}^N(y_i-\hat y_i)^2=\sum_{i=1}^N(\hat u_i - \cancel{\bar{\hat u}}^{\space0})^2$$

Où $SCT$ est la somme des carrés totaux, $SCE$ est la somme des carrées expliques, et $SCR$ est la somme des carrés des résidus.

Avec cette terminologie, on rappelle le coefficient de détermination :

$$R^2=\frac{SCE}{SCT}=1-\frac{SCR}{SCT}$$

- $R^2 = 1$ : si tous les points correspondant aux données se trouvent sur la droite d’ajustement.
- $R^2 = 0$ : les variations entre les $\bar y_i$ ne capturent quasiment rien de la variation observée entre les $y_i$.
- Remarque : un faible $R^2$ n’implique pas forcément que la régression des MCO ne sert à rien, mais que d’autres “problèmes” peuvent expliquer ce résultat.

## Espérance et variance

### Les cinq hypothèses fondamentales

Par la suite, on va supposer les cinq hypothèses ”fondamentales” qui suivent :

- $H_1$ : $\mathbb E [u_i] = 0$
- $H_2$, la homoscédasticité ou variance constante : $\text{Var}(u_i)=\mathbb E[u_i^2]=\sigma^2_u$
- $H_3$,: la variable explicative $x_i$ est non aléatoire
- $H_4$, spécificité : le modèle est correctement spécifié.
Dans ce cas c’est linéaire, donc $y_i = \beta_0+\beta_1x_i+u_i$.
- $H_5$, non colinéarité: la variable explicative $x_i$ n’est pas constante pour toutes les observations.

> [!note]
> Les estimateurs $\hat \beta_0$ et $\hat \beta_1$ peuvent être biaisés. La source normalement vient du non respect du modèle spécifie (utiliser $\ln x$ quand ça devrait être $x$, ou vice-versa) ou de H3 : $\mathbb E [\mathbf{x} u] \ne 0$ donc $\text{Cov}(\mathbf{x}, u) \ne 0$.

Sous ces hypothèses, il découle que :

- Les estimateurs $\hat β_0$ et $\hat β_1$ des MCO sont **sans biais et a variance minimale**, aussi appelés les estimateurs de Gauss-Markov**.** Donc :

$$E(\hat\beta_0)=\beta_0 \text{\hspace{8pt}et\hspace{8pt}}E(\hat\beta_1)=\beta_1$$

    
- Les variances sont les suivantes, mais il nous manque un paramètre $\sigma^2_u$.
    

$$V(\beta_1)=\frac{\sigma^2_u}{\sum_{i=1}^N(x_i-\bar x)^2}

\text{\hspace{8pt}et\hspace{8pt}}

V(\beta_0)=\frac{\sigma^2_u}{n}\frac{\sum_{i=1}^Nx_i^2}{\sum_{i=1}^N(x_i-\bar x)^2}$$

- Si on prend la variances des résidus, ce serait un estimateur biaisé de $\sigma^2_u$.
Néanmoins, Il existe un estimateur sans biais de $\sigma^2_u$, où $k$ le nombre de var. explicatives. Dans ce cas, $k=1$.

$$\hat\sigma^2_u=\frac{\sum_{i=1}^n\hat u_i^2}{N-(k+1)} \implies E(\hat\sigma^2_u)=\sigma^2_u$$

## Inférence

### Hypothèse de normalité des erreurs

On se permet d’ajouter une hypothèse aux cinq hypothèses précédentes :

- Hypothèse complémentaire : $u_i \sim \mathcal N(0, \sigma^2_u)$ et $\text{Var}(u_i|x_i)=\text{Var}(u_i)=\sigma^2_u$.
$u_i$ est normale et ne dépend pas des variables explicatives.

Tel hypothèse implique que $y|x \sim \mathcal N(\beta_0+\beta_1x_1, \sigma^2_u)$.

![[ressources/01_rappels_et_regression_lineaire_untitled_1.png]]

Avec de grands échantillons, l’hypothèse de normalité n’est plus nécessaire.

### Test bilatéral de $\beta_k$ $(t$-test$)$

En bref, on utilise un test de Student pour estimer chaque $\beta_i$ de notre modèle. Je prends ce qu’on a fait en Statistique Mathématique 2.

Quelques différences :

- Le test était présenté originalement avec $\mu$ comme paramètre et $\bar X$ comme statistique. Là, on change à $\beta_k$ comme paramètre et $\hat\beta_k$ comme statistique.
- Le test était présenté originalement avec $(n-1)$ le paramètre de la loi de Student, qui sont les degrés de liberté. Dans ce cas, les degrés de liberté sont $(n-(k+1))$, où $k$ est le nombre de variables explicatives (on compte de $\beta_1$ à $\beta_n$, on ignore la constante $\beta_0$).

---

Dans ce cas et vu précédemment, on utilise une variable de Student comme $T$. Ceci est juste valide si et seulement si on est sous $H_0$, car $\mu_0$ serait donc la moyenne de $\bar X$

Ceci n’est plus le cas quand on considère le cas général (càd. peu importe si $H_0$ ou si $H_1$), car on ne peut donc garantir que $\mu_0$ est la vraie moyenne de $H_0$ et tout la statistique $T$ ne suit plus une loi de Student.

#### Cas bilatéral

$$\tau=\left\{T=\frac{\hat\beta_k-\cancel{E(\hat\beta_k)}}{\hat\sigma_{\hat\beta_k}}^{\space = \beta_k=0}\hspace{-20pt}, A =\{T: -t^{(n-(k+1))}_{1-\alpha/2}<T< t^{(n-(k+1))}_{1-\alpha/2} \} \right\}

\\[8pt]

H_0:\beta_k=0\text{ vs. }H_1:\beta_k\ne0$$

De même, on pourrait isoler $\hat\beta_k$ dans l’inégalité pour obtenir ce qui suit :

$$\tau=\left\{ T=\hat\beta_k, A=\{ T : 0-\hat\sigma_{\beta_k} t^{(n-(k+1))}_{1-\alpha/2} < T < 0+\hat\sigma_{\beta_k}t^{(n-(k+1))}_{1-\alpha/2} \} \right\}$$

$$\text{Rejeter si : }|T| \le t^{(n-(k+1))}_{1-\alpha/2 }, \text{ accepter sinon.}$$

#### Cas unilatéral

Dans le cas des tests unilatéraux, on définit $A$ comme suit :

$$H_0 : \beta_k \le 0 \longrightarrow A=\{ T : T <t^{(n-(k+1))}_{1-\alpha }\} \iff \bar A =\{ T : t^{(n-(k+1))}_{1-\alpha } \le T\}

\\

H_0 : \beta_k \ge 0 \longrightarrow A=\{ T : t^{(n-(k+1))}_{1-\alpha }<T\} \iff \bar A =\{ T :T \le t^{(n-(k+1))}_{1-\alpha }\}$$

La prof. veut qu’on explicite la règle de decision, qui est dans la définition de $\bar A$.

$$\text{Rejeter si : }|T| \le t^{(n-(k+1))}_{1-\alpha }, \text{ accepter sinon.}$$

### Significativité globale du modèle $(F$-test$)$

Ce test s’appuie sur la statistique de Fisher :

$$F=\frac{SCE/k}{SCR/\big(n-(k+1)\big)}=\frac{R^2/k}{(1-R^2)/\big(n-(k+1)\big)}\sim \mathcal F(v_1,v_2)$$

Les valeurs de la loi de Fisher ont déjà été calculés dans une table. Le test prend donc la forme qui suit, et la nulle affirme que la relation entre $y$ et chacune des variables explicatives $x_i$ est nulle.

$$\tau=\left\{ F \text{ comme statistique}, A=\{F: F<f^{(v_1,v_2)}_{1-\alpha}\} \right\}

\\[6pt]

H_0 : \forall i \le k,  \beta_i=0 \text{ vs. } H_1 : \exist i\le k, \beta_i\ne 0$$

Normalement, le test de Student et le test de Fisher nous mène toujours à la même conclusion. Il semble que, dans ce cours, on fera de tests de Fisher seulement unilatéraux.

$$\text{Rejeter si : }F\ge f^{(v_1,v_2)}_{1-\alpha}, \text{ accepter sinon.}$$
