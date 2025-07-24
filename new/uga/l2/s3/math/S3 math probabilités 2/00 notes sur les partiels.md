# 00 // notes sur les partiels

Date de création: October 26, 2022 4:10 PM
Modifié: June 9, 2023 1:58 PM

# Contrôles de l’année passée

## Évaluation d’une intégrale suite à IPP

J’ai tendance à faire un erreur quand j’intégre par parties une intégrale indéfinie : l’évaluation de l’intégrale de départ passe à l’intégral $-\int vdu$, et non à toute l’expression $uv-\int vdu$.

$$
\text{Correct :} \int_0^\infin x^2e^xdx = \left[x^2e^x - 2\int x e^xdx\right]^\infin_0

\\

\text{Incorrect :} \int_0^\infin x^2e^xdx = x^2e^x - 2\int^\infin_0 x e^xdx
$$

## Intégration des fonctions paires et impaires

Il existe une astuce par rapport aux fonctions paires et impaires, et leurs intégrales définies sur des intervalles symétriques $[-a,a]$. On peut voir l’intuition visuelle juste en bas.

$$
\begin{align*}

f(x) \text{ paire} &: f(x)=f(-x) \implies \int_{-a}^af(x)dx = 0

\\

f(x) \text{ impaire} &: f(x)=-f(x) \implies \int_{-a}^af(x)dx = 2\int_{0}^af(x)dx

\end{align*}
$$

![Fonction paire, notons que l’aire entre la courbe et l’axe x s’annule elle-même.](new/uga/l2/s3/math/S3%20math%20probabilités%202/00%20notes%20sur%20les%20partiels/Untitled.png)

Fonction paire, notons que l’aire entre la courbe et l’axe x s’annule elle-même.

![Fonction impaire, notons que l’aire est symétrique autour de l’axe y. Il est utile de calculer l’aire seulement d’un côté et le multiplier par 2 pour trouver tout l’aire. ](new/uga/l2/s3/math/S3%20math%20probabilités%202/00%20notes%20sur%20les%20partiels/Untitled%201.png)

Fonction impaire, notons que l’aire est symétrique autour de l’axe y. Il est utile de calculer l’aire seulement d’un côté et le multiplier par 2 pour trouver tout l’aire. 

## Relation entre LGN et TCL

Soit $\bar{X}_n$ la moyenne empirique de $n$ V.A. iid. Donc :

- Loi des Grands Nombres : tant que $n \rightarrow \infin$, la distance entre $\bar{X}_n$ et $\mathbb{E}[X]$ devient plus petite que tout nombre réel $a>0$ avec probabilité $1$.
- Théorème Centrale de la Limite : tant que $n \rightarrow \infin$, la V.A. $\bar{X}_n$ converge en loi vers $\mathcal{N}(0, \frac{\sigma^2}{n})$.

Il faut laisser clair une chose : la moyenne empirique toujours va converger vers la moyenne théorique. Toujours. On peut réécrire les deux théorèmes comme suite, $a > 0$ :

$$
\begin{align*}

\text{LGN :} & \lim_{n\rightarrow\infin} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = 1

\\

\text{TCL :} & \lim_{n\rightarrow\infin} \mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) = \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx \space (*)

\end{align*}

\\
\\[8pt]
(*): \text{cette dernière formulation du TCL est incorrecte ! voir note dessous.}
$$

D’un côté, il semble que $(\bar{X}_n-\mathbb{E}[X])$  tend vers $0$. Au même temps, il semble que c’est égale à l’intégrale. Donc, lequel des deux ? La première.

Il existe un problème avec la deuxième : si $n \rightarrow \infin$, la variance devient $0$, et la variance comme telle n’est pas utile
$$. Imaginons la courbe qui viendrait si la variance était $0$ : il n’existe pas de dispersion autour de la moyenne et $\bar{X}_n$ serait toujours égal à $\mathbb{E}[X]$, càd. $(\bar{X}_n-\mathbb{E}[X])$ serait toujours égal à $0$.

