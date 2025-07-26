# 03 // firme dominante et barrières à l’entrée

[Slides de firme dominante](corolleur_f._2021_22_lecture_3_firmes_dominantes.pdf)

# Rappels de monopole, cas général

## Le but du monopole : maximisation de profits

Un monopole est une firme telle qu’elle est la seule firme dans un marché. Elle cherche, comme tout agent rationnel, à maximiser ses profits. Ces profits sont décrits par la fonction suivante, où $p(q)$ est la fonction de demande inverse et non pas un prix constante comme donnée (différent du cas de concurrence parfaite !) :

$$
\pi(q)=p(q)\cdot q-CT(q)
$$

L’optimisation se fait trouvant le maximum de la fonction $\pi(q)$, c’est-à-dire, trouvant les $q$ pour lesquels sa première dérivée égal à $0$ et la deuxième dérivée soit négative. Ces sont les conditions de premier et deuxième ordre, respectivement.

$$
q^* = q:\frac{\partial\pi(q)}{\partial q} = 0 \text{ et }\frac{\partial^2\pi(q)}{\partial^2 q}<0
$$

## Comparaison avec la concurrence parfaite

La plupart du temps on se confronte à une demande linéaire de la forme $p(q)=a-bq$ et une fonction de coût total $CT(q)=F+cq$, où $c$ est un coût constant marginal. Si on essai d’appliquer la maximisation de profits à cette demande dans le cas de monopole, on arrive à $q^*_m=\frac{a-c}{2b}$ et $p_m^*=p(q^*_m)=\frac{a+c}{2}$.

D’autre côté, dans la concurrence parfaite où $p^*=c$, il vient que $q^* = \frac{a-c}{b}$. Si on compare, le prix du monopole est plus grand ($\frac{a+c}{2} > c$) et la quantité plus petite ($\frac{a-c}{2b} < \frac{a-c}{b}$).

**Remarque**. Notons que $q^m=\frac{q^c}{2}$.

![aas.png](aas.png)

Note : dans le cas de monopole, le surplus de producteur est égal au profit si et seulement si les coûts fixes sont nuls. Sinon, SP > Profit (le surplus de prod. ignores les coûts fixes).

Avec ce graphe, on peut apprécier que :

- Avec les fonction qu’on à supposé, $SC^m=\frac{SP^m}{2}=DWL$ (dead-weight loss).
- Le surplus total en monopole ($SC^m+SP^m$) est $\frac{3}{4}$ du surplus total en concurrence parfaite ($SC^m+SP^m+DWL$ dans l’image).

## Effet d’une hausse des coûts constants sur le prix de monopole

Pour simplifier, on suppose que la fonction de coûts est $CT(q)=cq$ où $c>0$. En plus, on dira que pour la demande inverse, $p(0)>c$ et $p\prime (q)< 0$, cette dernière condition étant le cas normal. On étudiera l’effets d’une hausse des coûts quand la fonction est concave, linéaire et convexe.

Premièrement, on verra la condition de premier ordre :

$$
\frac{\partial\pi(q)}{\partial q} = 0 \iff p\prime(q)q+p(q)-c=0 \iff \underbrace{p\prime(q)q+p(q)}_\text{Revenu marginal}=\underbrace{c}_\text{Coût marginal}
$$

De la même manière, on calcule la dérivée du revenu marginal :

$$
\frac{\partial Rm(q)}{\partial q}= p\prime\prime(q)q+2p\prime(q)

\\
\text{}
\\

\text{Rappel : } p\prime(q)<0, \text{par supposition}
$$

Ayant dérivé deux fois, on arrive à la fonction $p\prime\prime(q)$, dont le signe déterminera si la demande est concave, convexe où linéaire. Ici, on peut évaluer chaque cas :

