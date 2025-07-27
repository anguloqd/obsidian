# 04 // discrimination prix en monopole

[Slides de discrimination prix](ressources/04_discrimination_prix_en_monopole_corolleur_f._2020_21_lecture_4_discrimination_prix.pdf)

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled.png)

# Tarification non linéaire

## Définition et types

La tarification linéaire est un même prix pour tout le monde, donc cette tarification n’est pas discriminante. Les tarifications non linéaire sont donc celles discriminantes, et elles se divisent en trois types :

- **Discrimination de 1er degré** : prix personnalisés, épuisant le consentement à payer des individus qui sont connus par la firme (bref, la firme connaît la courbe de demande et les prix de reserves des consommateurs)
- **Discrimination de 2ème degré** : le consentement à payer est une information privée, connue de l’agent, la firme propose des menus de prix pour le conduire à le révéler
- **Discrimination de 3er degré** : la firme dispose d’une variable observable, corrélée avec le consentement à payer, dont elle se sert pour discriminer

Dans le cas d’un monopole multi-produits, il peut proposer des différents prix selon les paniers de bien proposés, comme des offres groupées (*bundles* de produits) ou les ventes liées.

## Conditions (pour *toutes* les discriminations !)

Les conditions nécessaires pour que la firme puisse exercer une telle tarification sont comme suit : 

- La firme dispose d’un pouvoir de marché.
- **Les préférences des consommateurs doivent être hétérogènes** (la demande est non constante, les consommateurs ont des différents prix de reserve) et la firme a la capacité de les apprécier, au moins plus ou moins.
- Comme détail technique, **la revente doit être impossible entre segments** (sinon ceux qui payent le moins revendront aux autres).

## Différenciation et discrimination

La discrimination n’a pas besoin de la différenciation. En effet, une firme peut discriminer toujours en offrant le même produit. Par contre, c’est vrai aussi que la différenciation de produits est un moyen de renforcer la discrimination :

- Les demandeurs vont révéler leur type et classification par rapport aux produits différenciés
- Au même temps, la revente est naturellement limitée, car les produits ne sont vraiment pas les mêmes.

# Discrimination du 1er degré

## Modèles typiques

Dans la pratique, ce discrimination inclut de la différenciation. Il existe deux modèles ici : 

1. Les modèles plus simple utilisent deux produits : produit 1 et produit 2, chacun ayant sa courbe de demande propre.
2. Un autre type de modèle est un seul bien à deux prix différents : $p_1$ et $p_2$. La quantité du bien vendu à $p_1$ serait $q_1$ et de même avec $q_2$, d’où $q=q_1+q_2$. Bref, $p_1$ serait le prix constante pour les personnes “riches” et $p_2$ pour les personnes “moins riches”.
    1. Parfois, cette stratégie de discrimination est meilleure pour le profit de la firme mais aussi pour le surplus de consommateur (et moins de perte sèche) que dans le cas où la firme applique bêtement la stratégie $q$ tel que $Rm=Cm$. 
        
        ![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_1.png)
        

# Discrimination du 3ème degré

## La présence de deux marchés

Cette discrimination existe pour les établissement mono-produit mais aussi pour les multi-produits. Dans le deux cas, il y a segmentation.

- **Mono-produit** : un seul bien est vendu sur deux marchés différents, donc deux demandes différentes et deux stratégies de prix différentes à appliquer, d’où la *discrimination*.
- **Multi-établissement** : deux bien sont localisés, l’un au segment 1 au l’autre au segment 2.

## Modèle de coûts constants : $Cm = \bar{c}$

La logique : puisque le coûts sont constants, la firme décide à quel segment $i\in\{1,2\}$ vendre par rapport aux revenus marginaux $Rm$, qui dépendent des demandes de chaque segment.

Si on applique le programme d’optimisation de profit pour chaque quantité de produit dirigé à un segment (dans ce cas, $q_1$ et $q_2$), on obtient la conclusion qui suit :

