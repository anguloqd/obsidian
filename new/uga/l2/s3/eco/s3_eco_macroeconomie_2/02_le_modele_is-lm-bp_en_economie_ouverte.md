# 02 // le modèle is-lm-bp en économie ouverte

# Passage à l’économie ouverte

## Introduction de la courbe BP

Dans une économie ouverte, il faut ajouter une nouvelle condition d’équilibre : l’équilibre de la balance des paiements, qui sera représentée par une courbe BP venant s’ajouter aux courbes IS (marché des biens) et LM (marché monétaire).

Notons que l’équilibre de la balance des paiements signifie qu’il n’y a ni entrées ni sorties nettes de devises et que le marché des changes est donc en équilibre. La courbe BP représente donc simultanément l’équilibre de la balance des paiements et du marché des changes. 

# La construction du modèle

## Incidence de l’ouverture extérieure sur IS et LM

### Incidence sur la courbe IS

La courbe IS représente le marché des biens. Si on considère les exportations et importations, l’équation d’équilibre de offre et demande des produits est :

$$
Y = C + I + G + XN
\newline
Y = (C_0 + cY) + (bi) + G + (X-M)
$$

$X$ et $M$ sont des fonctions d’exportation et importation, respectivement. Leurs définitions, et aussi les définitions de leurs variables, sont les suivantes :

- $e_r$ : “compétitivité”, taux de change réel. $e_r = \frac{P_{RDM}}{P}  e$.
    - $P$ est niveau de prix (reste du monde/local), $e$ est le taux de change nominal.
    - Cette mesure de compétitivité peut-être $> 1$ (si on est relativement compétitifs) ou entre $0$ et $1$ (cas contraire).
- $Y_{RDM}$ : revenu du reste du monde.
- $x_1$ : sensibilité du taux de change réel sur la quantité d’exportations.
- $x_2$ : sensibilité du revenu du reste du monde sur la quantité d’exportations.
- $m_1$ : sensibilité de $e_r$ sur la quantité d’importations.
- $m_2$ : sensibilité de $Y$ sur la quantité d’importations.

$$
X=X(e_t,Y_{RDM})=x_1 e_r + x_2 Y_{RDM}
\newline
M = M(e_t, Y)= m_1 e_r + m_2 Y
$$

Note sur l’équation de $M$ : elle est décroissante par rapport a $e_r$, la compétitivité. Si $e_r \uparrow$, les produits propres sont de meilleure qualité que ceux extérieurs, donc on les garde. Similairement, si $e_r \downarrow$, les produits extérieurs sont plus attractifs, donc on vend les propres pour acquérir les extérieurs.

Finalement, on remplace leurs expressions sur la équation d’équilibre de IS ouverte. Le résultat final serait alors le suivante, rappelant que $s>0$ est proportion marginale à épargner et $b<0$ élasticité-intérêt de l’investissement (négatif).

$$
i = \frac{s+m_2}{b}Y - \frac{1}{b}(C_o +G+x_1e_r+x_2Y_{RDM}-m_1 e_r)
$$

$i$ reste encore une fonction linéaire de $Y$. En comparaison avec la pente $\frac{s}{b}$ en économie ouverte de $Y$. la pente ici est $\frac{s+m_2}{b}$ et elle est encore toujours négative et **plus forte qu’en économie fermée** (en termes de valeurs absolue). L’explication est la suivante :

Comparons le terme $\frac{s_f}{b}Y$ avec $\frac{s_o+m_2}{b}Y$, qui sont les deux égaux à $i$ dans leurs contextes fermée et ouverte. Si $i$ augmente une même chiffre pour les deux cas, et on suppose une même production $Y$,, donc forcément $\frac{s_f}{b} = \frac{s_o + m_2}{b}$, ce qui implique que $s_f > s_o$ si on suppose $m_2 > 0$. Formulé autrement, s’il y a un changement en $i$, $Y$ doit avoir une variation plus grande en économie fermée pour que l’égalité fermée reste vérifié, et moins de variation en économie ouverte car le pente est plus forte.