- Demande concave $\iff p\prime\prime(q) < 0$ : la dérivé de $Rm$ est négative, donc $Rm$ est décroissant par rapport à $q$. Finalement, une hausse de $c$ sera une baisse de $q$.
- Demande linéaire $\iff p\prime\prime(q) = 0$ : même conclusion.
- Demande convexe $\iff p\prime\prime(q) >0$ : on étudie donc le signe de  $p\prime\prime(q)q+2p\prime(q)$.
    - Si $|p\prime\prime(q)| > |2p\prime(q)|
    
    \implies
    
    \frac{\partial Rm(q)}{\partial q}= p\prime\prime(q)q+2p\prime(q) >0$, ce cas n’est pas compatible avec le fait ou supposition que $Rm$ est en dessous de la courbe de demande (qui est conséquence de $q >0$, $p(q)>0$ et $p\prime(q)<0$).
    - Si $|p\prime\prime(q)| < |2p\prime(q)|
    
    \implies
    
    \frac{\partial Rm(q)}{\partial q}= p\prime\prime(q)q+2p\prime(q) <0$, et donc $Rm$ est décroissante par rapport à $q$. Donc, même conclusion, le monopole réduira les quantités offertes.

## Effets de la concavité de la demande sur les surplus

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled.png)

Sur une demande convexe, l’impact sur la baisse de prix est plus fort. Donc, plus une demande est concave, plus lentement descend le prix par rapport à la quantité offerte (au moins au début de la courbe, car il semble que les deux courbes concaves et convexes, ont un partie élastique (presque horizontale) et un partie inélastique (presque verticale).

Une demande convexe commence étant inélastique puis élastique, et l’inverse pour un demande concave qui commence étant élastique puis inélastique.

Un monopole sera plus récitent à augmenter $q$ pour une demande convexe que pour une demande concave (au moins dans leurs parties inélastique et élastique, respectivement).

<aside>
💡 Note pratique #1 : rappel que élasticité est normalement l’élasticité-prix de la quantité (combien bouge la quantité par rapport au prix). La quantité étant inélastique au prix implique que le prix est élastique à la quantité. De la même manière, quand la quantité est élastique au prix, le prix est inélastique à la quantité.

</aside>

<aside>
💡 Note pratique #2 : le monopole préfère une demande inélastique, les consommateurs préfèrent une demande élastique.

</aside>

En plus, rappelons que $q^m=\frac{q^c}{2}$ et $SC^m=\frac{SP^m}{2}$ dans le cas de demande linéaire. Ceci change pour des demandes concaves et convexes (supposons que la demande concave est par dessous de la demande linéaire et la convexe est par dessus, c’est qui mathématiquement ne devrait pas être toujours le cas, donc on fait cette supposition).

Pour le cas concave (inférieur) :

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_1.png)

- $q^m \ge \frac{q^c}{2}$
- $SP \ge 2SC$

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_2.png)

Pour le cas convexe (supérieur) :

- $q^m \le \frac{q^c}{2}$
- $SP \le 2SC$

## Monopole multi-établissement

Le monopole peut produire **un même bien** (pas deux bien différents !) au sein de plusieurs établissements, chacun avec un coût spécifique pas forcément égaux. Le but serait de répartir la production des produits qui se produisent en établissement $1$ et $2$, $q_1$ et $q_2$ respectivement, de manière que $Rm = Cm_1 = Cm_2$.

Dans ce cas d’exercices, on a une relation directe ou équation qui lie la quantité produit d’un bien et son coût marginal, et aussi le fait que la quantité totale produite est $Q = q_1 + q_2$. Au moment d’exprimer Q par rapport au chaque $Cm_i$, l’”unification” de $Cm_1$ et $Cm_2$ est égale à $Cm_T$. Voyons un exemple :

$$
C_1(q_1)=3q_1^2, C_2(q_2)=q_2^2 \implies \underbrace{Cm_1=6q_1, Cm_2=2q_2}_{\text{relation directe entre } q_i -Cm_i}

\\
\text{}
\\

Cm_1=Cm_2 \implies 6q_1 = 2q_2 \implies 3q_1=q_2 \implies Q = q_1+q_2 = 4q_1

\\\text{}\\

p(Q)=100-Q \implies RT = Q \cdot p(Q) \implies Rm = 100-2Q = 100 - 8q_1

