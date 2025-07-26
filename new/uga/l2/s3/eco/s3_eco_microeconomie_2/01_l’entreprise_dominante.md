# 01 // l’entreprise dominante

[Slides de partie 1](slides_partie_1_micro2_vers_et_2022.pdf)

# Le monopole

La définition la plus basique d’un monopole est celle firme qui est le seule producteur dans un marché. On pourrait mentionner ici que la firme propose un prix plus haut au prix concurrentiel.

## La maximisation du profit

### Tarification du monopole

Rappelons que la fonction de demande est une correspondance de la quantité demandé en fonction du prix. Par habitude, on exprime plutôt la fonction de demande inverse, $p(q) = aq + b$, avec $a<0$ et $b>0$.

D’ailleurs, le profit du monopole s’écrit : $\pi = RT(q) - CT(q)$.
RT est la recette totale ou revenu totale, et CT est le coût totale.
Si on analyse le terme RT, on sait que $RT(q) = p(q) \times q$. C’est la quantité de produit vendus fois leur prix.

**Note** : dans la concurrence parfaite, $RT(q) = p^* \times q$. Ici, $p^*$ est une constante, est le $p$ de l’intersection de l’offre et la demande, ce qui est différent de $p(q)$. Par contre, dans le monopole, on utilise effectivement toute la courbe de demande $p(q)$ dans la recette totale.

La chose à retenir c’est que le prix du marché établi par le monopôle dépend du comportement de l’ensemble des consommateurs, c’est-à-dire de la fonction de demande du marché (inverse).

En outre, ils existent d’autres indicateurs basées sur la recette :

- Recette moyenne : $RM = \frac{RT(q)}{q}$
- Recette marginale : $Rm = \dfrac{\mathrm{d}}{\mathrm{d}q} RT(q)$
- Pour le monopole, la recette marginale est toujours inférieure à la recette moyenne (pas le cas dans concurrence parfaite).

Finalement, il existe une relation entre $Rm$, $p$ et la elasticité-prix $\epsilon$.
Sachant que la condition de maximisation de profit c’est $Rm = Cm$, on obtient avec un peu d’algèbre…

$$
Rm = Cm = p(q)[1-\frac{1}{|\epsilon|}]
$$

On peut réarranger cette dernière équation pour obtenir la règle de l’élasticité inverse ou règle de mark-up.

<aside>
🖊️ *Le prix de marché est un **taux de marge** sur le coût marginal.
Un monopole augmente son taux de marge à mesure que la demande
devient faiblement élastique.*

</aside>

$$
\underbrace{\frac{p-Cm}{p}}_{\text{Taux de marge}}=\underbrace{\frac{1}{|\epsilon|}}_\text{Élasticité inverse}
$$

### Pouvoir de marché du monopole

Le pouvoir de marché est la capacité d’une firme à proposer un prix supérieur à son coût marginal. L’intensité du pouvoir de marché est mesurée par la règle de
l’élasticité inverse ou règle du mark-up qui définit de fait l’indice de Lerner :

$$
L=\frac{p-Cm}{p}=\frac{1}{|\epsilon|}
$$

- Si $|\epsilon| → \infin$, donc $L → 0$, qui est le cas de concurrence parfaite.
- Si $|\epsilon| → 0$, donc $L → \infin$, qui est le cas du monopole (ou plutôt un nombre très grande, car $\infin$ n’est pas une quantité spécifique !)
- Le pouvoir de marché d’un monopole est inversement proportionnel à l’élasticité-prix de la demande de marché.

### Equilibre du monopole et économie du bien-être

Une *perte sèche* ou *charge morte* (deadweight) est une quantité de transactions qui n’est pas faite qui serait faite s’il y avait un équilibre concurrentiel, c’est-à-dire, s’il avait une offre tel que $p(q)_D = Cm$ . (à gauche c’est le prix demandé). Notons que dans l’équilibre concurrentiel (ou il y a plain d’entreprises), $P = Cm$, tant que en équilibre de monopôle, $P > Cm$.

Dans le cas monopole, la quantité offerte $q^*$ est celle où on vérifie $Cm = Rm$. Puis, pour savoir la quantité vendue, on cherche le prix $p^*$ qui correspond à la quantité de l’équation précédente, on determine l’équilibre de monopole $(p^*, q^*)$ et finalement on est capables de calculer $\pi$.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled.png)

## Règles alternatives de gestion

### Maximisation du chiffre d’affaires

