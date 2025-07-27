# 02 // interactions stratégiques

[Slides de partie 2.pdf](ressources/02_interactions_strategiques_slides_partie_2_micro2.pdf)

# Théorie des jeux non coopératifs

## Introduction

La théorie des jeux est très utilisée en économie. Par exemple : comportements des firmes en concurrence imparfaite et environnement concurrentiel, contrats incitatifs (principal et agent, relation d’emploi…), coordination et incitations au seins d’une entreprise (jeux d’équipe…).

Ils existent deux grandes branches de théories des jeux :

1. Jeux non-coopératifs
    1. Jeux simultanés
    2. Jeux séquentiels
2. Jeux coopératifs

Dans ce cours, on va s’intéreser aux jeux non-coopératifs à information complète. Avant d’y rentrer, on presente un peu de vocabulaire et notions de base.

### Information dans la théorie des jeux

Un jeux est dit **à information complète** si tous les éléments de la liste qui suit sont connus par tous les joueurs. Elle concerne les jeux simultanés et séquentiels. Si l’un de ces éléments n’est pas connu par un joueur, le jeux est **à information incomplète**.

- Préférences de joueurs (utilités associés à chaque résultat)
- Actions disponibles
- Identité et nombre des joueurs
- Ordre des décisions

En plus, **et seulement par rapport aux jeux séquentiels**, on peut mentionner l’information parfaite ou imparfaite, où les joueurs connaissent (ou non) ce que tous les joueurs ont pris comme action toutes les périodes de temps précédentes, respectivement.

### Stratégies pures et mixtes

Une stratégie pure est un algorithme déterministique pour chaque situation où le joueur puisse rencontrer. Une stratégie mixte est une distribution de probabilité sur les actions ou stratégies pures.

## Jeux avec décisions simultanées

### Représentation et concepts

Un jeux simultané est un jeux où les joueurs prennent leurs stratégies au même temps et ils ne jouent le jeux qu’une seule fois. Ils sont représentés sous forme normale (matricielle). Il a trois composants :

- L’ensemble de joueurs : $N = \{1, \dots, n\}$.
- L’ensemble non vide des actions du joueur i : $S_i = \{a_1, \dots, a_m\}$
- La fonction d’utilité pour le joueur $i$ asocié à chaque situation (combinaison d’actions de tous les joueurs). $u_i(S) : \underbrace{S_1 \times \dots \times S_n}_{S} \mapsto \R$.

Les concepts et vocabulaire de base sont les suivants :

- Action : ce qui le joueur peut jouer. Elles sont contenues dans $S_i$ pour le joueur $i$.
- Stratégie : une série d’actions qui définit totalement (déterministiquement) le comportement du joueur. Elle peut être vue aussi comme un algorithme pour le jeu.
- Gains : les résultats du jeu associés au choix de ces stratégies. Ils sont le résultat de la fonction d’utilité $u_i$ pour le joueur $i$.

### Stratégies pures et l’équilibre de Nash pure

La stratégie pure propose une définition complète du comportement du joueur pour toute situation envisageable. À nouveau, c’est un algorithme déterministique. Une petite note importante c’est que une stratégie peut être aussi prendre une seule action. Dans ce cas, une stratégie se confond avec une action, mais normalement “stratégie” et “action” sont différentes et à ne pas confondre.

Pour construire un stratégie pure, on doit déterminer la meilleur stratégie pour chaque situation. Une telle manière c’est la méthode d’élimination par itération des stratégies strictement dominées**.**

**Élimination des stratégies dominées**. On dit qu’une stratégie $s’_i$ est *strictement dominée* par $s_i$ ****si, les actions des autres constantes, les gains de $i$ sont toujours strictement supérieurs s’il joue $s_i$ à la fois de $s’_i$.

Ayant défini une stratégie pure, on peut maintenant parler de **l’équilibre de Nash** pure :

> Un équilibre de Nash dans un jeu de deux joueurs est une paire de stratégies, chacune étant la meilleure réponse â l’autre.

Plus généralement, un équilibre de Nash est une liste de stratégies, une par joueur, telle qu’aucun joueur n’est incité à changer unilatéralement la sienne, en termes d’amélioration de son propre gain.
> 