\\\text{}\\

\text{Maximisation : } Rm = Cm_1 \implies 100-8q_1=6q_1 \implies q_1 \approx 7, q_2 = 3q_1 = 21

\\\text{}\\
Q^* = q_1+ q_2 = 29, p^* = 71.
$$

Il y a quelques enseignements à tenir en tête :

- Quand les coûts marginaux sont distincts, le monopole réduit la production de l’établissement aux coûts élevés. Notons que le monopole produit plus dans le établissement 2 car il est moins cher. Dans ce point de production, les coûts marginaux sont égaux.
- La quantité finale d’équilibre est telle où la recette marginale est égale aux deux coûts marginaux, qui sont déjà égaux à eux-mêmes.
- Attention : les coûts de production ici sont non liés ! Ils ne partagent pas une plateforme logistique.

### Fonction de coût de la forme $C_i(q_i) = c_iq_i+d_iq_i^2$

Ici, $c_i$ et $d_i$ sont des constantes et on veut déterminer pour quels $c_i$ le monopole multi-établissement va produire dans un établissement, dans les deux ou aucun.

- On calcule $\partial \pi / \partial q_i$ et on monte un système d’équations comme si c’était de fonctions de réactions de $q_A$ en termes de $q_B$ et vice versa.
- On remplace un $q_i$ dans l’équation de l’autre et on résout, de même pour l’autre $q_j$.
- On pose la condition $q_i > 0$ et on résout pour déterminer $c_A$ en termes des autres termes $f(c_B, d_B)$, de même pour $c_B$ en termes des autres termes $f(c_A, d_A)$.
- On devrait arriver à un graphique de cette forme :
    
    ![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_3.png)
    

La droite bleu est la fonction $c_A = f(c_B, d_B)$ et la droite rouge est la fonction $c_B = f(c_A, d_A)$. Si on est dessous une courbe, on produit la quantité qui correspond au coût representé par cette courbe, i.e. on produit $q_A$ si on est dessous la droite bleu. Si on est dessus, on ne produit pas.

## Monopole naturel et son profit

Rappel de S3 :

- Un monopole est naturel si CM décroissante à long terme.
    - Si tel est le cas, la fonction de coût original (pas CM !) sera sous-additive.
- CM décroissante est une **condition suffisante mais pas nécessaire**. La condition nécessaire est la sous-additivité des coûts, et on peut en avoir même dans la partie croissante de CM.
- Le profit du monopole peut être nul si à l’équilibre RM=CM.
- Le profit peut même être négatif s’il est plus rentable de produire que d’arreter la production. Particulièrement, un $p^*$ qui soit dessous la courbe CM mais supérieur à CVM (qui est le seuil de fermeture).
- Un monopole naturel n’est pas toujours un monopole soutenable. La condition nécessaire d’un monopole soutenable est que le $p^*$ fixé se trouve dans la partie décroissante de CM.

# Extension de monopole à $n$ biens

## Demandes liées, coûts indépendants

Dans ce cas, la fonction de demande prend le prix d’un bien “composé” des autres deux biens : $q(p_C) = a - p_C$, où $p_C = f(p_A,p_B)$, souvent $p_C = p_A + p_B$. En plus, le coûts indépendants se traduisent dans une fonction de la forme $C(q_A,q_B)=c_A(q_A)+c_B(q_B)$.  Le fait de poser $p_C$ comme fonction de $p_A, p_B$ signifie que les prix sont fixés conjointement.

### Cas de biens complémentaires

Pour des biens complémentaires ($\epsilon_{AB} < 0$), fixer les prix séparément conduit à des nivaux de **prix trop élevés** pour maximiser le profit joint. Dit autrement, pour des biens complémentaires, le monopole fixera des prix moindres afin de maximiser son profit.

Dans le cas de fixer les prix séparément pour des compléments :