À la place produire la quantité $q$ qui vérifie l’équation $Cm = Rm$, on cherche $q$ tel que $Rm = 0$. Un monopole peut décider d’en faire pour maximiser ser ventes (même si cela ne maximise pas le profit !).

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_1.png)

### La tarification au coût marginal (prix “concurrentiel”)

Situation où $p(q) = Cm$. EDF, GDF (anciennement Gaz de France), SNCF, Orange sont tous des monopoles naturels. Pour motives de justice sociale, l’état les oblige de tarifer au coût marginal pour limiter leur pouvoir de marché. C’est comme cela qu’on passe du monopôle naturel au monopôle institutionnel.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_2.png)

### La gestion à l’équilibre

Un monopole publique est censé de couvrir ses coûts et de bénéficier au consommateurs. Donc, si jamais on trouve deux valeurs de $q$ qui satisfassent l’équation $p(q) = CM$, prendre la quantité la plus petite est paradoxale au but de bénéficier le consommateur, car y'a de consommateurs qu'on pourrait bénéficier sans rien perdre. $\pi$ doit être forcément égal à 0.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_3.png)

Apparemment selon le prof., “si $Cm > CM$, tarification au $Cm$ plus bénéfique pour le surplus collectif que la gestion à equilibre”.

## Monopole naturel et monopole soutenable

### Le monopole naturel

Il existe une définition économique et une autre mathématique de “monopole naturel”.

- Économiquement, une entreprise est un monopole naturel quand il est moins coûteux de produire à une seule entreprise plutôt qu’à plusieurs pour servir le marché (c’est-à-dire, la demande).
- Mathématiquement, la fonction de coût du bien concerné est *sous-additive* : $C(q) < C(q_1) + C(q_2)$, où $q = q_1 + q_2$. Par exemple, le coût de produire 50 unités, puis 100 unités est supérieur que de produire tout simplement 150 unités d’un seul coup. Valable aussi avec les couts moyens.

Une conséquence de cette définition est qu’une condition suffisante pour avoir un monopole naturel est que les couts moyens $CM$ soient décroissants pour tout niveau de production. $CM$ décroissant $\implies$ Rendements croissants.

**Attention**. Voyons le cas des activités multi-produits : **la propriété de rendements d’échelle croissants ne constitue ni une condition suffisante ni nécessaire de la sous-additivité des coûts**. De là l’importance des *économies de gamme*.

### Du monopole naturel au monopole soutenable

Pour chercher à se prémunir de l’entrée de nouveaux concurrents, le monopole naturel doit être *soutenable*. Un monopole est soutenable si et seulement s’il exerce une combinaison prix-quantité “soutenable”.

C’est-à-dire, si le monopole produit une couple $(p,q)$ où la courbe de demande coupe la courbe de coût moyen (dans sa phase décroissante), mathématiquement $p(q) = CM$. Notons que cette dernière égalité implique que le monopole soutenable applique *au moins* la stratégie de gestion à l’équilibre où $RM = 0$.

Formellement, un monopole naturel est un monopole soutenable si :

1. Il existe $q$ tel que $\frac{C(q_s)}{q_s} = p(q_s)$. La première fraction est égale à $CM$.
2. $p(q_s) \times q_s - C(q_s) ≥ 0$. Le monopole est profitable.
3. Si toute couple $(p_e, q_e)$ telle que $p(q_e) < p(q_s)\text{ et }q_e \le Q_D(p_e) \implies p(q_e) \cdot q_e - C(q_e) < 0$. Toute couple où le prix de l’entrant soit inférieur au monopole et son coût soit plus grand que son revenu implique que son profit est forcément négatif.

Notons que, dans cette situation, on suppose que le monopole et la firme entrante ont la même courbe de coûts.

![asd.png](asd.png)

Étude de cas limite : dans la prochaine image, il existe un monopole qui produit à la coupure entre la demande et le $CTM$. Notons que le monopole peut vendre son bien à toute demandeur au-dessus du point de coupure, mais il laisse le segment entre le point de coupure et les prix $p_0$ où $CTM$ est dessous du prix de la coupure. Un entrant pourrait produire une quantité parmi elles, disons $q_0$, et proposer un prix entre $p_0$ et $p(q_m)$, ce qui le permet un profit.

Ce dernier étude limite met un point sur l’importance que le point de coupure soit à gauche du minimum de la courbe de $CTM$ et pas à droite de celle-ci.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_4.png)

**Tip** : différence avec gestion à l'équilibre et monopole soutenable. Le dernier utilise, au pire, le critère de gestion à l'équilibre et, EN PLUS, il faut être au minimum de la courbe CTM. À gauche du minimum est soutenable, à droite du minimum non (voir photos).