$$
\pi=p_1(q_1)q_1+p_2(q_2)q_2-c(q_1+q_2) \\
\text{}
\\\implies  \frac{\partial\pi}{\partial q_1}=\frac{\partial p_1(q_1)q_1}{\partial q_1}-\frac{\partial c(q_1+q_2)}{\partial q_1}=0 \iff Rm_1=Cm
\\
\text{}
\\\implies  \frac{\partial\pi}{\partial q_2}=\frac{\partial p_2(q_2)q_2}{\partial q_2}-\frac{\partial c(q_1+q_2)}{\partial q_2}=0 \iff Rm_2=Cm
\\
\text{}
\\
\implies Rm_1=Rm_2
$$

Et, en général, pour $n$ segments/produits, leurs $Rm$ sont tous égaux et égaux aussi à $Cm$ :

$$
Rm_i=Rm_{i\ne j}\hspace{12pt}\text{ et }\hspace{12pt}Rm_i=Cm_i
$$

## Modèle de coûts non constants

La commodité du modèle à coûts constants était qu’on pouvait déduire les $q_i^*$ de chaque produit par lui-même, càd. sans besoin de considérer les coûts des autres produits. Ici, ce ne plus possible. **On est forcés à résoudre un système d’équations en $q_i$ et $q_j$** pour déterminer les quantités optimales. Par exemple :

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_2.png)

Ici, la fonction de coût marginale n’est plus $Q=q_i+q_j$ mais $2Q=2(q_1+q_2)$, d’où $C(Q)=Q^2=(q_i+q_j)^2$ (absence de coûts fixes), et on sait que la fonction quadratique n’est pas linéaire, donc on ne peut pas traiter les cas de chaque quantité séparément.

## La demande coudée : $p^{D_{1+2}}$

Pour les deux segments de marché, normalement il y a un qui est disposé à payer plus que l’autre en général. Disons que $D_1$ est le segment disposer à payer plus cher, et $D_2$ moins cher. Un exemple de ceci se voit comme suit :

$$
p^{D_1} = \underbrace{100}_{a_1} - q\hspace{12pt}\text{ et }\hspace{12pt}p^{D_2} = \underbrace{20}_{a_2} - q
$$

On peut déduire que le client de $D_1$ qui a le plus grand prix de réserve est celui avec $100$ (le coefficient libre), et $20$ pour le plus grand prix de réserve de $D_2$. La firme donc confronte une dilemme : soit elle choisit le prix optimal pour le marché plus riche $D_1$, ou un prix pour le deux marchés $D_1$ et $D_2$.

Une partie importante de ce modèle est déduire qu’est-ce que serait la courbe de demande des deux marchés. Pour cela, on écrit les courbes de demande dans la forme non inverse, on les additionne comme suit :

$$
\left.
\begin{array}{r}
q^{D_1}=100-p \\
q^{D_2}=20-p
\end{array}
\right\} \implies q^{\Sigma}=120-2p \implies p^{\Sigma}=60-\frac{1}{2}q
$$

$p^\Sigma$ n’est pas vraiment une courbe de demande, on verra à quoi elle sert après. Si on graphique les trois demandes, on obtient ce qui suit :

![](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_3.png)