**Théorème**. Un équilibre atteint utilisant la méthode par élimination des stratégies dominées est toujours un équilibre de Nash. **Par contre, la réciproque est fausse** : ils existent d’équilibres de Nash qui ne sont pas atteints par l’élimination des stratégies dominées. 

On peut rencontrer aussi des stratégies *faiblement dominées*, où les gains de $i$ jouant $s’_i$ sont au moins aussi importants que s’il joue $s_i$, les actions des autres constantes.

Quand ils n’existent pas des stratégies dominées, strictement ou faiblement, la méthode présentée avant n’est pas utile pour trouver des équilibres de Nash. Ici, on présente la méthode des croissement des meilleures ripostes.

**Croissement des meilleures ripostes**. Une meilleure riposte pour joueur $i$ est la meilleure stratégie en fixant une stratégie de joueur $i’$ au préalable (même si le jeux est simultané). La croissance de meilleures ripostes est une liste d’stratégies telle que chaque stratégie de chaque joueur est son meilleure riposte aux stratégies des autres.

Il se peut qu’on trouve plus d’un équilibre de Nash, ce qui est totalement valide. On peut raffiner le choix d’équilibre de Nash, c’est-à-dire classifier les équilibres de Nash :

- Équilibre pareto-dominant : c’est l’équilibre de Nash dont la somme d’utilités de tous les joueurs est la plus grande.
- Équilibre dominant par le risque : c’est simplement l’équilibre de Nash qui assure des utilités modeste au pire et de meilleures utilités au mieux, pour chaque joueur.

Ils existent des définitions plus mathématiques de ces deux raffinements ici : [https://en.wikipedia.org/wiki/Risk_dominance#:~:text=Risk dominance and payoff dominance,Nash equilibria in the game](https://en.wikipedia.org/wiki/Risk_dominance#:~:text=Risk%20dominance%20and%20payoff%20dominance,Nash%20equilibria%20in%20the%20game)

**Point focal**. Ce n’est pas exactement un équilibre de Nash, c’est une solution que les gens ont tendance à choisir par défaut en l'absence de communication. Elle est faite à partir du sens commun.

**Note #1**: il est irrelévant de classifier un équilibre comme dominant par le risque ou pareto-dominant s’il n’y a qu’un seul équilibre issue de l’élimination de stratégies strict. dominées.

**Note #2**: aucun jeu à somme nulle a un equilibre de Nash pure.

**Note #3**: si le prof. n’explicite pas de chercher un équilibre (mixte), on juste cherche les équilibres pures.

### Théorème de tradition orale

Pensons au dilemme des prisonniers :

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled.png)

Après avoir analysé, on sait que le seul équilibre de Nash est si les deux prisonniers se dénoncent, c’est un équilibre qui domine par le risque. On se demande alors si les joueurs pourrait jamais choisir une situation (pas nécessairement un équilibre !) qui soit efficient au sens de Pareto : où on ne peut pas améliorer la situation d’un joueur sans rendre pire la situation d’un autre.

En fait, il est possible de tomber sur la situation Pareto-efficient où les deux se taisent, mais il faudrait jouer le jeux une infinité de fois.

Si on jouait le jeu une quantité finie de fois connue, à chaque jeu les prisonniers vont se dénoncer. Cela dit, si on jouait le jeu à l'infini et si les joueurs sont “suffisamment patients”, il existe un équilibre de Nash où les joueurs se taisent à chaque fois.

> **Théorème de tradition orale**. Pour un jeu infiniment répété, toute stratégie qui donne un gain au moins égal à celui qu’on obtiendrait avec l’équilibre de Nash du jeu de base peut être un équilibre possible, si la préférence pour le présent n’est pas trop forte.
> 

On mesure la préférence pour le présent avec un facteur de réduction $\delta$ (entre 0 et 1) des utilités des jeux futurs. Si jamais un des joueurs se détourne de la situation pactée, l’autre joueur peut donc jouer son action individuelle minmax en permanence (grim trigger) et l’utilité que le joueur égoïste aurait reçu ne sera pas la peine dans le futur, avec l’infinité des situation qui arrivent.

