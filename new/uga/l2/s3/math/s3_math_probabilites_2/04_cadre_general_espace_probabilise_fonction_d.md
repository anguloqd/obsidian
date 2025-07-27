# 04 // cadre général : espace probabilisé, fonction de répartition et de densité

# Espace probabilisé

## Préparation : $\sigma$-algèbre

Une $\sigma$-algèbre ou tribu sur un ensemble $\Omega$ est un ensemble $\mathcal{A} \subset \mathcal P(\Omega)$ qui vérifie les trois propriétés suivantes. Notons que $A$ est un sous-ensemble de $\mathcal A$.

1. $\Omega \in \mathcal A$, où $\Omega$ est considéré l’univers dans le contexte
2. Stabilité par la complémentation : $A \in \mathcal A \implies A^c \in \mathcal A$
3. Stabilité par l’union dénombrable ($\sigma$-additivité) : si $(A_i)_{i \ge 1} \in \mathcal A$, alors $\bigcup_{i \ge 1} A_i \in \mathcal A$.

Appliquant les lois de De Morgan avec les propriétés 2 et 3, on arrive a la stabilité par l’intersection dénombrable, car $\left( \bigcup_{i≥1} A_i \right)^c = \bigcap_{i≥1} A_i^c$.

Les deux $\sigma$-algèbres les plus basiques et extrêmes sur $\Omega$ sont $\{\empty, \Omega\}$ et $\mathcal P (\Omega)$. Toute autre $\sigma$-algèbre reste sur ces deux extrêmes.

### Propositions

**Lemme**. L’intersection de deux $\sigma$-algèbres est un $\sigma$-algèbre sur $\Omega$.

Soit $C \in \mathcal P(\Omega)$. Il existe une plus petite $\sigma$-algèbre sur $\Omega$ contenant $C$. On l’appelle la $\sigma$-algèbre engendrée par $C$ et on la note $\sigma(C)$. C’est, en fait, l’intersection des toutes les $\sigma$-algèbres qui contiennent $C$.

En langage naturel, $C$ est un événement, et on cherche la plus petite $\sigma$-algèbre sur les résultats qui contient l’événement.

## Définition des espaces probabilisés : $\{\Omega, \mathcal A, \mathbb P\}$

Pour toute la suite, on ne se limite pas à juste parler de V.A. entières mais aussi de V.A. réelles. Pour cela, il faut présenter les axiomes de la manière suivante, et en l’accompagnant d’un exemple avec un dé.

Un espace probabilisé est un concept mathématique pour modeler une expérience aléatoire, représenté comme un triplet $\{ \Omega, \mathcal{A}, \mathbb{P} \}$.

- $\Omega$ : l’univers, ou l’ensemble des *résultats* de l’expérience. Pour un dé. : $\{1,2,3,4,5,6\}$.
- $\mathcal{A}$ : une tribu, $\sigma$-algèbre ou simplement l’ensemble d’*événements*. Chaque membre de cet ensemble est formellement un “événement”, **qui est différent des “résultats”** de $\Omega$. Normalement, on prend comme $\mathcal{A}$ l’ensemble des parties de $\Omega$, c’est-à-dire $\mathcal{P}(\Omega)$.

Par exemple, un événement peut être simplement que le dé montre $2$, dans ce cas $\{2\} \in \mathcal{A}$, mais aussi que le dé montre un nombre pair, donc $\{2,4,6\} \in \mathcal{A}$.
- $\mathbb{P}$ : la loi de probabilités ou mesure de probabilité, qui est une fonction qui associe une probabilité à chaque événement—formellement $\mathcal{A} \mapsto [0,1]$— et qui vérifie $\mathbb{P}(X\in\Omega)$ = 1 et $\mathbb P \left( \bigcup_{i≥1} A_i \right) = \sum_{i≥1} \mathbb{P}(A_i)$, supposons que les A_i sont 2-à-2 disjoints. Ceci implique que la fonction ou application $\mathbb P$ est $\sigma$-additive.

