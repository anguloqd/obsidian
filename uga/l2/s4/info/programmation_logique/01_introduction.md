## 01 // introduction

[Slides d’intro](coursprologl2_1_(3).pdf)

## Principaux paradigmes en programmation

### Programmation déclarative et Prolog

Ils existent deux grandes catégories qui se divisent en plusieurs sous-catégories : la programmation impérative, où la machine se retrouve dans des états et on change son état en donnant directement et clairement d’ordres (ordre es synonyme de ”impérative”) à exécuter pour arriver au résultat désiré ; et déclarative, où on explicite à peine quelques propriétés du résultat désiré mais on explicite pas comment y arriver.

Java est un langage impératif orienté-objet (il groupe d’ordres dépendant de l’état où la machine se trouve), Scheme est un langage déclaratif fonctionnel (le résultat est reçu comme la valeurs d’une série de fonctions), et Prolog est un langage déclaratif logique (le résultat est reçu comme une déduction logique ou un réponse à un système de ***faits*** et ***règles***).

## Prolog : programmation logique

### Décrire le problème et laisser à Prolog le résoudre

On utilise ce langage quand il n’existe pas d’algorithme pour résoudre un problème, mais que le contraintes qui définissent la solution sont connues. Un programme Prolog est composé de faits et règles, et est exécuté avec des requêtes (*queries* en Anglais).

Note : les deux faits et règles sont des *clauses,* et l’ensemble de clauses qui ont le même nom et même nombre d’arguments (même arité) sont des *prédicats*. Parfois on dit “prédicat” quand on veut juste dire “clause”, c’est normale la confusion, souvent il est plus utile de parler de prédicats.

### Faits : propositions de base

Les faits ou **propositions** sont des affirmations vraies et donnent une propriété à un objet. Elles utilisent le verbe “être” comme dans “le soleil est une étoile”, qui donne au soleil le propriété d’étoile, comme si le soleil est désormais une constante de type “étoile”. Elles sont les **propositions de base**.

Pour le cas de la proposition capitale, notons qu’on peut lier plusieurs objets sous un prédicat, mais on n’explicite pas comme elles sont liées. Dans ce cas, on pourrait l’interpréter comme “Paris est la capitale de France”, mais notons déjà que cela c’est notre interprétation ! **Prolog juste sait qu’il existe une proposition vraie par rapport au nom “capitale” qui lie aux constantes `france` et `paris`**.

```prolog
– etoile(soleil).
– capitale(france, paris).
– temperaturesSemaine14([5,7,7,4,2,4,10]).
– position(roi,b,7).
```

**Les prédicats ne sont pas de fonctions !** C’est-à-dire, elles ne retournent pas une valeur qui pourrait être gardée/affectée dans une variable, et donc on ne peut pas mettre directement un prédicat directement dans un autre prédicat.

### Règles : opérations logiques avec des faits

Les règles sont les opérations logiques de premier ordre, elle prennent des objets comme des variables. Par exemple, $X$ est une planète $\equiv$ ($X$ est un astre)$\land$($E$ est une étoile de $X$)$\land$($X$ est un satellite de $E$).

```prolog
planete(X) :- astre(X),etoile(E),satellite(X,E).
```

Normalement, le symbole $\equiv$ signifie si et seulement si ($\iff$) dans la logique de première ordre. Cela dit, en Prolog, le symbole de “définition” (`:-`) en fait est une implication logique et ne pas une équivalence logique. Si $p_1, \dots, p_n$ sont des prédicats, alors :

$$\text{En Maths : } p_1(\dots)\land p_2(\dots)\land \dots \land p_n(\dots) \implies r(\dots)

\\

\text{En Prolog : } r(\dots) \space \underbrace{:-}_{\implies} \space p_1(\dots)\land p_2(\dots)\land \dots \land p_n(\dots)$$

### Requêtes : exécution

La manière de faire des exécutions en Prolog sont les requêtes, où on demande quel objet vérifierait un prédicat (fait ou règle), ou des objets pour lesquels un prédicat serait vrai.

On peut spécifier toutes le variables comme constantes (dans ce cas, Prolog juste nous retourne si c’est vrai ou faux) ou on peut spécifier quelques variables et laisser les autres libres (dans ce cas, Prolog nous montrera les combinaisons des variables non-spécifiés qui vérifieraient le prédicat).

```prolog
?- factorielle(4,24) % true
?- planete(lune) % false

?- factorielle(4,X) % X=24
```

Par défaut, tous les objets n’ont pas une propriété, et on spécifient ceux qui l’ont. Le code qui suit le rend clair :

```prolog
- herbivore(chevre)

?- herbivore(chevre) % true
?- herbivore(loup) % false
?- carnivore(loup) % error ! le prédicat n'est pas défini, unknown procedure
```

### Particularités sur le software SWI-Prolog

- Une ligne qui commence avec `-` est une clause, et avec `?-` est une requête.
- Toutes les clauses (faits et règles) finissent avec un point `.`.
- On fait un commentaire sur ligne avec `%`.
- La définition d’une règle se fait avec `:-`, tant que l’affectation d’une constante avec une propriété se fait simplement avec la forme `propriete(constante)`, où le nom de la constante et le fait sont les deux en minuscules.
- Il peut y avoir plusieurs conditions après le `:-`, séparées par des virgules ou des points-virgules. La virgule correspond à un ET logique (conjonction, $\land$) et le point-virgule à un OU logique (disjonction, $\lor$).
- **Constantes et variables** : une constante commence forcément par une minuscule, un entier ou un flottant. Une variable commence par majuscule ou par `_`.
    - Le variables utilisées dans un fait ou règle sont universellement quantifiées par Prolog, avec le quantificateur mathématique $\forall$ qui signifie “pour tout”.
    - Le variables utilisées dans une requête sont existentiellement quantifiées par Prolog, avec le quantificateur mathématique $\exists$ qui signifie “existe-t-il”.
- **Variables anonymes** : si jamais on veut faire une requête qui prend plusieurs arguments mais il y en a quelques-uns qui ne nous intéressent pas, on utilise le symbole `_` à la place de l’argument.
    - Une variable commençant par '`_`' et de longueur ≥ 2 n'est pas anonyme/muette.

    ```prolog
    -mange(loup, chevre). % fait
    -carnivore(X) :- mange(X, Y), animal(Y). % règle
    -cruel(X) :- mange(X, _). % règle, le 2ème argument ne nous intéresse pas
    
    -? cruel(loup) % true
    ```

### Opérateurs basiques

- `<`,`>`,`=<`,`>=`,`=:=` (calcul, puis égalité), `=\=`, `mod`
- L’opérateur `=` ne fait pas de calculs : `X=5+2` est différent de `X=7`
Il faut se dire que `=` est une égalité de “opérations” et pas de valeurs.
- `is` fait des calculs et  puis fait la “affectation”
(ce n’est pas vraiment de l’affectation, mais ça marche pareil)
