# 02 // cas dénombrable : indépendance, espérance, dispersion

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

# Espérance : $\mathbb E [X]$

## Définition et propriétés

### Définition

Mathématiquement, c’est la moyenne pondérée des résultats de la V.A $X$. Intuitivement, c'est la moyenne des résultats qu'on observerait si on pouvait répéter l’expérience une infinité de fois. Elle seulement existe si la série $\sum (x \cdot \mathbb P(X=x)$ est absolument convergente, sinon on dit que $X$ ne possède pas une espérance.

$$
\mathbb{E}(X) = \sum_{x \in \Omega_X} (x\cdot \mathbb P(X=x))
$$

### Propriétés

**Linéarité de l’espérance**. L’espérance de la somme est la somme des espérances, même si elles sont dépendantes.

$$
\mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y]
\newline
\mathbb{E}[\alpha X] = \alpha \mathbb{E}[X]  
$$

**Produit des espérances**. Si deux V.A. sont **forcément indépendantes**  $\implies$ l’espérance du produit égal le produit des espérances. **Réciproque fausse**.

$$
\mathbb{E}[XY] =\mathbb{E}[X]\mathbb{E}[Y] 
$$

**Espérance d’une V.A. fonction d’autre V.A**. Supposons une fonction réelle $f(x)$ et une VA définie sur une VA comme $Y=f(X)$. Donc, si la série $\sum(f(X) \cdot \mathbb P(X=x))$ est absolument convergente, donc on peut parler de l’espérance de $f(X)$ (ou de $Y$ aussi).

$$
\mathbb{E}[\overbrace{f(X)}^Y] = \sum_{x\in\Omega_X} (\overbrace{f(X)}^Y\cdot \mathbb P(X=x) )
$$

# Moments et variance : $\text{Var}(X)$

## Définitions et théorèmes

### Définition de variance et théorèmes

Un moment est une notion sortie de la physique. Si $n \in \N$ et $X$ est une V.A. avec espérance finie, donc $\mathbb{E}[X^n]$ est le moment d’ordre $n$ de $X$. Encore plus, $\mathbb{E}[(X-\mathbb{E}[X])^n]$ est le moment *centré* d’ordre $n$ de $X$. “Centré” veut dire centré autour de la moyenne, car à chaque valeur de $X$ on soustrait la moyenne, donc l’ensemble qui en ressort a comme nouveau centre $0$.

La variance est le moment d’ordre $2$ de $X$, c’est-à,dire, la valeur espérée du carré de la somme des écarts de chaque observation par rapport à la moyenne. Intuitivement, elle est simplement une mesure de dispersion de la moyenne, exprimée en unités carrées. **La variance est toujours positive !**

$$
\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}[X])^2] =\sum_{x\in\Omega_X}( (x-\mathbb{E}[X])^2\cdot \mathbb P(X=x))
$$

- **Théorème de König-Huygens**. $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$
Cette relation rend plus confortable le calcul de la variance.
- **Inégalité de Cauchy-Schwarz**. $|\mathbb{E}(XY)| \le \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}$

### L’écart type

La racine carré de la variance est connue comme l’écart-type, noté comme $\sigma = \sqrt{\text{Var}(X)}$. Elle est exprimé en unités de la V.A., tant que la variance est en unités carrées.

# Covariance et corrélation

## Covariance : $\text{Cov}(X,Y)$

La covariance est une mesure de variation entre deux V.A. Si les deux variables aléatoires ont tendance à être du même signe, la covariance sera positive. Si elles ont tendance à être de signe distincts, la covariance sera négative. L’unité de mesure de la covariance sera l’unité de $X$ fois celle de $Y$.

$$
\text{Cov}(X,Y)=\mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[X])] = \mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]
$$

**Propriété**. Si $X,Y$ indépendantes $\implies \text{Cov}(X,Y) = 0$. Réciproque fausse.

## Coefficient de corrélation de Pearson : $\rho_{X,Y}$

Le problème de la covariance est que il est plus difficile de mesurer le niveau jusqu’à une V.A. a une influence sur l’autre. Donc, on utilise la corrélation, qui la version normalisé de la covariance. On note ici $\sigma$ l’écart-type d’une V.A.

$$
\rho_{X,Y}=\frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

Le signe du coefficient de corrélation a la même fonction que dans la covariance : si les deux VA ont une relation linéairement directe ou inverse. En plus, la corrélation est toujours bornée entre $[-1, 1]$, d’après l’inégalité de Cauchy-Schwartz.

Si la corrélation égal $1$ ou $-1$, donc il existe une fonction linéaire directe (de ponte positive) ou inverse (de pente négative), respectivement, qui décrit parfaitement la relation entre $X$ et $Y$.