# 02 // régressions linéaires

# Motivation

## Quand on veut utiliser une régression linéaire

- On l'utilise quand on pense que une variable indépendante $x$ est un prédicteur d'une variable réponse $y$.
- Spécifiquement, si la relation entre $x$ et $y$ peut expliquée d'une manière linéaire, c’est-à-dire, avec une droite.

# Outils

## Méthode des moindres carrés

- La formule classique pour un droite est $y = f(x) = ax+b$,
- On veut la droite $y$ tel que la différence entre $f(x)$ et la valeur réelle y qui correspond a $x$ soit la plus petite possible, c'est-à-dire, les écart verticaux.
- Étant donné que les carrés pénalisent les valeurs extrêmes (écart-type), on les utilise.
- Toute droite de régression doit passer par le centre de gravité, c'est-à-dire, $(\bar{x},\bar{y})$.

## Formule pour trouver $a$ et $b$

- Alors, si $y = ax+b$, les valeurs pour $a$ et $b$ qui minimisent les écarts verticaux sont :
    - $a = \text{Cov}(X,Y)/Var(X)$.
    - $b = \bar{y} - a\bar{x}$
- Quelques formules utiles pour y arriver :
    - $\text{Var}(X) = E[X^2] - E[X]^2$
    - $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$

# Indicateurs de performance

## Coefficient de corrélation linéaire : $r$

- Dès qu'il y a deux points $(x,y)$ ou plus, on peut utiliser la méthode de moindres carrés.
- Cela veut pas dire, par contre, que c'est une bonne idée de toujours l'utiliser. Alors, ici on présent le coefficient de corrélation linéaire.
    - $r = \text{Cov}(X,Y)/\sqrt(\text{Var}(X)\text{Var}(Y))$
    - $-1 \le r \le 1$.
    - $r$ est du même signe de $a$ (la pente de la droite).
    - Si $|r| \ge 0.9$, on considère légitime de dire qu'il y a une relation linéaire entre $X$ et $Y$. Illégitime sinon.

## Coefficient d'amélioration : $R^2$

- La variance entre les valeurs réelles de $Y$ (non ceux qui appartient à droite) est $\text{Var}(Y)$.
- Notons que chaque point $Y$ peut être écrit comme l'estimé de la droit plus l'erreur ou le résidu.
    - $Y = (ax + b) + (\varepsilon)$.
    - Alors, $\text{Var}(Y) = \text{Var}(ax+b) + \text{Var}(\varepsilon)$, par linéarité de la variance de variables indépendantes !
    - $R^2 = \text{Var}(ax+b) / \text{Var}(Y)$.
    - $R^2$ est la variabilité de $Y$ expliqué par $X$.
    - Notons que $R^2$ est le carré de $r$, le coefficient de corrélation linéaire.
    - De même, $R^2$ est légitime si $R^2 \ge 0.81$.

# Extras

## Dilemme : expliquer $y$ avec $x$ ou $x$ avec $y$

- C'est un faux problème.
- Si $y = ax+b$ (la droite qu'explique $y$ en termes de $x$) a $|r|$ proche de $1$, alors ce serait de même pour $(x = ay + b)$.
- Les deux droites sont alors pratiquement égaux, et toutes les droites entre ces deux aussi.

## Changement de variable

- Si la nuage de points n'as pas une forme linéaire, mais on peut appliquer une fonction telle que $f(y)$ suivi une ligne (la fonction inverse de la fonction qui suivi les points), on peut donc appliquer une régression linéaire.
- Normalement, la fonction qu'on va appliquer est une $\exp()$ ou un $\ln()$.