La courbe rouge est $p^{D_1}$, la bleue est $p^{D_2}$ et la verte est $p^\Sigma$. 
[https://www.desmos.com/calculator/a17orpj16q](https://www.desmos.com/calculator/a17orpj16q)

Voyons : si le prix est entre $[20,100]$, le seule marché qui voudra acheter est $D_1$ (donc la courbe rouge entre $p=100$ et $p=20$). Par contre, si le prix est inférieur à $20$, les deux marchés participeront (donc, la courbe verte entre $p=20$ jusqu’à $p=0$). On en déduit que la courbe de demande pour les deux marchés est donc comme suit :

$$
p^{D_{1+2}}=
\begin{cases}
p^{D_1},  \text{ si }p\in[20,100]
\\
p^\Sigma, \text{ si }p < 20
\end{cases}
$$

La courbe qui en résulte est une courbe défini par morceaux, d’où l’utilité de calculer $p^\Sigma$. Cette type de demande s’appelle “demande coudée”, car l’intersection en $p=20$ ressemble un coude.

Il faudra voir quelle profit est le plus grand : si le profit de servit le marché le plus riche $\pi_1$ ou le profit de servir les deux marchés $\pi_{1+2}$. Il n’existe pas une réponse standard, il faut passer par les deux situations.

**Note pratique**. une firme en train de optimiser pour servir le marché $1$ (le plus riche) peut arriver à un prix où elle peut servir (et elle sert effectivement !) les deux marchés.

## Apparition de l’élasticité $\epsilon=-\frac{\partial q}{\partial p} \cdot \frac{p}{q}$

On peut faire apparaître l’élasticité pour tracer de conclusions intéressantes dans l’optimisation du profit par rapport à chaque quantité. À nouveau, supposant des coûts constants :

$$
\pi=p_1(q_1)q_1+p_2(q_2)q_2-\underbrace{(cq_1+cq_2)}_{c(q_1+q_2)}
\\
\text{}
\\
\frac{\partial\pi}{\partial q_i}=0 \implies \frac{\partial p_i(q_i)}{\partial q_i}q_i+p_i(q_i)-c=0\implies p_i(q_i)\left(1-\frac{1}{\epsilon_i}\right)=c
$$

Pour maintenir la dernière égalité la plus à droite, si $\epsilon_i \nearrow$, donc $p_i \searrow$ et inversement.
**Le segment le plus sensible au prix bénéficie d’un prix moindre**.

# Discrimination du 2ème degré

## La différence subtile avec la discrimination de 1er degré

Voyons la différence avec la discrimination du 1er degré pour mieux comprendre :

- **Discrimination de première degré** : permet de prix personnalisés—càd. c’est la firme qui peut signaler qui veut quoi, et prend l’initiative d’offre ses produits.
- **Discrimination de deuxième degré** : ne permet pas de prix personnalisés—càd. la firme va plutôt offrir à tout le marché et laisser que les consommateurs choisissent leur menu, à la place d’aller directement au consommateur à l’imposer une offre.

## Modèle de menu de prix dépendant de la qualité

On suppose un marché de taille $n$, laquelle se divise en deux segments : les types “supérieurs” et les types “inférieurs”. Les supérieurs valorisent plus la qualité du produit que les inférieurs. 

On note la quantité de supérieurs comme $\lambda$ et les inférieurs comme $(n-\lambda)$. Il est évident que la somme des deux groupe conforme la taille de marché $n$.

On suppose aussi deux produits qu’on va offrir à tout le marché, où un produit est de meilleure qualité que l’autre, et donc plus cher. L’objectif est que les supérieurs achètent le produit *pro* et que les inférieurs achètent le produit *basique*. Chaque groupe a un prix de reserve constant pour chacun des produits.

![](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_4.png)

Dans cet exemple, la firme vend deux version d’un logiciel : version pro et version basique. Le marché est de taille $120$, avec $\lambda$ chercheurs et $(120-\lambda)$ d’autres consommateurs.
Ici sont leurs prix de reserve pour chaque version.

Dans ce modèle, on cherche des prix pour les deux versions du bien qui satisfassent deux contraintes. On note $p$ le prix fixé par la firme et $r(S,I)$ le prix de reserve des supérieurs pour le produit inférieur :

- **Contrainte de participation** : $p_\text{Inf} ≤ r(I,I)$.
Les inférieurs doivent participer en achetant le produit basique.
- **Contrainte d’auto-selection** : $p_\text{Sup}-p_\text{Inf} ≤ r(S,S)-r(S,I)$.
Les supérieurs vont basculer ou “se sélectionner eux-mêmes” du produit basique au produit pro si la différence de prix entre le deux est *couverte/tolérée* (ou plus petite) que la différence de leurs reserves entre les deux produits. Sinon, il reste avec le produit basique.

Comme autre hypothèse du modèle, les supérieurs vont payer plus cher que les inférieurs pour les deux produits.

### Solution

Souvent, on déduit les meilleurs prix par essai et erreur. On commence pour trouve  un $p_\text{Inf}$ qui satisfasse la contrainte de participation, puis un $p_\text{Sup}$ pour la contrainte d’auto-selection.

1. On découvre, avec essai et erreur fixant $p_\text{Inf}$, que $r(I,I)=2$. Donc, on fixe $p_\text{Inf}=2$.
2. On découvre, avec essai et erreur fixant les deux prix, que $r(S,I)=5$ et $r(S,S)=9$. Donc, $p_\text{Sup} - 2 ≤ 9-5 \iff p_\text{Sup} ≤ 6$. On fixe $p_\text{Sup}=6$.

Normalement, cette discrimination rapporte moins de profits que la discrimination de 1er degré, **mais parfois il peut en rapporter plus si comparé avec le prix uniforme !** Basiquement, ça dépend de $\lambda$, la quantité de consommateurs sup. dans le marché. 

**Note** : la stratégie du prix uniforme qui appliquerait la firme serait de **ne vendre que le produit pro**, supposant qu’il en connaît ses reserves : ils vend $\max(r(S,S)\cdot \lambda, r(I,S) \cdot n)$, càd. il vendra celui qui le rapporte le plus de profit soit vendant seulement aux supérieurs à leurs prix de reserves, soit vendant à tout le monde aux prix de reserves des inférieurs.

## Enseignements du modèle

Les enseignements du modèle sont comme suit :

1. Les prix sont choisis afin de s’approprier l’intégralité du surplus des consommateurs valorisant le moins la qualité. Ceux valorisant le plus la qualité bénéficient d’un surplus positif (rente informationnelle).
2. Le menu de prix est optimal si :
    1. Si la proportion de types valorisant le plus la qualité est ni trop petite ni trop forte,
    2. Si passer d’une qualité basse à forte augmente proportionnellement plus le surplus des types valorisant le plus qualité que ceux le valorisant le moins.
3. Le menu de prix accroît le *welfare* si vendre la basse qualité conduit à une expansion du marché, dans le cas contraire le menu de prix détériore le *welfare*.

# Tarification binôme

## Modèle $T(q) = A+pq$

La tarification binôme est la vente d’un seul produit qui comprend deux parties : une partie fixe et une partie variable. Aller à une soirée *peut être vu* comme un produit à deux parties : le coût de l’entrée elle-même étant la partie fixe, et les boissons consommés après étant la partie variable.

Le produit intégral a comme prix intégral $T(q) = A+pq$, où $A$ est le prix de la partie fixe, et $p$ le prix de chaque unité variable et $q$ la quantité des unités variables. La firme cherche à fixer le prix de $T$ pour chaque client tel qu’il soit égal à son prix de reserve (discrimination parfaite).

Supposons en premier le typique modèle de monopole, où la firme fixe le prix de chaque unité (variable) qui correspond à la quantité telle que $Rm=Cm$. On sait qu’il y à un surplus de consommateurs pour les consommateurs qui en achètent. Maintenant, la firme veut fixer une partie fixe f, différente pour chaque consommateur, pour accaparer leur surplus. 

Pour le profit, on écrirait donc $\pi = \sum_i^n T(q_i) - C(\sum_i^n q_i)$. 

## Exemple

Pour la fonction de coûts, supposons $C(q) = F + cq$, donc $Cm=c$, une constante. On va considérer la fonction de demande de chaque individu (pas des consommateurs agrégés !) comme $p=V-q$.

1. En premier temps, on va fixer le prix de l’unité variable p appliquant le critère d’optimisation classique $Rm=Cm$. 
2. Une fois on a les $p^*$ et $q^*$ de ce consommateur, on regarde son surplus. Pour un prix fixe optimal $A$, on fixe $A = SC$.

Suivant ce méthode, la tarification binôme a comme résultat que $p^*=\frac{V+c}{2}, q^*=\frac{V-c}{2}$ et $SC=\frac{(V-c)^2}{8}$. La tarification binôme finale serait $T^*=\frac{(V-c)^2}{8}+\frac{V^2-c^2}{4}$.

Par contre, on pourrait fixer aussi $p=Cm$ (comme si c’était concurrence parfaite) et puis accaparer le surplus de consommateur. Pour ce résultat, $p=Cm=c, q=V-c, SC=\frac{(V-c)^2}{2}$, d’où la tarification binôme finale serait $T^*=\frac{V^2-c^2}{2}$.

Si on compare les deux solutions, il convient mieux de fixer $p=Cm$ quand $V>c$, c’est-à-dire toujours !

# Discrimination prix multi-produits

## Vocabulaire

Supposons qu’on a deux bien $A$ et $B$. Selon la manière dont on vend les deux bien, on peut définir la vente comme suit :

- $A$ et $B$ : biens indépendantes
- $(A+B)$ : *bundling* pur, pas possible d’acheter l’un sans l’autre
- $A, B, (A+B)$ : *bundling* mixte. 
Possible d’acheter individuellement et groupellement.
$(A+B)$ est moins cher que d’acheter individuellement $A$ et $B$
- $A, (A+B)$ : liaison ou *tying*, où B le bien lié et A le bien liant
Possible d’acheter $A$ sans $B$, mais pas $B$ sans $A$.
- $B, (A+B)$ : liaison ou *tying*, où A le bien lié et B le bien liant
Possible d’acheter $B$ sans $A$, mais pas $A$ sans $B$.

## Vente en package : biens en proportions fixes

### Modèle de Stigler

Supposons deux consommateurs, $A$ et $B$, et deux produits offerts par une firme, un logiciel tableur genre Excel et un logiciel de traitement de texte genre Word.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_5.png)

