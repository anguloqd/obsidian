# 02 // les MCO en profondeur

[02_les_mco_en_profondeur_l2_regressionlineaire_mco_1.pdf](ressources/02_les_mco_en_profondeur_l2_regressionlineaire_mco_1.pdf)

## Introduction générale

Ce chapitre approfondit l'analyse de l'estimateur des Moindres Carrés Ordinaires (MCO) dans le contexte du modèle de régression linéaire. L'objectif principal est de fournir une compréhension complète des propriétés asymptotiques de cet estimateur, en mettant l'accent sur le point de vue économétrique qui considère les MCO comme un cas particulier de la Méthode des Moments.

L'analyse se concentre sur plusieurs aspects fondamentaux : les propriétés asymptotiques de l'estimateur des MCO, les conditions d'identification des paramètres d'un modèle de régression linéaire (notamment les conditions de rang sur le processus générateur de $\mathbf{x}_i$), et l'introduction de la notion de projection linéaire d'une variable aléatoire sur un vecteur de variables aléatoires.

## Le modèle de régression linéaire fondamental

### Définition et cadre général

Le modèle de régression linéaire se présente sous une forme générale où l'on considère :

$$y_i = \mathbf{x}_i' \boldsymbol{a}_0 + u_i \text{ avec } E[u_i] \equiv 0$$

Ce modèle devient un modèle de régression proprement dit lorsque la condition d'exogénéité de $\mathbf{x}_i$ est vérifiée. L'exogénéité constitue une propriété fondamentale qui distingue un simple modèle linéaire d'un véritable modèle de régression.

**Définition de l'exogénéité** : $\mathbf{x}_i$ est exogène par rapport à $u_i$ si $E[u_i|\mathbf{x}_i] = E[u_i] \equiv 0$.

Cette définition implique que l'espérance conditionnelle du terme d'erreur sachant les variables explicatives est égale à son espérance inconditionnelle, qui est nulle par hypothèse. Cette condition est préférée à la simple absence de corrélation car elle est nécessaire pour les modèles de forme non linéaire et facilite l'analyse de l'hétéroscédasticité potentielle des termes d'erreur.

### Hétéroscédasticité conditionnelle

La modélisation économétrique distingue deux cas importants concernant la variance des termes d'erreur :

**Modèle homoscédastique** : Les termes d'erreur ont une variance constante conditionnellement à $\mathbf{x}_i$, c'est-à-dire $E[u_i^2|\mathbf{x}_i] = V[u_i|\mathbf{x}_i] = V[u_i]$. On définit alors le paramètre $\sigma_0^2 \equiv V[u_i] = E[u_i^2|\mathbf{x}_i]$.

**Modèle hétéroscédastique** : La variance des termes d'erreur dépend de $\mathbf{x}_i$, soit $E[u_i^2|\mathbf{x}_i] = V[u_i|\mathbf{x}_i] \neq V[u_i]$. Dans ce cas, $V[u_i|\mathbf{x}_i]$ est potentiellement une fonction de $\mathbf{x}_i$, ce qui correspond à une hétéroscédasticité conditionnelle de forme inconnue.

### Flexibilité du cadre linéaire

Malgré sa forme apparemment simple, le modèle de régression linéaire peut représenter des relations relativement complexes grâce à la transformation des variables. Le critère déterminant est la linéarité dans les paramètres, non dans les variables originelles.

**Modèles avec effets carrés** : On peut inclure des termes quadratiques en transformant les variables originelles. Par exemple, avec $\tilde{x}_{1,i} \equiv x_i$ et $\tilde{x}_{2,i} \equiv x_i^2$, on obtient :
$$y_i = b_{0,0} + b_{1,0}\tilde{x}_{1,i} + b_{2,0}\tilde{x}_{2,i} + u_i = \alpha + b_{1,0}x_i + b_{2,0}x_i^2 + u_i$$

**Modèles quadratiques complets** : Les modèles peuvent inclure simultanément des effets carrés et croisés pour capturer des interactions complexes entre les variables explicatives.

**Modèles en logarithmes** : L'utilisation de transformations logarithmiques permet de modéliser des relations non linéaires tout en conservant la linéarité paramétrique, facilitant ainsi l'interprétation en termes d'élasticités.

## Trois méthodes de calcul de l'estimateur des MCO

### Vue d'ensemble méthodologique

L'estimateur des MCO peut être calculé selon trois approches distinctes, chacune apportant un éclairage particulier sur la nature de cet estimateur. L'estimateur des MCO de $\boldsymbol{a}_0$ dans le modèle de régression linéaire s'écrit :

$$\hat{\boldsymbol{a}}_N^{MCO} \equiv \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{x}_i y_i$$

Les trois approches diffèrent par leur fondement conceptuel : l'approche par les moindres carrés constitue une méthode d'ajustement pure, tandis que les approches directe et par la méthode des moments s'appuient explicitement sur les propriétés statistiques du processus générateur des $(\mathbf{x}_i, y_i)$.

### Approche par les moindres carrés

Cette première approche considère l'estimation comme un problème d'optimisation visant à minimiser la somme des carrés des résidus. L'estimateur des MCO est défini comme :