Ici un lien utile : [https://en.wikipedia.org/wiki/Folk_theorem_(game_theory)#:~:text=In game theory%2C folk theorems,of an infinitely repeated game](https://en.wikipedia.org/wiki/Folk_theorem_(game_theory)#:~:text=In%20game%20theory%2C%20folk%20theorems,of%20an%20infinitely%20repeated%20game).

### Stratégies mixtes

Il n’est pas rare de trouver des jeux où il n’y a pas d’équilibres de Nash. Les jeux à somme nulles n’ont jamais d’équilibres de Nash. Donc, on a recours aux stratégies mixtes. Pour trouver la meilleure stratégie mixte, on doit associer une possibilité à chaque stratégie.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_1.png)

Après, on calcules les utilités espérées de Lui et Elle étant donné qu’il va au théâtre $T$ ou au football $F$. Dans ce cas : 

$$
\mathbb{E}[L(T)]=2t+0(1-t) = 2t
\newline
\mathbb{E}[L(F)]=0t+(1-t) = 1-t
\newline
\text{ }
\newline
\mathbb{E}[E(T)]=0q+(1-q) = 1-q
\newline
\mathbb{E}[E(F)]=2q+0(1-q) = 2q
$$

Maintenant, on compare les utilités associés à chaque action pour chaque joueur. Un joueur va jouer une stratégie $i$ pour une certaine probabilité associé si l’utilité espérée à cette stratégie est supérieur aux autres stratégies. 

Par exemple, pour lui, l’utilité espérée de jouer $T$ est supérieur à $F$ quand $2t > 1-t$, où $t>\frac{1}{3}$. Donc, si on pense rationnellement, il va jouer $T$ si son utilité associée est supérieur à jouer $F$, ce qui dépend de si $t>\frac{1}{3}$ ou non. On raisonne similairement pour elle et on arrive à qu’elle va jouer $T$ si $q < \frac{1}{3}$ et $F$ sinon.

Un petit détail ce que on construit l’espérance d’une action avec les probabilités des actions des autres joueurs, pas avec les probabilités du même joueur !!!

Finalement, on peut construire notre fonction de décision. Une décision est une action avec probabilité $1$, càd. avec certitude. Pour lui, s’il sait que $\mathbb{P}(E(T))=t>\frac{1}{3}$, il voudra toujours aller au théâtre, donc il fixera $q=1$ et $q=0$ sinon. Pareillement pour elle, qui fixera $t=1$ ou $t=0$ si $\mathbb{P}(L(T))=q<\frac{1}{3}$ ou non, respectivement.

On construit alors les fonctions de meilleures décisions pour chaque joueur :

$$
\mathbb{P}(L^*(T))=
\begin{cases}
1, \text{ si } t > \frac{1}{3} \\
0, \text{ si } t < \frac{1}{3}
\end{cases}
\space\space\text{et}\space\space
\mathbb{P}(E^*(T))=
\begin{cases}
1, \text{ si } q < \frac{1}{3} \\
0, \text{ si } q > \frac{1}{3}
\end{cases}
$$

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_2.png)

Les lignes rouges et bleus sont les fonctions de meilleures décisions. Leur point de coupure indiquent un équilibre de Nash mixte. Ces fonctions peuvent nous montrer aussi plusieurs équilibres, par exemple :

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_3.png)

Mais notons, les équilibres à $(0,0)$ et $(1,1)$ sont décisions pures et déterministes, donc elles correspondent à d’équilibres de Nash pures.

> **Théorème de Nash**. Tout jeu fini possède au moins un équilibre de Nash si les stratégies mixtes sont autorisées.
> 

Ceci est garanti si et seulement si :

1. L’ensemble de stratégies de chaque joueur est convexe et compact,
2. La fonction de paiement de chaque joueur est continue et concave en la
propre stratégie du joueur.

## Jeux avec décisions séquentielles

### Représentation et concepts

Un jeu sous forme extensive représente :

- le nombre de joueurs
- quel joueur joue pour chaque étape du jeu
- les actions de chaque joueur
- ce que les joueurs savent au moment où ils jouent
- les gains de chaque joueur pour chaque issue possible du jeu

On utilise un arbre de jeu où, à chaque point de décision, il existe un nœud. Le premier nœud au début du jeu s’appelle le nœud de départ, et les nœuds au bas du jeu s’appellent les nœuds terminaux, chacun contenant les gains des joueurs **par ordre d’apparition dans le jeu**.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_4.png)

Dans ce type de jeux, il est important de mentionner la notion d’information parfaite et imparfaite. L’information est parfaite quand chaque joueur connaît les actions précédentes de toutes les périodes de temps précédentes pour tous les joueurs.

