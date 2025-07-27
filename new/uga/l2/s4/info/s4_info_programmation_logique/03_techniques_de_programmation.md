# 03 // techniques de programmation

[Slides de techniques 1](ressources/03_techniques_de_programmation_coursprologl2_3.pdf)

[Slides de techniques 2](ressources/03_techniques_de_programmation_coursprologl2_4.pdf)

# Prédicat `writef/2`

## Imprimer des variables dans la console

C’est juste un prédicat pour concaténer ou inclure de valeurs de variables dans une chaîne. Le première paramètre est la chaîne à imprimer contenant `%t` pour les parties variables, et le deuxième paramètre est la liste de valeurs en ordre à afficher dans le string.

```prolog
writef("Le joueur %t a gagné %t points.",[Nom,Pts])
```

# Écriture d’un test `if`

## Une suite de prédicats est déjà un test `if`

Tant que le mot clé if n’existe pas dans Prolog, on peut la simuler en écrivant plusieurs règles (”fonctions”) sous le même prédicat (”symbole”), comme si c’était de la surcharge de fonctions/méthodes en programmation par objets.

```prolog
% écrire min/3 qui détermine la plus petite de deux valeurs
min(X,Y,Y) :- X>=Y. % le minimum entre X et Y est Y si X >=Y.
min(X,Y,X) :- X=<Y. % le minimum entre X et Y est X si X <=Y.

min(4,7,R). % R=4.
```

# Programmation avec un *accumulateur*

## Technique très importante et caractéristique de Prolog !

Un accumulateur est juste l’idée d’une liste qui initialement est vide et à la quelle on ajoute des éléments à chaque itération d’un processus jusqu’à qu’on arrive au résultat désiré.

```prolog
% écrire un prédicat qui inverse l’ordre des éléments d’une liste

inverse(L,R) :- inverse(L,[],R).
inverse([],Acc,Acc). (ou inverse([],Acc,R):- R=Acc.) % fait
inverse([X|L],Acc,R) :- inverse(L,[X|Acc],R)

?- inverse([a,b,c,d],L).
% L=[d,c,b,a]
```

# La coupure `!` et le prédicat `fail`

## La coupure `!`

L’exploration systématique est une force de Prolog, mais elle conduit parfois à une explosion
combinatoire. l existe un moyen de restreindre l’exploration de l’arbre de recherche avec la syntaxe `!`. Dans un prédicat, toutes les valeurs de variables choisies avant le `!` seront fixés comme la valeur définitive de chaque variable, càd ces variables deviendront de constantes.

```prolog
a(1).
a(2).
b(1).
b(2).
p(X):- a(X), b(X)

?- p(X).
%X=1 ;
%X=2.
```

```prolog
a(1).
a(2).
b(1).
b(2).
p(X):- a(X), !, b(X).

?- p(X).
%X=1.
% remarque : X=2 n'est pas solution !
```

**Note : la coupure `!` ignore toutes les règles du même prédicat en-dessous**. Voyons :

```prolog
a(X) :- b(X), c(X).
a(X) :- d(X), e(X).
b(1).
b(Z):- d(Z).
c(1).
c(2).
d(2).
e(2).

?- a(X).
% X=1, X=2, X=2.
```

```prolog
a(X) :- b(X), !, c(X).
a(X) :- d(X), e(X).
b(1).
b(Z):- d(Z).
c(1).
c(2).
d(2).
e(2).

?- a(X).
%X=1.
```

Notons que la réponse X=2 de la première ligne de `a` n’apparaît pas comme solution car la valeur de X de fixe à 1. De même, les lignes en-dessous de a ne sont pas appelés, donc la deuxième solution n’est pas applicable. 

## Le prédicat `fail`

Ce prédicat est toujours faux. Il oblige Prolog à un retour arrière jusqu’au dernier point de choix.

```prolog
afficheChiffres :- between(1,9,X), write(X), nl, fail.
afficheChiffres. % notons que X n'est pas paramètre de afficheChiffres,
									% c'est vraiment comme un fonction sans paramètres
									% elle juste utilise X dans sa définition
```

## La combinaison des deux

Permet d’exprimer une exception ou la négation d’une condition.

```prolog
premier(N):- N1 is N-1,between(2,N1,X),N mod X=:=0,!,fail.
premier(_).
```

# Règles dynamiques avec `assert/1` et `retract/1`

## Ajouter et retirer des faits et règles dès la console

Dans l’écriture de requêtes (et pas l’écriture de prédicats), on peut ajouter et supprimer des faits et règles avec `assert` et `retract`, respectivement.

