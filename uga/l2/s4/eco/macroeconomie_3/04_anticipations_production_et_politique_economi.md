## 04 // anticipations, production et politique économique

[Slides de IS/LM/PC](ressources/04_anticipations_production_et_politique_economi_chapitre_4b_diapo.pdf)

## Le modèle IS/LM/PC

### Différences avec IS/LM

On voudrait introduire la courbe de Phillips dans le modèle IS/LM, d’où l’ajout de PC. On s’intérésse au passage du court au moyen terme, ce qui permet d’étudier les effets macroéconomique d’un choc ou d’une politique.

L’offre à court terme est donné par l’équation suivant :

$$Y=C(Y-T)+I(Y,r+x)+G$$

La différence avec le traditionnel IS/LM est l’inclusion de la prime de risque $x$ dans l’intérêt $r$ (en fait, c’est plutôt le taux directeur réel). Tel intérêt est donné pas LM horizontale, càd LM est la courbe $r=\bar{r}$, une constante.

### Emploi et production potentiels : $N_n$ et $Y_n$

À la fin du chapitre 1, on avait introduit une forme finale de la relation inflation-chômage :

$$\underbrace{\pi_t-\pi_{t-1}}_{\Delta\pi}=-\alpha(u_t-u_n)$$

> [!note]
> Pour simplicité, on évite de spécifier la période $t$ dans l’’inflation et le chômage à chaque moment. On juste considère la période actuelle $t$ ($\pi$) et une période future quelconque, pas forcément $t+1$ ($\pi^e$). Ceci devient donc :
>
> $$
> \underbrace{\pi-\pi^e}_{\Delta\pi}=-\alpha(u-u_n)
>
$$
On rappelle que $\alpha$ est l’impact du chômage $u$ sur les salaires $W$, ou “l’élasticité-chômage des salaires”, et c’est une relation en sens inverse.

- Si $u > u_n$, la variation de l’inflation $\Delta\pi$ est négative, donc elle baisse en temps $t$.
- Si $u < u_n$, la variation de l’inflation $\Delta\pi$ est positive, donc elle augmente en temps $t$.

$u$ étant le taux de chômage, on peut bien écrire la population de travail total $L$ comme la somme des travailleurs actifs $N$ et de chômeurs $U$ (tout en quantités absolues et non pas des taux), ce qui nous permet de faire les manipulations qui suivent :
$$
u=\frac{U}{L}=\frac{(L-N)}{N}=1-\frac{N}{L} \iff N=L(1-u)
$$
De plus, on dira qu’une unité de travailleurs actifs est égal à une unité de production : $N=L$. Il vient que $Y=L(1-u)$. Ceci est intéressant quand on se trouve sur le taux de chômage naturel ($u=u_n$), d’où on peut tracer deux définitions importantes :

- Emploi structurel, potentiel ou plein emploi : $N_n =L(1-u_n)$
- Production structurel, potentielle ou pleine production : $Y_n=L(1-u_n)$

Avec la deuxième définition, on peut déduire **l’écart de production** : la distance entre la production actuelle avec la production potentielle.
$$
Y-Y_n=L\left((1-u)-(1-u_n)\right)=-L(u-u_n)
$$
Il est évident que, quand on est sur le plein emploi (càd. quand $u=u_n$), l’écart de production est nul. On peut remplacer $(u-u_n)$ avec $-(Y_t-Y_n)/L$ dans la relation emploi-chômage :
$$
\underbrace{\pi-\pi^e}_{\Delta\pi}=\frac{\alpha}{L}(Y-Y_n) \implies \underbrace{\pi-\pi_{t-1}}_{\Delta\pi}=\frac{\alpha}{L}(Y-Y_n), \text{ supposant }{\pi^e=\pi_{t-1}}
$$
D’où on déduit que $\pi_t$ augmente quand $Y > Y_n$. En général, l’inflation a une relation en même sens que la production.

## Dynamique et équilibre de moyen terme

### Taux d’intérêt réel ou neutre : $r_n$

On vient de voir que l’inflation $\pi$ augmente si la production actuelle $Y_t$ est plus grande que la production en plein emploi $Y_n$. Ceci est un effet à court terme.

À moyen terme, les agents réagissent à la hausse de $\pi$. Particulièrement, la Banque Centrale augmente le taux d’intérêt $r$, ce qui diminue la production actuelle. Le point où le taux d’intérêt $r$ a augmenté de sorte que la production actuelle à diminue jusqu’à $Y_t=Y_n$, on appelle ce point le taux d’intérêt naturel ou neutre $r_n$.

## La nouvelle courbe IS

![untitled](ressources/04_anticipations_production_et_politique_economi_untitled.png)

### L’inclusion des anticipations : $A$

On propose une écriture des anticipation tout simplement comme $A=C+I$. Ceci implique que $A$ est une fonction qui prend comme variables indépendantes la production $Y$, les taxes $T$, les taux d’intérêt $r$ et la prime de risque, $x$ (laquelle on suppose constante pour toute les périodes).

Mais, pour que ce soit vraiment des anticipations, on doit aussi prendre en compte les futurs de toutes ces variables. Finalement, la fonction d’anticipation devient ce qui sui :
$$
Y=A(Y,Y^e,T,T^e,r,r^e)+G
$$

Ayant inclus les variables anticipées dans $A$, on ne spécifie jamais une forme fonctionnelle de $A$, on juste va établir des relations en même sens avec $Y,Y^e$ et des relations en sens inverse avec $T,T^e$ et $r,r^e$.

![untitled](ressources/04_anticipations_production_et_politique_economi_untitled_1.png)

On fait remarquer au passage que les anticipations diminuent l’élasticité de $A$ à $r$ actuel :

- Une baisse de $r$ comme dans le graphique modifie peu le VAN des revenus futurs et donc de $W$.
- Pour sa part, $I$ va augmenter peu si la baisse de $r$ est vu comme transitoire.
- Bref, si on a une production $Y$ qui baisse un peu mais qu’on pense que elle augmentera au futur ($Y^e > Y$), donc la consommation $C$ se réduit très peu, car la baisse de $Y$ est vue comme transitoire.

## Politique monétaire et anticipations

### Exemple : économie en crise

Supposons une économie en crise, où la Banque Centrale voudrait baisser $r$. Si les anticipations sont fixes et non accordes à un $r$ diminué, donc l’effet sera pauvre. Par contra, si les anticipations s’ajustent avec la baisse de r, donc la politique monétaire sera effective et $Y\nearrow$. Bref, l’effectivité des politique monétaires dépendront aussi des anticipations accordes.

### Exemple : déficit budgétaire

Supposons une économie ou l’état souhait de réduire son déficit. Quelle que soit la mesure prise contre le déficit ($G\searrow$ ou $T\nearrow$), l’effet sera le même :

- À court terme, baisse de $A$ et donc baisse de $Y$.
- À moyen terme, les capitaux $K$ sont fixes, donc un changement de la productivité viendra seulement d’une augmentation du travail $L$.
    - En plus, les variations des dépenses publiques ne changeront pas $Y$ : si l’état réduit ses dépenses, les ressources produits pour satisfaire la demande de l’état vont se redirectionner au secteur privé, donc la productivité reste la même.
- À long terme, hausse de $I$, donc hausse de $K$ et de $Y$.
- En introduisant les anticipations, alors :
    - Une réduction du déficit implique hausse $Y^e$ et baisse $r^e$
    - **Une baisse de $G$ ne conduit plus forcément à une baisse de $Y$**
