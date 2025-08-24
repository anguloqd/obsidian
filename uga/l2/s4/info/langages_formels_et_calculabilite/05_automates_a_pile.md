## 05 // automates à pile

[Slides du chapitre 5](ressources/05_automates_a_pile_chapitre_5_compressed.pdf)

## Motivation

### Limitations des automates finis

Ils existent des certains langages que les automates finis ne peuvent pas accepter, en raison de leur manque de mémoire. Ceci signifie qu'ils ne peuvent pas être utilisés pour analyser les langages, tels que les langages de programmation, qui peuvent avoir des structures emboitées sur une profondeur arbitraire.

```java
public class HelloWorld {
	public static void main(String[] args) {
		// Prints "Hello, World" to the terminal window.
		System.out.println("Hello, World"); }
}
```

Etant donnée une séquence de parenthèses ouvrantes (gauches), il n'y a donc aucun moyen de se souvenir de combien ont été observées pour pouvoir les faire correspondre aux parenthèses fermantes (droites).

Pour surmonter les limitations des AEF, il semble opportun de construire une machine avec une forme de mémoire qui permettrait de “se souvenir” des parties de chaîne ou de mot déjà lues. **Voilà la motivation d’ajouter une pile aux automates**.

## Automate à pile

Un automate à pile (AAP) peut être vu comme un automate fini avec l’ajout d’une pile (ou “stack” en anglais) vers laquelle des symboles peuvent être empilés (”pushed”) ou dépilés (”popped”).

![untitled](ressources/05_automates_a_pile_untitled.png)

### La pile et ses symboles

Par rapport à la pile, la machine peut seulement empiler des symboles sur le haut de la pile et les lire à partir du haut de la pile – c.à.d. elle n'a accès à aucune autre partie que le haut de la pile. **C’est comme une boîte de Pringles** : pour atteindre le troisième symbole à partir du haut, les deux symboles du dessus doivent être dépilés d'abord.

Les symboles de la pile forment un ensemble fini de symboles $\Gamma$ qui peut inclure tout l’alphabet de la machine, mais aussi de symboles uniques à la pile qui marchent comme de **marqueurs internes**. Un symbole spécial peut être utilisé pour marquer le fond de la pile (quand il est dépilé, on sait alors que la pile est vide). On adoptera le symbole $\$$.

### Les transitions

Pour les AEF, les transitions dépendent de l’état actuel $q$ et du symbole actuellement lu $s$, et il passe un nouveau état $q^\prime$. Donc, pour les AEF, les transitions sont une fonction comme suit :

$$
\delta:(q, s) \mapsto q^\prime
$$

Pour les AAP, on ajoute une dépendance au symbole placé en haut de la pile $p$ et, **en plus, il empile un nouveau symbole** sur le haut de la pile $p^\prime$. Donc, les transitions d’un AAP sont :

$$
\Delta:(q, r, p) \mapsto (\{q^\prime, p^\prime\}_{{}_{i}})
$$

De la même manière que la tête de lecture ou la bande de lecture est supposée se déplacer après que le symbole courant a été lu, le symbole du haut de la pile est supposé être dépilé après qu’il a été lu.

**Note #1** : sauf cas particulier, les AAP sont supposés non-déterministes.

**Note #2** : dans les AAP, le symbole empilé, le symbole dépilé, et le symbole lu sur la bande, peuvent être $\varepsilon$. Ceci permet à la machine de changer d'état sans lire de symbole ou altérer sa pile.

### Définition mathématique d’un AAP

On peut finalement définir formellement un automate à pile appelé $M$ comme une tuple :

$$
M=\{Q,F \subseteq Q,q_0\in Q, \Sigma,\Gamma,\$\in\Gamma, \Delta\}
$$

- $Q$ : l’ensamble d’états
    - $F \subseteq Q$ : l’ensemble d’états finaux
    - $q_0 \in Q$ : l’état initial de $A$
- $\Sigma$ : l’alphabet (un ensemble de symboles) **du ruban**
- $\Gamma$ : l’alphabet (un ensemble de symboles) **de la pile**
    - $\$ \in \Gamma$ : le symbole initial de la pile