Supposons un cas initial où la firme juste offre les deux logiciels individuellement. Le plus grand prix qu’il pourrait fixer pour chaque logiciel est le prix de reserve minimum entre les consommateurs $A$ et $B$. Donc, le logiciel tableur sera vendu à un prix de $\$70$ et le logiciel de texte à $\$25$. Pour l’achat des deux (individuellement), le prix sera donc $\$95$.

Supposons maintenant un deuxième cas où on considère un package des deux logiciels. Si jamais un tel package est vendu, les client voudront que le prix du package soit moindre ou égale que la somme des prix individuels. Notons que si on fixe le prix du package à $\$100$, le profit de la firme serait plus grand que le prix en cas 1 càd. $\$95$.

La limitation de ce modèle est qu’on considère pas les coûts de production et qu’on considère pas le cas de seulement vendre les biens en package, sans possibilité d’acheter individuellement.

### Modèle d’Adams et Yellen

Ici, on considère de coûts marginaux constants $c_1$ et $c_2$, et encore deux types de consommateurs $X$ et $Y$, chacun avec un prix de réservation constants pour chacun des deux biens vendus.

### Aucun *bundling* : $A$ et $B$, mais pas $(A+B)$

Le prochain graphique a $p_1$ comme abscisses et $p_2$ comme ordonnées. Pour le moment, on ne tient pas en compte les coûts.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_6.png)

