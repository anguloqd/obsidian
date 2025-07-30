# 01 // rappels sur régression linéaire

[01_rappels_sur_regression_lineaire_l1_regressionlineaire_intro_1.pdf](ressources/01_rappels_sur_regression_lineaire_l1_regressionlineaire_intro_1.pdf)

## Deux exemples d'effets causaux difficiles à identifier

### Identification des paramètres d'un modèle

Variables explicatives exogènes, variables explicatives endogènes, modèle de régression

### Le problème de l'identification, covariances et paramètres

Les concepts présentés à partir des exemples sont présentés dans le cas général

## Formation et salaire

On analyse ici un problème « emblématique » (qui a valu le prix Nobel à Heckman en 2000), sous une forme un peu caricaturale.

**Objectif.** On veut estimer l'effet moyen, en termes de salaire, d'une formation BAC+5 par rapport à un BAC seul. On veut l'effet causal moyen de la formation BAC+5 :

$$x_i \tilde{} \rightarrow y_i$$

effet d'acquis de connaissances sur le salaire

C'est une mesure de l'efficacité « économique » du BAC+5.

**Les données.** Un grand échantillon ($i = 1,...,N$) de jeunes salariés avec le « BAC » ($\tilde{x_i} = 0$) et avec « BAC+5 » ($\tilde{x_i} = 1$). On dispose de leurs salaires, $y_i$, 10 ans après leur BAC. Ces salariés ont tous le même âge, sexe, …

### Examen théorique de la question posée

Une manière simple de poser le problème consiste à écrire le modèle :

$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

On a alors :
- Salaire d'un « BAC » ($\tilde{x_i} = 0$) : $\alpha_0 + u_i$
- Salaire moyen d'un « BAC » ($\tilde{x_i} = 0$) : $\alpha_0$
- Salaire d'un « BAC+5 » ($\tilde{x_i} = 1$) : $\alpha_0 + b_0 + u_i$
- Salaire moyen d'un « BAC+5 » ($\tilde{x_i} = 1$) : $\alpha_0 + b_0$
- Effet BAC+5 / BAC : $b_0$

Reste maintenant à estimer $b_0$, mais avant ça il faut savoir si $b_0$ est :
« Estimable » avec les données disponibles ⇔ identifiable

### Examen de l'identification des paramètres du modèle

$$\mathbf{a_0} \equiv (\alpha_0, b_0)$$
$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

On va en fait montrer ici que $\mathbf{a_0} \equiv (\alpha_0, b_0)$ est identifiable avec les données disponibles, i.e. les $(y_i, \tilde{x_i})$ avec $i = 1,...,N$, si et seulement si $\text{Cov}[\tilde{x_i}; u_i] = 0$.

L'intuition sous-jacente est simple :

1. Le seul estimateur de $\mathbf{a_0} \equiv (\alpha_0, b_0)$ qu'on sache estimer à partir des données disponibles est l'estimateur des MCO.
2. L'estimateur des MCO de $\mathbf{a_0} \equiv (\alpha_0, b_0)$ est biaisé si $\text{Cov}[\tilde{x_i}; u_i] \neq 0$.
3. On ne peut estimer $\text{Cov}[\tilde{x_i}; u_i]$ puisque les $u_i$ ne sont pas observés.

On montrera ensuite que, dans le cas de l'effet de « BAC+5 » sur le salaire, on a vraisemblablement $\text{Cov}[\tilde{x_i}; u_i] > 0$.

### L'estimateur des MCO

L'estimateur des MCO de $\mathbf{a_0}$, $\hat{\mathbf{a}}_{MCO}^N$, ne converge pas vers $\mathbf{a_0}$ si $\text{Cov}[\tilde{x_i}; u_i] \neq 0$

Avec $\mathbf{a_0} \equiv (\alpha_0, b_0)$ et $\mathbf{x_i} \equiv (1, \tilde{x_i})$, on écrit ici le modèle sous la forme générale « compacte » :