- $\Delta$ : la (multi-)fonction de transition de la forme $\Delta(q, r, p) = (\{q^\prime, p^\prime\}_{{}_{i}})$

## Diagramme de transitions pour les AAP

### Illustrations et transitions

![Exemple de aap.](ressources/05_automates_a_pile_untitled_1.png)

Exemple de AAP.

En différence avec les diagramme de transitions des AEF, les arcs des AAP ont des étiquettes de la forme $(x,y ; z)$, où :

- $x$ est le symbole lu sur la bande de lecture
- $y$ est le symbole dépilé
- $z$ est le symbole empilé

### Transition $\Delta$ en fonction de mots au lieu de symboles

Par rapport à la fonction de transition $\Delta$, on la définir aussi pas en fonction de symboles, mais plutôt en fonction de mots :

$$
\Delta(q, u, \alpha) = (q^\prime, \beta)
$$

- $u \in\Sigma^*$ : le mot sur le ruban, c’est une chaîne de symboles de gauche à droite
- $\alpha\in\Gamma^*$ : le mot sur la pile dépilé, c’est une chaîne de symboles du haut en bas
- $\beta\in\Gamma^*$ : le mot empilé sur la pile qui remplace $\alpha$, de haut en bas

Telle transition se lit comme suit : “si dans l’état $q$, l’automate lit le mot $u$ sur le ruban (de gauche à droite) et si le mot $\alpha$ figure en haut de la pile (de haut en bas), alors l’automate passe dans l’état $q^\prime$ : le mot $u$ a été lu et $\alpha$ est remplacé par $\beta$ en haut de la pile”.

#### Implications et cas particuliers

Avec cette définition de $\Delta$ en fonction de mots, il y a quelques implications à remarquer à ce qui concerne la chaîne vide $\varepsilon$. Reprenons la forme $\Delta(q, u, \alpha) = (q^\prime, \beta)$ :

- Si $\alpha = \varepsilon$ et $\beta \ne \varepsilon$, il s’agit d’une transition permise quel que soit le symbole sur la pile.
Ici, on va juste mettre $\beta$ tout en haut de la pile et **ne rien dépiler**.
- Si $\alpha \ne \varepsilon$ et $\beta = \varepsilon$, on a dépilée la pile une fois (càd. son tout premier élément en haut).
Ici, **on n’a rien empilé**.
- Si $\alpha = \varepsilon$ et $\beta = \varepsilon$, alors la pile est inchangée.
- Si $u = \varepsilon$, le changement d’état et la modification de la pile se font sans mouvement de la tête ou du ruban. **Ceci ne signifie pas qu’on lit une case en blanc !** Une case en blanc n’est pas la même qu’un mot vide, un mot vide ne contient pas de symboles tant que le blanc est lui-même un symbole.

#### Exemple

Voyons la transition (formellement, la correspondance de $\Delta$) suivante :

$$
\Delta(q_1,100,XX) = (q_2,Y)
$$

![Étape 1 : point de depart](ressources/05_automates_a_pile_untitled_2.png)

Étape 1 : point de départ

![Étape 2](ressources/05_automates_a_pile_untitled_3.png)

Étape 2

### Configurations : $(q, u, \sigma)$

Une configuration est juste un triplet de la forme $(q,u, \sigma)$ où $q$ est un état, $u$ est le mot de $\Sigma^*$restant à lire et $\sigma$ est un mot de $\Gamma^*$ contenu dans la pile .

Avec cette forme, on définit une configuration initiale, celle prise par tous les AAP au début :

$$
(q_0, w, \$): \text{où }q_0 \text{ état initial et } \$ \text{ symbole initial de la pile}
$$

De même, on définit une configuration terminale, nécessaire pour que l’AAP puisse s’arrêter :

$$
(q_f, \varepsilon, \beta): \text{où }q_f \text{ état final et } \beta \text{ le reste de la pile}
$$

