# 03 // estimation non paramétrique et fonctionnelle

# Motivation

## La loi mère est inconnue !

L’estimation non paramètre vient quand on considère que la loi mère—la loi suivie par les observations iid. qui composent un échantillon—ne fait pas partie d’une famille paramétrable de lois.

Il ne peut donc plus s’agir ici d’estimer un paramètre qui déterminerait totalement la loi et par suite toute caractéristique de celle-ci. Dès lors deux orientations sont possibles :

- Estimation non paramétrique ponctuelle : on s’intéresse uniquement à quelques valeurs caractéristiques de la loi
- Estimation fonctionnelle : on veut estimer la loi dans sa globalité par sa fonction de répartition ou sa densité, ou sa fonction de probabilité

# Estimation non paramétrique (ponct. et par IC)

## Estimation de $\mu$ et $\sigma^2$

### Estimant $\mu$

Rappelons quelques faits importants pour la suite : 

- Les moments empiriques simples ou centrés, s’ils existent, sont des estimateurs sans biais des moments correspondants de la loi mère
- Comme conséquence de la LGN, ces estimateurs sont convergents presque sûrement
- Pour que le moment d’ordre $k$ converge, il suffit que $\mathbb E[|X^k|]$ existe.

Pour un sondage d’une population ***finie***, ces conditions sont donc réunies, ceux-ci étant des caractéristiques descriptives de la population dans son ensemble. Soit $\mu$ et $\sigma^2$ la moyenne et la variance de la loi inconnue en question (supposant qu’elles existent), et soit $n\ge 30$, donc

$$
\mathbb E[\bar X] = \mu\hspace{8pt}\text{ et\hspace{8pt} Var}(\bar X)=\frac{\sigma^2}{n}
$$

La première relation reflétant un biais nul et la deuxième montrant directement la convergence en moyenne quadratique. En conclusion, nous utiliserons naturellement la moyenne empirique pour estimer la moyenne de la loi, nous satisfaisant de ces propriétés.

<aside>
💡 Il n’est pas possible de dire si tel est le meilleur choix possible, sauf à imposer des conditions restrictives sur la nature de la loi mère, ce qui n’est pas dans l’esprit de l’estimation non paramétrique.

</aside>

En plus, et aussi grâce à $n\ge 30$ (pour TCL) et la convergence de $S^2$ vers $\sigma^2$, pour n'importe quelle loi des $X_i$, on a que

$$
\frac{\bar X-\mu}{S/\sqrt n}\sim\mathcal T_{n-1}
$$

Donc, indifférent de la loi des $X_i$, on peut avoir un IC classique (à $95\%$) pour le paramètre $\mu$ :

$$
IC_{95\%}(\mu)=\left[\bar X-t_{97.5\%}^{(n-1)}\frac{S}{\sqrt n}, \bar X+t_{97.5\%}^{(n-1)}\frac{S}{\sqrt n} \right]
$$

### Influence de valeurs extrêmes ou aberrantes sur $\bar X$

Il a été dit qu’en principe $n ≥ 30$ suffit. Cependant, l’approximation par une loi de Student posera problème pour des VA dont les queues de distribution sont allongées et peuvent produire des observations très éloignées du centre.

Une valeur très excentrée va influencer fortement la valeur de $X_i$ et encore plus, car  interviennent des écarts au carré, celle de la variance $S^{2^\prime}$, rendant ainsi ces statistiques trop instables pour garantir l’approximation par une loi de Student si la taille de l’échantillon n’est pas très élevée.

Pour les mêmes raisons, si les observations sont contaminées par des valeurs aberrantes l’approximation sera défaillante. Ceci peut provenir, par exemple, d’erreurs dans le recueil des informations ou de présences de valeurs étrangères au phénomène étudié (dans les sondages, présence d’individus distincts n’appartenant pas à la population).

Si l’on soupçonne la présence de valeurs très extrêmes ou aberrantes, on peut soit éliminer purement et simplement les valeurs trop éloignées par examen de la distribution des  observations (histogramme), soit réduire leurs poids dans le calcul de la moyenne et de la variance. On définit ainsi des $M$-estimateurs dont l’étude des propriétés fait l’objet de la théorie de la robustesse.

### Estimant $\sigma^2$

De la même manière qu’on construit une statistique sur $\bar X$ “centrée-réduite”,$\left(\frac{\bar X - \mu}{S/\sqrt n} \right)$, qui suit une loi connue (Student), on peut faire de même avec la variance empirique $S^{2^\prime}$, **sous la condition stricte que les $X_i$ suivent forcément une loi gaussienne** :

$$
\frac{(n-1)S^{2^\prime}}{\sigma^2}\sim\chi^2_{n-1}
$$

Par contre, dans cette section, on a présumé qu’on ne connaît absolument pas la loi qui suivent les $X_i$. Si cette loi n’est pas gaussienne, on ne peut plus affirmer que telle statistique sur $S^{2^\prime}$ suit une loi de $\chi^2$, **même si $n$ tend vers l’infini**.

Ok, on laisse tomber telle statistique de $\frac{(n-1)S^{2^\prime}}{\sigma^2}$. Ceci dit, on peut dire que $S^{2^\prime}$ tout courte suit elle-même une loi gaussienne. Ici, on devrait faire une petite note :

<aside>
💡 Comme pour la loi des grands nombres il existe différentes versions du TCL partant de conditions plus ou moins restrictives.

En particulier, il n’est pas nécessaire que les VA soient de même loi ni même qu’elles soient indépendantes dans la mesure ou leur degré de dépendance reste faible. Ceci explique que certains phénomènes naturels répondent bien a un
modèle gaussien du fait que la variable étudiée résulte de l’addition d’effets aléatoires multiples.

Ainsi, on peut établir un comportement asymptotique gaussien pour d’autres types de statistiques dans la mesure ou elles sont des moyennes de VA qui, sans être nécessairement indépendantes pour $n$ fini, tendent à être iid. quand $n → ∞$.

</aside>

Ceci est le cas pour $S^{2^\prime}$ : les élément $(X_i-\bar X)$  (et donc leur carrés) tendent à devenir indépendants du fait que $\bar X$ converge vers $\mu$. Il est toutefois nécessaire que $\text{Var}(S^{2^\prime})$ existe, mais ceci est garanti si $\mu_4=\mathbb E [X^4]$ existe aussi, qui est le raccourci qu’on utilise le plus souvent.