$$\hat{\boldsymbol{a}}_N^{MCO} \equiv \arg\min_{\boldsymbol{a}} \sum_{i=1}^N (y_i - \mathbf{x}_i'\boldsymbol{a})^2$$

L'objectif est de trouver la valeur de $\boldsymbol{a} \in \mathbb{R}^K$ qui minimise soit la somme des carrés des résidus, soit de manière équivalente l'erreur quadratique moyenne de prédiction des $y_i$ par les $\mathbf{x}_i'\boldsymbol{a}$.

**Interprétation** : Ce critère constitue un critère d'ajustement pur. On recherche la valeur de $\boldsymbol{a}$ telle que la prédiction de $y_i$ par $\hat{y}_{i,N} \equiv \mathbf{x}_i'\hat{\boldsymbol{a}}_N^{MCO}$ minimise la somme des carrés des écarts.

Les conditions du premier ordre du programme de minimisation conduisent à :

$$\frac{\partial}{\partial \boldsymbol{a}} \sum_{i=1}^N (y_i - \mathbf{x}_i'\boldsymbol{a})^2 = -2\sum_{i=1}^N \mathbf{x}_i(y_i - \mathbf{x}_i'\hat{\boldsymbol{a}}_N^{MCO}) = \mathbf{0}$$

Cette condition implique que les résidus de la régression sont orthogonaux aux variables explicatives par construction de $\hat{\boldsymbol{a}}_N^{MCO}$, soit $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i(y_i - \mathbf{x}_i'\hat{\boldsymbol{a}}_N^{MCO}) = \mathbf{0}$.

La résolution de ce système donne directement l'expression de l'estimateur des MCO. La somme des carrés des résidus est convexe en $\boldsymbol{a}$ et strictement convexe si et seulement si $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'$ est inversible.

### Approche directe

L'approche directe exploite directement l'exogénéité des $\mathbf{x}_i$ dans le modèle de régression. L'exogénéité implique que $E[u_i|\mathbf{x}_i] = \mathbf{0}$, ce qui donne $\text{Cov}(u_i, \mathbf{x}_i) = E[\mathbf{x}_i u_i] = \mathbf{0}$.

En partant du modèle $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$, on obtient :
$$E[y_i|\mathbf{x}_i] = E[\mathbf{x}_i'\boldsymbol{a}_0 + u_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{a}_0 + E[u_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{a}_0$$

En multipliant par $\mathbf{x}_i$ et en prenant l'espérance :
$$E[\mathbf{x}_i y_i] = E[\mathbf{x}_i \mathbf{x}_i'\boldsymbol{a}_0] = E[\mathbf{x}_i \mathbf{x}_i']\boldsymbol{a}_0$$

Si $E[\mathbf{x}_i \mathbf{x}_i']$ est inversible, on peut résoudre pour obtenir :
$$\boldsymbol{a}_0 = (E[\mathbf{x}_i \mathbf{x}_i'])^{-1} E[\mathbf{x}_i y_i]$$

L'estimateur convergent s'obtient en remplaçant les espérances théoriques par leurs contreparties empiriques selon la Loi des Grands Nombres. Cette démarche exploite la forme spécifique de $E[\mathbf{x}_i y_i]$ telle qu'elle découle du modèle de régression.

### Méthode des moments et principe d'analogie

La méthode des moments constitue l'approche la plus générale et sera utilisée tout au long de l'analyse économétrique ultérieure. Elle repose sur l'exploitation de la condition d'orthogonalité fondamentale découlant de l'exogénéité.

**Condition d'orthogonalité** : L'exogénéité des $\mathbf{x}_i$ dans le modèle linéaire $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ implique $E[u_i|\mathbf{x}_i] = \mathbf{0}$, ce qui donne la condition d'orthogonalité $E[\mathbf{x}_i u_i] = \mathbf{0}$.

En combinant cette condition avec $u_i = y_i - \mathbf{x}_i'\boldsymbol{a}_0$, on obtient :
$$E[\mathbf{x}_i(y_i - \mathbf{x}_i'\boldsymbol{a}_0)] = \mathbf{0}$$

Cette condition de moment peut être exploitée dans le cadre de la Méthode des Moments selon le principe d'analogie de Goldberger.

**Principe d'analogie** : Si $\boldsymbol{\beta}_0$ vérifie la condition de moment $E[\mathbf{h}(\mathbf{w}_i; \boldsymbol{\beta}_0)] = \mathbf{0}$, alors l'estimateur $\hat{\boldsymbol{\beta}}_N$ est défini comme la solution du problème empirique correspondant : $\frac{1}{N}\sum_{i=1}^N \mathbf{h}(\mathbf{w}_i; \hat{\boldsymbol{\beta}}_N) = \mathbf{0}$.

Dans le cas du modèle de régression, $\boldsymbol{a}_0$ est la solution de $E[\mathbf{x}_i(y_i - \mathbf{x}_i'\boldsymbol{a})] = \mathbf{0}$, et l'estimateur de la méthode des moments $\hat{\boldsymbol{a}}_N^{MM}$ est défini par :
$$\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i(y_i - \mathbf{x}_i'\hat{\boldsymbol{a}}_N^{MM}) = \mathbf{0}_{K \times 1}$$

**Équivalence des méthodes** : La résolution de cette équation montre que $\hat{\boldsymbol{a}}_N^{MM} = \hat{\boldsymbol{a}}_N^{MCO}$, établissant l'équivalence entre les trois approches.

L'approche par la méthode des moments illustre le rôle fondamental de l'exogénéité des $\mathbf{x}_i$, condition nécessaire pour démontrer les bonnes propriétés de $\hat{\boldsymbol{a}}_N^{MCO}$, notamment sa convergence dans un modèle linéaire.

## Propriétés asymptotiques de l'estimateur des MCO

### Convergence de l'estimateur

L'établissement de la convergence de l'estimateur des MCO constitue un résultat fondamental qui nécessite l'exploitation conjointe de l'exogénéité des variables explicatives et de la Loi des Grands Nombres.

**Propriété de convergence** : Soit $\{(y_i, \mathbf{x}_i); i = 1,2,...,N\}$ un échantillon de variables aléatoires réelles telles que $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ avec $E[u_i|\mathbf{x}_i] = E[u_i] \equiv 0$. L'estimateur des MCO de $\boldsymbol{a}_0$ existe avec une probabilité approchant 1 et est convergent : $\hat{\boldsymbol{a}}_N^{MCO} \xrightarrow{p} \boldsymbol{a}_0$ quand $N \to +\infty$.

**Démonstration** : En partant de l'expression de l'estimateur et en substituant $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$, on obtient :
$$\hat{\boldsymbol{a}}_N^{MCO} = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{x}_i(\mathbf{x}_i'\boldsymbol{a}_0 + u_i)$$

Après simplification :
$$\hat{\boldsymbol{a}}_N^{MCO} = \boldsymbol{a}_0 + \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1} \frac{1}{N}\sum_{i=1}^N \mathbf{x}_i u_i$$

La Loi des Grands Nombres implique que $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i' \xrightarrow{p} E[\mathbf{x}_i\mathbf{x}_i']$ et $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i u_i \xrightarrow{p} E[\mathbf{x}_i u_i]$. L'exogénéité des $\mathbf{x}_i$ assure que $E[\mathbf{x}_i u_i] = \mathbf{0}$.

L'inverse de $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'$ existe avec une probabilité approchant 1 et converge vers $(E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$. Par continuité de l'application inverse, on obtient :
$$\hat{\boldsymbol{a}}_N^{MCO} \xrightarrow{p} \boldsymbol{a}_0 + (E[\mathbf{x}_i\mathbf{x}_i'])^{-1} \cdot \mathbf{0} = \boldsymbol{a}_0$$

### Normalité asymptotique

La normalité asymptotique de l'estimateur des MCO découle de l'application du Théorème Central Limite aux termes aléatoires intervenant dans l'expression de l'estimateur.

**Propriété de normalité asymptotique** : Sous les conditions du modèle de régression, l'estimateur des MCO vérifie :
$$\sqrt{N}(\hat{\boldsymbol{a}}_N^{MCO} - \boldsymbol{a}_0) \xrightarrow{L} \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_0)$$

où la matrice de variance asymptotique $\boldsymbol{\Sigma}_0$ prend deux formes selon l'homoscédasticité ou l'hétéroscédasticité des termes d'erreur.

**Cas hétéroscédastique général** :
$$\boldsymbol{\Sigma}_0 = (E[\mathbf{x}_i\mathbf{x}_i'])^{-1} E[u_i^2 \mathbf{x}_i\mathbf{x}_i'] (E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$$

**Cas homoscédastique** : Si $E[u_i^2|\mathbf{x}_i] = \sigma_0^2$, alors :
$$\boldsymbol{\Sigma}_0 = \sigma_0^2 (E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$$

**Démonstration** : En utilisant la décomposition précédente, on a :
$$\sqrt{N}(\hat{\boldsymbol{a}}_N^{MCO} - \boldsymbol{a}_0) = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1} \frac{1}{\sqrt{N}}\sum_{i=1}^N \mathbf{x}_i u_i$$

Le Théorème Central Limite appliqué à $\frac{1}{\sqrt{N}}\sum_{i=1}^N \mathbf{x}_i u_i$ donne :
$$\frac{1}{\sqrt{N}}\sum_{i=1}^N \mathbf{x}_i u_i \xrightarrow{L} \mathcal{N}(\mathbf{0}, E[u_i^2 \mathbf{x}_i\mathbf{x}_i'])$$

puisque $E[\mathbf{x}_i u_i] = \mathbf{0}$ par exogénéité et $V[\mathbf{x}_i u_i] = E[u_i^2 \mathbf{x}_i\mathbf{x}_i']$.

La convergence de $\left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1}$ vers $(E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$ et l'application des propriétés de convergence des combinaisons de suites donnent le résultat final.

Dans le cas homoscédastique, la loi des espérances itérées permet de simplifier : $E[u_i^2 \mathbf{x}_i\mathbf{x}_i'] = E[E[u_i^2|\mathbf{x}_i] \mathbf{x}_i\mathbf{x}_i'] = \sigma_0^2 E[\mathbf{x}_i\mathbf{x}_i']$.

### Estimation de la variance asymptotique

L'utilisation pratique des résultats de normalité asymptotique nécessite l'estimation de la matrice de variance $\boldsymbol{\Sigma}_0$. Deux approches sont disponibles selon les hypothèses sur l'hétéroscédasticité.

**Propriété des estimateurs de la variance asymptotique** : La variance asymptotique $\boldsymbol{\Sigma}_0$ peut être estimée par :

**Estimateur robuste à l'hétéroscédasticité (White)** :
$$\hat{\boldsymbol{\Sigma}}_N^W = \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1} \left(\frac{1}{N}\sum_{i=1}^N \hat{u}_{i,N}^2 \mathbf{x}_i\mathbf{x}_i'\right) \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1}$$

**Estimateur sous homoscédasticité** :
$$\hat{\boldsymbol{\Sigma}}_N = \hat{\sigma}_N^2 \left(\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'\right)^{-1}$$

où $\hat{\sigma}_N^2 = \frac{1}{N-1}\sum_{i=1}^N \hat{u}_{i,N}^2$ et $\hat{u}_{i,N} = y_i - \mathbf{x}_i'\hat{\boldsymbol{a}}_N^{MCO}$.

L'estimateur de White est particulièrement utilisé par les micro-économètres qui travaillent sur des phénomènes hétérogènes où l'hypothèse d'homoscédasticité est peu plausible. Sa robustesse à l'hétéroscédasticité en fait un choix privilégié dans de nombreuses applications empiriques.

## Identification des paramètres

### Conditions de rang et unicité de la solution

L'identification des paramètres d'un modèle de régression linéaire nécessite non seulement l'exogénéité des variables explicatives, mais également une condition de rang qui garantit l'unicité de la solution du problème d'estimation.

Lorsque l'on utilise la méthode des moments avec la condition d'orthogonalité $E[\mathbf{x}_i(y_i - \mathbf{x}_i'\boldsymbol{a})] = \mathbf{0}$, il est essentiel que cette équation caractérise $\boldsymbol{a}_0$ de manière unique. Cette exigence conduit à la condition fondamentale d'inversibilité de $E[\mathbf{x}_i\mathbf{x}_i']$.

**Propriété d'unicité de la solution** : Soient $\mathbf{M}$ une matrice réelle $(P \times K)$, $\mathbf{x}$ un vecteur réel $(K \times 1)$ et $\mathbf{m}$ un vecteur réel $(P \times 1)$. L'équation $\mathbf{M}\mathbf{x} = \mathbf{m}$ admet une solution unique en $\mathbf{x}$ si et seulement si $\text{rang}(\mathbf{M}) = K = \dim(\mathbf{x})$ (ce qui suppose $P \geq K$).

**Propriétés de rang et inversibilité** : Soit $\mathbf{M}$ une matrice réelle carrée de dimension $P$. Les conditions suivantes sont équivalentes : $\mathbf{M}$ est inversible si et seulement si $\text{rang}(\mathbf{M}) = P$. Pour une matrice semi-définie positive, $\text{rang}(\mathbf{M}) = P$ équivaut à ce que $\mathbf{M}$ soit définie positive.

**Propriété d'identification dans le modèle de régression** : Soit $\{(y_i, \mathbf{x}_i); i = 1,2,...,N\}$ un échantillon de variables aléatoires réelles telles que $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ avec $E[u_i|\mathbf{x}_i] = E[u_i] \equiv 0$. Le vecteur de paramètres $\boldsymbol{a}_0$ est identifiable si et seulement si $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$, ce qui équivaut à dire que $E[\mathbf{x}_i\mathbf{x}_i']$ est inversible.

### Interprétation des conditions de rang

La condition de rang sur $E[\mathbf{x}_i\mathbf{x}_i']$ admet une interprétation intuitive en termes de variation des variables explicatives. En notant $\mathbf{x}_i = (1, \tilde{\mathbf{x}}_i')'$ où $\tilde{\mathbf{x}}_i$ représente les variables explicatives autres que la constante, la condition d'inversibilité équivaut à :

1.  $V(\tilde{x}_{k,i}) > 0$ pour tout $k = 1,...,K-1$ (chaque variable explicative doit varier)
2.  Les éléments de $\tilde{\mathbf{x}}_i$ ne sont pas parfaitement linéairement liés entre eux
3.  $V[\tilde{\mathbf{x}}_i]$ est inversible (absence de multicolinéarité parfaite)

Cette condition représente l'équivalent asymptotique de la condition $\text{rang}(\mathbf{X}) = K$ utilisée à distance finie. Elle garantit que chaque paramètre du modèle peut être identifié de manière unique à partir de la variation des données.

### Distinction entre conditions générales et internes

L'analyse de l'identification distingue deux types de conditions :

**Conditions d'identification générales** : La condition $E[u_i|\mathbf{x}_i] = \mathbf{0}$ est générale par rapport au modèle linéaire $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ avec $E[u_i] \equiv 0$. Elle assure que le modèle de régression est bien spécifié.

**Conditions d'identification internes** : La condition "E[\mathbf{x}_i\mathbf{x}_i']$ est inversible" est interne au modèle de régression linéaire. Elle garantit l'unicité de la solution une fois que l'exogénéité est établie.

Ces conditions sont complémentaires : $\boldsymbol{a}_0$ est identifié dans le modèle de régression linéaire si et seulement si $E[\mathbf{x}_i(y_i - \mathbf{x}_i'\boldsymbol{a})] = \mathbf{0}$ implique $\boldsymbol{a} = \boldsymbol{a}_0$, ce qui équivaut à dire que $\boldsymbol{a}_0$ est l'unique solution de cette équation.

## La projection linéaire et ses propriétés

### Définition et caractérisation

La projection linéaire constitue un concept central qui éclaire la nature de l'estimateur des MCO et ses liens avec la prédiction optimale. Elle représente une forme d'espérance conditionnelle linéaire qui généralise la notion de régression.

**Propriété de projection linéaire** : La projection linéaire de $y_i$ sur $\mathbf{x}_i$, notée $EL[y_i|\mathbf{x}_i]$, est définie par :
$$EL[y_i|\mathbf{x}_i] \equiv \mathbf{x}_i'\boldsymbol{\gamma}$$

où $\boldsymbol{\gamma} \equiv \arg\min_{\mathbf{g}} E[(y_i - \mathbf{x}_i'\mathbf{g})^2]$. Le paramètre $\boldsymbol{\gamma}$ est unique si et seulement si $E[\mathbf{x}_i\mathbf{x}_i']$ est inversible.

**Interprétation** : $EL[y_i|\mathbf{x}_i]$ représente la meilleure prédiction linéaire de $y_i$ par $\mathbf{x}_i$ au sens de l'espérance de l'erreur quadratique. La linéarité en $\mathbf{x}_i$ distingue cette projection de l'espérance conditionnelle générale $E[y_i|\mathbf{x}_i] \equiv \arg\min_{m(\cdot)} E[(y_i - m(\mathbf{x}_i))^2]$.

### Propriétés fondamentales

**Propriétés de la projection linéaire** : La projection linéaire $EL[y_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{\gamma}$ vérifie :

1.  **Orthogonalité** : Le résidu de projection $e_i \equiv y_i - \boldsymbol{\gamma}'\mathbf{x}_i$ vérifie $E[e_i|\mathbf{x}_i] = \mathbf{0}$.

2.  **Expression explicite** : Si $E[\mathbf{x}_i\mathbf{x}_i']$ est inversible, alors $\boldsymbol{\gamma} = (E[\mathbf{x}_i\mathbf{x}_i'])^{-1}E[\mathbf{x}_i y_i]$.

3.  **Décomposition avec constante** : Si $\mathbf{x}_i = (1, \tilde{\mathbf{x}}_i')'$, alors :
    $$\boldsymbol{\gamma}' = (\delta, \boldsymbol{\lambda}')$$
    
    avec $\boldsymbol{\lambda} = V[\tilde{\mathbf{x}}_i]^{-1}\text{Cov}[y_i, \tilde{\mathbf{x}}_i]$ et $\delta = E[y_i] - \boldsymbol{\lambda}'E[\tilde{\mathbf{x}}_i]$.

### Liens avec le modèle de régression

La projection linéaire entretient des liens profonds avec le modèle de régression linéaire, permettant de distinguer les aspects d'ajustement des aspects causals.

**Équivalence projection-régression** : Les deux propositions suivantes sont équivalentes :

$$y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i \text{ avec } E[u_i|\mathbf{x}_i] = E[u_i] = 0$$

$$EL[y_i|\mathbf{x}_i] = E[y_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{a}_0$$

Cette équivalence révèle que la projection de $y_i$ sur $\mathbf{x}_i$ coïncide avec la partie déterministe d'un modèle de $y_i$ en $\mathbf{x}_i$ si et seulement si $y_i$ suit un modèle de régression linéaire en $\mathbf{x}_i$. Deux conditions sont nécessaires : la linéarité du modèle et l'exogénéité des variables explicatives.

### Décomposition universelle

**Propriété de décomposition** : On peut toujours écrire $y_i$ sous la forme :
$$y_i = \boldsymbol{\gamma}'\mathbf{x}_i + e_i$$

avec $E[e_i|\mathbf{x}_i] = \mathbf{0}$, en choisissant $\boldsymbol{\gamma} \equiv \arg\min_{\mathbf{g}} E[(y_i - \mathbf{x}_i'\mathbf{g})^2]$.

Cette décomposition reste valable même si $y_i$ ne suit pas un modèle de régression linéaire. Il est toujours possible de calculer un estimateur convergent de $\boldsymbol{\gamma}$ et donc de $EL[y_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{\gamma}$.

**Distinction fondamentale** : L'équation $y_i = \boldsymbol{\gamma}'\mathbf{x}_i + e_i$ ne définit pas un modèle économétrique de $y_i$ en fonction de $\mathbf{x}_i$. Cette équation constitue une décomposition mathématique de $y_i$ en sa projection linéaire sur $\mathbf{x}_i$ et le résidu de cette projection, orthogonal à $\mathbf{x}_i$ par construction.

### Lien avec l'estimateur des MCO

**Propriété MCO-projection** : L'estimation par MCO fournit toujours un estimateur du paramètre de la projection linéaire :

Si $EL[y_i|\mathbf{x}_i] = \mathbf{x}_i'\boldsymbol{\gamma}$, alors $\hat{\boldsymbol{a}}_{MCO,N} \xrightarrow{p} \boldsymbol{\gamma}$ lorsque $N \to +\infty$.

Cette convergence implique que $\mathbf{x}_i'\hat{\boldsymbol{\gamma}}_{MCO,N}$ représente le meilleur prédicteur linéaire de $y_i$ en fonction de $\mathbf{x}_i$. Cependant, $\hat{\boldsymbol{a}}_{MCO,N}$ n'est un estimateur convergent du paramètre causal $\boldsymbol{a}_0$ que si le modèle considéré est effectivement un modèle de régression.

Cette distinction entre identification d'effets causals et optimisation de l'ajustement ou de la prédiction constitue un point crucial en économétrie appliquée.

## Analyse des conditions de rang

### Interprétation des conditions d'identification

La condition d'identification $E[\mathbf{x}_i\mathbf{x}_i']$ inversible peut être analysée plus finement grâce aux projections linéaires. Cette approche permet de comprendre concrètement ce que signifient les conditions de rang.

Avec $\mathbf{x}_i = (1, \tilde{\mathbf{x}}_i')'$, la condition $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$ équivaut à $V[\tilde{\mathbf{x}}_i]$ inversible, ce qui se traduit par :

1.  $V(\tilde{x}_{k,i}) > 0$ pour tout $k = 1,...,K-1$ (chaque variable explicative doit varier)

2.  Les éléments de $\tilde{\mathbf{x}}_i$ ne sont pas parfaitement linéairement liés entre eux (absence de multicolinéarité parfaite)

### Concept de partie spécifique

Pour analyser plus précisément ces conditions, on introduit le concept de partie spécifique d'une variable explicative.

**Définition de partie spécifique** : Une variable $\tilde{x}_{k,i}$ d'un vecteur $\tilde{\mathbf{x}}_i$ peut toujours être décomposée :
$$\tilde{x}_{k,i} = EL[\tilde{x}_{k,i}|\tilde{\mathbf{x}}_{i,-k}] + \tilde{e}_{k,i}$$

où $\tilde{e}_{k,i} \equiv \tilde{x}_{k,i} - EL[\tilde{x}_{k,i}|\tilde{\mathbf{x}}_{i,-k}]$ représente la partie spécifique de $\tilde{x}_{k,i}$ dans $\tilde{\mathbf{x}}_i$. Le vecteur $\tilde{\mathbf{x}}_{i,-k}$ désigne $\tilde{\mathbf{x}}_i$ amputé de $\tilde{x}_{k,i}$.

Avec $EL[\tilde{x}_{k,i}|\tilde{\mathbf{x}}_{i,-k}] \equiv \delta_k + \boldsymbol{\lambda}_{k,-k}'\tilde{\mathbf{x}}_{i,-k}$, on obtient :

$$\tilde{x}_{k,i} = \underbrace{\delta_k + \boldsymbol{\lambda}_{k,-k}'\tilde{\mathbf{x}}_{i,-k}}_{\text{Partie corrélée à } (1,\tilde{\mathbf{x}}_{i,-k}')'} + \underbrace{\tilde{e}_{k,i}}_{\text{Partie spécifique de } \tilde{x}_{k,i}}$$

### Propriétés des parties spécifiques

Les parties spécifiques $\tilde{e}_{k,i}$ vérifient des propriétés fondamentales :

1.  **Espérance nulle et orthogonalité** : $E[\tilde{e}_{k,i}] = 0$ et $E[\tilde{\mathbf{x}}_{i,-k}'\tilde{e}_{k,i}] = \mathbf{0}$

2.  **Orthogonalité mutuelle** : $E[\tilde{e}_{k,i}\tilde{e}_{\ell,i}] = \text{Cov}(\tilde{e}_{k,i}, \tilde{e}_{\ell,i}) = 0$ si $k \neq \ell$

3.  **Multicolinéarité parfaite** : S'il existe $\mathbf{m}_k$ et $\eta_k$ tels que $\tilde{x}_{k,i} = \eta_k + \mathbf{m}_k'\tilde{\mathbf{x}}_{i,-k}$, alors $\tilde{e}_{k,i} = 0$

**Interprétation** : La partie spécifique $\tilde{e}_{k,i}$ représente la part d'information spécifique à $\tilde{x}_{k,i}$ dans un modèle linéaire en $\tilde{\mathbf{x}}_i$. Elle est nulle en cas de multicolinéarité parfaite et constitue la source de variation qui permet d'identifier les paramètres correspondants.

### Conditions de rang reformulées

**Théorème d'équivalence des conditions de rang** : Les conditions suivantes sont équivalentes :

1.  $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$
2.  $E[\mathbf{x}_i\mathbf{x}_i']$ est inversible
3.  $V[\tilde{\mathbf{x}}_i]$ est inversible
4.  $V[\tilde{e}_{k,i}] > 0$ pour $k = 1,...,K-1$

La dernière condition exprime qu'chaque variable explicative doit posséder une véritable partie spécifique, c'est-à-dire une source de variation qui lui est propre.

## Anatomie de l'estimateur des MCO

### Mécanisme d'identification

L'analyse par les parties spécifiques révèle le mécanisme fondamental d'identification dans un modèle de régression linéaire.

Considérons le modèle : $y_i = \alpha_0 + \sum_{k=1}^{K-1} b_{k,0}\tilde{x}_{k,i} + u_i$ avec $E[u_i] = 0$.

En substituant la décomposition $\tilde{x}_{k,i} = \delta_k + \boldsymbol{\lambda}_{k,-k}'\tilde{\mathbf{x}}_{i,-k} + \tilde{e}_{k,i}$, on obtient après regroupement :

$$y_i = (\alpha_0 + \sum_{k=1}^{K-1} b_{k,0}\delta_k) + \sum_{k=1}^{K-1} b_{k,0}\tilde{e}_{k,i} + \sum_{\ell \neq k} b_{k,0}\boldsymbol{\lambda}_{k,-k}'\tilde{\mathbf{x}}_{i,-\ell} + u_i$$

Cette reformulation montre que ce sont les variations de $\tilde{e}_{k,i}$ qui identifient $b_{k,0}$. Le reste de $\tilde{x}_{k,i}$ (sa projection sur les autres variables) ne contribue pas spécifiquement à l'identification du paramètre correspondant.

### Expression de l'estimateur

**Propriété d'anatomie de l'estimateur MCO** : L'estimateur des MCO peut être exprimé sous la forme :

$$b_{\ell,0} = V[\tilde{e}_{\ell,i}]^{-1}\text{Cov}(\tilde{e}_{\ell,i}, y_i)$$

pour $\ell = 2,...,K$, ou de manière équivalente :

$$\boldsymbol{b}_0 = V[\tilde{\mathbf{e}}_i]^{-1}\text{Cov}(\tilde{\mathbf{e}}_i, y_i)$$

où $\tilde{\mathbf{e}}_i = (\tilde{e}_{1,i},...,\tilde{e}_{K-1,i})'$.

L'équivalence entre ces formulations provient du fait que la matrice $V[\tilde{\mathbf{e}}_i]$ est diagonale par construction (les parties spécifiques ne sont pas corrélées entre elles).

**Interprétation** : Le terme $\text{Cov}(\tilde{e}_{\ell,i}, y_i) = \text{Cov}(\tilde{x}_{\ell,i} - EL[\tilde{x}_{\ell,i}|\tilde{\mathbf{x}}_{i,-\ell}], y_i)$ représente la covariance de $\tilde{x}_{\ell,i}$ et $y_i$ purgée de la partie de $\tilde{x}_{\ell,i}$ corrélée aux autres éléments de $\tilde{\mathbf{x}}_i$. Cette analyse retrouve l'idée de covariance partielle associée à la régression, illustrant comment les MCO mesurent des effets "toutes choses égales par ailleurs".

## Efficacité de l'estimation

### Précision asymptotique

Dans le cas homoscédastique, la loi asymptotique de l'estimateur des MCO s'écrit :

$$\sqrt{N}(\hat{\boldsymbol{a}}_{MCO,N} - \boldsymbol{a}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \sigma_0^2(E[\mathbf{x}_i\mathbf{x}_i'])^{-1})$$

La matrice $(E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$ mesure la précision asymptotique de l'estimateur. La précision est d'autant plus grande que :

1.  $\sigma_0^2$ est petit (termes d'erreur du modèle faibles)
2.  $(E[\mathbf{x}_i\mathbf{x}_i'])^{-1}$ est petite au sens de l'ordre matriciel, soit $E[\mathbf{x}_i\mathbf{x}_i']$ grande

### Conditions d'estimation précise

**Facteurs déterminant la précision** : Dans un modèle de régression linéaire, on obtient une estimation précise de $\boldsymbol{a}_0$ si :

1.  **Pouvoir explicatif élevé** : Les termes d'erreur du modèle sont petits, indiquant que le pouvoir explicatif de $\tilde{\mathbf{x}}_i$ pour $y_i$ est important (bonne spécification de la forme fonctionnelle)

2.  **Absence de multicolinéarité** : Les éléments de $\tilde{\mathbf{x}}_i$ sont peu corrélés entre eux, garantissant que les $\tilde{e}_{k,i}$ constituent des parts importantes des $\tilde{x}_{k,i}$

3.  **Variabilité suffisante** : Les $\tilde{e}_{k,i}$ sont suffisamment variables (absence de variables explicatives quasi-constantes)

### Analogie avec les plans d'expérience

La condition $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$ en théorie asymptotique s'apparente à la condition $\text{rang}(\mathbf{X}) = K$ en échantillon fini lorsque $\mathbf{X}$ est considérée comme fixe. Des conditions analogues aux précédentes guident la construction de plans d'expérience efficaces.

En agronomie, pour étudier l'effet de deux facteurs $\tilde{x}_1$ et $\tilde{x}_2$ sur $y$, il faut :

1.  Faire suffisamment varier les niveaux des deux facteurs (dans la limite de validité du modèle)
2.  Ne pas faire varier systématiquement ensemble les niveaux des facteurs (éviter la colinéarité)

## Diagnostic des problèmes d'identification

### Problèmes empiriques courants

En pratique économétrique, la matrice $\mathbf{X}$ est généralement de plein rang colonne. Cependant, des problèmes peuvent survenir lorsque certains éléments de $\tilde{\mathbf{x}}_i$ sont fortement (sans l'être parfaitement) linéairement liés entre eux, ou lorsque certaines variables sont très peu variables.

Ces situations ne posent pas de problème théorique mais créent de sérieux problèmes pratiques : l'estimation de $\boldsymbol{a}_0$ devient impossible ou très peu précise (et très instable).

### Indicateurs de problèmes

On détecte ces problèmes lorsque :

1.  Le logiciel refuse d'inverser $\mathbf{X}'\mathbf{X} = \sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'$
2.  Les valeurs estimées de $\hat{\boldsymbol{\Sigma}}_N^W$ ou $\hat{\boldsymbol{\Sigma}}_N$ sont très grandes (écarts-types estimés "énormes")

**Analyse diagnostique** : Si l'écart-type estimé de $\hat{\alpha}_{MCO,N}$ est très grand et :

*   Si seul celui de $\hat{b}_{k,MCO,N}$ est également très grand, alors la variable $\tilde{x}_{k,i}$ varie trop peu
*   Si ceux de $\hat{b}_{k,MCO,N}$ et $\hat{b}_{\ell,MCO,N}$ sont très grands, alors soit ces variables varient trop peu, soit elles sont fortement linéairement liées

Le diagnostic peut être affiné en analysant les relations entre variables par les techniques de projection linéaire.

### Problèmes de multicolinéarité spécifiques

Les problèmes de multicolinéarité sont fréquents en économétrie, mais les économètres n'utilisent généralement pas les procédures statistiques standards (régression sur composantes principales, etc.).

**Exemples typiques** :

1.  **Économétrie de la consommation** : Modèles de la forme
    $$Cons_i = \alpha_0 + b_{1,0} prix_{1,i} + b_{2,0} prix_{2,i} + b_{3,0} revenu_i + u_i$$

    avec $prix_{1,i}$ et $prix_{2,i}$ très liés. Solution habituelle : retirer une des variables ou abandonner l'estimation.

2.  **Effets âge-expérience-génération** : Ces trois variables sont par définition linéairement liées (âge = expérience + âge d'entrée sur le marché du travail), posant un problème d'identification fondamental.

### Multicolinéarité dans les données de panel

**Données hiérarchisées ou en clusters** : Considérons le modèle
$$y_{it} = \alpha_{i,0}\tilde{d}_i + \alpha_{t,0}\tilde{d}_t + b_{1,0}\tilde{x}_{it} + b_{2,0}\tilde{x}_{2,it} + b_{3,0}\tilde{x}_{3,t} + u_{it}$$

où $\tilde{d}_i = 1$ si observation de l'individu $i$, 0 sinon.

**Problèmes d'identification** :

*   Les $\alpha_{i,0}$ et $b_{2,0}$ ne sont pas identifiables séparément si $\tilde{x}_{2,it}$ varie essentiellement avec $i$ et $I$ (nombre d'individus) est petit
*   Les $\alpha_{t,0}$ et $b_{3,0}$ ne sont pas identifiables séparément si $\tilde{x}_{3,t}$ varie essentiellement avec $t$ et $T$ (nombre de périodes) est petit

**Exemple agricole** : Si $y_{it}$ représente la production de l'exploitation $i$ en période $t$, $\tilde{x}_{it}$ les prix agricoles, et $\tilde{x}_{3,t}$ un trend de progrès technique avec des indicatrices annuelles pour le climat, alors :

*   Les variations de $\tilde{x}_{it}$ dans le temps reflètent l'évolution générale du marché
*   Les variations de $\tilde{x}_{it}$ entre individus reflètent les spécificités des marchés locaux ou la qualité des produits

Si la qualité constitue un problème, $\tilde{x}_{it}$ peut devenir endogène, soulevant des questions sur le calcul des indices de volume et de prix.

## Remarques importantes sur l'exogénéité

### Limites des diagnostics automatiques

Aucun logiciel ne peut détecter si $E[u_i|\mathbf{x}_i] \neq \mathbf{0}$ dans un modèle linéaire. Si l'utilisateur demande le calcul de $\hat{\boldsymbol{a}}_{MCO,N}$, le logiciel l'effectuera indépendamment du caractère biaisé ou non de cet estimateur. Cette vérification relève de la responsabilité de l'économètre et constitue l'objet des développements ultérieurs du cours.

### Projection universelle et identification causale

**Propriété générale des projections** : On suppose que $V[\tilde{\mathbf{x}}_i]$ est inversible et on note $EL[y_i|\mathbf{x}_i] = \delta + \boldsymbol{\lambda}'\tilde{\mathbf{x}}_i = \boldsymbol{\gamma}'\mathbf{x}_i$.

Avec les parties spécifiques $\tilde{e}_{k,i}$ définies précédemment et $\tilde{\mathbf{e}}_i = (\tilde{e}_{1,i},...,\tilde{e}_{K-1,i})'$, on a :

1.  $\boldsymbol{\gamma}' = (\delta, \boldsymbol{\lambda}')$ avec $\boldsymbol{\lambda} = V[\tilde{\mathbf{x}}_i]^{-1}\text{Cov}(y_i, \tilde{\mathbf{x}}_i)$ et $\delta = E[y_i] - \boldsymbol{\lambda}'E[\tilde{\mathbf{x}}_i]$

2.  $\boldsymbol{\lambda} = V[\tilde{\mathbf{e}}_i]^{-1}\text{Cov}(y_i, \tilde{\mathbf{e}}_i]$

3.  $EL[y_i|\tilde{\mathbf{e}}_i] = E[y_i] + \boldsymbol{\lambda}'\tilde{\mathbf{e}}_i = EL[y_i|\mathbf{x}_i]$

Cette dernière propriété indique que projeter $y_i$ sur $\mathbf{x}_i$ ou sur $(1, \tilde{\mathbf{e}}_i')'$ produit la même projection, car $(1, \tilde{\mathbf{e}}_i')'$ constitue une combinaison linéaire des éléments de $\mathbf{x}_i$.

## Synthèse du chapitre

### Conditions fondamentales

Un modèle linéaire $y_i = \boldsymbol{a}_0'\mathbf{x}_i + u_i$ avec $E[u_i] = 0$ constitue un modèle de régression si et seulement si $E[u_i|\mathbf{x}_i] = \mathbf{0}$. Cette condition d'exogénéité doit être examinée théoriquement par analyse du processus générateur commun des $(y_i, \mathbf{x}_i)$.

Le paramètre $\boldsymbol{a}_0$ est identifiable dans ce modèle de régression si et seulement si $V[\tilde{\mathbf{x}}_i]$ est inversible, condition équivalente à $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$ ou $E[\mathbf{x}_i\mathbf{x}_i']$ inversible. Cette condition peut être vérifiée empiriquement.

### Condition d'orthogonalité et estimation

Lorsque les conditions précédentes sont satisfaites, le modèle $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ avec $E[u_i] = 0$ et $E[u_i|\mathbf{x}_i] = \mathbf{0}$ implique la validité de la condition d'orthogonalité :

$$E[(y_i - \mathbf{x}_i'\boldsymbol{a}_0)\mathbf{x}_i] = \mathbf{0}_{K \times 1}$$

Cette condition de moment, fondée sur l'exogénéité de $\mathbf{x}_i$, caractérise $\boldsymbol{a}_0$ de manière unique.

### Application du principe d'analogie

Le principe d'analogie définit l'estimateur de la Méthode des Moments $\hat{\boldsymbol{a}}^{MM}_N$ à partir de la contrepartie empirique :

$$\hat{\boldsymbol{a}}^{MM}_N \text{ est solution de } \frac{1}{N}\sum_{i=1}^N (y_i - \mathbf{x}_i'\boldsymbol{a})\mathbf{x}_i = \mathbf{0}_{K \times 1}$$

On démontre alors que $\hat{\boldsymbol{a}}_{MM,N} = \hat{\boldsymbol{a}}_{MCO,N}$ et que :

$$\sqrt{N}(\hat{\boldsymbol{a}}_{MCO,N} - \boldsymbol{a}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, (E[\mathbf{x}_i\mathbf{x}_i'])^{-1}E[u_i^2\mathbf{x}_i\mathbf{x}_i'](E[\mathbf{x}_i\mathbf{x}_i'])^{-1})$$

### Cas homoscédastique

Dans le cas où les termes d'erreur sont homoscédastiques ($E[u_i^2|\mathbf{x}_i] = V[u_i|\mathbf{x}_i] = \sigma_0^2$), on a :

$$E[u_i^2\mathbf{x}_i\mathbf{x}_i'] = \sigma_0^2 E[\mathbf{x}_i\mathbf{x}_i']$$

et donc :

$$\sqrt{N}(\hat{\boldsymbol{a}}_{MCO,N} - \boldsymbol{a}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \sigma_0^2(E[\mathbf{x}_i\mathbf{x}_i'])^{-1})$$

### Distinction ajustement-identification

Le cours établit une distinction fondamentale : si $E[u_i|\mathbf{x}_i] \neq \mathbf{0}$ (endogénéité), alors :

1.  $\hat{\boldsymbol{a}}_{MCO,N} \xrightarrow{p} \boldsymbol{\gamma} \neq \boldsymbol{a}_0$ (estimateur biaisé)

2.  $\boldsymbol{\gamma} \equiv \arg\min_{\mathbf{g}} E[(y_i - \mathbf{x}_i'\mathbf{g})^2]$ (paramètre de projection linéaire)

Dans tous les cas, l'estimateur des MCO permet de calculer de bonnes prédictions linéaires de $y_i$ par $\mathbf{x}_i$ : $\mathbf{x}_i'\hat{\boldsymbol{a}}_{MCO,N} \xrightarrow{p} \mathbf{x}_i'\boldsymbol{\gamma}$.

Cependant, une mesure satisfaisante de $\boldsymbol{a}_0$ (l'effet causal recherché) n'est obtenue que si $E[u_i|\mathbf{x}_i] = \mathbf{0}$, condition d'exogénéité de $\mathbf{x}_i$ par rapport à $u_i$. Cette différence cruciale sépare une logique d'ajustement d'une logique d'identification.

## Analyse approfondie des conditions d'identification

### Démarche générale d'identification

La démarche d'identification des paramètres d'un modèle de régression linéaire suit une logique méthodique. Premièrement, on définit $\boldsymbol{a}_0$ comme la solution d'un problème théorique appelé "problème limite". Dans le cas du modèle de régression linéaire, ce problème s'énonce ainsi :

$$\boldsymbol{a}_0 \text{ est solution en } \boldsymbol{a} \text{ de l'équation } E[(y_i - \mathbf{x}_i'\boldsymbol{a})\mathbf{x}_i] = \mathbf{0}$$

Cette équation découle directement de la forme du modèle $y_i = \mathbf{x}_i'\boldsymbol{a}_0 + u_i$ avec $E[u_i] = 0$, combinée à l'exogénéité de $\mathbf{x}_i$ par rapport à $u_i$ qui implique $E[u_i|\mathbf{x}_i] = \mathbf{0}$.

Deuxièmement, on considère que $\boldsymbol{a}_0$ est identifié si et seulement si $\boldsymbol{a}_0$ constitue la solution unique du problème théorique considéré. Dans le cadre du modèle de régression linéaire, cette unicité est garantie si et seulement si $E[\mathbf{x}_i\mathbf{x}_i']$ est inversible.

### Justification par le principe d'analogie

Cette démarche trouve sa justification dans l'utilisation du principe d'analogie. Le problème théorique considéré représente également le problème limite (quand $N \to +\infty$) du problème empirique utilisé pour calculer l'estimateur $\hat{\boldsymbol{a}}_N$ de $\boldsymbol{a}_0$.

La Loi des Grands Nombres et ses variantes permettent alors d'espérer que si le problème théorique identifie correctement $\boldsymbol{a}_0$, alors le problème empirique doit permettre de calculer un estimateur $\hat{\boldsymbol{a}}_N$ "proche" de $\boldsymbol{a}_0$ lorsque $N$ est grand bien que fini.

En substance, pour analyser les conditions d'identification de $\boldsymbol{a}_0$, on se place dans "le meilleur des cas", celui où l'on dispose d'un échantillon de taille infinie, sachant qu'empiriquement on sera dans une situation proche si on dispose d'un grand échantillon (sous certaines conditions de régularité).

### Application pratique des conditions de rang

Pour le cas d'un modèle de régression linéaire, si $N$ est grand et $\text{rang}(E[\mathbf{x}_i\mathbf{x}_i']) = K$, alors il y a très peu de chances que $\frac{1}{N}\sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'$ (et donc $\mathbf{X}'\mathbf{X} = \sum_{i=1}^N \mathbf{x}_i\mathbf{x}_i'$) ne soit pas inversible.

Cette observation pratique souligne l'importance de la condition de rang théorique pour garantir l'existence de l'estimateur des MCO dans les applications empiriques. Elle établit également le lien entre les propriétés asymptotiques (théoriques) et les propriétés à distance finie (pratiques) de l'estimateur.