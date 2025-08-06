# 04 // tests d’hypothèses paramétriques

# Introduction

## Théorie de la décision

Dans l’approche paramétrique la plus générale, un test statistique consiste a décider d’accepter ou de rejeter une hypothèse spécifiant que $θ$ appartient à un ensemble de valeurs $Θ_0$. Cette hypothèse de référence est appelée *hypothèse nulle* et est notée $H_0$. À contrario, on définit l’*hypothèse alternative*, notée $H_1$, pour laquelle $θ$ appartient a $Θ_1 = Θ\setminus Θ_0$. 

En bref, on identifiera cette situation en écrivant que l’on teste :

$$
H_0:\theta\in\Theta_0 \text{ vs. }H_1:\theta\in\Theta_1
$$

Notons qu’on ne pourra jamais dire avec sûreté que $\theta\in\Theta_0$ ou $\Theta_1$, on ne pourra jamais connaître $\theta$. Donc, ça se lira plutôt comme une proposition probabiliste comme “on est $95\%$ sûrs que $\theta\in\Theta_0$” et pareil pour $\Theta_1$. Il faudra définir une manière “probabiliste” de prendre cette décision, souvent par des intervalles de confiance d’une statistique $T$ à deux bornes ou juste borné d’un côté, mais généralement connue comme la **région de décision**.

Il pourrait se donner trois cas :

- Nulle et alternative simples, où $\Theta=\{\theta_0,\theta_1\}$
    
    $$
    H_0:\theta=\theta_0\text{ vs. }H_1:\theta=\theta_1
    $$
    
- Nulle simple et alternative multiple
    
    $$
    H_0:\theta=\theta_0\text{ vs. }H_1:\theta\ne\theta_0
    $$
    
- Nulle et alternative multiples
    
    $$
    H_0:\theta\in\Theta_0\text{ vs. }H_1:\theta\in\Theta_1
    $$
    

# Les tests

## Hypothèse simple, alternative simple

### Premières définitions

C’est le cas où

$$
H_0:\theta=\theta_0\text{ vs. }H_1:\theta=\theta_1
$$

Un test pour $H_0$ est une règle de décision fondée sur la valeur réalisée $t\in\mathbb{R}$ d’une statistique $T$, appelée statistique de test, qui est un estimateur de $\theta$. La règle suit :

- Si $t\in A$, une partie de $\mathbb{R}$, donc on accepte $H_0 : \theta=\theta_0$;
- Si $t \in \bar A$, qui est $\mathbb{R}\setminus A$, on rejette $H_0$ et on accepte $H_1:\theta=\theta_1$.

**Si ça peut nous servir, $A$ veut dire “acceptation” et particulièrement l’acceptation de la nulle $H_0$, et normalement dans le test on cherche $\bar A$ càd. rejeter $H_0$**. Le tableau ci-dessous nous montre les situations désirables et non désirables :

|  | Rejeter $\mathcal{H}_0$ $(PP)$ | “Accepter” $\mathcal{H}_0$ $(PN)$ |
| --- | --- | --- |
| $\mathcal{H}_0$ est fausse **$(P)$** | OK $(TP)$ : $1-\beta$ | Erreur de Type II $(FN)$ : $\beta$ |
| $\mathcal{H}_0$ est vraie **$(N)$** | Erreur de Type I $(FP)$ : $\alpha$ | OK $(TN)$ : $1-\alpha$ |

![untitled](ressources/04_tests_d’hypotheses_parametriques_untitled.png)