![Untitled](new/uga/l2/s3/math/S3%20math%20probabilités%202/05%20cadre%20général%20théorème%20centrale%20de%20la%20limit/Untitled.png)

$$
F(x)=
\begin{cases}
0, x < 0 \\
1, x \ge 0
\end{cases}
$$

![Untitled](new/uga/l2/s3/math/S3%20math%20probabilités%202/05%20cadre%20général%20théorème%20centrale%20de%20la%20limit/Untitled%201.png)

$$
"f(x)"=
\begin{cases}
1, x=0 \\
0, x \ne 0
\end{cases}
$$

Il est correct de construire une fonction de répartition qui représenterait la fonction de répartition de $(\bar{X}_n-\mathbb{E}[X])$. En fait, une variable aléatoire avec telle fonction de répartition est appelée une **variable aléatoire dégénérée**.

Par contre, il n’est pas possible de construire une densité, car il devrait avoir une aire sous la courbe égale à $1$ quand $x=0$, mais ce n’est pas possible, car le “rectangle” sous $f(x)$ n’as pas de ampleur, donc son aire est toujours $0$.

Le choix de multiplier $(\bar{X}_n-\mathbb{E}[X])$ par $\sqrt{n}$ permet de laisser tendre $n$ vers l’infini et que la variance ne soit pas nulle. Particulièrement, on garanti l’existence d’une variance non-nulle, mais aussi non-infinie, c’est qui nous est utile.

<aside>
💡 On pourrait concevoir deux formes de présenter le TCL : la réelle et la pratique.

$$
\begin{align*}

\text{TCL réel : }
\lim_{n\rightarrow\infin} \mathbb{P}(-a\le\sqrt{n}(\bar{X}_n-\mathbb{E}[X]) \le a) &= \int_{-a}^a \mathcal{N}\left(0,\sigma^2\right)dx

\\

\text{TCL pratique : }
\mathbb{P}(-a\le\bar{X}_n-\mathbb{E}[X] \le a) &\approx \int_{-a}^a \mathcal{N}\left(0,\frac{\sigma^2}{n}\right)dx

\end{align*}
$$

Il ne faut absolument pas appliquer une limite $\lim_{n \rightarrow \infin}$ dans la formulation pratique. Il sert comme une bonne approximation à partir de $n \ge 30$, mais **il ne fait objectivement plus de sens si on laisse $n$ tendre vers l’infini !** Je l’avais fais en dessus pour expliquer le besoin d’ajouter le facteur $\sqrt{n}$.

</aside>

# CC1

#1.a. : si le test d’Alembert $\lim_{n\longrightarrow\infin} |\frac{u_{n+1}}{u_n}|$ ne converge pas, le test est inconclusif de la même manière que si l’expression égal $1$.

#2.a. : on peut re-indexer la somme pour réécrire le terme général et appliquer propriétés de fractions ou exposants ou etc.

$$
S=\sum_{k=0}^\infin \frac{k}{(k+1)!} \implies S=\sum_{k=1}^\infin \frac{k-1}{k!} = \sum_{k=1}^\infin \frac{k}{k!} - \sum_{k=1}^\infin \frac{1}{k!} 
$$

#2.e : pense à des séries qui ont des termes qui alternes mais que leurs séries de Taylor de base ne sont pas alternants. Il se peut que le $(x)$ dans le Taylor soit $(-x)$. **Fais gaffe ! Si la Taylor de $e^x$ commence dès $k=0$, il faut soustraire le première terme !!!** Par exemple :

$$
e^x = \sum_{k=0}^\infin \frac{x^k}{k!}=1+\frac{x}{1!}+\dots \implies e^{-x}=\sum_{k=0}^\infin \frac{(-x)^k}{k!}=1-\frac{x}{1!}+\frac{x^2}{2!}-\frac{x^3}{3!}+\dots
$$

# CC2

Mec, en vrai il faut intégrer plus vite.