$$y_i = \mathbf{x_i'} \mathbf{a_0} + u_i \text{ avec } E[u_i] \equiv 0$$

L'estimateur des MCO de $\mathbf{a_0}$ est donné par (voir le cours de régression) :

$$\hat{\mathbf{a}}_{MCO}^N \equiv (\mathbf{X'X})^{-1} \mathbf{X'y}$$

avec :

$$\mathbf{y} \equiv \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_N \end{pmatrix}_{N \times 1}$$

et

$$\mathbf{X} \equiv \begin{pmatrix} \mathbf{x_1'} \\ \mathbf{x_2'} \\ \vdots \\ \mathbf{x_N'} \end{pmatrix} = \begin{pmatrix} x_{1,1} & x_{2,1} & \cdots & x_{K,1} \\ x_{1,2} & x_{2,2} & \cdots & x_{K,2} \\ \vdots & \vdots & \ddots & \vdots \\ x_{1,N} & x_{2,N} & \cdots & x_{K,N} \end{pmatrix}_{N \times K}$$

Nous écrirons ici l'estimateur des MCO sous la forme :

$$\hat{\mathbf{a}}_{MCO}^N = \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} y_i$$

en utilisant :

$$\mathbf{X'X} = \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'}$$ et $$\mathbf{X'y} = \sum_{i=1}^{N} \mathbf{x_i} y_i$$

et en multipliant par $\frac{1}{N}$ les deux $\sum_{i=1}^{N} ...$

Cette écriture est « lourde » mais facilite l'analyse de la convergence de $\hat{\mathbf{a}}_{MCO}^N$ puisqu'on utilise la LGN.

On veut ici montrer que :

$$\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0} \text{ si } \text{Cov}[\tilde{x_i}; u_i] = 0$$

et :

$$\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0} + \boldsymbol{\beta} \text{ avec } \boldsymbol{\beta} \neq \mathbf{0} \text{ si } \text{Cov}[\tilde{x_i}; u_i] \neq 0$$

> **Remarque.** Pour tous les estimateurs de cette partie : $\hat{\mathbf{a}}^N = \mathbf{a_0} + \frac{1}{N} \sum_{i=1}^{N} ...$

Le modèle de $y_i$ nous donne que $y_i = \mathbf{x_i'} \mathbf{a_0} + u_i$, on a donc :

$$\hat{\mathbf{a}}_{MCO}^N = \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} (\mathbf{x_i'} \mathbf{a_0} + u_i)$$

Après développement, on obtient :

$$\hat{\mathbf{a}}_{MCO}^N = \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \mathbf{a_0} + \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} u_i$$

et après simplifications :

$$\hat{\mathbf{a}}_{MCO}^N = \mathbf{a_0} + \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} u_i$$

car :

$$\left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \mathbf{a_0} = \mathbf{a_0}$$

> **Remarque.** Pour tous les estimateurs de cette partie : $\hat{\mathbf{a}}^N = \mathbf{a_0} + \frac{1}{N} \sum_{i=1}^{N} u_i ...$

L'estimateur des MCO est convergent pour $\mathbf{a_0}$, i.e. $\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0}$, si :

$$\left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} u_i \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{0}$$

On sait, par la loi LGN, que :

