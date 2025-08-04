# 05 // thm. de De Moivre-Laplace

# Théorème de De Moivre-Laplace

## Le théorème : une approximation d’une loi binomiale

$$
Z_n = \frac{X_n - np}{\sqrt{np(1-p)}} = \frac{X_n - \mu}{\sigma} \implies \left(\lim_{n\rightarrow\infty} Z_n\right)\sim\mathcal N(0,1)
$$

Si $X_n$ est une V.A. de ordre $n$ suivant une loi binomiale, donc $Z_n$ serait une V.A. normale de moyenne $0$ et variance $1$. On doit respecter, par contre, quelques conditions :

- $np \ge 10$.
- $n(1-p) \ge 10$.

**Attention**. $X$ n'est pas la probabilité, mais le résultat de la variable aléatoire ! Après de calculer $Z_n$, tu doit utiliser un table $Z$ pour savoir à quelle probabilité correspond ton $Z$.

On utilise souvent cette théorème quand on veut trouver, dans le contexte de loi binomiale, une probabilité de $\mathbb P (k_\text{min}\le X_\mathcal{B}\le k_\text{max})$, càd. la probabilité d’observer un nombre de succès $X_\mathcal{B}$ dans l’intervalle $[k_\text{inf}, k_\text{sup}]$, mais $n$ est trop grand. Avec cette approximation, trouver telle probabilité revient à ce qui suit :

$$
\mathbb P (k_\text{inf}\le X_\mathcal{B}\le k_\text{sup}) \approx \int_{z_\text{inf}}^{z_\text{sup}} \mathcal N(0,1)dz,\text{ où } z_\text{inf/sup}=\frac{k_\text{inf/sup}-\mu}{\sigma}
$$

## La table $Z$ : trouver l’aire sous la courbe de $\mathcal N(0,1)$

![](https://i.pinimg.com/736x/48/17/ef/4817ef9d245f015924effa926a985e46--normal-distribution-statistics.jpg)