Un cas particulier de la configuration terminale est $(q, \varepsilon, \varepsilon)$, où l’automate est acceptant du mot et sur une pile vide. Ceci est équivalent à l’$\varepsilon$-transition des AEF.

### Exemple

Supposons un langage $L = \{a^nb^n : n \ge 1\}$. On veut tracer un diagramme de transitions d’un AAP $M$ qui accepte tous les mots de ce langage.

On voit qu’on a une quantité $n$ de $a$, puis la même quantité $n$ de $b$. Une solution est d’empiler $a$ pendant qu’on lit des $a$, puis dépiler $a$ quand on lit des $b$. On note qu’on dépilera la même quantité de $a$ que les $b$ qu’on va lire, donc ceci marche bien. On configure l’AAP ainsi :

$$
\Delta(q,a,\varepsilon)=(q,a)\\
\Delta(q,b,a)=(q,\varepsilon)\\
\Delta(q,\varepsilon, \$)=(q,\varepsilon)
\\
\text{}
\\
\text{C. initiale}: (q,aaabbb,\$)\\
\text{C. finale}: (q, \varepsilon, \varepsilon)
$$

![untitled](ressources/05_automates_a_pile_untitled_4.png)

On voit que la troisième transition sert à “finaliser” l’AAP : **on le dit de juste dépiler $\$$**, sans ne rien lire sur le ruban ni rien ajouter sur la pile. **Intuitivement, si on a dépilé le symbole initial $\$$, on a fini de lire le mot**.

Reprenons un diagramme de ruban et pile pour voir les étapes :

![Étape 1 : point de départ, on lit les $a$. On emploi cette transition trois fois.](ressources/05_automates_a_pile_untitled_5.png)

Étape 1 : point de départ, on lit les $a$. On emploi cette transition trois fois.

![Étape 3 : on a lit tous les $b$, maintenant on finalise la lecture de l’AAP avec la transition finale.](ressources/05_automates_a_pile_untitled_6.png)

Étape 3 : on a lit tous les $b$, maintenant on finalise la lecture de l’AAP avec la transition finale.

![Étape 2 : on a lit tous les $a$, maintenant on lit les $b$. On emploi cette transition trois fois aussi.](ressources/05_automates_a_pile_untitled_7.png)

Étape 2 : on a lit tous les $a$, maintenant on lit les $b$. On emploi cette transition trois fois aussi.

![Étape 4 : ici l’AAP a conclu. **Ceci n’est pas une transition**, c’est juste pour montrer l’AAP eteint.](ressources/05_automates_a_pile_untitled_8.png)

Étape 4 : ici l’AAP a conclu. **Ceci n’est pas une transition**, c’est juste pour montrer l’AAP éteint.

## AAP et langages

### Similitudes entre l’AAP et l’AEF

Tout pareil que l’AEF, l’AAP accepte une chaîne s’il peut lire tout un mot et arrivant à une configuration finale à partir d’une configuration initiale.

Si $M$ est un AAP, on note $L(M)$ le langage accepté par $M$, càd. l’ensemble des chaînes acceptés par $M$. En plus, si les transitions de l’APP données par la fonction $\Delta$ sont toutes de la forme $\Delta(q,u,\varepsilon)=(q^\prime, \varepsilon)$, **$M$ simule un AEF, car elle n’utilise pas la pile !**

Ce dernier fait signifie que tous les langages acceptés par les AEF—les langages réguliers—sont aussi des langages acceptés par les AAP. La réciproque n’est pas vrai : au tout début du chapitre on a mentionné un exemple de langage accepté par un AAP mais pas par un AEF.

#### Exemple

On se donne un $M$ avec les paramètres suivants :

$$
Q=\{q_0,q_1\},\space \Sigma = \{a,b,c\},\space \Gamma =\{A,B\},\space F=\{q_1\}
$$

Et avec une fonction de transition $\Delta$ comme suit :

