# 02 // automates à états finis

Date de création: February 22, 2023 3:01 PM
Modifié: June 23, 2023 10:35 AM

[Slides du chapitre 2](Chapitre_2.pdf)

# Automates à états finis déterministes (AEFD)

## Définition formelle

Mathématiquement, un automate à états finis déterministe est une tuple de cinq éléments :

- $\Sigma$ : un ensemble fini non vide de symboles
- $Q$ : un ensemble fini **non vide** d’états, qui contient deux sous-éléments importants
    - $F \subseteq Q$ : un sous-ensemble d’*états finaux* (possiblement vide ou égal à $Q$)
    - $q_0 \in Q$ : un élément distingué appelé **état initial,** qui est toujours présent dans $Q$**.
    Note :** l’état initial peut être aussi un état final.
- $\delta : Q \times \Sigma \mapsto Q$ : une fonction de transition **partielle** appelée *fonction de transition*
    - Elle est partielle car son domaine peut bien ne pas contenir toutes les posibles couples d’un symbole de $\Sigma$ et un état de $Q$.

## Définition et propriétés

Dans le domaine de l’informatique théorique, une automate à états finis déterministe représente une machine abstraite. Un AEFD est traditionnellement vu comme une machine à ruban :

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled.png)

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%201.png)

Quelques précisions par rapport à cette machine à ruban spécifique…

- Le ruban est divisé en cases et ilimité à droite
- Il existe une tête de lecture positionnée sur une seule case à la fois
- Chaque case contient soit un seul symbole de $\Sigma$, soit aucun symbole (et donc elle est vide, représenté avec un blanc “ “).
- Au départ, elle se trouve sur l’état initial $q_0$ et la tête de lecture est sur la première case non vide à partir de la gauche. Si toutes les cases du ruban sont vides, la machine départ sur n’importe quelle case.
- Pour passer au prochain symbole, en premier la machine évalue sont état actuel et le symbole actuel ($q_1=\delta(q_0, a)$), puis elle détermine le prochain état et passe au prochain symbole
- Un mot est reconnu ou accepté si et seulement si le mot est entièrement “lu” (tout le mot est entièrement à gauche de la tête de lecture, pas un seul symbole dessous de la tête) et la machine s’arrête dans un état dit final. Dans la dernière image qui suit, on suppose que $q_2$ est l’état final dans l’exemple.

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%202.png)

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%203.png)

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%204.png)

## Transitions, successions et acceptation de mots

Supposons une AEFD avec les propriétés suivantes, où $q_0$ est l’état initial et final. Par exemple, on déduit du tableau que $\delta(q_1,1)=q_2$.

| $\tau$ | $\{0,3,6,9\}$ | $\{1,4,7\}$ | $\{2,5,8\}$ |
| --- | --- | --- | --- |
| $q_0 :$ | $q_0$ | $q_1$ | $q_2$ |
| $q_1 :$ | $q_1$ | $q_2$ | $q_0$ |
| $q_2 :$ | $q_2$ | $q_0$ | $q_1$ |

Notons que si on tente de lire le mot $25170462$, on arrive à l’accepter (surtout, on finit sur un état final).

Notons qu’on peut faire la même chose avec un diagramme de transition. Rigoureusement, un diagramme de transitions pour un AEFD est juste une représentation imagée de la fonction de transition de la machine.

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%205.png)

**Notons qu’un tableau ou diagramme de transition ne nous indique pas le mot ou input à lire, mais seulement les règles pour le lire et s’il pourrait être accepté par l’automate.** Si jamais on a un mot ou input qui est en contradiction avec le diagramme ou tableau, on le rejète.

### Relations de succession

Une configuration courante est la couple $(q,w)$, où $q$ est l’état courant et $w$ est le mot qui reste à lire sur le ruban (comptant le symbole courant sur lequel est la tête de lecture).

Une succession immédiate est une relation entre deux configurations notée “$\rightarrow$”, comme $(q, w) \rightarrow (q\prime, w\prime)$. Elle est vraie si et seulement si $w=x\land w\prime, \space x\in \Sigma$  et $\delta(q,x)=q\prime$. Ici, $\land$ est l’opérateur de concaténation.

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%206.png)

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%207.png)

Une succession est une relation entre deux configurations notée “$\rightarrow^*$”, comme $(q_1, w_1) \rightarrow^* (q_n, w_n)$. Elle est vérifiée si et seulement si $\forall i \in \N : 1 \le i \le n, (q_{i-1},w_{i-1}) \rightarrow (q_i,w_i)$. Intuitivement, si entre la configuration initial et la configuration final ils existent des configurations qui se succèdent immédiatement jusqu’à arriver à la configuration finale.

Dans cette dernière relation, il existe le cas particulier $n=0$ définit à part, où la configuration initiale et finale sont la même, et donc on définit que $(q, w) \rightarrow^* (q,w)$. Cette dernière proposition implique que **la relation de succession (non immédiate) est réflexive** ($aRa$ vrai).

### Définition d’acceptation d’un mot

Avec la définition de succession, on peut formaliser la définition de mot accepté. Un mot est accepté par l’AEFD $A$ si et seulement si $(q_0,w) \rightarrow^* (q_f,\varepsilon), q_f \in F$, où $\varepsilon$ est le caractère vide ou blanc et $q_f$ est un état final.

Encore plus, on peut définit un langage accepté par l’AEFD $A$ à partir d’un alphabet $\Sigma$ si et seulement si tous ses mots sont acceptés par l’AEFD, càd. $L(A, \Sigma) =\{w \in \Sigma^* : w \text{ accepté par } A \}$. 

# Automates et expressions régulières

## Diagrammes de transition

Souvent, on va plutôt travailler avec des regex au lieu de langages réguliers. On peut créer aussi un diagramme de transition avec des expressions régulières comme suit :

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%208.png)

