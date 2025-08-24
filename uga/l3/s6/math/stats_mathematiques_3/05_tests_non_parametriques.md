## 05 // tests non paramétriques

[slides non param stat 3 annote.pdf](ressources/05_tests_non_parametriques_slides_non_param_stat_3_annote.pdf)

## Introduction

### Définition

Un test est dit non-paramétrique s'il peut être appliqué quelle que soit la distribution des observations. Puisque la distribution (normale ? exponentielle ? uniforme ? autre ?) n'est pas spécifiée, on n'a aucun paramètre à estimer. On ne fait **aucune hypothèse sur les distributions, on les considère continues et c’est tout !**

Il existe une multitude de méthodes et de tests non paramétriques, certains plutôt grossiers, d'autres beaucoup plus raffinés, qui permettent de tester plusieurs types d'hypothèses (équidistribution de deux échantillons, symétrie d'une distribution, indépendance, etc.) En voici quelques illustrations.

## Intervalles sur les quantiles

### Rappels

Rappelons la notion de quantile. Soit $X$ une variable aléatoire de type continu dont la densité est f$(x)$ et dont la fonction de répartition est $F(X)$. Soit $p$ une proportion strictement entre $0$ et $1$.

Supposons que $F(x) = p$ admette une unique solution en $x$. Cette solution est dite : "quantile d'ordre $p$". Cette racine (ou solution) est notée $\xi_p$. Ainsi,

$$
P(X \leq \xi_p) = F(\xi_p) = p
$$

### Encadrage binomiale

Pour commencer, si $X_1, \cdots, X_n$ sont des observations, on les ordonne par ordre croissant, comme $Y_1 ≤ Y_2 ≤ … ≤ Y_{n-1} ≤ Y_n$, où $Y_i = X_{(n)}$, cette dernière appelée la statistique d’ordre $n$.

Pour que la $i$-ème statistique d'ordre soit inférieure à $\xi_p$ il faut qu'il y ait au moins $i$ valeurs observées inférieures à $\xi_p$. De plus, pour que la $j$-ème statistique d'ordre soit supérieure à $\xi_p$, il faut qu'il y ait moins de $j$ valeurs inférieures à $\xi_p$.

Ainsi, si nous considérons qu'une valeur inférieure à $\xi_p$ est un succès, alors, parmi les $n$ essais indépendants, il doit y avoir entre $i$ et $j − 1$ succès pour que l'événement qui nous intéresse se réalise. Donc

$$
P(Y_i < \xi_p < Y_j) = \sum_{k=i}^{j-1} \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}
$$

### Exemple

On veut un intervalle de confiance pour le troisième quartile en observant un échantillon de taille $10$. On a

$$
P(Y_4 < \xi_{3/4} < Y_9) = \sum_{k=4}^{9-1} \frac{10!}{k!(10-k)!} \left(\frac{3}{4}\right)^k \left(\frac{1}{4}\right)^{n-k} \approx 0.9240
$$

Ainsi, en utilisant $Y_4$ et $Y_9$, on obtient un intervalle de confiance à $92.40\%.$

![image.png](ressources/05_tests_non_parametriques_image.png)

