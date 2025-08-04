# 04 // ANOVA : analyse des variances

[Slides d’ANOVA](ressources/04_anova_analyse_des_variances_slides_anova_1_stat1_annote.pdf)

# Régression linéaire pour les variables qualitatives

## Le passage de $X$ à $\xi$

Reprenons notre modèle de régression linéaire :

$$
Y=\beta_1\underbrace{\xi}_X+\beta_0+\epsilon
$$

Dans la littérature statistique, on va trouver souvent la variable explicative comme $\xi$ au lieu de $X$. Le changement n’est pas seulement esthétique, par contre. Dans l’exemple passé, $X$ était de nature quantitative. On ira plus loin essayant d’**établir une régression linéaire sur une variable explicative *qualitative***, d’où le changement à $\xi$. Idéalement, on voudrait regrouper les valeurs de $X$ dans des groupes/échantillons dont la propriété commune est la valeur de $\xi$.

On trouve, par contre, un problème : une régression linéaire ne fait plus de sens quand $\xi$ est une qualité et non pas une qualité, et non plus le produit $\beta_1\xi$. On donnera une valeur quantitative à $\xi$ représentant une qualité.

## Facteur à deux modalités

Par exemple, supposons qu’on mène un étude scientifique où on veut observer la différence d’un caractéristique de patients quand ils prennent un traitement expérimental vs. un placébo. L’échantillon qui prend le traitement et noté $n_1$, et $n_2$ pour ceux prenant le placébo.

$$
n_1=\{X_{1,1},X_{1,2},\dots,X_{1,| n_1|}\},\space \xi=\xi_1
\\
n_2=\{X_{2,1},X_{2,2},\dots,X_{2,|n_2|}\},\space \xi=\xi_2
$$

On a donc deux échantillons possiblement différentes, et donc deux régressions linéaires différentes qu’on pourrait appliquer, chacune avec sa propre valeur de $\xi_i$.

Par le théorème centrale, quelle que soit la loi que suivent les observations, les échantillons $n_1$ et $n_2$ suivent une loi normale de moyenne $\mu$ et d’une variance $\frac{\sigma^2}{|n_i|}$, où $|n_i|$ est la taille de l’échantillon $i$.

Le but de l’analyse de variance ou ANOVA est de savoir si, en fait, la moyenne des deux échantillons est la même o non. Si la moyenne est la même, alors $\xi_1=\xi_2$, donc le facteur n’a pas d’effet sur les observations. Comme on fait souvent en statistique, on déclare l’hypothèse nulle $\mathcal{H}_0 : \mu_1=\mu_2=\mu \iff "\xi\text{ n'explique pas }X"$ , puis on veuille à la rejeter.

Quand c’est seulement deux échantillons, et donc deux moyennes $\bar{X}_1$ et $\bar{X}_2$, l’objectif devient $\mathcal{H}_0: \bar{X}_1 - \bar{X}_2 = 0$. Pour un statistique qui prend la forme de la différence de deux moyennes échantillonnales, on peut utiliser la variable $t$ de Student : $t=\frac{\bar{X}_1 - \bar{X}_2}{S_{\bar{X}_1 - \bar{X}_2}}$.

## Facteur à $n$ modalités

Rien empêche qu’on puisse généraliser à $n$ échantillons. L’hypothèse nulle $\mathcal{H}_0$ devient donc :

$$
\mathcal{H}_0:\mu_1=\mu_2=\dots=\mu\iff"\xi\text{ n'explique pas }X"
$$

Comment on peut dire si les moyennes sont le mêmes ou non ? On peut partir par regarder la déviation carrée de chaque moyenne empirique échantillonnale par rapport à la moyenne empirique populationnelle. Cette statistique s’appelle la somme des carrés due au modèle :

$$
SCM=\sum_{i=1}^nn_i(\bar{X}_i-\bar{X})^2
$$

On s’attend à ce que $SCM$ soit très proche de zéro si $\mathcal{H}_0$ est vraie. On prendra comme deuxième statistique $\bar{X_i}-\mu$, et on en fera deux observations :

1. Telle statistique s’estime $\bar{X_i}-\bar{X}$.
2. Sous $\mathcal{H}_0$, elle est égale à $\bar{\epsilon}_i$, la moyenne des erreurs de chaque observation dans l’échantillon $i$ par rapport à la moyenne réelle de l’échantillon $i$.

Avec un peu d’algèbre et de quelques propriétés, on arrive à ce qui suit :

$$
\begin{align*}
&Var(X_i-\mu)=Var(\bar{\epsilon}_i)
\\
\text{}
\\
&=Var\left(\frac{1}{|n_i|}\sum_{j=1}^{|n_i|}\epsilon_{i,j}\right)
&
\\
\text{}
\\

