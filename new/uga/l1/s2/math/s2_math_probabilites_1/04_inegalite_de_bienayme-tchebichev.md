# 04 // inégalité de bienaymé-tchebichev

# Inégalité de Bienaymé-Tchebichev

## L’inégalité : une borne supérieure utile sur une V.A $X$

$$
P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}
$$

L’interprétation est que la probabilité que la valeur de $X$ soit à $k$ écart-types ou plus de la moyenne $\mu$ est plus petit que $\frac 1 {k^2}$. C’est un théorème assez générale, utile parce qu’il y a peu de conditions sur la loi de $X$, mais pas trop utile parce la borne supérieure $\frac 1 {k^2}$ est assez grande comme borne.

- $X$ prend de valeurs dans tout $\R$.
- La moyenne $μ$ est finie.
- La variance $σ$ est différent de zéro.
- Cette inégalité est seulement utile quand $k > 1$.

## Le raisonnement

La probabilité que la valeur de $X$ soit éloignée de la moyenne $\mu$ devient de plus en plus petit.

Pensons à une loi normale sur $X$ (mais ça applique aussi avec d'autres distributions !). La probabilité que $X$ soit à $2σ$ ou plus de la moyenne est petite, et à $3σ$ encore plus petite.

Graphiquement, le plus éloigné de la moyenne $\mu$ on est, le plus petit la queue de la distribution devient (à droite et gauche).

**Attention**. la formulation originale nous parle de la **QUEUE** de la distribution (à droite et gauche) et non pas du **CENTRE** !