Avant d’établir la loi de $S^{2^\prime}$ qui nous intéresse, il faut mentionner un fait important pour le calcul :

$$
\mathbb E[S^{2^\prime}]=\sigma^2 \hspace{8pt}\text{et}\hspace{8pt}\text{Var}(S^{2^\prime})=\frac{1}{n}\left(\mu^\prime_4-\frac{n-3}{n-1}\sigma^4\right), \text{où }\mu^\prime_4=\mathbb E[(X-\bar X)^4]
$$

Finalement, on peut établir la loi de $S^{2^\prime}$ asymptotique à une Gaussienne comme suit, qui est juste une application du TCL “théorique et original” :

$$
\lim_{n\rightarrow\infin}

\frac{\sqrt n (S^{2^\prime}-\sigma^2)}{\sqrt{\mu^\prime_4-\sigma^4}}

\sim\mathcal N(0,1)
$$

### Un IC dans le cas non paramétrique pour $\sigma^2$

On peut réécrire cette dernière statistique pour arriver à une plus pratique :

$$
\frac{\sqrt n (S^{2^\prime}-\sigma^2)}{\sqrt{\mu^\prime_4-\sigma^4}}=\frac{\sqrt n (S^{2^\prime}-\sigma^2)}{\sigma^2\sqrt{\underbrace{(\mu^\prime_4/\sigma^4)}_\text{Curt.}-1}}
$$

Le terme marqué $(\mu^\prime_4/\sigma^4)$ est connu comme le *coefficient de curtose*. Il vaut $3$ pour la loi Gaussienne, plus de $3$ pour un loi à pic plus prononcé, et moins de $3$ pour un pic plus plat.

Dans le cas Gaussien, cette expression est bien la version centrée et réduite de $\frac{(n-1)S^{2^\prime}}{\sigma^2}$ au facteur $\sqrt{(n-1)/n}$ près, puisque la loi $\chi^2_{n-1}$ est de moyenne $(n-1)$ et de variance $2(n-1)$. Par ailleurs, la loi de $\chi^2$ tend à devenir gaussienne quand $n$ tend vers l’infini.

Finalement, pour construire un intervalle de confiance asymptotique, on peut envisager d’estimer $(\mu^\prime_4-\sigma^4)$ par sa version empirique $(M^\prime_4-S^4)$, ou également le coefficient de curtose par la curtose empirique $(M^\prime_4/S^4)$, mais la convergence est lente et un $n$ trop grand sera nécessaire pour espérer une bonne approximation.

On peut recourir à une approche dite par rééchantillonnage dont l’intérêt est général et c’est pourquoi nous y consacrons une section spécifique. Cette approche sera également appropriée pour l’estimation de l’écart-type.

## Estimation de quantiles

### Définition et notes

Un quantile d’ordre $p$ est la quantité sur la loi de distribution tel qu’elle “sépare” la population et contient $p\%$ de la population à sa gauche.

$$
\kappa_{p} : F(\kappa_p)=p  \iff \kappa_p=F^{-1}(p)
$$

Notons que, étant donné une loi, la probabilité d’observer une valeur $x\le \kappa_p$ est égale à $p$. Une autre interprétation importante sont les quantiles comme des “points de coupure” car la valeur $\kappa_p$ divise la loi en $p\%$ à sa gauche et $(1-p)\%$ à sa droite. 

Il faut clarifier, à nouveau, que les quantiles sont des points de coupure sur la loi (densité, dans ce cas). Mais ce chapitre traite les cas d’une loi non connue, et qu’on en observe un échantillon.

**Note pratique**. On sait que la fonction de répartition devrait avoir une inverse car elle est injective (croissante) et surjective, donc bijective et donc inversible.

### Notation et premiers théorèmes

Normalement on adopte la notation “le $k$-ième $q$-quantile” théorique pour le point $k/q$, ou simplement $p$ pour exprimer un nombre réel sans se soucier de trouver $k$ et $q$ pour représenter le quantile. Si on parle d’un échantillon/population de taille $n$ particulier, son $k$-ième $q$-quantile est $n\frac{k}{q}$ ou $np$.

Avant de continuer, on note $\kappa_p$ le quantile $p$ de la population (et donc $\kappa_p=F^{-1}(p)$) et $\hat\kappa_p$ l’estimateur du précédent, qui on va définir comme tout simplement le quantile $p$ de l’échantillon. Si on suppose une densité continue $f$, on a donc

$$
\lim_{n\rightarrow\infin} n\text{Var}(\hat\kappa_{\lfloor np\rfloor +1})=\frac{p(1-p)}{f(\kappa_p)^2}

\text{\hspace{6pt}et\hspace{6pt}}

\lim_{n\rightarrow\infin}\frac{f(\kappa_p)}{\sqrt{p(1-p)}}\sqrt n(\hat\kappa_{\lfloor np\rfloor +1}-\kappa_p)\sim\mathcal N(0,1)

\\[10pt]

\text{Formulation plus pratique : } \hat\kappa_p \sim \mathcal N\left(\mu=\kappa_p,\hspace{4pt} \sigma^2=\frac{p(1-p)}{nf(\kappa_p)^2}\right) \text{si }n\text{ fini}
$$

Ceci nous permet de conclure que la quantile empirique $\hat\kappa_p$ est asymptotiquement sans biais et converge en moyenne quadratique vers sont estimande $\kappa_p$ puisque sa variance tend vers $0$ (on peut aussi montrer qu’elle converge presque sûrement).

### Construire un IC de $\kappa_p$

Par contre, on a un souci : $f(\kappa_p)$ est inconnu. L’objectif c’est donc d’estimer ponctuellement $f(\kappa_p)$ pour construire un IC de $\kappa_p$. On sait que si on prend une observation $X_i$ d’une loi, celle-ci a probabilité $p$ d’être inférieur ou égale à $\kappa_p$ et $1-p$ sinon. Ceci est donc juste une loi de Bernoulli.

Pour un échantillon $n$ à plusieurs observations, on appelle $n_\text{inf}$ la quantité d’observations inférieures ou égales à $\kappa_p$, ce qui serait une loi binomiale. Donc $n_\text{inf}\sim\mathcal B(n, p)$ ou 

$$
\mathbb P(\ell_1\le n_\text{inf} \le \ell_2) = \sum_{k=\ell_1}^{\ell_2} \binom{n}{k}p^k(1-p)^{n-k}
$$

Les $\ell_1$ et $\ell_2$ sont des limites pour encadrer. Ici, on veut se fixer deux tâches :