&=\frac{1}{|n_i|^2}Var\left(\sum_{j=1}^{|n_i|}\epsilon_{i,j}\right),
&\text{la variance est quadratique}
\\
\text{}
\\

&=\frac{1}{|n_i|^2}\sum_{j=1}^{|n_i|}\underbrace{Var(\epsilon_{i,j})}_{\sigma_\epsilon^2},
&\text{ les erreurs sont iid.}
\\
\text{}
\\

&=\frac{1}{|n_i|^2}\sum_{j=1}^{|n_i|}\sigma_\epsilon^2
&
\\
\text{}
\\

&=|n_i|\frac{\sigma^2_\epsilon}{|n_i|^2}
&
\\
\text{}
\\

&=\frac{\sigma_\epsilon^2}{|n_i|}
&
\end{align*}
$$

Alors, c’est quoi $\sigma^2_\epsilon$, la variance des erreurs ? Voyons :

$$
\begin{align*}
\sigma^2_\epsilon
&=\frac{1}{n-a}\sum_{i=1}^a\sum_{j=1}^{n_i}(\epsilon_{i,j}-\bar{\epsilon})^2
&
\\

&=\frac{1}{n-a}\sum_{i=1}^a\sum_{j=1}^{n_i}\epsilon_{i,j}^2 &\bar{\epsilon}=0\text{, par hypothèse}
\\

&=\frac{1}{n-a}\underbrace{\sum_{i=1}^a\sum_{j=1}^{n_i}(X_{i,j}-\bar{X}_i)^2}_{SCE}
&
\end{align*}
$$

$SCE$ signifiant ici somme des carrés des erreurs. Comme on veut estimer le paramètre réel $\sigma^2_\epsilon$ et l’expression finale de dépend des observations et statistiques des observations, $\frac{SCE}{n-a}$ sert comme un estimateur de $\sigma^2_\epsilon$. 

### Mettant tout ensemble

Observons ce qu’on a :

- $SCM/(a-1)$ est une somme de carrés de variance $\sigma^2 \implies \frac{SCM}{\sigma^2}\sim\chi^2(a-1)$
- $\frac{SCE}{n-a}$ est une somme de carrés qui estime $\sigma^2_\epsilon \implies \frac{SCE}{\sigma^2_\epsilon}\sim\chi^2(n-a)$

La variable statistique finale sera $F=\frac{SCM/(a-1)}{SCE/(n-a)}\sim\mathcal{F}_{a-1,n-a}$, une variable de Fisher. Le critère pour rejeter $\mathcal{H}_0$ est que la probabilité d’observer le $F$ qu’on observe soit très petite,  Ceci correspond à une valeur de la statistique même $F$ très grand, donc un $SCM$ très grand où un $SCE$ très petit.

Formellement, on rejette $\mathcal{H}_0$ seulement si :

$$
F\ge q_{1-\alpha}^{\mathcal{F}_{a-1,n-a}}
$$

où $q$ est le quantile d’ordre $(1-\alpha)$ de la loi, càd la valeur seuil de $F$ pour qu’on puisse rejeter l’hypothèse.

## Revue de l’équation de la variance

Pour la dispersion totale, posons de plus la “somme de carré totale” pour la dispersion totale :

$$
SCT=\sum_{i=1}^a\sum_{j=1}^{n_1}(X_{i,j}-\bar{X})^2
$$

On peut établir l’équation de la variance suivante :

$$
SCT=SCM+SCE
$$

Cette décomposition met en évidence le fait que la dispersion totale des données ($SCT$) est formée d’une partie ($SCM$) expliquée par le fait que les populations sont différentes, et d’une autre partie ($SCE$) qu’on attribue au hasard. Autrement dit, $SCE$ représente les différences individuelles alors que $SCM$ représente les différences entre les groupes.

On rejette l’hypothèse que les populations d’origine des groupes sont de même moyenne si les différences entre les groupes sont trop grandes par rapport aux différences individuelles. Cette analyse est appelée *analyse de variance*.

Les calculs se font aisément à l’aide des formules suivantes :

$$
SCM=\sum_{i=1}^a n_1\bar{X}_i^2-n\bar{X}^2
\\
SCT=\sum_{i=1}^a\sum_{j=1}^{n_i}X^2_{i,j}-n\bar{X}^2
\\
SCE=\sum_{i=1}^a\sum_{j=1}^{n_i}X^2_{i,j}-\sum_{i=1}^a n_i\bar{X_i}^2
$$

![untitled](ressources/04_anova_analyse_des_variances_untitled.png)