```prolog
% ajoutera ces nouveaux fait et règle
assert(etoile(soleil)).
assert(planete(X):-astre(X),etoile(E),satellite(X,E)).

meilleurScore(marie,2556).
retract(meilleurScore(_,_)) % supprimera tous les faits appeles "meilleurScore"
```

# Récupération de toutes les solutions

## Prédicat `findall/3`

`findall/3` est un prédicat prédéfini qui prends une variable et un prédicat et retourne dans le troisième paramètre `L` une liste avec toutes les valeurs de `X` qui vérifient le prédicat passé en paramètre.

```prolog
?-findall(X,planete(X),L).
% L=[terre,venus]

?-findall(X,(between(0,9,X),X mod 3 =:= 0),L).
% L=[0,3,6,9]
```

# Intégrammes

Les intégrammes appelés parfois logigrammes sont un type de casse-tête logique. On donne un certain nombre d'indices, desquels il faudra déduire l'intégralité des relations entre tous les éléments.

## Premier intégramme

> Max, Eric et Luc habitent chacun une maison différente. Ils possèdent chacun un animal domestique distinct. Les maisons sont le studio, le pavillon et le château. Les animaux sont le chat, le cheval et le poisson.

Les conditions sont :
> 
> - Max a un chat.
> - Eric n’habite pas en pavillon.
> - Luc habite un studio, il n’as pas le cheval.
> 
> La question c’est : **qui habite le château et qui a le poisson** ?
> 

```prolog
% les maisons :
maison(studio).
maison(pavillon).
maison(château).

% les animaux :
animal(chat).
animal(cheval).
animal(poisson).

% le prédicat habitation représente la relation
% entre une personne, sa maison et son animal :

	% Max a un chat :
	habitation(max,M,chat) :- maison(M).

	% Eric n’habite pas en pavillon :
	habitation(eric,M,A) :- maison(M), M\==pavillon, animal(A).

	% Luc habite un studio, il n’a pas le cheval :
	habitation(luc,studio,A):-animal(A),A\==cheval.

% le prédicat resoudre décrit l’ensemble du problème à résoudre
% avec ses 4 éléments inconnus et affiche la solution :

resoudre :-
 habitation(max,MM,chat),
 habitation(eric,ME,AE),
 habitation(luc,studio,AL),
 MM\==studio, MM\==ME, ME\==studio,
 AE\==chat, AE\==AL, AL\==chat,
 writef("max %t chat\n",[MM]),
 writef("eric %t %t\n",[ME,AE]),
 writef("luc studio %t\n",[AL]).

% ?- resoudre.
% max pavillon chat
% eric chateau cheval
% luc studio poisson
% true ;
% false.
```

## Deuxième intégramme

> Dans une rue, 3 maisons voisines sont de couleurs différentes : rouge, bleue et verte. Des personnes de nationalités différentes vivent dans ces maisons et elles ont chacune un animal de compagnie différent. Les nationalités sont anglais, espagnol et japonais. Les animaux sont les jaguar, l’escargot et le serpent.

Les conditions sont :
> 
> - L'anglais vit dans la maison rouge.
> - Le jaguar est l'animal de l'espagnol.
> - Le japonais vit à droite de la maison du possesseur de l'escargot.
> - Le possesseur de l'escargot vit à gauche de la maison bleue.
> 
> La question c’est : **qui possède le serpent ?**
> 

On va représenter la solution par une liste de 3 termes, chaque terme aura la forme suivante : `maison(couleur,nationalité,animal)`. Aussi, le prédicat solution sera `serpent(N, Rue)`, où `N` est la nationalité du possesseur du serpent et `Rue` est la liste de 3 termes `maison`.

```prolog
serpent(N, Rue) :-

	% Rue est représentée par une liste de 3 maisons :
	length(Rue,3),

	% il y a une maison rouge, une maison bleue et une maison verte :
	member(maison(rouge,_,_),Rue),
	member(maison(bleue,_,_),Rue),
	member(maison(verte,_,_),Rue),

	% l'anglais vit dans la maison rouge :
	member(maison(rouge,anglais,_),Rue),

	% le jaguar est l'animal de l'espanol :
	member(maison(_,espagnol,jaguar),Rue),

	% le japonais vit à droite de la maison du possesseur de l'escargot :
	nextto(maison(_,_,escargot),maison(_,japonais,_),Rue),

	% le possesseur de l'escargot vit à gauche de la maison bleue :
	nextto(maison(_,_,escargot),maison(bleue,_,_),Rue),

	% le troisième animal est un serpent :
	member(maison(_,N,serpent),Rue).

% ?- serpent(N,Rue).
% N = japonais,
% Rue = [maison(rouge, anglais, escargot),
 % maison(bleue, japonais, serpent),
 % maison(verte, espagnol, jaguar)]
```