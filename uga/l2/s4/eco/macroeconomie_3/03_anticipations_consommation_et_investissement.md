## 03 // anticipations, consommation et investissement

[Slides de consommation et investissement](ressources/03_anticipations_consommation_et_investissement_chapitre_3_diapo.pdf)

## La consommation : $C$

### Théorie du consommateur prévoyant

Le consommateur fixe sa consommation comme une partie totale de sa richesse actuelle $W$(patrimoine, actifs+pasifs) mais aussi comme la VAN des revenus futurs. Supposons que, dans l’année ou période $t$, les revenus bruts perçus sont $Y_t$ et les taxes sont $T_t$. On déduit que le revenu net de la période $t$ est $(Y_t-T_t)$.

**Finalement, le “capital humain” $K^H$ est la VAN des revenus nets futurs** : $K^H_t=VAN(Y^e_t-T^e_t)$. On déduit que c’est une fonction des revenus futurs, des impôts futurs et des taux d’intérêt futurs : $K^H_t=K^H_t(Y^e_t,T^e_t,i^e_t)$.

Une première version de ce modèle est de considérer le capital humain dans la richesse, et donc la consommation actuelle dépend seulement de la richesse :  $C=C(W)$. Ceci, par contre, nous donne des résultats exagérés et pas réalistes sur la richesse actuelle de quelqu’un. Pour spécifier, ceci donne une sûreté absolue au 100% des revenus espérés.

Une deuxième version considère que la consommation actuelle dépend de la richesse et aussi du revenu actuelle : $C=C(W,Y_t-T_t)$. Chaque des variables incluent de l’anticipation :

- Pour $W$, les valeurs des actifs et passifs dans le futur sont des estimations.
- Pour le capital humain, il dépend des estimations du revenu futur, des impôts futurs mais aussi de taux d’intérêt futurs. Cette dernière implique que la consommation peut changer même si le revenu reste le même (dans le cas où les taux d’intérêt changent).

## L’investissement : $I$

Si la consommation dépend de la richesse et des revenus nets, l’investissement dépend du taux d’intérêt réel et de la demande courante. Particulièrement, si la VAN d’un projet d’investissement est plus grande que le coût du projet, c’est un projet rentable.

### Estimation de la durée de vie du capital physique

Supposons que l’investissement évalué est une machine, comme une voiture. La plupart des machines peuvent durer virtuellement autant qu’on le souhaite, mais à un coût de plus en plus élevé.

On actualise la valeur de la machine chaque année ou période à travers un taux de dépréciation $\delta$. En période initiale, la valeur d’une machine est x. L’année prochaine, la machine perd $\delta\%$ de son valeur, donc la valeur est $x \times (1-\delta)$. L’année qui suit, la valeur est $x \times (1-\delta)^2$, etc.

### Calcul de la VAN du profit

Tel investissement (capital physique, dans ce cas) génère de profits. Pour la profit de chaque année $t$, on le note $\Pi_t^e$. On parle de profit réels, pas de profits nominaux. On calcule alors la VAN réelle pour chaque profit réel futur :

$$VAN(\Pi_t^e)=\frac{\Pi_{t+1}^e}{(1+r_t)}+(1-\delta)\frac{\Pi_{t+2}^e}{(1+r_t)(1+r_{t+1}^e)}+\dots \\ \text{} \\ =\sum_{t=0}^n (1-\delta)^t \frac{\Pi_{t+1}^e}{\prod_{u=0}^t (1+r_u)}$$

**Doute** : pourquoi on déprécie le profit et non pas les valeurs des machines ?

### Décision d’investissement

On retourne à l’investissement. On déduit qu’elle dépend positivement de la VAN des profits et négativement des taux d’intérêts réels $r_t$ et du prix de l’investissement $P$.

$$I=I\left( VAN(\Pi_t^e), P\right)=VAN(\Pi_t^e)-P$$

Finalement, cela serait l’investissement d’un seul (une seule machine). On pourrait le généraliser à $n$ investissements.

## Profits courants et anticipés

### Leur liens avec l’investissement

Les entreprises peuvent s’attendre à ce que le profit courant prédise généralement bien le profit futur. En fait, l’investissement $I$ est plus affecté par le profits courants que ceux futurs.

![untitled](ressources/03_anticipations_consommation_et_investissement_untitled.png)

Si le profit d’une firme est faible, elle est contrainte à emprunter pour investir, mais l’endettement l’expose à un risque de rentabilité. Si le profit est fort, par contre, ses garanties de repaiement sont plus fortes et ses besoins d’emprunter sont moindres. Si le profit est encore plus forte, la firme pourrait même se financer elle-même.

Le profit dépend finalement des ventes et du stock de capital. On se donne une forme fonctionnelle du profit comme $\Pi_t=\Pi\left(\frac{Y_t}{K_t}\right)$. L’expression à l’intérieur est le revenu par unité de $K$ en période $t$. Le profit dépend donc positivement de la demande $Y_t$ et négativement du capital $K_t$.

On va admettre aussi que $\Pi$ baisse lors des récessions et croît en période d’expansion. Si on s’était dit que les profits futurs dépend des profits courants, et que l’investissement dépends des deux, donc on établit un lien positif entre production courante et investissement.

## Comparaison : consommation et investissement

### Similitudes

**Permanence de variation du pouvoir** : pour les firmes, moins une variation des ventes est considérée comme durable, moins elle influe sur les anticipations de profits et donc sur les décisions d’investissement. C’est analogue pour les consommateurs, leurs variations de revenus et leurs choix de consommation.

### Différences

La théorie du consommateur implique que, devant une hausse de leur revenu qu’ils jugent permanente, les consommateurs réagissent en augmentant leur consommation au plus d’un même montant, et cette augmentation de la consommation présente réduit la consommation future. **L’aumentation de la consommation présente est inférieur ou égale à la var. de revenu**.

Par contre, dans la théorie de l’investissement, **l’augmentation de l’investissement pourrait être même plus grande que l’augmentation des ventes** si elles jugent que ce dernières sont permanentes.

On en déduit que l’investissement $I$ devrait être plus volatile que la consommation $C$. Si bien $C$ et $I$ sont plutôt corrélés, $I$ varie bien plus que $C$.

Cela dit, normalement $C$ représente beaucoup plus du PIB que $I$ (En France, $C$ est $55\%$ du PIB et $I$ et $20\%$), donc l’échelle de variation absolue des deux grandeurs est comparable. $C$ et $I$ contribuent à parts à peu près égales aux fluctuations du PIB.