- On veut choisir leurs valeurs tel que $\mathbb P(\ell_1\le n_\text{inf} \le \ell_2) \ge 0.95$ et quand même bien proche aussi de $0.95$.
- On veut $\ell_1+\ell_2=n$ ou au moins une approximation de $n$, ce qui permettra que l’intervalle $[\ell_1, \ell_2]$ soit le plus symétrique possible autour de $n/2$, et donc le plus étroit.

Une observation clé c’est que, si on choisit $\ell_1$ tel qu’il est vrai que $(X_{(\ell_1)} \le\kappa_p)$, donc il est impliqué qu’il existe ***au moins*** une quantité $\ell_1$ d’observations inférieures ou égales à $\kappa_p$, et donc c’est une équivalence avec la proposition $(\ell_1\le n_\text{inf})$. De même avec $(\kappa_p \le X_{(\ell_2+1)})$ et $(n_\text{inf} \le \ell_2)$. Mettant tout ensemble :

$$
\mathbb P(\ell_1\le n_\text{inf} \le \ell_2) = \mathbb P(X_{(\ell_1)}\le\kappa_p\le X_{(\ell_2+1)}),

\\[10pt]

\text{et donc}

\\[6pt]

\mathbb P(X_{(\ell_1)}\le\kappa_p\le X_{(\ell_2+1)})=\sum_{k=\ell_1}^{\ell_2} \binom{n}{k}p^k(1-p)^{n-k}
$$

La dernière égalité tient pour quelque soit $\kappa_p$. C’est en jouant avec $\ell_1$ et $\ell_2$ qu’on peut trouver un IC à n’importe quel niveau de signification, normalement $95\%$.

## Méthodes de rééchantillonnage

Le rééchantillonnage est le fait de tirer de sous-échantillons à partir d’un échantillon, l’objectif étant de simuler la variabilité des estimateurs et de réduire le biais d’un estimateur référence. **Particulièrement, on va s’intéresser à estimer la variance d’un estimateur $\hat\theta$**.

Il existent deux méthodes : la méthode jackknife et la méthode bootstrap. Pour les deux méthodes, **on va parler de “l’estimateur de maximum de vraisemblance”**. Ceci n’a rien à voir avec l’estimation de maximum de vraisemblance comme le $\max L(\theta|\bold x)$, mais c’est plutôt la version empirique $\hat\theta$ d’une statistique paramétrique $\theta$.

### La méthode du jackknife

### → La méthode en soi

L’objectif ici est de créer un estimateur $\hat\theta^*$ avec moins de biais que $\hat\theta$. Par la suite, on considère que $\theta=\varphi([X_i])$ (le paramètre se déduit avec un algorithme $\varphi$ sur les $X_i$) et que $\hat\theta=\varphi([x_i])$.

Pour la méthode du jackknife, on aura besoin de :

- Un paramètre $\theta$;
- Un estimateur du paramètre $\hat\theta$ qui est ***convergent et biaisé***
- Un échantillon réalisé $[x_i]$

En premier, on crée l’idée de “$j$-ème sous-échantillon” $[x_i]_{-j}$ comme le sous-échantillon qui contient tous les éléments de l’échantillon original sauf le $j$-ème élément.

Deuxième, on définit une nouvelle statistique $\hat\theta_j$ appelée “$\hat\theta$ privé de $j$” : cette statistique calcule l’estimateur sur $[x_i]_{-j}$. C’est comme si on considérait l’échantillon tiré comme tout la population et puis on en prend $n$ échantillons de taille $(n-1)$.

$$
\hat\theta_{-j}=\varphi([x_i]_{-j})
$$

Troisième, on définit autre statistique qui s’appelle le “$j$-ème pseudovaleur” (en anglais, le “$j$-th leave-out-one”) comme suit. Ceci est une combinaison linéaire convexe. Pour rappel, la combinaison linéaire d’estimateurs sans biais est aussi sans biais ssi. la somme des coefficients est égal à 1 (i.e. convexe).

$$
\hat\theta^*_{j}=n\hat\theta_n-(n-1)\hat\theta_{-j}
$$

Finalement, on définit l’estimateur jackknife $\hat\theta^*$ comme la moyenne des pseudovaleurs :

$$
\hat\theta^*=\frac{1}{n}\sum_j \hat\theta_{j}^*
$$

### → Créer un IC approché avec les pseudovaleurs

Notons que la statistique finale $\hat\theta^*$ est une moyenne. On peut estimer la variance de cette statistique comme

$$
s^2_{\hat\theta^*}=\frac{1}{n-1}\sum_{i=1}^n(\hat\theta_j-\hat\theta^*)^2
$$

Pour finalement arriver à la construction d’un intervalle de confiance :

$$
IC_{95\%}(\theta)\approx[\hat\theta^*-(t^{n-1}_{2.5\%})s_{\hat\theta^*}, \hat\theta^*+(t^{n-1}_{97.5\%})s_{\hat\theta^*}]
$$

### → L’intérêt de cette méthode

<aside>
💡 La proposition importante c’est que, si le biais de $\hat\theta$ est de la forme $\frac c n$, où $c$ constante, **alors l’estimateur jackknife $\hat\theta^*$ est sans biais**. Si le biais contient au moins un terme $\frac c n$, donc $\hat\theta^*$ réduira le biais en $\frac c n$. La preuve est la proposition 8.2 du livre de Michel Lejeune, page 178.

Le résultat du jackknife sur un estimateur est un autre estimateur avec un biais plus baisse. De faire du jackknife sur la variance non corrigée nous retourne la variance corrigée, par exemple.

Pour un estimateur sans biais comme $\bar X$, de faire du jackknife sur $\bar X$ nous retourne l’estimateur lui-même.

</aside>

En général, la loi étant totalement inconnue, on ne connaît pas la forme du biais, mais on s’attend à ce qu’il soit de toute façon réduit par la procédure décrite.

Outre la réduction du biais, l’intérêt du jackknife, primordial ici, est de **permettre l’estimation de l’écart-type de l’estimateur de base**, c’est-à-dire $s_{\hat\theta}$, et la possibilité de construire un intervalle de confiance approché.

### → Observations finales

Il y a une proposition très importante admise sur le livre de Michel Lejeune. Soit $\hat\theta^*$ l’estimateur jackknife de $\theta$ et soit $s^2_{\hat\theta^*}$ la variance de l’estimateur jackknife. Donc,

