# 02 // théorie du signal

[Slides : Série de Fourier.pdf](ressources/02_theorie_du_signal_slides_srie_fourier_annote.pdf)

[Slides : Transformée de Fourier.pdf](ressources/02_theorie_du_signal_slides_transforme_fourier_annote.pdf)

[Slides : traitement de signal.pdf](ressources/02_theorie_du_signal_slides_traitement_du_signal_annote.pdf)

[Exo 3.2 cpt maths : série de Fourier à harmoniques réelles.pdf](ressources/02_theorie_du_signal_ex_3.2_cpt_maths.pdf)

# Introduction

## À quoi ça sert

Un signal est le support physique d'une information ou d'une commande. Il se présente sous différentes formes : signal électromagnétique (signal électrique, signal magnétique, signal radioélectrique...), signal acoustique (son, échographie...), signal graphique (film...), etc.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled.png)

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_1.png)

Le signal de gauche est périodique. On aura tendance à le résumer par l'observation de son évolution sur la période $T$ (série de Fourier). On ne pourra pas faire de telle restriction pour le signal de droite (transformée de Fourier).

## Classification énergique

Une classification peut être faite à partir des notions d'énergie ou de puissance d'un signal. Au signal $f(t)$ (fonction complexe ou réelle de $t$), on associe sur le support temporel $\tau$ :

- L'énergie $E_f$ associée, si elle existe :
    
    $$
    E_f=\int_0^\tau |f(t)|^2dt
    $$
    
- La puissance moyenne associée $P_f$, si elle existe :
    
    $$
    P_f=\lim_{\tau\rightarrow\infty} \frac{1}{\tau} \int_0^\tau|f(t)|^2dt=\lim_{\tau\rightarrow\infty}\frac{1}{\tau} E_f
    $$
    

Les signaux périodiques et les signaux aléatoires permanents font partie de la classification de signaux à puissance moyenne finie.

Les signaux “réels” (rencontrés en pratique) sont des signaux a énergie finie (définis sur une durée finie), cependant les signaux a puissance moyenne finie sont souvent utilisés pour modéliser des générateurs de signaux périodiques, par exemple. Enfin, certains signaux théoriques n’appartiennent ni à l’une ni à l’autre de ces catégories.

## Représentation en temps et fréquence

Voyons la prochaine courbe $x(t)=\cos(t)$ qui pourrait représenter de l’énergie, de l’intensité du son, etc. On dirait que la période de $\cos(t)$ est $2\pi$, mais on ne connaît pas exactement la direction de la répétition : si on lit de droite à gauche, on dirait que la courbe se répète aussi à chaque $-2\pi$ unités de temps ! Donc on dit que sa période est $T_0=\pm 2\pi$ unités de temps per cycle.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_2.png)

En réalité, on garde juste un période à deux signes dans le cas où la signal $x(t)$ présente un seul phénomène de période $t_0$, càd. si $t_0$ est la périodicité minimale du signal, toute autre période est un multiple de $t_0$. **Si la signal n’est pas élémentaire, on garde juste $f_0$ positif**.

> [!note]
> Un signal élémentaire est juste un signal harmonique : càd, un signale qui admet une unique fréquence $\pm f_0$. Les autres signaux sont dit “non-harminques” ou “compliqués”.

La représentation spectrale d’un signal (à droite) est une fonction de la fréquence $f_0 = 1/T_0$, et les unités de fréquence est “quantité d’un cycle par une unité de temps”. Dans le cas d’un signal à un seul phénomène, on divise l’amplitude (maximum absolue du signal $x(t)$) par deux dans ce cas et on le graphique contre $\pm f_0$.

# Séries de Fourier

> [!note]
> Les exercices en partiel sur les séries de Fourier sont normalement comme suit : calculer coefficients de Fourier pour monter la série, appliquer thm. de Dirichlet pour confirmer la convergence, et puis le thm. de Parseval pour “faire un truc”, càd. une conséquence logique intéressante.

## Définitions requises

### Continuité par morceaux