# Entreprise dominante et dissuasion à l’entrée

## La stratégie du prix limite

### Définition et hypothèses de base

La notion de comportement stratégique est la base de la théorie des jeux, et c’est que les décisions des agentes sont interdépendantes. On peut le voir comme “je sais que mes actions auront des conséquences sur les autres”.

Ils existent deux définition de la stratégie du prix limite : celle de Glais est un peu vague, tandis que celle de Carlton et Perloff nous permet de construire notre modèle.

- **Définition de Glais**
Le prix limite est une stratégie de prix qui correspond à proposer un prix inférieur au prix qui maximise le profit propre.
- **Définition de Carlton et Perloff**
Le prix limite est un prix proposé tel que la demande résiduelle de l’entrant soit insuffisante pour permettre à l’entrant de faire du profit non-négatif.

Dans ce dernier, la *demande résiduelle* est la demande qui va rester à l’entrant s’il rentre au marché. Mathématiquement, le demande résiduelle est égale à la demande de marché originale moins la quantité produite par le monopole.

Le prix limite n’est pas le prix de marché, mais le prix stratégique que la firme installe propose en anticipant que l’entrant propose son prix de marché.

Côte hypothèses, on a 4 premières hypothèses de “sens commun”, et on ajoute 2 autres pour construire le modèle Sylos-Labini de cette stratégie.

1. On se place sur deux périodes, avant et après l'entrée.
2. On considère deux firmes : la firme installée, présente durant les deux périodes, et l'entrant potentiel.
3. La demande est stable dans le temps.
4. Les consommateurs sont indifférents au choix de l'une ou l'autre firme.
5. Sylos-Labini : la firme en place maintient le niveau de production initial en période 2.
6. Sylos-Labini : l'entrant potentiel anticipe une absence de réaction de la firme installée à la suite de son entrée.

### Situation #1 : Avantage absolu de coût et économies d’échelle

Point de départ : le prix fixé par l'entreprise installée peut être supérieur au coût moyen de l'entrant potentiel, et **dissuader malgré tout l'entrée**. C’est ça l’avantage absolu de coût.

### Conditions initiaux

Sur un marché, la fonction de demande d'un produit est donnée par la forme linéaire classique : $p(q) = b - aq$, avec $a,b>0$.

L’entreprise installée produit une quantité $q_F$ à coûts constants : $Cm = CM = c$, où $c \in \R^+$.

### Entrée de la firme rivale et prix limite

Une firme désire entrer sur le marché pour produire une quantité $q_e$ à un coût $c_e$, avec $c_e > c$, afin de respecter l'existence de l'avantage absolu de coût. À quel niveau la firme installée peut-elle fixer son prix pour rendre l'entrée non profitable ?

D'après hypothèse 6 de Sylos-Labini, l'arrivée du concurrent occasionne une baisse du prix du marché à cause de la production supplémentaire de l'entrant. Ainsi, pour que l'entrée ne soit pas profitable, il faut que le prix du marché, à l'issue de l'entrée, soit inférieur au coût de production de l'entrant potentiel.

Le prix de marché est $p = b - a(q_F + q_e)$. S’il doit être inférieur au coût de l’entrant, donc $p < c_e \iff b - a(q_F + q_e) < c_e$.

On veut vérifier la dernière inégalité. Il existe un prix $p_F$ associé a la quantité de la firme installée, $q_F$. $p_F = b - aq_F$. Donc, on isole $q_F$ pour injecter $p_F$ dans l’inegalité à vérifier. On arrive à :

$$
b - a(\frac{1}{a}(b-p_F) + q_e)<c_e \iff p_F < c_e +aq_e
$$

Le prix de vente qui dissuadera l'entrée d'un concurrent potentiel est donné par l'inégalité précédente : il s'agit du prix-limite.

**Plus l'entrant a fixé un volume de production important, plus le prix du marché baissera suite à l'entrée et plus le prix limite pourra être élevé par rapport aux coûts de l'entrant.**

Si on fait un raisonnement algébrique identique, on peut montrer que la condition $c_F + aq_e < p_F$ doit être vérifiée pour que la firme installée ne fasse pas de perte une fois l'entrée réalisée.

Finalement, le rangs de prix limites $p_F$ sont ceux qui vérifient :

$$
c_F + aq_e < p_F < c_e +aq_e
$$

### Situation #2 : Avantage lié à des économies d’échelle