- On réécrit les prix : $q(p_C)=a-p_C=a-(p_A+p_B) \implies p_A=a-p_B-q_A$
- Avec ce dernière réécriture de $p_A$, on peut déterminer le revenu total, donc le revenu marginal et finalement appliquer la condition de maximisation $Rm_A=Cm_A$, et idem pour $B$.
- On monte un système d’équations de type “fonctions de réactions”, donc on exprime le prix d’un bien comme fonction du prix de l’autre bien. On détermine les prix d’équilibre $p_A^*,p_B^*$, puis on determine $q_{\text{total}}(p_A^*,p_B^*)$ avec sa définition de départ pour finalement calculer le profit.

Dans le cas de fixer les prix conjointement pour des compléments :

- On suppose que $p_A=p_B$ et $p=p_A + p_B$.
- On fait une maximisation de profit normale comme s’il s’agissait d’un bundle d’un seul produit. Puis, pour le prix d’équilibre $p^*$, on pourra facilement déduire les prix individuels.
- **On doit arriver à que le prix moindre et un profit plus élevé que dans le cas précédent**.

### Cas de biens substituts

Pour des biens substituables ($\epsilon_{AB} > 0$), les prix fixes centralement seront d’un niveau supérieur (relativement au cas indépendant) et i**dem pour le profit**. Donc, le monopole voudra fixer les prix centralement dans les deux cas, mais la différence ce que le prix sera plus élevé dans les cas des bien substituts et moindre dans le cas des compléments.

## Demandes indépendants, coûts liés

Prenons une forme fonctionnelle de la demande inverse $p_i(q_i,q_j)=a-bq_i-gq_j$ et une fonction de coût comme $c(q_1,q_2)=\frac{c}{2}(q_1^2+q_2^2)-\beta q_1q_2$, tous coefficients positifs (attention aux signes négatifs, ils sont bien mis !) et $b>g$. Cela implique des économies de gamme.

Ici, $\beta$ est la complémentarité de coût et $g$ est l’effet prix croisé accru. $\beta$ a une relation au même sens que la quantité d’équilibre produite, et $g$ a une relation inverse à la quantité d’équilibre (car ils deviennent plus substituables/homogènes).

## Coûts liés : cas d’économies d’apprentissage

On peut voir les deux produits comme le même produit mais dans deux périodes différentes. Prenons la forme suivante de profit qu’on cherche à maximiser, $\delta$ le facteur d’escompte :

