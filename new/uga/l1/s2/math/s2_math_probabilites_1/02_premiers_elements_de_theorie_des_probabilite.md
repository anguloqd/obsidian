# 02 // premiers éléments de théorie des probabilités

# Les bases

## Les événements : $\omega \in \Omega$

Soit $\Omega$ l’univers d’événements, càd., l’ensemble de tous le possibles résultats d’une expérience aléatoire. Un événement est un sous-ensemble de l’univers $\Omega$.

Quand on parle de variables aléatoires, un événement est une valeur prise (ou un ensemble de valeurs) par la variable aléatoire. Donc, on pourrait noter que l’événement “un dé montre $6$” comme $A : (X=6)$. Mais on peut parler aussi des événements sans parler de variables aléatoires.

Selon sa définition, un événement reçoit une classification d'événements :

- **Événement certain** : avec probabilité $1$, l’événement se produit toujours.
- **Événement impossible** : avec probabilité $0$, l’événement se produit jamais.
- **Événement complémentaire** : si on fixe un événement $E$ avec un probabilité $p$, donc l'événement "non E", noté comme $\neg E$, a une probabilité $(1-p)$.
- **Événement élémentaire** : événements qui se réalisent pour une seule issue de l’expérience. Exemple : pile ou face, pour construire des suites de pile ou faces.

## Algèbre d’événements : $\mathcal A = \{S,O\}$

Pour rappel, une *algèbre* est une duple $\{S,O\}$ avec $S$ un ensemble d’éléments et $O$ un ensemble d’opérations applicables à $S$ de sorte que leur résultat reste encore dans $S$. Cette propriété s’appelle la *fermeture* ou *stabilité* de $S$ par rapport aux opérations de $O$, et est nécessaire dans la définition d’une algèbre..

Quand on parle d’une algèbre d’événements $\mathcal{A}=\{S,O\}$, $S$ contient des événements et $O$ les opérations suivent, avec $A$ et $B$ deux événements de $S$ :

- **Réunion (dénombrable)** : **$A\cup B$**
L'ensemble pour lequel les événements $A$ ou $B$ sont vrais, ou les deux.
- **Intersection (finie)** : $A \cap B$
L'ensemble pour lequel les deux A et B sont vrais.
- **Complémentation** : $A^c$
L'ensemble pour lequel $A$ est faux.

À partir de ce trois opérations, on peut déterminer la relation entre deux événements $A$ et $B$ :

- **Événements incompatibles** : si $A \cap B = \empty$.
- **Événements complémentaires** : si $A \cup B = \Omega$.
    - Note. Dans la définition de l’algèbre $\mathcal{A}$, on peut définir l’ensemble d’événements qui contient tous les événements $\Omega$, o bien juste un partie d’eux $S\subset \Omega$.

# Les probabilités des événements

## Définition et propriétés

Partons des axiomes de probabilités, même si on va les condenser à l’extrême ici. Un espace de probabilité est le triplet $(\Omega, \mathcal{A}, \mathbb{P})$, où $\Omega$ est l’univers, $\mathcal{A}$ une tribu/$\sigma$-algèbre/algèbre d’événements, et $\mathbb{P}$ est une fonction $\Omega \mapsto [0,1]\in\R$ pour donner une probabilité à un événement.

À partir de cela, on peut déterminer les probabilités des événements qui sont issus des opérations de deux événements atomiques (les résultats de l’expérience) :

- $\mathbb P(A\cup B) = \mathbb P(A) + \mathbb P(B) - \mathbb P(A \cap B)$
- $\mathbb P(\neg A) = 1 - \mathbb P(A)$
- $\mathbb P(A \cup B) \le \mathbb P(A) + \mathbb P(B)$

## Probabilité conditionnelle

La probabilité conditionnelle de $B$ donné $A$, notée comme $\mathbb P(B|A)$, nous mène à réduire notre vision de $B$ à partir de tout l’univers jusqu’à la partie de l’univers où un certain événement $A$ s’est produit. La définition mathématique est comme suit :

$$
\mathbb P(B|A) = \frac{\mathbb P(A \cap B)}{\mathbb P(A)}
$$

Une théorème puissant par rapport aux probabilités conditionnelles est le **théorème de Bayes**, qui relie $\mathbb P(A|B)$ avec $\mathbb P(B|A)$ :

$$
\mathbb P(A|B) = \frac{\mathbb P(B|A)\mathbb P(A)}{\mathbb P(B)}
$$

# Indépendance

## Notion et événements indépendants

La définition d’indépendance est alors :

$$
A,B \text{ sont indépendants} \iff \mathbb P(A \cap B) = \mathbb P(A) \mathbb P(B) 
$$