### *Bundling* pur : $(A+B)$, mais pas $A$ ou $B$ individuellement

Si jamais la firme offre un package des deux biens, il est clair que son prix doit être $p_B<p_1+p_2$. La différence dans ce modèle par rapport au précédent ce que les consommateurs n’ont pas un prix de réservation pour un package (*bundle*), ils juste décident d’en acheter si les réservations individuelles sont moindre que le prix du *bundle* : $r_1+r_2<p_B$.

Pour le prochain graphique, on trace une fonction linéaire : $p_B = p_1 + p_2$, où on fixe $p_B$ comme une constante et $p_1$ et $p_2$ comme des variables $x$ et $y$ resp.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_7.png)

On construit la droite $p_B = p_1 + p_2$. Tous les points en dessous sont des clients dont leurs reserves ne leur mènent pas à acheter le *bundle*. Tous les points sur la courbe sont des clients intérésés par le *bundle*. Par contre, la firme ne peuvent pas vendre ni a $G$ ni a $H$, car leur reserves pour le prix du bien 2 et bien 1, resp., sont moindre que leurs coûts de fabrication, donc il ne vaut pas la peine de vendre aux client dans ces régions.

### *Bundling* mixte : $A$, $B$ et $(A+B)$

On prend un autre graphique pareil à celui d’avant, mais on ignore les coûts et on ajoute quelques autres aires. Pour le point x sur le graphique, il s’agit d’un consommateur dont ses réservations sont $p_1<r_1$ et $r_2<p_2$, donc il achète du bien 1 sans bien 2. C’est analogue pour le consommateur du point $y$. Le consommateur du point $z$ achète les deux biens.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_8.png)