Une fonction $f$ est continue par morceaux si son domaine admet une suite $C$ de $n$ valeurs $\{c_1, \dots, c_n\}$ tel que la fonction est continue sur l’intervalle ouvert délimité par les points de coupe adjacents et aussi si les limites sur chaque $c_i$ existe.

$$
f \text{ continue par morceaux sur Dom}_f \iff

\begin{cases}
\forall i< n, f \text{ continue sur } ]c_i, c_{i+1}[
\\
\forall x_i \in C, f(c_i^+) \text{ et } f(c_i^-) \text{ existe}
\end{cases}
$$

Notons qu’il n’est jamais nécessaire que $f(c_i)$ soit définit, juste qu’elle admet une limite sur $f(c_i)$.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_3.png)

### L’harmonique fondamentale

L’harmonique fondamentale est la fonction suivante :

$$
\theta \mapsto e^{\frac{2\pi k}{T}\theta i}
$$

Tant que celle-ci n’est pas trop facile à voir, il faudrait rappeler l’égalité suivante :

$$
e^{\frac{2\pi k}{T}\theta i}=\cos\left(\frac{2\pi k}{T} \theta\right) + i\sin\left(\frac{2\pi k}{T} \theta\right)
$$

Donc, la harmonique fondamentale est juste une somme “orthogonale” d’une composante réelle $(\cos)$ et une composante imaginaire $(i\sin)$.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_4.png)

### Périodicité (et examples avec l’harmonique fondamentale)

Une fonction $f$ est périodique si :

$$
f\text{ périodique } \iff \exist T\in\mathbb{R}^+, \forall x\in\mathbb{R}, f(x)=f(x+T)
$$

**Remarque**. Si $f$ est périodique sur 
$$, $f$ est périodique aussi sur $kT$, où $k\in\Z$. Un tel cas est si $f$ est $\frac T n$-périodique, $f$ est aussi $T$-périodique. Il faut absolument que $k\in\Z$. Un coefficient de période k réel non entier ne capture pas tous les évènements. Par exemple, $k=3/2$ capture un vrai période de chaque deux, càd. quand $k$ devient entier.

**Propriété**. La périodicité peut être conservé dans la somme de plusieurs fonctions. Particulièrement, si $\{f_1,\cdots,f_n\}$ sont T-périodiques et si $\{a_1, \cdots, a_n\}$ sont des complexes, $\sum_j {a_j f_j}$ est aussi $T$-périodique. 

- Un cas particulier est, si les $\{f_1,\cdots, f_n\}$ sont $\frac T k$-périodiques, avec chaque entier $k$ différent pour chaque fonction, la combinaison linéaire reste T-périodique.

**Exemple**. Dans le plan complexe, toujours avec $k\in\Z$…

- La fonction $f_1(\theta)=e^{i\theta}$ est $2\pi$-périodique.
Elle trace le cercle unitaire, où $\theta$ est l’angle en radians avec l’axe $x$.
- Si on la modifie à $f_2(\theta)=e^{2\pi i \theta}$, elle sera $1$-périodique.
La différence avec la première c’est que celle-ci trace tout un cercle en premier (c’est la fonction du coefficient $2\pi$ là), puis s’arrête à $\theta$ radians du cercle.
- Si on la modifie $f_3(\theta)=e^{2\pi k i \theta}$ elle reste encore $1$-périodique. Maintenant pour un certain $\theta$, on fait $k$ cercles (le coefficient $(2\pi\times k)$) puis on s’arrête à $\theta$ radians.
- Si $T\ne0$, $f_4(\theta)=e^{\frac{2\pi}{T} i \theta}$ est $T$-périodique. On trace un cercle (et on s’arrête sur $f_4(\theta)=1$) chaque fois que le coefficient de i, le $\frac{2 \pi}{T}\theta$, est un multiple de $2\pi$. Le $\theta$ plus petit pour cela est donc $\theta=T$.
- Par ce même raisonnement, $f_5(\theta)=e^{\frac{2\pi k}{T} i \theta}$ est aussi T-périodique, car $2\pi k$ est un multiple de $2\pi$ si $\theta=T$. **La différence** ce que le plus petit $\theta$ pour que tout le coefficient vale juste $2\pi$ est $\theta =T/k$.