$$\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \xrightarrow{p}_{N \rightarrow +\infty} E[\mathbf{x_i} \mathbf{x_i'}]$$ 

et 

$$\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} u_i \xrightarrow{p}_{N \rightarrow +\infty} E[\mathbf{x_i} u_i]$$

En combinant ces résultats on obtient :

$$\left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} \mathbf{x_i'} \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x_i} u_i \xrightarrow{p}_{N \rightarrow +\infty} E[\mathbf{x_i} \mathbf{x_i'}]^{-1} \times E[\mathbf{x_i} u_i] = E[\mathbf{x_i} \mathbf{x_i'}]^{-1} \times \text{Cov}[\tilde{x_i}; u_i]$$

Finalement on obtient :

$$\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0} + E[\mathbf{x_i} \mathbf{x_i'}]^{-1} \text{Cov}[\tilde{x_i}; u_i]$$

et donc :

$$\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0} \text{ si } \text{Cov}[\tilde{x_i}; u_i] = 0$$

et :

$$\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a_0} + \boldsymbol{\beta} \text{ avec } \boldsymbol{\beta} \neq \mathbf{0} \text{ si } \text{Cov}[\tilde{x_i}; u_i] \neq 0$$

Puisque $\hat{\mathbf{a}}_{MCO}^N$ est le seul estimateur de $\mathbf{a_0}$ qu'on sache calculer à partir des données disponibles on a :

$\mathbf{a_0}$ n'est identifiable à partir des $(y_i, \tilde{x_i})$ que si $\text{Cov}[\tilde{x_i}; u_i] = 0$.

### Approche alternative

On peut retrouver le problème lié à $\text{Cov}[\tilde{x_i}; u_i] \neq 0$ à partir de calculs simples.

Avec $E[u_i] \equiv 0$ et $y_i = \alpha_0 + b_0 \tilde{x_i} + u_i$, on a :

$$E[y_i] = \alpha_0 + b_0 E[\tilde{x_i}]$$

et donc :

$$\alpha_0 = E[y_i] - b_0 E[\tilde{x_i}]$$

Les termes $E[y_i]$ et $E[\tilde{x_i}]$ sont estimables, i.e. identifiables, puisque par la LGN on a :

$$\bar{y}_N \equiv \frac{1}{N} \sum_{i=1}^{N} y_i \xrightarrow{p}_{N \rightarrow +\infty} E[y_i]$$
et 
$$\bar{\tilde{x}}_N \equiv \frac{1}{N} \sum_{i=1}^{N} \tilde{x_i} \xrightarrow{p}_{N \rightarrow +\infty} E[\tilde{x_i}]$$

Donc $\alpha_0$ est identifiable si $b_0$ est identifiable.

Reste donc à savoir si on peut estimer $b_0$ à partir des données disponibles.

Dans le modèle :

$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

$b_0$ représente l'effet causal de $\tilde{x_i}$ vers $y_i$.

On sait estimer simplement la covariance entre $\tilde{x_i}$ et $y_i$ :

$$\frac{1}{N} \sum_{i=1}^{N} (\tilde{x_i} - \bar{\tilde{x}}_N)(y_i - \bar{y}_N) \xrightarrow{p}_{N \rightarrow +\infty} \text{Cov}[\tilde{x_i}; y_i]$$

Par application des propriétés des covariances on a :

$$\text{Cov}[\tilde{x_i}; y_i] = \text{Cov}[\tilde{x_i}; \alpha_0] + \text{Cov}[\tilde{x_i}; 1 \times \tilde{x_i}] + b_0 \text{Cov}[\tilde{x_i}; u_i]$$

c'est-à-dire :

$$\text{Cov}[\tilde{x_i}; y_i] = V[\tilde{x_i}] b_0 + \text{Cov}[\tilde{x_i}; u_i]$$

Une covariance mesure une corrélation, i.e. c'est un concept « symétrique », c'est une mesure (très) imparfaite d'une relation causale

L'équation $\text{Cov}[\tilde{x_i}; y_i] = V[\tilde{x_i}] b_0 + \text{Cov}[\tilde{x_i}; u_i]$ donne :

$$V[\tilde{x_i}]^{-1} \text{Cov}[\tilde{x_i}; y_i] = b_0 + V[\tilde{x_i}]^{-1} \text{Cov}[\tilde{x_i}; u_i]$$

Or on sait que :

$$\hat{b}_{MCO}^N = \frac{\sum_{i=1}^{N} (\tilde{x_i} - \bar{\tilde{x}}_N)(y_i - \bar{y}_N)}{\sum_{i=1}^{N} (\tilde{x_i} - \bar{\tilde{x}}_N)^2} \xrightarrow{p}_{N \rightarrow +\infty} V[\tilde{x_i}]^{-1} \text{Cov}[\tilde{x_i}; y_i]$$

ce qui donne ici :

$$\hat{b}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} b_0 + V[\tilde{x_i}]^{-1} \text{Cov}[\tilde{x_i}; u_i]$$