$$
\max_{p_1,p_2} \underbrace{p_1q_q(p_q)-C(q_1(p_q)}_{\pi_1} + \underbrace{\delta\big(p_2q_2(p_2)-c_2(q_1(p_1),q_2(p_2))\big)}_{\pi_2}
$$

Avec un peu d’algèbre, on arrive à déduire que les prix optimaux $p_1^*,p_2^*$ sont tels que $Rm_2 = Cm_2$ et $Rm_1 < Cm_1$. La chose à retenir c’est que $q_1^*$ est plus élevée que dans le cas statique (càd. dans le cas d’une seule période), donc **le profit de court terme est sacrifié**.

# Pouvoir de marché et bien-être

## Taux de marge : pouvoir de monopole

### L’élasticité $\epsilon=\frac{\Delta \%p(q)/p}{\Delta\%q/q}$

La première des manières de mesurer le pouvoir d’une firme est avec l’élasticité de la quantité demandée $\epsilon = \frac{\text{d}p(q)}{\text{d}q}$, qui est négative dans cet écriture précise. 

On peut réécrire aussi le revenu marginale comme $Rm=p(q)\left[1-\frac{1}{|\epsilon|}\right]$ et faire la substitution dans la condition de maximisation $Rm=Cm$, donc $p(q)\left[1-\frac{1}{|\epsilon|}\right] = Cm$.

On voit qu’en concurrence parfaite, la firme n’a aucun pouvoir de marché, donc l’élasticité $\epsilon$ tend vers l’infini et donc on arrive à la définition de concurrence parfaite : $p = Cm$.

Une autre curiosité c’est que, sachant la CPO $Rm=Cm$, un monopole ne fixera jamais $q$ tel que $|\epsilon|<1$ (partie inélastique de la demande), cari sinon $Rm<0$.

À part de l’élasticité, une autre manière de mesurer le pouvoir d’une firme est le taux de marge, défini comme $\mu = \frac{p-Cm}{Cm}$ et encadré entre $0$ et l’infini. Avec un peu d’algèbre, on peut le réécrire aussi comme $\mu=\frac{1}{|\epsilon|-1}$.

Cela dit, on avait mentionné au début du chapitre 1 que la manière préférée de mesurer le pouvoir de marché c’est avec l’indice de Lerner $L=\frac{p-Cm}{p}$, où $L=1$ si on se trouve en monopole et $L=0$ si on se trouve en concurrence parfaite.

## Pouvoir de marché et monopole multi-produits

La marge (mesurée avec l’indice de Lerner) pour des bien indépendants $1$ et $2$ (càd. non substituts ni compléments) est $\frac{p_q-Cm_1}{p_q}=\frac{1}{\epsilon_{11}}$, idem pour bien $2$.

On verra que dans le cas des biens 1 et 2 substituts et compléments, respectivement :

$$
\text{Biens substituts :  }\frac{p_q-Cm_1}{p_q}=\frac{1}{\epsilon_{11}}-\underbrace{\frac{(p_2-Cm_2)\epsilon_{12}q_2}{p_1\epsilon_{11}q_1}}_{\text{terme négatif}}> \frac{1}{\epsilon_{11}}

\\\text{}\\

\text{Biens compléments :  }\frac{p_q-Cm_1}{p_q}=\frac{1}{\epsilon_{11}}-\underbrace{\frac{(p_2-Cm_2)\epsilon_{12}q_2}{p_1\epsilon_{11}q_1}}_{\text{terme positif}} < \frac{1}{\epsilon_{11}}
$$

On conclut que la marge des biens substituts sera plus élevée dans le cas des biens indépendants, et la marge de biens compléments sera moindre que dans le cas de biens indépendants.

## ✔️: Mesurer empiriquement le taux de marge

Le premier problème estimant le taux de marge d’une entreprise c’est que **ses coûts ne sont pas publiquement déclarés**, il est donc impossible de connaître ses coûts marginaux. **On *estime* donc ses coûts marginaux avec ses coûts variables**.

Le problème de $Cm$ c’est que une hausse dans les coûts fixes serait ignoré dans le taux de marge. Si on calcule le taux avec les coûts variables, les taux de marges reflétés sont moindres qu’en les calculant avec les coûts marginaux.

## Coûts sociaux d’un monopole

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_4.png)

Note : au moment de la conception de ces deux concepts de perte sèche, on faisait l’hypothèse *ad hoc* sur l’élasticité de la demande égal à $1$ pour tous les secteurs (il n’était pas accesible de calculer les vraies élasticités à cet époque-là).

En plus, on peut réécrire la DWL à la Harberger pour un Cm constant : $DWL = \frac{1}{2}L_m\epsilon p_mq_m$, où $m$ signifie les prix et quantités en monopole.

# Firme dominante avec frange concurrentielle

## Note : les monopoles au 100% n’existent pas

Les marchés avec une firme représentant 100% du marché sont rares, plus fréquents sont ceux « proches » du monopole (e.g. : 92% Google) ou plus généralement supérieur à 40% (seuil généralement retenu pour repérer une firme dominante, ou susceptible de l’être).

## Hypothèse du modèle

Les hypothèses de ce modèle sont six : H-A-PT-NF-DM-OF

1. Biens homogènes.
2. La firme dominante a une avantage en coût.
3. Toute les autres firmes non-dominantes sont *price-takers* et fixent $p=Cm$.
4. La quantité de firmes dans la frange est soit fixe, soit variable.
5. La firme dominante connaît la courbe de demande de marché $Q_M(p)$.
6. La firme dominante détermine la quantité produite par la frange concurrentielle, donc elle connaît l’offre $Q_F(p)$.

## Particularités du modèle