[Binary classification](https://en.wikipedia.org/wiki/Binary_classification)

[Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)

Étant donnée que la décision se fonde sur un résultat d’origine aléatoire, on caractérisera chaque erreur par sa probabilité. Une probabilité d’erreur est appelée *risque.* Particulièrement :

- Le risque de Type I est $\alpha=\mathbb P(t\in\mathcal C|H_0)$
À lire : la probabilité d’observer une valeur de $T$ qui nous mène à penser que $H_0$ est fausse tant qu’elle est en fait vraie.
- Le risque de Type II est $\beta=\mathbb P(t\in \bar {\mathcal C} |H_1)$.
À lire : la probabilité d’observer une valeur de $T$ qui nous mène à penser que $H_0$ est vraie tant que, en fait, $H_1$ est vraie.

Dans la pratique, on fait

1. On choisit arbitrairement $\alpha$, normalement $\alpha=0.05$.
2. Si $\alpha=0.05$, on détermine la région critique $\mathcal C$ tel que $\mathbb P(t\in\bar {\mathcal C }|H_0)=0.05.$
    1. On voit aussi que la loi de la statistique de test $T$ doit être parfaitement connue sous $H_0$, tant que c’est pas le cas de $T$ sous $H_1$.
    2. La construction d’un test consiste donc à rechercher une statistique pertinente dont on connaît la loi sous $H_0$.

La région de rejet étant ainsi déterminée, la région de non rejet l’est aussi et donc également le risque de deuxième espèce $β$ . Il est essentiel de garder à l’esprit que, dans une procédure de test, **on contrôle le risque** $α$ mais pas le risque $β$.

Il est naturel de poser comme exigence que la statistique ait une plus forte propension a tomber dans la région de rejet quand $H_1$ est la bonne hypothèse, ce que nous transcrivons mathématiquement par la condition que la probabilité de rejeter $H_0$ soit plus élevée sous $H_1$ que sous $H_0$, et si possible nettement plus élevée. Ceci est la même chose qu’un test dit “sans biais”, comme on le mentionne dans la section suivante.

$$
\underbrace{\mathbb P(t\in\mathcal C|H_1)}_{1-\beta}\ge \underbrace{\mathbb P(t\in\mathcal C|H_0)}_\alpha
$$

Toute la recherche d’une bonne statistique de test, intuitive ou non, repose sur ce principe que nous allons maintenant formaliser avec la notion de puissance.

### Puissance et biais d’un test

La puissance d’un test est définie comme la capacité de rejeter $H_0$ quand elle est effectivement fausse, donc

$$
\mathbb P(t\in\mathcal C|H_1)=1-\beta
$$

On pourrait aussi définir la puissance d’un test comme une fonction. Particulièrement, une fonction $\phi$ pour des valeurs du paramètre $\theta$ :

$$
\phi(\theta)=\mathbb P(t\in\mathcal C|\theta)
$$

Un test est dit *sans biais* si sa puissance est supérieure ou égale à son risque $\alpha$, donc

$$
\mathbb P(t\in\mathcal C|H_1)\ge\mathbb P(t\in\mathcal C|H_0) \iff 1-\beta\ge\alpha
$$

En conclusion, **une condition naturelle pour qu’une statistique soit éligible pour tester une hypothèse est qu’elle induise un test sans biais.** Incidemment, ce terme de “sans biais” n’a pas de rapport direct avec la notion de biais d’un estimateur. On entrevoit dès lors que le choix entre plusieurs tests potentiels, pour une hypothèse nulle donnée, **se jouera sur la puissance**.

**Définition : comparaison de tests par la puissance**. On pourrait comparer la puissance de deux tests : un test $\tau_1$ est plus puissant, au niveau $\alpha$, que le test $\tau_2$ si la signification de $\tau_2$ est $\alpha$ ou inférieur (habituellement normal), et la puissance de $\tau_1$ est supérieure à celle de $\tau_2$.

L’objectif sera finalement de rechercher le test le plus puissant parmi tous. Il existe un tel test dans le cas où $H_0$ et $H_1$ sont des hypothèses simples, mais cela n’est pas nécessairement vrai dans le cas où l’hypothèse alternative est multiple. Par ailleurs et en général, quand une statistique de test donne le test le plus puissant a un niveau donné, elle reste optimale à tout autre niveau.

**Définition : convergence de tests**. Finalement, on peut dire que la procédure de test est *convergente* quand, pour une suite de tests $\{\tau_n\}$ de taille d’échantillon $n$, dont on peut extraire une suite de leurs puissances $\{1-\beta_n\}$, $\lim_{n\rightarrow\infty} (1-\beta_n) = 1$ ou, également, $\lim_{n\rightarrow\infty} \beta_n=0$. Donc, la puissance tend vers $1$ quand l’échantillon s’agrandit.

En d’autre termes, on doit avoir la garantie qu’on gagne à observer de très grands échantillons, de sorte qu’il est pratiquement sûr de détecter une hypothèse nulle $H_0$ qui serait fausse à la limite. 

### 🔖 Extra : estimateur *exhaustive*

Avant de préciser cela notons qu’un test $\tau$, tel que nous avons présenté les choses, est parfaitement défini par le couple statistique de test — région d’acceptation. :

$$
\tau=\{T,A\}
$$

Ceci est valide car $α$, $β$ et la puissance $(1 − β)$ en découlent (même si conceptuellement le choix de $α$ précède celui de $A$, mais pour $α$ fixé il y a différentes façons de choisir une région—généralement un intervalle—de probabilité $α$ sur la loi de $T$ sous $H_0$).

En fait, il n’est même pas nécessaire de se référer à une statistique de test. Mettons en évidence la fonction de l’échantillon définissant la statistique $T=h(\mathbf{x})$ et $\mathbb A$ l’ensemble des points de $\mathbb{R}^n$, réalisations du vecteur $\mathbf{X}$, défini par

$$
\mathbb A=\{\mathbf{x}:\underbrace{h(\mathbf{x})}_t\in \bar {\mathcal C} \}
$$

Mais notons, $(t\in \bar {\mathcal C})$ est équivalent $(\mathbf{X}\in\mathbb A)$. Le test est donc parfaitement défini par la région d’acceptation $\mathbb A$ dans $\mathbb{R}^n$. D’une façon générale, un test s’identifie à une région d’acceptation dans l’espace des réalisations. Cela dit, cette vision des tests est rarement utile, et normalement on passe par une statistique $T$.

## Test de RV : rapport de vraisemblance simple (et multiple)

### Définition, cas simple

Dans cette section, on reste sur une hypothèse et alternatives simples. Un test de rapport de vraisemblance simple de $H_0$ vs. $H_1$ au niveau $\alpha_0$  fixé au préalable, est un test défini de la forme suivante :

$$
\tau = \left\{ T=RV=\frac{L(\theta_0|\mathbf{x})}{L(\theta_1|\mathbf{x})},\space  \mathcal C=\{RV: RV \le C\}\right\}
$$

La valeur de $C$ est déterminée par le risque fixe $\alpha_0 = \mathbb P(\mathcal C|\theta=\theta_0)$, donc **il est vraiment important de fixer $\alpha=\alpha_0$ avant de calculer le rapport de vraisemblance**. Dans la pratique, $C$ est normalement plus petit que $1$, pour garantir un $\alpha$ faible.

Si la région $\mathcal C$ obtenue par ce test entre hypothèse simples ne dépend pas de la valeur choisie de $\theta_1$, alors on aura un test UPP.

Quelque chose d’intérêt c’est qu’on peut calculer, dans le cas simple, une fonction de puissance explicite.

Le déroulement d’un exo. est souvent comme suit :

1. Proposer la densité des $X_i$, supposées iid., puis calculer la vraisemblance.
2. Dire qu’on fixe $\alpha=\alpha_0$.
3. Calculer $RV$ et puis affirmer que $RV \le C$.
4. Simplifier $RV$ le plus possible en isolant les $x_i$ d’un côté et la constante de l’autre côté absorbe tous les termes et facteurs nécessaires.
    1. Un exemple c’est d’arriver à $\sum_{i=1}^n x_i \ge C_4$. Notons que ceci nous montre la condition pour avoir un vrai positif. $C_4$ est la quantité que la $C$ original a absorbé d’autre termes.
5. On revient à la définition de $\alpha_0 =\mathbb P (\sum_{i=1}^n X_i \ge C_4 | \theta=\theta_0)$. On calcule finalement la valeur concrète de $C$.

### Cas $H_0$ simple vs. $H_1$ multiple

Il y a deux sous-cas : quand $H_1$ est unilatérale (qui est le meilleur cas pour nous) et quand $H_1$ est bilatérale.

Faisons le premier sous-cas. Supposons $H_0 : \theta = \theta_0$.

- Si $H_1 : \theta > \theta_0$, on dira que la region critique du test de Neyman-Pearson sera celui du test $H_0 : \theta = \theta_0$ vs. $H_1 : \theta = \theta_1$, où $\theta_1 > \theta_0$.
- C’est analogique si $H_1 : \theta < \theta_0$.

Un problème qui arrive c’est qu’on ne peut plus calculer une fonction de puissance explicite si $\theta_1$ n’est pas simple.

Pour le deuxième sous-cas, il n’existe pas de test UPP. La région critique au risque $\alpha_0$ s’obtient par la réunion des regions critiques $\mathcal C_1$ et $\mathcal C_2$ des tests unilatéraux à risque $\alpha_0/2$.

### Théorèmes notables

Il y a trois théorèmes importantes conséquence de RV :

- **Lemme de Neyman-Pearson**.
Le test de RV est le plus puissant de tous, pour $\alpha\in ]0,1[$.
- Le test de RV est sans biais : $1-\beta\ge\alpha$.
Pour Neyman et Pearson, leur esprit aussi est que $\beta > \alpha$, selon le prof. Quand c’est pas le cas, on appel ceci “incohérent”.
- Le test de RV est convergent ($n\rightarrow\infty , \beta\rightarrow0$), sous de conditions mineures.

Les preuves des deux premiers théorèmes sont dans le matériel de Michel Lejeune, à partir de la page 208.

### 🔖 Extra : caractérisation d’un test

S’agissant d’estimer $θ$, certaines statistiques peuvent être exclues du fait qu’elles n’utilisent pas de façon exhaustive toute l’information contenue dans l’échantillon $\mathbf{X}$. À l’inverse, on peut s’attendre à ce qu’un “bon” estimateur soit une statistique qui ne retienne que ce qui est utile de l’échantillon. Une statistique $T(\mathbf{X})$ est donc dite exhaustive si

$$
\mathbb P \Big(\mathbf{X}=\mathbf{x}\space|\space T(\mathbf{X})=t,\theta\Big)=\mathbb P \Big(\mathbf{X}=\mathbf{x}\space|\space T(\mathbf{X})=t\Big)
$$

ou, alternativement,
$$
I(\theta|S(\mathbf{X}))=I(\theta|\mathbf{X}). 
$$
$$
\text{ Rappel : } 
\\[8pt]
I(\theta|\mathbf{x})=\mathbb E\left[\left( \frac{\partial \ln L}{\partial\theta}(\theta)-\cancel{\mathbb E[s(\theta)]}^{\space0}\right)^2\right]=\int_\Omega \left( \frac{\partial \ln L}{\partial\theta}(\theta)\right)^2L(\theta|\mathbf{x})d\theta
$$

En pratique, on n’évoque pas cette égalité pour les calculs. mais on passe plutôt par le **théorème de factorisation**. On peut dire aussi que la statistique $T$ est exhaustive s’ils existent deux fonctions $g$ et $h$ mesurables telles que :

$$
f(\mathbf{x}|\theta)=g(T(\mathbf{x})|\theta)\times h(\mathbf{x})
$$

On voit bien qu’on parle de “factorisation” parce qu’on finit par exprimer $f$ comme le produit de deux facteurs. En plus, $g$ contient information sur la statistique réalisée (et donc indirectement de l’échantillon) et le paramètre—tant que $h$ contient information juste sur l’échantillon réalisé. Tout le membre de droit est appelé “la densité conjointe” dans ce contexte, un nom qu’on utilisera souvent.

Deux propositions importantes découlent déjà de la définition d’exhaustivité :

- Si $T$ est une statistique exhaustive et $T^\prime$ une statistique telle qu’on peut réécrire $T$ comme fonction de $T^\prime$, donc $T^\prime$ est exhaustive elle-même.
- Pareillement, si c’est $T^\prime$ la statistique fonction de $T$ comme $T^\prime(\mathbf{X})=f(T(\mathbf{X}))$ qui est exhaustive, et si $f$ est bijective, donc $T^\prime$ est aussi exhaustive.

En plus, on peut parler de exhaustivité minimale d’une statistique $T^*$ si elle est exhaustive et si, pour tout statistique exhaustive $T$, on peut trouver une fonction $f$ telle que $T^*(\mathbf{X})=f(T(\mathbf{X}))$. Une condition de régularité est que le domaine ou support de la densité des $\mathbf{X}$ ne dépend pas du paramètre inconnu, ce qui élimine la loi uniforme.

En règle générale, une statistique exhaustive est minimale. Tout estimateur pertinent est fonction d’une statistique exhaustive minimale.

## Hypothèses multiples

### Redéfinitions du cas simple

Un test d’hypothèse et alternative simple est souvent peu réaliste. Ici, on suppose que $\theta$ peut prendre plusieurs valeurs sous $H_0$ et plusieurs valeurs différents sous $H_1$. C’est la définition générale, ou on utilise $\theta\in\Theta_0$ et non pas l’égalité à une seule valeur exacte comme $\theta=\theta_0$, et de même pour $H_1$.

$$
H_0:\theta\in\Theta_0 \text{ vs. }H_1:\theta\in\Theta_1
$$

Supposons ici que $H_0$ est vraie, donc $\theta\in\Theta_0$. On n’utilisera plus $\alpha$ pour parler du risque de première espèce, mais de $\mathbb P(T\in\bar A|H_0)$. Notons que, pour chaque valeur possible du paramètre $\theta\in\Theta_0$ on peut associer un risque de première espèce différent, donc $\alpha(\theta)$.

Le ***niveau du test*** $\alpha$ est donc défini comme le plus grand risque possible induit par le paramètre $\theta$ si c’est le cas que $H_0$ est vraie : 

$$
\alpha=\sup_{\theta\in\Theta_0}\alpha(\theta)
$$

C’est analogique pour l’hypothèse alternative $H_1:\theta\in\Theta_1$ et le risque de deuxième espèce $\beta(\theta)$. La définition d’un test sans biais est aussi analogique. On prend une notation de puissance comme suit :

$$
h(\theta)=1-\beta(\theta)
$$

Les définitions de test plus puissants changent un peu, on parlera maintenant d’un test $\tau_1$ uniformément plus puissant qu’un autre $\tau_2$ au niveau $\alpha$ si : 

$$
\alpha_{\tau_2} \le \alpha,

\hspace{8pt}

\forall \theta\in\Theta_1:h_1(\theta) \ge h_2(\theta)

\hspace{6pt}
\text{et}
\hspace{6pt}

\exists\theta^*\in\Theta_1 :h_1(\theta^*) > h_2(\theta^*).
$$

Voyons que cela veut juste dire que la puissance de $\tau_1$ est supérieure quand $H_0$ est fausse ou également quand $H_1$ est vraie, donc on suppose que $\theta\in\Theta_1$.

Finalement, on peut parler du test uniformément le plus puissant au niveau $\alpha$, ou du test UPP en $\alpha$ tout court. Ce test est uniformément plus puissante que tous les autres tests.

Ceci étant dit, rien ne garantit l’existence de ce test et en fait souvent il n’existe pas pour toutes les valeurs de $\theta$. Le plus commun est que il existe $\tau_1$ qui est le plus puissant pour quelques valeurs de $\theta$, $\tau_2$ pour quelques autres valeurs de $\theta$, etc.

Néanmoins, le résultat de Neyman-Pearson obtenu dans la situation simple s’étend assez naturellement à des situations d’hypothèses multiples dites unilatérales, très fréquentes en pratique.

### Cas de tests unilatéraux

Le test prend la forme suivante :

$$
H_0:\theta\le\Theta_0 \text{ vs. }H_1:\theta>\Theta_1\text{\hspace{8pt}ou\hspace{8pt}}H_0:\theta\ge\Theta_0 \text{ vs. }H_1:\theta<\Theta_1
$$

Cette structure de test est assez commune et il y a une proposition importante sur ce type de test : l’existence d’un test UPP est garantie si 

- $T=t(\mathbf{x})$ est une statistique exhaustive minimale
- Pour toute couple $(\theta,\theta^\prime)$ tel que $\theta<\theta^\prime$, le RV $L(\theta|\mathbf{x})/L(\theta^\prime|\mathbf{x})$ est monotone de $T$.

Dans ce cas, la région d’acceptation est de la forme $T<k$ ou $T>k$.

On peut aussi garantir l’existence d’un test UPP dans une autre situation : si la loi mère dont on tire l‘échantillon $f$ est de la **classe exponentielle** et si $\eta(\theta)$ est monotone, donc il existe un test UPP et la région de rejet est $\sum_{i=1}^nT(x_i)<k$ ou $\sum_{i=1}^nT(x_i)>k$. 

> [!note]
> La “classe exponentielle” est une famille de fonctions qui peuvent s’exprimer de la forme suivante
>
> $$
> f(x|\theta)=h(x)g(\theta)e^{\eta(\theta)T(x)}\text{ ou } f(x|\theta)=h(x)e^{\eta(\theta)T(x)-A(\eta)}
> $$
>
> La première forme est celle présentée dans le matériel de Michel Lejeune, tant que la deuxième forme est présentée dans la page de Wikipédia. Dans le cas de Wikipédia :
>
> - $T(x)$ est une statistique exhaustive.
> Normalement, cette statistique est juste $x$, l’observation.
> - $h(x)$ est la “mesure de base”, une fonction positive
> Attention ! Ce $h(x)$ ne doit pas avec la fonction puissance d’un test !
> - $\eta(\theta)=T^\prime(x) \ln f(x|\theta)$ est le “paramètre naturel”.
> Sa définition est la dérivée de la fonction génératrice cumulante. qui est une fonction qui capture toutes les propriétés statistiques de la distribution.
> - $A(\theta)$ est le log. du facteur de normalisation.
>
> $$
> A(\eta)=\ln\left( \int_Xh(x)e^{\eta(\theta)T(x)}dx \right)
> $$
>
> - Si jamais on préfère la version avec $g(\theta)$, à savoir que
> $g(\theta)=e^{-A(\eta)} \iff A(\eta)=-\ln(g(\theta))$.
>
> On pourra voir un liste de plusieurs distributions écrites sous cette forme [ici](https://en.wikipedia.org/wiki/Exponential_family#:~:text=as%20logit.-,Table%20of%20distributions,-%5Bedit%5D).

Il faudrait consacrer un moment pour parler du choix de $H_0$ dans ce cas : si on la choisit $\theta \le\theta_0$ ou $\theta\ge\theta_0$. **Généralement, l’erreur qui serait considérée le plus indésirable et problématique serait l’erreur assigné à $\alpha$.** Si on désigne une alarme d’incendie, on voudrait que son erreur de première espèce soit qu’elle ne sonne pas tant qu’il y a du feu, et on laisse l’erreur de deuxième espèce le cas plus courant de sonner quand il n’y a pas du feu.

### Cas de tests bilatéraux

Le test prend la forme suivante :

$$
H_0:\theta=\theta_0 \text{ vs. }H_1:\theta\ne\theta_0

\text{\hspace{8pt}ou\hspace{8pt}}

H_0:\theta\in[\theta_1,\theta_2] \text{ vs. }H_1:\theta\notin[\theta_1,\theta_2]
$$

Le premier test ici est plutôt utilisé quand $\theta$ représenté l’écart entre deux paramètres de la population, disons que $H_0$ est que la différence entre la moyenne de deux populations est nulle, donc $H_0 : \theta=\mu_1-\mu_2=0$.

Le deuxième test est utilisé si le paramètre est dans un intervalle de tolérance acceptable. La région d’acceptation habituelle prend la forme $t\in[c_1,c_2]$ pour $t$ une réalisation de la statistique.

L’usage veut que l’on détermine les valeurs critiques $c_1$ et $c_2$ en répartissant $α/2$ sur chaque extrémité. Ainsi, pour le cas $H_0 : θ = θ_0$, ces valeurs seront telles que $\mathbb P (T <c_1|H_0) = \mathbb P(T >c_2|H_0) = α/2$.

Par contre, cette règle ne conduit pas au test UPP-sans biais si la loi de $T$ n’est pas symétrique (le test peut même ne plus être sans biais). Dans la classe exponentielle, la formulation plus générale est que la fonction de répartition $F$ doit être telle que la dérivée par rapport a $θ$ de $\mathbb P(T <c_1) + \mathbb P(T >c_2)$ s’annule en $θ_0$.

## 🔖 Extra : rapport de vraisemblance généralisé

Si le RV (rapport de vraisemblance simple) était un quotient, le RVG (rapport de vraisemblance généralisé) le sera aussi. Particulièrement, le RVG est une fonction $\lambda$ telle que

$$
\lambda(\mathbf{x})=\frac{\sup_{\theta\in\Theta_0}L(\theta|\mathbf{x})}{\sup_{\theta\in\Theta}L(\theta|\mathbf{x})}
$$

Ainsi, on définit le test du RVG par une région de rejet de la forme

$$
\lambda(\mathbf{x})<k\le1
$$

Il est évident que $\lambda(\mathbf{x})$ est inférieur ou égal à $1$ pour toute réalisation $\mathbf{x}$. Notons que le dénominateur de $\lambda(\mathbf{x})$ est juste l’estimation de maximum de vraisemblance ! Le RVG relève de la même rationalité que le RV simple. Si, pour une réalisation donnée, la vraisemblance atteint un maximum dans $H_0$ qui reste bien inférieur a son maximum absolu (dessous d’un $k$ arbitraire) dans tout l’espace paramétrique $Θ$, alors il y a lieu de douter de cette hypothèse.

Il faudrait noter que, dans le cas d’hypothèse et alternative simples, le test du RVG est équivalent au test du RV simple. Explication dans le matériel de Michel Lejeune, p. 236. 

Le $k$ choisit ici nous donnera notre erreur de première espèce $\alpha$. On choisit $k$ de telle manière que l’équation suivante est vraie, donc

$$
\sup_{\theta\in\Theta_0} \mathbb P(\lambda(\mathbf{x})<k)=\alpha
$$

Par contre, connaître la loi du RVG est problématique. Parfois on aura une forme simple, mais le plus normale sera de disposer une approximation asymptotique très utile.

Le test du RVG n’a pas de propriétés d’optimalité notables mais on constate dans des situations usuelles qu’il donne le test UPP-sans biais. Cependant, il possède des propriétés asymptotiques intéressantes, notamment sa convergence moyennant des conditions de régularité analogues a celles de l’estimateur du maximum de vraisemblance.

### Paramètre de nuisance

Dans le cas où un paramètre d’intérêt suit une loi mère à plusieurs paramètres, et une hypothèse nulle fait référence à un seul des paramètres, on dit “paramètres de nuisances” à tout autre paramètre non concernée par $H_0$. 

Par exemple : si on fait une hypothèse nulle sur la moyenne d’un population gaussienne et on ne dit rien sur la variance, la variance est le paramètre de nuisance.

Une fois on a établi une région de rejet associé à un test, si l’hypothèse nulle est de la forme $H_0:\theta_1\le\theta\le\theta_2$ et $H_0$ ignore un deuxième paramètre de la loi mère $\rho$, il existe un test UPP-sans biais pour une famille de la classe exponentielle si sa densité peut s’écrire

$$
f(x|\theta,\rho)=h(x)g(\theta,\rho)e^{\eta_1(\theta)T_1(x)+\eta_2(\rho)T_2(x)}
$$

On notera que ceci n’est pas vérifié par la loi de Gauss qui ne sépare pas ainsi $μ$ et $σ^2$ dans la partie exponentielle. De fait, il n’existe pas de test UPP-sans biais pour $H_0 : μ_1 ≤ μ ≤ μ_2$ considérée ci-dessus. Ces résultats se généralisent a plusieurs paramètres de nuisance.

### Approchant une région de rejet de grands échantillons

Soit une famille paramètre $\{f(x|\theta) : \theta\in\Theta, \Theta\subseteq \mathbb{R}^k\}$ et $H_0$ concernant $r$ valeurs composantes de $\theta$, donc $1\le r\le k$. Supposons que les conditions sont telles que l’EMV $\theta^*$ est BAN. Donc, la statistique $\Lambda_n=\lambda(\mathbf{X})$ est telle que

$$
\lim_{n\rightarrow\infty}-2\ln(\Lambda_n)\sim\chi^2(r)
$$

Donc, comme la région de rejet $\lambda < k$ est équivalente à $-2\ln\Lambda >k^\prime$, on rejettera à un niveau approximatif $\alpha$ si

$$
-2\ln\Lambda>q_{\chi^2(r)}^{1-\alpha}
$$

Ce résultat dont la validité s’étend au-delà de l’échantillonnage aléatoire simple autorise un test approché dans des situations complexes. C’est pourquoi on trouve le test du RVG de façon omniprésente dans les logiciels.

# Test paramétriques usuels

> [!note]
> Le tests ci-dessous peuvent se diviser en deux catégories : test où on compare un paramètre contre une valeur numérique de référence, comme “$\mu=2$” ; et des tests où on compare les paramètres de deux échantillons, comme “$p_1 = p_2$”.

## Loi normale

### Test sur $\mu$, $\sigma^2$ connu $(z$-test$)$

Le test, en version bilatérale, est comme suit

$$
\tau=\left\{T=\frac{\bar X-\mu_0}{\sigma/\sqrt n} , A =\{T: -z_{1-\alpha/2}<T< z_{1-\alpha/2} \} \right\}

$$$$

H_0:\mu=\mu_0\text{ vs. }H_1:\mu\ne\mu_0
$$

On utilise telle forme de T car on sait qu’elle suit une loi normale standard. Mais, réarrangeant l’inégalité qui définit $A$, on peut réécrire le test d’une manière plus naturelle : 

$$
\tau=\left\{ T=\bar X, A=\{ T : \mu_0-\frac{\sigma}{\sqrt n} z_{1-\alpha/2} < T < \mu_0+\frac{\sigma}{\sqrt n} z_{1-\alpha/2} \} \right\}
$$

Les quantiles $z$ sont à déterminer avec une table à quantiles. Notons que l’erreur de première espèce $\alpha$ est répandu moitié-moitié des deux côtés de la courbe. Ce test est un UPP-sans biais.

![untitled](ressources/04_tests_d’hypotheses_parametriques_untitled_1.png)

Dans le cas unilatérale, qui sont aussi UPP mais pas sans biais, on a que :

- $H_0 : \mu \le \mu_0\text{ vs. }H_1 : \mu > \mu_0$
On suppose que $\mu = \mu_0$ (qui maximise risque de première espèce), puis la région de rejet est juste du côte droite de la gaussienne standard. Ceci se reflète dans la région d’acceptation et, surtout, la région de rejet (non-acceptation) :  $$
    A=\{ T : T <z_{1-\alpha}\} \iff \bar A =\{ T : z_{1-\alpha } < T\}
    $$
- $H_0 : \mu \ge \mu_0\text{ vs. }H_1 : \mu < \mu_0$
Analogiquement au cas précédent. La région de rejet de $H_0$ est la queue gauche de la gaussienne normale standard.   $$
    A=\{ T : z_{1-\alpha}<T\} \iff \bar A =\{ T :T<z_{1-\alpha}\}
    $$
    ![Untitled](ressources/04_tests_d’hypotheses_parametriques_untitled_2.png)

### Test sur $\mu$, $\sigma^2$ inconnu $(t$-test$)$

Dans ce cas et vu précédemment, on utilise une variable de Student comme $T$. Ceci est juste valide si et seulement si on est sous $H_0$, car $\mu_0$ serait donc la moyenne de $\bar X$. Ceci arrêt d’être le cas quand on considère le cas général (càd. peu importe si $H_0$ ou si $H_1$), car on ne peut donc garantir que $\mu_0$ est la vraie moyenne de $H_0$ et tout la statistique $T$ ne suit plus une loi de Student.  

$$
\tau=\left\{T=\frac{\bar X-\mu_0}{S/\sqrt n} , A =\{T: -t^{(n-1)}_{1-\alpha/2}<T< t^{(n-1)}_{1-\alpha/2} \} \right\}

\\[8pt]

H_0:\mu=\mu_0\text{ vs. }H_1:\mu\ne\mu_0
$$

De même, on pourrait isoler $\bar X$ dans l’inégalité pour obtenir ce qui suit :

$$
\tau=\left\{ T=\bar X, A=\{ T : \mu_0-\frac{S}{\sqrt n} t^{(n-1)}_{1-\alpha/2} < T < \mu_0+\frac{S}{\sqrt n} t^{(n-1)}_{1-\alpha/2} \} \right\}
$$

Dans le cas des tests unilatéraux, on définit $A$ comme suit :

$$
H_0 : \mu \le \mu_0 \longrightarrow A=\{ T : T <t^{(n-1)}_{1-\alpha }\} \iff \bar A =\{ T : t^{(n-1)}_{1-\alpha } \le T\}

$$$$

H_0 : \mu \ge \mu_0 \longrightarrow A=\{ T : t^{(n-1)}_{1-\alpha }<T\} \iff \bar A =\{ T :T \le t^{(n-1)}_{1-\alpha }\}
$$

### Test sur $\sigma^2$, $\mu$ inconnu $($test de $\chi^2$$)$

Pour tous le cas, on utilisera la statistique $T$ qui suit :

$$
T=\frac{(n-1)S^2}{\sigma^2_0}\sim\chi^2(n-1)
$$

Notre test devient donc, pour le cas bilatéral :

$$
\tau=\left\{T=\frac{(n-1)S^2}{\sigma^2_0}, A =\{T: -{\chi^2}^{(n-1)}_{1-\alpha/2}<T< {\chi^2}^{(n-1)}_{1-\alpha/2} \} \right\}

$$$$

H_0:\sigma^2=\sigma^2_0\text{ vs. }H_1:\sigma^2\ne\sigma^2_0
$$

Et le test est aussi réécrit comme

$$
\tau=\left\{T=S^2, A =\{T: -\left(\frac{\sigma^2_0}{n-1}\right){\chi^2}^{(n-1)}_{1-\alpha/2}<T<\left(\frac{\sigma^2_0}{n-1}\right){\chi^2}^{(n-1)}_{1-\alpha/2} \} \right\}

$$

Particulièrement, pour le cas bilatéral, une note importante c’est que la loi $\chi^2$ n’est pas une loi symétrique. Dans le cas normale, on se servait de telle propriété pour fixer des quantiles correspondant à $\alpha/2$ des deux côtés.

Dans ce cas, on pourrait faire ça mais cela nous laisse avec un test qui n’est pas UPP-sans biais. Un test UPP-sans biais est possible, mais on doit faire un choix de quantiles $\alpha_1$ et $\alpha_2$ tels que $\alpha_1+\alpha_2=\alpha$ qui est compliquée et donc évitée ici.

Pour le cas unilatéral, on a un test UPP-sans biais comme suit :

$$
H_0 : \sigma \le \sigma_0 \longrightarrow A=\{ T : T <{\chi^2}^{(n-1)}_{1-\alpha }\} \iff \bar A =\{ T : {\chi^2}^{(n-1)}_{1-\alpha } \le T\}$$$$H_0 : \sigma \ge \sigma_0 \longrightarrow A=\{ T : {\chi^2}^{(n-1)}_{1-\alpha }<T\} \iff \bar A =\{ T :T \le {\chi^2}^{(n-1)}_{1-\alpha }\}
$$

À titre de curiosité, si la moyenne $\mu$ était connue, on utiliserait le fait suivant, les développement étant analogue aux précédents.

$$
\frac{\sum_{i=1}^n(X_i-\mu)^2}{\sigma^2}\sim\chi^2(n)
$$

### Comparaison de $\mu_1$ et $\mu_2$  (et cas échantillons appariés)

On suppose que on a deux échantillons tirés de deux gaussiennes différentes, et on veut comparer leurs moyennes. Normalement, on pose

$$
H_0:\mu_1-\mu_2=0\text{ vs. } H_1:\mu_1-\mu_2<0
$$

En fait, c’est de ce fait qu’on parle d’une “hypothèse nulle” pour faire référence à que la différence entre les deux moyennes est nulle.

### Supposition de même variance, inconnue $($$t$-test de variance groupée$)$

Notre statistique $T$ sera comme suit

$$
T=\frac{(\bar X_{1,n_1}-\bar X_{2,n_2})-(\mu_1-\mu_2)}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\sim \mathcal T(n_1+n_2-2)
$$

où $S_p$ est l’écart-type groupé de $\sigma^2_1$ et $\sigma^2_2$, càd. les variances moyennées de leurs dégrées de liberté. À savoir, la variance groupé de $\sigma^2_1$ et $\sigma^2_2$ est

$$
S^2_p=\frac{(n_1-1)S^2_1+(n_2-1)S^2_2}{n_1+n_2-2}
$$

Cette statistique (la variance groupée) est sans biais de la variance supposée commune. Ce n’est pas le cas si on prend la racine carrée pour essayer d’estimer l’écart-type.

Finalement, on donne la version bilatérale du test :

$$
\tau=\left\{T\text{ comme ci-dessus}, A =\{T: -t^{(n_1+n_2-2)}_{1-\alpha/2}<T< t^{(n_1+n_2-2)}_{1-\alpha/2} \} \right\}
$$

Puis, on donne la version unilatérale du test en termes de la région d’acceptation $A$ :

$$
H_0 : \mu_1 \le \mu_2 \longrightarrow A=\{ T : T <t^{(n_1+n_2-2)}_{1-\alpha }\} \iff \bar A =\{ T : t^{(n_1+n_2-2)}_{1-\alpha } \le T\}
$$$$
H_0 : \mu_1 \ge \mu_2 \longrightarrow A=\{ T : t^{(n_1+n_2-2)}_{1-\alpha }<T\} \iff \bar A =\{ T :T \le t^{(n_1+n_2-2)}_{1-\alpha }\}
$$

Notamment, avec une telle région de rejet, le risque $α$ maximal est atteint pour $μ_1 = μ_2$ et le test proposé est donc bien de niveau $α$. Ces sont des tests UPP-sans biais.

### Supposition de variances différentes, inconnues $($$z$-test asymptotique$)$

On devra se contenter d’une propriété asymptotique qu’on utilisera si $n_1,n_2 > 100$. On fera des légères modifications à la statistique $T$ de sorte **qu’on ne groupe pas** les variances. On renomme $T$ à $Z$, car on fera un $z$-test asymptotique.

$$
T=\frac{(\bar X_{1,n_1}-\bar X_{2,n_2})-(\mu_1-\mu_2)}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} \to Z=\frac{(\bar X_{1,n_1}-\bar X_{2,n_2})-(\mu_1-\mu_2)}{\sqrt{\frac{S^2_1}{n_1}+\frac{S^2_2}{n_2}}}
$$

Alors, on a que 

$$
\lim_{n_1,n_2\rightarrow\infty} Z_{n_1,n_2} \sim \mathcal N(0,1)
$$

On se servira de ce fait seulement pour un test unilatéral, de la forme suivante.

$$
H_0:\mu_1-\mu_2\le\Delta_0, 

\hspace{8pt}

H_0:\mu_1 - \mu_2 =\Delta_0

\hspace{4pt}
\text{ou}
\hspace{4pt}

H_0:\mu_1-\mu_2\ge\Delta_0
$$

Il suffit pour cela de retrancher $\Delta_0$ de $(\bar X_1 - \bar X_2)$. Le cas bilatéral pose de difficultés majeures. La puissance de ce test est pauvre quand les $n_1$ et $n_2$ sont petits. Ce problème s’appelle le problème de Behrens-Fisher.

### Supposition de variances différentes, connues $($$z$-test proprement$)$

Il suffit de modifier légèrement la statistique $Z$ précédente pour remplacer les estimateurs $S^2_1$ et $S^2_2$ par les vraies $\sigma^2_1$ et $\sigma^2_2$.

$$
Z=\frac{(\bar X_{1,n_1}-\bar X_{2,n_2})-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma^2_1}{n_1}+\frac{\sigma^2_2}{n_2}}}
$$

