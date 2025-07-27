# 02 // marchés financiers et anticipations

[Slides des anticipations](ressources/02_marches_financiers_et_anticipations_chapitre_2_-_diapo.pdf)

# Valeur Actuelle Nette (VAN)

## Définition

La VAN sur une suite de revenus $Z=(Z_t)_{t=0}^\infin$ est la valeur présente des revenus anticipés d’un investisseur. Elle sert pour déterminer une décision d’investissement.

- Si VAN $>$ Coût initial, donc le projet est rentable.
- Si VAN $<$ Coût initial, donc le projet n’est pas rentable.

Cette statistique doit être construite à l’aide d’informations sur $Z$ et sur le taux de rendement $i=(i_t)_{t=0}^\infin$.

On déduit que $1$ euro au présent vaut $(1+i_0)$ dans une année. Donc, on déduit que $\frac{1}{(1+i_0)}$ euros au présent vaut $1$ euro dans une année. Ceci est une VAN simple, car on considère juste une année. Par contre, on pourrait généraliser à $n$ années ou périodes de temps d’emprunt.

$$
VAN(Z)=Z_0+\frac{Z_1}{1+i_0}+\frac{Z_2}{(1+i_0)(1+i_1)}+\dots \frac{}{}=Z_0+\sum_{p=0}^n\frac{Z_{p+1}}{\prod_{q=0}^p (1+i_q)}
$$

On constate que plus le revenu est lointain, plus le facteur d’actualisation ($\frac{1}{\prod_q (1+i_q)}$) est faible, est donc plus les valeurs actuelle de chaque période devient aussi fables. On conclut que la VAN dépend positivement des revenus courants et anticipés, et négativement des taux d’intérêt présents et futurs.

Cela dit, a partir de la période $1$ et au-delà, on ne connaît vraiment pas ni les revenus ni les taux des rendements. Donc, on doit utiliser de anticipations de $Z_i^e$ et $i_i^e$, $i≥1$.

## VAN d’un revenu réel

On peut tout diviser par P, le prix d’un bien représentatif de l’économie (souvent représentant le niveau de prix), pour obtenir la VAN réelle :

$$
\frac{VAN(Z)}{P} = \frac{1}{P}\left(Z_0+\frac{Z_1^e}{1+i_0}+\frac{Z_2^e}{(1+i_0)(1+i_1^e)}+\dots\right)=
\\
\text{}
\\
z_0+\frac{z_1^e}{1+r_0}+\frac{z_2^e}{(1+r_0)(1+r_1^e)}+\dots
$$

Où les $z_i$ sont les revenus réels et les $r_i$ sont les taux d’intérêt réels.

# Prix des obligations et courbe des taux

## Définition d’obligation et de courbe des taux

### Les obligations (et terminologie)

Les obligations sont une forme d’emprunt, normalement avec une durée de moyen ou long terme. Celui qui emprunt l’argent est *l’emetteur*, et celui qui prête l’argent est *le souscripteur* ou *le créancier*. Au moment de la créer, il est déterminé un montant principal, une date de maturité, un taux d’intérêt (qui engendre un coupon) et une période.

- Le montant principal est la quantité d’argent à être empruntée par l’emetteur du souscripteur.
- La date de maturité est la date où, une fois arrivée, l’emetteur devra repayer le souscripteur le montant principal.
- Le taux d’intérêt est un pourcentage utilisé pour calculer les coupons. Les coupons est tel pourcentage du montant principal. Si le montant principal est 1000 et l’intérêt et 1%, donc le coupon est 10. **Le coupons sont aussi appelés les intérêts** (et non pas les taux d’intérêts, le taux est le pourcentage, l’intérêt tout court est le montant en unités monétaires).
- La période est une durée de temps telle que, à chaque échéance avant de la maturité, l’emetteur payera au souscripteur un coupon. Normalement, **cette période est une année**, donc chaque année l’emetteur paye un coupon au soucripteur.

À la date de maturité, l’emetteur aura rétabli le montant principal au souscripteur et, en plus, tous et chaque coupon de chaque période. On déduit que le rendement ou le profit du souscripteur est la somme des coupons, où simplement coupons multiplié par la quantité de périodes.

Pour les agents financier, les deux caractéristiques d’une obligation sont **le risque de défaut** (probabilité que l’emetteur ne puisse pas payer les coupons ou le principal), et **la maturité** (durée pendant laquelle l’acheteur reçoit des versements ou coupons).

### Les courbes de taux

Une courbe de taux est juste un graphe avec une période (à partir d’aujourd’hui) en abscisse et le taux de rendement pour les obligations en ordonné.

