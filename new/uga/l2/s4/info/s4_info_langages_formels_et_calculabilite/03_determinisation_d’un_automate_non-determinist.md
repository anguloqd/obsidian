# 03 // déterminisation d’un automate non-déterministe (AEFND)

[Slides du chapitre 3](ressources/03_determinisation_d’un_automate_non-determinist_chapitre_3_compressed.pdf)

# Relation entre les AEFD et AEFND

## Leur différences

Dans le cas AEFD, la transition d’un état est donnée par une fonction mathématique, qui prend un couple état-symbole et retourne **un et un seul état**. Dans la définition formelle de fonction, les éléments du domaine ont chacun *une seule image*.

Dans les diagrammes de transitions pour les automates déterministes, cette condition de “une seule image” est reflétée par l’absences d’arcs multiples partant d’un même état et étiquetés par le même symbole.

Si on relâche le contrainte d’une seule image par couple état-symbole, on obtient une multi-fonction. Dans un diagramme de transitions, cela signifie qu'il peut y avoir plusieurs arcs avec le même symbole partant d'un même état.

![Notons que, dans l’état $1$, la couple état-symbole $(1,a)$ peut correspondre à $1$ mais aussi à $2$. De même pour $(1,b)$, qui correspond à $1$ ou $3$. Cette machine est donc non-déterministe (aefnd).](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled.png)

Notons que, dans l’état $1$, la couple état-symbole $(1,a)$ peut correspondre à $1$ mais aussi à $2$. De même pour $(1,b)$, qui correspond à $1$ ou $3$. Cette machine est donc non-déterministe (AEFND).

On dit qu’un mot est accepté par un AEFND s’il existe un chemin possible pour que la machine arrive dans un état accepté. Toute tentative de traduire directement un AEFND par un programme sur un ordinateur demande d’implémenter un mécanisme de retour en arrière (*backtracking* en anglais). Particulièrement, chaque fois qu’on choisit un arc ou chemin, on se rappelle de ce choix et on y revient si les symboles qui suivent ne permettent pas d’accepter le mot input.

## L’équivalence

Il est visible qu’un AEFND permet de représenter des procédures complexes de reconnaissance de chaîne avec moins d'états que ce qu’un AEFD nécessiterait. Cela dit, **tout langage accepté par un AEFND est aussi accepté par un AEFD, car ces langages sont des *langages réguliers*.** 

Donc, un AEFND n’est pas plus puissant qu’un AEFD, même si un AEFD a besoin généralement de plus d’états pour pouvoir accepter le même langage.

# Construire un AEFD à partir d’un AEFND

## Déterminisation

L’algorithme de déterminisation pour construire un AEFD à partir d’un AEFND est par construction de sous-ensembles. 

![untitled](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_1.png)

![untitled](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_2.png)

1. On commence de l’état de départ de AEFND. Ce serait aussi l’état initial de l’AEFD.
2. Quand on arrive a une bifurcation (correspondance multiple d’un couple état-symbole vers un état) $\delta(1,a)= 2$ ou $3$, et donc $\delta^\prime(1,a)=\{2,3\}$. On regroupe tous les états d’arrivée dans un nouveau état qui représente cet ensemble d’états. Formellement,
    
    $$
    \delta^\prime(\{q_0,\dots,q_n\},a)= \bigcup_{i=0}^n \delta({q_i},a)
    $$
    
3. Après, pour répliquer les arcs qui sort de chaque état qui compose le nouveau état, pour chaque symbole possible, on se demande s’il existe une connexion entre ce symbole et chaque état composant. C’est-à-dire, dans le cas d’avant, $\delta^\prime(\{2,3\},a)$ n’existe pas ni pour $2$ ni $3$, donc il n’y a pas un arc de symbole $a$, mais il y en a pour $b$ car $\delta(2,b)=4$ et $\delta(3,b)=5$. On regroupe à nouveau tous ces états dans le nouveau état $\{4,5\}$.
4. On refait le même processus et on voit qu’on replique la branche d’états $(2,4)$ et la branche d’états $(3,5,6)$.
5. On fixe comme états finaux les nouveaux états qui sont composés seulement d’états finaux.

