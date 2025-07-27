# 03 // réduction d’endomorphismes

# Rappel: changement de base

## Préparation : de $y=f(x)$ à $\bold{Y}_{B'}=A\bold{X}_B$

Soit $E$ un espace vectoriel de dimension finie et soit $B = (e_1, e_2, \dots , e_p)$ une base de $E$. Comme annotation, si $B$ est la base canonique, on n'écrit pas un souscrit $B$ sur un vecteur, il ne faut pas mentionner la base.

Rappelons que tout élément $x$ de $E$ se représente comme : $x = x_1e_1 + x_2e_2 + \dots + x_pe_p$. On dit que le vecteur colonne $\{x_1, x_2,\dots, x_p\}_B^T$ contient les coordonnées de $x$ sous la base $B$ de $E$.

L’objective est de faire une analogie de "$y = f(x)$" dans l'algèbre linéaire. Le premier pas est de fixer $f : E \mapsto F$ et $A = \text{Mat}_{B,B'}(f)$ (la matrice qui contient l'image de la base de $E$ exprimé dans la base de $F$).

Après, soit $\bold{X}$ un vecteur colonne de $E$ (exprimé dans la base $B$) et $\bold{Y}$ un vecteur colonne de $F$ (exprimé dans la base $B'$). Finalement, l'analogie de “$y = f(x)$" serait "$\bold{Y} = A\bold{X}$". Voyons que, dans le monde de l’algèbre linéaire, multiplier $\bold{X}$ par A à gauche est l’équivalence d’appliquer une fonction. Multiplier est d’appliquer une fonction.

## Matrice de passage d'une base $B$ à une autre $B^\prime$ : $P_{B,B^\prime}$

Soit $E$ un espace vectoriel de dimension finie $n$. On sait que toutes les bases de $E$ ont $n$ éléments. Fixons deux bases du même ensemble $E$ : $B$ et $B'$.

La **matrice de passage** $P_{B,B'}$ est la matrice qui exprime les vecteurs de $B'$ en termes de l'ancienne base $B$. C’est le concept le plus important du changement de base.

Si on multiplie un vecteur à la droite de $P_{B,B’}$, il se "traduit" de $B'$ à $B$. L'arrivée est toujours la base $B$ avec laquelle on s'exprime actuellement. On la note aussi $\text{Mat}_B(B')$.

<aside>
⚠️ Quelques notes par rapport à $P_{B,B’}$ :

- Puisqu'on reste dans un même espace vectoriel $E$, on peut noter $\text{Mat}_{B',B}(\text{id}(E))$.
- Ici, $\text{id}(E)$ est une fonction de $E \mapsto E$ qui laisse un vecteur inchangé. La seule chose qui change donc c'est l'expression de l'image de la base $B'$ exprimés en termes de la base $B$.
- Mais, puisque l'image "ne change rien", on juste exprime $B'$ en termes de $B$.
- **Fais attention à l'inversion des bases dans la notation !**
</aside>

On devrait connaître trois propriétés importantes de la matrice de passage :

- $P_{B',B} = (P_{B,B'})^{-1}$
- Prenons 3 bases : $B$, $B'$, $B''$. Donc $P_{B,B''} = P_{B,B'} \cdot P_{B',B''}$.
- $\bold{X} = P_{B,B'} \cdot \bold{X'}$, pour $\bold{X}$ élément de $E$ exprimé en $B$ et $\bold{X'}$ qui est le même élément de $E$ mais exprimé en $B'$.

## Formule de changement de base

### Sur deux espaces vectoriels $E$ et $F$

Rappelons : une **matrice d'application linéaire** décrit une fonction de $E \mapsto F$. Elle montre l'image de la base de départ dans la base d'arrivée. Une **matrice de passage** exprime un nouvelle base en terme d'une ancienne base toujours d'un même ensemble $E$. Il est très important de comprendre la différence entre les deux !

<aside>
⛑️ Aide : la notation $\text{Mat}_{1,2}$ se lit “de $1$ à $2$” tant que $P_{1,2}$ se lit “à $1$ de $2$”. $\text{Mat}$ se lit dans “le bon ordre”, càd. de gauche à droite ; et $P$ dans l’ordre inverse.

</aside>

La formule de changement de base est la suivante :

$$
B=Q^{-1}AP
$$

- On considère 4 bases : $\mathcal{B}_{E}$, $\mathcal{B}_{E}'$, $\mathcal{B}_{F}$, $\mathcal{B}_{F}'$.
- $A = \text{Mat}_{\mathcal{B}_{E},\mathcal{B}_{F}}(f)$ et $B = \text{Mat}_{\mathcal{B}_{E}',\mathcal{B}_{F}'}(f)$ sont des fonctions.
- $P = P_{\mathcal{B}_{E},\mathcal{B}_{E}'}$ et $Q = P_{\mathcal{B}_{F},\mathcal{B}_{F}'}$ sont des passages.

Lisons de droite à gauche pour comprendre ce que elle veut nous dire :

$$
B\bold{Y}_{\mathcal{B}}=Q^{-1}AP\bold{Y}_{\mathcal{B}'}\\[4pt](e\mathcal{b}'_e)\rightarrow_{\text{id}_E} (E,\mathcal{B}_E)\rightarrow_f(F,\mathcal{B}_F)\rightarrow_{\text{id}_F}(F,\mathcal{B}'_F)
$$

1. $P$ : On prend un vecteur $\bold{Y}$ de notre ensemble $E$ et on change sa base de $\mathcal{B}_{E}'$ à $\mathcal{B}_{E}$.
2. $A$ : Après, on applique $f$ et le résultat sera en $\mathcal{B}_{F}$.
3. $Q^{-1}$ : Finalement, on va exprimer le vecteur résultat de $\mathcal{B}_{F}$ à $\mathcal{B}_{F}'$.
Attention ! Ce ne pas $Q$, mais $Q^{-1}$, ça m’a posé de problèmes.
4. $B$ : Mais, notons que tout cela serait le même que prendre $\bold{Y}$ exprimé en $\mathcal{B}_{E}'$ et prendre son image par $f$ exprimé en $\mathcal{B}_{F}'$.

### Sur un même espace vectoriel $E$

Le processus est plus simple si on parle d'un endomorphisme $E \mapsto E$ :

$$
B = P^{-1}AP
$$

- $P = P_{\mathcal{B},\mathcal{B}'}.$
- $A = \text{Mat}_{\mathcal{B}}(f)$.
- $B = \text{Mat}_{\mathcal{B}'}(f)$.

Interprétation :

1. $P$ : On prend un vecteur $\bold{Y}$, écrit en $\mathcal{B}'$, et on le réécrit en $\mathcal{B}$.
2. $A$ : Après, on passe $E$ par la fonction $f$, ce qui nous laisse un résultat en $\mathcal{B}$.
3. $P^{-1}$ : Finalement, on reprend l'image avec $B$ et on la réécrit en $\mathcal{B}'$.
4. $B$ : Notons que tout cela serait le même si on applique la fonction nous laissant un résultat en $\mathcal{B}'$.

### Matrices semblables

On dit que la matrice $B$ est semblable à la matrice $A$ s’il existe une matrice inversible $P ∈ M_n(K)$ telle que $B = P^{−1}AP$. Deux matrices semblables représentent le même endomorphisme, mais exprimé dans des bases différentes.

- La relation "être semblable" est réflexive, symétrique et transitive.

# Diagonalisation de matrices

## Polynôme caractéristique : $P_{M,C}(\lambda) = \det(M-\lambda I)$

Le polynôme caractéristique est le polynôme unitaire (dont le coefficient du
terme de plus haut degré est 1) lié à la matrice $M$ par $P_M(\lambda) = \det(M-\lambda I)$. Il est invariant sous la similarité de matrices. Par exemple :

$$
M = \begin{bmatrix}
1&-1&0\\
1&-2&-1\\
0&-1&1
\end{bmatrix}
\implies
\det(M-\lambda I) =
\begin{vmatrix}
1-\lambda&-1&0\\
-1&2-\lambda&-1\\
0&-1&1-\lambda
\end{vmatrix}
\newline
\text{}
\newline
= -\lambda(\lambda-1)(\lambda-3)
$$

Il y a des situations où il y a une “racine double”, c’est-à-dire, ou un facteur du polynôme caractéristique est au carré (ou à autre puissance différente de 1). Dans ce cas, pour construire la matrice de passage $P$, on devra déduire deux bases linéairement indépendantes du valeur propre. Si c’est impossible, la matrice est non-diagonalisable.

J’ai tendance à me tromper aux calculs du polynôme caractéristique. **Si on te donne la réponse factorisée, expande-la.**

## Valeur propre : $\lambda$

Une fois établi notre polynôme caractéristique, les valeurs propres seront simplement les racines du polynôme. On déduit de l’exemple que elles sont $0$, $1$ et $3$.

On note ici que l’ensemble de racines d’un polynôme caractéristique d’une matrice est appelé le *spectre* de $M$ et noté comme $\text{Sp}(M)$. 

## Sous-espace propre : $E_\lambda=\text{Ker}(M-\lambda I)$

Le sous-espace propre $E_\lambda$ est le noyau de $(M-\lambda I)$. Si $v$ appartient $E_\lambda$, alors : 

$$
v \in \text{Ker}(M-\lambda I) \iff (M-\lambda I)v = 0 \iff Mv = \lambda v
$$

## Vecteur propre : $v_\lambda$

Un vecteur propre $v_\lambda$ associé a un valeur propre $\lambda$ est un tel vecteur qui satisfait l’équation $Mv_\lambda = \lambda v_\lambda$. Intuitivement, le vecteur propre d’un opérateur linéaire est la direction où cet opérateur fonctionne comme si c’était une escalade. En la pratique, on ne cherche pas seulement un vecteur propre, mais une base des vecteurs propres. Continuant avec l’exemple (les solutions sont des bases):

$$
E_\lambda = \{0,1,3\} \implies \begin{cases}
E_0 = \{k \overrightarrow{(1,1,1)},\space k \in \R \}\\
E_1 = \{k \overrightarrow{(1,0,-1)},\space k \in \R \}\\
E_3 = \{k\overrightarrow{(1,-2,1)},\space k \in \R \}\\
\end{cases}
$$

Si on crée une famille avec ces bases de chaque sous espace propre, la famille est libre.

Notons que de chaque équation $Mv=\lambda v$, pour tous les valeurs propres de $\lambda$, j’arrive à extraire une base comme solution, C’ést-à-dire, pour chaque valeur propre $\lambda$, l’opération $(M - \lambda I)$ nous laisse au moins une équation ou ligne de la matrice qui est linéairement dépendante des autres. Et bien sûr, à ce moment là on a une droite ou plan solution, donc une infinité de $v$ possibles, lesquels on peut exprimer avec une base.

Normalement, $(M - \lambda I)$ sera une matrice avec une seule ligne dépendante des autres. Parfois, il arrive que il y a deux ou plus, donc la solution en fait est un plan ou une structure linéaire de dimension plus grande. On peut, dans ce cas, extraire plus d’un seul vecteur base de solutions. Un plan est décrit avec une base de dimension $2$, donc on en peut extraire deux vecteur bases, par exemple.

Ce dernier est utile dans le cas d’un valeur propre avec multiplicité algébrique $> 1$, voir la section de matrices non-diagonalisables. 

## Diagonalisation en pratique : $A = PDP^{-1}$

Finalement, on construit notre diagonalisation qui est de base $A = PDP^{-1}$. Elle devient ce qui suit. Les couples vecteurs-valeurs doivent être dans la même colonne de leurs matrices respectives.

$$
M=
\overbrace{
\begin{bmatrix}
1&1&1\\
1&0&-2\\
1&-1&1
\end{bmatrix}
}^P
\overbrace{
\begin{bmatrix}
0&0&0\\
0&1&0\\
0&0&3
\end{bmatrix}
}^D
P^{-1}
$$

**Théorème**. Si $f$ est un endomorphisme de $\R^n$ a travers la matrice $M$, les assertions suivantes sont équivalentes :

- On peut trouver une base de vecteurs propres $(v_{\lambda_1}, \dots, v_{\lambda_n})$.
- La somme directe des sous espaces propres $E_{\lambda_i}$engendre $\R^n$.
- Dans la base de vecteurs propres $(v_{\lambda_1}, \dots, v_{\lambda_n})$, la matrice $M$ de $f$ est diagonale.

**Note** : la trace est une invariant de similitude. C’est-à-dire, $\text{Tr}(M)=\text{Tr}(D)$. Ceci est utile pour déterminer des valeurs dans la diagonale de $D$ qu’on ne connaît pas.

# Applications

## Puissance d’une matrice : $M^n=PD^nP^{-1}$

Appliquer une puissance à une matrice diagonale est beaucoup plus facile en termes de computation que à une matrice non-diagonale. Particulièrement, si on reprend la matrice diagonale D de l’exemple passé…

$$
\begin{bmatrix}
0&0&0\\
0&1&0\\
0&0&3
\end{bmatrix}^n =
\begin{bmatrix}
0^n&0&0\\
0&1^n&0\\
0&0&3^n
\end{bmatrix}
$$

La définition d’une puissance est la multiplication répétitive d’une base. Notons que :

$$
\begin{align*}
M^n & = \overbrace{M \times M \times \dots \times M}^\text{n fois}
\newline
& = PD\cancel{P^{-1}} \times \dots \times \cancel{P}DP^{-1}
\newline
& = PD^nP^{-1}
\end{align*}
$$

## Inverse d’une matrice : $M^{-1}=PD^{-1}P^{-1}$

De même avec l’opération inverse, qui est aussi un exposant $-1$. On aura besoin de la propriété $(AB)^{-1} = B^{-1} A^{-1}$, et aussi de la associativité de matrices. Le résultat final c’est que l’exposant agit sur la matrice diagonale, qui est de nouveau convenant pour les opération de puissances comme vu dans la section passée.

$$

M^{-1} = [(PD)(P^{-1})]^{-1} = (P^{-1})^{-1}(PD)^{-1} = PD^{-1}P^{-1}
$$

## Exponentielle d’une matrice : $e^M=Pe^DP^{-1}$

Si bien la notion de $e^M$, avec $M$ une matrice, ne fais pas du sens, on utilise plutôt l’expansion de Taylor de la fonction $e^x$. Cette dernier fait du sens car on a juste besoin d’une définition de puissances de matrices, ce qu’on a déjà vu et construit.

$$
e^x = \sum_{n \ge 0} \frac{x^n}{n!} \implies e^M = \sum_{n \ge 0} \frac{M^n}{n!}= \sum_{n \ge 0} \frac{PD^nP^{-1}}{n!}= P(\sum_{n \ge 0}\frac{D^n}{n!})P^{-1}

\newline
\text{ }
\newline

\text{Or, }
\sum_{n \ge 0}\frac{D^n}{n!} =
\begin{bmatrix}
\sum_{n \ge 0} \frac{0^n}{n!} & 0 & 0 \\
0 & \sum_{n \ge 0}\frac{1^n}{n!} & 0 \\
0 & 0 & \sum_{n \ge 0} \frac{3^n}{n!}
\end{bmatrix}
=
\begin{bmatrix}
e^0 & 0 & 0 \\
0 & e^1 & 0 \\
0 & 0 & e^3
\end{bmatrix} = e^D

\newline
\text{ }
\newline

\text{Finalement, } e^M = Pe^DP^{-1}
$$

## Application aux systèmes différentiels linéaires

Commençons avec un exemple. On a le système d’équations différentiels ($y_i = y_i(x)$):

$$
\begin{cases}
\begin{align*}
&y^\prime_1 &{=} &&{y_1} &&+ && y_2
\\
&y^\prime_2 &{=} &&{4y_1} &&- &&2y_2
\end{align*}
\end{cases}
$$

Avant de chercher les solutions, on écrit le système sous forme matricielle comme suit :

$$
\bold{y^\prime}=A\bold{y} \iff 
\begin{bmatrix}
y^\prime_1 \\
y^\prime_2
\end{bmatrix}
=
\begin{bmatrix}
1 & 1 \\
4 & -2
\end{bmatrix}
\begin{bmatrix}
y_1 \\
y_2
\end{bmatrix}
$$

La solution n’est pas encore claire ici. Donc, si $A$ est diagonalisable avec $P$ comme matrice de passage, on va simplement supposer que $\bold{y}=P\bold{u}$, où $\bold{u}$ est un vecteur inconnu. La transformation suivante nous sera utile :

$$
\bold{y}=P\bold{u} \implies \bold{y^\prime} = P\bold{u^\prime} \implies P^{-1}\bold{y'} = \bold{u'} \implies
\overbrace{
P^{-1}A\bold{y}=\bold{u'}}^{(\bold{y'}=A\bold{y})}
\\
\text{}
\\
\implies
\overbrace{
P^{-1}AP\bold{u}=\bold{u'}}^{(\bold{y}=P\bold{u})} \implies \bold{u^\prime}=D\bold{u}
$$

Pourquoi est-elle utile ? Le système d’équations du départ est “couplé”, càd. on ne peut pas séparer $y_1$ et $y_2$ pour trouver des solutions particulières. Par contre, quand le système n’est pas couplé, il est plus facile de trouver une solution particulière.

Il arrive que le système n’est pas couplé quand la matrice qui le décrit, $A$, est triangulaire. Si on voit $\bold{u^\prime}=D\bold{u}$, la matrice du système $D$ est une matrice diagonale et donc triangulaire. Donc, on peut trouver des solutions à ce système qui est plus simple et puis arriver à la solution du système de départ.

On diagonalise alors $A$, et on détermine sa matrice de passage $P$ et celle diagonalisée $D$ pour finalement déterminer $\bold{u^\prime}$:

$$
\overbrace{\begin{bmatrix}
1&1\\
4&-2
\end{bmatrix}}^A=
\overbrace{\begin{bmatrix}
-1&1\\
4&1
\end{bmatrix}}^P
\overbrace{
\begin{bmatrix}
-3&0\\
0&2
\end{bmatrix}}^D
P^{-1}

\implies

\overbrace{
\begin{bmatrix}
u^\prime_1 \\
u^\prime_2
\end{bmatrix}}^\bold{u^\prime}
=
\overbrace{
\begin{bmatrix}
-3&0\\
0&2
\end{bmatrix}}^D
\overbrace{
\begin{bmatrix}
u_1\\
u_2
\end{bmatrix}}^\bold{u}=
\begin{bmatrix}
-3u_1\\
2u_2
\end{bmatrix}
$$

Rappelons l’équation qui lie les valeurs propres d’une transformation linéaire à elle-même : $Mv=\lambda v$. Dans ce contexte, il faut penser plutôt à une fonction $y$ ou $u$ à la place d’une transformation linéaire, et particulièrement cette fonction est la dérivé d’une autre fonction : $y^\prime(v)=\lambda v$. En plus, si on ajoute la contrainte $y^\prime(0) = c, c\in\R$, alors on déduit que $y(x)=ce^{\lambda x}$.

Pensons l’interprétation de $y^\prime(v)=\lambda v$ : dériver la fonction est la même chose que l’escalader par $\lambda$. C’est presque la même chose qu’avec la transformation linéaire ! On peut donc voir, pour chaque $y_i$, leur dérivées est juste une combinaison linéaire entre elles. C’est donc un système d’équations différentiels ***linéaire***. On déduit donc $u_1$ et $u_2$ :

$$
\overbrace{
\begin{bmatrix}
u^\prime_1 \\
u^\prime_2
\end{bmatrix}}^\bold{u^\prime}
=
\begin{bmatrix}
-3u_1\\
2u_2
\end{bmatrix}
\implies

\overbrace{
\begin{bmatrix}
u_1\\
u_2
\end{bmatrix}}^\bold{u}
=
\begin{bmatrix}
c_1e^{-3x}\\
c_2e^{2x}
\end{bmatrix}
$$

On retourne à l’équation qui lie $\bold{y}$ et $\bold{u}$ : $\bold{y} = P \bold{u}$. Maintenant, on peut déduire $\bold{y}$ :

$$
\overbrace{
\begin{bmatrix}
y_1\\
y_2
\end{bmatrix}}^\bold{y}=
\overbrace{\begin{bmatrix}
-1&1\\
4&1
\end{bmatrix}}^P
\overbrace{
\begin{bmatrix}
u_1\\
u_2
\end{bmatrix}}^\bold{u} =
\overbrace{\begin{bmatrix}
-1&1\\
4&1
\end{bmatrix}}^P
\overbrace{
\begin{bmatrix}
c_1e^{-3x}\\
c_2e^{2x}
\end{bmatrix}}^\bold{u}=
\begin{bmatrix}
-c_1e^{-3x}+c_2e^{2x} \\
4c_1e^{-3x}+c_2e^{2x}
\end{bmatrix}
$$

Ici, on a théoriquement fini. Si jamais on a des conditions sur $y_i(0) = c, c\in\R$, on peut déterminer $c_1$ et $c_2$. Disons que $y_1(0)=1$ et $y_2(0)=6$, donc : 

$$
\begin{cases}
\overbrace{1}^{y_1(0)} = -c_1+c_2\\
\underbrace{6}_{y_2(0)} = 4c_1+c_2
\end{cases} \implies \begin{cases}
c_1= 1\\
c_2=2
\end{cases}
\implies
\begin{cases}
y_1= -e^{-3x}+2e^{2x}\\
y_2= 4e^{-3x}+2e^{2x}
\end{cases}

$$

**Théorème**. Si $M$ est une matrice diagonalisable, donc la solution générale d’un système peut être exprimé comme : $\bold{y} = \sum_i^n c_ie^{\lambda_i x}\bold{v}_i$, où $\lambda_i$ est le valeur propre associé et $\bold{v}_i$ est le vecteur propre associé (ou vecteur en colonne $i$ de la matrice de passage $P$).

## Application aux suites récurrentes

Rappelons que multiplier une vecteur par une matrice nous retourne un vecteur. La matrice est, dans ce sens, une sorte de fonction. Grâce à ça, on peut développer un sens de récurrence avec de matrices, particulièrement pour les suites où un prochain terme est une combinaison linéaires des termes passés. Ici, la fonction récurrente sera la matrice $M$.

$$
\text{Soit }U_p=\overrightarrow{(u_p,v_p,w_p)}\text{ et } U_{p+1}=\overrightarrow{(u_{p+1},v_{p+1},w_{p+1})}
\newline
\text{}
\newline
\text{ tel que }
\begin{align*}
\begin{cases}
u_{p+1} = u_p - v_p \\
v_{p+1} = -u_p+2v_p-w_p \\
w_{p+1} = -v_p+w_p
\end{cases}
\end{align*}.
\text{ Donc, } U_{p+1}=
\overbrace{
\begin{bmatrix}
1 & 1 & 0\\
-1 & 2 & -1\\
-1 & 1 & 0
\end{bmatrix}
}^M
U_p
$$

Rappelons aussi que appliquer une “fonction” $p$ fois à une vecteur est la même chose que la multiplier $p$ fois par la matrice d’application $M$, c’est-à-dire multiplier par $M^p$.

Or, on sait que appliquer des puissances à matrices diagonaux est plus simple qu’à d’autres matrices. Donc, on diagonalise $M$ et cela rendra les calculs des prochains termes de la suite beaucoup plus simple.

$$
M=PDP^{-1} \implies U_{p+1}=(PDP^{-1})U_p \implies U_p = P D^p P^{-1} U_0.
$$

La dernière expression, après avoir fait tous les produits entre vecteurs et matrices, sera une expression explicite des termes généraux de $u_p$, $v_p$ et $w_p$. 

# Matrices non-diagonalisables

## Un cas particulière de matrices

Pas toute matrice est diagonalisable, une telle matrice est dite *matrice défectueuse*. Formellement, une matrice défectueuse est une matrice carré qui n’a pas une base complète de vecteurs propres.

$$
M \text{ défecteuse} \iff M\text{ n’as pas } n \text{ vecteurs propres linéairement indépendantes}.
\newline
M \text{ défecteuse} \implies M \text{ a moins de  } n \text{ valeurs propres distincts. Réciproque fausse.}
$$

Ici c’est important le concept de multiplicité algébrique. Pensons à cet exemple :

$$
M = \begin{bmatrix}
3&-1&1\\
0&2&0\\
1&-1&3
\end{bmatrix}
\implies \text{det}(M-\lambda I)=-(\lambda-2)^2(\lambda-4)
$$

La valeur $\lambda=2$ annule deux facteurs polynomiaux. Donc, on dit que la valeur propre $2$ a une multiplicité algébrique de $2$.

Dans ce cas, il est possible qu’on n’arrive pas à extraire une quantité suffisante de vecteurs bases des matrices $(M-\lambda I)$, dans ce cas $\lambda = 2$. Pour que ce soit possible, la matrice $(M-\lambda I)$ doit avoir une quantité de lignes linéairement dépendantes à la multiplicité algébrique de la valeur propre $\lambda$.

Dans la section “vecteur propre”, j’explique que c’est car on peut extraire plus de bases avec plus de lignes dépendantes dans la matrice $(M-\lambda I)$. Si on veut diagonaliser la matrice associé au polynôme $-(\lambda-2)^2(\lambda-4)$, $(M-2I)$ doit avoir $2$ lignes linéairement dépendantes ou plus, sinon elle n’est pas diagonalisable.

Mais, en général, voir un facteur polynomial répété implique une matrice non-diagonalisable.

Il est plus clair avec l’exemple du professeur fait en TD dans ce PDF.

[Exo 5.3 ALG3.pdf](ressources/03_reduction_d’endomorphismes_ex_5.3_alg3.pdf)