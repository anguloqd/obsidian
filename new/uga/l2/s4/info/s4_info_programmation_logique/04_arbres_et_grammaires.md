# 04 // arbres et grammaires

Date de création: April 10, 2023 8:43 PM
Modifié: July 19, 2023 5:52 PM

[Slides d’arbres et grammaires](coursprologl2_5_(4).pdf)

# Arbres

## Définition en Informatique

Les arbres sont une structure de données récursive en Informatique pour représenter des graphes acycliques orientés possédant une unique racine, et tous les nœuds hors-racine ont un unique parent (leur définition en maths.). Si chaque nœud de l’arbre a deux fils au plus, on parle d’un arbre binaire.

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled.png)

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_1.png)

Un arbre binaire équilibré contenant N nœuds a une hauteur (distance racine-feuilles) d’environ $\log_2(N)$.

## En Prolog

Un arbre binaire est une liste de la forme [racine, sous-arbre gauche, sous-arbre droit].

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_2.png)

```prolog
[8,
	[3,
		[1,[],[]], [6,
			[4,[],[]], [7,[],[]]]],
	[10,[],
		[14,
			[13,[],[]],[]]]]
```

### Parcours en largeur

On peut le voir horizontalement : en premier les nœuds de niveau 0 (racine), puis ceux de niveau 1, etc.

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_3.png)

### Parcours en profondeur : version infixée

On commence dès la racine, on parcourt tout le sous-arbre gauche, puis on retourne à la racine, puis tout le sous-arbre droit.

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_4.png)

```prolog
parcoursInfixe([]).

parcoursInfixe([Racine,G,D]):- 
	parcoursInfixe(G),
	writef("%t ", [Racine]),
	parcoursInfixe(D).
```

### Parcours en profondeur : version préfixée

On va à gauche chaque fois que c’est possible, sinon on va a droit. On commence dès la racine, puis sous-arbre gauche, puis sous-arbre droit.

![8, 3, 1, 6, 4, 7, 10, 14, 13](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_5.png)

8, 3, 1, 6, 4, 7, 10, 14, 13

```prolog
parcoursPrefixe([]).

parcoursPrefixe([Racine,G,D]):-
	writef("%t ",[Racine]),
	parcoursPrefixe(G),
	parcoursPrefixe(D).
```

### Parcours en profondeur : version postfixée

C’est comme si on allait à droite à chaque fois que c’est possible, sinon à gauche, mais juste à la fin on inverse l’ordre de nœuds. Dans l’exemple qui suit, si on allait à droite chaque fois que c’est possible on obtient le chemin 8,10,14,13,3,6,7,4,1. La version postfixée est finalement ce chemin mais inversé. On parcourt sous-arbre gauche, puis sous-arbre droit, puis racine.

![1, 4, 7, 6, 3, 13, 14, 10, 8](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_5.png)

1, 4, 7, 6, 3, 13, 14, 10, 8

```prolog
parcoursPostfixe([]).

parcoursPostfixe([Racine,G,D]):-
	parcoursPostfixe(G),
	parcoursPostfixe(D),
	writef("%t ",[Racine])
```

# Grammaires

## Définition

La DCG (*definite clause grammar* en anglais) est une manière d’exprimer la grammaire d’un langage naturel ou formel. Elle s’appelle clause de grammaire définie car elle représente une grammaire comme un ensemble de clause définies en logique de premier ordre.

On commence par définir une phrase `s` (sentence) divisée la plupart du temps en sujet `np` (noun phrase) et prédicat `vp` (verb phrase). Dans le sujet on trouve le déterminant `d` et le nom `n`, tant que dans le prédicat on trouve tout en premier le verbe `v`, puis l’objet ou deuxième sujet, ayant la forme aussi de `d` puis `n`.

```prolog
sentence --> noun_phrase, verb_phrase.
noun_phrase --> det, noun.
verb_phrase --> verb, noun_phrase.
det --> [the].
det --> [a].
noun --> [cat].
noun --> [bat].
verb --> [eats].
```

![untitled](new/uga/l2/s4/info/s4_info_programmation_logique/04_arbres_et_grammaires/untitled_6.png)

## En Prolog

On montre un autre exemple avec une phrase de verbe “regarde” au milieu de “Pierre” et “Marie”.

```prolog
s(L) :- sn(L1), sv(L2), append(L1, L2, L).
sn(L) :- np (L).
sv(L) :- vt (L1), sn(L2), append(L1, L2, L).
np([pierre]).
np([marie]).
vt([regarde]).

?- s([pierre, regarde, marie]).
true

?- s(X).
X = [pierre, regarde, pierre] ;
X = [pierre, regarde, marie] ;
X = [marie, regarde, pierre] ;
X = [marie, regarde, marie].
```

On pourrait encore l’écrire en langage DCG et cela serait transformé en langage Prolog.

```prolog
s --> sn, sv.
sn --> np.
sv --> v, sn.
np --> [pierre].
np --> [marie].
v --> [regarde].
```

```prolog
s(L1, L2) :- sn(L1, L3), sv(L3, L2).
sn(L1, L2) :- np(L1, L2).
sv(L1, L2) :- v(L1, L3), sn(L3, L2).
np([pierre|L], L).
np([marie|L], L).
v([regarde|L], L).
```