On pourrait éventuellement corriger le biais $V[\tilde{x_i}]^{-1} \text{Cov}[\tilde{x_i}; u_i]$ si on pouvait calculer un estimateur de $\text{Cov}[\tilde{x_i}; u_i]$ (on sait estimer $V[\tilde{x_i}]^{-1}$) mais :

**On ne peut estimer $\text{Cov}[\tilde{x_i}; u_i]$ puisque $u_i$ n'est pas observé**

### Résumé et définitions

Pour résumer. On vient de montrer que $\mathbf{a_0}$ n'est identifiable à partir des $(y_i, \tilde{x_i})$ que si $\text{Cov}[\tilde{x_i}; u_i] = 0$.

Ceci nous amène à introduire des définitions importantes :

**Définition.** Si $\text{Cov}[\tilde{x_i}; u_i] = 0$ alors $\tilde{x_i}$ est *exogène* dans le modèle (linéaire) considéré.

**Définition.** Le modèle :
$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

est un modèle de régression (linéaire simple) si $\text{Cov}[\tilde{x_i}; u_i] = 0$.

**Interprétation.** C'est un modèle dont « on a le droit d'estimer les paramètres par les méthodes de régression » (car ces méthodes reposent sur des estimateurs, MC, convergents dans ce cas).

**Définition.** Si $\text{Cov}[\tilde{x_i}; u_i] \neq 0$ alors $\tilde{x_i}$ est *endogène* dans le modèle considéré.

On a un problème d'identification si $\tilde{x_i}$ est endogène dans $y_i = \alpha_0 + b_0 \tilde{x_i} + u_i$.

L'endogénéité des variables explicatives un problème très fréquent en économétrie.

### Retour à l'exemple « BAC+5 »

La question de l'identification de l'effet « BAC+5 » se résume ici de la manière suivante : L'hypothèse $\text{Cov}[\tilde{x_i}; u_i] = 0$ est-elle valide ?

On a de bonnes raisons de penser que ce n'est pas le cas ici.

Le terme d'erreur $u_i$ est une variable inobservée, l'examen de cette question doit d'abord être « théorique ». Il s'agit d'examiner le contenu de $u_i$ et ses liens avec $\tilde{x_i}$, ce qui repose sur l'analyse du PGD de $(y_i, \tilde{x_i})$

Dans le modèle $y_i = \alpha_0 + b_0 \tilde{x_i} + u_i$ le terme d'erreur $u_i$ contient les effets de tout ce qui détermine $y_i$ et qui n'est pas représenté par $\alpha_0 + b_0 \tilde{x_i}$.

Ici $y_i = \text{salaire}_i$ et $\tilde{x_i} = \text{bac+5}_i$ :

