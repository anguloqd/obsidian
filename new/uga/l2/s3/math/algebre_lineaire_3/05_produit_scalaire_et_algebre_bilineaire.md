# 05 // produit scalaire et algèbre bilinéaire

# Définitions

## Produit scalaire : ce n’est pas que le produit matriciel

Le produit scalaire n’est pas seulement le produit matriciel. En réalité, un produit scalaire est une opération d’une famille d’opération qui satisfait quelques propriétés :

$$
f :(x,y) \mapsto \langle x,y \rangle
$$

- Linéaire par rapport à chaque variable :
$\langle x+ \lambda x', y \rangle = \langle x,y \rangle + \lambda\langle x',y \rangle$ et $\langle x, y+ \lambda y' \rangle = \langle x,y \rangle + \lambda\langle x,y' \rangle$
- Symétrie : $\langle x,y \rangle = \langle y,x \rangle$
- Définition positive : $\langle x,x \rangle \ge 0$ et  $\langle x,x \rangle = 0 \implies x = 0$.

# Norme et distance issues

Une norme et une distance sont aussi des concepts qui ne sont pas représentés par une seule fonction, mais par une famille de fonctions qui vérifie quelques propriétés.

## Norme : $||x||$

Une norme est toute fonction $f : x \mapsto ||x|| \in \mathbb{R}^+$ qui intuitivement capture une “distance” d’un point à partir de l’origine. Elle doit vérifier les conditions suivantes :

- $||\lambda x|| = |\lambda| ||x||$
La norme est multiplicative, càd. $f(xy)=f(x)f(y)$
- $||x+y|| \le ||x|| + ||y||$
Inégalité triangulaire
- $||x|| = 0 \implies x = 0$ 
Si la longueur ou magnitude d’un élément est $0$, donc il est le vecteur nul

On peut définir une ***norme issue du produit scalaire*** : $||x|| = \sqrt{\langle x,x \rangle}$, ce qui nous donne la norme euclidienne, la norme la plus populaire (la ligne diagonale entre deux points). Cela dit, on peut avoir des normes qui ne sont pas issues ou définies à partir du produit scalaire.

**Théorème : Inégalité de Cauchy-Schwarz**. $|\langle x,y \rangle| \le \sqrt{||x||}\sqrt{||y||}$. Cette inégalité devient une égalité stricte en valeur absolue si et seulement si $x$ et $y$ sont colinéaires entre eux.

## Distance : $d(x,y)$

Une distance entre deux points est toute fonction $f : (x,y) \mapsto d(x,y) \in \mathbb{R}^+$ qui vérifie ce qui suit :

- $d(x,y)=0 \iff x=y$ 
Si la distance entre deux points est $0$, $x$ et $y$ sont à la même position
- $d(x,y)=d(y,x)$
La distance de $x$ à $y$ est la même de $y$ à $x$, on appelle ceci *symétrie*
- $d(x,z) \le d(x,y) + d(y,z)$
Inégalité triangulaire

Similairement, on peut définir une distance issue d’une norme : $d(x,y)=||x-y||$. **Par contre, deux observations :**

- La norme dont la distance est issue n’est pas forcément une norme euclidienne.
- On n’a même pas besoin de définir la distance à partir d’une norme. Il y a des distances sans une norme correspondante. Par exemple :
    - $d_1(x,y) = 0\text{ si }x=y, 1\text{ sinon}.$
    - $d_2 (x,y) = |\arctan x - \arctan y\space|$
    - Une norme est déduite d’une distance si $d(\alpha x, \alpha y)=|\alpha|d(x,y)$.

Malgré ça, dans la pratique une distance est issue par une norme et les distances “inusuelles” sont juste utilisés pour induire un concept. Par exemple, $d_2$ donne un exemple d’un espace métrique incomplet.

# Orthogonalité

## Définition et théorème de Pythagore généralisé

On dit que deux vecteurs $x$ et $y$ sont **orthogonaux** si et seulement si $\langle x,y \rangle = 0$.

**Théorème de Pythagore**. Deux vecteurs $x$ et $y$ sont orthogonaux si et seulement si |$|x+y||^2=||x||^2+||y||^2$. De manière générale, une famille de vecteurs $\{x_i\}$ est orthogonale deux à deux si et seulement si $||x_1+ \dots+ x_n||^2 = ||x_1||^2 + \dots + ||x_n||^2$.

## Un ensemble $F^\perp$ orthogonal à un autre $F$

Avec cette définition, on peut définir un ensemble $F^\perp \in E$ de vecteurs orthogonal à un autre ensemble $F\in E$ de vecteurs tel que $F^\perp = \{y\in E : \langle x,y \rangle = 0, \forall x \in F \}$. C’est-à-dire, chaque vecteur de $F^\perp$ est orthogonal à tous les vecteurs de $F$.

- **Propriété #1** : $(F^\perp)^\perp = F$.
- **Propriété #2** : Si $F = \text{Vect}(\{a_i\})$, donc $F^\perp = \big\{ \{x_i\} : a_1x_1 + \dots + a_n x_n = 0 \big\}$
- **Propriété #3** : $E = F \oplus F^\perp$.

On peut donc voir chaque vecteur de $E$ comme une somme d’un vecteur de $F$ et de $F^\perp$. C’est-à-dire, $x = p_F(x) + p_{F^\perp}(x)$. Donc, une projection d’un vecteur $x$ sur un ensemble  est le vecteur $x_F$, c’est-à-dire, le composant du vecteur  qui vient de l’ensemble .