On peut déduire que la demande résiduelle qui s’addresse à la firme dominante est $q_D=q_M(p)-q_f(p)$, où la première fonction est la demande intégrale du marché et la deuxième est l’offre de la frange. **Elle devra tenir compte de la réponse de la frange à ses prix**.

Notons que toutes **ces fonctions de demande ne sont pas des fonctions de demandes inverses** ! Donc dans ce modèle, on travaillera comme $p$ comme variable indépendante. 

### La fonction de profit change !

La fonction de profit du monopole ou de la firme dominante est donc comme suit :

$$
\pi_D=p\cdot q_D(p)-c(q_D(p))
$$

**Pour optimiser le profit, on applique la CPO mais par rapport au prix, pas par rapport à la quantité !**

$$
\frac{\partial\pi_D}{\partial p}=q_D+p\frac{\partial q_D}{\partial p}-\frac{\partial c}{\partial q_D}\frac{\partial q_D}{\partial p}=0

\iff
q_D+\underbrace{\frac{\partial q_D}{\partial p}}_!\left( p-\frac{\partial c}{\partial q_D}\right)=0

$$

On connaît tous les termes du membre gauche de la deuxième égalité à exception de $\partial q_D/ \partial p$. Pour la determine, on revient à la réécriture de la quantité offerte par la demande et on la dérive partiellement :

$$
\frac{\partial q_D}{\partial p}=\frac{\partial q_M}{\partial p}-\frac{\partial q_F}{\partial p} \implies q_D+\underbrace{\left( \frac{\partial q_M}{\partial p}-\frac{\partial q_F}{\partial p} \right)}_\text{remplace dans CPO}\left( p-\frac{\partial c}{\partial q_D}\right)=0
$$

Finalement là, on peut trouver le $p^*$ optimal, car le monopole connaît la demande de marché $q_M$, la demande adressée à la frange $q_F$ et bien sûr ses propres coûts $c$.

L’un de points importants de ce modèle avec $n$ fixe (les firmes de la frange) c’est qu’une hausse de prix réduit la demande qui lui est adressée au monopole pour deux raisons : la hausse de prix permet à la frange d’accroître son offre (son désavantage en coût est réduit), et la quantité demandée sur le marché diminue en raison de la hausse du prix.

L’autre des points importants : on peut écrire l’indice de Lerner de la firme dominante comme $L^D = \frac{p^*-Cm(Q^*)}{p^*}= \frac{S^D}{S^f\epsilon_S^f +\epsilon}$. On se rend compte que son pouvoir de marché dépend donc de :

- $S^D$ : relation directe, la quantité offerte par la firme dominante i.e. sa part de marché.
- $\epsilon$ : relation inverse, l’elasticité de marché $\%\Delta Q^M/\%\Delta p$
- $\epsilon_S^f$ : relation inverse, l’élasticité-prix de l’offre de la frange $\%\Delta Q^f/\%\Delta p$
- $S^F$ : relation inverse, la part de marché de la frange.
- $Cm$ : relation inverse, son efficacité technologique.

# Concurrence monopolistique

## Hypothèses

La concurrence monopolistique est un modèle reposant sur les hypothèses suivantes :

- Atomicité : nombre important de firmes
- Des produits *différenciés* :
    - Chaque entreprise produit un bien distinct des autres (variétés différentes)
    - Les consommateurs ont des préférences sur ces variétés
    - Chaque entreprise possède alors un pouvoir de marché sur sa niche de marché
- Libre entrée et sortie sur le marché (absence de coûts fixes irrécupérables, etc.)
- Information parfaite.
- Mobilité parfaite des inputs.

## Généralités

On note $F$ les coûts fixes. Plus $F$ est forte, moins il y aura de variétés/firmes, et donc plus la perte sèche est forte.

À court terme, l’équilibre en concurrence monopolistique est similaire à celui d’un monopole ($Rm=Cm$). À long terme, c’est plutôt similaire à celui de la concurrence parfaite ($p=Cm$).

Il y a des caractéristiques générales d’exercices de ce sujet :