### Cas d’échantillons appariés

Deux échantillons sont appariées si on observe un échantillon des caractéristiques d’individus libellées, puis on applique une “transformation” et on re-observe les caractéristiques des mêmes individus. On voit un “avant” et un “après” des individus.

Par exemple, un premier échantillon pourrait être le prix des plusieurs fromage un jour, puis le deuxième échantillon serait le prix des mêmes fromages un autre jour. Chaque fromage retrouve son “pair” dans l’autre échantillon.

Dans ce cas, notre statistique est une $T$ qui suit un loi de Student à $n-1$ degrés de libertés. La différence ici avec le cas de comparaison de moyennes avec des variances inconnues supposées égales sont les degrés de liberté.

### Comparaison de $\sigma^2_1$ et $\sigma^2_2$ $($$F$-test ou test d’ANOVA$)$

On s’intéresse ici seulement dans l’égalité des variances, donc

$$
H_0:\frac{\sigma^2_1}{\sigma^2_2}=1\text{ vs. } H_1:\frac{\sigma^2_1}{\sigma^2_2}\ne1
$$

On se servira de la statistique $T$ suivante :

$$
T=\frac{S^2_1/\sigma^2_1}{S^2_2/\sigma^2_2}\sim\mathcal F(n_1-1,n_2-1)
$$