Point de départ : la firme installée et l’entrant potentiel disposent de la même technologie, c’est à dire possèdent une structure de coûts identique.

La firme en place peut profiter de sa présence antérieure sur le marché pour dégager d’importantes économies d’échelle (donc vendre d’importantes quantités). Elle ne laisse à l’entrant potentiel qu’un volume trop faible pour être rentable. **Basiquement, les consommateurs de la firme installée ne vont pas acheter le produits de la firme entrante, même s’il sont au même prix**.

Dans cette première situation, on voit que la firme installé peut appliquer la stratégie de monopole de maximisation de profit (vendre $q$ qui vérifie $Cm(q) = Rm(q)$), et que cela déjà suffit pour dissuader l’entrant qui voudrait appliquer la même stratégie.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_5.png)

Par contre, dans cette deuxième situation, la firme installée ne peut pas appliquer la maximisation de profits, car la quantité $q_m$ lié au résultat de la stratégie ne vérifie pas les inégalités importantes pour dissuader l’entrant qui applique aussi la stratégie de maximisation de profits $Cm_e = Rm_e$. Donc, la firme installer décide de choisir arbitrairement $q_L$, et cette quantité-ci arrive à dissuader l’entrant.

Remarque : car la firme installée ne peut pas appliquer la maximisation de profits, elle n’est plus un “monopole”, mais juste une entreprise dominante. 

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_6.png)

## La stratégie de prédation par le prix

### Définition et conditions

La stratégie de prédation par le prix est une stratégie qui s’agit de fixer un prix suffisamment bas pour une période suffisamment longue pour :

- soit pour éliminer une partie ou la totalité de la concurrence existente,
- soir pour dissuader une partie ou la totalité de la concurrence potentielle.

Une fois que les concurrents ont abandonné le marché ou que les entrées potentielles
sont évitées, le prédateur pourra alors augmenter ses prix de façon significative.

Pour qu’elle soit effective, la prédation par le prix doit être *crédible*, pour les concurrents actuels et les potentiels. Notons que le prix prédateur à deux fonctions simultanées : pour les concurrents potentiels, le prix prédateur est une *signal* de ce que les arriverait s’ils rentrent au marché. Au même temps, le prix prédateur permet d’eliminer la concurrence actuelle.  

### Hypothèses de base

1. L'entreprise prédatrice dispose de moyens financiers suffisants.
2. Deux entreprises ayant une structure de coût identique se partagent le marché.
3. L'entreprise prédatrice est anciennement installée, la "victime" est nouvellement installée.

Dans le graphique ci-dessous, lorsque le prix du marché est $p^*$, les consommateurs achètent une quantité $q^*$.

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_7.png)

![untitled](new/uga/l2/s3/eco/s3_eco_microeconomie_2/01_l’entreprise_dominante/untitled_8.png)

<aside>
💡 Si on était dans une situation de prix limite et on fixe “bêtement” un prix limite tel que $p$ soit toujours dessous de la courbe de couts moyens de l’entrant, cela est plutôt prédation par le prix et non un prix limite. 

Le fait de fixer le prix comme ça pourrait entraîner des pertes, et s’il y a de pertes ce n’est plus un prix limite, car **le prix limite ne peut pas entraîner des pertes**.

</aside>

## Limites et crédibilité de ces stratégies

### Limites d’une stratégie de prédation

- S’il n’ya pas de barrières d’entrée, la petite entreprise peut facilement sortir du marché et revenir quand le monopole tente de remonter grandement le prix.
- Problèmes de crédibilité devants les concurrents potentiels : ils ne croient pas que la firme installée puisse entraîner ses grandes pertes juste pour éviter l’entrée d’autres concurrents.
- Le rachat d’une entreprise petite de la part d’autre entreprise qui était dehors le marché et n’a pas donc subi les pertes du prix de prédation, ce qui le rend finalement facile pour sauter les barrieres d’entrées. Ici on n’a pas diminuer la concurrence par un membre, mais remplacé un concurrent par une autre extérieur.
- Une petite entreprise est plus resiliente de ce que la firme installée anticipait et entraîne des grandes pertes qui durent beaucoup dans le temps pour l’entreprise dominante.

### Critique du modèle traditionnel de prix limite

Dans le modèle de prix limite, on suppose que l’entrant va appliquer le stratégie de maximisation de profits $Cm=Rm$, et fixer une quantité et prix qui s’en déduisent. Il pourrait aussi appliquer une autre couple $(p,q)$ avec une autre stratégie, ce qui mérite donc plus d’évaluation.