## 01 // test du $\chi^2$ (khi-deux)

## Le test

### Principes d’un test statistique

- Généralement, il existe deux principes pour créer une statistique pour le test d'hypothèses :
    - Elle mesure l’extrémité de notre résultat, $H_0$ étant vrai
    - Elle suit une distribution de probabilité connue.
    - Ces propriétés nous permettent de trouver une région critique bien définie pour rejeter l'hypothèse nulle.

### La distribution $\chi^2(n)$ et $H_0$

C'est un test statistique très important pour aider à déterminer si deux variables sont indépendantes ou non. Il prend comme statistique $\chi^2(n)$, qui est une somme des carrés de $n$ variables normales standard iid :

$$
\chi^2(n)=\sum_{i=1}^nX_i^2,\hspace{4pt}\text{où }X_i\sim\mathcal{N}(0,1)
$$

Maintenant, on doit fixer qu’est-ce  que notre $H_0$. La définition de $H_0$ change selon le test statistique lancé, et pour celui-ci, indique que **les deux variables son indépendantes**. C'est à dire, on commence ce test en pensant que les deux variables son indépendantes.

Pour rejeter $H_0$, on doit être capable de dire que la valeur de $\chi^2(n)$ obtenu correspond au $5\%$ extrême. C’est-à-dire, la probabilité d’observer la valeur de notre $\chi^2(n)$ est $5\%$ ou moins. Éventuellement, on pourra changer ce seuil à une autre valeur, comme $1\%$.

**Attention**. Le rejet de $H_0$ n’implique pas forcément une relation de causalité.

### Extra : **$V$ de Cramér**

Une fois on a notre valeur de $\chi^2(n)$, on pourrait l’utiliser pour créer un autre indicateur : la $V$ de Cramér. L'indicateur va de $0$ a $1$ et désigne le niveau de dépendance de deux variables.

$$
V=\sqrt{\frac{\chi^2(n)/n}{\min(k-1,r-1)}},\hspace{4pt}k \text{ nombre de colonnes et }r \text{ nombre de lignes}
$$

La p-value de la signification de $V$ est exactement la même calculée pour $\chi^2(n)$.

- Relation nulle ou très faible : inférieur a $0.10$
- Relation faible : entre $0.10$ et $0.20$
- Relation moyenne : entre $0.20$ et $0.30$
- Relation forte : au dessus de $0.30$
