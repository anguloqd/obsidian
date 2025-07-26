# 01 // matrices et applications linéaires

# Rang d'une famille de vecteurs

## Définition

Soit $E$ un $\mathbb{K}$-espace vectoriel et soit $\{v_1 , . . . , v_p\}$ une famille finie de vecteurs de $E$. Le rang de la famille $\{v_1 , . . . , v_p\}$ est la dimension du sous-espace vectoriel $\text{Vect}(v_1, . . . , v_p)$ engendré par les vecteurs $\{v_1 , . . . , v_p\}$. Autrement dit : $\text{rg}(v_1, . . . , v_p) = \text{dim } \text{Vect}(v_1, . . . , v_p)$.

- **Propositions importantes**  :
    - $0 \le \text{rg}(v_1, . . . , v_p) \le  p$, où $p$ est nombre d’éléments dans la famille
    - $\text{rg}(v_1, . . . , v_p) \le \text{dim }E$, si $E$ de dimension finie.
- Remarques :
    - Le rang d’une famille vaut $0$ si et seulement si tous les vecteurs sont nuls.
    - Le rang d’une famille $\{v_1, . . . , v_p\}$ vaut p si et seulement si la famille $\{v_1, . . . , v_p\}$ est libre.

## Rang d'une matrice

On définit le rang d’une matrice comme étant le rang de ses vecteurs colonnes. C’est-à-dire, la dimension de l’espace engendré des vecteurs colonnes de la matrice.

Une matrice intéressante par rapport à son rang est une **matrice échelonnée**. On dit qu’une matrice est échelonnée par rapport aux colonnes si le nombre de zéros commençant une colonne croît strictement colonne après colonne, jusqu’à ce qu’il ne reste plus que des zéros. Autrement dit, la matrice transposée est échelonnée par rapport aux lignes. Par exemple :

$$
\begin{bmatrix}
+&0&0&0&0&0\\
*&0&0&0&0&0\\
*&+&0&0&0&0\\
*&*&+&0&0&0\\
*&*&*&0&0&0\\
*&*&*&+&0&0
\end{bmatrix}
$$

Ici, les $∗$ désignent des coefficients quelconques (nuls ou non), et les $+$ des coefficients strictement non nuls. Le rang d’une matrice échelonnée par colonnes est égal au nombre de colonnes non nulles.

## Opérations conservant le rang

Telles opérations sont les opérations élémentaires :

1. **Escalade** : $C_i ← λC_i$ avec $λ \ne 0$. On peut multiplier une colonne par un scalaire non nul.
2. **Somme escaladée** : $C_i ← C_i + λC_j$ avec $λ ∈ K$ (et $j \ne i$). On peut ajouter à la colonne $C_i$ un multiple d’une autre colonne $C_j$.
3. **Échange** : $C_i ↔ C_j$. On peut échanger deux colonnes.

Plus généralement, on peut dire que l’opération $C_i ← C_i + ∑_{i \ne j} λ_jC_j$ conserve le rang de la matrice. L’espace vectoriel engendré par les vecteurs colonnes est conservé par ces opérations.

## Rang, matrices inversibles et transposées

Par rapport aux matrices inversibles, une matrice carrée de taille $n$ est inversible si et seulement si elle est de rang $n$.

Par rapport aux matrices transposées, on a que $\text{rg}A = \text{rg}(A^T)$. Cela n'implique pas que l'E.V. représenté par $A$ est le même que celui représenté par $A^T$ !

# Application linéaires en dimension finie

## Construction et *caractérisation*

Une application linéaire crée une correspondance entre les vecteurs d'un espace $A$ à un autre espace $B$. C’est juste une fonction.

Supposons que $A$ n'a que deux vecteurs, $\{v_1, v_2\}$ et le même pour $B$, $\{w_1, w_2\}$. Donc, il existe une **unique application linéaire** pour chaque possible manière unique de faire des correspondances entre les vecteurs de $A$ et $B$. Et donc, il existe une unique matrice qui décrit une unique application linéaire, il y a bijection.

<aside>
💡 On dit aussi que chaque A.L. est ***caractérisée*** par une unique matrice. **Si on connaît les coefficients, on connaît la A.L.**

</aside>

Il peut être vite fatigant de devoir faire des opérations mathématiques pour savoir quel vecteur $v$ de $A$ correspond à quel vecteur $w$ de $B$. Donc, c'est plus vite si on sépare chaque vecteur comme un produit des coordonnées et les vecteurs bases.