Un intervalle de confiance pour le 3e quartile est donc $]4.03; 14.73[$. Pour cet exemple, les auteurs ont échantillonné une population de loi E(5). On montre facilement que la valeur théorique de ce quartile est $Q_3 = 10\ln(2) = 6.93$

## Test d’équidistribution de deux échantillons

### Test du $χ²$… encore !

Nous avons beaucoup parlé du test du $\chi^2$ en début de semestre ainsi qu'en début de formation tant pour tester l'adéquation d'une série observée à une série théorique que pour tester l'indépendance (qui revient à comparer une loi jointe observée à une loi jointe produit des marges).

$$
\mathcal{D}\chi^2 = n \sum_{i,j} \frac{(f_{ij} - f_{i\cdot} f_{\cdot j})^2}{f_{i\cdot} f_{\cdot j}} \sim \mathcal{D}\chi^2(k - 1)
$$

Puisque dans ce cas la distribution de la variable observée n'est pas supposée connue, nous pouvons parler de test non paramétrique.

Dire que deux variables $X$ et $Y$ sont équidistribuées est équivalent à dire que la distribution d'une variable est indépendante du fait qu'il s'agisse d'un $X$ ou d'un $Y$.

En découpant l'intervalle $]−∞, +∞[$ en $k$ tronçons $I_1, I_2, \cdots I_k$, on peut dénombrer

$$
N_{1j} = \text{Card}\{i : X_i \in I_j\} = \text{"nombre de X dans } I_j\text{"}
$$

$$
N_{2j} = \text{Card}\{i : Y_i \in I_j\} = \text{"nombre de Y dans } I_j\text{"}
$$

On obtient donc un tableau $2×k$ et la suite se fait exactement comme s'il s'agissait d'un test d'indépendance.

![Example du tableau.](ressources/05_tests_non_parametriques_image_1.png)

Example du tableau.

### Le test de Wilcoxon

Ce test qui suit est l’équivalent de l’ANOVA non paramétrique pour un facteur à deux modalités. Pour plus de deux modalités, le test s’appelle Kruskall-Wallis.

Considérons deux échantillons $X_1, X_2, \cdots, X_{n_X}$ et $Y_1, Y_2, \cdots, Y_{n_Y}$. On veut tester l'hypothèse

$$
H_0 : F_X = F_Y
$$

#### Le tri

Pour appliquer le test de Wilcoxon, on ordonne (disons, de la plus petite à la plus grande) l'ensemble des $n = n_X + n_Y$ observations.

On obtient alors un mot formé de $n_X + n_Y$ lettres ($n_X$ fois la lettre $\text X$ et $n_Y$ fois la lettre $\text Y$).

**Exemple**. Si $X = (17.1, 14.5, 20.3, 8.3)$ et $Y = (5.2, 10.3, 12.4)$, on obtient le mot $\text{YXYXXXX}$ (la plus petite des $7$ observations est un $Y$, la deuxième est un $\text X$, …, les $3$ plus grandes sont des $\text X$).

#### La variable

La variable du test de Wilcoxon est

$$
W = \sum_{i=1}^{n_X} R_i
$$

où $R_i$ désigne le rang de l'observation $X_i$ parmi les $n = n_X + n_Y$ observations en ordre croissant.

$H_0$ sera rejetée si $W$ est significativement grand ou significativement petit. En vertu du Théorème Central Limit, si $n_X$ et $n_Y$ sont tous deux grands, la statistique convergera en densité à la loi normale suivante :

$$
W \overset{d}{\longrightarrow} \mathcal{N} \left( n_X \cdot \frac{n+1}{2}, \; \sqrt{ \frac{n_X n_Y (n+1)}{12} } \right)
$$

- Dérivation de la loi


    Soit $W$ une statistique de somme de rangs. Sous l'hypothèse nulle $\mathcal{H}_0$, on a $F_X = F_Y$et les rangs $R_i$ suivent une loi uniforme :

    $$
    R_i \sim \mathcal{U}([[ 1, n ]]), \quad \text{où } n = n_X + n_Y

$$

    
    Espérance et variance des rangs :
    
    $$
    \mathbb{E}[R_i] = \frac{n+1}{2}, \quad \text{Var}(R_i) = \frac{n^2 - 1}{12}
    
$$

    On a :
    
    $$
    \mathbb{E}[W] = \mathbb{E} \left[ \sum_{i=1}^{n_X} R_i \right] = \sum_{i=1}^{n_X} \mathbb{E}[R_i] = n_X \cdot \frac{n+1}{2}
    

$$
    
    Attention : les $R_i$ ne sont pas indépendants.
    
    La variance se calcule donc en tenant compte des covariances :
    
    $$
    \text{Var}(W) = \text{Var} \left( \sum_{i=1}^{n_X} R_i \right) = \sum_{i=1}^{n_X} \text{Var}(R_i) + \sum_{\substack{i,j=1 \\ i \ne j}}^{n_X} \text{Cov}(R_i, R_j)
    \\
    = n_X \cdot \frac{n^2 - 1}{12} + n_X(n_X - 1) \cdot C
    
$$

    où $C$ est une constante (covariance entre deux rangs distincts).
    
    Supposons qu’il n’y ait pas de $Y$, donc $n_X = n$ : tous les $X$ sont en tête, donc la variance est nulle :
    
    $$
    \frac{n(n^2 - 1)}{12} + n(n - 1) \cdot C = 0 \Rightarrow C = -\frac{n+1}{12}
    

$$
    
    On remplace $C$ dans la variance générale :
    
    $$
    \text{Var}(W) = n_X \cdot \frac{n^2 - 1}{12} + n_X(n_X - 1) \cdot \left( -\frac{n+1}{12} \right)
    
$$

    $$
    = \frac{n_X(n+1)}{12} \left[ n - 1 - (n_X - 1) \right] = \frac{n_X n_Y (n+1)}{12}
    

$$
    
    On a donc :
    
    $$
    W = \sum_{i=1}^{n_X} R_i, \quad \mathbb{E}[W] = n_X \cdot \frac{n+1}{2}, \quad \text{Var}(W) = \frac{n_X n_Y (n+1)}{12}
    
$$

    Si $n_X$ est grand, on applique le théorème central limite (version sans indépendance) :
    
    $$
    W \overset{d}{\longrightarrow} \mathcal{N} \left( n_X \cdot \frac{n+1}{2}, \; \sqrt{ \frac{n_X n_Y (n+1)}{12} } \right)
    

$$
    

### Conclusion du test

L'hypothèse $H_0$ sera donc rejetée au seuil α si

$$

\left|\frac{W - \frac{n_X(n+1)}{2}}{\sqrt{\frac{n_X n_Y (n+1)}{12}}}\right| > q_{\alpha/2}

$$

où $q_{\alpha/2}$ est le quantile théorique de la loi normale $\mathcal N(0;1)$ :

$$

P(N(0;1) > q_{\alpha/2}) = \frac{\alpha}{2}

$$

Remarque : Le test de Wilcoxon est excellent pour détecter les différences de position (médiane, moyenne). Pour détecter les différences de dispersion, il ne vaut pas grand chose.

Si, par exemple, on observe le mot $\text {XXXXXXXYYYYYYYYXXXXXXX}$, l'hypothèse d'équidistribution est évidemment fausse (tous les $\text Y$ sont au centre et les $\text X$ sont aux deux bouts) ; le test de Wilcoxon, pourtant, donnera une valeur de $W$ tout-à-fait compatible avec l'hypothèse d'équidistribution.

# Test de Spearman pour l’indépendance

## Motivation

Nous avons déjà été amenés à tester l'indépendance de deux variables avec le test du $\chi^2$, en particulier pour les couples de variables qualitatives. Ce test reste le plus usité.

On pourra également parler du test de Spearman basé sur la corrélation des rangs.

On pourrait considérer un test basé sur le coefficient de corrélation échantillonnal $r$ obtenu des n couples $(X_i, Y_i)$ d'un couple de variables $(X, Y)$.

On a pu observer que la nullité de ce coefficient de corrélation n'entraînait pas à coup sûr l'indépendance des variables. En effet, le coefficient de corrélation r est pleinement aveugle face aux relations non linéaires du type $Y = X^2$.

Le coefficient de corrélation de rangs (noté $R^*$) est celui qu'on obtient en remplaçant simplement les observations $X_i$ et $Y_i$ par leurs rangs $R_{X(i)}$ et $R_{Y(i)}$.

$R_{X(i)}$ est le rang obtenu par $X_i$ dans l'échantillon X ordonné ; de même, $R_{Y(i)}$ est le rang de $Y_i$ parmi les n valeurs de Y observées dans l'ordre.

L’idée est qu’**on ne fait plus la corrélation sur les observations de X et Y mais sur leurs rangs**.

## La variable

Le coefficient de corrélation de rangs est

$$

R^* = \text{corr}(R_X, R_Y)

$$

Et se calcule par la formule :

$$

R^* = \frac{ \frac{1}{n} \sum_{i=1}^n R_X(i) R_Y(i) - \left( \frac{1}{n} \sum_{i=1}^n R_X(i) \right) \left( \frac{1}{n} \sum_{i=1}^n R_Y(i) \right) }

{ \sqrt{ \left( \frac{1}{n} \sum_{i=1}^n R_X^2(i) - \left( \frac{1}{n} \sum_{i=1}^n R_X(i) \right)^2 \right)

\left( \frac{1}{n} \sum_{i=1}^n R_Y^2(i) - \left( \frac{1}{n} \sum_{i=1}^n R_Y(i) \right)^2 \right) } }

$$$$

= \frac{ n \sum_{i=1}^n R_X(i) R_Y(i) - \left( \sum_{i=1}^n R_X(i) \right) \left( \sum_{i=1}^n R_Y(i) \right) }
{ \sqrt{ \left( n \sum_{i=1}^n R_X^2(i) - \left( \sum_{i=1}^n R_X(i) \right)^2 \right)
\left( n \sum_{i=1}^n R_Y^2(i) - \left( \sum_{i=1}^n R_Y(i) \right)^2 \right) } }
$$
On remarque toutefois que puisque les $R_X(i)$ (et les $R_Y(i)$) ne sont qu’une permutation des entiers de $1$ à $n$, on a :
$$
\sum_{i=1}^n R_X(i) = \sum_{i=1}^n i = \frac{n(n+1)}{2}

$$$$

\sum_{i=1}^n R_X^2(i) = \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}