**Note** : on peut voir donc $p_F(x) + p_{F^\perp}(x)$ comme la fonction identité $\text{Id}(x)$.

# Bases orthonormées

## Définition

Soit $B=\{e_i\}$ une base de $E$. Elle est orthonormée si :

- $\forall e_i\in B, ||e_i||=1$.
- Les vecteurs sont deux à deux orthogonaux : $\langle e_i, e_j \rangle = 0, i \ne j$.

Une première note importante à faire c’est que, si $F_1\in E$ tel que $F_1=\text{Vect}(e_1)$, donc

$$
p_{F_1}(u)=\langle u, e_1 \rangle e_1 
\\
\text{D'où, } u = \text{Id}(u)=p_{F_1}(u)+\dots+p_{F_n}(u)=\langle u,e_1\rangle e_1 +\dots+ \langle u,e_n \rangle e_n
\\
\text{Et, appliquant Pythagore, }||u||^2=\langle u,e_1 \rangle^2 + \dots + \langle u,e_n \rangle^2
$$

Pour tout ce qui précède, il est vital que la norme de $||e_i|| = 1$. Sinon, la règle générale est :

$$
p_F(u)=\frac{\langle u,v \rangle}{||v||^2}v
$$

**Théorème**. Soit $E$ un espace (hilbertien ou hermitien) de dimension $n$ muni d’un produit scalaire/hermitien. Donc, il existe dans $E$ des bases orthonormées.

## Projection orthogonale : $p_F(u)=\sum_{i=1}^n \lang u, e_i \rang e_i$

Sur l’espace vectoriel $E$ de dimension $n$, soit $F$ un sous-espace de base orthonormé $\{e_1\}$.

**Théorème**. La projection orthogonale de $u\in E$ sur $F$ est :

$$
p_F(u)= \langle u, e_1\rang e_1 + \dots + \lang u, e_n \rang e_n=\sum_{i=1}^n \lang u, e_i \rang e_i
$$

La chose à retenir est que la projection orthogonale $v=p_F(u)$ d’un vecteur $u$ est le point qui minimise la distance de $u$ à $v$. C’est-à-dire : $||u-p_F(u)||=\inf \{ ||u-v||,  v\in F\}$.

# Orthonormalisation : procédé de Gram-Schmidt

## L’algorithme et le théorème qui le garantit

> [!note]
> Théorème. Si $\{v_i\}$ est famille libre, donc il existe une unique $\{e_i\}$ orthonormée telle que :
>
> 1. $\{e_i\}$ engendre le même espace que $\{v_i\}$, donc $\text{Vect}(\{e_i\})=\text{Vect}(\{v_i\})$
> 2. Les produits scalaires entre deux vecteurs de $\{e_i\}$ et $\{v_i\}$ resp. sont strict. positifs. C’est-à-dire, $\lang v_i, e_j \rang > 0, \forall i,j \le n$.

À partir d’une famille libre de vecteurs $\{v_i\} \in E$, on peut construire une base orthonormée $\{e_i\}$ avec ce procédé de Gram-Schmidt. La logique est la suivante :

1. De la famille $\{v_i\}$, on normalise $v_1$ à $e_1$, qui sera le premier vecteur orthonormée de $\{e_i\}$
2. On prend $v_2$ et on lui rend orthogonal à $v_1$, donc on a $o_2$, puis on normalise et on a $e_2$.
3. On prend $v_3$, on l’orthogonalise p.r. à $\{v_1,v_2\}$ et on le normalise, on finit avec $e_3$.
4. Pour $v_n$, on l’orthogonalise p.r. à $\{v_{n-1}\}$, puis on le normalise et on finit avec $e_n$.
5. La base orthonormée finale sera finalement donné par $\{e_1, e_2, \dots, e_n\}$.

Plus mathématiquement, et soit $p_\mathbf{u}(\mathbf{v})=\frac{\lang \mathbf{u},\mathbf{v} \rang}{\lang \mathbf{u},\mathbf{u} \rang} \cdot \mathbf{u}$ la projection orthogonale de $\mathbf{v}$ sur $\mathbf{u}$, donc l’algorithme ou le procédé de Gram-Schmidt est comme suit :

$$
\begin{align*}
&&\mathbf{u}_1 = \mathbf{v}_1 &&\longrightarrow &&\mathbf{e}_1=\frac{\mathbf{u}_1}{||\mathbf{u}_1||} \\

&&\mathbf{u}_2 = \mathbf{v_2} - p_{\mathbf{u}_1}(\mathbf{v}_2) &&\longrightarrow &&\mathbf{e}_2=\frac{\mathbf{u}_2}{||\mathbf{u}_2||} \\

&&\mathbf{u}_3 = \mathbf{v_3} - p_{\mathbf{u}_1}(\mathbf{v}_3) - p_{\mathbf{u}_2}(\mathbf{v}_3)  &&\longrightarrow &&\mathbf{e}_3=\frac{\mathbf{u}_3}{||\mathbf{u}_3||} \\

&& &&\vdots \\

&&\mathbf{u}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} p_{\mathbf{u}_i}(\mathbf{v}_k)&&\longrightarrow &&\mathbf{e}_k=\frac{\mathbf{u}_k}{||\mathbf{u}_k||} \\

\end{align*}
$$

![Les deux premières étapes de gram-schmidt.](ressources/05_produit_scalaire_et_algebre_bilineaire_untitled.png)

Les deux premières étapes de Gram-Schmidt.