$$
f(x)=f\left(\sum_{i=1}^nx_ie_i \right)=\sum_{i=1}^nx_if(e_i)=\sum_{i=1}^nx_iv_i
$$

Après, on juste passe chaque vecteur base par la fonction. Les vecteurs résultants seront une base de l'image de $f(x)$.

<aside>
❗ **Attention** **!** Les vecteurs résultants ne sont pas forcément une base de tout $B$, juste la base de $\text{lm}(f)$. Ils pourrait être la base de $F$ si et seulement si $f(x)$ est surjective, car donc $\text{Im}(f) = B$, et si les vecteurs sont indépendants entre eux. Sinon, au moins la famille $\{f(e_1), ... , f(e_n)\}$ est génératrice.

</aside>

Deux notes pratiques :

- Il y a même des fois ou on ne peut pas computer tous les vecteurs, mais cela suffit avec les images des vecteurs bases.
- Notons que les scalaires des vecteurs bases de partie sont les mêmes de ceux d'arrivée !

## Rang, applications linéaires et théorème du rang

### Rangs et applications

Normalement, on parle de rang d'une famille de vecteurs comme la dimension de l'espace engendré de ce famille. C’est-à-dire, $\text{rg}(\{v_1, . . . , v_p\}) = \text{dim } \text{Vect}(\{v_1, . . . , v_p\})$.

Quand on parle du *rang d'une A.L*., on parle du rang de la image de $f$, qui est un sous-ensemble de l'ensemble d'arrivée ou codomaine. Notons que la famille de vecteurs composée de l'image de la base du départ engendre toute l'image de $f$. Donc, $\text{rg}(f) = \text{dim } \text{Im}(f) = \text{dim } \text{Vect}(\{f(e_1), . . . , f(e_n)\})$.

**Proposition**. Le rang est plus petit que la dimension de $E$ et aussi plus petit que la dimension de $F$, si $F$ est de dimension finie : $\text{rg}(f) \le \text{min}(\text{dim } E, \text{dim } F)$.

### Théorème du rang

Le théorème sous la forme original est $\text{dim } E = \text{dim Ker}(f) + \text{dim Im}(f)$. Cela dit, une autre écriture est $\text{dim }E = \text{dim Ker}(f) + \text{rg}(f)$.

Dans la pratique, cette formule sert à déterminer la dimension du noyau connaissant le rang, ou bien le rang connaissant la dimension du noyau. Normalement, on connaît la dimension de $E$.

## Application linéaire entre $E$ et $F$ de même dimension

Soit $f : E \mapsto F$ un isomorphisme (fonction bijective et linéaire) d’espaces vectoriels. Si $E$ (respectivement $F$) est de dimension finie, alors $F$ (respectivement $E$) est aussi de dimension finie et on a $\text{dim }E = \text{dim }F$.

- Une autre reformulation c'est : si $\text{dim }E = \text{dim }F$ et si $f$ est injective ou surjective.

## Matrices et applications linéaires

### Les applications linéaires écrites comme des matrices

À nouveau, une application linéaire est représentée par une ***unique*** matrice. On avait dit aussi que, si on passe une base de $E$ par la fonction, l'image de ce famille sera une base de $\text{Im}(f)$.

Mais, notons que finalement cette famille appartient à l'ensemble d'arrivée, $F$. Donc, on peut exprimer les images de la base de départ avec la base d'arrivée de manière ***unique***.

Dans la prochaine équation, on exprime l’image d’un vecteur $e_j$ de la base $B$, avec la base d’arrivé $B^\prime=(f_i)_{1\le i\le n}$ :

$$
f(e_j)=a_{1,j}f_1+a_{2,j}f_2+\dots+a_{n,j}f_n=\begin{bmatrix}a_{1,j}\\a_{2,j}\\\vdots\\a_{n,j}\end{bmatrix}_{B^\prime}
$$

<aside>
❗ **Attention !** On utilise la lettre $f$ pour la fonction/A.L. et aussi pour les vecteurs de la base $B^\prime$.

</aside>

La matrice d'application linéaire $f$ (par rapport aux bases $B$ et $B'$) est la matrice dont la $j$-ième colonne est constituée par les coordonnées du vecteur $f(e_j)$ dans la base $B^\prime=(f_i)_{1\le i\le n}$.

