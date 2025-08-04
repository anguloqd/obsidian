# 01 // rappels sur les espaces vectoriels

# Équations linéaires ou cartésiennes

## Définition et astuces

Une équation cartésienne définit un sous-espace vectoriel. Par exemple :

$$
E =
\left\{
v =
\begin{bmatrix}
x \\
y \\
z \\
\end{bmatrix} :
2x - y - z = 0
\right\}
$$

Le coefficient libre doit être forcément $0$ ! Cela implique que le vecteur nul appartient à l’ensemble, condition nécessaire pour un sev.
Si le coefficient libre était différent de $0$, on ne parlerait pas d’un espace vectoriel mais d’un ***espace affin***, car le vecteur nul n’y est pas inclus.

De cette manière, on décrit l’ensemble de points qui appartient à ce plan.
Dans $\mathbb{R}^n$, une équation linéaire à $n$ variables décrit un sous-espace vectoriel de dimension $(n-1)$.

On peut aussi décrire un même ensemble d’un hyperplan de dimension $n$ avec $n$ points ou vecteurs appartenant à l’hyperplan
Par exemple, notons que $[1,1,1]$ et $[0,1,-1]$ vérifient l’équation cartésienne $2x-y-z=0$. Donc, ils appartiennent l’ensemble.
Finalement, on peut décrire le même hyperplan comme l’espace engendré de ces deux vecteurs.

$$
E = \text{Vect}
\Biggl(
\begin{bmatrix}
1 \\
1 \\
1 \\
\end{bmatrix}
,
\begin{bmatrix}
0 \\
1 \\
-1 \\
\end{bmatrix}
\Biggr)
$$

Un ensemble d’équations linéaires est dit “lié” si on peut décrire une avec une combinaison linéaire des autres. C’est le même comme les familles de vecteurs liées. Si on prend l’équation d’avant et on la multiplie toute par $2$, l’ensemble solution reste exactement le même. Donc, les deux équations $2x-y-z=0$ et $4x-2y-2z=0$ décrivent le même ensemble, ou sont essentiellement “la même équation”.

De la même manière, une structure linéaire (une ligne, un plan, un hyperplan) peut être vu comme l’intersection de deux autres structures linéaires non-liées ou l’ensemble solution d’un système d’équations. Par exemple, dans $\mathbb{R}^3$, l’intersection de deux plans non-liées décrit une droite.

Dans $\mathbb{R}^n$, un système de $k$ équations linéaires non-liées, chacune à $n$ variables, décrit un sous-espace vectoriel de dimension $(n-k)$. 
C’est-à -dire, un ensemble $E_1, …, E_k$ non-lié implique que le chaque équation est une “pièce d’information unique” et, s’il existe une solution, c’est le vecteur nul (supposant coefficient libre égal $0$).

## Équations vectoriels d’une droite et un plan

Pour le cas d’une droite dans le plan 2D, l’expression est celle-ci. Ici, c’est la forme générale, c’est-à-dire, on représente un ensemble de points. Pour représenter un point spécifique, on fixe $\lambda$ et on commence à varier $x$ pour obtenir $y$. Notons que si on veut représenter un sous-espace vectoriel, forcément le vecteur position $(P_1, P_2)$ est le vecteur nul $(0, 0)$.

$$
(x,y) = (P_1, P_2) + \lambda (v_1,v_2)
$$

De même, on peut la définir comme cela pour un plan. et s’il s’agit d’un sous-espace vectoriel, donc le vecteur position est aussi le vecteur nul. On fixe $\lambda$ et on fait varier $x$ et $y$ pour obtenir $z$.

$$
(x,y,z) = (P_1, P_2, P_3) + \lambda (v_1,v_2,v_3)
$$

Notons que quand on dit “on fait varier $x$ et $y$ pour obtenir $z$”, $z$ est une variable dépendante de $x$ et $y$, c’est-à-dire, $z$ est contrainte à $x$ et $y$. Dans le cas 2D, $y$ est contrainte à $x$ si on a une seule équation.

Si on ajoute une autre équation d’un plan $E_2$ (non-colinéaire à la $E_1$) à notre système d’équations, implicitement on ajoute une contrainte sur $y$. Maintenant, on fait varier $x$ pour obtenir $y$ et $z$. On peut donc écrire $y$ et $z$ en termes de $x$, ce qui tombe bien pour trouver de solutions aux deux équations.

$$
\\[8pt]
\begin{cases} E_1 : x+y+z=0
\end{cases} \text{ } \\[7pt]
\implies (x,y,z) = (x,y,-x-y)
\newline x, y \text{ indépendentes}.
$$

$$
\begin{cases}
E_1 : x+y+z=0 \\
E_2 : x + 2y + 3z = 0
\end{cases}
\\[7pt]
\implies (x,y,z) = (x,-2x,x)
\newline
x\text{ indépendent}.

$$

Si on ajoutait une équation qui serait une combinaison linéaire des équation déjà appartenant au système, on ne change rien, les solutions restent le mêmes. Dans le cas d’une droite dans l’espace, ajouter une équation liée serait d’ajouter un plan qui contient la droite intersection des deux autres équations. Elle est donc redondante.

Finalement, si on ajoute une troisième équation non-liée, $x$ n’est plus indépendant, et la solution devient juste un point dans l’espace. Toutes les coordonnées ($x$, $y$ et $z$) sont liés les unes aux autres. Si toutes les équations représentent des sous-espaces vectoriels, la solution est triviale : le vecteur nul. Si on essaie d’exprimer une coordonnée en termes des autres, on arrive forcément à $0$ a travers la simplification de l’algèbre.

$$
\begin{cases}
E_1 : x+y+z=0 \\
E_2 : x + 2y + 3z = 0 \\
E_3 : x+4y+9z = 0
\end{cases}
\implies (x,y,z) = (0,0,0)
\newline

$$