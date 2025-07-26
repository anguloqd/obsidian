# 03 // théorie des graphes

# Introduction

[Slides de théorie de graphes](slides_graphes_minfo_annote2.pdf)

## Définition intuitive et formelle d’un graphe (orienté)

On introduit le concept d’un graphe avec un exemple : un site internet est composé de cinq pages notées $A$, $B$, $C$, $D$ et $E$. En un clic, on peut passer d’une page à certaines autres selon les possibilités suivantes.

- De la page $A$, on peut passer en un clic aux pages $C$ et $E$.
- De la page $B$, on peut passer aux pages $A$ et $D$.
- Depuis la page $C$, on peut accéder à la page $B$ ou rester sur $C$.
- Quand on est sur la page $D$, on peut seulement aller sur la page $C$ et de la page $E$, on ne peut aller que sur la page $A$.

![Graphique sagittal.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled.png)

Graphique sagittal.

Un graphe est une tuple $G=\{V,E\}$. Les points ou nœuds sont appelés des *sommets* et son ensemble est noté $V$, et les flèches orientés sont appelées des *arcs* et son ensemble est $*E*$. 

Par rapport à la notation, les sommets sont simplement notés avec de lettres comme $V=\{a_0, a_1, \dots, a_n\}$, tant que les arcs sont notés comme des couples de $E$ comme $E=\{(a_1,a_2),(a_3,a_5),(a_7,a_{11})\}$ pour dire qu’il existe un arc qui part du sommet $a_3$ pour arriver au sommet $a_5$, par exemple.

# Matrice d’adjacence

## Définition et exemple

Pour formaliser une certaine configuration de sommets et d’arcs d’un graphe $G$, on utilise une matrice dite *d’adjacence*. Cette matrice compte les chemins allant du sommet en ligne au sommet en colonne.

Pour le graphe précédent, on obtient cette matrice d’adjacence :

![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_1.png)

$$
M_G=\begin{bmatrix}
0&0&1&0&1\\
1&0&0&1&0\\
0&1&1&0&0\\
0&0&1&0&0\\
1&0&0&0&0
\end{bmatrix}
$$

Si on ajoutait un autre chemin allant de $D$ à $C$, on changerait l’entrée $(4,3)$ à $2$ pour compter le total des chemins.

On peut définir aussi les ensembles de successeurs et de prédécesseurs d’un sommet donné. Pour $A$, on note ses successeurs $\Gamma^+(A)=\{C,E\}$ et ses prédécesseurs $\Gamma^-(A)=\{B,E\}$.

## Chemin et longueur dans un graphe orienté

Un chemin est défini formellement comme une suite de sommets tel qu’un tout sommet est successeur du sommet précédent, à exception du premier sommet.

$$
\text{Il y a un chemin }v_a\text{-}v_z \text{ de longueur }n-1 \iff \exists(\{v_i\}_{i=0}^n): \\
v_i\in V,(v_i,v_{i+1})\in E, v_0=v_a, v_n=v_z
$$

- Un chemin élémentaire ne passe pas deux fois par un même sommet.
    - Un chemin *hamiltonien* passe une seule fois par tous les sommets du graphe.
- Un chemin simple ne passe deux fois par un même arc.
- Un *circuit* est un chemin dont le sommet de départ et d’arrivé sont le même sommet.

<aside>
❗ Comme conséquence de cette définition, **il existe toujours un chemin de longueur $0$ d’un sommet à lui-même, sans besoin de le connecter à lui-même avec un arc**.

Pour un graphe avec un seule sommet connecté à lui-même, le chemin de longueur plus courte est $0$, càd. de ne pas bouger du sommet. La chemin de ce sommet à lui-même passant par la boucle est de longueur $1$.

![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_2.png)

</aside>

Notons déjà qu’un chemin de longueur $1$ est tout simplement un arc, qui sont notés dans la matrice d’adjancence. Deux sommets sont *adjacents* s’il sont connectés par un arc. Une propriété intéressante de telle matrice est qu’on peut en déduire les chemins de longueur $n$ générale avec l’opération $M^n$. 

![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_1.png)

$$
M=\begin{bmatrix}
0&0&1&0&1\\
1&0&0&1&0\\
0&1&1&0&0\\
0&0&1&0&0\\
1&0&0&0&0
\end{bmatrix}\\
\text{}\\
M^2=\begin{bmatrix}
1&1&1&0&1\\
0&0&2&0&1\\
1&1&1&1&0\\
0&1&1&0&0\\
0&0&1&0&1
\end{bmatrix}
$$

Il y a, par contre, de choses importantes à remarquer :