$$
\frac{\hat\theta^*-\theta}{s_{\hat\theta^*}/\sqrt n}\sim\mathcal T_{n-1}, \text{ mais rappelons que} \lim_{n\rightarrow\infin}\frac{\hat\theta^*-\theta}{s_{\hat\theta^*}/\sqrt n}\sim\mathcal N(0,1)
$$

Notons que la statistique elle est très pareille à 

$$
\frac{\bar X-\mu}{\sigma/\sqrt n}
$$

Et que celle-ci aussi suit une loi normale. Donc, la proposition résulte du fait que les pseudovaleurs tendent à être indépendantes et gaussiennes pour une grande variété de
statistiques, on peut donc voir l’analogie que les pseudovaleurs $[\hat\theta^*_j]$ sont comme les observations $[X_i]$ de $\bar X$.

En ce qui concerne l’approximation asymptotique de l’intervalle de confiance issu du jackknife, il est difficile de savoir à partir de quelle taille d’échantillon elle devient satisfaisante. Pour les petits échantillons, le bootstrap offre une alternative plus sûre.

### La méthode du bootstrap

### → Préparation

Juste avant de commencer, on va faire une modification importante à l’espérance $\mathbb E[X]$ ou plutôt la moyenne $\mu$ dans ce contexte :

$$
\overbrace{\int_\Omega x\cdot f(x) \space dx}^{I_1} = \overbrace{\int _\Omega x\space dF(x)}^{I_2}, \text{ car }

\\[8pt]

\frac{d}{dx}F(x)=f(x) \iff dF(x)=f(x)dx
$$

Le deuxième intégrale est l’intégrale de Riemman-Stieltjes, est c’est une généralisation de la première intégrale. Bref, on peut utiliser $I_1$ seulement si $X$ a une fonction de densité, tant que on peut toujours utiliser $I_2$ (continu ou discrète) avec la seule condition que $X$ admet une espérance finie.

Finalement et d’ailleurs, on considère que “l’estimateur de maximum de vraisemblance” d’un paramètre est juste sa version empirique sur l’échantillon.

### → La méthode en soi

On commence par observe un échantillon $\bold x=[x_i]_{1\le i\le n}$. On crée un sous-échantillon $\bold x^*$ **de la même taille** que $\bold x$ dont les valeurs sont des **tirages avec remise** de $\bold x$. Notons que le plus probable est que le nouveau sous-échantillon aura des valeurs répétés, mais cela ne pose pas des problèmes.

Ayant fait ça, on estime $\theta$ en calculant $\hat\theta^*$ sur le nouveau échantillon. On répète cette estimation $M$ fois jusqu’à ce qu’on finit avec $M$ estimations de $\theta$, qu’on garde dans un vecteur $\hat{\Theta}^*=[\hat\theta^*_i]_{1\le i\le M}$

Finalement, on estime la variance de $\hat\theta$ en calculant la variance empirique des éléments dans $\hat\Theta^*$, donc

$$
s^2_{\hat\theta^*}=\frac{1}{M-1}\sum_{i=1}^M(\hat\theta^*_i-\mu_{\hat\theta^*})^2 \text{\hspace{8pt}et\hspace{8pt} }\lim_{n\rightarrow\infin}s^2_{\hat\theta^*}=^\text{p.s.}s^2_{\hat\theta}
$$

On montre que, lorsque $M$ tend vers l’infini, l’estimateur issu de cette procédure tend presque sûrement vers l’estimateur du maximum de vraisemblance du paramètre $\text{Var}(\hat\theta)$. **Oui, il faut rappeler que $\text{Var}(\hat\theta)$ est un paramètre**.

En pratique, $M = 100$ fournit une approximation suffisante de cet EMV car l’écart sera alors négligeable par rapport à l’erreur d’estimation du maximum de vraisemblance lui-même.

### → Première construction d’un IC pour $\theta$

En supposant que $\hat\theta$ est asymptotiquement sans biais et gaussien, on peut construire un IC de $\theta$ comme suit

$$
IC_{95\%}(\theta)\approx[\hat\theta-1.96s^*_{\hat\theta},\hat\theta+1.96s^*_{\hat\theta}]
$$

L’approximation gaussienne est fréquemment légitime, en particulier si $\hat\theta$ est lui-même une estimation du maximum de vraisemblance de $\hat\theta$. 

Par contre, celle-ci n’est pas assurée pour tous les types de statistiques ou bien elle peut être trop lente pour fournir une approximation satisfaisante au vu de la taille $n$ de l’échantillon.

### → Deuxième construction d’un IC pour $\theta$

Si on peut admettre que 

- la distribution de $\hat\theta$ tend vers une gaussienne quand $n\rightarrow\infin$;
- la variance a une forme équivalente à $\sigma^2_\theta/n$, où $\sigma^2_\theta$ est constante
- on connaît un estimateur convergent de $\sigma^2_\theta$ qu’on note simplement $s^2_\theta$

Donc on peut appliquer une méthode *studentisée*. On modifie la méthode de sorte que, à chaque fois qu’on calcule une instance de $\hat\theta^*$ sur un nouveau échantillon, on calcule aussi $s^2_{\hat\theta^*}$. On finira donc avec un vecteur $\hat\Theta^2$ et un autre vecteur $\bold s^2_{\hat\theta^*}$ On définie un troisième vecteur $\bold T^*$ tel que

$$
\bold T^*=[T^*_i]_{1\le i \le n},\text{ où }T_i^*=\frac{\hat\theta^*_i-\hat\theta}{s^*_{\hat\theta^*, i}/\sqrt n}
$$

Finalement, on calcule les quantiles empiriques $t^*_{2.5\%}$ et $t^*_{97.5\%}$ pour établir l’IC comme suit :

$$
IC_{95\%}(\theta)\approx[\hat\theta-(t^*_{2.5\%})\frac{s}{\sqrt n},\hat\theta+(t^*_{2.5\%})\frac{s}{\sqrt n}]
$$

Il faudrait par contre que $M \ge 1000$ pour avoir des approximations précises.

### → Observations finales