- $u_i$ contient les effets de la chance (santé, opportunités, …), des aptitudes et des autres « caractéristiques » non mesurées … de i ($y_i$ résulte du choix de i et de son employeur, s'il en a)

et :

- $\tilde{x_i}$ dépend, en partie, des aptitudes (et des autres caractéristiques non mesurées) de i car $\tilde{x_i}$ résulte d'un choix ± contraint de i.

Si j est un individu avec « des aptitudes » au-delà de la moyenne alors :

- $u_j$ est relativement élevé

et :

- l'individu j est certainement un BAC+5, i.e. $P[\tilde{x_j} = 1]$ est élévée.

Selon toute vraisemblance, on a donc $\text{Cov}[\tilde{x_i}; u_i] > 0$ et dans :

$$\text{Cov}[\tilde{x_i}; y_i] = V[\tilde{x_i}] b_0 + \text{Cov}[\tilde{x_i}; u_i] > V[\tilde{x_i}] b_0$$

la quantité $\text{Cov}[\tilde{x_i}; u_i]$ ne peut être estimée, et donc $b_0$ ne peut être estimé à partir des données disponibles, $b_0$ n'est pas identifiable ici.

**Solutions.** Soit on abandonne, soit on améliore notre modèle de $y_i$ pour tenir compte de ce que $\text{Cov}[\tilde{x_i}; u_i] > 0$, i.e. on apporte de l'information supplémentaire à notre modèle, relative à $\text{Cov}[\tilde{x_i}; u_i]$.

En résumé, dans un modèle de la forme :

$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

tel que $\text{Cov}[\tilde{x_i}; u_i] \neq 0$ le paramètre $\mathbf{a_0} \equiv (\alpha_0, b_0)$ n'est pas identifiable.

Résoudre ce problème suppose un apport d'information permettant de gérer le fait que $\text{Cov}[\tilde{x_i}; u_i] \neq 0$ :

**Problème d'identification = Déficit d'information.**

C'est ce qu'on va apprendre à faire dans cette partie du cours.

Dans l'exemple « BAC+5 » le problème d'identification = endogénéité de $\tilde{x_i}$

C'est un problème très fréquent en économétrie.

Dans l'exemple considéré, l'endogénéité de $\tilde{x_i}$ est essentiellement liée à une variable explicative « omise », l'aptitude (pour les études et la « carrière »).

> **Remarque. Données expérimentales versus données « réelles »**
> 
> Pour évaluer l'effet d'un traitement en médecine, on fait un groupe de patients « placebo » ($\tilde{x_i} = 0$) et un groupe de patients « traités » ($\tilde{x_i} = 1$), puis on mesure et on compare leur état de santé $y_i$.
> 
> La répartition aléatoire des patients dans les groupes « placebo » et « traités » garantit que dans le modèle :
> $$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$
> on a :
> $$\text{Cov}[\tilde{x_i}; u_i] = 0$$
> 
> **Alternative :** On considère que les $\tilde{x_i}$ sont fixes et que seul $u_i$ est aléatoire.
> 
> Ce modèle est un modèle de régression dont on peut estimer les paramètres par les MCO, voire par simple comparaison de moyennes.
> 
> L'expérience a été construite pour ça : pour simplifier l'analyse des effets causaux.

> **Remarque. Modèle linéaire et effets hétérogènes**
> 
> Pour l'analyse statistique des effets de « BAC+5 », on a posé le modèle :
> $y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$
> 
> Ce modèle suppose en fait que l'effet de « BAC+5 » est homogène pour tous individus, il est mesuré par le paramètre « fixe » $b_0$.
> 
> En pratique, on pose plutôt le modèle suivant :
> $y_i = \alpha_i + b_i \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$
> 
> i.e., un modèles à paramètres aléatoires, $b_i$ et $\alpha_i \equiv \alpha_0 + u_i$.
> 
> L'analyse et l'estimation de tels modèles est l'objectif de la Partie C du cours.

## Equilibre proie-prédateur

On analyse ici un problème non économique, celui de la mesure du nombre de proies nécessaire à chaque prédateur dans un écosystème en l'équilibre.

**Objectif.** On veut estimer le nombre de proies nécessaire à la vie d'un prédateur dans un écosystème en équilibre. L'effet causal est que les proies permettent la survie des prédateurs par un effet « nourriture ».

**Les données.** Un échantillon ($i = 1,...,N$) d'écosystèmes, et on a mesuré pour chacun d'entre eux le nombre de proies ($\tilde{x_i}$) et de prédateurs ($y_i$).

Une manière simple de poser le problème consiste à poser le modèle :

$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$

et $\alpha_0 \simeq 0$ si les écosystèmes sont à l'équilibre « en moyenne ». Le nombre de proies nécessaires à chaque prédateur est $b_0^{-1}$ à l'équilibre.

Avec l'exemple précédent on a vu que $\mathbf{a_0} \equiv (\alpha_0, b_0)$ est identifiable à partir des $(y_i, \tilde{x_i})$ uniquement, si $\text{Cov}[\tilde{x_i}; u_i] = 0$ (c'est une condition nécessaire).