Finalement, si la compétitivité augmente $e_r$, on augmente les importations et diminue les exportations. (?)

### Incidence sur la courbe LM

Reprenons la définition originale de la courbe LM, où $g>0$ est élasticité-revenu de $O_M$ et $h<0$ est élasticité-intérêt de $O_M$ (**elle est croissante !!!**) :

$$
i = \frac{O_M/P}{h} - \frac{g}{h}Y
$$

Sur la définition de masse monétaire réelle, notons qu’on peut décomposer le terme de masse monétaire $O_M$ comme suit. CINT est le crédit interne, RES sont les réserves de change. 

$$
\frac{O_M}{P} = \frac{CINT+RES}{P}
$$

On introduit un nouveau composant : $BCA$, la balance de capitaux ou compte financier.

$$
BCA = K_\text{entrants} - K_\text{sortants}
$$

Notons que $BCA > 0$ si $K_\text{entrants} > K_\text{sortants}$. C’est à dire, le pays local est attractif pour les placements de capitaux, donc $i > i_{RDM}$. Il est moins attractif si $BCA < 0$.

La prof. n’explicite pas la nouvelle équation pour la droite LM, mais en réalité $BCA$ est inclut comme un terme composant à effet direct dans $O_M$. Donc, $BCA$ a un effet : si $BCA > 0$, donc il existe une variation positive sur la masse monétaire $\Delta^+O_M$ et la droite LM se déplace à droite. Inversement pour $BCA < 0$.

## Construction de la courbe BP

### Construction logique de la courbe

La condition d’équilibre de la balance des paiements est la suivante, où $BTC$ fonction de $Y$ et $BCA$ fonction de $i$.

$$
BP = BTC(Y) + BCA(i) = 0
$$

D’un point de vue d’analyse, on distingue les paiements extérieurs :

- Transactions courantes ($BTC$) : opérations liées à l’échange international de produits. Importations/exportations de produits, revenus de facteurs de production, transferts des agents privés ou des administrations, etc. $BTC$ est en équilibre quand l’importation de produits est la même quantité que ceux reçu par les exportations et revenus.
- Mouvements de capitaux non monétaires ($BCA$) : placements financiers à long terme, investissements directs à l’étranger, placements financiers à court terme du secteur privé non bancaire. On exclut les placements financiers à court terme des banques privés et agents publiques, ils font partie des variations des réserves de change $\Delta RES$.

Eventuellement, $BTC$ et $BCA$ peuvent se compenser. Par exemple, si on exporte trop, on peut utiliser le solde entrant des exportations et les placer à l’étranger.

$BP$ ne doit pas être forcément en équilibre. En effet, on peut avoir $BP > 0$, ce qui signifierait une entrée net de capital. L’inverse est vrai pour $BP > 0$. Pour bien élaborer sur cette conséquence :

- Si $i>i_{RDM}$, on a une entrée nette de capital, donc $\text{Solde} > 0$.
- Si $i<i_{RDM}$, on a une sortie nette de capital, donc $\text{Solde} < 0$.

Cela dit, pour la construction de la droite BP sur le plan $(Y,i)$, on note seulement les couples qui vérifient $BP = BTC + BCA = 0$. Elle est une courbe croissante.

Étudions la prochaine figure. Si on a une augmentation du revenu national $\Delta^+Y$, on augmente les importations $\Delta^+M$. On est en déséquilibre sur le point B. Pour rétablir l’équilibre, il est possible d’emprunter plus des capitaux étrangers, nécessitant une hausse du taux local $i$ par rapport au taux étranger $i_{RDM}$pour devenir plus attractif, ce qui nous mène à C. Finalement, une augmentation de $Y$ a besoin d’une augmentation du taux $i$ pour garder l’équilibre.

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled.png)

### Construction formelle de la courbe

La condition d’équilibre de la courbe BP est $BTC + BCA = 0$. On fait quelque remplacements et on arrive donc à ce qui suit. $ê$ est le taux de change anticipé.

$$
BTC+BCA=0
\newline
(X-M)+BCA=0
\newline
(x_1 e_r+x_2 Y_{RDM})-(m_1 e_r + m_2 Y)+k(i-i_{RDM}+ê)=0
$$

