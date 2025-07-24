# 02 // estimation paramétrique

Date de création: July 16, 2024 11:45 PM
Modifié: December 28, 2024 2:13 AM

# Rappel : espace probabilisé

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

<aside>
💡 Lorsqu’une expérience est conduite, on imagine que la “nature” “sélectionne” un **résultat** unique $\omega$ de l’univers $\Omega$, supposons $\omega = 2$. Tous les **événements** de $\mathcal{A}$ qui contiennent le **résultat** $\omega$ sont dit *produits*. Par exemple, l’événement “le dé montre $2$” s’est produit, mais l’événement “le dé montre un nombre pair” s’est aussi produit, et de même pour l’événement “le dé montre un nombre premier”, car $2$ est premier.

Cette "sélection" se produit de telle manière que, si l'expérience se répétait plusieurs fois, le nombre d'occurrences de chaque événement comme fraction du nombre total d'expériences conduites tendrait très probablement vers la probabilité attribuée à cet événement par la fonction de probabilités $\mathbb{P}$. Ceci c’est juste la loi des grands nombres.

</aside>

On peut se demander pourquoi ne pas choisir un autre $\mathcal{A}$ différent de $\mathcal{P}(\Omega)$. Pour le cas où $\Omega$ est dénombrable, on peut se contenter toujours faisant cette choix de $\mathcal{A}$.

Par contre, pour le cas non dénombrable comme $\Omega = \R$, si on définissait $\mathcal{A}=\mathcal{P}(\R)$, il serait faux que choisir un sous-ensemble quelconque de $\Omega$ soit un événement. Ceci est hors du cours, mais c’est une conséquence du théorème d’Ulam.

Pour cette raison, dans le cas non dénombrable, $\mathcal{A} \subset\mathcal{P}(\Omega)$  et non $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ comme dans le cas dénombrable.

## Propriétés des probabilités

<aside>
💡 Pour simplicité de notation, on note simplement $\mathbb P(a\in A) = \mathbb P(A)$.
$a$ est une variable d’intérêt dont on parle souvent, donc ce n’est pas nécessaire de la mentionner tout le temps. $A$ peut être un ensemble ou un intervalle.

</aside>

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

# Motivation

## Paramètres et statistique paramétrique

Plusieurs notions en statistique sont définies à partir de la définition de paramètre, dont sa définition est relativement vague étant donné qu’il s’agit d’un concept de base. Un **paramètre** est une quantité mesurée d’une population statistique qui résume ou décrit un aspect de la population, comme une moyenne ou un écart-type.

À partir de ça, la **statistique paramétrique** est une branche des statistiques qui suppose que les données d'échantillon proviennent d'une population qui peut être modélisée de manière adéquate par une distribution de probabilité qui a un ensemble fixe de paramètres. La plupart des méthodes statistiques connues sont paramétriques.

<aside>
💡 **Exemple**. Si on suppose que la taille des personnes en France suit une distribution normale (ou une autre distribution connue qui accepte des paramètres), alors un petit ensemble de paramètres peut être mesuré (la moyenne et l’écart-type, dans ce cas) pour décrire exactement cette population.

</aside>

Dans tout problème statistique, on dispose d’une observation $x$ d’un élément aléatoire $X$, qui est une seule variable ou un vecteur (une collection de plusieurs variables). La statistique inférentielle associe cette observation à un modèle statistique ou une structure statistique qui est un **espace probabilisé** $\{\Omega, \mathcal A, \mathbb P\}$ où :

- $\Omega$ est l’espace des observations, les valeurs possibles de notre élément aléatoire $X$
- $\mathcal A$ est la tribu des événements observables associés à $\Omega$
- $\mathbb P$ est une famille de lois de probabilité possibles pour $X$, définie sur $\mathcal A$

Ce dernier élément du triplet permet de définir un autre ensemble important : $\mathbb F$, qui serait l’ensemble des fonction de répartition possibles pour $X$.

Dans le cadre de la statistique paramétrique, on suppose que $\mathbb F$ est en bijection avec un ensemble de paramètres $\Theta$ appartenant à un espace de dimension finie $n$. Plus simplement, chaque fonction de répartition $F$ dans $\mathbb F$ correspond à un unique paramètre $\theta$ dans $\Theta$ et vice-versa.

$$
\mathbb F = \left\{F(\cdot,\theta) : \theta\in\Theta \subset \R^n \right\}
$$

Le point $\cdot$ serait éventuellement la place d’une variable cumulative $x$ de l’élément aléatoire $X$ d’intérêt (on parle, finalement, d’une fonction de répartition). La valeur $F(x,\theta)$ serait donc “la probabilité d’observer une valeur inférieur ou égale à $x$ dans notre caractéristique d’intérêt $X$—taille, poids, etc.—, sachant que les paramètres de la population sont $\theta$”.

On n’écrit pas $F(x,\theta)$ sur la définition de $\mathbb F$ parce que cela serait une valeur concrète de la fonction $F$ et ne plus une fonction en soi.

## Le problème avec $\theta$

Si l’on connaît la valeur de $θ$, on peut maîtriser la loi de probabilité $F(·, θ)$. **Mais, en pratique, la valeur de $θ$ est inconnue**. Pour déterminer la valeur de $θ$, que l’on utilisera en pratique, on procède de la manière suivante :

1. On utilise un échantillon des VAs iid. de cette loi : $\{X_1, X_2, \cdots, X_n\}$
2. On réalise les valeurs de l’échantillon : $\{X_1=x_1, X_2=x_2,  \cdots, X_n=x_n\}$
3. On calcule une certaine valeur numérique que l’on considérera comme une valeur approchée de $θ$ et qu’on appelle un estimateur de $θ$.