Finalement, on peut faire une combinaison linéaire sur l’harmonique fondamentale **qui serait en tout T-périodique**. On appelle ceci un “polynôme trigonométrique” mais c’est un faux polynôme.

$$
P_N(x)=\sum_{_N}^N c_ke^{\frac{2pi k}{T}ix}=\sum_{_N}^N c_kz^k
$$

Les termes d’un polynôme sans coefficients sont $x^k+x^{k-1}+\cdots+x+1$, avec $k\in\Z$. On pose donc $z=e^{\frac{2pi k}{T}ix}$ et on pourra dire que $z^k+z^{k-1}+\cdots+z+1$ est un “polynôme trigonométrique”.

### Base de $E(T)$

À partir de l’espace des fonctions continues par morceaux T-périodiques, on peut définir un produit hermitien d’intérêt.

$$
\lang f,g\rang\in E^2=\frac{1}{T}\int_0^Tf(u)\bar g (u)du
$$

Les harmoniques élémentaires (ou “harmoniques fondamentales”) pour reconstituer un signal $T$ périodique sont donnés par la famille suivante :

$$
(e_k)_{k\in\Z} \text{, avec } e_k(x)=e^{\frac{2\pi k}{T} i x}

\\

$$

On admet que ce qui suit (la manipulation algébrique est dans les slides) :

$$
\lang e^{\frac{2\pi k}{T} i p}, e^{\frac{2\pi k}{T} i q}\rang=
\begin{cases}
1, \text{ si }p=q
\\
0, \text{ si }p\ne q
\end{cases}
$$

Comme rappel, une famille orthogonal est une famille d’éléments $(v_k)$ dont le produit scalaire (dans ce cas, produit hermitien) est $0$ deux-à-deux.

Si on prend des couples dans $(e_k)$, on voit que $p\ne q$ toujours, et donc $(e_k)$ est orthogonale (libre). En plus, on sait que elle trace le cercle unitaire, donc elle est de rayon $1$ et donc elle est orthonormée. Elle est génératrice de tout $E(T)$ mais c’est plus compliqué à voir, donc on l’admet.

## Coefficients de Fourier

### Définition

À ce stade, on voudrait décomposer une fonction de $E(T)$ comme une somme de signaux élémentaires de $(e_k)$. On cherche donc les coefficients de cette combinaison linéaire, appelés les coefficients de Fourier. On se sert du produit hermitien définit précédemment. 

$$
c_p(f)=\lang f, e_p\rang=\frac{1}{T}\int_0^Tf(x)e^{-\frac{2\pi p}{T}ix}dx
$$

Le conjugué de $e_p$ se voit dans le signe négatif dans l’exposant, ce qui reflète le nombre complexe représenté sur l’axe des abscisses.

### Exemple

Supposons le signal binaire suivant :