$$
\Delta(q_0,a,\varepsilon)=(q_0,A), \space
\Delta(q_0,b,\varepsilon)=(q_0,B), \space
\Delta(q_0,c,\varepsilon)=(q_0,\varepsilon)\\
\Delta(q_1,a,A)=(q_1,\varepsilon), \space
\Delta(q_1,b,B)=(q_1,\varepsilon)
$$

Le langage accepté par $M$ est le langage $L(M)=\{wcw^R : w \in \{a,b\}^*\}$, où $w^R$ signifie “l’inverse de $w$”. La définition de $M$ est telle qu’elle enregistre dans la pile le sous-mot $w$ avant d’arriver au symbole $c$, et puis elle le lit à l’inverse en dépilant les symboles accumulés de $w$.

![Celle-ci est la solution finale. La manière d’y arriver est décrite dessous.](ressources/05_automates_a_pile_untitled_9.png)

Celle-ci est la solution finale. La manière d’y arriver est décrite dessous.

### AAP et grammaires hors-contextes

#### Rappel et explication du terme “contexte”

> [!note]
> **Rappel**. Dans une grammaire hors-contexte (GHC), la partie gauche d'une règle de grammaire est un non-terminal et la partie droite peut consister en tout nombre de terminaux ou non-terminaux, dans n'importe quel ordre.

Les GHC sont appelées *hors-contexte* parce que leurs règles de réécriture peuvent être appliquées sans rapport avec le contexte dans lequel elles apparaissent.

Ici, le terme “contexte” signifie les symboles terminaux qui sont autour des symboles non-terminaux. Par exemple, voyons ce deux règles :

$$
A\Rightarrow_1P,\space xAy \Rightarrow_2P
$$

La première règle est une règle hors-contexte puisque $A$ peut être réécrite en $P$ dans n'importe quel contexte. Par contre, la seconde n'est pas hors-contexte puisque $A$ peut seulement être réécrite en $P$ si elle apparaît entre un $x$ et un $y$. **Telles règles sont appelées *sensibles au contexte***.

**Théorème**. Les langages générés par les grammaires hors-contexte sont **exactement** les langages acceptés par les automates à piles.

#### Algorithme : définir les paramètres de l’AAP à partir des ceux de la GHC

Les paramètres d’une grammaire sont $G = \{V_T, V_N, S, R\}$. Donc, pour définir ceux de l’AAP $M$, on les fixe comme suit :

$$
M=\{Q,F \subseteq Q,q_0\in Q, \Sigma,\Gamma,\$\in\Gamma, \Delta\}
$$

- $Q=\{p,q,r\}$
- $\Sigma=V_T$
- $\Gamma=V_N\cup V_T\cup \{\$\}$, où $\$ \notin(V_N\cup V_T)$
- $\$ \in \Gamma$
- $q_0=p$
- $F=\{r\}$
- $\Delta$ sera la fonction de transition dérivé des règles de la grammaire.

#### Algorithme : dériver $\Delta$ de l’AAP à partir de $R$ de la GHC

L’algorithme pour créer un AAP à partir d’une GHC est comme suit :

1. D'abord, il marque le fond de la pile avec $\$$.
2. Ensuite, il empile $S$, le symbole de départ de la grammaire, sur la pile et entre dans l'état $q$.

    $$
    \Delta(p,\varepsilon,\varepsilon) = (q,S)


$$
    
3. Si $\
$$ n’est pas encore revenu sur le dessus de la pile, donc :
    1. Soit l'automate dépile un non-terminal $A$ du haut de la pile et le remplace par la partie droite d'une règle de réécriture (de la forme $A \Rightarrow\varphi$) pour ce non-terminal.
        
        $$
        \Delta(q,\varepsilon,A)=(q,\varphi)
        
$$

    2. Soit l'automate dépile un terminal du haut de la pile pendant qu'il lit le même terminal sur l’entrée.
        
        $$
        \Delta(q,x,x)=(q,\varepsilon)
        

$$
        
4. Quand $\
$$ revient en haut de la pile, l'automate se déplace dans son état d'acceptation/final.
    
    $$
    \Delta(q, \varepsilon,\$)=(r,\varepsilon)
    
$$