On veut exprimer $i$ en termes de $Y$. Donc, avec de la manipulation algébrique, on arrive finalement à :

$$
i=i_{RDM}-ê+\frac{1}{k}(-x_1 e_r -x_2 Y_{RDM}+m_1 e_r)+\frac{m_2}{k}Y
$$

On se rend compte que la pente de la fonction $i(Y)$ serait $\frac{m_2}{k}$, ce qui est positive, car l’elasticité-revenu des importations $m_2$ est positive, et de même pour l’élasticité-intérêt des entrées nettes de capitaux $k$. Elle est donc croissante.

**Note math.** : élasticité-$x$ de $y$ veut dire “sensibilité de $y$ quand on fait varier $x$”.
L’élasticité-prix de la demande veut dire plutôt l’elasticité-prix de la quantité demandée.
Elle serait effectivement $\frac{\Delta\% Q}{\Delta\% P}$, avec la var. ind. en dénominateur.

## Interprétation et déplacement de la courbe BP

### Interprétation de la pente de BP

La pente de BP ($\frac{m_2}{k}$) et l’effet sur le taux d’intérêt sont d’autant plus forts
que la demande d’importations $M$ est élastique au produit intérieur $Y$ (à travers de $m_2$) et que l’offre de capitaux $BCA$ est inélastique au taux d’intérêt $i$ (à travers de $k$).

À ce moment, il est utile d’appeler $m_2$ comme le coefficient d’ouverture commerciale et $k$ le coefficient d’ouverture financière.

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled_1.png)

Gardant en tête $\frac{m_2}{k}$, pensons à deux cas extrêmes qui sont les deux courbes BP à gauche : quand la pente est 0 et quand la pente est infinie. Mathématiquement, on va juste ajuster à $k$ pour être $0$ ou infinie et représenter ces extrêmes, on laisse $m_2$ constant.

### Absence de mouvements de capitaux : $k \rightarrow 0$

Si la pente est infinie ou BP est parfaitement inélastique, donc aucun changement de $i$ n’aura un effet sur $Y$. Plus spécifiquement, le taux d’intérêt $i$ sont sans effet sur l’équilibre extérieur et BP est une droite verticale qui represente simplement la balance de transactions courantes ($BP = BTC$). Il n’y a pas une connexion entre les marchés financiers nationaux.

### Parfaite mobilité des capitaux : $k \rightarrow \infin$

Si la pente est $0$ ou parfaitement élastique, tous les capitaux réagissent de manière infiniment grande à une variation du taux d’intérêt. Le taux d’intérêt est complètement indépendante de l’équilibre interne et du revenu national. Si on voit l’équation de $i$, elle devient $i = i_{RDM} - ê$. Le taux d’intérêt est simplement égal au taux d’intérêt international corrigé par la dépréciation ou l’appréciation éventuellement anticipée de la monnaie nationale.

Ce taux est un quantité fixe $i^*$ dont il est impossible de s’écarter : si on a un taux plus grand, tous les capitaux viendront au pays car il est plus attractif ; et si on a un taux plus petit, tous les capitaux vont fuir car ce n’est plus rentable. 

### Interprétation de la position de BP

Les variables qui pourrait réalistiquement être forcés à changer sont le revenu étranger $Y_{RDM}$. le taux de change réel $e_r = \frac{eP_{RDM}}{P}$ ($e$ taux de change nominal), taux de change étranger $i_{RDM}$ et taux de change anticipé $ê$.

**Note math.** : rappel que la courbe BP est une courbe croissante et non décroissante. Donc, si on le voit comme $y=ax+b$ avec $a>0$, $b$ aura des impacts en sens direct sur $i$ et des impacts en sens inverse avec la position de BP, i.e. allant à droite ou gauche).

