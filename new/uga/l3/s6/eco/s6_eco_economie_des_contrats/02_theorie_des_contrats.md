# 02 // théorie des contrats

[Partie II Théorie des Contrats 2022.pdf](partie_ii_thorie_des_contrats_2022.pdf)

<aside>
💡 Remarquer pour l’examen finale : utilité de réservation dans la contrainte de participation (par définition, le salaire si je suis au chômage) // Le trois points : “comment vont agir les agents, quantité et prix d’équilibre”. // “rente informationnelle” différence entre w_i en info parfaite et w_i en asymétrie d’info // “exo de partiel final” : la contrainte de participation dépend de la forme de sa fonction d’utilité !!! (son attitude vers le risque)

</aside>

# Introduction

![…](new/uga/l3/s6/eco/s6_eco_economie_des_contrats/02_theorie_des_contrats/untitled.png)

…

# La sélection adverse

## Éléments de base

Si la sélection adverse est présentée comme “opportunisme pré-contractuel”, la définition est l’inobservabilité d'une caractéristique du bien échangé par l'un des agents, ou simplement “asymétrie d’information d’un agent par rapport à l’autre”.

Ceci peut se présenter comme des avantages pour le vendeur (ex. voitures d’occasion) ou pour l’acheteur (ex. le souscripteur d’assurance). On voit donc qu’il y a du risque d'opportunisme précontractuel de la part de l'agent le plus informé.

Ceci provoque deux conséquences :

- Incompatibilité avec le cadre néoclassique du fonctionnement des marchés concurrentiels
- Risque de disparition des marchés ou de rationnement de l'offre de biens

## Exemple

…

## Solutions : signal et filtrage

### Signal (Spence, 1974)

Les agents détenant une information privée, et qui peuvent être handicapés par la sélection adverse, prennent l’initiative d’envoyer un signal ou d’adopter un comportement (mais avec un coût) qui dévoile leur information aux autres parties.

Comme exemples, on trouve les « bons » vendeurs de voitures (en proposant une garantie) ou du signalement de la productivité par les « bons » employés (via leur niveau d’étude). Ils s’autosélectionnent (contrainte d’autosélection).

Encore faut-il que le signal soit efficace, c-à-d qu’il révèle l’information de manière crédible pour les agents non informés, ce qui n’est généralement pas gratuit !

### Filtrage et discrimination (Rothschild & Stiglitz, 1976)

Les agents non informés, et qui peuvent être handicapés par la sélection adverse, amènent les agents informés à faire un choix parmi un ensemble de proposition, afin d’obtenir les informations privés. Il s’agit de discriminer les agents en différentes catégories en fonction de certains critères.

Comme exemple, proposer deux types de contrats d’assurance, un contrat à franchise
élevée et à prime faible (type 1), et un contrat à franchise faible et à prime élevé (type 2). Les souscripteurs du contrat de type 1 préfèrent une prime faible, quitte à accepter une franchise élevée en cas d’accident, ils anticipent donc peu d’accidents et représentent des conducteurs à faible risque. Inversement pour les conducteurs à haut risque qui préfèrent un contrat de type 2.

## Conclusion

Problèmes de sélection adverse : situations d’information incomplète et asymétrique ex-ante (ou pré-contractuel).

Les agents non informés sont toujours défavorisés par les asymétries informationnelles, tandis que les autres bénéficient d’une « rente informationnelle ».

Mécanismes concurrentiels : inefficaces car les équilibres obtenus ne sont plus des optimums de Pareto, mais des optimums de « second rang » (avec gaspillages de ressources).

Possibilités de mécanismes / contrats incitatifs pour contrer les problèmes de sélection adverse mais à un coût non nul.

# L’aléa moral

## Introduction

Les relations principal-agent sont les situations dans lesquelles un individu (l’agent) agit sous la direction d’un autre (le Principal) et est supposé agir conformément aux objectifs du principal.

Cette situation introduit d’asymétries informationnelles : le principal est non informé quant :

- aux actions prises par l’agent (relations principal-agent avec action cachée)
- aux circonstance dans lesquelles les actions prises par l’agent ont été prises (relations principal-agent avec information cachée).

Il y a donc un risque d’opportunisme post-contractuel (intérêt pour tirer au flanc) de la part de l’agent le plus informé : risque moral ou aléa moral pour le principal.

## Le modèle de départ : action observable