$$
f(x)=
\begin{cases}
0, x\in[2k\pi, (2k+1)\pi[ \text{ où }k\in\Z

\\

1, x\in[(2k+1)\pi, 2k\pi[ \text{ où }k\in\Z
\end{cases}
$$

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_5.png)

Notons qu’elle est donc de période $2\pi$. On fixe $T=2\pi$ et on cherche les coefficients de Fourier.

**Une note très importante c’est qu’on calcule $c_0$ séparément**. Notons que de mettre $n=0$ sur l’expression en-dessus provoque une division par zéro. **Dans la pratique, on calcule $c_0$ directement de la définition des coefficients, puis on trouve une forme générale de $c_n$ pour les autres coefficients.**

$$
c_o=\frac{1}{2\pi}\int_0^{2\pi}f(x)dx=\frac{1}{2\pi}(\pi)=\frac{1}{2}
$$

Après, on peut obtenir la forme générale en développant la définition des coefficients :

$$
c_n(f)=\frac{1}{T}\int_0^Tf(x)e^{-\frac{\cancel{2\pi} p}{\cancel{2\pi}}ix}dx ...=\frac{1-e^{-\pi i n}}{-2\pi in}=
\begin{cases}
\frac{1}{2}, \text{si } n=0
\\
0, n\text{ pair non-zéro}
\\
\frac{1}{-\pi i n}, n\text{ impair}
\end{cases}
$$

Notons que est défini pour $n\in\mathbb{N}$. Mais à travers une propriété, on pourrait étendre cette définition à des indices $n$ négatifs avec les conjugués.

$$
c_{-n}(f)=\begin{cases}
\frac{1}{2}, \text{ si }n=0
\\
0, n\text{ pair non-zéro}
\\
\frac{1}{-\pi i (-n)}=\frac{1}{\pi i n}=\overline{\frac{-1}{\pi i n}}=\overline{c_n(f)}, n\text{ impair}
\end{cases}
\\[10pt]
\text{ Donc, et en générale, } c_n(f)=\overline{c_n(f)}, \text{ si } f \text{ réelle} 
$$

Donc, en calculant quelques coefficients de Fourier, on obtient…

$$
n\in[-3,3], c_n\in\left\{\frac{1}{-3\pi i},0,\frac{1}{-\pi i},\frac{1}{2}, \frac{1}{-\pi i}, 0, \frac{1}{-3\pi i}\right\}
$$

### Propriétés

- Si $f$ et $g$ continues par morceaux et égales sauf en leurs points de discontinuité, leurs coefficients de Fourier sont égaux.
- Si $f$ est intégrable (intégrale à valeur finie), les coefficients de Fourier de $f$ sont bornés (finis). Rappelons la propriété des intégrales : $\left|\int_0^T h(x)dx\right|\le\int_0^T |h(x)|dx$. Donc, on peut voir que :
    
    $$
    \underbrace{\left|\frac{1}{T}\int_0^T f(x)e^{-\frac{2\pi}{T}ipx}dx\right|}_{c_n} \le \frac{1}{T}\int_0^T|f(x)|\cancel{|e^{-\frac{2\pi}{T}ipx}|}^{\hspace{4pt}=1}dx
    $$
    
- Si $f$ est de classe $\mathcal C^1$, donc

$$
c_n(f^\prime)=\frac{2\pi i n}{T}c_n(f) \iff c_n(f)=\frac{T}{2\pi i n}c_n(f^\prime),\hspace{1pt}n\ne0
$$

## Série de Fourier et théorèmes

### Définition

Rappelons de la définition de coefficients de Fourier qu’ils sont la “quantité” de la harmonique fondamentale d’ordre $p$ dans $f$.

$$
c_p(f)=\lang f, e_p\rang
$$

Donc, la série de Fourier est la somme en appliquant chaque quantité d’harmonique $c_p$ sur l’harmonique $e_p$. On peut aussi parle de la “$N$-ième somme partielle de Fourier”.

$$
\underbrace{S_N(x)}_\text{somme partielle}\hspace{-8pt}=\sum_{-N}^N c_p e^{\frac{2\pi}{T}ipx} \longrightarrow_{N\rightarrow\infty} \underbrace{S_f(x)}_\text{ série}
$$

### Définition alternative, avec harmoniques réelles

La présentation de cette définition (et la démonstration aussi !) se trouve dans l’exercice 3.2 de TD du cours.

Les coefficients de la série se servent de l’harmonique complexe $e^{2\pi i n x}$. On peut définir des coefficients réels $a_n(f)$, $b_n(f)$ et une série de Fourier équivalente qui utilise seulement ces coefficients.

$$
\begin{cases}
a_n(f)=c_n(f)+c_{-n}(f)
\\
b_n(f)=i(c_n(f)-c_{-n}(f))
\end{cases}

\iff 

\begin{cases}
c_n(f)=\frac{a_n(f)-ib_n(f)}{2}
\\[6pt]
c_{-n}(f)=\frac{a_n(f)+ib_n(f)}{2}
\end{cases}

\\[10pt]

\begin{align*}
a_0(f) &=\frac 1 T \int_T f(t)dt
\\[8pt]
a_n(f)&=\frac{2}{T} \int_Tf(t)\cos\left(\frac{2\pi}{T}nt\right)dt, n>0
\\[8pt]
b_n(f)&=\frac{2}{T} \int_Tf(t)\sin\left(\frac{2\pi}{T}nt\right)dt, n>0
\end{align*}
$$

La série de Fourier serait alors :

$$
S_n(f)=\frac 1 2 a_0(f)+\sum_{k=1}^n\left(a_k(f)\cos\left(\frac{2\pi}{T}kx \right)+b_k(f)\sin\left(\frac{2\pi}{T}kx \right) \right)
$$

### La convergence : théorème de Dirichlet

La convergence de la série est la convergence des sommes partielles. La série de Fourier d’une fonction $f$ ne converge pas nécessairement, et, même lorsqu’elle converge en un point $x_0$, sa somme n’est pas toujours égale à $f(x_0)$.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_6.png)

**Théorème de Dirichlet**. Soit $f$ une fonction continue par morceaux, périodique de période $T$. Si $f$ admet en tout point une dérivée à gauche et une dérivée à droite, **donc sa série de Fourier converge en tout point $x_0$**.  De plus,

$$
S_f(x)=\frac{f(x_0^{-})+f(x_0^{+})}{2}
$$

De cette formula, on verra que la série attribue la moyenne sur un point de discontinuité.

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_7.png)

En plus, si $f$ est $\mathcal C^1$ par morceaux et continue, on a la convergence uniforme de la série (ici on parle de la norme sup) :

$$
\lim_{N\to\infty}||S_N-f||_\infty=0 \iff\lim_{N\to\infty}\left(\sup_{x\in[0,T]} |S_N(x)-f(x)|\right)=0 
$$

### Conservation d’énergie : théorème de Bassel-Parseval

Ici, on voit une autre analogie avec le théorème de Pythagore. Rappelons Pythagore dans $\mathbb{R}^n$ : le carré de la norme-deux d’un vecteur et la somme des carrés de ses coefficients (coordonnées) au carré.

$$
\begin{align*}
||v||^2&=\sum_{i=1}^n||P_{\text{vect}(e_i)}(v)||^2
\\
&=\sum_{i=1}^n || \lang v, e_i \rang e_i ||^2
\\
&= \sum_{i=1}^n |\lang v, e_i \rang^2 \cancel{||e_i||^2}^{\hspace{4pt}=1}
\\
&=\sum_{i=1}^n |\lang v, e_i\rang|^2
\end{align*}
$$

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_8.png)