![untitled](new/uga/l2/s4/eco/s4_eco_macroeconomie_3/ressources/02_marches_financiers_et_anticipations_untitled.png)

## VAN comme critère de décision

Face à deux obligations, on peut utiliser la VAN pour décider laquelle vaut plus en temps présent. On prend deux hypothèses :

1. Les deux obligations ont le même rendement.
2. L’investisseur n’est intéressé que par le rendement.
Il ne prend pas en compte les risques encourus.

Prenons deux obligations : $O_1$ à une maturité d’un an qui donne droit à un versement de 100, et $O_2$ qui mature dans deux ans pour le même rendement. $P_1$ et $P_2$ sont leurs prix.

Leur prix à présent sont les valeurs actuelles du rendement. C’est-à-dire :

$$
P_1 = \frac{100}{(1+i_0)}, \space P_2=\frac{100}{(1+i_0)(1+i_1^e)}
$$

<aside>
✏️ Notation : maintenant $P_{A,B}$ est le prix dès temps $A$ à temps $B$, et de même avec le taux d’intérêt $i_{A,B}$. Notons que ce qu’on notait avant $P_1$ et $P_2$ peuvent être réécrits comme $P_{0,1}$ et $P_{0,2}$.

</aside>

Réfléchissons à $P_2$, car on va faire deux investissements en deux périodes. À la fin de la première période, on a la possibilité de vendre l’obligation au lieu d’attendre la maturité. Quel est le prix à ce moment là de l’obligation ? C’est encore le même critère : c’est la valeur “actuelle” (à ce moment-là) du rendement de l’obligation. **On parle d’une estimation**.

$$
P_{1,2}^e = \frac{100}{(1+i_{1,2}^e)}
$$

On note qu’on peut réécrire le prix actuel de $O_2$ en injectant le prix anticipé d’une obligation de temps 1 à temps 2. **La chose à retenir est que le prix est la valeur actuelle d’un prix estimé dans le futur**. Une équation qui lie le $P_{0,B}$ avec $P_{1,B}$ est appelée “**relation d’arbitrage**”. 