En particulier, le consommateur du point z achète le bundle parce qu’il se trouve dans l’aire jaune du graphique ci-dessous, mais pas forcément quand on est sur la droite de p_B on achète le bundle ! Regardons l’aire jaune sombre, où un client qui y soit aura des reserves moindres que les prix, mais proche aux prix quand-même.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_9.png)

On sait déjà qu’un consommateur va toujours acheter un *bundle* si $r_1 < p_1$ et $r_2 < p_2$. Il peut aussi acheter le bundle si l’une des réservations (disons $r_2$) est plus petite que le prix d’un des biens, par exemple $r_2 < p_2$, donc le consommateur n’achète pas individuellement le produit 2.

La condition pour qu’il achète le *bundle* sur le produit qui l’intéresse individuellement est que le surplus du consommateur pour le *bundle* soit plus grande que d’acheter le bien 1, normalement quand le prix $p_2$ est proche de la différence du bundle avec $p_2$ (finalement, $p_2$ est assez proche de $r_2$, meme si par dessus).

### Enseignements

- Le *bundling* mixte est généralement meilleur que celui pur.
- Les ventes avec un bundle sont plus importantes que pour une tarification de monopole simple (linéaire), **mais les chiffres d’affaites n’est pas le profit !**
- L’impact d’un *bundle* sur le profit dépend :
    - Des coûts supportés pour la production des biens : le bundling fonctionne bien
    dans le cas où $Cm$ est proche de $0$.
    - De la distribution des préférences des consommateurs : il est d’autant plus intéressant que les préférences sont hétérogènes.

### Exemple de cours de Pepall et al.

Supposons un monopole qui vend bien 1 et bien 2, dont leurs coûts $Cm_1=100$ et $Cm_2=150$, et quatre type de consommateurs :

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_10.png)

- Si le monopole applique tarification linéaire (bien 1 et bien 2 indépendants, pas de *bundling*) utilisant le critère d’optimisations de profit, $Cm=Rm$, les prix optimaux seront $p_1^*=250$ et $p_2^*=450$, et son profit sera de $\pi_L=\$750$.
- S’il applique un *bundling* pur (bien 1 et bien 2, mais pas indépendents), le meilleur prix à vendre sera $p_B=\$500$ pour que tout le monde en achète. Le profit serait $\pi_P=\$1000$, supérieur à celui en tarification linéaire.
- S’il applique un *bundling* mixte (bien 1, bien 2 et bien 1 et 2), on reprend les prix déterminés dans le cas de tarification linéaire, $p_1^*=250$ et $p_2^*=450$ (**mais pas forcément !**) et le prix du bundle on le fixe à $p_B=\$500$.  On évalue le surplus de chaque consommateur pour savoir qu’est-ce qu’ils choisirait, le surplus étant la différence entre le prix effectif et la reserve du consommateur :
    - $A$ : le surplus est $\$0$ soit achetant seulement le bien 2, soit achetant le *bundle*
    - $B$ : achète le *bundle* (surplus de $\$25$) sur le bien 1 (surplus de $\$0$)
    - $C$ : achète le bien 1 (surplus de $\$50$) sur le *bundle* (surplus de $\$20$)
    - $D$ : achète le bien 1 (surplus de $\$200$) sur le *bundle* (surplus de $\$0$)
    - Le profit de la firme est $\pi_M = \$800$ ou $\$850$, dépendant si $A$ achète le bien 2 ou le *bundle*. En tout cas, supérieur au *bundle* pur.
    
    Finalement, on a repris les prix de tarification linéaire pour la tarification de *bundling* mixte, **mais ceci n’est pas forcément l’optimal**. Si la firme fixe $p_1=\$450$, $p_2=\$450$ et $p_B=\$520$, on peut calculer que le profit final est $\pi_{M^*}=\$1190$. On a absorbé les surplus des tous les consommateurs à exception de $B$, qui garde $\$5$ en surplus. 
    

### Conclusions