Notons que si $A$ est indépendant de $B$, $B$ est aussi indépendant de $A$. 

La formulation plus général (si les événements sont indépendants ou dépendants) est alors :

$$
\mathbb P(A \cap B) = \mathbb P(A)\mathbb P(B|A)
$$

Pourtant, si $A$ et $B$ sont indépendants, donc $\mathbb P(B|A) = \mathbb P(B)$, et la définition de la probabilité conditionnelle est $\mathbb P(B|A) = \frac{\mathbb P(A \cap B)}{\mathbb P(A)}$ et on arrive à l’égalité précédente si on multiplie par $\mathbb P(A)$ aux deux membres de l’égalité et on substitue avec $\mathbb P(B)$ sans condition.

On peut généraliser cette notion indépendance pour un famille événements, pas seulement à deux événements. L’indépendance *entre eux* veut dire l’indépendance de 2 événements dans la famille pour toute possible couple d’événements possible à choisir.

$$
\{A_1,\dots,A_n\} \text{ sont indépendants entre eux} \iff \mathbb P \left( \bigcap_{i=1}^n A_i \right) = \prod_{i=1}^n\mathbb P(A_i)
$$

## Variables aléatoires indépendantes

De même, on peut définir V.A qui gardent cette idée d’indépendance. L’univers $\Omega$, dans ce cas, contient toutes le possibles couples valeurs que $X_1$ et $X_2$ pourraient prendre. Si $X_1$ est une pièce et $X_2$ un dé, donc :

$$
\Omega=
\overbrace{
\{X_1 = 0, X_1 = 1\}
}^{\Omega_1}
\times
\overbrace{
\{X_2=1, \dots , X_2 =6 \}}^{\Omega_2}
$$

On peut penser à $\Omega_1$ et $\Omega_2$ comme l’univers “local” de la pièce et du dé, respectivement. C’est à dire, l’ensemble des résultats qu’on aurait si on jouais *seulement* avec une pièce ou un dé, respectivement.

> [!note]
> Notons que l’expérience est *le jeu conjoint de la pièce et du dé*. C’est n’est pas le jeu *seul* de la pièce ou du dé. Donc, **chaque résultat dans $\Omega$ nécessite que toute variable aléatoire prenne une valeur**.
>
> Après, si on voudrait considérer seulement le résultat d’une seule variable aléatoire (disons, la pièce montre pile) ignorant l’autre, ou pourrait écrire :
>
> $$
> \text{Manière incorrecte : } S = \{X_1 =0\}
> \newline
> \text{}
> \newline
> \text{Manière correcte : }S = \{X_1 =0\}\hspace{6pt} \times \underbrace{\{X_2 = x,\hspace{4pt}x \in \Omega_2\}}_{\text{"peu importe la valeur du dé"}}
>
> $$
>
> De cette manière, on considère le résultat du l’univers local $\Omega_1$ lié à la pièce $X_1$ quand elle montre une pile.

Formellement, l’indépendance entre une famille de V.A est vérifiée si et seulement si :

$$
\mathbb P \left( \bigcap_{i=1}^nX_i \right)= \prod_{i=1}^n\mathbb P(X_i )
$$

## V.A comme des fonctions d’autres V.A et leur indépendance

Notons qu’on peut construire une variable aléatoire sur une autre variable aléatoire. Prenons $X$ comme le résultat d’un dé et définissons $Y = 2X+3$. $Y$ est simplement une fonction affine définie sur le résultat du dé. Si le dé montre $4$, on le multiple par $2$ et on somme $3$, $Y$ serait donc $11$.

Il faut ne pas confondre que $Y$ est une variable aléatoire qui applique une fonction affine, **$Y$ n’est pas la fonction affine elle-même** !

$$
f:\R \mapsto \R, f(x)=2x+3
\newline
Y = f(X)= 2X+3. \implies \Omega_Y=\{5,7,9,11,13,15\}
$$

Avec cela dit, si une famille de V.A sont indépendantes, définir des variables aléatoires sur les V.A indépendantes de bases restent bien sûr indépendantes entre elles. 

$$
\{ X_1,\dots,X_n \} \text{ V.A indépendantes,  }
\{f_1(x), \dots, f_n(x) \} \text{ fonctions réelles.}

\newline
\text{ }
\newline

\text{Soit }Y_i = f_i(X_i). \text{ Donc, } \mathbb P \left( \bigcap_{i=1}^n \overbrace{Y_i}^{f_i(X_i)} \right)= \prod_{i=1}^n \mathbb P(\overbrace{Y_i}^{f_i(X_i)})
$$