Continuant avec l’exemple, si on suppose un dé non-pipé, donc $\mathbb{P}(X \in \{2\})=\frac{1}{6}$ et $\mathbb{P}(X \text{ pair}) = \mathbb{P}(X \in \{2,4,6\}) = \frac{1}{2}$.

> [!note]
> Lorsqu’une expérience est conduite, on imagine que la “nature” “sélectionne” un **résultat** unique $\omega$ de l’univers $\Omega$, supposons $\omega = 2$. Tous les **événements** de $\mathcal{A}$ qui contiennent le **résultat** $\omega$ sont dit *produits*. Par exemple, l’événement “le dé montre $2$” s’est produit, mais l’événement “le dé montre un nombre pair” s’est aussi produit, et de même pour l’événement “le dé montre un nombre premier”, car $2$ est premier.
>
> Cette "sélection" se produit de telle manière que, si l'expérience se répétait plusieurs fois, le nombre d'occurrences de chaque événement comme fraction du nombre total d'expériences conduites tendrait très probablement vers la probabilité attribuée à cet événement par la fonction de probabilités $\mathbb{P}$. Ceci c’est juste la loi des grands nombres.

On peut se demander pourquoi ne pas choisir un autre $\mathcal{A}$ différent de $\mathcal{P}(\Omega)$. Pour le cas où $\Omega$ est dénombrable, on peut se contenter toujours faisant cette choix de $\mathcal{A}$.

Par contre, pour le cas non dénombrable comme $\Omega = \R$, si on définissait $\mathcal{A}=\mathcal{P}(\R)$, il serait faux que choisir un sous-ensemble quelconque de $\Omega$ soit un événement. Ceci est hors du cours, mais c’est une conséquence du théorème d’Ulam.

Pour cette raison, dans le cas non dénombrable, $\mathcal{A} \subset\mathcal{P}(\Omega)$  et non $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ comme dans le cas dénombrable.

## Propriétés des probabilités

> [!note]
> Pour simplicité de notation, on note simplement $\mathbb P(a\in A) = \mathbb P(A)$.
> $a$ est une variable d’intérêt dont on parle souvent, donc ce n’est pas nécessaire de la mentionner tout le temps. $A$ peut être un ensemble ou un intervalle.

### Propriétés basiques

- $\mathbb P (\empty) = 0$.
- $\mathbb P (A^c) = 1 - \mathbb P (A)$.
- Additivité simple : $\mathbb P \left( \bigcup_{i=1}^n A_i \right) = \sum_{i=1}^n \mathbb P (A_i)$. Il faut que les $A_i$ soient disjoints.

### D’autres propriétés

**$\sigma$-additivité d’intervalles**. Imaginons que notre espace d’événements $\mathcal A$ contient des intervalles, qu’on notera $B_n$. On en prend une famille d’intervalles et on imagine que les intervalles devient de plus en plus grandes, c’est-à-dire, le prochain intervalle contient l’actuel, ou $B_n \subset B_{n+1}$.  Donc :

$$
\mathbb P \left( \bigcup_{n \ge 1} B_n\right ) = \lim_{n \rightarrow \infin} \mathbb P(B_n)
$$

En outre, et ignorant la condition d’agrandissement du prochain intervalle $B_{n+1}$, on a la propriété suivante. Elle n’est pas une égalité stricte car il se peut que les $B_n$ ne soient pas disjoints.

$$
\mathbb P \left( \bigcup_{n \ge 1} B_n\right ) \le \sum_{n \ge 1} \mathbb P (B_n)
$$

# Fonction de répartition : $F_X(x)$

## La probabilité accumulée jusqu’à un certain point $t$

Soit $\mathbb P$ une loi de probabilité sur $\R$. On définit une fonction de répartition $F$ comme :

$$
F_X(t) = \mathbb P(X\le t)
$$