Si on parle d’information imparfaite en jeux séquentiels, il faut parler de l’ensemble d’informations, qui est l’ensemble de nœuds où le même joueur joue et où il ne sait pas à quel nœud particulier il se trouve. Dans l’image précédente, l’ensemble d’information de J2 sont ses deux nœuds, supposons qu’il sait pas ce que J1 a joué.

Tout jeu sous forme extensive peut s’écrire sous forme normale si toutes les stratégies possibles de joueurs sont spécifiées de manière suffisamment exhaustive, **il faut que ce soit en information imparfaite pourque ça puisse simuler un jeux de décisions simultanées**.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_5.png)

[Deriving Normal Form from Extensive Form Games.pdf](ressources/02_interactions_strategiques_deriving_normal_form_from_extensive_form_games.pdf)

### L’équilibre de Nash parfait en sous-jeux

Avant d’introduire cette notion d’équilibre, il faut définir ce qui est un sous-jeu : c’est simplement un ensemble composé d’un nœud et tous les nœuds qui le succèdent. Le jeux même est un sous-jeu de lui-même.

Après, on peut parler de l’induction à rebours : c’est une méthode pour trouver d’équilibres de Nash d’un jeu séquentiel. On commence par les états finaux ou nœud terminaux du jeu et on monte et passe par chaque sous-jeu récursivement vers le nœud initial. À chaque nœud, on determine l’action optimale du joueur qui joue.

L’équilibre qui sort de cette méthode est appelé ***équilibre parfait en sous-jeu***. Formellement, est une combinaison de stratégies telle que les actions prescrites par ces stratégies constituent un équilibre de Nash dans tous les sous-jeux.

![Avec l’induction à rebours, l’équilibre parfait en sous-jeu est {Dp, tl}.](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_6.png)

Avec l’induction à rebours, l’équilibre parfait en sous-jeu est {Dp, TL}.

Note #1 : Un équilibre parfait en sous-jeu est un équilibre de Nash. **Reciproque fausse**.

Note #2 : dans les jeux simultanées, un équilibre de Nash pure était un ensemble avec **juste une action** pour chaque joueur. Ici, est une **liste de actions** pour chaque joueur.

### Applications : menace crédible et engagement stratégique

Supposons qu’ils existent les joueurs A et B. A communique à B que son comportement mènera une réponse de la part de A. Si telle réponse est un net positif, est un engagement. Sinon, est une *bluff*. Une menace est crédible si la réponse est un net positif, et non-crédible sinon. Cette définition est celle de Schelling.

Particulièrement, une menace non-crédible est faite avec l’espoir de ne pas l’éxécuter, car elle serait pénalisante.

Dans le graphique d’un jeu séquentiel, pour que une menace soit crédible dans un équilibre, à chaque nœud ou on peut exécuter la menace, on l’éxécute.

![Le rouge est un équilibre parfait de sous-jeu, tant que le bleu est un équilibre de Nash tout court.](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_7.png)

Le rouge est un équilibre parfait de sous-jeu, tant que le bleu est un équilibre de Nash tout court.

# L’oligopole non coopératif

<aside>
💡 Une firme dans ce contexte d’oligopole est censée de vouloir toujours maximiser le profit mathématiquement. Les critères de gestion alternative comme la gestion à l’équilibre n’existe plus ici. On est dans le contexte de théorie de jeux.

</aside>

## Duopole de Cournot (concurrence par la $q$, simultané)

<aside>
💡 Un exo de Cournot à l’examen prend 10 minutes, maximum 15 minutes.

</aside>

### Description et hypothèses du modèle

- Deux firmes produisent un bien homogène en quantités $q_1$ et $q_2$, respectivement.
- Leur fonctions de coût total sont identiques : $C_1(q_1) = C_2(q_2)$.
- La production totale de l’économie est la sommes des quantités : $q = q_1+q_2$.
- La demande est atomique : $p=p(q)=p(q_1+q_2)$
- La variable stratégique est la quantité et non pas le prix.
- Les firmes veulent maximiser son profit.
- **Variation conjecturale** : chaque firme fait une conjecture sur la production de son concurrent en réaction à sa production propre, puis elle corrige sa production.

Comme conclusion du modèle, l’équilibre de duopole atteint nous mène à des prix, quantités et profit intermédiaires entre le prix de monopole et le prix concurrentiel.