La condition $\text{Cov}[\tilde{x_i}; u_i] = 0$ est-elle une hypothèse valide ?

Il y a de fortes chances que non. Les nombres de proies et de prédateurs se déterminent « simultanément », l'écosystème cherchant toujours à retourner à l'équilibre par ajustement simultané des nombres de proies et prédateurs :

- le nombre de proies détermine le nombre de prédateur selon un effet « nourriture disponible » : $\tilde{x_i} \rightarrow y_i$

mais on a également :

- le nombre de prédateurs détermine le nombre de proies, selon un effet « élimination par la chasse » : $y_i \rightarrow \tilde{x_i}$.

Cette analyse du PGD des $(y_i, \tilde{x_i})$ montre que si $y_i$ est fonction de $\tilde{x_i}$, $\tilde{x_i}$ est également fonction de $y_i$, i.e $\tilde{x_i}$ et $y_i$ se déterminent « simultanément ».

Dans le modèle :

$$y_i = \alpha_0 + b_0 \tilde{x_i} + u_i \text{ avec } E[u_i] \equiv 0$$

$\tilde{x_i}$ étant fonction de $y_i$, elle est également fonction de $u_i$ avec ici :

$$\text{Cov}[\tilde{x_i}; u_i] < 0$$

un excès de prédateurs ($u_i$) diminuant le nombre de proies ($\tilde{x_i}$).

**Conclusion.** $\tilde{x_i}$ est endogène dans le modèle considéré, et $\mathbf{a_0} \equiv (\alpha_0, b_0)$ n'est pas identifiable à partir des seules données considérées.

On retrouve ce problème d'endogénéité, dit problème de simultanéité, en économétrie, par exemple pour l'analyse de fonctionnement de marchés dans lesquels les prix et les quantités échangées se déterminent conjointement, dans le cadre de l'équilibre de marché.

## Le problème de l'identification, covariances et paramètres

On considère ici le modèle linéaire sous sa forme générale :

$$y_i = \mathbf{x_i'} \mathbf{a_0} + u_i = \alpha_0 + \mathbf{\tilde{x_i'}} \mathbf{b_0} + u_i \text{ avec } E[u_i] \equiv 0$$

Si $\mathbf{b_0}$ est identifiable, i.e. peut être estimé à partir des données, alors la constante $\alpha_0$ est identifiable par :

