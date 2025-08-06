# 00 // notes de td/tp/qcm

# TD

## TD1

- Les critères de correction d’un algorithme sont les suivants : être correcte (faire ce qu’il est censé de faire), être lisible/compréhensible et être efficace (l’efficacité de la mémoire est prioritaire sur l’efficacité de temps/complexité algorithmique).
- Toutes les instances de classe sont visibles entre elles toujours. Donc, une instance de classe `C` peut accéder aux attributs `private` de l’autre instance sans problème.
- Appeler des méthodes dans la condition d’un `for` ou `while` n’est pas efficace. Il faudrait garder la méthode dans une variable puis appeler la variable.
- Avec les buffers, n’oublies pas d’actualiser la taille effective !
- Fais attention aux hypothèses simplificatrices que tu fais. Toujours pense au cas le plus général des arguments quand tu désignes des méthodes.

# TP

## TP1

- Il peut avoir un seul `public class` dans un fichier, que c’est aussi le nom du fichier `.java`.
- Il y a des classes dont on peut appeler leurs méthodes sans besoin d’une instance d’elles.
Un exemple est la class `Math` ou `Integer` qui ont des méthodes `public static` comme `.pow` sans besoin de l’utiliser sur un nombre courant ni les attributs d’une instances, mais juste les paramètres passés en argument.
- La structure d’une méthode `.equals` est
    1. Confirmer si `obj` est `instanceof` la classe d’intérêt
    Normalement on fais la proposition en négatif : si `obj` n’est pas instance de `C`, return false. Puis tu continues.
    2. Garder `obj` dans une variable `x` et **le caster au passage** !!!!!!!!
    3. Compare le contenu de l’instance courante et l’`obj` d’intérêt (qui est désormais gardé dans une variable `x` de même type)

# QCM

## QCM #1 : 02/10

- Possible de faire `string x = null;`, pourquoi j’ai trouvé un erreur ? On peut pas faire des nulls avec des types simples, mais j’avais eu une autre erreur sans les types simples je crois !
- On déclare un attribut d’instance {`int i`;} d’une classe `C`. Si le constructeur fait `C(int a){int i = a;}` ce `int i` est une variable locale, pas un attribut. II faudrait faire `{i=a;}` et non pas `{int i = a;}`. **Mettre le type de variable avant implique qu’on définit une nouvelle variable**.
- Avoir une définition au niveau de la déclaration d’un attribut, puis avoir le constructeur changer la valeur, impose la valeur du constructeur sur la valeur au niveau de la définition.
- On peut pas utiliser `this` dans une méthode `static`. Ça fait pas de sens de faire this (contexte d’instance) dans une méthode static (contexte de classe).
    - De même, une méthode `static` accède seulement a des attributs `static`. En vrai, “static” est plus restrictif.
- Cast quand on passe un paramètre ? Pas inclus mais je me rappelle plus.
- Apprendre quand y’a un erreur d’exécution et erreur de compilation !

## Erreurs de compilation et exécution

### Compilation

- Erreurs de syntaxe
- Erreurs de type
Ici c’est l’erreur quand on affecte un objet de type incompatible à la variable/référence.
- Accéder un attribut non défini (qui ne veut pas dire “non initialisé”, c’est différente)
Variables non déclarées
- Appeler une méthode qui n’existe pas

### Exécution

- NullPointerException (j’ai déjà raté une question parce que je pensais que c’était un erreur de compilation)
- ArrayIndexOutOfBoundsException
- ArithmeticException
- ClassCastException
**LE `CAST` ET LE `INSTANCEOF` SONT SEULEMENT POSSIBLES EN RELATION D’HÉRITAGE!**
- IllegalArgumentException

## QCM #2 : 16/10

- Un exo confusant
- Une classe qui contient une méthode abstraite est forcément abstraite et doit être forcément déclarée abstraite
- Il peut y avoir une classe abstraite qui n’a aucune méthode abstraite, dont toutes ses méthodes sont bien définies (pense à classe Math).
- Une class abstraite PEUT avoir un constructeur. Le constructeur ne doit pas avoir le mot clé “abstract”. Il doit avoir un corps, du coup des accolades explicites.
    - Le corps peut être explicité ou laisse vide. Par contre, les accolades sont nécessaires.
- Piège instanceOf() à la place de instanceof.
- On lève jamais une exception avec .equals() même si le instanceof à l’intérieur. (La définition de equals retourne false s’il y a un erreur avec instanceof, par exemple si les deux classes à comparer n’ont pas une relation d’héritage)

## QCM #3 : 06/11

- C c = null; faire c instanceof C est false. instanceof utilise le type réel de l’objet et non pas le type déclaré (de référence).
- A a = new C(); Le type déclaré est le type assumé par le compilateur, celui avant du nom de la variable. Ici, c’est le type A.
    - (C) a; ceci changerait le type déclaré de A à C.
- Deux choses sur les interfaces : elles ne doivent forcément pas avoir des attributs (différemment des classes abstraites) ; et aussi elle peut ne pas avoir aucune méthode abstraite (càd. que d’avoir des méthodes réalisées). Une interface vide est valide.
- Import miashs.* où il y a une classe X dans le paquet miashs et un sous paquet miashs.inff5 qui contient lui-même une autre classe X. Le * importe juste miashs.X et non pas miashs.inff5.X
    - Par contre, on peut acceder au X de miashs.inff5 si on appeler toujours la classe d’intérêt par son nom complet : new miashs.inff5.X() sans besoin d’importer miashs.inff5. On pourrait coder toujours comme ça, mais ce n’est pas pratique.
- Questions d’exceptions :
    - Lancer une exception (throw new Runtime… Exception… etc) est un erreur d’exécution, pas de compilation (j’ai coché erreur de compilation, oups).
    - Pour les Exception, si class C {static void m() throws Exception{…}} et une autre classe appelle à travers une méthode à m(), comme class D{void k() {C.m()}}, telle méthode k() doit aussi spécifier “throws Exception”, sinon erreur de compilation.
        - Si k() est tel que void k() throws Exception{C.m()}, ça marche.
        - Si on appelle k() dans un try-catch Exception, ça marche.
        - Si on appelle k() dans un try-catch RuntimeException-catch Exception, dans cet ordre, ça marche.
        - Si on catch l’Exception avant de RuntimeException, c’est un erreur à la compilation. L’erreur plus générale (Exception, supertype de RuntimeException) doit être attrapé après les erreurs plus spécifiques.
        - Attraper un RuntimeException avec un catch Exception marche ? étant donné que Exception père de RTExc. ?
- Les types simples peuvent normalement de transtyper entre eux, suivant certains règles. Transtyper un simple à un objet est erreur de compilation. L’inverse aussi.