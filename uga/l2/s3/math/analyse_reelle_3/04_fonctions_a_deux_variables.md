## 04 // fonctions à deux variables

## Points critiques, extrêmes locaux et globaux

### Points critiques : $\frac{\partial f}{\partial x}=0$

Un point critique par rapport à une variable $x$ pour une fonction à deux variables $f(x,y)$ est l’ensemble de points $(x,y)$ tel que $\frac{\partial f}{\partial x} = 0$, et de même pour $y$.

Notons que la expression qui en résulte peut dépendre des deux variables, d’une des deux, ou d’aucune.

### Discriminant $\Delta f(x,y)$ et extrêmes locaux

Le discriminant d’une fonction $f(x,y)$ est l’expression suivante :

$$\Delta f(x,y)=\left[\frac{\partial^2 f}{\partial x \partial y}\right]^2-\frac{\partial^2 f}{\partial x^2}\frac{\partial^2 f}{\partial y^2}=s^2-rt$$

Si $(a,b)$ est un point critique :

- Si $[\Delta f]_{(a,b)} > 0 \iff (a,b)$ est un point selle pour $f$.
- Si $[\Delta f]_{(a,b)} < 0$ et…
    - $[r]_{(a,b)} \text{ ou } [t]_{(a,b)} > 0 \iff (a,b)$ est minimum locale de $f$.
    - $[r]_{(a,b)} \text{ ou } [t]_{(a,b)} < 0 \iff (a,b)$ est maximum locale de $f$.
    - $[r]_{(a,b)} \text{ ou } [t]_{(a,b)} = 0 \iff$on ne peut rien en conclure.
- Si $[\Delta f]_{(a,b)} = 0$, on ne peut rien conclure.

### Extrêmes globaux

Si on peut démontrer que pour une valeur concrète de $y=y_0$, la fonction $f(x,y)$ diverge vers l’infini positif ou négatif, cela suffit pour dire que $f(x,y)$ n’as pas de maximum ou minimum global, respectivement. C’est de même pour $y$ qui est la variable qui bouge et $x=x_0$ la variable qui reste fixe.

## Continuité et dérivabilité partielle

### Définition de continuité pour une fonction bivariable

$$\begin{align}
f \text{ continue en } (x_0,y_0) &:\lim_{x \rightarrow x_0, y \rightarrow y_0}f(x,y)=f(x_0,y_0) \\
\text{Pour un point de la forme } (c_0,c_0) &:\lim_{x \rightarrow c_0} f(x,x)=f(c_0,c_0)
\end{align}$$

### Définition de dérivabilité pour un fonction bivariable

$$\begin{align*}
&f \text{ dérivable p.r. à }x \text{ en } (x_0,y_0) : \text{(analogiquement pour } y) \\
&\frac{\partial f}{\partial x}(x_0,y_0)= \lim_{x \rightarrow x_0}\frac{f(x,y_0)-f(x_0,y_0)}{x-x_0} \text{ existe,} \\
&\text{et dérivé continue en } (x_0,y_0) \text{ si :} \\
&\lim_{x \rightarrow x_0} \frac{\partial f}{\partial x}(x,y_0)=\frac{\partial f}{\partial x}(x_0,y_0)
\end{align*}$$

**Note #1** : “dérivable” ici signifie que $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$ existent et ont une valeur concrète (non-infinie), respectivement.

**Note #2** : une fonction bivariable $f(x,y)$ peut ne pas être continue et quand même avoir des dérivées partielles. Ceci est différent dans le cas d’une fonction univariable $f(x)$.

## Intégration double sur un intervalle non-rectangulaire

### Régions de type I et type II

Une région dans le plan cartésien est de type I s’il existe deux fonctions tel que la région est contenue verticalement entre les deux. C’est similaire pour les régions de type II, mais ici la région est contenue horizontalement.

$$\begin{align*}
&\text{Type I : } D=\{(x,y) : a≤x≤b, g_1(x)≤y≤g_2(x)\} \\
&\text{Type II : } D=\{(x,y) : c≤y≤d, h_1(y)≤x≤h_2(y)\}
\end{align*}$$

![Régions de type i.](ressources/04_fonctions_a_deux_variables_untitled.png)

Régions de type I.

![Régions de type ii.](ressources/04_fonctions_a_deux_variables_untitled_1.png)

Régions de type II.

### Théorème de Fubini

Pour une fonction $f(x,y)$ continue sur la région $D$, on a que :

$$\begin{align*}
&\text{Type I : } \iint_D f(x,y) \, dy \, dx = \int_a^b \left[\int_{g_1(x)}^{g_2(x)} f(x,y) \, dy\right] dx \\
&\text{Type II : } \iint_D f(x,y) \, dy \, dx = \int_c^d \left[\int_{h_1(y)}^{h_2(y)} f(x,y) \, dx\right] dy
\end{align*}$$

[Double Integrals Over General Regions](https://math.libretexts.org/Courses/Montana_State_University/M273%3A_Multivariable_Calculus/15%3A_Multiple_Integration/Double_Integrals_Over_General_Regions)
