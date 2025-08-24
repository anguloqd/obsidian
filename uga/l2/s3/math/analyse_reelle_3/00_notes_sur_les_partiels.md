## 00 // notes sur les partiels

## CC1

#1.2.b. : il arrive de voir $n$ comme un paramètre dans un intégrale de variable $t$. Le paramètre $n$ ne permet pas d’arriver à une forme fermée ou explicite. Donc, il serait bon de développer quelques cas de $n$ pour regarder le motif. **Il est utile de faire division longue, où D° dén. ≤ D° num., même s’ils sont égaux !**

$$
-\begin{align*}
I_n=\int_0^1 \frac{(t^2)^{n+1}}{1+t^2} \implies &I_0 = \left[t-\arctan(t)\right]^1_0 \space (*)\\
& I_1= \left[\frac{t^3}{3}-t+\arctan(t)\right]^1_0 \\
& I_2= \left[\frac{t^5}{5} - \frac{t^3}{3}+t-\arctan(t)\right]^1_0
\end{align*}
\\
\text{}
\\
I_n = (-1)^n
\left[
\left(
\sum_{k=0}^n (-1)^k\frac{t^{2k+1}}{2k+1}
\right) - \arctan(t)
\right]^1_0 = (-1)^n\left[S_n - \frac{\pi}{4}\right]
\\
\text{}
\\
\dots
\\
\text{}
\\
(*) \space I_0 = \int_0^1 \frac{t^2}{1+t^2}dt = \int_0^1\underbrace{1-\frac{1}{1+t^2}}_\text{division longue}dt
$$

Mais, en fait, dans ce cas, **IL FAUT RAPPELER QU’ON PEUT CHANGE L’ORDRE DE LA SOMME ET DE L’INTÉGRALE**.

$$
\sum_{k=0}^n \int_0^1 (-t^2)^k = \int_0^1 \sum_{k=0}^n (-t^2)^k=\int_0^1 \frac{1-(-t^2)^{n+1}}{1-(-t^2)}
$$

#1.2.c. : il peut être utile d’utiliser les intégrales passées pour des formes fermées légèrement changées.

#1.2.d., **théorème** : le produit de deux suites, $(a_n)$ et $(b_n)$, où $a_n \longrightarrow 0$ et $(b_n)$ bornée, tend vers $0$. Particulièrement utile quand $b_n = (-1)^n$ ou une fonction trigonométrique comme $b_n = \cos(n)$ qui est bornée.

#2 : apprendre dérivées et intégrales des fonctions trigo., particulièrement fonctions circulaires inverses.

### Post-correction

#2.3 : si on demande le domaine de convergence, **IL FAUT SAVOIR SI ON INCLUT LES BORNES**. Test individuel de -R et R dans le D.L.

#3.1 : pour justifier la continuité, on peut noter qu’une fonction est un **quotient de deux fonction continues**. Aussi, pour un point individuel d’une fonction, on utilise la définition de continuité f$(x_0)=\lim_{x\rightarrow x_0} f(x)$.

#3.2 : si on demande de calculer dérivées partielles d’un fonction sur un point, on doit le faire avec la définition de limite !

$$
\frac{\partial f(x,0)}{\partial x}=\lim_{x\rightarrow 0}\frac{f(x,0)-f(0,0)}{x-0}. \text{ Analogiquement pour } y.

\\
\text{}
\\

\frac{\partial f}{\partial x}=
\begin{cases}
\text{qqch., si } x \ne0 \\
\frac{f(x,0)-f(0,0)}{x-0}, \text{ si } x=0
\end{cases}
$$

#3.3 : une question si $f(x)$ est de clase $\mathcal{C}^1$ signifie qu’on doit savoir si les dérivés partielles de cette fonctions sont continues, particulièrement s’il y a des points individuellement définis (fonction par branches). Très pareil à démontrer continuité, mais avec les dérivés partielles.

## CC2

### Tip à part…

Pour les changements d’indice dans les sommes, si on applique une transformation à $k$ qui arrive jusqu’à $n$ sur le symbole $\Sigma$, on applique la transformation contraire à $k$ sur l’expression.

$$
\sum_{k=0}^nx^k = \sum_{k=1}^{n+1}x^{k-1}
$$

Similairement, si notre $n$ (dernier terme de la somme) est un peu différent sur $\Sigma$, on peu changer la variable qui la représente.

$$
\text{On sait :} \sum_{k=0}^n x^k=\frac{1-x^{n+1}}{1-x}. \text{ Donc, } \overbrace{\sum_{k=0}^{n-1}}^{\text{Soit }m=n-1}x^k = \sum_{k=0}^mx^k
\\
\text{}
\\
\text{Finalement, } \sum_{k=0}^mx^k=\frac{1-x^{m+1}}{1-x}=\frac{1-x^{(n-1)+1}}{1-x} = \frac{1-x^n}{1-x}
$$
