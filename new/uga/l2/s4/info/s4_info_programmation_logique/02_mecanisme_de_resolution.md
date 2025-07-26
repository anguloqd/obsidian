# 02 // mécanisme de résolution

[Slides de mécanisme de résolution](coursprologl2_2_(2).pdf)

# Unification

## Faire correspondre deux expressions, si possible

Procédé par lequel on essaie de rendre deux clauses identiques par des substitutions, en donnant des valeurs aux variables qu’elles contiennent, càd. **en instanciant** les variables.

```prolog
-? p(a,X) = p(a,b) % X = b
-? p(a,b) = p(b,a) % false, impossible car a et b sont des constantes
-? p(X,Y) = p(a,b) % X = a, Y = b
-? p(X,X) = p(a,b) % false, impossible que X = a et X = b au même temps
-? X=Y,p(X,Y)=p(a,b) % false
```

# Parcours de résolution

## Recherche exhaustive

Prolog en premier teste les possible solutions du haut en bas, et lit les règles de gauche à droit.

```prolog
- pere(charlie, david). % (p1)
- pere(henri, charlie). % (p2)
- papy(X,Y) :- pere(X,Z), pere(Z,Y). % (p3)

-? papy(X,Y). % requête
```

![Voyons que Prolog teste en premier le paire (charlie,david) pour le première appel à `pere(X,Z)`, puis il teste (henri,charlie). Quand Prolog arrive a un point où il est impossible de trouver une proposition vraie, il s’arrête, reviens en arrière au dernier point de choix (*backtrack*) en défaisant toutes les unifications ou maths faits depuis ce point, et essaie la combinaison suivante, comme ça il teste toutes les possibilités possibles.](new/uga/l2/s4/info/s4_info_programmation_logique/02_mecanisme_de_resolution/untitled.png)

Voyons que Prolog teste en premier le paire (charlie,david) pour le première appel à `pere(X,Z)`, puis il teste (henri,charlie). Quand Prolog arrive a un point où il est impossible de trouver une proposition vraie, il s’arrête, reviens en arrière au dernier point de choix (*backtrack*) en défaisant toutes les unifications ou maths faits depuis ce point, et essaie la combinaison suivante, comme ça il teste toutes les possibilités possibles.

# Opérateurs

## Expressions arithmétiques

- `is` : analogue de calcul puis affectation. `=` ne fait pas des calculs à droite !
`N is 5*X` est différent de `N=5*X` !
    - **On utilise `is` avec les opérations numériques et `=` avec les opérations de strings !**
- `+`, `-`, `*`, `//` (division entière), `/` (division flottante), `mod`, `^`
- `abs(X)`, `log(X)`, `sqrt(X)`, `exp(X)`, `sign(X)`, `random(X)`, `sin(X)`, `cos(X)`, `tan(X)`, `min(X,Y)`, `max(X,Y)`, `pi`, etc.

```prolog
?- X is 2^20, Y is exp(1) % X = 1048576, Y = 2.718281828459045
?- Z is random(100)+100. % Z = 151.
?- X is sin(pi/2), Y is cos(pi). % X = 1.0, Y = -1.0.
?- S1 is sign(20), S2 is sign(-12). % S1 = 1, S2 = -1.
```

## Comparaison et unification

[récapitulatif d’opérateurs](recapitulatifoperateurs_(2).pdf)

- `T1==T2` : true si T1 est identique à T2
- `T1\==T2` : true si T1 n’est pas identique à T2
- `T1=T2` : true si T1 peut s’unifier avec T2
- `T1\=T2` : true si T1 ne peut pas s’unifier avec T2

```prolog
?- f(X)==f(x). % false.
?- f(X)=f(x). % X = x.
?- f(X)\=f(x). % false.
?- f(X)\==f(x). % true.
```

## Prédicats de comparaison

- `X=:=Y` : calcul de chaque coté, puis évaluation de possible égalité
- `X=\=Y` : calcul de chaque coté, puis évaluation de possible inégalité
- `X<Y`, `X>Y`
- `X=<Y`, `X>=Y`

```prolog
?- 5 = 3 + 2. % false, car le côte droit reste une opération est n'est pas calculé
?- 5 =:= 3 + 2. % true
```

## Entrées et sorties de texte

```prolog
% affichage
-? write("hello!"). % hello!
-? write(X). % s'utilise quand X a déjà une valeur après évaluer dans une clause

% lecture
?- read(A).
|: toto. % ceci a été écrit par l'utilisateur
% A = toto.
```

## Listes et le symbole `|`

Les listes s’utilisent comme suit :

```prolog
-? [4, toto, 12]. % cette liste est une liste "constante"
-? []. % liste vide
-? : [[1,2],[3,4],[[5]],toto]. % liste de listes

- notes([12,6,14,17,11]). % fait
-? notes(X). % X = [12,6,14,17,11]
```

On peut utiliser la syntaxe `|` pour référencier les premiers éléments à gauche d’une liste et puis le reste de la même liste comme suit :

```prolog
–? [X|L] = [1,2,3]. %  X=1 et L=[2,3]
–? [X,Y|L]=[1,2,3]. % X=1, Y=2, L=[3]

–? [_,Y|L]=[1,2,3]. % Y=2, L=[3]
–? [X|_] = [1,2,3]. %  X=1

–? [X|L] = []. % false
–? [X|L] = [1]. %  X=1 L=[]

–? [[X,Y]|L] = [[a,1],[b,2],[c,3]]. % X=a, Y=1, L=[[b,2],[c,3]]
```

# Parcours d’une liste en Prolog

## Regarder récursivement l’élément le plus à gauche

On le fait de manière récursive : on définit un cas de base et puis le cas récursif. Pour le cas de base, on indique la valeur qui correspondra ou se “mappera” à la liste vide `[]`.

```prolog
% somme des éléments d’une liste
somme([], 0).
somme([T|Q], S) :- somme(Q, S1), S is T + S1.

% nb de pairs dans une liste

nbpairs([], 0). % solution du cours, cas de base
nbpairs([T|Q], N) :- T mod 2 =:= 0, nbpairs(Q, N1), N is N1+1.
nbpairs([T|Q], N) :- T mod 2 =:= 1, nbpairs(Q, N).

nbpairs2([],0). % ma solution, cas de base
nbpairs2([A|B], N) :-
    nbpairs2(B, N1), Parite is ((A+1) mod 2), N is (Parite+N1).
```