Les résultats ou les performances de l’agent peuvent prendre une valeur y, avec y \in [y_1, y_2]. Cette valeur dépend non seulement de l’effort a de l’agent, avec a \in [a_\min, a_\max], mais également d’un facteur aléatoire
 assimilé à un élément dont l’agent n’a pas le contrôle.

La performance aléatoire s’écrit donc : y(a,\theta), avec dy/da > 0, et sa densité de probabilité est conditionnelle au choix de l’effort par l’agent : p(y|a)

Comme hypothèse, le prix de vente du bien fabriqué par l’agent est donné et égal à 1.

Dans ce modèle, on aura la perspective du principal, donc on voudra maximiser l’utilité espérée du principal. Voici les formules :

- L’utilité du principal : V_P(y-w(y)), avec V_P\prime>0 et V_P\prime\prime \le 0. Donc il peut être neutre ou riscophobe.
- L’utilité de l’agent : V_A(w(y)-C(a)), où C est la désutilité liée à l’effort, avec V_A\prime>0 et V_A\prime\prime \le 0; et aussi C\prime>0 et C\prime\prime \le 0.
- L’utilité de réservation de l’agent ou son coût d’opportunité est donnée et égale à U_A.

Le programme du principal devient donc : \max_{w(y), a} E[V_P(w(y), a)] sous la contrainte E[V_A(w(y), a)] \ge U_A.

$$
\begin{cases}
\max_{w(y), a} \int_{y_1}^{y_2} V_P(y-w(y)) p(y|a)dy, \text{sous la contrainte}
\\
\int_{y_1}^{y_2}V_A(w(y))p(y|a)dy-C(a) \ge U_A
\end{cases}
$$

La solution à telle problème (w^*(y), a^*) est obtenue à travers de la fonction lagrangienne : \max_{w(y), a} L[w(y), a]

$$
L = \int_{y_1}^{y_2} V_P(y-w(y)) p(y|a)dy + \lambda[\int_{y_1}^{y_2}V_A(w(y))p(y|a)dy - C(a) - U_A]
$$

Les dérivées de L par rapport à w(y) et a sont, respectivement :

$$
\frac{\partial L}{\partial w(y)} = 0 \iff -V_P^\prime(y-w(y))+\lambda V_A^\prime(w(y))=0
$$

$$
\frac{\partial L}{\partial a} = 0 \iff \int_{y_1}^{y_2} V_P(y-w(y)) \frac{dp(y|a)}{da}dy + \lambda[\int_{y_1}^{y_2}V_A(w(y))\frac{dp(y|a)}{da}dy - C  ^\prime(a)] = 0
$$

Le multiplicateur de Lagrange finit par être $\lambda = V_P^\prime / V_A^\prime$. Si on défini r_i = -V^{\prime\prime}_i / V^\prime_i, on a donc

$$
\frac{dw^*}{dy} = \frac{r_P}{r_P+r_A} \iff w^*(y) = \alpha y + C 
$$

Si l’agent est neutre au risque (r_P=0) et l’agent riscophobe, on a donc w*’(y) = C, dont la valeur de C est donnée par l’optimum de la contrainte de participation :

$$
 C = V_A^{-1}[U_A + C(a^*)]
$$

Finalement, il y a trois assertions à retenir :

- Si le Principal est neutre au risque et l’Agent est riscophobe, ce dernier touche un salaire fixe indépendant de sa performance (y) et dépendant uniquement de son niveau d’effort. Le risque est totalement supporté par le Principal.
- Si les deux sont riscophobes, c’est l’importance relative de leur degré d’aversion au risque qui détermine l’intensité du risque que chacun supporte.
- A noter que l’observation de l’effort ne supprime les conflits d’intérêt entre les deux. Le principal est capable de choisir une politique d’incitation sans faire supporter l’intégralité du risque à l’Agent.
    - Comme il peut observer a*, il,est en droit de le licencier et de lui verser un salaire nul dans le cas où l’action n’est pas a* : « schéma par palier avec menace crédible »

## Modèle avec action cachée

Posons le contexte du modèle :

- Les résultats ou la production de l’Agent peuvent prendre un nombre fini de valeurs : yi , avec yi une variable aléatoire.
- Résultats incertains de l’activité de l’agent, mais vérifiables par le Principal
- Possibilité pour l’Agent de mettre en œuvre deux types d’effort pour arriver aux résultats yi : e_H et e_B, avec e_H > e_B
- Niveaux d’effort impossibles à observer par le Principal

