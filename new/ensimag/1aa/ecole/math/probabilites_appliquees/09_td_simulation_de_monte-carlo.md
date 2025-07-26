# 09 // TD simulation de monte-carlo

Moyenne empirique : E(\bar(X)_n) = E(X_i) pour tout i.

Variance : Var(\bar{X}_n) = \frac{Var(X_i)}{n} ou aussi \frac{\sigma^2}{n}. La méthode de monte-carlo se repose sur le fait que la variance tends vers zero lorsque n grandit.

TCL : la variable z_n = \frac{\bar X_n - \mu}{\sigma / \sqrt{n}} a pour limite en loi lim_{n\to\infin} P(Z_n \le x) = \int_{-\infin}^{\infin} \frac{1}{\sqrt{2\pi}} \exp(-\frac{t^2}{2})) dt, qui est \mathcal N(0,1).

Vitesse de convergence : \bar{X}_n \to \mu quand n \to \infin à la même vitesse que \frac{\sigma}{\sqrt n} \to 0 quand n \to +\infin. L’ordre de convergence de \bar{X}_n \to \mu c’est de o(\frac{1}{\sqrt n}).

Intervalle de confiance : on a accès à un échantillon des (X_i). On ne connaît pas \mu = E(X_i) mais on connaît \sigma^2 = Var(X_i). On essaye de trouver [\bar{X}_n - a, \bar{X}_n + a] . Avec l’intervalle de confiance, pour des fin pratiques, on peut jouer sur la confiance qu’on choisit, ou la taille de l’échantillon.