- $Y_{RDM}$ : Relation inverse avec pos. de BP. Si l’étranger a plus de revenu, ils vont augmenter leurs importations, augmentant aussi nos importations. Puisque l’étranger aura moins d’argent pour faire leurs transactions, il faudra augmenter notre taux d’intérêt $i$ pour les convaincre d’investir dans notre pays.
- $e_r$ : Relation directe droite avec pos. de BP si et seulement si l’élasticite-taux des importations $m_1$ est plus petite que l’élasticité-taux des exportations $x_1$. Dans le livre, il semble que $e_r$ effectivement a la même variation avec $i$, ce qui implique que $x_1 > m_1$. Une augmentation de notre compétitivité augmente nos exportations (nettes), et donc on a plus d’argent, ce qui descend notre taux d’intérêt.
- $i_{RDM}$ : Relation inverse avec pos. de BP, car une augmentation de $i_{RDM}$ nous rend moins attractif aux investissements et, pour garder l’équilibre de BP, on est forcés à réduire BTC forcément à travers notre production $Y$ pour tout $i$ inchangé, ou vu de la manière contraire, $i$ augmente relatif à la production pour nous maintenir compétitifs et attractifs aux capitaux.
- $ê$ : Relation directe avec pos. de BP, car si on anticipe que notre monnaie sera plus demandé au futur que celle extérieur (ou si la raison de prix augmente à notre faveur compétitif) donc on pourra se permettre de descendre proportionnellement notre taux d’intérêt $i$.

Chaque fois on veut évaluer l’effet d’un changement de ces facteurs sur BP, **il faut absolument toujours retourner à l’équation $BTC+BCA=0$** et partir de là pour déterminer les effets.

# Dilemmes de politique économique

## La contradiction entre équilibre interne et équilibre externe

### Les différents cas de figure dans le modèle IS-LM-BP

Rappels : $BTC = X-M= (x_1 e_r+x_2 Y_{RDM})-(m_1 e_r + m_2 Y)$ et “l’équilibre extérieur” signifie $BP = BTC + BCA = 0$. L’équilibre de BTC sera donc $X=M$.

À partir d’ici, on aura une préférence pour parler de $BTC$ au lieu de $BP$, car la balance de paiements est trompeuse. Pour donne une courte explication, elle cache l’endettement extérieur, ce qui n’est pas le cas avec $BTC$. **L’objectif d’équilibre externe est donc souvent formulé en termes de balance des transactions courantes**.

Les dilemmes dont on parlera seront ces situations où on doit prioriser soit les objectifs internes (augmenter $Y$ jusqu’à plein-emploi, même si on n’a pas un équilibre de $BTC$) soit les objectifs externes (diminuer $Y$ jusqu’à l’équilibre de $BTC$, même si on n’a pas un équilibre dans le marché de biens).  

Le schéma pour expliquer la suite est le suivante. $Y_{pe}$ serait le niveau maximum de production possible. On va tracer des droites verticaux $Y_{BTC}$ qui montre le niveau où $BTC$ est en équilibre.

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled_2.png)

### Le dilemme d’un pays structurellement déficitaire

Structurellement déficitaire signifie simplement qu’on importe plus de ce qu’on exporte. On voit que les importations propres dépendent du revenu national (voir éq. de $BTC$), et le problème c’est que notre propension d’importation $m_1$ est tellement forte qu’on ne peut pas augmenter $Y$ sans augmenter fortement aussi $M$.

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled_3.png)

Si on produit plus de le niveau de $Y$ qui assure l’équilibre de $BTC$ ($X=M$), on devient déficitaires. On devient excédentaires si on est à gauche de la droite $BTC$.

Dans les zones 1 et 3 les décisions à prendre sont claires : soit on réduit le sous-emploi et l’excedent au même temps, ou l’inflation et le déficit au même temps. En zone 2, il n’y a pas exactement une réponse correcte, car ils existent d’avantages et désavantages de faire augmenter ou diminuer $Y$. Celui-ci est le **dilemme sous-emploi-déficit**.

### Le dilemme d’un pays structurellement excédentaire

Similairement, un pays structurellement excédentaire est celui qui exporte plus de ce qu’il importe.

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled_4.png)

À nouveau, les zones 1 et 3 ne présentent pas de dilemmes, seulement la zone 2. Celui-ci est le **dilemme inflation-excédent**.