En termes d’efficacité, il est préférable pour les consommateurs d’avoir un duopole à la Cournot sur un monopole, tant que pour les firmes il serait mieux d’agir comme un monopole (oligopole coopératif, où deux firmes sous une entente).

### L’équilibre de Cournot-Nash

L’équilibre des quantités produites est déduit en appliquant la condition d’optimisation de premier ordre des profits de chaque firme.

$$
\text{Profit de }i : \pi_i(q_i+q_j)=p(q_i+q_j)\times q_i -C(q_i)

\\
\text{}
\\

\text{CPO} : \frac{\partial \pi_i}{\partial q_i} = 0 \iff \frac{\partial p(q_i+q_j)}{\partial q_i}q_i + p(q_i+q_j) - \frac{\partial C(q_i)}{\partial q_i} =0
$$

La fonction qui resulte d’appliquer la CPO, et isolant $q_i$ d’un seul côté, au profit de la firme $i$ est la **fonction de réaction de la firme $i$**. **Notons qu’elle prend comme argument la quantité de l’autre firme !**

$$
q_i = R_i(q_j)= \frac{1}{\partial p/\partial q_i}\left(\frac{\partial C}{\partial q_i} -  p(q_i+q_j) \right)
$$

L’équilibre est donc le pair de quantités qui satisfait le système d’équations ci-dessous :

$$
\left.
\begin{array}{l}
q_i=R_i(q_j)
\\
q_j=R_j(q_i)
\end{array}
\right\} \implies 
\begin{array}{l}
q_i^* = R_i(R_j(q_i)) \\
q_j^* = R_j(R_i(q_j))
\end{array}
$$

Cet équilibre $(q_i^*,q_j^*)$ est un équilibre de Cournot-Nash. Il correspond à l’intersection des fonctions de réaction.

### Analyse graphique

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_8.png)

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_9.png)

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_10.png)

### Représentation sous forme normale

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_11.png)

Si l’équilibre de Nash trouver n’est pas celui trouvée par le système d’équation, **on a un erreur**. Il peut avoir deux sources d’erreur : erreur dans le calculs des $q$ d’equilibre, ou erreur dans le calculs des profits $\pi$.

**Note practique** : toute stratégie hors d’équilibre en Cournot est strictement dominée, à la hausse et à la baisse.

## Duopole de Stackelberg (concurrence par la $q$, séquentiel)

### Description et hypothèse du modèle

Les hypothèses restent presque les mêmes en comparaison au duopole de Cournot, à exception que ce jeu est séquentiel et non pas simultané. Particulièrement, l’hypothèse de séquentialité est énoncée comme suit :

- La firme *leader* a une information complète sur la courbe de réaction de l’autre
firme. La firme *follower* cherchera à maximiser son profit compte-tenu de la situation qui a été créée par la firme leader.

### Détermination de l’équilibre

Le leader choisira la quantité que maximise son profit, supposant qu’il connaît la quantité de réaction du follower. Donc, en comparaison avec Cournot, la firme follower maintient sa fonction de réaction (le follower accepte la quantité du leader comme constante), tant que le leader utilise la fonction de réaction du follower dans sa propre réaction.

$$
\text{Cournot : }\frac{\partial p(q_1+q_2)}{\partial q_1}q_1 + p(q_1+q_1) - \frac{\partial C(q_1)}{\partial q_1} =0
\\
\text{}
\\
\text{Stackelberg } : \frac{\partial p(q_1+R_2(q_1))}{\partial q_1} q_1 + p(q_1+R_2(q_1)) - \frac{\partial C(q_1)}{q_1} =0
$$

Le critère de réaction de la firme leader sera le $q$ qui maximise le profit, qui est-ce qui est exprimé en haut. Notons qu’on ne parle plus d’une fonction de réaction du leader.

### Analyse graphique

Pour représenter l’équilibre sur un graphique, il faudrait aussi représenter des courbes *isoprofits*. Ce sont des courbes qui représentent un même profit \pi pour toute combinaison de q_1 et q_2 qui l’atteignent.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_12.png)

Plus inférieure est la position de l’isoprofit, plus grand est le profit qu’elle représente. Pour chaque niveau de production de $q_2$, on trace une ligne horizontale qui coupe quelque courbe d’isoprofit forcément dans son sommet. Ce point-là correspond à la quantité $q_1$ que le leader doit produire pour maximiser son profit.