- L’approche bootstrap est appropriée dans des situations très complexes, ou il n’y aura généralement pas d’alternative, et pas uniquement dans le cadre de l’échantillonnage aléatoire simple. C’est donc un outil extrêmement précieux qui est devenu viable avec les capacités de calcul actuelles.
- Pour des types très divers de statistiques, il a été démontré que la distribution générée par les valeurs $\hat\Theta^*=[\hat\theta^*_i]_{1\le i \le M}$ en faisant tendre $M$ vers l’infini, appelée distribution bootstrap de la statistique $\theta$, converge vers la vraie distribution de $\theta$ quand $n$ tend vers l’infini et ceci de façon rapide.
    - C’est-à-dire que, quand $M\rightarrow\infin$, l’estimateur bootstrap $\hat\theta^*$ tend vers l’estimateur de maximum de vraisemblance $\hat\theta$ et, quand $n\rightarrow\infin$, l’estimateur de maximum de vraisemblance $\hat\theta$ tend vers le vrai paramètre $\theta$.
- Signalons en particulier qu’alors que le jackknife échoue pour obtenir un intervalle de confiance pour la médiane (ou un quantile) de la loi mère, le bootstrap donne un résultat très proche de l’intervalle proposé vers la fin de la section précédente.

# Estimation fonctionnelle

## Estimation de la densité

### L’histogramme

Si bien l’histogramme s’intéresse plutôt à l’estimation de pourcentage entre les intervalle que le même histogramme établit, on va l’étudier comme une estimation de densité.

La définition mathématique d’un histogramme est comme suit : on prend un échantillon et on crée une suite de valeurs qui seront la point de coupes des barres de l’histogramme. On crée des intervalles basées sur ces points de coupe et finalement on peut définir la fonction histogramme.

$$
\begin{align*}
\text{Points de coupure : }&\{a_i\}_{1\le i\le {m}} \text{ tel que } a_i < a_{i+1}

\\[7pt]

\text{ Intervalles : }&\{I_i\}_{1\le i\le {m-1}}=\{I_1=]a_1,a_2], \cdots, I_m=]a_{m-2},a_{m-1}]\}

\\[7pt]

\text{Fonction longueur : }
&\ell(I_i)=a_{i+1}-a_i
\\[7pt]

\text{Effectif dans interv. : }

&\{n_i\}_{1\le i\le {m-1}} : n_i=|\{x_i : x_i\in I_i\}|

\\[3pt]

\text{Fonction histogramme : }

&\hat f_n(x)=

\frac{n_i/n}{\ell(I_i)} \text{, où }x\in I_i
\end{align*}
$$

Le plus souvent sera que la grille de découpage $\{a_i\}$ sera de longueur régulière $h$, donc 

$$
\forall i\in\N,\space a_{i+1}-a_i=h \implies \hat f_n(x)=\frac{n_i}{nh} \text{, où }x\in I_i
$$

Notons que si on somme l’aire sous toute les barres, on doit arriver à $1$. Enfin, il s’agit d’une estimation d’une densité, donc la somme des toutes les probabilités doit valoir $1$.

En plus, si on tire juste une observation $x_1$ de la population, la vrai probabilité que telle valeur tombe dans l’intervalle $I_i$ est notée $p_i$, qu’on estime comme $n_i/n$. Pour un échantillon de taille $n$, on va dire que la variable aléatoire $n_i \sim \mathcal B(n,p_i)$ compte le nombre d’observations qui tombe dans l’$i$-ème intervalle. Voyons la conséquence :

$$
\begin{align*}
\hat f_n(x) = \frac{n_i}{nh} \text{ et } n_i\sim\mathcal B(n,p_i)\implies

&\space\mathbb E[\hat f_n(x)]=\frac{1}{nh}\mathbb E[n_i]=\frac{np_i}{nh}=\frac{p_i}{h}

\\[7pt]

&\space \text{Var}[\hat f_n(x)]=\frac{np_i(1-p_i)}{n^2h^2}=\frac{p_i(1-p_i)}{nh^2}
\end{align*}
$$

On sait, en plus, que

$$
p_i=\int_{a_i}^{a_{i+1}}f(x)dx
$$

D’où $p_i/h$ serait la valeur moyenne de $f$ sur l’intervalle $I_i$. Il faut rappeler que la définition d’un estimateur sans biais est

$$
\mathbb E[\hat f(x)]=f(x), \text{ et voyons que } \mathbb E[\hat f_n(x)]=\frac {p_i} h
$$

Donc $\hat f_n(x)$ n’est donc sans biais que pour les valeurs de $x\in I_i$ où la vraie densité $f$ prend cette valeur moyenne, que c’est juste un point particulier dans un intervalle réelle… donc juste un point $x^*_i$ ou un ensemble de points. Pour la plupart d’un intervalle, $\hat f_n(x)$ est biaisé. Le biais sur un point $x$ différent de $x^*_i$ est $f(x^*_i)-f(x)=p_i/h-f(x)$.

### Comportement asymptotique de l’histogramme

Rappelons qu’il y a deux paramètres pour l’histogramme qui peuvent tendre vers l’infini ou zéro : l’effectif $n$ et la taille régulière $h$.

### Par rapport à l’espérance et au biais de $\hat f$

Si le biais sur un point $x_i\ne x^*_i$, le biais est donc $f(x^*_i)-f(x_i)$. Notons que c’est biais ne dépend pas de $n$, donc si $n\rightarrow\infin$ ne nous sert pas. En fait, il faudrait c’est plutôt faire tendre simultanément $n\rightarrow\infin$ et $h\rightarrow 0$.

### Par rapport à la variance de $\hat f$

Par rapport à la variance de l’estimateur, càd $\frac{p_i(1-p_i)}{nh^2}$, elle ne tend vers zéro que quand $nh\rightarrow \infin$.  Voyons que cela le rend donc difficile pour $h$, qui doit tendre vers zéro mais “infiniment moins rapide” que la fonction $1/n$ pour que $nh$ tende vers l’infini. On pourrait donc fixer la longueur régulière des intervalles $h$ comme $c/n$, où $c$ constante.

Concrètement, cela se traduit comme “plus $n$ est grand plus, il y a avantage a resserrer les intervalles mais pas trop, afin de garder de grandes valeurs de $n_i$ (effectif dans intervalle $i$)”.

Il est à noter que ces conditions qui assurent la convergence en moyenne quadratique—soit
$n → ∞$, $h → 0$, $nh → ∞$—restent nécessaires pour assurer d’autres modes de convergence, notamment en probabilité ou presque sûrement.

### Par rapport à l’EQM de $\hat f$ (erreur quadratique moyenne)

Si f est deux fois dérivable, donc pour tout $x$ on a que

$$
\text{EQM}(\hat f_n(x))= \frac{h^2}{12}(f^\prime(x))^2+\frac{f(x)}{nh}+o(h^2)+o(\frac{1}{nh})
$$