Bref, dans un AEFND, quand on a une situation de correspondance multiple d’un couple état-symbole à un état, on regroupe tous les états d’arrivée dans un nouveau état qui représente cet ensemble d’états.

[](https://cours.univ-grenoble-alpes.fr/pluginfile.php/1594921/mod_resource/content/2/Chapitre_3.pdf)

## $\varepsilon$-fermeture

La $\varepsilon$-fermeture est un ensemble lié à un état : c’est l’ensemble d’états atteignables à partir de l’état $q$ par une suite quelconque de transitions vides, **même 0 transitions (càd. on reste dans le même état $q$)**. On le note $E(q)$.

On considère une suite de transitions $\varepsilon$ une seule transition jusqu’à que on ne peut plus enchaîner avec une autre transition $\varepsilon$ mais avec un caractère propre.

![Ici, l’ensemble $E(1)$ est $\{12346\}$.](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_3.png)

Ici, l’ensemble $E(1)$ est $\{1,2,3,4,6\}$.

Il est utile de calculer les $\varepsilon$-fermeture de chaque état avant d’appliquer l’algorithme de déterminisation pour composer un AEFD à partir de AEFND.

![AEFND du langage $(a+b)c^*$.](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_4.png)

AEFND du langage $(a+b)c^*$.

![AEFD correspondant.](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_5.png)

AEFD correspondant.

# L’algorithme de construction de sous-ensembles

## Fonctions nécessaires

Avant de le présenter formellement, on va définir deux fonctions :

- Fonction $\varepsilon$-fermeture : prend un état en entrée et retourne l'ensemble des états atteignables à partir de cet état, à partir d’une ou plusieurs $\varepsilon$ transitions.
- Fonction déplacement :  prend un état et un caractère, et retourne l'ensemble des états atteignables par une transition sur ce caractère.

## L’algorithme

Avec cela présenté, on peut formaliser l’algorithme :

1. Créer l'état de départ de l’AEFD en prenant la $\varepsilon$-fermeture de l'état de départ du AEFND.
2. Pour tout nouvel nouvel état AEFD on prend tous et chaque symbole d’entrée possible :
    1. Appliquer *déplacer* à l'état nouvellement créé et au symbole d’entrée ; cela retournera un ensemble d'états.
    2. Appliquer la $*\varepsilon$-fermeture* à cet ensemble d'états, potentiellement résultant en un nouvel ensemble.
3. Cet ensemble d'états AEFND sera un seul état dans l’AEFD.
4. Chaque fois que nous générons un nouvel état AEFD, nous devons lui appliquer l'étape 2.
5. Le processus est complet lorsque l'application de l'étape 2 ne génère plus de nouvel état.
6. Les états de fin du AEFD sont ceux qui contiennent au moins un état de fin du AEFND.

# Minimisation des AEFD

## Besoin et états *équivalents*

La minimisation des AEFD est née du besoin de simplifier des AEFD qui ont des états et transitions qui sont “pas nécessaires”.

![untitled](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_6.png)

![untitled](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/ressources/03_determinisation_d’un_automate_non-determinist_untitled_7.png)

Notons que dans le cas du AEFD précédent, les états $2$ et $3$ dans $A$ “jouent le même rôle”, càd. une fois que $A$ est dans l'état $2$ ou $3$, il accepte la même chaîne suffixe ($a^*$). On dit deux états sont “**équivalents**” s’ils acceptent la même chaîne suffixe. Nous pouvons éliminer l'état $3$ sans changer le langage de $A$, en redirigeant vers $2$ les arcs menant vers $3$.

**Théorème**. Un AEFD peut être minimisé s’il y a des paires d’états $(q,q^\prime) \in Q$ qui sont équivalents. Deux états sont équivalents s’ils acceptent le même langage.