D’autre manière, pour le $q_1$ de chaque sommet d’isoprofit, il existe un $q_2$ duquel produire $q_1$ atteint le profit maximum.

![Notons que le sommet est aussi où la droite tangente est constante.](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_13.png)

Notons que le sommet est aussi où la droite tangente est constante.

Quand le leader maximise son profit, il connaît la fonction de réaction de la firme follower. Il commencera à descendre d’isoprofit en isoprofit jusqu’à arriver à la dernière isoprofit qui touche la fonction de réaction du follower. Ce courbe-la est le profit maximum, et son point de coupure avec $R_2$ contient le $q_2$ qui maximise le profit.

![**LE POINT OU $R_1 = R_2$ EST L’ÉQUILIBRE DE COURNOT. DONC $\pi^\text{Stack}_1 > \pi_1^\text{cournot}$.**](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_14.png)

**LE POINT OU $R_1 = R_2$ EST L’ÉQUILIBRE DE COURNOT. DONC $\pi^\text{Stack}_1 > \pi_1^\text{Cournot}$.**

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_15.png)

Conclusions :

- Le suiveur produit moins que chez Cournot, le leader produit plus que chez Cournot.
- La $q$ du leader est plus grande que la $q$ du follower.

### Représentation sous forme extensive

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/ressources/02_interactions_strategiques_untitled_16.png)

- L’équilibre de Stackelberg est l’équilibre de Nash parfait en sous-jeu.

## Duopole de Bertrand (concurrence par le $\$$, simultané)

### Description et hypothèses de base

Hypothèses “évidentes” :

- La firme cherche à maximiser son profit.
- Le bien produit est parfaitement homogène.
- Les firmes ont la capacité de production pour fournir la totalité du marché.

Hypothèses plus importantes : 

- La variable stratégique de chacune des firme sur le marché est le **prix**.
- La demande assumée par chaque firme dépend de son niveau de prix par rapport à l’autre firme. Particulièrement, pour la firme $i$, sa quantité demandée est :
    
    $$
    D_i(p_1,p_2)=
    \begin{cases}
    D(p_i), \text{ si } p_i<p_j \\
    \frac{D(p)}{2}, \text{ si } p_i=p_j=p \\
    0, \text{ si } p_i>p_j
    \end{cases}
    $$
    

### Détermination de l’équilibre

> **Théorème de Bertrand**. Sous les 5 derniers hypothèses, le seule équilibre de prix est $p_1^*=p_2^*=Cm$.
> 

Mais notons, $p=Cm$ est la condition d’équilibre d’un marché concurrentiel, donc l’équilibre est celui de la concurrence parfaite. Encore plus, **on suppose que $Cm$ est constante !**

La **paradoxe de Bertrand** est que, alors qu’elles sont deux, les entreprises agissent
comme si elles étaient un nombre infini. Elles se comportent ainsi conformément à l’hypothèse d’atomicité de la concurrence parfaite.

L’équilibre de Bertrand, comme l’équilibre de Cournot, est un équilibre de Nash.

On arrive mathématiquement à que $Cm$ est le prix d’équilibre si on cherche les prix de $i$ (resp. $j$) qui maximise son profit respectif. **Celle-ci est aussi la fonction de réaction**. C’est-à-dire :

$$
R_i(p_j)=p_i^*=\argmax_{p_i} \pi_i(p_i,p_j), \text{ où } \pi_i(p_i,p_j)= \overbrace{(p_i-Cm)}^{\text{ Revenu moyen}} \times D_i(p_i,p_j)
$$

### Conclusion

On note que si $p_i=c$, donc $p_i-c=0$, donc si le revenu moyen de chaque unité vendue est $0$, le profit $\pi_i$ est aussi $0$, donc l’équilibre de Bertrand correspond à l'optimum social (équilibre de concurrence). Il est donc préférable pour les consommateurs sur les duopoles de Cournot et Stackelberg.

**Le résultat de Bertrand dépend de plusieurs hypothèses très restrictives.** 

Particulièrement, il se peut qu’il soit plus profitable pour une entreprise A de n’est pas concurrir par le prix si son concurrent ne peut pas couvrir toute la demande de marché avec sa production.