Étant donné que les probabilités sont toujours entre $0$ et 
$$, et que la somme de toutes les probabilités est $1$ est la somme d’aucune est $0$, on conclut que $F$ est croissante et borné entre $0$ et $1$.  En plus, on ajoute une possibilité d’être ***continue à droite*** (càd. si elle présente des sauts, le point où se produit le saut sera inclut dans le prochain échelon et pas l’actuel).

Toutes ces propriétés permettent de définir une autre unique fonction ou loi de probabilité $f$.

# Fonction de densité : $f_X(x)$

## Presque identique à une loi de probabilité

### Motivation

Dans le cadre dénombrable, on avait une fonction appelée “loi de probabilité” $\mathbb P$ qui assigne chaque valeur possible d’une expérience aléatoire avec une probabilité. Elle nous permet de dire que “la probabilité de l’expérience $X$ résulte en $x$ est $\mathbb P(X=x)$, ou que la probabilité qu’elle soit contenu dans un intervalle $[a,b]$ est $\mathbb P(a \le X \le b)$”.

Dans le cadre générale, ceci n’est plus le cas. Particulièrement, on ne peut pas parler de la probabilité que $X$ soit exactement égal à $x$, car pour tout $x$, $\mathbb P(X=x)=0$, car il y a une infinité de valeurs que $X$ peut prendre. On peut, par contre, parler d’une probabilité de que $X$ soit contenu dans un intervalle, qui serait donné comme suit :

$$
\mathbb P(a \le X  \le b)  \iff F_X(b)-F_X(a)
$$

Pourquoi on se souci de faire remarquer tout ça ? **Parce qu’il ne faut pas penser que la fonction de densité est la même chose que la loi de probabilité**, que c’est un erreur que j’ai déjà fait. Il peut être utile penser que la fonction de densité parle des “probabilités relatives” tant que la fonction de répartition parle des “probabilités absolues ou réelles”.

### Définition et conditions

Pour définir une fonction de densité, on part du principe qu’on peut déterminer (ou on connaît déjà) sa fonction de répartition. Particulièrement, s’il existe une telle fonction $f_X(x)$ qui vérifie le condition suivante en bas, $f_X(x)$ est donc la fonction de densité de $\mathbb{P}$.

$$
\underbrace{F(t)}_{\mathbb P(X\le t)}=\int_{-\infin}^tf_X(x)dx
$$

**Note**. Il se peut, parfois, que la fonction de répartition existe tant que la fonction de densité non !  Une condition pour que la densité existe est $\lim_{x \longrightarrow \epsilon} \int_{-\epsilon}^{\epsilon} f(x)dx = 0$. La source de problèmes est normalement que la fonction de répartition $F$ est discontinue.

La fonction de densité a quelques similitudes avec la loi de probabilité d’une V.A. dénombrable. Particulièrement, il faut qu’elle vérifie les deux axiomes d’une loi de probabilité : quelle soit toujours positive et que la somme de probabilités soit égale à $1$.

$$
\forall x\in \R,\hspace{4pt} f_X(x)\ge0 \space\text{ et }\space\int_\Omega f_X(x)dx = 1
$$

Ici, $\Omega$ est un ensemble des valeurs que la variable aléatoire $X$ peut prendre.

# Propriétés généralisées du cas dénombrable

Les propriétés et notions suivantes se généralisent aussi du cas dénombrable au cadre général: **probabilité conditionnelle, indépendance, espérance et moments**.

## Par rapport à l’espérance