- $M^n$ donne la matrice des chemins de **longueur strictement égale à $n$**, et non pas de longueur inférieur ou égale à $n$.
- Partant de $A$ jusqu’à $B$, il n’existe pas un chemin de longueur 1 mais de longueur 2.
- Partant de $A$ jusqu’à $E$, il existe un chemin de longueur 1, mais pas de longueur 2.
- Partant de $B$ jusqu’à $C$, il existe **deux** chemins de longueur 2 !

## Fermeture transitive

La fermeture transitive est un opération qui prend un graphe et retourne un autre graphe. En particulier, s’il existe un chemin partant de $v_i$ à $v_j$ de n’importe quelle longueur, on rajoute un arc direct $(v_i,v_j)$. 

![Graphe de départ à gauche, sa fermeture transitive à droite.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_3.png)

Graphe de départ à gauche, sa fermeture transitive à droite.

En particulier, pour déterminer la fermeture transitive $\tilde{M}_G$ un graphe $G$ à $n$ sommets, l’opération est comme suit :

$$
\tilde{M}_G= M_G\oplus M^{[2]}_G\oplus\dots\oplus M^{[n]}_G=\bigoplus_{i=0}^n M^{[i]}_G
$$

Où $\oplus$ est l’addition booléenne et $M^{[n]}$ est la $n$-ième puissance booléenne de $M$.

- $M^{[n]}$ reemplace chaque entrée $m_{ij}$ avec $0$ si $m_{ij} = 0$ et $1$ si $m_{ij} > 0$.
Basiquement, nous dit s’il existe au moins un chemin entre deux sommets si $1$ et $0$ sinon.
- L’addition booléenne $a\oplus b$ est $0$ si $a+b=0$, et $1$ si $a+b>0$.

Donc, pour ce graphe $G$ :

$$
M_G^{[1]}=
\begin{bmatrix}
0&1&0\\
1&0&1\\
0&0&0
\end{bmatrix},\space
M_G^{[2]}=
\begin{bmatrix}
1&0&1\\
0&1&0\\
0&0&0
\end{bmatrix},\space
M_G^{[3]}=
\begin{bmatrix}
0&1&0\\
1&0&1\\
0&0&0
\end{bmatrix}
\\
\text{}
\\
\tilde{M}_G=M^{[1]}\oplus M^{[2]}\oplus M^{[3]}=
\begin{bmatrix}
1&1&1\\
1&1&1\\
0&0&0
\end{bmatrix}
$$

Finalement, chaque entrée de $\tilde{M}_G$ devrait s’interpreter comme s’il existe au moins un chemin de taille égale ou inférieur à $n$ qui va de $v_i$ à $v_j$ si $\tilde{m}_{ij}=1$, et $0$ sinon.

# Graphes non-orientés

## Définition

En différence avec les graphes orientés, les arcs d’un graphe non-orienté pourrait être considérés bidirectionnels. Il n’est plus important la direction, mais la connexion entre deux sommet. Comme ça, on n’a plus besoin de spécifier la direction de chaque arc.

![Un graphe oriente.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_4.png)

Un graphe orienté.

![Le même graphe, mais non-oriente.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_5.png)

Le même graphe, mais non-orienté.

Le vocabulaire des graphes non-orientés change par rapport à ceux orientés : les chemins sont appelés des *chaînes* ; les chemins élémentaires (dont *hamiltoniens*) et simples sont les chaînes élémentaires et simples ; et, parfois, les arcs dans les graphes non-orientés sont appelés *arêtes*.

Pour déduire la matrice d’adjacence $M_{G^\prime}$ d’un graphe non-orienté à partir de celle d’un graphe orienté, on le fait en deux parties :

1. On inverses **toutes** les directions du graphe orienté, ce qui serait la même chose que transposer $M_{G}$, donc on obtient un graphe dont la matrice d’adjacence est $M_G^t$.
2. On l’additione avec la matrice du graphe original, pour obtenir celle du graphe orienté.
On notera qu’on a été obligé d’orienter deux fois la boucle sur $C$, d’où le coefficient $2$ sur la diagonale. Aussi, la matrice $M_{G^*}$ est symétrique (par rapport à la diagonale).
    
    $$
    M_{G^*}=M_G+M_{G}^t
    $$
    

Un sommet $v$ est dit **connexe** si, pour tous les autres sommets $w$ ($w\ne v$), il existe une **chaîne** (équivalence de chemin d’un graphe non orienté) reliant $v$ à $w$. Bref, à partir de $v$, on peut arriver à tout autre sommet du graphe. Un graphe est **connexe** si tous ses sommets sont connexes.