Soient les probabilités p_i^H et p_i^B que la production atteigne la valeur y_i lorsque l’effort est Haut ou Bas. La distribution de la variable Y|e_H domine stochastiquement à Y|e_B.

$$
P(y\le y_i|e_H) = \sum_{k=1}^ip_k^H \le \sum_{k=1}^ip_k^B = P(y\le y_i|e_B)
$$

Il y a toujours trois question à répondre, selon le prof. Llerena :

- Comment les agents vont-ils se comporter ?
- Quels contrats le Principal proposera-t-il à l’Agent ?
- De quels variables dépendra la rémunération de l’Agent ?

<aside>
📌 L’indice i est là parce que on suppose que les résultats de la variable aléatoire y sont dénombrables. Si on suppose que $y\in \{1,5,11\}$, donc il y a trois résultats qu’on indexe avec $i\in\{1,2,3\}$.

</aside>

Hypothèses :

- V(.) est **la fonction d’utilité uniquement pour processer le salaire** de l’agent. On suppose qu’elle est positive et croissante convexe (donc riscophobe).
- Soit V l’utilité de réservation de l’agent.
- Les coûts de l’agent sont C(e_H)=C_H \ge C(e_B)=C_B

La fonction d’utilité de l’agent est donc :

$$
\begin{cases}
U(w,e_i) = v[w(y)]-C(e_i) \text{, s'il accepte le contrat} \\ 
U = V, \text{sinon}
\end{cases}

$$

L’agent, ne connaissant pas le résultat de son activité avant de choisir son effort, maximise son Utilité Espérée.

Le Principal est neutre au risque et son utilité est donnée par son profit : $\Pi(y) = y - w(y)$

À part, il y a deux contraintes à saturer (vérifier) :

- Contrainte d’incitation : pour que l’Agent fournisse l’effort e_H , il faut que le Principal fasse en sorte que l’espérance d’utilité de l’Agent avec e_H soit supérieure à celle qu’il obtiendrait avec le niveau e_B
    
    $$
    \sum_{i=1}^n p_i^H v(w_i) - C_H \ge \sum_{i=1}^n p_i^B v(w_i) - C_B
    $$
    
- Contrainte de participation : encore faut-il que la rémunération proposée par le contrat soit attractif par rapport à l’extérieur, d’où la seconde contrainte :
    
    $$
    \sum_{i=1}^n p_i^H v(w_i) - C_H  \ge V
    $$
    

Compte tenu du schéma de rémunération proposé par le Principal (les w_i), l’Agent doit constater qu’il est avantageux non seulement d’accepter ce contrat mais également de fournir l’effort e_H .

La condition de premier ordre est :

$$
\frac{1}{V^\prime(w_i)} = \lambda + \mu \left[1 - \frac{p_i^B}{p_i^H}\right]
$$

La règle optimale proposée par le Principal est un compromis entre les motifs d’incitation et d’assurance de l’Agent.

Le ratio de vraisemblance précise comment l’observation des résultats devient un signal de l’effort fourni par l’Agent, d’où dans l’équation (1) une rémunération optimale décroissante avec le ratio [p_i^B / p_i^H].

### Et si l’agent était plutôt risque-neutre et non risquephobe ?

S’il est neutre au risque, il ne voudrais plus une “assurance” dans le contrat, ce qui veut dire que la partie fixe n’est plus indispensable pour l’agent. En plus, l’utilité “intermédiaire” du salaire devient $v(w_i) = \alpha w_i = w_i$.

Donc, pour saturer la contrainte de participation :

$$
\sum_{i=1}^np_i^Hv(w_i)-C_H=V \iff \sum_{i=1}^np_i^Hv(w_i) = V + C_H
$$

On calcule l’espérance du profit :

$$
\Pi^* = E[\Pi] = \sum_{i=1}^n p_i^H (y_i-w_i) \\
\text{Puis, notons que de la CP, } \\
\sum_{i=1}^n p_i^H (y_i-w_i) = \sum_{i=1}^n p_i^H y_i - (V + C_H)
$$

Le maximum est atteint quand $w_i = y_i - \Pi^*$.

Dès lors que l’Agent est neutre au risque, le Principal transfère sur celui-ci la totalité du risque (salaire directement lié au résultat), moyennant le paiement d’un montant fixe P*, et cela quel que soit l’état de la nature. L’agent est alors le “bénéficiaire résiduel”.

Il faut dire aussi qu’il fournit l’effort maximum qui maximise le profit du Principal.