et, si on laisse tendre $n → ∞$, $h → 0$ et $nh → ∞$ on finit donc avec

$$
\text{EQM}(\hat f_n(x))=\frac{h^2}{12}(f^\prime(x))^2+\frac{f(x)}{nh}
$$

Donc les restes de séries disparaissent. Le premier terme est dû au biais au carré et le deuxième terme à la variance.

Maintenant, on ne s’intéresse plus a laisser $h\rightarrow\infin$ mais à savoir la vitesse de convergence de l’EQM à zéro en choisissant une valeur concrète de $h$. Si on prend la dérivé de EQM par rapport à $h$ et on l’annule, le $h$ qu’on obtient pour atteindre le minimum de EQM serait

$$
h=
\left(
\frac{6f(x)}{f\prime(x)^2}
\right)^{1/3}n^{-1/3}
$$

Si on choisit tel $h$, l’EQM serait asymptotiquement équivalent à $g(x)n^{-2/3}$, où g est une fonction seulement d’argument $x$ qui dépend de $f(x)$ et $f^\prime(x)$, et donc on dit que la vitesse de convergence est $n^{-2/3}$.

### Observations finales

Le choix de $h$ mentionné ci-dessus est juste utile en théorie, on ne pourra pas s’en servir étant donné qu’on ignore $f(x)$ et $f^\prime(x)$. Il y a d’autres manières proposées populaires pour choisir $h$.

Finalement, si $f$ est discontinue aux bornes de son support (voir la loi uniforme, la loi exponentielle ou la loi de Pareto) les résultats développés ne sont pas valables en ces bornes. De plus, si celles-ci sont inconnues, l’histogramme pose problème.

### Les estimateurs à noyaux

L’une des caractéristiques de l’histogramme est ne de pas être continu ni lisse. Ici, on va proposer un autre estimateur de la densité qui est lisse.

### Préparation

Un noyau est juste une fonction réelle non négative et intégrable. En plus, dans le contexte d’estimation fonctionnelle, on ajoute deux autres conditions :

- L’aire sous la fonction noyau est égale à $1$.
Ceci est pour assurer que le noyau est lui-même une densité.
- La fonction noyau est symétrique autour d’une de ses valeurs $x$.

En plus, si la fonction $K$ est un noyau, la fonction $K^*$ définie comme $K^*(u)=\lambda K(\lambda u)$ est aussi un noyau. Ceci nous permettra d’appliquer un “scale” approprié aux données.

### L’estimateur lui-même

Maintenant, on suppose avoir tiré un échantillon $[x_i]$ de taille $n$ d’une population. On veut estimer la densité réelle avec l’estimateur $\hat f$ défini comme

$$
\hat f(x)=\frac{1}{nh} \sum_{i=1}^nK\left(\frac{x-x_i}{h}\right)
$$

où il nous reste le choix de h, appelé la “fenêtre de comptage” ou “bandwidth” en anglais. 

Pour illustrer l’objectif, supposons qu’on définit K comme une gaussienne $\mathcal N(0,2.25)$ et qu’on tire un échantillon $[-2.1,-1.3,-0.4,1.9,5.1,6.2]$. Voyons c’e que ça donne pour un histogramme $(h=2)$ et un estimateur à noyau.

![untitled](new/uga/l3/s5/math/s5_math_stats_mathematiques_2/ressources/03_estimation_non_parametrique_et_fonctionnelle_untitled.png)

Notons que l’estimateur somme toutes les courbes normaux d’aire $1/6$ pour avoir finalement une courbe d’aire $1$.

Intuitivement, on voudrait choisir un $h$ aussi petit comme les données permettent, mais ceci est un choix compliqué à faire et exploré après.

### Le choix de noyau

Le noyau ne doit pas forcément être une gaussienne. Il existe plusieurs choix de noyaux, chacun avec ses avantages. On appelle “support” le domaine du noyau où $K(u)\ne 0$ et, si $u$ est dehors, donc le noyau l’assigne $0$.

![untitled](new/uga/l3/s5/math/s5_math_stats_mathematiques_2/ressources/03_estimation_non_parametrique_et_fonctionnelle_untitled_1.png)

- Le premier et deuxième noyau sont simples, mais seul le noyau triangulaire fournit une estimation continue de la vrai densité.
- Le troisième a une optimalité théorique mais sans grand intérêt pratique.
- Le quatrième est peut-être le meilleur choix, car il a les avantage du noyau gaussien mais sont support n’est pas infini à différence du dernier. En plus, son avantage théorique est très proche du troisième noyau.

### Comportement asymptotique des estimateurs à noyau

Avant de commencer, il faut une réécriture utile de l’estimateur noyau comme suit :

$$
\hat f(x)=\frac{1}{nh}\sum_{i=1}^nK\left(\frac{x-X_i}{h}\right) \iff\hat f(x)=\frac{1}{n}\sum_{i=1}^n Z_i, \text{ où }Z_i=\frac{1}{h}K\left(\frac{x-X_i}{h}\right) 
$$

Notons que l’estimateur $\hat f$, qui est une variable aléatoire, sera juste la moyenne de la somme des $Z_i$.

### Par rapport à l’espérance et le biais de $\hat f$

Il y a beaucoup de développements dans le matériel, mais on saut jusqu’à la fin pour comprendre le résultat. Ici, $x$ est la variable indépendante de l’estimateur $\hat f$, et $t$ la variable indépendante de la vrai densité $f$. On a donc, **pour un $x$ fixé**,

$$
\begin{align*}
\mathbb E[\hat f(x)]-f(x)=\frac{h^2}{2}f^{\prime\prime}(x)\int_\R u^2K(u)du+o(h^2), \text{ où }u=\frac{x-t}{h}
\end{align*}
$$

Pour h petit le biais dépend donc de f(x) et du moment d’ordre 2 du noyau. Le biais est du signe de f”(x) : si f est concave en x le biais est négatif, si elle est convexe le biais est positif.

On voit que le biais se présente tel qu’il sous-estime les maximums et sur-estime les minimums de la vrai densité $f$. La méthode tend à écrêter les creux et les pics de la densité, ce qui est un inconvénient majeur.

### Par rapport à la variance et l’EQM de $\hat f$

Pour la variance, on a que :

$$
\text{Var}(\hat f(x))=\frac{1}{nh}f(x)\int_\R K(u)^2du+O\left(\frac 1 n\right)
$$

Pour l’erreur quadratique moyenne et **un $x$ fixé**, on a que