## Arbres

Un arbre est un graphe non-orienté qui est connexe, mais aussi qui est *acyclique*, càd. qui ne possède pas de *cycles*. Un cycle est juste la notion de circuit mais pour dans les graphes non-orientés.

En d’autres termes, un arbre est un graphe non-orienté où pour toute couple de sommets $(v_i,v_j)$, il existe **strictement et exactement** une seul chaîne qui les connecte. Ceci implique qu’une chaîne d’un sommet vers lui-même peut être coupé en deux : une “sous-chaîne” où on s’éloigne du sommet et une autre chaîne où on revient au sommet. La deuxième chaîne est l’inverse de la première.

Dans l’exemple dessous, si on pars et revient à $6$ passant par $2$, on va en premier à $2$ et puis on fait exactement la sous-chaîne inverse.

![Un arbre.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_6.png)

Un arbre.

[Cycle (graph theory)](https://en.wikipedia.org/wiki/Cycle_(graph_theory))

[Connectivity (graph theory)](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_vertices_and_graphs)

[Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_(graph_theory))

## Graphes pondérés

Un graphe pondéré est un graphe dont les arcs ont des valeurs correspondants. On défini aussi la “valeur” d’un chemin de $v_i$ à $v_j$ comme la somme des valeurs de arcs qui le composent. **Le graphe pondéré peut-être orienté ou non-orienté**.

![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_7.png)

Par exemple, dans ce graphe pondéré :

- Le chemin $(B,A,E,C)$ vaut $4+3+5=12$
- Le chemin $(B,D,E,C)$ vaut $7+4+5=16$
- Le chemin $(B,D,C)$ vaut $7+8=15$

Parmi ces chemins, le chemin minimal est (1) et le maximal est (2).

## L’algorithme de Dijkstra : recherche du chemin le plus court

Avant de commence, le terme “distance” dans le contexte de l’algorithme de Dijkstra est juste la valeur de l’arc qui connecte un sommet avec un autre, et non pas la longueur d’un chemin. On pourrait penser que la valeur d’un arc représente les kilomètres entre les deux sommets.

<aside>
💻 En reformulant plus simplement :

1. On marque tous les sommets comme non visités.
2. On donne à tous les sommets une distance provisoire : $0$ au sommet source et $\infin$ aux autres. Aussi, on marque le sommet source comme sommet courant.
3. Pour tous les voisins non visités du sommet courant :
    1. On calcule la distance à travers le sommet courant (distance accumulé depuis le sommet source + la distance du passage direct).
    2. Si cette nouvelle distance est plus courte que la distance provisoire existante, on la remplace et on garde en tête le chemin qui la produit, sinon on garde la précédente.
4. Quand on ait fini, on marque le sommet courant comme visité.
5. On vérifie si le sommet destination a été marqué visité.
    1. Si oui, on arrête, on a fini l’algorithme.
    2. Sinon, on marque comme sommet courant celui qui n’est pas encore marqué comme visité et qui a la distance provisoire la plus petite. **On répète dès l’étape 3**.
</aside>

**Note** : un axiome courant en mathématiques dit que si on a le chemin le plus court entre un point et un autre, alors, si on prend un point de ce chemin, la suite du chemin est encore le chemin le plus court de ce point vers l’extrémité.

[Dijkstra&#039;s algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)

### Exemple

1. Sur un graphe pondéré, orienté ou non, on se donne un sommet d’entrée (sommet source), disons $A$. On fixe la distance à lui-même à $0$.  On gardera en tête les sommets visités et les non-visités. On marque le sommet $A$ comme le sommet courant et comme sommet visité.
    
    ![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_8.png)
    
2. Pour tous les sommets différents de la source, on marque que leur distance provisoire est infinie. On la marque sur les sommets.
    
    ![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_9.png)
    
3. Pour chaque successeur non visité de $A$ ($B$,$D$ et $E$), on compare si la distance directe (la valeur de l’arc que les connecte) est plus petite que leur distance provisionnelle. On garde la distance la plus petite entre les deux comme la ***nouvelle* distance provisoire**.
    
    ![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_10.png)
    
4. On marque $A$ comme sommet visité, sa distance provisoire comme distance plus courte définitive, on le rougit (c’était déjà rougit mais quand même) et on recommence sélectionnant le sommet non visité avec la distance provisoire la plus petite, dans ce cas $E$. Le voisins non visité de $E$ est juste $D$.
    1. Dans ce cas, la somme de la distance cumulée ($6$) et la distance directe ($3$) est plus petite que la distance provisoire de $D$ ($10$) $(A,E,D)=9$ est plus court que $(A,D)=10$, donc on rougit $E$ et **on le redonne une nouvelle distance provisoire**.
    2. Pour B, la distance plus courte est la distance directe. On ne les rougit pas.
    3. On marque sur les sommets successeurs directes leurs distances plus courtes et **finalement on marque les successeurs comme des sommets visités**. Leurs distances provisoires à ce moment là deviennent leurs distance plus courtes à partir du sommet source ($A$). Notons que sur $D$, la distance plus court est $9$ (passant par $E$) et non pas $10$ (passage directe).
    
    ![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_11.png)
    
5. On répète avec tous les autres sommets non-visités jusqu’à arriver à notre sommet destination.
    1. Pour $C$, on cherche ses prédécesseurs directes qui sont aussi visités ($F$ est prédécesseur mais pas visité encore, donc on ne le considère pas). Après, on cherche le minimum à partir de ces sommets, comptant la distance depuis $A$ et ajoutant la distance directe à $C$.
        1. Pour $B$, ça serait $7+7=14$.
        2. Pour $D$, ça serait $9+2=11$. Il est le chemin le plus court.
        3. Le chemin le plus court de $A$ à $C$ est donc $(A,E,D,C)$.
        4. On marque $C$ comme visité et on rougit le prédécesseur qui a minimisé la distance, càd. $D$.
    2. De même pour $F$, cette fois connaissant la distance la plus courte à $C$. Ses prédécesseurs visités sont $C$ et $D$.
        1. $C$ est de distance directe $5$ et distance cumulée $11$. Donc, la distance du chemin plus court de $A$ à $F$ passant par $C$ est $5+11=16$.
        2. $D$ de distance directe $9$ et distance cumulée $9$ aussi. Donc, la distance du chemin plus court de $A$ à $F$ passant par $D$ est $9+9=18$.
        3. Passer par $C$ donne un chemin plus courte. Donc, on donne à $F$ comme distance plus courte $16$, on le marque visité et on rougit le prédécesseur qui a minimisait la distance, càd $C$.
    
    ![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_12.png)
    
6. Si on arrive marque visité notre sommet destination, on le rougit et on a fini l’algorithme.

# Ordonnancement

[Slides d’ordonnancement](slides_ordonnancement_minfo_annote.pdf)

## Dessin d’un graphe par niveaux

On peut dire qu’un sommet dans un graphe est de niveau $0$ s’il n’as pas de prédécesseur dans l’ensemble de sommets $S$. L’ensemble de sommets de niveau 0 est noté $S_0$. Ayant défini $S_0$, on peut définir $S_n$ récursivement comme suit :

$$
S_n = S - S_{n-1}
$$

![Cette méthode écrire, de gauche à droite, les sommes de $S_0$ jusqu’à $S_n$ resulte en des graphes bien ordonnés comme celui-ci.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_13.png)

Cette méthode écrire, de gauche à droite, les sommes de $S_0$ jusqu’à $S_n$ resulte en des graphes bien ordonnés comme celui-ci.

Le but de l’ordonnancement, si on voit les sommets comme des tâches, est de parcourir toutes les tâches du graphe par niveau. Par exemple, pour $E$, les tâches $BDA$ doivent être faites.

## MPM : Méthode des potentiels metra

La réalisation d’un projet passe par l’exécution de différentes tâches, de durées souvent différentes. Si certaines tâches peuvent être réalisées simultanément, d’autres nécessitent que certaines tâches aient été réalisées antérieurement. Faire l’ordonnancement d’un projet consiste à organiser ce projet en respectant les contraintes d’antériorité des tâches tout en minimisant la durée totale de réalisation.

<aside>
❗ La méthode MPM (Méthode des potentiels metra) permet l’ordonnancement de projets, c’est la méthode que nous exposerons dans ce cours. Nous aurions pu choisir la méthode PERT, mais elle est plus complexe à mettre en oeuvre.

</aside>

Reprenons le graphe précédente, on l’ajoute un sommet “fin” après $C$ et, à chaque arc, on ajoute un numéro qui représentera les unités de temps pour compléter la tâche et passer à la suivante.

![untitled](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_14.png)

Ayant ce graphe comme base, on va s’intéresser à construire deux indicateurs :

- Date au plus tôt : la date à laquelle on peut démarrer une tâche **sans en avoir raté**.
- Date au plus tard : la date la plus tardive à laquelle on peut démarrer une tâche sans **retarder le projet**.

On doit en premier calculer les dates au plus tôt des toutes les tâches pour pouvoir construire la date au plus tard.

### Date au plus tôt : $t(X)$

On denote la date au plus tôt du sommet $B$ comme $t(B)$. En plus, on notera par la suite la durée du passage d’une tache à une autre comme $d(B,D)$ (le cas de la durée de $B$ à $D$, par exemple). On note que $d(X,X)=0$.

1. On fixe un indice $i=0$. On commence en évaluant $t(s_0)$, pour tous les sommets $s_0$ de $S_0$. Trivialement, on peut les commencer immédiatement car elles sont les toutes premières tâches, donc $\forall s_0 \in S_0,\hspace{4pt} t(s_0) = 0$.
2. On passe à $i=1$, on calcule $S_1 = S - S_0$. Pour $D$ et $A$, on voit que la seule manière de les commencer c’est de passer par B, donc $t(D) = d(B,D) = 2$ et $t(A) = d(B,A)=2$.
3. On voit que $t(E)=\min\big(t(D)+d(D,E), t(A)+d(A,E)\big)$. C’est-à-dire, la date au plus tôt des tâches prédécesseuses plus leurs distance à $E$. On déduit que $t(E)=7$, passant de D à E. 
4. En general, si $\Gamma^-(X)$ est l’ensemble de prédécesseurs d’un sommet $X$, donc : 
    
    $$
    t(X)=
    \begin{cases}
    0, \text{ si } X\in S_0
    \\
    \max\big( \{t(s^-_X)+d(s^-_X,X): s^-_X \in \Gamma^-(X)\} \big), \text{ sinon }
    \end{cases}
    $$
    
5. Quand on arrive à la fin, $t(\text{fin})=14$, le projet dure $14$ jours au mieux sans raté aucune tâche).

### Date au plus tard : $T(X)$

Maintenant, on va calculer la date au plus tard. La différence ici c’est qu’on commence dès la fin jusqu’àux premiers tâches du projet. On rappelle que la date au plus tard est la date la plus tardive où on commence une tâche sans retarder le projet, càd de sorte que toutes les tâches du niveau précédent soient complètes (même si les tâches du niveau courant ne le sont pas).

On lance un indice $i=0$ et on fixe $n$ comme la quantité des niveaux de tâches en total, tout ça pour construire l’indice qui nous intéresse : $j = n-i$.

1. Si on commence par la fin du projet, donc $j=5$. On note que $T(\text{fin})=t(\text{fin})=14$. Bien évidemment, la seule date à laquelle on peut atteindre la fin du projet c’est d’avoir complété toutes les tâches.
2. On passe à $j=4$, le sommet $C$. La date la plus tardive est donc $T(C)=T(\text{fin})-d(C,\text{fin})=14-4=10$.
3. Pour $j=3$ c’est le sommet $E$. Même chose : $T(E)=T(C)-d(E,C)=10-3=7$.
4. Pour $j=2$, on parle de $D$ et $A$. On commence par $A$. La chose intéressante ici c’est que on devra voir tous les successeurs de $A$ : $C$ et $E$, donc $T(A)=\min\big(T(C)-d(A,C),\hspace{2pt}T(E)-d(A,E)\big)$. On déduit aussi que $T(D)=2$.
5. En général, si $\Gamma^+(X)$ est l’ensemble de prédécesseurs d’un sommet $X$, donc :

$$
T(X)=
\begin{cases}
t(\text{fin}), \text{ si } X=\text{fin}
\\
\min\big(\{T(s^+_X)-d(X,s^+_X):s^+_X \in \Gamma^+(X)\}\big), \text{ sinon}
\end{cases}
$$

### Graphique final et la marge d’une tâche

![Pour chaque tâche, on nota sa date au plus tôt dans la casse gauche et sa date au plus tard dans la casse droite.](new/uga/l2/s4/math/s4_math_math_pour_l’info/03_theorie_des_graphes/untitled_15.png)

Pour chaque tâche, on nota sa date au plus tôt dans la casse gauche et sa date au plus tard dans la casse droite.

La marge d’une tâche est la différence entre sa date au plus tôt et sa date au plus tard. Si la marge d’une tâche est $0$, on dit que la tâche est *critique*. Un chemin critique est un chemin ne contenant que des tâches critiques, comme $BDEC$ par exemple.

En soi, le chemin critique n’est pas tangiblement important, mais il doit servir de référence pour l’organisation du projet. **Aucune tâche ne peut être retardée sans impliquer un retard de fin du projet**. Imaginons deux manières de faire le projet : $BD+BAEC$ et $BA+BDEC$. La première manière prend moins de temps ($14$) que la deuxième ($16$).

Le chemin le plus vite est tel que, à chaque tâche qu’on soit, on prend la tâche critique parmi les tâches successeuses.