Donc, on en déduit que norme au carre de $f$ est égal à la somme de toutes les coefficients/coordonnées au carré. Ceci est l’**identité de Parseval**.

$$
||S_f||^2= ||f||^2 \iff
\underbrace{\sum_{-\infty}^\infty|c_k|^2}_{||S_f||^2} = \underbrace{\frac{1}{T}\int_0^T|f(u)|^2du}_{||f||^2}
$$

Notons donc que la somme des carrés des coefficients “reconstitue” toute la quantité de l’intégrale du carré de f sur une période, qui est l’énergie. Avec le facteur de $1/T$, c’est plutôt la puissance moyenne, mais le passage à déduire l’énergie est assez simple.

Si on additionne juste une quantité fini de coefficients, de $-N$ à $N$, on obtient l’inégalité de Bessel. Elle devient égalité stricte juste dans le cas de somme de $-\infty$ à $\infty$, que c’est le cas de Parseval.

$$
||S_N||^2 \le ||f||^2 \iff
\underbrace{\sum_{-N}^N|c_k|^2}_{||S_N||^2} \le \underbrace{\frac{1}{T}\int_0^T|f(u)|^2du}_{||f||^2}
$$

# Transformée de Fourier

## Plus besoin de la périodicité

![[https://fr.wikipedia.org/wiki/Transformation_de_Fourier](ressources/02_theorie_du_signal_untitled.gif)

[https://fr.wikipedia.org/wiki/Transformation_de_Fourier](https://fr.wikipedia.org/wiki/Transformation_de_Fourier)

### Motivation et rappels

Dans les séries de Fourier, le signal de base est un signal forcément périodique. S’il n’y a plus de périodicité, on peut avoir toutes les longueurs/fréquences d’ondes sur $\mathbb{R}$ et non plus une fréquence multiple de $1/T$.

Avant d’aborder, quelques rappels. Une fonction $f$ sur $\mathbb{R}$ est localement intégrable si $|f|$ est intégrable sur tout segment. Une conséquence c’est que toute fonction continue par morceaux est localement intégrable. On atteint que **$f$ est intégrable si** $f$ est localement intégrable et $\int_\mathbb{R}|f(x)|dx$ est fini.

La conséquence qui nous intéresse le plus de $f$ intégrable sur $\mathbb{R}$ est que donc la fonction $g(y)= f(x)e^{2\pi i x y}$ intégrable pour $y\in\mathbb{R}$. Le module de l’harmonique vaut $1$.

Quelques exemples d’intégrabilité :

- Si $f$ est intégrable sur $[a,b]$ et $f$ vaut nulle dehors $[a,b]$, $f$ est intégrable sur $\mathbb{R}$.
- $f(x)=\frac{1}{1+x^2}$ est intégrable sur $\mathbb{R}$.
- Si $b>0$, $f(x)=P(x)e^{-b|x|}$ est intégrable sur $\mathbb{R}$, où $P(x)$ est un polynôme.
- $f(x)=P(x)e^{{-x}^2}$ est intégrable sur $\mathbb{R}$.
- Si $f$ continue périodique non nulle, **elle n’est pas intégrable sur $\mathbb{R}$**.
- Si $g$ intégrable et $h$ continue bornée, $gh$ est intégrable sur $\mathbb{R}$.
    - $|h| < M$, donc $|gh| \le M|g|$.

### Définition et interprétation

Si le signal non-périodique $f$ est intégrable sur $\mathbb{R}$, on appelle transformée de Fourier de $f$ la fonction $\hat f$ définie comme :

$$
\hat f (y) = \lang f, e_{1/y}\rang =\int_\mathbb{R} f(x)e^{-2\pi i x y} dx
$$

Notons qu’ici on préfère parler directement de la fréquence de l’harmonique, $y$, plutôt que de sa période, qui serait donc $1/y$. La définition du produit hermitien est la même utilisé dans le cas de séries de Fourier.

L’interprétation est intéressante. Pour chaque $y$, $\hat f(y)$ est la quantité d’harmonique $e_{1/y}$ dans le signal $f$. Quand $y=0$, $\hat f(0)$ est la composante continue de fréquence nulle (constante) du signale, le “baseline”.

$$
\hat f(0)=\int_\mathbb{R} f(u)du
$$

Notons que, si on fait une analogie avec le cas des séries de Fourier où $c_n(f) = \lang f, e_n\rang$, donc on pourrait penser que $\hat f (y)$ est le coefficient $1/y$ de Fourier. On explore ceci dans la section “théorème d’inversion”.

### Propriétés et théorèmes

- Toute fonction continue par morceaux et a support compact (borné) est intégrable et admet donc une transformée de Fourier.
    - Il faut cependant remarquer que la transformée de Fourier d’une telle fonction **n’est jamais a support borné**.
- La transformée de Fourier est une application linéaire. Si $f,g$ intégrables et $\alpha,\beta \in\mathbb{R}$ :
    
    $$
    \widehat{\alpha f+\beta g}=\alpha \hat f + \beta \hat g
    $$
    
    Ceci est permis car le produit hermitien est linéaire à gauche.
    
- Tout comme les séries de Fourier, si $f$ et $g$ sont intégrables et égales sauf en leurs points de discontinuités, elles ont la même transformée de Fourier.
- Si $f$ intégrable, $\hat f$ est une fonction continue et tends vers $0$ à l’infini.
- Si $f,g$ continues par morceaux intégrables, alors

$$
\int_\mathbb{R} \hat f(t)g(t)dt=\int_\mathbb{R} f(t)\hat g(t)dt
$$

- La transformée de Fourier d’une fonction translatée est comme suit. (La computation algébrique est sur les diapos)
    
    $$
    f_a(x)=f(x+a) \iff \hat f_a(y)=e^{2\pi i a y} \hat f(y)
    $$
    

### Rapport différentiation-Fourier

Par rapport aux dérivées, la transformée de Fourier apparaît dans quelques équations intéressantes. En particulier, on s’intéresse en premier temps à la dérivé de la transformée $(\hat f)^\prime$, puis à la transformée de la dérivé $\widehat{(f^\prime)}$.

Pour la dérivé de la transformée $(\hat f)^\prime$, il y a une condition importante a vérifier : $f$ intégrable mais aussi $g(t)=tf(t)$ intégrable :

$$
(\hat f)^\prime(y)=\widehat{-2\pi i t f}(y)
$$

Pour la transformée de la dérivé $\widehat{(f^\prime)}$, il faut que $f$ soit de classe $\mathcal C^1$ (différentiable et dérivé continue), et aussi $f$ et $f^\prime$ intégrables. Il existe aussi un cas générale $k$ :

$$
\widehat{(f^\prime)}(y)=2\pi i y \hat f(y)
\\[5pt]
\widehat{(f^{(k)})}(y)=(2\pi i y)^k \hat f(y)
$$

### Théorème d’inversion et théorème de Parseval

La synthèse harmonique n’est possible que si l’on peut, a partir d’une transformée de Fourier, revenir au signal temporel. Le théorème suivant montre en quelque sorte que $\hat f$ caractérise la fonction $f$.

Notons déjà que $\hat f (y)$ pourrait être vu comme le coefficient $1/y$ de Fourier. **Est-ce que l’analogie se tienne ?**

$$
\text{Série : } c_n(f) = \lang f, e_n \rang \to \lim_{N\to\infty} \sum_{n=-N}^N c_n(f) e^{\frac{2\pi}{T}inx} = f(x)
\\
\text{Transf. : } \hat f(y)= \lang f, e_{1/y}\rang \to \int_\mathbb{R} \hat f(y) e^{2\pi xyi}dy \space\underbrace{=}_?\space f(x)
$$

Déjà, notons que telle intégrale serait juste la transformée de la transformée de Fourier. En plus, si $f$ continue intégrable et $\hat f$ intégrable, donc la égalité est vérifiée. Ceci est le **théorème d’inversion**.

$$
\int_\mathbb{R} \hat f(y) e^{2\pi xyi}dy = \widehat {(\widehat f)}=f(-x)
$$

- Si $f$ et $g$ continues intégrables, $\hat f$ et $\hat g$ intégrables et égales, alors $f=g$.

Finalement, un autre théorème utile est le **théorème de Parseval**, différent de l’identité de Parseval. Si $f$ et $g$ intégrables et leurs transformées de Fourier $\hat f$ et $\hat g$ aussi, donc le produit hermitien des transformées est égal au produit hermitien des signaux.

$$
\int_\mathbb{R} \hat f \bar{\hat g}dx=\int_\mathbb{R} f\bar g dx
$$

- Un corollaire est que si $g=f$, $\int_\mathbb{R} |\hat f|^2dx=\int_\mathbb{R} |f|^2dx$, càd. l’énergie de la transformée équivaut l’énergie du signal.

### Questions :

- Graphique magnitude v. fréquence ????
- Utilités :
    - Delta de Dirac, définition dérivée de Fourier : [https://mathworld.wolfram.com/DeltaFunction.html](https://mathworld.wolfram.com/DeltaFunction.html)
    - Transformée de sin(x) et cos(x) : [https://www.tutorialspoint.com/fourier-transform-of-the-sine-and-cosine-functions](https://www.tutorialspoint.com/fourier-transform-of-the-sine-and-cosine-functions)
    - Transformée de Fourier de sin(x) selon Wolfram : 
    [https://mathworld.wolfram.com/FourierTransformSine.html](https://mathworld.wolfram.com/FourierTransformSine.html)
    Il semble qu’il faut normaliser/paramétriser le truc ????
    - [https://en.wikipedia.org/wiki/Fourier_transform](https://en.wikipedia.org/wiki/Fourier_transform)
    - [https://en.wikipedia.org/wiki/Dirac_comb](https://en.wikipedia.org/wiki/Dirac_comb)
    - [https://en.wikipedia.org/wiki/Dirichlet_kernel](https://en.wikipedia.org/wiki/Dirichlet_kernel)
    - [https://en.wikipedia.org/wiki/Band-pass_filter](https://en.wikipedia.org/wiki/Band-pass_filter)
    - [https://en.wikipedia.org/wiki/Spectral_density](https://en.wikipedia.org/wiki/Spectral_density)

## Table des transformées fréquentes

![untitled](new/uga/l3/s5/math/s5_math_comple_maths_1/ressources/02_theorie_du_signal_untitled_9.png)

# Traitement de signal

## Convolution

Soit $f$ une fonction intégrable. Pour éliminer des fréquences gênantes dans le spectre de $f$, il suffit de multiplier, par exemple, $\hat f$ par une fonction $g$ nulle hors d'un intervalle $[a, b]$ (on parle alors de filtre passe-bas, passe-haut et passe-bande.

Soit $H(y)=\hat f(y)\hat g(y)$ une fonction continue par morceaux nulle hors de $[a,b]$, donc intégrable. Supposons que $H$ est la transformée de Fourier d'une certaine fonction qu'on ne connaît pas, disons $h(x)$. Alors, par le théorème d'inversion :

$$
\begin{align*}
h(x) &= \int_\mathbb{R} H(y)e^{2\pi i xy}dy
\\
&= \int_\mathbb{R} \left( \int_\mathbb{R} f(u)e^{-2\pi u y}\right) \hat g(y)e^{2\pi i xy}dy
\\
&= \int_\mathbb{R} f(u) \left( \int_\mathbb{R} \hat g(y)e^{-2\pi i (u-x)y}dy\right )du
\\
&=\int_\mathbb{R} f(u)g(x-u)du
\end{align*}
$$

En fait, cette dernière écriture est appelée le produit de convolution.

$$
f\star g(x) = \int_\mathbb{R} f(u)g(x-u)du
$$

Comme propriétés, on observe que :

- $f\star g(x) = g \star f(x)$
- Si $f,g$ intégrables, donc $\widehat{f\star g}=\hat f \hat g$.
Autrement dit, la transformation de Fourier transforme un produit de convolution en produit ordinaire. Ceci explique, en partie, l’intérêt de la convolution pour le filtrage.
- Si $f,g$ intégrables, et aussi $fg, \hat f$ et $\hat g$ intégrables, donc $\widehat{(fg)}=\hat f \star \hat g$.
Ceci est juste l’égalité précédente en utilisant le théorème d’inversion.

## Rapport support-différentiation-Fourier

Soit $I$ un intervalle de bornes $a,b$ qui est ouvert, semi-ouvert ou fermé. L’adhérence de $I$ est l’ensemble de points de $\mathbb{R}$ qui est le plus petit fermé qui contient $I$. Tout ça pour dire, l’adhérence de I est l’intervalle fermé de bornes $a$ et $b$ : $[a,b]$.

- Si $A, B$ parties de $\mathbb{R}$, on note l’ensemble $“A+B”=\{a+b\in \mathbb{R}: a\in A, b\in B\}$.
- Si $f,g$ continues par morceaux à supports bornés, $f\star g$ à support borné et $\text{supp}(f\star g)\sub\text{supp}(A) + \text{supp}(B)$.

Finalement, il résulte du théorème de dérivation sous le signe intégral que si $f$ est intégrable et $g$ de classe $\mathcal C^∞$ a support compact (borné), $f ⋆ g$ est de classe $\mathcal C^∞$ et

$$
(f \star g)^{(k)}=f\star (g^{(k)})
$$