Il y a des raisons pour que le déficit se développe plutôt dans les pays qui luttent en priorité contre le chômage (étant struct. déficitaires), et que l’excédent apparaissent dans les pays qui s’attaquent en priorité à l’inflation (étant struct. excédentaires) : les premiers tolèrent plus d’inflation et stimulent davantage l’activité que les seconds; la compétitivité-prix est donc moindre et la demande d’importations plus forte chez les premiers que chez les seconds; les premiers ont tendance au déficit, et les seconds à l’excédent.

## L’arbitrage délicat entre changes fixes et changes flexibles

### La fixité de change, responsables des dilemmes

Pas expliqué dans le cours.

### La solution apparente aux dilemmes : les changes flexibles

[(Lire la page 153 !) Jacques Généreux - Économie politique - Tome 1.pdf](jacques_gnreux_-_conomie_politique_-_tome_1_-_conomie_descriptive_et_comptabilit_nationale.pdf)

Si la balance de paiements est déficitaire, il en résulte une demande nette de devises étrangères (celle qu’on veut avoir pour arriver à l’équilibre) qui fait monter le taux de change $e_r$ (dépréciation de notre monnaie). Le taux de change $e_r$ montera jusqu’à ce que le déficit (la demande excédentaire de devises) ait disparu, et ça arrivera à travers la stimulation des exportations grâce a nos bas prix. C’est analogue si BP est excédentaire.

Par contre, on trouve une période du temps où on a un déficit sans augmentation des exportations, ou l’analogue pour l’excédent. Cela arrive simplement parce que les importations et exportations ne sont pas parfaitement élastiques au taux de change $e_r$, et le pays extérieur prend du temps pour se rendre compte que nos prix sont plus attractif et il dégage en importation de nos produits.

### Conditions de Marshall-Lerner

Avant, on notait $(X - M)$ comme le montant en monnaie des exportations nettes. On va redéfinir la notation : $P_X$ comme le niveau de prix des exportations qu’on effectue, $P_M$ comme le niveau de prix des importations, et $X$ et $M$ seront simplement le volume ou quantité de exportations et importations, respectivement.

Donc, $P_X \times X$ sont nos recettes à l’exportation et $P_M \times M$ sont les dépenses à l’importation.

Retournant à l’analyse, pour diminuer le déficit extérieur de BP, il faudrait que les recettes augmentent plus que les dépenses, càd. le rapport $\frac{XP_X}{MP_M}$ augmente. Or, si on subit une dévaluation de notre monnaie, cela implique que $P_X$ diminue. Donc, il faudrait que $X$ augmente relatif à $M$ et plus vite que ce que descend $\frac{P_X}{P_M}$.

Ici, on peut énoncer les premiers des conditions, **appelé le théorème des élasticités critiques** : si la balance des transactions courantes est initialement en équilibre, elle retourne vers l’équilibre à la suite d’une dévaluation $\Delta^+ e_r$ (ou d’une dépréciation) si la somme en valeur absolue des élasticités-prix des exportations et des importations est supérieure à 1.

$$
e_X + e_M > 1, \text{ avec } e_X = \frac{\frac{\Delta X}{X}}{\frac{\Delta P_X}{P_X}} \text{ et } e_M = \frac{\frac{\Delta M}{M}}{\frac{\Delta P_M}{P_M}}
$$

Cela dit, on peut explorer le cas aussi ou la $BTC$ n’est pas initialement en équilibre mais en déficit. Dans ce cas, la somme des élasticités doit être plus importante, dans une proportion qui dépend du déficit initial.

$$
e_X+e_M>1+e_M \left( \frac{M-X}{X} \right)
$$

### La courbe en J

C’est juste un représentation graphique qui met en évidence l’effet des inélasticités imparfaites des nos importations, et qu’**il prend du temps pour que le reste du monde se rende compte de la compétitivité acquise de nos produits** suite à une dévaluation de nos prix.  

![untitled](new/uga/l2/s3/eco/s3_eco_macroeconomie_2/02_le_modele_is-lm-bp_en_economie_ouverte/untitled_5.png)