Ce chapitre navigue cette question, plus précisément la définition de deux types d’estimations : l’estimation ponctuelle et l’estimation par intervalle de confiance.

## Notion de statistique

Une statistique est à un échantillon ce qu’un paramètre est à une population : une certaine quantité numérique qui décrit un aspect de l’échantillon, ou tout simplement une **fonction des données**. Si $[X_i]_{1\le i\le n}=[X_1, \cdots, X_n]$ est un échantillon, voyons quelques exemples :

$$
\begin{align*}
&\hat\theta_1([X_i])=\bar X_n
&\text{Moyenne échantillonnale}
\\[8pt]
&\hat\theta_2([X_i])=\frac{1}{n}\sum_{i=1}^n(X_i-\bar X_n)^2=S^{2^\prime}_n
&\text{Variance échantillonnale non corrigée}
\\[14pt]
&\hat\theta_3([X_i])=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X_n)^2=S^{2}_n
&\text{Variance échantillonnale corrigée}
\\[14pt]
&\hat\theta_4([X_i])=\frac{\text{Nombre de }X_i\le x}{n}=F_n(x)
&\text{Répartition échantillonnale}
\\[14pt]
&\hat\theta_5([X_i])=\max([X_i])=X_{(n)}
&n-\text{ième statistique d'ordre}
\\[14pt]
&\hat\theta_6([X_i])=\min([X_i])=X_{(1)}
&1-\text{ième statistique d'ordre}
\\[14pt]
&\hat\theta_7([X_i])=X_{(n)}-X_{(1)}
&\text{Étendue échantillonnale}
\end{align*}
$$

Chaque réalisation $[x_1, \cdots, x_n]$ de l’échantillon aléatoire $[X_1,\cdots, X_n]$, qu’on appelle les données statistiques ou observations, produit une valeur de chacune des statistiques.

Le traitement théorique d’un problème d’inférence portant sur une population $X ∼ F(x, θ)$ consiste a choisir une statistique appropriée (par exemple, $X$ tout seul, $\bar X_n$, $S^2_n$, $X_{(n)}$) et à associer, à chaque valeur de la statistique choisie, une décision a propos du paramètre inconnu. La décision peut prendre différentes formes, trois desquelles seront traitées dorénavant :

1. **Estimation ponctuelle** : on peut décider que le paramètre a une certain valeur.
2. **Estimation par intervalle** : on peut décider que le paramètre se trouve vraisemblablement dans un certain intervalle.
3. **Test d’hypothèses** : on peut décider que la valeur du paramètre est égale (ou n’est pas égale) à un nombre fixé d’avance.

# Estimation ponctuelle

## Définition

Avant d’aborder les types d’estimation ponctuelle, on doit bien la définir :

- L’estimande $\theta$ est la valeur réalisé du paramètre qui nous est d’intérêt.
La plupart du temps, il s’agit tout simplement d’un paramètre de population.
- L’**estimateur** $\hat \theta$ est une règle ou algorithme pour inférer la vraie valeur d’un paramètre, et il est une fonction des données, donc on écrit $\hat \theta(x_1,\cdots,x_n)$.
La valeur réalisée de cet estimateur aurait tendance, en un certain sens, s'approcher du paramètre inconnu.
- L’estimé est le résultat numérique concrète réalisé une fois on a appliqué la règle de l’estimateur. Celle-ci est aussi l’**estimation ponctuelle** telle quelle.

Comme exemple, il se peut qu’il nous intéresse la moyenne d’une population $\mu$ (estimande). Donc, notre estimateur pourrait être la moyenne échantillonnale $\bar X_n$, et donc les règles sont juste d’additionner tous les valeurs observés et puis les diviser par $n$. Notre estimé serait la valeur concrète que l’estimateur a pris comme une fonction des données.

## Biais d’un estimateur et convergence

Le biais d’un estimateur est défini comme sa différence sa valeur espérée avec son estimande, donc :

$$
b_n=\mathbb E [\hat\theta_n]-\theta
$$

Un estimateur est dit “sans biais” si sa valeur espérée est égale à l’estimande ou, en équivalence, si le biais est nul :

$$
\text{Estimateur sans biais }\iff\mathbb E[\hat\theta_n]=\theta
$$

En plus, on peut parler d’un estimateur qui est asymptotiquement sans biais si l’espérance de l’estimateur tend vers l’estimande quand n tend vers l’infini :

$$
\text{Estimateur asymptotiquement sans biais }\iff \lim_{n\rightarrow \infin}\mathbb E[\hat\theta_n]=\theta
$$

Voyons que ce que dit l’équation précédente ce que l’espérance de l’estimateur tend vers l’estimande et non pas l’estimateur lui-même tend vers l’estimande. Par contre, ceci pourrait être le cas. On définit une suite $(\hat\theta_i)_{i\le n}$ et on dit que l’estimateur est convergente en probabilité à l’estimande si :

$$
\hat\theta_n \rightarrow \theta \text{ en probabilité} \iff \forall \varepsilon>0, \mathbb P\left(\lim_{n\rightarrow\infin}|\hat\theta_n-\theta|<\varepsilon\right)=1
$$

**Théorème**. Tout estimateur sans biais, ou asymptotiquement sans biais, dont la variance tend vers $0$ quand $n$ tend vers l’infini, est convergent.

Un exemple de ce dernier théorème est $\bar X_n \rightarrow \mu$ en moyenne quadratique ou d’ordre $2$.

**Théorème**. Une combinaison linéaire *convexe* d’estimateurs sans biais est aussi un estimateur sans biais. Une combinaison linéaire est convexe si la somme des coefficients égal $1$.

## EQM et qualité d’un estimateur

Il faut savoir qu’il n’existe pas un seul estimateur sans biais pour un paramètre. Par exemple, les statistiques $X_2$, $2X_3-X_1$ et $\bar X_n$ sont tous des estimateurs sans biais de $\mu$. Donc, quel estimateur choisir ? 

<aside>
💡 **Le professeur de ce cours insiste sur le fait que, même s’il y a plusieurs estimateurs de la moyenne poblationelle, il est *naturel* de sélectionner la moyenne échantillonnale comme estimation de la moyenne poblationelle**.

</aside>

Une manière est de regarder l’erreur moyenne quadratique (ou MSE comme Mean Square Error en anglais) de l’estimateur par rapport à son estimande :

$$
\begin{align*}
&\text{Var}(\hat\theta_n)=\mathbb E[(\hat\theta_n-\mathbb E[\hat\theta_n])^2]
\\
&\text{EQM}(\hat\theta_n)= \mathbb E[(\hat\theta_n-\theta)^2]=\text{var}(\hat\theta_n)+\text{biais}(\hat\theta_n)^2
\end{align*}
$$

(On peut arriver à la dernière égalité si on écrit $\text{EQM}(\hat\theta_n)= \mathbb E[(\hat\theta_n-\theta)^2]=\mathbb E\left[(\hat\theta_n-\mathbb E[\hat\theta_n])+\mathbb E[\hat\theta_n]-\theta)\right]^2$ et en développant. Ce théorème s’appelle la décomposition de l’erreur moyen quadratique). 

Jusqu’ici, l’estimateur ne dois pas forcément être sans biais. Un théorème important c’est que, si $\hat\theta_n$ est sans biais, donc son $\text{EQM}(\hat\theta_n)=\text{var}(\hat\theta_n)$, donc tout simplement sa variance.

**Théorème**. Si $\text{EQM}(\hat\theta_n)=0$, alors $\hat\theta_n \rightarrow \theta$ en moyenne quadratique, et donc converge en probabilité.

Il faut aussi dire que $b^2_n(\theta)$ est l’erreur structurelle, qui devient $0$ si $\hat\theta$ est sans biais. On peut donc voir que, en général, on voudrait un estimateur sans biais.

**Note**. Dans la question où si on veut diminuer la variance ou le biais mais on ne peut pas diminuer les deux simultanément, on fera le nécessaire (diminuer l’un ou l’autre) pour diminuer le **EQM**.  

### Domination : “efficace” entre deux estimateurs sans biais

Pour comparer deux estimateurs **sans biais**, on dit que $\hat\theta_n$ est plus “efficace” $\hat\theta_n^\prime$si et seulement si $\text{var}(\hat\theta_n) \le \text{var}(\hat\theta_n^\prime)$. Cet utilisation du mot “efficace” sera l’utilisation dite relative. On verra une autre manière d’appeler un estimateur comme efficace qui sera plus importante.

On peut avoir une idée de dominance aussi même sans parler ‘absence de biais”. $\hat\theta_1$ “domine” à $\hat\theta_2$ ssi. $\text{EQM}(\hat\theta_1) \le \text{EQM}(\hat\theta_2)$. Notons que $\hat\theta_1$ pourrait dominer $\hat\theta_2$ si le premier a un petit biais et le deuxième a une grande variance.

## Borne de Cramér-Rao et estimateurs *efficaces*

Tout ce qui suit sera utile pour les méthodes de construction d’un estimateur. Tout en premier, on devra définir la fonction de vraisemblance d’un échantillon réalisé $x=[x_i]_{i\le n}$ comme $L_n\left(x|\theta\right)$. Il serait utile de voir la fonction de densité $f_X(x,\theta)$ à deux variables au même temps.

- Si on fixe $\theta$, on reste avec une fonction $f_X: x\mapsto f(x|\theta)$, qui est notre fonction de densité commune sachant qu’elle est affectée par les paramètres $\theta$.
- Si on fixe la réalisation $x$, on reste avec une fonction $f_X : \theta \mapsto f(\theta|x)$, et c’est cette fonction ici qui est notre fonction de vraisemblance $L$.
- [Exemple avec distribution exponentielle ici](https://www.desmos.com/calculator/wy50ozzzrg). $L$ ici serait $g(x)$.

$$
L(\theta|x)=\prod_{i=1}^nf_X\left(x|\theta\right)
$$

Ayant défini la fonction de vraisemblance, on peut définir la [fonction de score](https://en.wikipedia.org/wiki/Score_(statistics)), qui sera le gradient de la log-vraisemblance quand les paramètres ont les valeurs réalisées $\theta^*$ (calculer la log-vraisemblance est moins coûteux si la loi mère en question contient des puissance ou des exponentielles). Le résultat est aussi un vecteur marquant la direction de plus vite croissance, et son module est le taux de croissance dans telle direction. Le score indique la sensitivité de la vraisemblance.

$$
\begin{align*}
&\text{Cas uniparamétrique : } s(\theta_I)=\frac{\partial\ln L}{\partial \theta}(\theta_I)=\frac{\partial}{\partial\theta}\sum_{i=1}^n\ln\left(f_X\left(x|\theta_I\right)\right)

\\[8pt]

&\text{Cas générale : } s(\theta_I)=\nabla{\ln(L(\theta_I))}=\left[\frac{\partial \ln L}{\partial \theta_1}(\theta_I), \hspace{3pt}\cdots, \frac{\partial \ln L}{\partial \theta_n}(\theta_I)\right]
\end{align*}
$$

Ici, $\theta_I$ est “$\theta$ comme input”, pour distinguer du $\theta$ comme forme différentielle.

Un point important du score **sous quelques conditions** est que, si $\theta_I$ est le vrai vecteur paramètre de la population càd. $\theta_I=\theta$, l’espérance du score évalué à $\theta$ est égal à $0$. Ce dernier résultat s’appelle l’équation de vraisemblence et est important pour le calcul de la variance.

$$
s(\theta_I)=\frac{\partial\ln L}{\partial \theta}(\theta_I)=0 \implies \theta_I=\theta
$$

Les conditions sont :

1. La dérivée partielle de $f(x|θ)$ par rapport à $θ$ existe [presque partout](https://en.wikipedia.org/wiki/Almost_everywhere).
(Il peut ne pas exister sur un ensemble nul, tant que cet ensemble ne dépend pas de $*θ*$)
2. L'intégrale de $*f(x|θ)*$ peut être différenciée sous le signe de l'intégrale par rapport à $*θ*$, et de même pour $\mathbb E[\hat\theta|\theta]$ 
3. Le [support](https://en.wikipedia.org/wiki/Support_(mathematics)) de $*f(x|θ)*$ ne dépend pas de $*θ*$

Avec cette fonction, on peut créer la statistique dite “[information de Fisher](https://en.wikipedia.org/wiki/Fisher_information)”, qui quantifie l’information d’un paramètre contenue dans la loi de distribution de $X$, qui dépend précisément de $\theta$. Formellement, l’information est la variance du score.

$$
I(\theta)=\mathbb E\left[\left( \frac{\partial \ln L}{\partial\theta}(\theta)-\cancel{\mathbb E[s(\theta)]}^{\space0}\right)^2\right]=\int_\Omega \left( \frac{\partial \ln L}{\partial\theta}(\theta)\right)^2L(\theta|x)d\theta

\\[7pt]

$$

**Note pratique #1**. On peut écrire la définition de l’information de Fisher avec la fonction de densité du paramètre étant donné l’échantillon réalisé $X=x$ (càd. la vraisemblance $L$), ou bien avec la fonction de densité de l’échantillon étant donné le paramètre réalisé ou le vrai paramètre. En fait, avec la fonction de densité de $X$ ça semble être plus facile.

$$
I(\theta)=\mathbb E\left[\left( \frac{\partial \ln L}{\partial\theta}(\theta)\right)^2\right]=\int_\Omega \left( \frac{\partial \ln L}{\partial\theta}(\theta)\right)^2L(\theta|x)d\theta 
\\[7pt]
\text{ou, de manière équivalente, }
\\[7pt]
I(\theta)=\mathbb E\left[\left( \frac{\partial \ln f}{\partial\theta}(x|\theta)\right)^2\right]=\int_\Omega \left( \frac{\partial \ln f}{\partial\theta}(x|\theta)\right)^2f(x|\theta)dx
$$

**Note pratique #2**. Si $\ln(L(\theta))$ est une fonction dérivable deux fois et la troisième condition de régularité mentionnée en dessus est vérifiée, on peut calculer l’information de Fisher d’une autre manière plus pratique.

$$
\text{Plus pratique pour les calculs }: I(\theta)=\mathbb E\left[-\frac{\partial^2 \ln L}{\partial\theta^2}(\theta^*)\right]
$$

**Théorème**. L’inverse de l’information de Fisher d’un paramètre $\theta$ est un minorant de la variance d’un estimateur sans biais de tel paramètre. Telle inverse de l’information est appelée la borne de Cramér-Rao. Une condition est que $I(\theta)$ existe pour tout $\theta$.

$$
\text{var}(\hat\theta_n)\ge \frac{1}{I(\theta)}
$$

Finalement, on définit un estimateur sans biais $\hat\theta_n$ comme *efficace* si

$$
\text{var}(\hat\theta_n)= \frac{1}{I(\theta)}
$$

### Exemple avec la distribution exponentielle

- Prend un échantillon de la distribution exponentielle avec $\theta=\lambda$ indéterminé et une seule VA, $X$.

$$
X\sim f(x|\lambda)=\lambda e^{-\lambda x}
$$

- Puisque on a une seule VA, la fonction de vraisemblance est la même que la densité de $X$.
    
    $$
    L(\lambda|x)=f(x|\lambda)
    $$
    
- Détermine la log-vraisemblance, puis la fonction de score.

$$
\begin{align*}
&\ln(L(\lambda)) = \ln(\lambda)-\lambda x=\ln(\lambda)-\lambda x \implies  
s(\lambda)=\frac{\partial \ln L}{\partial \lambda}(\lambda)=\frac{1}{\lambda}-x
\end{align*}
$$

- Puis, la fonction d’information de Fisher.
    
    $$
    \begin{align*}
    &-\frac{\partial^2 \ln L}{\partial \lambda^2}(\lambda)=\frac{1}{\lambda^2} &&\text{Préparation pour }I(\lambda)
    \\[10pt]
    &&\vdots
    \\[10pt]
    &I(\lambda)=\mathbb E \left[ -\frac{\partial^2 \ln L}{\partial \lambda^2}(\lambda)\right]
    &&\text{Définition de }I(\lambda)
    \\[10pt]
    &\int_\Omega \left( -\frac{\partial^2 \ln L}{\partial \lambda^2}(\lambda)\right)L(\lambda|x)dx
    &&\text{Définition de }\mathbb E
    \\[14pt]
    &\int_\Omega \left(\frac{1}{ \lambda^2}\right)L(\lambda|x)dx
    &&\text{Remplacement de la valeur}
    \\[14pt]
    &\frac{1}{ \lambda^2}\int_\Omega L(\lambda|x)dx
    &&\text{Constante sort de l'intégrale}
    \end{align*}
    $$
    
    Mais, voyons que intégrale de la densité dans toutes les valeurs de $x$ définies doit être $1$, par définition. Donc, finalement :
    
    $$
    I(\lambda)=\frac{1}{ \lambda^2}\cancel{\int_\Omega f(x|\theta)dx}^{\space1}=\frac{1}{\lambda^2}
    $$
    
    On est d’accords avec l’info de la distribution exponentielle sur Wikipédia. On est d’accord aussi avec [ce post de MathStackExchange](https://math.stackexchange.com/questions/1899995/fisher-information-for-exponential-distribution).
    

## Méthodes de construction d’un estimateur

<aside>
❗

Phrase du prof: la méthode de construction de l’estimateur ne garantit pas sa qualité !

</aside>

### Méthode des moments

Supposons que $θ$, le paramètre qu’on veut estimer, soit le seul paramètre inconnu et que $\mu$ soit une fonction de $θ$ : $\mu = φ(θ)$. Comme exemple pratique, l’écart-type est une fonction de la moyenne.

Si $φ$ est bijective, elle admettra une application inverse qui nous permettra d’écrire $θ = φ^{−1}(\mu)$. On en conclut donc :

$$
\mu=\varphi(\theta) \hspace{10pt}\text{et}\hspace{10pt}\theta=\varphi^{-1}(\mu)\iff\hat\theta=\varphi^{-1}(\bar X_n)
$$

Le but est de exprimer la moyenne populationnelle $\mu$ comme une fonction du paramètre $\theta$. Et, puisque la moyenne est le moment d’ordre $1$ d’une variable aléatoire, le nom de cette méthode est donc la méthode des moments.

1. On établit l’équation : $\mu=\mathbb E[X]=\varphi(\theta)$. Les calculs viennent avec la déf. de $\mathbb E$.
2. On détermine le paramètre théorique : $\theta = \varphi^{-1}(\mu)$
3. On détermine finalement la statistique de l’estimande avec un remplacement simple : $\hat\theta=\varphi(\hat\mu)=\varphi(\bar X)$

**Note**. L’estimateur obtenu par la méthode des moments n’est pas nécessairement sans biais.

Il est vrai que le moment le plus utilisé en pratique est le moment d’ordre $1$, càd. la moyenne $\mu=\mathbb E[X]$, et aussi qu’il est naturel d’estimer $\mathbb E[X]$ avec $\bar X$, la moyenne empirique des $X_i$. Cela dit, on peut le faire aussi sur $\mathbb E[X^2]$ avec la moyenne empirique des $X^2_i$, en on généralise avec tous les $k$-moments de $X$, $\mathbb E[X^k]$ avec $X^k_i$.

Pour avoir une meilleure notation, on note $\mu^\prime_k$ le moment d’ordre $k$ de la population, puis $m^\prime_k$ serait le moment d’ordre $k$ échantillonnale, d’où $\mu^\prime_1=\mathbb E[X]$ et $\lim_{n\rightarrow\infin} m^\prime_1 = \mathbb E[X]$, ce qu’on a dit sur le paragraphe précédent.

En plus, pour chaque $\mu^\prime_k$, on considère qu’il existe une fonction $\varphi_k$ qui prend tous les paramètres et qui nous retourne le moment d’ordre $k$ de la population.

Dans le cas ou la distribution est déterminée par plus d’un paramètre, $\theta=[\theta_1, \cdots, \theta_n]$, on pourrait tenter de calculer autant de moments que des paramètres pour après faire un système d’équations. Supposons qu’on veut estimer $n$ paramètres, donc on sait que

$$
\begin{cases}
\mu^\prime_1&=&\varphi_1(\theta_1, \cdots,\theta_k)
\\
&\vdots&
\\
\mu^\prime_k&=&\varphi_k(\theta_1, \cdots,\theta_k)
\end{cases}

\longrightarrow

\begin{cases}
m^\prime_1&=\varphi_1(\hat\theta_1,\cdots,\hat\theta_k)
\\
&\vdots
\\
m^\prime_k&=\varphi_k(\hat\theta_1,\cdots,\hat\theta_k)
\end{cases}
$$

Par exemple, pour estimer les paramètres d’une normale :

$$
\begin{cases}
\mathbb E[X] = \mu
\\
\mathbb E[X^2] = \mu^2 + \sigma^2
\end{cases}

\rightarrow

\begin{cases}
\hat{\mathbb E}[X] = \underbrace{\frac{1}{n}\sum_{i=1}^n X_i}_{\bar {X_n}}=\hat\mu

\\[30pt]

\hat{\mathbb E}[X^2] = \frac{1}{n}\sum_{i=1}^n X_i^2=\hat{\mu^2} + \hat{\sigma^2}
\end{cases}

\\[10pts]

\text{Finalement, }
\begin{cases}
\hat \mu = \underbrace{\frac{1}{n}\sum_{i=1}^n X_i}_{\bar {X_n}}

\\[30pt]

\hat{\sigma^2} = \frac{1}{n}\sum_{i=1}^n X^2_i-\hat{\mu^2}
\end{cases}
$$

Notons que le dernier pas c’est de “mettre un chapeau à tout”, càd. de passer du paramètre à l’estimateur.

Rappel. $S^{2}$ est la variance “qu’on ne veut pas”, la variance non corrigée. Après, on peut la corriger comme $S^{2^\prime}=\frac{n}{n-1}S^{2}$.

### Méthode du maximum de vraisemblance

On appelle l’estimateur du maximum de vraisemblance (EMV) du paramètre $\theta$, donne l’échantillon réalisé $x$, au $\beta$ tel que

$$
\theta ^*_{\bold x}\text{est EMV de }\theta\iff\theta^*_{\bold x}=\max_{\theta\in\Theta}L(\theta|\bold x)
$$

Bref, on appelle EMV l’input $\theta^*$ qui maximise la fonction de vraisemblance $L$ étant donné un échantillon observé. **Notons donc, pour toute réalisation différente de l’échantillon, on aura un EMV différent aussi, donc EMV est une fonction de l’échantillon $\bold x$.** Ceci étant dit, je vais juste simplifier sa notation à $\theta^*$.

Par contre, la définition ci-dessus ne nous garantit ni l’existence, ni l’unicité d’un tel estimateur. Pour trouver l’input $\theta$ qui maximise $L$, et supposant que $L$ est deux fois dérivable, on calcule $\theta^*$ tel que

$$
\begin{cases}
\frac{\partial L}{\partial\theta}(\theta^*)=0

\\[10pt]

\frac{\partial^2 L}{\partial\theta^2}(\theta^*)<0
\end{cases}
$$

Par contre, le plus souvent c’est de calculer $\theta^*$ tel que

$$
\begin{cases}
\frac{\partial \ln L}{\partial\theta}(\theta^*)=0
\\[10pt]
\frac{\partial^2 \ln L}{\partial\theta^2}(\theta^*)<0
\end{cases}
$$

**Optimiser $\ln(L)$ est normalement plus simple que $L$. Dans la pratique, on injecte le resultat obtenu de la première équation dans la deuxième**. Rappelons, par ailleurs, que si $θ^*$ est un EMV de $θ$ alors $g(θ^*)$ est l’EMV du paramètre $g(θ)$ pour $g$ continue.

**Exemple**. Supposons qu’on observe un échantillon, et qu’on s’intéresse au paramètre de la variance, donc $\theta=\text{var}(X)$. On détermine un estimateur sans biais de $\theta$, dans ce cas $\hat\theta={S^2}^\prime$. Puis, on calcule $\theta^*$ qui maximise la probabilité $L(\theta|x)$ . Finalement, si $g(x)=\sqrt{x}$, donc on a que

$$
g(\theta^*)\text{ est un EMV de }g(\theta)=g(\text{var(X)})=\sqrt{\text{var(X)}}=\sigma_X
$$

**Note**. $g(\hat \theta)$ peut ne pas être sans biais. Notons que $g({S^2}^\prime)=\sqrt{{S^2}^\prime}=S^\prime$ ne peut pas être un estimateur sans biais de $σ$, car on aurait alors

$$
\text{var}(S^\prime)=\mathbb {E}[{S^2}^\prime]-\mathbb E^2[S^\prime]=\theta-\theta =0
$$

Et ce qui n’est pas possible, car $\text{var}(X) >0$ par définition. Contradiction.

### Comportement asymptotique et conditions

Soit $\{\theta^*_n\}$ une suite de $\theta^*$ qui change avec l’augmentation de $n$. Donc, les valeurs de cette suite sont telles qu’elles se distribuent de manière gaussienne quand $n \rightarrow\infin$

$$
\lim_{n\rightarrow\infin} \sqrt{n}(\theta^*_n-\theta)\sim\mathcal N\left(0,\frac{1}{I(\theta)}\right) \iff \lim_{n\rightarrow\infin} \theta^*_n\sim\mathcal N\left(\theta,\frac{1}{nI(\theta)}\right)
$$

C’est qui est juste une application du théorème central de la limite, donc on cherche que $n\ge30$. On devra admettre à nouveau les conditions pour la nullité de l’espérance du score.

Notons que donc $\theta^*_n$ est asymptotiquement sans biais et asymptotiquement efficace, ce qui implique qui $\theta^*_n$ converge en moyenne quadratique (et on pourrait assurer qu’il converge presque sûrement avec d’autres conditions). Ces propriétés se résument comme que $\theta^*_n$ est un estimateur BAN : best asymptotically normal.

# Estimation par intervalle de confiance

## Motivation et définition

Un estimateur donne une valeur unique comme estimation. La valeur obtenue a peu de chances de coïncider avec celle du vrai paramètre, qui est inconnu.

L’estimation par intervalle de confiance consiste a entourer, d’un intervalle $[a, b]$, la valeur de l’estimateur et affirmer plutôt que $θ$ se trouve dans $[a, b]$. On peut alors choisir $a$ et $b$ de telle sorte que la probabilité que cette proposition soit vraie soit assez élevée.

## Intervalle de confiance pour $\mu$, connaissant $\sigma^2$

<aside>
💡 J’ai joué un peu avec la dist. exponentielle pour construire un intervalle de confiance
[https://www.desmos.com/calculator/9kkl96qxre?lang=fr](https://www.desmos.com/calculator/9kkl96qxre?lang=fr)

</aside>

Pour lancer cette estimation de $\mu$, on doit établir deux suppositions :

- La loi/distribution de la population dont on calcul le paramètre $\mu$ est connue.
La plupart du temps, on suppose qu’elle est une distribution normale pour pouvoir construire l’intervalle de confiance.
- La variance $\sigma^2$  est connue.
Par contre, cette supposition n’est pas réaliste. On y retournera après.

Étant donné qu’on veut estimer $\mu$ avec $\bar X$, on va calculer un intervalle $[a,b]$ tel que la probabilité que $\mu$ soit couverte soit grande, normalement $95\%$.

1. On prend un échantillon $X=[X_1,\cdots,X_n]$ d’où on suppose que $X\sim\mathcal N(\mu,\sigma^2)$.
2. On construit notre statistique qui estimerait le paramètre d’intérêt $\mu$, dans ce cas $\bar X$.
3. On détermine la loi de notre estimateur $\bar X$. On devrait savoir qu’une somme de $n$ VA normales est aussi une VA normale, particulièrement $\bar X \sim (\mu, \frac{\sigma^2}{n})$. Il faudrait calculer ceci *analytiquement* si la loi des $X_i$ de base n’est pas normale.
4. Une fois déterminée la loi de $\bar X$, on commence à se servir de ses propriétés connues pour établir un intervalle $[a,b]$ tel que 
    
    $$
    \mathbb P(a\le \bar X \le b)=0.95
    $$
    
5. On se sert de la propriété de la distribution normale suivante. Notons qu’on peut s’en servir même si on connaît pas $\mu$.
    
    $$
    \bar X \sim \mathcal N(\mu,\frac{\sigma^2}{n}) \iff\underbrace{\left(\frac{\bar X-\mu}{\sigma/\sqrt n}\right)}_Z\sim\mathcal N(0,1)
    $$
    
6. On change notre direction à vouloir encadrer $95\%$ de la loi de $z$ sous un nouveau intervalle. Arbitrairement, on voudra que cet intervalle soit symétrique autour de $0$, donc
    
    $$
    \mathbb P(-q\le Z\le q)=0.95 \implies q\approx1.96
    $$
    
7. On réécrit l’inégalité encadrante en termes des paramètres et l’estimateur
    
    $$
    \begin{align*}
    &\mathbb P(-q\le Z\le q)
    &\text{Préparation}
    \\[5pt]
    &\mathbb P \left( -1.96 \le \frac{\bar X-\mu}{\sigma/\sqrt n}\le1.96\right)
    &\text{Substitution}
    \\[5pt]
    &\mathbb P \left( -1.96\frac{\sigma}{\sqrt n} \le \bar X-\mu\le1.96\frac{\sigma}{\sqrt n}\right)
    &\text{Mult. par }\frac{\sigma}{\sqrt n}
    \\[5pt]
    &\mathbb P \left(\bar X -1.96\frac{\sigma}{\sqrt n} \le \mu\le\bar X+1.96\frac{\sigma}{\sqrt n}\right)
    &\text{Isolation de }\mu
    \end{align*}
    \\[10pt]
    
    \mathbb P \left(\bar X -1.96\sigma_{\bar X} \le \mu\le\bar X+1.96\sigma_{\bar X}\right)=0.95, \text{ où } \sigma_{\bar X}=\frac{\sigma}{\sqrt n}
    $$
    
8. Ici, on peut finalement substituer les valeurs connus de $n$, de $\bar X$ et la valeur de $\sigma$ qui découle de la valeur supposée connue de $\sigma^2$. On obtient une borne numérique concrète.
9. Éventuellement, si on veut une autre valeur de signification $\alpha$ différente de $5\%$, la forme générale de l’IC est
    
    $$
    \mathbb P \left(\bar X -z_{\alpha/2}\sigma_{\bar X} \le \mu\le\bar X+z_{\alpha/2}\sigma_{\bar X}\right)=\alpha,
    \\[10pt]
    \text{ où } z_{\alpha/2}\text{ est telle que }\mathbb P(-z_{\alpha/2}\le Z \le z_{\alpha/2})=1-\alpha
    $$
    

## $\sigma^2$ inconnue et la loi de Student

On avait dit qu’on supposée connue la valeur de $\sigma^2$, ce qui nous a permis d’établir l’IC. En réalité, ceci est difficilement le cas. Donc, avant d’estimer $\mu$ à travers un IC, on estime $\sigma^2$ avec une estimation ponctuelle, calculant dans ce cas $S^{2^\prime}$ et en le remplaçant dans l’IC de $\mu$, donc

$$
IC=[\bar X-z_{\alpha/2}\hat\sigma_{\bar X};\bar X+z_{\alpha/2}\hat\sigma_{\bar X}],\text{ où } \hat\sigma_{\bar X}=\sqrt{\frac{S^{2^\prime}}{n}}=\frac{S^\prime}{\sqrt n}
$$

Il faut se rappeler que la construction de l’intervalle de confiance s’est faite sous l’hypothèse que nous échantillonnons une population normale :

$$
Z=\frac{\bar X-\mu}{\sigma_{\bar X}}\sim\mathcal N(0,1)
$$

Mais, si on remplace $\sigma_{\bar X}$ dans la définition de $Z$ par $\hat\sigma_{\bar X}$, notons que le dénominateur est maintenant une variable aléatoire fonction des données (à cause de $S^\prime$) et ne plus une constante résultat de deux constantes, et donc **on ne peut pas assurer que $Z$ suit une loi $\mathcal N(0,1)$**. 

Afin de résoudre ce problème, on utilisera la loi de Student. La loi de Student à $k$ degrés de libertés est la loi du quotient, indépendant, d’une loi normale centrée-réduite et de la racine d’une loi de $χ^2$ divisé par son degré de liberté $k$.

$$
T=\frac{Z}{\sqrt{U/k}},\hspace{10pt}\text{ où }
\begin{cases}
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}=\frac{\bar X-\mu}{\sigma_{\bar X}}
\\[5pt]
U=\sum_{i=1}^kX_i^2\iff U \sim\chi^2_k
\end{cases}
$$

Dans ce cas, le numérateur $Z$ reste égal et on définit le dénominateur comme suit, où le facteur $1/\sigma^2$ devant est l’inverse de la variance de la population, pas de la moyenne échantillonnale.

$$
U=\frac{1}{\sigma^2}\underbrace{\sum_{i=1}^n(X_i-\bar X)^2}_{S^{2^\prime}\times(n-1)} \iff \begin{cases}
\frac{U}{n-1}=\frac{S^{2^\prime}}{\sigma^2}
\\[5pt]
U\sim\chi^2_{n-1}
\end{cases}
$$

Finalement, on écrit la variable aléatoire de Student $T$ comme suit, où $S^\prime$ est la racine carrée de la variance échantillonnale corrigée $S^{2^\prime}$ :

$$
T=

\frac{Z}{\sqrt{U/(n-1)}}
=

\frac{\bar X-\mu}{\underbrace{(\sigma/\sqrt{n})}_{\sigma_{\bar X}}}\times\frac{1}{S^\prime/\sigma}
=
\frac{\bar X-\mu}{S^\prime/\sqrt{n}}

\\[10pt]

\text{Finalement, }
T\sim\mathcal T_{n-1}
$$

Une autre manière de voir $T$ : “quotient indépendant d’une normale avec la racine d’une loi chi-carré divisée par ses degrés de libertés”. Le degrés de libertés sont $(n-1)$ car, le fait que la moyenne a été réalisé est une équation que les $X_i$ doivent respecter.

$$
T = \frac{\bar X_n - \mu}{(S_n/\sqrt{n})}=\frac{\frac{\bar X_n-\mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{S_n^2}{\sigma^2}}}=\frac{\mathcal N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}}
$$

## Les confusions autour des $\sigma$ et un exemple

Pour clarifier les doutes par rapport à toutes les notations sur $\sigma$, on suppose une population avec distribution uniforme de $\{1,2,3\}$ et on suppose un échantillon de $n=2$. Donc :

- $\sigma$ : paramètre, l’écart-type de la population, ici $\sigma=\sqrt\frac{2}{3}\approx0.82$.
- $\hat\sigma$ : estimateur, l’écart-type d’un échantillon observé.
Si on observe $\{2,3\}$, donc $\hat\sigma = \frac{1}{\sqrt{2}}\approx0.71$.
- $\sigma_{\bar X}$ : paramètre, l’écart-type de tous les possibles échantillons taille $2$.
    - Les possibles échantillons (supposant même probabilité de les observer) sont $\{1,2\}$, $\{1,3\}$, $\{2,3\}$, donc on en résulte avec une “nouvelle population dérivée” de $\{1.5, 2, 2.5\}$. En calculant l’écart-type, ici $\sigma_{\bar X}=\frac{1}{\sqrt6}\approx0.41$.
- $\hat\sigma_{\bar X}$ : estimateur, l’écart-type des moyennes échantillonnales observées.
    - Si on suppose qu’on est limités à observer un seul échantillon, disons $\{1,3\}$, donc on finit avec une $\bar X = 2$, et l’ensemble de moyennes échantillonnales qu’on peut observer est juste $\{2\}$. On ne peut pas calculer l’écart-type d’une seule valeur.
    - On aurait besoin d’observer au moins un autre échantillon de taille $2$ pour avoir un deuxième valeur de la moyenne échantillonnales, disons $2.5$, et puis finalement on pourrait calculer l’écart-type des moyennes échantillonnales observées, càd. $\{2,2.5\}$, qui serait $\hat\sigma_{\bar X}=\frac{1}{ \sqrt{8}}\approx0.35$.

**Attention**. Parfois c’est impossible de collecter un autre échantillon. Donc, dans ce cas, on peut faire une approximation acceptable si :

- On suppose que les $X_i$ suivent une loi normale (donc $\bar X$ aussi, par propriété dérivée de la loi normale), OU
- La taille $n$ de l’échantillon est $n\ge30$ (donc $\bar X$ tend vers une loi normale à cause du TCL)

Donc, si l’une de ces deux conditions est vérifiées, on peut prendre comme estimateur $\hat\sigma_{\bar X}$, qui dans ce cas serait

$$
\hat\sigma_{\bar X}=\frac{\hat\sigma}{\sqrt{n}}=\frac{1/\sqrt{2}}{\sqrt{2}}=0.5
$$

Notons que, si les $X_i$ suivent chacune une loi normal, c’est strictement vraie l’équation $\sigma_{\bar X} = \frac{\sigma}{\sqrt{n}}$ (sans les chapeaux $\land$ des estimateurs, on parle des vraies paramètres !), c’est une dérivation algébrique.

Par contre, si les $X_i$ suivent une autre loi (dans ce cas une loi uniforme), ce n’est pas vrai que $\sigma_{\bar X} = \frac{\sigma}{\sqrt{n}}$, c’est juste une approximation acceptable. La forme serrée de $\sigma_{\bar X}$ serait à calculer analytiquement en termes de $\sigma$ et $n$.

## Statistique pivotale

Une statistique $\varphi([X_i], \theta)$, qui est une fonction des observations $[X_i]_{1\le i\le n}$ et du paramètre $\theta$, est appelée “quantité pivotale” si sa distribution ne dépend pas du paramètre inconnu $\theta$.

Par exemple, et supposant $\sigma^2$ connue, la normalisation de la moyenne échantillonnale est une statistique pivotale, car sa distribution normalisée ne dépend pas de $\mu$. Peu importe la valeur de $\mu$, on sait que de prendre une moyenne échantillonnale et la normaliser par son $\mu$, quelle que soit, devrait suivre une loi normale standard. 

$$
Z=\varphi([X_i])=\frac{\bar X-\mu}{\sigma_{\bar X}}\sim\mathcal N(0,1)
$$

Dans le cas d’une distribution exponentielle de paramètre $\frac{1}{\theta}$, une statistique pivotale est 

$$
\frac{2}{\theta}\sum_{i=1}^nX_i\sim\chi^2_{2n}
$$

C’est l’existence d’une quantité pivotale qui permet la construction d’un intervalle de confiance. En effet, le fait que la distribution de $φ$ ne dépend plus du paramètre inconnu $θ$, **permet de trouver deux nombres $a$ et $b$, indépendants également de $θ$**, tels que 

$$
\mathbb P(a \le \varphi([X_i], \theta)\le b)=1-\alpha
$$

où $α$ est un nombre choisi par avance dans $[0, 1]$, normalement très petit.