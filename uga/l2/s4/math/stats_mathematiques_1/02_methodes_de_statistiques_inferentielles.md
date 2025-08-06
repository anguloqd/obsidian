# 02 // méthodes de statistiques inférentielles

[Slides de méthodes de stats inférentielles](ressources/02_methodes_de_statistiques_inferentielles_slides_mthodes_stat_inf_annote.pdf)

# Intervalle de confiance

## Motivation

Au croisement des statistiques et des probabilités, la démarche des statistiques inférentielles est de considérer l’observation $(x_1, \dots , x_d)$  comme la réalisation de $d$ répétitions $(X_1, \dots , X_d)$ d’une expérience aléatoire $X$.

La réalité est souvent entachée d’erreur. Cette démarche permet d’en tenir compte, d’imaginer, d’inférer le problème pur, et de travailler pour mieux comprendre l’erreur.

## Échantillon

On considère une suite de variables aléatoires $(X_i)_{i∈\mathbb{N}}$ identiques et indépendantes. Un échantillon de taille $d$ est l’ensemble des variables $(X_1, \dots, X_d)$. Une réalisation de cet échantillon est l’observation $(x_1, \dots, x_d)$. On travaillera alors sous la condition $(X_1 = x_1, \dots, X_d = x_d)$.

## Estimation

On cherche a connaître un paramètre $θ$ qui dépend de la loi de $X$ (par exemple son espérance ou sa variance). On réplique $n$ fois $X$ de manière indépendante $(X_1, \dots ,X_n)$. On évalue alors $θ$ par $\hat{θ} = \hat{θ}_n$ grâce aux réalisations possibles $(x_1, \dots , x_n)$ de l’échantillon a $n$ éléments. La valeur $\hat{θ}_n$ est nommée estimé ou estimation ponctuelle.

On prendra par exemple $\hat{θ}_n = \sum_i x_i/n$ pour estimer la moyenne de $X$, ou $\hat{σ} = \sum_i (x_i − \hat{θ}_n)^2/(n − 1)$ pour estimer la variance.

Pour récapituler, le paramètre réel constant inconnu est $θ$. Il est approché par l’estimateur $θ_n =
f(X_1, \dots, X_n)$, variable aléatoire, estimé grâce au relevé statistique par $\hat{θ} = \hat{θ}_n = f(x_1, \dots, x_n)$. On note parfois comme suit :

$$
\hat{\theta}_n=E[\theta_n|X_1=x_1, \dots, X_n=x_n]
$$

> [!note]
> **Note de la variance estimée**. La variance est une moyenne des écarts (au carré). Dans un échantillon de taille $n$, il y a $n-1$ écarts.

## Estimation par intervalle de confiance

On cherche à encadrer une V.A. ou une statistique dans un intervalle $[p,q]$ telle que la probabilité que la statistique appartienne à cet intervalle soit 95% (et donc 5% de risque). On veut donc déterminer $p$ et $q$. Ici, $f_n$ est notre statistique est c’est une fonction de la loi de $X$.

$$
P(\underbrace{\mu_n − aσ_n}_p ≤ f_n ≤ \underbrace{\mu_n + aσ_n}_q) = 0.95
$$

On admettra que $a = 1.96$ si notre intervalle de confiance est de $95\%.$

Pour déterminer finalement les valeurs de $p$ et $q$, on calcule $\mu_n=E[f_n]$ et $\sigma_n =\sqrt{Var(f_n)}$ utilisant la définition de la statistique $f_n$ en termes de $X$ et $n$. Une fois on a des valeurs concrètes de $X$ et $n$, et donc une valeur de $f_n$, on peut estimer $\mu_n$ et $\sigma_n$. **Finalement, on pourra calculer $p$ et $q$**.

# Intervalle de fluctuation

## Tracer de limites aux biais

L’intervalle de fluctuation est l’intervalle qui nous permet de prendre une décision en fonction de si la valeur réalisé de notre statistique se retrouve dans l’intervalle ou non. À $5\%$ de risque, l’intervalle est :

$$
[\mu-2\sigma, \mu+2\sigma]
$$

Note : réellement, le $2$ est remplacé pour un $1.96$.

Si la statistique se retrouve dehors de l’intervalle, on dira qu’on ne peut pas le faire confiance et qu’elle est biaisée.