Sous $H_0$, $T$ suit une loi de Fisher. Puisque on s’intéresse à l’égalité des variance, on mentionne seulement le test bilatéral dont la région d’acceptation $A$ est donc comme suit. **Fais attention aux souscripts des quantiles ! La différence des quantiles se trouve là !**

$$
\mathcal C =\{T: T\ge f^{(n_1-1,n_2-1)}_{\alpha/2} \text{ ou } f^{(n_1-1,n_2-1)}_{1-\alpha/2} \le T \}
$$

## Loi de Bernoulli (proportions)

### Test sur une proportion $p$

Pour le cas bilatéral, le test prend la forme suivante, où $\hat p_n = S_n/n$, $S_n$ étant la somme des succès dans $n$ observations :

$$
\tau =
\left\{T=
\frac{\hat p_n-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}},
\space
\mathcal C=\left\{T: T>-z_{\alpha/2} \text{ ou } z_{\alpha/2}<T  \right\}

\right\}

$$$$

H_0 : p=p_0\text{ vs. } H_1:p\ne p_0
$$

On ajuste $\mathcal C$ dans le cas unilatéral.

La statistique $T$ est dérivée basée dans le cas du théorème de De Moivre-Laplace, sauf que dans ce cas-là on s’intéresse à estimer la nombre de succès $S_n$ tant qu’ici on se fixe plutôt à la proportion de succès $P_n$.