![image (1).png](image_(1).png)

En termes plus simples, c’est la matrice dont les vecteurs colonnes sont l’image par $f$ des vecteurs de la base de départ $B$, exprimée dans la base d’arrivée $B'$. On note cette matrice $\text{Mat}_{B,B'}(f)$.

Deux remarques à faire :

- La taille de la matrice $\text{Mat}_{B,B'}(f)$ dépend uniquement de la dimension de $E$ et de celle de $F$.
- Par contre, les coefficients de la matrice dépendent du choix de la base $B$ de $E$ et de la base $B'$ de $F$. On ne peut pas choisir les dimensions de $E$ et $F$, mais on peut bien choisir des bases différentes de chaque espace vectoriel.

### Opérations sur les matrices des A.L.

$\text{Mat}_{B,B'}(f)$ représente une matrice d'une application linéaire. Cela dit, les suivantes propositions sont vraies :

- $\text{Mat}_{B,B'}(f + g)$ = $\text{Mat}_{B,B'}(f)$ + $\text{Mat}_{B,B'}(g)$
- $\text{Mat}_{B,B'}(λf) = λ\cdot \text{Mat}_{B,B'}(f)$
- On dirait que $\text{Mat}_{B,B'}(f)$ est une application linéaire !
- Cela dit, $B$ et $B'$ doit rester fixés.

Aussi, et **la propriété la plus importante** : $\text{Mat}_{B,B'}(g \circ f) = \text{Mat}_{B,B'}(g) \cdot  \text{Mat}_{B,B'}(f)$, où $g\circ f = g\left(f(x)\right)$.

## Deux cas particuliers : endomorphismes et isomorphismes

### Matrice d’un endomorphisme : $E \mapsto E$

<aside>
⚠️ Avant d'aborder les A.L. plus connus exprimés en forme matricielle, un point sur la notation :

- Si on prend la même base dans l'ensemble de départ et arrivée, alors on note $\text{Mat}_B(f)$.
- Si on prend deux bases différentes dans le même ensemble, alors on note $\text{Mat}_{B,B'}(f)$ pour deux bases $B$ et $B'$.
- Notons aussi que la taille de la matrice est toujours carrée dans cette section.
- **Propriété**. Si $f$ est un endomorphisme, alors $\text{Mat}_B(f^p) = (\text{Mat}_B(f))^p$, où $f^p$ est $f$ composée avec elle même $p$ fois. Ceci est juste une reformulation de la équivalence de composition/multiplication des matrices de A.L.
</aside>

- **Identité** : $\text{Mat}_B(f) = I_n$. 
Évident, car on prend la même base en départ/arrivée.
Mais ce n'est plus vrai si on a deux bases différentes !
- **Homothétie** : $\text{Mat}_B(f) = λ\cdot I_n$. 
Évident, une homothétie escalade les composants du vecteur.
- **Symétrie centrale** : $\text{Mat}_B(f) = -I_n$. 
Une symétrie central est une homothétie avec $λ = -1$.
- **Réflexion par rapport à la fonction ou axe de symétrie $y = x$** :
    
    $$
    \text{Mat}_B(f)=\begin{bmatrix}0&1\\1&0\end{bmatrix}
    $$
    
- **Rotation (de $\theta$ radians) :**
    
    $$
    \text{Mat}_B(f)=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}
    $$
    
    - Particulièrement, quand il y a $p$ rotations à la suite…
        
        $$
        \text{Mat}_B(f^p)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
        $$
        

### Matrice d'un isomorphisme : $f$ bijective et linéaire

$f$ est bijective (et donc isomorphe, parce que l’espace d’applications linéaires et un espace vectoriel et donc vérifie la propriété de linéarité) si et seulement si la matrice $\text{Mat}_{B, B’}(f)$ est inversible.

- Bijectivité $\iff$ Inversibilité.

De plus, si $f : E \mapsto F$ est bijective, alors la matrice de l’application linéaire $f^{−1} : F \mapsto E$ est la matrice $(\text{Mat}_{B,B'}(f))^{-1}$. Pour le déduire, par l’équivalence composition/multiplication, on observe facilement que $\text{Mat}_{B,B'}(f^{-1}) = (\text{Mat}_{B,B'}(f))^{-1}$.

# Changement de bases

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