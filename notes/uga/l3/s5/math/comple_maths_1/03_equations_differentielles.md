# 03 // équations différentielles

[Slides - Équations différentielles](ressources/03_equations_differentielles_slides_eq_diff_annote_3.pdf)

# Problème de Cauchy

## Définitions et exemple

On appelle problème de Cauchy au problème suivant :

$$
\begin{cases}
x^\prime(t)=f(t,x(t))
\\
x(t_0)=x_0\in\mathbb{R}
\end{cases}
$$

La condition $x(t_0) = x_0$ est dite “donnée de Cauchy” ou “condition initiale”. 

**Théorème #1 : Cauchy-Lipschitz**. Dans le problème de Cauchy précédent, si la fonction $f$ est continue et localement lipschitzienne par rapport a la deuxième variable $\big(x(t)\big)$, il existe une et une seule solution maximale au problème de Cauchy. Son intervalle de définition est ouvert.

**Définition #1**. On appelle champs de directions ou champs de tangentes de l’équation $x^\prime(t) = f(t, x(t))$ l’ensemble des vecteurs de pente $f(t, x(t))$ dans le plan $(t, x)$. Ces vecteurs sont tangents aux trajectoires des solutions de l’´equation.

**Exemple #1**.
$$
\begin{cases}
x^\prime(t)=t
\\
x(0)=0
\end{cases}
$$

![untitled](ressources/03_equations_differentielles_untitled.png)

Dans l’image précédente, juste avec la proposition $x^\prime(t)=f(t,x(t))$ et sans besoin de la condition initiale, on peut tracer le champ de directions. En intégrant, on dérive que $x(t)=t/2+C$. On pourra tracer des lignes tangentes de $x(t)$ en faisant varier le $C$. C’est finalement avec la condition initiale qu’on déduit que $C=0$.

**Définition #2**. L’isocline de pente $c$ est un ensemble de tous les points sur le champ de directions pour lesquelles la pente vaut $c$. C’est-à-dire, $f(t,x(t))=c$.

**Définition #3**. Les solutions sur l’isocline zéro sont dites *stationnaires*.

# Équation différentielle de premier ordre