$$
\begin{align*}
\text{EQM}(\hat f(x))
&=\frac{h^4}{4} \left(\int_\R u^2K(u)du\right)^2 f^{\prime\prime}(x)^2+\frac{f(x)}{nh}\int_\R K(u)^2du

\\[8pt]

&+o(h^4)
+O\left(\frac 1 n\right)
\end{align*}
$$

Faisant abstraction des termes o(h4) + O( 1n ) n´egligeables dans les conditions de convergence, on voit que plus la largeur de fenˆetre h est faible plus le biais diminue mais plus la variance augmente et, inversement, l’´elargissement de la fenˆetre augmente le biais et diminue la variance.

Si on prend telle expression pour cherche le h qui la minimise, telle h est d’ordre n^{-4/5}, qui est plus vite que le n^{-2/3} de l’EQM de l’histogramme.

Un autre indicateur de performance à considérer serait le EQIM : l’erreur quadratique intégrée moyenne. Bref, on prend l’intégrale de l’EQM pour tous les $x$, et donc on n’aura plus besoin de parler de “un $x$ fixé”.

$$
\begin{align*}
\text{EQIM}(\hat f)&=\int_\R\mathbb E\left[\left(\hat f(x)-f(x)\right)^2\right]dx=\int_\R\text{EQM}(\hat f(x))dx

\\[10pt]

&=\frac{h^4}{4}

\left(\int_\R u^2K(u)du\right)^2

\int_\R f^{\prime\prime}(x)^2dx

+\frac{1}{nh}\int_\R K(u)^2du

\\[8pt]

&+o(h^4)
+O\left(\frac 1 n\right)
\end{align*}
$$

De même, si on prend telle expression pour cherche le $h$ qui la minimise, telle $h$ est d’ordre $n^{-1/5}$, qui est plus vite que le $n^{-2/3}$ de l’EQIM de l’histogramme si on l’aurait calculée.

Ainsi, **en tant qu’estimateur fonctionnel, un estimateur a noyau converge plus vite vers la vraie densité f que l’histogramme**. Par contre, ce résultat repose sur un choix optimal très théorique (puisque dépendant de l’inconnue $f$) et de conditions de convergence artificielles. C’est pourquoi nous considérons maintenant les aspects pratiques.

### Choix pratiques du noyau $K$ et fenêtre $h$

Pour le choix de $K$, c’est plutôt indifférent si on se concentre à minimiser l’EQIM. Ceci a pu être constaté par calcul direct ou par simulation sur une grande variété de lois mères et est d’ailleurs confirmé sur l’expression asymptotique ci-dessus. Le noyau de Tukey est recommandé par son quasi-optimalité et son avantage de lissage.

Le choix de $h$ est bien plus difficile et moins satisfaisante : la plupart des propositions de choix de h reposent sur l’optimisation de l’EQIM (ou sur l’un des critères mentionnés plus loin, mais aucun n’est la panacée) et, par expérience, on constate souvent qu’elles ne fournissent pas nécessairement une estimation graphiquement satisfaisante, laissant subsister des variations locales (tendance a sous-lisser).

La méthode la plus sûre reste donc celle des essais et erreurs où, partant d’une valeur de toute évidence trop faible de h donnant des fluctuations locales indésirables, on augmente progressivement cette valeur jusqu’au seuil de disparition de telles fluctuations.

Même si les expressions asymptotiques sont à prendre avec précaution, elles permettent de vérifier sur diverses lois que la m´ethode des noyaux, outre le fait qu’elle peut donner une estimation lisse, est nettement plus efficace, au sens de l’EQIM, que l’histogramme.

## Estimation de la répartition

### La répartition empirique $F_n$, et l’utiliser comme estimateur $\hat F_n$

Pour estimer la vraie fonction de répartition $F$, on utilisera la répartition **empirique** $F_n$, **même si c’est une loi continue** ! Ici, $I$ est une fonction indicatrice, qui vaut $1$ si la valeur réalisé de $X_i$ se trouve dans $(-\infin,x]$ et vaut $0$ sinon.

$$
F_n(x)=\frac 1 n \sum_{i=1}^nI_{(-\infin,x]}(X_i)
$$

Notons que la fonction de répartition empirique n’est pas forcément un estimateur, donc pas besoin d’écrire un chapeau sur $F_n$ que du moment où on l’utilise comme estimateur $\hat F_n$.

Visuellement, c’est une fonction en escalier qui augmente de $1/n$ chaque fois que la valeur de la variable indépendante $x$ rencontre une valeur réalisée $x_i$.  

Notons que les $X_i$ sont des v.a. iid., et donc de les passer par la fonction indicatrice (une v.a. de Bernoulli masquée avec $p=F(x)$) et finir avec des $I(X_i)$ ne change pas le fait qu’elles sont des v.a. iid. En plus, on est en train de les additionner, donc une somme de v.a. iid. On peut donc évoquer le TCL, qui nous  mène a des faits remarquables :

Si on laisse $x$ fixé a une valeur arbitraire,

$$
n\hat F_n(x)\sim\mathcal B(n,F(x)) \implies \lim_{n\rightarrow\infin} \hat F_n(x)\sim\mathcal N\left(F(x),\frac{F(x)(1-F(x))}{n}\right)
$$

**Ceci est juste variable si $n$ est grand**. Notons donc, $\hat F_n(x)$ est asymptotiquement sans biais et la variance tend vers zéro. Donc, le MSE tend vers zéro, et donc $\hat F_n(x)$ est un estimateur convergent de $F(x)$. 

En plus, on peut construire un intervalle de confiance pour $p=F(x)$ tout de même comme on le ferait dans le cas d’une binomiale simple “de manuel”.

Finalement et le plus important, la répartition empirique comme estimateur $\hat F_n$ est un estimateur sans biais, convergent de $F(x)$ et le maximum de vraisemblance de $F$. Ce dernier résultat résulte trop compliqué, mais on dira juste que $\hat F_n$ est la fonction qui maximise la probabilité d’observer un échantillon réalisé.

$$
\hat F_n : \max_F L(F|[x_i])=\prod_{i=1}^nF^\prime(x_i)
$$

### Construire un intervalle de confiance pour chaque valeur $F(x)$

Avant, on voudrait montrer la convergence uniforme de $\hat F$ vers $F$. Ce théorème est celui de Glivenko-Cantelli, qui no dit que la différence entre la répartition réelle et son estimateur tend vers 0 si on augmente la taille de l’échantillon.