- On demande souvent quel est la taille de marché $n^*$ tel que le profit de chaque firme sera nul, appelé aussi la “condition de nullité”.
- La fonction de demande total est donnée comme $q=q_i+\sum_{i\ne j}q_j$, où un fixe une firme $i$.
En plus, à un moment donné (après d’appliquer la CPO) on supposera que toutes les firmes offrent la même quantité, donc la quantité offerte par les autres firmes est $\sum_{i\ne j}q_j=(n-1)q_i$.
- Il n’est pas tout à fait égal à la concurrence monopolistique ! La différence importante est que, si bien $RT=CT \iff RM(q^*)=CM(q^*)$, $p > Cm$ et non $p=Cm$. Le prix est un peu plus grand que celui de l’équilibre concurrentiel, et la quantité est plus petite, il y a de ressources inexploitées.

# Barrières à l’entrée

## Deux définitions

Une barrière à l’entrée est un obstacle empêchant l’entrée de concurrents sur un marché. Une barrière à l’entrée permet d’accroître (de conserver) son pouvoir de marché et donc d’accroître ses profits.

On va se rendre compte de qu’il n’y a pas d’unanimité sur les définitions, d’où la nécessité de préciser celle(s) retenu(es) au moment de l’analyse. Il existent deux principales définitions :

- Bain, 1956 : on compare le profit de la firme installé avant de l’entrée avec le profit de l’entrant après de l’entrée. Donc, $B_B=\pi_I(q_I^*)-\max(\pi_E(q_I^{**}, q_E^{**}), 0)$.
- Stigler, 1968 : on compare les profits des deux quand elles produisent $q_I^*$.
Donc $B_S=\pi_I(q_I^*)-\pi_E(q_I^*)$.

Dans la littérature, on peux classifier les barrières en deux : structurelles et stratégiques.

- Barrières structurelles (exogènes) : avantages naturels dont disposent les firmes installées.
- Barrières stratégiques (endogènes) : barrières érigées par les firmes installées (résultats de stratégies de prévention à l’entrée) .

## Crédibilité de l’engagement

Un engagement est crédible si, à chaque possibilité que la firme installée peut la jouer, il est la décision optimale pour elle de la jouer. En jeux simultanées, on parle d’une stratégie dominante. En jeux séquentiels, on parle d’un équilibre parfait en sous-jeux (EPSJ).

![En jeu simultané, il n’est pas crédible que le joueur 1 va jouer “agressif”.](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_5.png)

En jeu simultané, il n’est pas crédible que le joueur 1 va jouer “agressif”.

![Par contre, en jeu séquentiel où joueur 1 joue en premier, il est crédible qu’il joue agressif (s’il sait bien les profits de l’autre joueur dans chaque situation).](new/uga/l2/s4/eco/s4_eco_microeconomie_3/03_firme_dominante_et_barrieres_a_l’entree/untitled_6.png)

Par contre, en jeu séquentiel où joueur 1 joue en premier, il est crédible qu’il joue agressif (s’il sait bien les profits de l’autre joueur dans chaque situation).

## Dissuader, bloquer ou accommoder l’entrée

Posons deux firmes deux périodes ($t_1$ et $t_2$). où $I$ est la firme installée et $E$ l’entrant potentiel (entrée éventuelle en $t_2$). Pour $I$, on se demande s’il est de l’intérêt de manipuler sa variable stratégique (ex. dépenses R&D, publicité, prix, etc.) en $t_1$ afin de dissuader l’entrée de $E$ en $t_2$.

- La entrée est *bloquée* : la structure de coût et l’avantage de jouer en premier suffit. Donc, il est inutile d’engager en action de dissuasion, $E$ ne voudra pas entrer.
- L’entrée est *accommodée* : le profit de $I$ est supérieur s’il accepte l’entrée que lorsqu’il cherche à dissuader à $E$ avec un engagement/inversion qui serait non crédible.
- L’entrée est *dissuadée* : le profit de $I$ est supérieur s’il fait un engagement pour dissuader à $E$. Tout engagement est crédible.