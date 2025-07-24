# 01 // tests de $\chi^2$

Date de création: March 9, 2024 10:39 PM
Modifié: April 19, 2025 2:09 PM

[slides chi2 stat 3 annote.pdf](slides_chi2_stat_3_annote.pdf)

# Tests du $χ²$

## Test du $χ²$ pour l’*indépendance* entre deux variables

Dans cette section, on s'intéresse aux relations entre deux variables notées $X$ et $Y$. Supposons que l'on observe ces deux variables sur $n$ unités statistiques. A chaque individu $i$, on peut associer un couple d'observations $(x_i; y_i)$. Chaque variable peut-être quantitative ou qualitative.

Les données peuvent être représentées dans un tableau à double entrée appelé **tableau de contingence**.

Notons $m_{X_1}, ..., m_{X_J}$ les $J$ modalités de $X$, et $m_{Y_1}, ..., m_{Y_K}$ les $K$ modalités de $Y$.

Introduisons les quantités suivantes :

- $n_{jk}$ est le nombre de fois où le couple $(X, Y)$ prend la modalité $(m_{X_j}, m_{Y_k})$
- $n_{•k}$ est le nombre de fois où la variable $Y$ prend la valeur $m_{Y_k}$
- $n_{j•}$ est le nombre de fois où la variable $X$ prend la valeur $m_{X_j}$

### Distributions marginales

A partir du tableau de contingence, on peut retrouver la distribution de chacune des variables séparément.

![image.png](new/uga/l3/s6/math/S6%20math%20stats%20mathématiques%203/01%20tests%20de%20$%20chi^2$/image.png)

Les distributions de $X$ et de $Y$ sont appelées distributions marginales. Sur chaque variable, on peut calculer les indicateurs habituels (moyenne, variance, écart type si la variable est quantitative...). Ces paramètres sont qualifiés d’indicateurs marginaux.

### Statistique du χ²

En présence de deux variables, l'un des enjeux principaux est d'étudier (c'est à dire quantifier voire expliquer) la dépendance entre les deux caractères.

Si on était dans le cadre des probabilités, ce qui n'est pas le cas, alors deux caractères sont indépendants si la valeur de l'un n'a aucune influence sur la distribution de l'autre. Si tel était le cas, alors les distributions conditionnelles :

$$
f_{j|k} = \frac{f_{jk}}{f_{\bullet k}} \text{ et } f_{k|j} = \frac{f_{jk}}{f_{j\bullet}}
$$

seraient toutes semblables à la distribution marginale. Pour tout $(j, k)$, on devrait avoir :

$$
f_{j|k} = f_{j\bullet} \text{ et } f_{k|j} = f_{\bullet k}
$$

Ainsi, on aurait :

$$
f_{kj} = f_{j|k}f_{\bullet k} = f_{j\bullet}f_{\bullet k}
$$

D'où, si les deux variables étaient indépendantes, on aurait :

$$
n_{jk} = \frac{n_{j\bullet}n_{\bullet k}}{n}
$$

En statistiques, on ne peut que "quantifier la distance à l'indépendance" à travers **la statistique du $χ²$**, notée comme suit :

$$
D_{\chi^2} = n\sum_{j=1}^J\sum_{k=1}^K\frac{(f_{jk} - f_{j\bullet}f_{\bullet k})^2}{f_{j\bullet}f_{\bullet k}}
$$

On peut remarquer que :

$$
D_{\chi^2} = n\left(\sum_{j=1}^J\sum_{k=1}^K\frac{n_{jk}^2}{n_{j\bullet}n_{\bullet k}} - 1\right)
$$

ou de façon équivalente :

$$
D_{\chi^2} = \sum_{j=1}^J\sum_{k=1}^K\frac{\left(n_{jk} - \frac{n_{j\bullet}n_{\bullet k}}{n}\right)^2}{\frac{n_{j\bullet}n_{\bullet k}}{n}}
$$

où $J$ et $K$ sont le nombre de modalités de chacune des deux variables considérées. Le cas d'indépendance probabiliste serait alors équivalent à $D_{\chi^2} = 0$.

**Théorème.** La variable du test $D_{χ²}$ suit une loi du $χ²$ à $(K-1)(L-1)$ degrés de liberté.

### Interprétation

Au seuil $α\%$ (le plus souvent $α = 5\%$), il faut comparer $D_{χ²}$ au quantile d'ordre $1-α\%$ ($q_{0,95}$ le plus souvent) d'une loi du $χ²(d)$, où:

$$
d = (J-1)(K-1)
$$

L'interprétation est la suivante :

- si $D_χ² ≥ q_{1-α}$, on conclut que les deux variables sont dépendantes
- sinon, on conclut qu'elles sont indépendantes

## Test du $χ²$ pour l'*ajustement* d'une série à une loi de probabilité

<aside>
❗

Ce test est plutôt directement expliqué avec un exemple.

</aside>

<aside>
⚠️

Note pratique : On évite d'utiliser le test du $χ²$ si un effectif du tableau est inférieur ou égal à $5$ à cause de l'approximation avec le Théorème Central Limite.

</aside>

On considère une série de 500 sacs de ciment avec leurs poids. On souhaite tester si cette série suit une loi normale $(m, σ)$ avec :

$$
m ≈ 50.78, σ ≈ 3.74
$$

### Hypothèse nulle

On pose $H_0$ comme "La série observée est distribuée selon une loi normale $\mathcal N(50.78, 3.74)$"

### Variable du test

La statistique du test est :

$$
D_{χ^2} = \sum_{i=1}^l\frac{(O_i - T_i)^2}{T_i}
$$

où $O_i$ sont les effectifs observés et $T_i$ les effectifs théoriques.

**Théorème**. La variable du test $D_{χ²}$ suit une loi du $χ²$ à $(l-s-1)$ degrés de liberté, où $l$ est le nombre de modalités observées, $s$ est le nombre de paramètres estimés.

### Interprétation

Au seuil $α\%$, on compare $D_χ²$ au quantile $q_{1-α}$ de la loi du $χ²(d)$ :

- si $D_{χ²} ≥ q_{1-α}$, on conclut que les deux distributions ne peuvent pas être identiques
- sinon, on ne rejette pas cette hypothèse

### Application

Dans l'exemple des sacs de ciment :

- La loi du $χ²$ à $5$ degrés de liberté
- $D_{χ²} = 3.76$
- $q_{0.95} = 11.07$
- Puisque $D_{χ²} ≤ q_{0.95}$, on ne rejette pas l'adéquation des lois