Ce diagramme représente la expression régulière $a(aa^*b)^*b$, càd. les mots qui commencent avec $a$, puis au minimum une occurrence de (la regex qui commence par $a$, puis au minimum une occurrence de $a$, et finit par un $b$), et finit par un $b$. Par exemple :

- $a-aab-b$
- $a-aab-aab-b$
- $a-a(a…a)b-b$
- $a-(a(a…a)b…a(a…a)b)-b$
- etc.

Dans ce cas particulier, il est plus facilement commencer les boucles fermés construits par les états $2$ et $5$, et aussi par $5$ tout seul.

Voyons l’exemple plus simple du langage $\{x \cup y\}^*$, ou aussi l’expression régulière $(x+y)^*$. 

![Untitled](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%209.png)

**Note pratique**. Il est facile à voir que le symbole $+$ peut être lu comme “ou” et la concaténation $\cdot$ comme “et”.

# Automates à états finis non-déterministes (AEFND)

## Différences avec les AEFD

Notons que, dans les diagrammes de transition des AEFD, une transition (correspondance $(q_a,x)\mapsto q_b$) est uniquement déterminée par son état courant $q_0$ et le prochain symbole à lire $x$ (ou aussi le symbole dessous la tête de lecture).

Par contre, pour les AEFND, il peut avoir une situation où on puisse arriver à deux états différents partant du même état et lisant le même symbole. Cela veut dire que la fonction de transition \delta fait une correspondance d’une couple $(q,x)$ à un ensemble de états, et non pas un seul état. Formalisant :

- Cas AEFD : $\delta : Q \times \Sigma \mapsto Q$
- Cas AEFND : $\delta : Q \times \Sigma \mapsto \mathcal{P}(Q)$, où $\mathcal{P}(Q)$ est l’ensemble puissance de $Q$.

<aside>
✏️ Dans ce cours, plutôt que redéfinir $\delta$ comme le fait Wikipedia, on va tout simplement remplacer la fonction de transition avec un ensemble de possibles transitions appelé $R$.

</aside>

Dans la pratique, la plupart du temps une transition dans le cas AEFND nous mène à un seul état, mais faire cette redéfinition de l’image permet de représenter quand une transition peut nous mener à plus d’un état.

## Redéfinitions à partir des AEFD

On remplace la fonction de transition $\delta$ avec un ensemble $R$ appelé une “relation de transition”, qui contient des triplets ordonnés $(q, v, q\prime)$ où $q,q\prime \in Q$ et $v \in \Sigma^*$ et contient toutes les transitions valides et possibles.

- C’est-à-dire, **maintenant on remplace un symbole $x\in\Sigma$ dans le cas AEFD avec un mot $v$.**
- Encore plus, $v$ peut être le caractère vide $\varepsilon$, et dans ce cas la transition est dite “vide”. Ce cas est un cas de ”**indéterminisme**”.
- Un autre cas de indéterminisme est la situation où on a deux possibles transitions à partir d’un état $q$ et un mot $v$. Formellement, ils existent deux triplets dans $R$ $(q,v,q\prime)$ et $(q,v,q\prime\prime)$ tels que $q\prime \ne q\prime\prime$.

La définition de succession immédiate est aussi modifiée. $(q,w)$ est suivi de $(q\prime,w\prime)$ si et seulement si $w = v \land w\prime, \space v \in \Sigma^*$ et $(q,v,q\prime) \in R$, où $\land$ est la concaténation.

**Théorème de déterminisation des automates**. Pour tout AEFND $A$, il existe un AEFD $A^\prime$ tel que $L(A)=L(A^\prime)$. C’est-à-dire, deux automates (l’un déterministe et l’autre non-déterministe) acceptent le même langage.

![Cas non-deterministe.](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%2010.png)

Cas non-deterministe.

![Cas déterministe.](new/uga/l2/s4/info/S4%20info%20langages%20formels%20et%20calculabilité/02%20automates%20à%20états%20finis/Untitled%2011.png)

Cas déterministe.

## Wikipédia : redéfinition de l’acceptation de mots

<aside>
✏️ Je laisse cette redéfinition car je l’ai trouvé utile, même si elle fais pas partie du cours.

</aside>

Un mot ou input $w=x_0x_1…x_n$ est accepté par un AEFND $A$ s’il existe une suite d’états $\{r_i\} \in Q$  qui vérifie les trois conditions suivantes :

1. $r_0 = q_0$
La première condition indique que, pour lire l’input, on doit pouvoir commencer par l’état initial.
2. $r_{i+1} \in \delta(r_i,x_{i+1}), i \in [0,n-1]$
La deuxième condition indique que le prochain état $r_{i+1}$ est **atteignable** à partir de l’état actuel $r_i$ et si on décide de lire le symbole $x_{i+1}$ du mot actuel $w$. 
3. $r_n \in F$
La troisième condition indique que l’état atteint à la fin est un état final.

En vrai, la définition reste la même que le cas AEFD sauf la deuxième condition. Si on se permet d’expliquer pourquoi, voyons la deuxième condition dans les deux cas :

- Cas AEFD : $r_{i+1} = \delta(r_i,x_{i+1}), i \in [0,n-1]$
Dans ce cas, il existe seulement un état atteignable (et effectivement atteint) à partir de $(r_i, x_{i+1})$.
- Cas AEFND : $r_{i+1} \in \delta(r_i,x_{i+1}), i \in [0,n-1]$
Par contre, dans ce cas, l’état $r_{i+1}$ qui est nécessaire d’atteindre pour lire l’input $w$ est juste un élément de l’ensemble d’états atteignables à partir de $(r_i,x_{i+1})$ représenté par $\delta(r_i,x_{i+1})$.