$$
P_{0,2} = \frac{100}{(1+i_{0,1})(1+i_{1,2}^e)} = \frac{\frac{100}{(1+i_{1,2}^e)}}{(1+i_{0,1})}=\frac{P_{1,2}^e}{(1+i_{0,1})} \implies \underbrace{(1+i_{0,1})=\frac{P_{1,2}^e}{P_{0,2}}}_\text{vraie relation d'arbitrage}
$$

On voit que le taux d’intérêt dans une année à partir du présent, càd. de t=0 à t_1, sera différent du taux d’intérêt dans une année à partir de l’année prochaine, càd. de t=1 à t=2. On voudrait déduire un taux d’intérêt qui reste le même dans le passage de t=0 à t=1 et puis de t=1 à t=2. Ceci serait le taux d’intérêt noté comme $i_{0,2}$ et formellement s’appelle “**rendement à maturité**”.

$$
\begin{align*} 
\text{On cherche }i_{0,2} :\space &\frac{100}{(1+i_{0,1})(1+i_{1,2}^e)} = \frac{100}{(1+i_{0,2})^2}

\\

\implies& (1+i_{0,1})(1+i_{1,2}^e) = (1+i_{0,2})^2

\\

\implies& i_{0,2} \approx \frac{1}{2}(i_{0,1}+i_{1,2}^e)
\end{align*}
$$

Cette dernière ligne est juste une approximation. Et on généralise cette approximation à $n$ taux d’intérêts comme la moyenne des $n$ taux d’intêret d’un année à la suivante. Cette approximation est en fait un peu plus grande que la vraie valeur.

$$
i_{0,n} \approx \frac{1}{n}\left( \sum_{p=0}^{n-1} i_{p,(p+1)} \right)
$$

## Risque

Notons que $O_1$ n’a aucun risque car, au moment d’investir, on traite déjà avec un seul taux d’intérêt et on ne doit pas faire d’estimations d’autres taux dans le futur. Par contre, investir dans $O_2$ dépend (positivement, directement ou dans le même sens) du prix futur de l’obligation de l’année 1 à l’année 2, qui n’est pas encore défini.

Au cause de ce risque, les investisseurs peuvent demande une “prime de risque”, qui est une valeur qui se ajoute au prix. On la note $x > 0$. Reprenant depuis la relation d’arbitrage :

$$
P_{0,2}=\frac{P_{1,2}^e}{(1+i_{0,1}+x)}=\frac{100}{(1+i_{0,1}+x)(1+i_{1,2}^e)}
$$

On peut reprendre l’approximation précédente pour calculer à nouveau $i_{0,2}$ en tenant en compte ce prime de risque :

$$
i_{0,2} \approx \frac{1}{2}(i_{0,1}+i_{1,2}+x)
$$

Plus la maturité augmente, plus le risque augmente, donc $x$ aussi. L’investisseur ne tient plus seulement compte du rendement.

Idée : est-ce que il existe une prime pour chaque période d’une année à l’autre ? Si oui, il devrait exister aussi plusieurs risques pour plusieurs estimations de prix.

# Marchés financiers et variations des cours des actions

## Définition d’action et détermination de son prix

Une action est une partie du capital d’une entreprise. Elle donne droit à des dividendes, qui sont une partie ou un pourcentage de chaque profit de chaque période. La valeur des actions est donc la VAN des dividendes futurs (ou plutôt de leurs estimations).

Supposons une entreprise qui va avoir un seul profit dans le future, et donc il nous correspondra un seul dividende D. Le prix de l’action est donc la VAN du dividende. considérant une prime de risque.

$$
Q_0=\frac{D_1^e}{(1+i_{0,1}+x)}
$$

On considère maintenant que cette firme va avoir deux profits, donc on obtiendrait deux dividendes de cette action. Le prix actuel de l’action Q serait donc comme suit :

$$
Q_0=\frac{D_1^e}{(1+i_{0,1}+x)}+\frac{D_2^e}{(1+i_{0,1}+x)(1+i_{1,2}^e+x)}
$$

Notons que à la fin de la période 1, le détenteur de l’action peut décider de bien garder l’action ou de la revendre. Pour déterminer le prix de revente de l’action, on fait pareil comme on a fait avec l’obligation : on exprime la VAN du dividende de la période 2 comme si le temps présent était la période 1.

$$
Q_1^e = \frac{D_2^e}{(1+i_{1,2}^e+x)}

\\
\text{}
\\

\implies  \frac{D_2^e}{(1+i_{0,1}+x)(1+i_{1,2}^e+x)}=\frac{\frac{D_2^e}{(1+i_{1,2}^e+x)}}{(1+i_{0,1}+x)}=\frac{Q_1^e}{(1+i_{0,1}+x)}
$$

On peut donc réécrire le cas d’une firme qui reparte deux dividendes, cette fois-ci considérant les estimations des prix futurs de l’action.

$$
Q_0=\frac{D_1^e}{(1+i_{0,1}+x)}+\frac{Q_1^e}{(1+i_{0,1}+x)}
$$

Finalement, on pourrait généraliser ceci à $n$ dividendes obtenus dans le futur, d’où la valeur de l’action devient ce qui suit :

$$
Q_0=\frac{D_1^e}{(1+i_{0,1}+x)}+\frac{Q_1^e}{(1+i_{0,1}+x)}+\dots+\frac{Q_n^e}{(1+i_{0,1}+x)}

\\
\text{}
\\

Q_0=\frac{D_1^e}{(1+i_{0,1}+x)} + \sum_{p=1}^n\frac{Q_p^e}{(1+i_{0,1}+x)}
$$

Le valeur d’une action sont tous les valeurs au présent du prochain dividende et des prochains prix de l’action. On constate que le prix de l’action dépend directement (au même sens) des estimations de dividendes et inversement des taux d’intérêt.

## Effets de hausse des taux sur la bourse et l’activité éco.

Variations des prix des actions/obligations sont imprévisibles, et leur attractivité est déterminée par les anticipations des investisseurs. Anticipation d’une hausse des cours des actions amène à une hausse de celle-ci.

La relation de Phillips dans l’actualité est que, tant que le chômage $u$ se situe par-dessous de la NAIRU $u_n$ (et donc il crée de l’inflation $\pi$), il existe un risque que la FED fasse augmenter les taux d’intérêt. Si les marches financiers sous-estime la réussite du freinage de l’inflation à travers la hausse des taux, le cours des actions va baisser.

## Risque et bulles

Des bulles, ou des effets de modes, peuvent faire d´evier le cours des actions de leur “valeur fondamentale”. Pour de nombreux actifs, il est difficile de calculer une valeur fondamentale et le cours dépend beaucoup des anticipations sur le cours futur.

Dans la réalité, prime de risque $x$ n’est pas constante. Il existe un écart important et variable entre rendement des obligations et celui des actions, appelé ”equity premium”. Dans la réalité, le cours des actifs diffère largement de leur valeur fondamentale.