$$$$

n \sum_{i=1}^n R_X^2(i) - \left( \sum_{i=1}^n R_X(i) \right)^2
= \frac{n^2(n+1)(2n+1)}{6} - \frac{n^2(n+1)^2}{4}

$$$$

= n^2(n+1) \left( \frac{2n+1}{6} - \frac{n+1}{4} \right)

= \frac{n^2(n^2 - 1)}{12}

$$

Le coefficient de corrélation de rangs devient donc :

$$

R^* = \frac{ n \sum_{i=1}^n R_X(i) R_Y(i) - \frac{n^2(n+1)^2}{4} }

{ \frac{n^2(n^2 - 1)}{12} }

$$$$

= \frac{12 \sum_{i=1}^n R_X(i) R_Y(i)}{n(n^2 - 1)} - \frac{3(n+1)}{n-1}
$$
Posant $S^* = \sum_{i=1}^n R_X(i) R_Y(i)$, on observe que $R^*$ est fonction linéaire de $S^*$. Noter que :
$$
R^* = a S^* + b \quad \text{où} \quad
a = \frac{12}{n(n^2 - 1)} \quad \text{et} \quad b = -\frac{3(n+1)}{n-1}
$$
Il suffit donc de connaître la distribution de $S^*$ pour connaître celle de $R^*$. En fait, on a
$$
E[R^*|H_0] = aE[S^*|H_0] + b
$$
et
$$
\text{Var}[R^*|H_0] = a^2 \text{Var}[S^*|H_0]
$$
En cette fin de chapitre, on se passera du détail des calculs. Si $H_0$ est vraie, et si $n$ est grand, la statistique $S^*$ suivra approximativement (TCL) une loi normale
$$
N\left(\frac{n^2(n+1)^2}{4}; \sqrt{\frac{n^2(n+1)(n^2-1)}{144}}\right)
$$
On en déduit alors que $R^*$ suit une loi normale (bien plus jolie)
$$
N\left(0, \sqrt{\frac{1}{n-1}}\right)
$$
## Conclusion du test

L'hypothèse $H_0$ sera donc rejetée au seuil α si
$$
|R^*| > q_{\alpha/2} \sqrt{\frac{1}{n-1}}
$$
où $q_{\alpha/2}$ est le quantile théorique de la loi normale N(0;1) :
$$
P(N(0;1) > q_{\alpha/2}) = \frac{\alpha}{2}
$$