> [!note]
> Par contre, si la statistique est dans l’intervalle, on ne peut pas dire que on peut le faire confiance ! **On dit juste que *rien s’oppose au fait* qu’elle soit équilibrée**.
>
> Une pièce qui montre 58% des fois réalisées des piles se trouve dans l’intervalle de confiance d’une pièce qui montre en moyenne une pile 50% des fois, mais aussi si elle montre des pile 60% des fois (une pièce non-équilibrée quoi) !

Notons qu’ici, on utilise les paramètre théoriques ou non pas des estimations ponctuelles comme on la fait dans la section précédente !

# Introduction aux tests statistiques

## L’idée

On veut savoir si une proposition est vraie ou fausse ayant un morceau d’”évidence”, qui est une observation ou échantillon tiré d’un processus aléatoire. Normalement, cette proposition est sur un paramètre de ce processus aléatoire.

On décidera si on accepte ou non la proposition comme si c’était une preuve par contradiction. Soit $P$ la proposition qu’on veut démontrer, donc on cherchera à montrer que $\lnot P$ est fausse et donc que $P$ est vraie. La négation de $P$ reçoit le nom de “hypothèse nulle” et on la note $\mathcal{H}_0$.

La manière de dire si $\mathcal{H}_0$ est vraie ou fausse est déterminant la probabilité d’observer l’échantillon réalisé. Si la probabilité est très petite (normalement on fixe cette probabilité comme $5\%$), il est très peu probable que $\mathcal{H}_0$ soit vraie, et donc on la rejette, ce qui signifie qu’on accepte sa proposition contraire $P$.

On aura besoin de formuler une autre hypothèse quand on aura rejeté $\mathcal{H}_0$, qui s’appellera l’hypothèse alternative $\mathcal{H}_1$. On notera que les hypothèses ne sont pas nécessairement le contraire l’une de l’autre, et donc $\mathcal{H}_1$ n’est pas exactement $P$.

Il se peut aussi qu’on rejette $\mathcal{H}_0$ quand elle est vraie, ou qu’on échoue à la rejeter quand elle est fausse. Ces deux erreur sont des erreurs de première et deuxième espèce, respectivement.

|  | $\mathcal{H}_0$ est fausse | $\mathcal{H}_0$ est vraie |
| --- | --- | --- |
| Rejeter $\mathcal{H}_0$ | OK | Erreur de Type I |
| Échouer à rejeter $\mathcal{H}_0$ | Erreur de Type II | OK |

On notera α la probabilité d’erreur de première espèce, appelée parfois *seuil*. On prendra en général pour $α$ les valeurs $0.01$, $0.05$ ou $0.1$. Il est a noter que mécaniquement, si l’erreur de première espèce baisse, l’erreur de seconde espèce augmente.

## La variable ou statistique du test

On fixe la définition de la statistique qui nous intéresse. Elle est basée sur l’échantillon observé. Par exemple, la statistique peut être simplement la proportion de piles sur $20$ lancées.

## Zone de rejet et décision

Ayant définie la statistique, on se demande quelle est la probabilité qu’on ait observé la valeur réalisée de cette statistique, appelée $*p$-value*. Si la valeur est $5\%$ ou moins, on rejette $\mathcal{H}_0$, car on se dit qu’il est très peu probable qu’on ait observé la valeur de la statistique seulement par hasard et qu’il doit avoir une autre raison (qui est capturée par $\mathcal{H}_1$).

## Discussion

On peut faire plusieurs remarques sur ce que l’on ressent à propos du test 

- Plus l’échantillon est petit, plus le test est laxiste, mais cela peut-être l’inverse.
- La démarche semble plus robuste si l’on cherche a rejeter l’hypothèse $\mathcal{H}_0$ par analogie avec un raisonnement par l’absurde. (Test au sens de Fisher).
- On est tributaire du hasard dans le tirage de l’échantillon. En effet, les tests ont été créés dans le contexte de la qualité d’une production, ou l’échantillonnage est reproductible et ou on acceptera de jeter une production à tort si on peut sauver d’avantage de séries produites.

Pour toutes ces raisons, les tests ne restent qu’une aide à la décision, même s’ils sont largement utilisés dans tous les domaines scientifiques (sciences humaines, technologiques, économiques...). 

Enfin, en toute rigueur mathématique, le non rejet de l’hypothèse nulle ne vaut pas acceptation, mais nous permet juste de dire que rien ne s’oppose a $\mathcal{H}_0$. On renvoie à la discussion dans l’intervalle de fluctuation.