Par la suite, on va s’intéresser juste aux [V.As](http://V.As) qui ont admettent une fonction de densité. Donc, l’espérance d’une telle V.A X serait comme suit :

$$
\mathbb{E}[X]=\int_\Omega \ x\cdot f_X(x)\space dx
$$

Un outil pour le calcul de l’espérance, même si elle n’as pas de densité, est le suivant : soit $X$ une V.A. réelle, on peut la décomposer dans sa partie positive et négative comme suit.

$$
X = X^+-X^-, \text{ où } X^+=\max(X,0) \text{ et }X^-=-\min(X,0)

\\
\\

\text{Par linéarité de l'espérance, } \mathbb{E}[X] = \mathbb{E}[X^+] - \mathbb{E}[X^-]
$$

L’utilité de cette décomposition est que si $\mathbb{E}[X^+]$ ou $\mathbb{E}[X^-]$ n’existe pas, $\mathbb{E}[X]$ non plus.

On garde aussi la linéarité et la multiplicativité de l’espérance (cette dernière si $X_1$ et $X_2$ sont des V.A. indépendantes).

### Espérances des fonctions de $X$ : on garde le domaine $\Omega_X$ et la densité $f_X$

Pour calculer une espérance, on doit résoudre une intégrale défini dont l’intégrande (membre de l’intégrale ou la fonction à intégrer) est un produit : une variable et sa fonction de densité, normalement.

Par contre, si on veut calculer l’espérance d’une fonction de la V.A. $X$, il faut appliquer telle fonction à la variable dans l’intégrande en gardant toujours la densité de la V.A. originale $X$, et non pas voyant la densité de la fonction de la V.A $X$. Supposons qu’on veut déterminer l’espérance de $e^X$, donc :

$$
\begin{array}{ll}
\text{Manière correcte : } 
&
\mathbb E [e^X] = \int_{\Omega_X} (e^x) \cdot f_X(x) \space dx
\\[5pt]
\text{Manière incorrecte : } 
&
\mathbb E [e^X] = \int_{\Omega_{e^X}} (e^x) \cdot f_{e^X}(x) \space dx
\end{array}
$$

Les deux différences sont le change de $\Omega_X$ à $\Omega_{e^X}$ et le change de $f_X(x)$ à $f_{e^X}(x)$. En définitive, l’espérance suppose **contextuellement** qu’on garde le domaine de définition de l’intégrale $\Omega_X$ et la densité de la V.A. $f_X$. Quand on calcule une espérance, c’est une bonne pratique de se demander par rapport à quelle densité $f$ et à quel domaine $\Omega$.

On pourrait, effectivement, déduire une densité $f_{e^X}$ et un domaine de définition $\Omega_{e^X}$, mais cela on va l’explorer dans la dernière section de cette note.

## Par rapport à la variance

Supposant encore que les V.As d’intérêt admettent une fonction de densité, une fois on connaît l’espérance $\mathbb E[X]$ d’un cadre continu, on peut en déduire la variance $\text{Var}(X)$ :

$$
\text{Var}(X)=\mathbb E[(X-\mathbb E[X])^2] = \mathbb E[X^2]-\underbrace{\mathbb E[X]^2}_{\text{connu}},\text{ où } \mathbb E [X^2]=\int_{\Omega_X} x^2 \cdot f_X(x)\space dx
$$

Puisque $\mathbb E[X]$ est une constante (si elle existe; que ce n’est pas toujours le cas), $\mathbb E[X]^2$ est aussi une constante. 

# Densité d’une V.A. fonction de $X$ : $Y=\varphi(X)$

## Dérivation

Soit $X$ une V.A. de densité $d_X(x)$. Soit $\varphi$ une fonction monotonique et continûment dérivable, soit $Y = \varphi(X)$ la V.A. dont on veut trouver sa densité. Donc, la densité $f_Y(y)$ serait :

$$
f_Y(y)=\left[ (\varphi^{-1})'\right]_y \times f_X(\varphi^{-1}(y))
$$

La dérivation est tellement simple est jolie que je la laisse ici en bas. Partons de la fonction de répartition $F_Y(y)$ :

$$
F_Y(y)=\mathbb P(Y\le y)=\mathbb P(\varphi(X) \le y)= \mathbb P(X \le \varphi^{-1}(y))=F_X(\varphi^{-1}(y))
$$

Si on garde les membres les plus à gauche et à droite et on les dérive par rapport à $y$, on obtient la théorème présenté initialement.