- Le *bundling* mixte est toujours au moins aussi profitable que le *bundle* pur, mais il faut parfois ne pas y recourir.
- Certains consommateurs achètent le bundle mais ont des $r_i<Cm_i$ pour chaque produit $i$. La firme préférerait qu’ils n’achètent pas le bien $i$.
- Le bundle est profitable pour de fortes variations des préférences, **il ne l’est plus pour des $Cm$ croissants** (accroître les ventes coûte de plus en plus cher). Effectivement, dans chaque exemple, on avait fixé des coûts marginaux constants.

## Vente liées : bien lié et bien liant

Les ventes où un bien est lié à l’autre est une bonne stratégie quand les biens sont complémentaires. Telles ventes facilitent la discrimination en prix en révélant la préférence des consommateurs.

Voyons avec exemple avec des imprimantes et des cartouches. En premier temps, l’imprimante est loué par un monopole, et le cartouche est vendu sur le marché concurrentiel ($p_c=Cm=\$2$). On suppose deux types de consommateurs :

- Les universités, dont la demande de cartouches est $p_U(q)=16-q$
- Les collèges, dont la demande de cartouches est $p_C(q)=12-q$

La première stratégie consiste à trouver le prix optimal des cartouches, (déjà calculé à $\$2$), puis fixer le prix de l’imprimante au surplus de consommateurs. Puisqu’on suppose qu’on ne peut pas discriminer, on le fixe au surplus le plus petit. On verra dans le graphique ci-dessous que le surplus le plus petit est celui du collège : $\$50$. Donc, on fixe $p_i^*=\$50$.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_11.png)

Maintenant, supposons que la firme veut ne plus vendre l’imprimante seule mais en la liant au cartouche, en plus de vendre les cartouches tous seuls. Évidemment, la firme veut que le prix de l’imprimante qui compose le *bundle* soit inférieur que le prix de la vendre individuellement, donc moins de $\$50$.

Si la firme veut toujours fixer le prix du *bundle* au surplus le plus petit, donc il faudra faire remonter le prix des cartouches par rapport au prix de cartouches individuels dans le marché concurrentiel. On suppose que la firme fixe le nouveau prix des cartouches **individuels** à $p_{c}^{**} = \$4$. Ceci a l’effet de réduire le surplus des collèges à $\$32$ et celui des universités à $\$72$.

![untitled](new/uga/l2/s4/eco/s4_eco_microeconomie_3/ressources/04_discrimination_prix_en_monopole_untitled_12.png)

À l’équilibre, les universités veulent acheter $12$ cartouches pour $\$48$ et les collèges veulent $8$ cartouches pour $\$32$. Le but d’offrir le *bundle* est que le consommateurs préfèrent de l’achéter plutôt que d’acheter les cartouches tous seuls. Donc, on veut trouver le prix $p_c^B$ qui mène au consommateur d’acheter le bundle $(\$32, p_c^B)$.

<aside>
💡 Pourquoi on prend la l’aire du rectangle encadré entre $p_c^*=\$2$ et $p_c^{**}=\$4$ ? Si on remarque dans la réponse en bas, on va offrir $q_c^{**}$ dans le *bundle* mais au prix de marché concurrentiel, $p_c^*=\$2$, et non pas le nouveau prix $p_c^{**}=\$4$. En plus, dans ce cas, on peut discriminer par rapport au prix des cartouches dans le bundle (ce qui n’est pas possible avec le prix de l’imprimante).

</aside>

Si on offre aux universités le bundle d’une imprimante à prix $\$32$ avec $12$ cartouches pour $\$24$ en tout, le *bundle* aux universités en total couterait $\$56$. On respecte aussi que le cartouche dans le bundle est moins cher que le cartouche tout seule, car $\$24$ pour $12$ cartouches est moins que $\$48$ pour la même quantité de cartouches mais achetés individuellement.

On fait de même avec les collèges, et on les offre un bundle d’une imprimante à $\$32$ avec $8$ cartouches à $\$16$, le total du *bundle* aux collèges étant finalement de $\$48$.

On constate que le profit tiré des collèges est moindre qu’avec la premier stratégie ($\$48<\$50$), mais celui tiré des universités est plus grand ($\$56>\$50$). Finalement, pour chaque paire de consommateur auxquels on vend, le profit sera supérieur avec la deuxième stratégie, car $\$48+\$56 > \$50 + \$50$.