Un intervalle de confiance bilatéral serait donc:

$$
IC_{95\%}=
\left[ 
\hat p- 1.96 \sqrt{\frac{\hat p(1-\hat p)}{n}},
\hat p+ 1.96 \sqrt{\frac{\hat p(1-\hat p)}{n}}
\right]
$$

### Comparaison de $p_1$ et $p_2$, asymptotique $($$z$-test$)$

On a deux populations qui suivent une loi de Bernoulli de paramètres $p_1$ et $p_2$ respectivement et on veux tester que $H_0 : p_1=p_2$. Supposons qu’on réalise un échantillon de chaque population, **indépendants entre eux**, tels que : 

- Ils sont de taille $n_1$ et $n_2$ respectivement,
- Les proportions de succès observées seront $\hat p_1$ et $\hat p_2$ respectivement,
    - On vérifie les conditions de validité d’une gaussienne.
        - $n_1\hat p_1(1-\hat p_1) > 12$
        - $n_2\hat p_2(1-\hat p_2) > 12$

Donc, on a que

$$
\hat p_1-\hat p_2 \sim \mathcal N\left(p_1-p_2, \frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}\right)
$$

Et, sous $H_0$, on a que

$$
\hat p_1-\hat p_2 \sim \mathcal N\left(0,\space p(1-p)\left(\frac{1}{n_1} + \frac{1}{n_2} \right)\right)
$$

où $p=p_1=p_2$. Par contre, $p$ est inconnu, donc on fait une moyenne pondérée pour l’estimer :

$$
\hat p = \frac{s_1+s_2}{n_1+n_2}=\frac{n_1\hat p_1 + n_2\hat p_2}{n_1+n_2}
$$

où $s_1$ et $s_2$ sont les succès observés dans les échantillons #1 et #2, respectivement.

Le test bilatéral prend la forme qui suit, où $T$ est la normalisation de la statistique $(\hat p_1 - \hat p_2)$ :

$$
\tau =\left\{ T=\frac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1-\hat p)\left(\frac{1}{n_1} + \frac{1}{n_2} \right)}}, A= \{ T:-z_{1-\alpha/2}<T< z_{1-\alpha/2} \} \right\}
$$

### Résultat exact (loi hypergéometrique)

Pour une situation où les échantillons ne sont pas suffisamment grands pour faire un approximation gaussienne, on utilise un test sur une loi hypergéométrique. Les détails sont spécifiés dans le matériel de Michel Lejeune, page 237.

Pour des échantillons appariés (mesures répétées), on a besoin du test de McNemar.