[Variation of parameters](https://en.wikipedia.org/wiki/Variation_of_parameters)

## Présentation et stratégie de résolution

Considérons l’équation linéaire du premier ordre :

$$
y^\prime+a(t)y(t)=f(t)
$$

où $a$ et $f$ sont des fonctions continues sur un intervalle. Notons qu’on peut transformer une telle équation dans un problème de Cauchy (sans condition initiale), supposant que $g$ loc. lpz. sur la deuxième variable :

$$
\begin{align*}
&&y^\prime+a(t)y(t)=f(t)
\\
&\implies&y^\prime=f(t)-a(t)y(t)
\\
&\implies&y^\prime=g(t,y(t))
\end{align*}
$$

Notons donc que, du fait que on peut réécrire $y^\prime$ de telle manière, une unique solution est garantie pour toute condition initiale.

La stratégie de résolution d’une équation différentielle comme telle est de :

1. Déterminer **toutes** les solutions de l’équation homogène $y^\prime+a(t)y(t)=0$. Ceci est equivalent à
   $$y^\prime+a(t)y(t)=0 \iff y^\prime_0=-a(t)y_0(t)$$
2. Trouver **une** solution de l’équation complète $y^\prime+a(t)y(t)=f(t)$. Ceci est réécrit aussi comme     
	$$y^\prime+a(t)y(t)=f(t) \iff y^\prime_*=f(t)-a(t)y_*(t)$$
    
3. La solution générale sera $y=y_0+y_*$. Si on dérive les deux membres de cette dernière équation, on devrait trouver l’équation du départ.   
   $$
    \begin{align*}
    y^\prime & =y_0^\prime+y_*^\prime \\
    & =-a(t) y_0(t)+f(t)-a(t) y_0(t) \\
    & =-a(t)\left(y_0(t)+y_0(t)\right)+f(t) \\
    & =-a(t) y(t)+f(t) \\
    \end{align*}
    \\[6pt]
    y^{\prime}+a(t) y(t) =f(t)
    $$

## Résolution de l’équation homogène

Si $a$ est continue sur $I$ et admet des primitives, et $t_0\in ]\alpha, \beta[$, le théorème de dérivation des fonction composées montre que 

$$
\begin{align*}
y_0(t)&=\exp\left(-\int_{t_0}^ta(s)ds\right)
\\&=\exp(-A(t)+A(t_0))
\\&=\exp(-A(t))\times\exp(A(t_0))
\\&=C\exp(-A(t))
\end{align*}
$$

Notons que ce $C$ aura une valeur différente pour chaque valeur initiale $t_0$.

## Résolution de l’équation particulière

Ici, il suffit de trouve une solution à l’équation dite “particulière”. Pour ce faire, on peut utiliser la méthode de variation de la constante, aussi appelée méthode de Lagrange. On cherche une solution de la forme 

$$
\begin{align*}
y_*(t)&=C(t)\exp\left(-\int_{t_0}^ta(s)ds\right)
\end{align*}
$$

La solution est donc :

$$
y_*(t)=C(t)\exp\left(-A(t)\right)
$$

Il ne nous resterait que dériver $y_*(t)$ et résoudre l’équation particulière pour trouver la fonction $C(t)$.

## Exemple

Cherchons les solutions de l’équation suivante :

$$
y^\prime+2y=t^2+3t
$$

On commence par la solution de l’équation homogène : $y_0 = Ce^{-2t}$. On fait de même pour la solution particulière de l’équation particulière : $y_* = C(t)e^{-2t}$. Ayant ce dernier, on dérive $y_*$ :
$$
\begin{align*}
y_*^{\prime}(t) & =C^{\prime}(t) e^{-2 t}-2 C(t) e^{-2 t} \\
& =e^{-2 t}\left(C^{\prime}(t)-2 C(t)\right)
\end{align*}

$$$$
\text{On revient à l'équation : } y_*^{\prime}+2 y=t^2-3 t

$$$$

\begin{align*}

e^{-2 t}\left(C^{\prime}(t)-2 C(t)\right)+2 C(t) e^{-2 t} 
&=t^2-3 t
\\
e^{-2 t}\left(C^{\prime}(t)\cancel{-2C( t)+2 C(t)}\right) &= t^2-3 t
\\
e^{-2 t} C^{\prime}(t) & =t^2-3 t \\
C^{\prime}(t) & =\left(t^2-3 t\right) e^{2 t}
\end{align*}

$$$$

C(t)=\int\left(t^2-3 t\right) e^{2 t} d t=\frac{e^{2t}}{2}(t^2-4t+2)
$$

Ayant calculé $C(t)$, on peut finalement déduire $y_*$ :

$$
\begin{align*}
y_* &= C(t)e^{-2t}
\\ &= \left(\frac{e^{2t}}{2}(t^2-4t+2)\right)e^{-2t}
\\ &= \frac 1 2 (t^2-4t+2)
\end{align*}
$$

Et finalement, on peut calculer $y$ :

$$
\begin{align*}
y(t)&=y_0(t)+y_*(t)
\\ &= Ce^{-2t}+\frac 1 2 (t^2-4t+2)
\end{align*}
$$

# Équation différentielle de second ordre

## Présentation et stratégie de résolution

On parle particulièrement des équations différentielles **linéaires** de second ordre. Ici, $a$ et $b$ sont des constantes :

$$
y^{\prime\prime}+ay^\prime+by=c(t)
$$

La stratégie est assez similaire à celle du cas de premier ordre. On veut résoudre une équation homogène $E_0$, puis une équation particulière $E_*$, et la solution final sera la somme des deux : $y = y_0+y_*$. **La fonction $c(x)$ sera discutée dans la solution particulière**.

## Résolution de l’équation homogène

On résout cette équation par la méthode des [equations caractéristiques](https://en.wikipedia.org/wiki/Characteristic_equation_(calculus)). On commence par monter l’équation homogène :

$$
E_0 :y^{\prime\prime}_0+ay^\prime_0+by_0 = 0
$$

Particulièrement, dans le cas des EDO2 linéaires, toute équation différentielle homogène a une équation caractéristique correspondante :

$$
E_0:y^{\prime\prime}_0+ay^\prime_0+by_0 = 0 \longleftrightarrow E_\mathcal C:x^2+ax+b=0
$$

On devra trouver les racines de l’équation caractéristique, soit $\alpha_1$ et $\alpha_2$. Il n’est pas un problème si les racines sont complexes propres. On peut trouver deux cas des racines qui détermineront la forme de la solution de $y_0$ :

- Racines différentes ($\alpha_1 \ne \alpha_2$) : $y_0$ est de la forme $C_1e^{\alpha_1 x}+C_2e^{\alpha_2 x}$
- Racine double ($\alpha_1 = \alpha_2 = \alpha$) : $y_0$ est de la forme $(Ax+B)e^{\alpha x}$

## Résolution de l’équation particulière

La solution générale sera expliquée après, mais il faut dire qu’elle est très peu usitée. Dans la pratique, on suppose que $c(t) = P(t)e^{\beta t}$, où $P(t)$ un polynôme de degré $n$. Si ceci est le cas, donc la solution particulière est de la forme $y_*=Q(t)e^{\beta t}$.

- $d°(Q(t)) = d°(P(t)) = n$
Le cas si $\beta$—le coefficient de $x$ dans $e^{\beta x}$— n’est pas racine de $E_\mathcal C$
- $d°(Q(t)) = d°(P(t)) + 1 = n+1$
Le cas si $\beta$—le coefficient de $x$ dans $e^{\beta x}$— est racine simple de $E_\mathcal C$
- $d°(Q(t)) = d°(P(t)) + 2 = n+2$
Le cas si $\beta$—le coefficient de $x$ dans $e^{\beta x}$— est racine double de $E_\mathcal C$

On écrire $Q(t)$ dans sa forme plus générale selon son degré, comme $ax^2+bx+c$, $ax+b$, $a$, etc.

> [!note]
> Si le second membre $c(x)$ est une fonction trigonométrique, on essaie les $a\sin(x)+b\cos(x)$.

Une fois on connaît $y_*$, on dérive deux fois pour obtenir $y_*^\prime$ et $y_*^{\prime\prime}$, puis on injecte dans l’équation originale pour déduire les valeurs des constantes dans la formulation générale de $y_*$.

Finalement, la solution finale est la somme de la solution homogène et particulière : $y = y_0 + y_*$.

## Exemple

Considérons l'équation différentielle suivante :

$$
y'' - 3y' + 2y = e^x
$$

L'équation homogène et son équation caractéristique associée est donnée par :

$$
E_0 : y'' - 3y' + 2y = 0 \longleftrightarrow E_\mathcal C :x^2 - 3x + 2 = 0
$$

Les racines de cette équation caractéristique sont $1$ et $2$. La solution homogène correspondante est alors :

$$
y_0(x) = C_1e^{\alpha_1 x} + C_2e^{\alpha_2 x}, \text{ où } \alpha_1 = 1 \text{ et } \alpha_2 = 2
$$

Côte particulière, notons que $c(x) = P(x)e^{\beta x}=e^x$ d’où $P(x)=1$ et $\beta=1$. Notons que tel $\beta$ est solution de l’équation caractéristique $E_\mathcal C : x^2-3x+2 = 0$.

Grâce à ce dernier, la solution particulière est donc de la forme $Q(x)e^x$ avec $d°(Q(x)) = 0+1=1$. C’est à dire, la solution particulière est donc $y_*=(ax + b)e^x$, où :
$$
\begin{align*}
y'(x) &= (a + ax + b)e^x = (ax + a + b)e^x, \\
y''(x) &= (a + ax + a + b)e^x = (ax + 2a + b)e^x.
\end{align*}
$$

En injectant cette solution dans l'équation différentielle, nous obtenons :

$$
\begin{align*}
&(ax + 2a + b)e^x - 3(ax + a + b)e^x + 2(ax + b)e^x = e^x \\
&\implies 2a + b - 3a - 3b + 2b = 1 \\
&\implies -a = 1 \\
&\implies a = -1.
\end{align*}
$$

Notons que, quand on veut résoudre pour $a$, on n’a pas de condition sur $b$. La valeur de $a$ est $-1$ peu importe la valeur de $b$. Pour nous simplifier la vie, on dit donc que $b=0$, mais en réalité $b$ pourrait prendre n’importe quelle valeur arbitraire.

Ainsi, la solution particulière est donnée par

$$
y_*(x) = -xe^x
$$

Et finalement, la solution finale de $y$ est donc

$$
y=y_0+y_* \iff y=C_1e^x+C_2e^{2x}-xe^x=\underbrace{(C_1-x)}_{b\text{ dedans}}e^x+C_2e^{2x}
$$

On peut voir pourquoi on ne s’intéresse pas à quelle valeur de $b$ fixer : elle sera contenue ou absorbée par la constante $C_1$.

## D’autres notes

un polynome de 2me degré, s’il a des racines complexes propres, elles sont conjugués l’une de l’autre

il est toujours vérifié que la moyenne des racines égale l’axe de symmétrie verticale, racine réelles ou complexes propres

rappeler “lazy AC”

LIATE !

il faut toujours écrire “la solution générale est la somme des deux autres solutions”.

n’essaie pas de deviner les racines de l’équa de 2eme dégré, tu sert à rien lol

propiétés de dérivés de coefficients de fourier/transformée de fourier, utile pour un exo mélangé d’equa diff