$$\alpha_0 = E[y_i] - E[\mathbf{\tilde{x_i'}}] \mathbf{b_0}$$

Pour identifier $\mathbf{b_0}$ on ne sait estimer que des covariances.

Ici la covariance pertinente est :

$$\text{Cov}[y_i; \mathbf{\tilde{x_i}}] = \text{Cov}[\alpha_0; \mathbf{\tilde{x_i}}] + \text{Cov}[\mathbf{\tilde{x_i'}} \mathbf{b_0}; \mathbf{\tilde{x_i}}] + \text{Cov}[u_i; \mathbf{\tilde{x_i}}] = V[\mathbf{\tilde{x_i}}] \mathbf{b_0} + \text{Cov}[u_i; \mathbf{\tilde{x_i}}]$$

$$\text{Cov}[y_i; \mathbf{\tilde{x_i}}] = V[\mathbf{\tilde{x_i}}] \mathbf{a_0} + \text{Cov}[u_i; \mathbf{\tilde{x_i}}]$$

Deux cas sont à considérer :

1. **Toutes les variables explicatives du modèle sont exogènes**, i.e. on a :$$\text{Cov}[u_i; \mathbf{\tilde{x_i}}] = \mathbf{0}$$Alors $\mathbf{b_0}$, et donc $\mathbf{a_0} \equiv (\alpha_0, \mathbf{b_0})$, est identifiable (sous certaines conditions). L'estimateur des MCO de $\mathbf{b_0}$ est convergent.

2. **Certaines variables explicatives du modèle sont endogènes**, i.e. on a :	   $$\text{Cov}[u_i; \mathbf{\tilde{x_i}}] \neq \mathbf{0} \Leftrightarrow \text{Il existe } k \in \{2,...,K\} \text{ tel que } \text{Cov}[\tilde{x_{i,k}}; u_i] \neq 0$$Alors $\mathbf{b_0}$, et donc $\mathbf{a_0} \equiv (\alpha_0, \mathbf{b_0})$, n'est pas identifiable. L'estimateur des MCO de $\mathbf{a_0}$ n'est pas convergent en général.

A partir du chapitre 3 nous apprendrons à gérer le cas 2, ce qui suppose une bonne compréhension du cas 1 examiné en détail dans le chapitre suivant.

## Remarques importantes

On a utilisé des résultats/techniques fréquemment employés par la suite.

### Procédure 1. Estimation d'une espérance mathématique

Si on veut estimer l'espérance mathématique commune des matrices $\mathbf{W_i}$, $\mathbf{M_0} \equiv E[\mathbf{W_i}]$, à partir d'un (grand) échantillon d'observations de ces variables, il suffit d'utiliser la contre-partie empirique de $E[\mathbf{W_i}]$, i.e. la moyenne des $\mathbf{W_i}$, $\frac{1}{N} \sum_{i=1}^{N} \mathbf{W_i}$.

En effet, la LGN (sous certaines conditions de régularité) donne que :

$\mathbf{W_N} \equiv \frac{1}{N} \sum_{i=1}^{N} \mathbf{W_i} \xrightarrow{p}_{N \rightarrow +\infty} E[\mathbf{W_i}] = \mathbf{M_0}$

i.e. que $\mathbf{W_N} \equiv \frac{1}{N} \sum_{i=1}^{N} \mathbf{W_i}$ est un estimateur convergent de $\mathbf{M_0} \equiv E[\mathbf{W_i}]$.

### Procédure 2. Estimation de l'espérance mathématique d'une fonction paramétrée

Si on veut estimer l'espérance mathématique commune des $g(\mathbf{w_i}, \boldsymbol{\beta_0})$, $E[g(\mathbf{w_i}, \boldsymbol{\beta_0})]$, à partir d'un (grand) échantillon d'observations des $\mathbf{w_i}$ et d'un estimateur convergent de $\boldsymbol{\beta_0}$, $\hat{\boldsymbol{\beta_N}} \xrightarrow{p}_{N \rightarrow +\infty} \boldsymbol{\beta_0}$, il suffit d'utiliser la contre-partie empirique de $E[g(\mathbf{w_i}, \boldsymbol{\beta_0})]$, i.e. la moyenne des $g(\mathbf{w_i}, \boldsymbol{\beta_0})$ en remplaçant $\boldsymbol{\beta_0}$ par son estimateur convergent, $\hat{\boldsymbol{\beta_N}}$.

En effet, une variante de LGN, donne que (sous certaines conditions de régularité):

$\frac{1}{N} \sum_{i=1}^{N} g(\mathbf{w_i}, \hat{\boldsymbol{\beta_N}}) \xrightarrow{p}_{N \rightarrow +\infty} E[g(\mathbf{w_i}, \boldsymbol{\beta_0})]$

i.e. que $\frac{1}{N} \sum_{i=1}^{N} g(\mathbf{w_i}, \hat{\boldsymbol{\beta_N}})$ est un estimateur convergent de $E[g(\mathbf{w_i}, \boldsymbol{\beta_0})]$.

### Procédure 3. Estimation d'une fonction de paramètres estimables

On veut estimer $\mathbf{H_0} \equiv H(\mathbf{B_0}, \boldsymbol{\Gamma_0}^{-1})$ dont on sait que $H(\mathbf{B}, \mathbf{G})$ est une fonction continue en les éléments de $\mathbf{B}$ et $\mathbf{G}$ sur le domaine de définition des éléments de $\mathbf{B_0}$ et $\boldsymbol{\Gamma_0}^{-1}$.

Si on dispose d'un estimateur convergent de chacun des termes $\mathbf{B_0}$ et $\boldsymbol{\Gamma_0}$, $\hat{\mathbf{B_N}} \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{B_0}$ et $\hat{\boldsymbol{\Gamma_N}} \xrightarrow{p}_{N \rightarrow +\infty} \boldsymbol{\Gamma_0}$, alors les propriétés de la convergence en probabilité donne que :

$\hat{\mathbf{H_N}} \equiv H(\hat{\mathbf{B_N}}, \hat{\boldsymbol{\Gamma_N}}^{-1}) \xrightarrow{p}_{N \rightarrow +\infty} H(\mathbf{B_0}, \boldsymbol{\Gamma_0}^{-1}) \equiv \mathbf{H_0}$

sachant que l'estimateur $\hat{\mathbf{H_N}}$ existe avec une probabilité approchant 1.

Ce dernier résultat indique que $\hat{\boldsymbol{\Gamma_N}}$ peut ne pas être inversible, et donc $\hat{\mathbf{H_N}}$ peut ne pas exister, mais la probabilité que cela arrive devient nulle si $N \rightarrow +\infty$.

Ces techniques proviennent des résultats suivants, qui sont utilisés :

(i) pour analyser la convergence d'estimateurs

et :

(ii) pour construire des estimateurs (avec les techniques données ci-avant).

### Propriété 8. Loi (faible) des Grands Nombres d'une fonction paramétrée

Soient (i) $\{\mathbf{w_i} ; i = 1,2,...\}$ une suite de vecteurs aléatoires de $\mathbb{R}^W$ tels que les $\mathbf{w_i}$ sont iid pour $i = 1,2,...$ et (ii) $\boldsymbol{\beta_0}$ un vecteur de réels. On a (sous certaines conditions de régularité) :

$\frac{1}{N} \sum_{i=1}^{N} g(\mathbf{w_i}, \hat{\boldsymbol{\beta_N}}) \xrightarrow{p}_{N \rightarrow +\infty} E[g(\mathbf{w_i}, \boldsymbol{\beta_0})] \text{ si } \hat{\boldsymbol{\beta_N}} \xrightarrow{p}_{N \rightarrow +\infty} \boldsymbol{\beta_0}$

### Propriété 9. Inversion d'une suite de matrices convergeant en probabilité

Soit $\{\mathbf{M_N} ; N = 1,2,...\}$ une suite de matrices aléatoires telle que $\mathbf{M_N} \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{M_0}$ et $\mathbf{M_0}$ est inversible. On alors :

(i) la matrice $(\mathbf{M_N})^{-1}$ existe avec une probabilité approchant 1

et :

(ii) $(\mathbf{M_N})^{-1} \xrightarrow{p}_{N \rightarrow +\infty} (\mathbf{M_0})^{-1}$.

### Propriété 10. Transformation continue d'une suite convergeant en probabilité

Soient $\{\mathbf{w_N} ; N = 1,2,...\}$ une suite de vecteurs aléatoires et $H(\mathbf{w})$ une fonction continue en $\mathbf{w}$ sur le domaine des $\mathbf{w_N}$. On alors :

$\mathbf{w_N} \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{w_0} \Rightarrow H(\mathbf{w_N}) \xrightarrow{p}_{N \rightarrow +\infty} H(\mathbf{w_0})$