$$
\lim_{n\rightarrow\infin}\left(\sup_{x\in\R}|\hat F_n(x)-F(x)|\right)=^\text{p.s.}0
$$

Grâce à Kolmogorov-Smirnov, la borne $\sup$ de la différence est utilisée pour créer l’intervalle de confiance de $F(x)$ comme suit

$$
\text{Soit la statistique }D_n=\sup_{x\in\R}|\hat F_n(x)-F(x)|. \text{ Donc, }

\\[8pt]

\lim_{n\rightarrow\infin}\mathbb P(\sqrt{n}D_n<x)=
\underbrace{1-2\sum_{k=1}^\infin(-1)^{k-1}e^{-2{(kx)}^2}}_{G(x)}
$$

Notons que $G(x)$ est la répartition de la statistique $\sqrt{n}D_n$. La fonction $G(x)$ est vraiment puissante, du fait qu’elle ne dépend pas de la vrai répartition de départ $F(x)$, même pour $n$ fini. De ce fait, elle a été tabulée. À partir de $n = 40$, l’approximation par $G(x)$ est correcte à $10^{−2}$ près. En plus, son quantile de $95\%$ est aussi tabulé. Voyons,

$$
\mathbb P(\sqrt{n}\sup_{x\in\R}|\hat F_n-F(x)|< g_{95\%})\simeq95\% \text{ Mais, voyons que }

\\[10pt]

\sqrt{n}\sup_{x\in\R}|\hat F_n-F(x)|< g_{95\%}\iff\forall x \in\R, \sqrt{n}|\hat F_n-F(x)|< g_{95\%}

\\[8pt]

\text{Finalement, } IC_{95\%}(F(x))=\left[\hat F_n(x)-\frac{g_{95\%}}{\sqrt{n}}, \hat F_n(x)+\frac{g_{95\%}}{\sqrt{n}}\right]
$$

En plus, pour la fonction $G(x)$ on peut faire une simplification : si $x>0.8$ et $n=40$, $G(x)$ vaut presque juste $1-2e^{-2{x}^2}$. Étant donné qu’on s’intéresse quand $x=0.95$, $G(x)\approx 1.36$.

$$
IC_{95\%}(F(x))=\left[\hat F_n(x)-\frac{1.36}{\sqrt{n}}, \hat F_n(x)+\frac{1.36}{\sqrt{n}}\right]
$$

### Lissage de $F_n$

Très pareil à la section des estimateurs â noyau, on définit un nouveau estimateur $\hat F_n$ différent de la répartition empirique $F_n$. Cette estimateur sera une intégrale d’un estimateur à noyau $\hat f_n$ :

$$
\begin{align*}
\hat F_n(x) &= \int_{-\infin}^x\hat f_n(t)dt=\int_{-\infin}^x\frac{1}{nh}\sum_{i=1}^nK\left( \frac{t-x_i}{h}\right)dt

\\

&=\frac{1}{nh}\sum_{i=1}^n\int_{-\infin}^xK\left( \frac{t-x_i}{h}\right)dt

\\

&= \frac 1 n \sum_{i=1}^n\int_{-\infin}^{\frac{x-x_i}{h}}K(v)dv, \text{ où }v=\frac{t-x_i}{h}
\end{align*}
$$

Notons que, dans la dernière ligne, on a mis le $1/h$ à l’intérieur de l’intégrale, puis il disparaît avec le changement de variable.

Définissons  le “noyau intégré” comme $H$ et on aura un meilleure écriture de $\hat F_n$

$$
H(u)=\int_{-\infin}^uK(x)dx \implies \hat F_n(x)=\frac 1 n\sum_{i=1}^nH\left( \frac{x-x_i}{h}\right)
$$

Ici, comme pour la densité, se pose le problème de la largeur de fenêtre optimale. Il est toutefois moins crucial en raison de la plus faible sensibilité de l’estimation a ce paramètre de lissage.

Par exemple, on s’était dit que le noyau de Tukey est le plus pratique. Sa version intégrée serait donc

$$
H(u)=
\begin{cases}
0,\text{ si }u\le-1
\\
\frac{1}{16}(3u^5-10u^3+15u+8), \text{ si } -1\le u\le1
\\
1, \text{ si } 1 \le u
\end{cases}
$$

Lorsqu’on examine le graphe obtenu avec différents noyaux, on constate que la différence est imperceptible. Ceci s’explique par le fait que l’estimation d’une fonction de répartition est fortement contrainte par la condition de croissance de $0$ à $1$, et par sa continuité à droite. De ce fait, le problème est beaucoup plus simple que pour la densité.

En particulier, la croissance implique de faibles courbures et donc peu ou pas de problème de biais, contrairement a la densité. Il n’y a donc pas d’avantage tangible à utiliser des noyaux ou autres instruments de lissage sophistiqués et nous préconisons donc l’emploi du noyau de Tukey.

Notons bien, toutefois, que les estimations de densités obtenues par dérivation seront,
quant à elles, très sensibles aux variations jugées mineures pour la fonction de répartition. Malgré ce constat, il n’est pas inutile d’examiner le biais et la variance, de façon asymptotique, comme cela a été fait pour la densité.

### Comportement asymptotique du lissage de $F_n$

Pour la suite, on suppose un noyau de Rosenblatt, mais les résultats sont valables pour les noyaux les plus courants.

### Par rapport à l’espérance et au biais

Pour le biais, on trouve que

$$
\mathbb E[\hat F_n(x)-F(x)]=\frac {h^2}2 f\prime(x)\int_\R u^2K(u)du+o(h^2)
$$

Si bien la répartition empirique $F_n$ est sans biais, un lissage $\hat F_n$ introduit un faible biais. En fait, ce biais s’annule aux extrema de la vrai répartition $F$.

### Par rapport à la variance et l’EQM

Pour la variance, on a que

$$
\text{Var}(\hat F_n(x))=\frac{1}{n}\left(
F(x)[1-F(x)]
+hf(x)\left[\int_{-1}^1H^2(u)du-1\right]+o(h)
\right)
$$

On retrouve dans le premier terme de son expression asymptotique la variance de $F_n$. Par conséquent, on gagne sur la variance de $F_n$ si le deuxième terme est négatif, soit  $\left[\int_{-1}^1H^2(u)du\right]<1$, ce qui est vérifié pour les noyaux intégrés courants.

Pour ce qui concerne l’erreur quadratique moyenne, elle sera améliorée si la diminution de variance compense le biais au carré.