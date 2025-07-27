# 01 // java

# Premiers éléments de programmation Java

## Lecture

En premier, on doit importer le `Scanner` pour lire les entrées de l'utilisateur. Après, on crée un nouveau `Scanner`.

```java
import java.util.Scanner;
Scanner s = new Scanner(System.in);
```

Chaque fois qu’on veut prendre les entrées de l’utilisateur, on utilisera le `Scanner` crée. En plus, il est conseillable de fermer le scanner pour utiliser la mémoire avec efficience.

```java
int nbExemple = s.nextInt(); // ici, la console demande un int à l'utilisateur
s.close(); // fermer le scanner pour garder de la mémoire
```

Il existe une méthode pour presque tout type primitive de Java, à exception de char, pour lequel on utilise une petite astuce. Ici sont toutes les méthodes :

```java
s.nextBoolean();
s.nextByte();
s.nextDouble();
s.nextFloat();
s.nextInt();
s.nextLine();
s.nextLong();
s.nextShort();

s.nextLine().charAt(0); // astuce pour prendre un type char de l'utilisateur
```

Conseil : il est mieux de créer des différents `Scanner` dépendant des la quantité de type de variables qu’on va lire. Un `Scanner` qui lit deux type primitives différents peut causer d’erreurs, il m’est déjà arrivé ! 

## Les variables

Elles sont des “boîtes“ pour garder des valeurs dans la RAM du PC.
Le format des valeurs sont les types primitives, qui sont les formes les plus basiques d’information pour créer des structures de données. Ils sont :

- `String` (avec majuscule, sinon erreur !),
- Nombres entiers :
    - `byte`, du -128 au 128 (-2^7 à 2^7)
    - `short`, du -32.768 au 32.767 (-2^15 à 2^15-1)
    - `int`, du -2.147.483.648 au 2.147.483.647 (-2^31 à 2^31-1)
    - `long`, du -9.223.372.036.854.775.808 au -9.223.372.036.854.775.807 (-2^63 à 2^63-1)
- Nombres fractionnaires (réels) :
    - `float`, du 1.40239846e-45 au 3.40282347e38, positif ou négatif.
    Ils finissent par f, ex.: **`float** f = 3.145f;` sinon erreur !
    - `double`, du 4.9406564584124654e-324 au 1.7976931348623157e308, positif ou négatif.
    Ils finissent par D, ex.: **`double** d = 3.13457599923384753929348D;` sinon erreur !
- `boolean`, true/false,
- `char` (string d'une seule lettre, mais ce pas une string).

Pour transformer une variable à autre, on utilise un "cast".

```java
int a = 7;
float b = 3;
int res; // prend 0 comme valeur par défaut
res = a / (int) b;
```

Le cast, dans ce cas, est le `(int)` juste à droite de l'affectation.
Notons que, si b n’était pas transformé à un `int`, on aurait un erreur, car res doit être défini par l’opération de deux entiers.
En plus, `int` arrondit vers le bas.

## Les tests

Java utilise les conditions logiques communes des maths. Particulièrement, `<`, `<=`, `>`, `<=`, `==` et `!=`. **Pour comparer des `string`, on utilise la méthode `.equals()`.**

- `if` exécutera un bloc si la condition est vraie,
- `else` l’exécutera si toute condition précédente est fausse,
- `else if` l’exécutera si la condition précédente est fausse et la actuelle est vraie.
- C’est possible d’imbriquer des conditionnels.

```java
if (condition1) {
  // bloc à exécuter si condition1 vraie
} else if (condition2) {
  // bloc à exécuter si condition1 fausse et condition2 vraie
} else {
  // bloc à exécuter si condition1 fausse et condition2 fausse aussi
}
```

### (*) `switch`, `break` et `default`

Le mot clef `switch` rends plus simple l’écriture et lecture des opérations qui auraient besoins d’`if` imbriqués.
Optionnellement, il y a deux autres mots clefs qui vont avec `switch`:

- `break` est utilisé pour n’évaluer plus l’expression et sortir du conditionnel.
Si on n’utilise pas `break`, on va réévaluer indéfiniment l’expression et jamais sortit du conditionnel.
- `default` est utilisé si jamais aucun `case` est vrai.

```java
switch(expression) {
  case x:
    // bloc à exécuter si expression == x
    break;
  case y:
    // bloc à exécuter si expression == y
    break;
  default:
    // bloc à exécuter si expression != x et expression != y
```

## Les itérations

Les itérations ou “loops” en anglais sont des exécutions répétitives d’un bloc de code sous une condition vérifiée.

### `while`

`while` est le loop le plus simple en Java.
Un bloc de code sera répété jusqu’à qu’une condition ne soit plus vérifiée.

```java
while (condition) {
  // bloc de code à exécuter si condition vraie
}
```

Une variante est le loop `do/while`, qui exécutera le code une fois, puis exécutera de nouveau le code tant que la condition soit vérifiée. 

```java
do {
  // bloc de code à executer 
}
while (condition);
```

### `for`

`for` est un loop avec une syntaxe plus simple, à condition qu’on sache combien de fois on va itérer. Il faudra une variable indice i, une condition sur ce variable indice et son incrémentation. 

```java
for (int i = 0; condition sur i; i++) {
  // bloc de code à exécuter tant que la condition sur i soit vérifiée
}
```

Une variante est le loop `for-each`, qui itère sur un liste et pas sur une variable indice. Le nom de la variable est local dans le loop, pendant que le nom de la liste doit être global.

```java
for (type nomVariable : nomListe) {
  // bloc de code à executer
}
```

### (*) `break` et `continue` dans les loops

C’est possible aussi d’utiliser `break` et `continue` dans les loops. `continue` arrêt l’exécution d’un bloc de code et passe à la suivante itération. `break` arrête le loop complètement et en sort. On peut les utiliser avec les deux `while` et `for`.

```java
int i = 0;
while (i < 10) {

	if (i == 4) {
		i++;
		continue;
	}
	
	else if (i == 7) {
		break;
	}

	else {
		System.out.println(i);
		i++;
	}

}
```

## Les méthodes (fonctions)

Le nom formel d’une fonction en Java c’est une *méthode* ou method. Une méthode c’est une fonction forcément défini dans une `class`. On verra après qu’est-ce qu’une `class`.

Particulièrement, une méthode est un bloc de code qui est exécuter seulement quand il est appelé. Ils acceptent des données pour faire ses actions, appelés *paramètres*. Ils sont utiles pour définir un bloc de code une fois et le réutiliser plusieurs fois.

```java
public class Script {
  static void maMethode() {
    // bloc de code à executer chaque fois que la méthode est appelée
  }
}
```

Il y a deux mots clés avant maMethode, qui sont `static` et `void`.

- `static` signifie que la méthode appartient dans la class Main et pas dans un objet de la `class` Script (ou de la class “principale”, si on veut).
- `void` signifie que maMethode ne retourne aucune valeur. Si jamais elle en retourne, on devra spécifier le type primitive de la valeur retournée, comme `string`, `int`, etc.; et aussi écrire “`return` maVariable” dans la méthode, normalement à la fin.

Les paramètres effectifs—c’est à dire, la valeur spécifique qui prend les paramètres abstraits—sont appelés *arguments.*

Il est aussi possible de définir une méthode et de l’utiliser dans la définition d’une autre méthode.

### Fonctions utiles

- `Math.Random()` : retourne un nombre entre 0 et 1. C’est une fonction sans paramètres.
- `Math.sqrt(x)` : retourne la racine carrée de x. Elle a un paramètre de type double. Comme il n’y a pas de perte d’information à transformer un int, un short, etc. en double, il n’est pas nécessaire d’utiliser un cast si le paramètre est entier ou float, la conversion se faisant automatiquement par Java.
- `Math.pow(x,y)` : retourne x^y . Attention à l’ordre des paramètres.

### (*) Surcharge de méthodes

Il est possible de définir deux méthodes avec le même nom. Normalement, c’est fait quand les deux méthodes font des actions similaires, est c’est plus convenant de les avoir sous un même nom.

```java
// manière longue
static int sommeInt(int x, int y) {
  return x + y;
}

static double sommeDouble(double x, double y) {
  return x + y;
}

public static void main(String[] args) {
  int nb0 = sommeInt(8, 5);
  double nb1 = sommeDouble(4.3, 6.26);
  System.out.println("int: " + nb0 + ", double: " + nb1);
}

// ---------------------------------------------------------------------

// manière courte, avec surcharge de méthodes
static int somme(int x, int y) {
  return x + y;
}

static double somme(double x, double y) {
  return x + y;
}

public static void main(String[] args) {
  int nb0 = somme(8, 5);
  double nb1 = somme(4.3, 6.26);
  System.out.println("int: " + nb0 + ", double: " + nb1);
}

```

Notons que Java peut faire la différence entre les deux fonctions à partir des types des variables. 

### (*) Rang des variables

Quand une variable est définie, sa valeur est accessible **seulement dans la région ou elle à été définie**. Cette région est appelée le rang de la variable, et elle est marquée par l’aire entre deux accolades `{}`.

```java
public class Main {
  public static void main(String[] args) {

    // [si on écrit du code ici,
		// ce n'est pas possible
		// d'utiliser la variable x]

    **{ // ici, on ouvre un 2ème bloc de code avec les accolades**

      int x = 100;

      // désormais, on peut utiliser la variable x 

      System.out.println(x);

   **} // ici, c'est la fin du bloc de code #2**

  // [ici ce n'est pas encore possible
	// d'utiliser la variable x, car elle
	// a été défini seulement dans le bloc #2]

  }
}
```

Un bloc de code (avec `{}`) peut exister par si seul ou accompagné des mots clés comme `if`, `while` et `for`. Dans le cas de `for`, les variables dans les parenthèses du `for` font aussi partie de code, même s’ils sont avant de l’ouverture des accolades.

### (*) Définition récursive d’une méthode

Une méthode définie par récursion est une fonction qui s’appelle elle même dans sa définition. Une définition par récursion a besoin de deux éléments:

- **Le *cas de base* (ou plusieurs cas de base)** : une réponse de la fonction ou elle retourne une valeur fixe et immédiate, sans besoin de s’appeler elle même.
- **Le *cas de propagation* (ou le pas récursif)** :  une réponse de la fonction qui à besoin d’une autre réponse de la fonction, et se rapprochant finalement au cas base.

```java
public class Main {
  
	// corps principal du code
	public static void main(String[] args) {
			
    int result = sum(3);
    System.out.println(result);

  }
	
	// fonction récursive
  public static int sum(int k) {
		
    if (k = 0) {
      return 0; // cas de base

    } else {
      return k + sum(k - 1); // cas de propagation
    }

  }

}

// ---------------------------------------------------------------------

// résultat
// appel #1 : 3 + sum(2)
// appel #2 : 3 + 2 + sum(1)
// appel #3 : 3 + 2 + 1 + sum(0)
// appel #4 : 3 + 2 + 1 + [0], on applique le cas de base ici
// finalement, sum(3) = 7.
```

## (*) Les classes

![Un *objet* est une collection de de données et operations.](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/ressources/01_java_untitled.png)

Un *objet* est une collection de de données et opérations.

Java est un langage de programmation orientée objet (POO). Dans ce type de langage, tout est vu comme un objet. Un objet est juste une collection de données et procédures, connues comme attributs (ou variables ou *fields*) et méthodes.

Encore plus, Java est un langage à classes. C’est à dire, chaque objet est une instance d’une `class`. Une `class` est une structure de base, pendant que un objet est le bâtiment construit sur cette structure.

Déjà, tout programme Java commence comme suit. Le nom de la `class` doit être forcément écrit avec majuscule ! On accède aux attributs et méthodes avec la syntaxe `.`.

```java
public class Programme {
	// bloc de code
}
```

C’est à dire, **le même programme Java est une `class`**. Donc, on peut construire des attributs et méthodes. Ces attributs serait accessibles dans les méthodes, **même si elles n’y sont pas définies,** car elles sont déjà incluses avec la déclaration d’un objet.

Il faut savoir qu’on peut créer des objets uniquement dans la méthode `main`.

```java
public class Programme {
	
	int nb0 = 1;
	int nb1; // pas besoin de donner une valeur, on peut juste la déclarer

	public static void main(String[] args) {
    Programme monObj = new Programme(); // on crée l'obj. DANS le "main"
    System.out.println(monObj.nb0);
	}

}

// retourne 1
// notons que "monObj" est un objet de type "Programme"
```

Par convention, dans l’écriture d’un programme complexe, on définit quelque `class` dans un fichier Java et on les utilise dans un autre fichier Java où on écrit le code principale. Il est nécessaire que les deux fichiers soient présents sur le même dossier. 

```java
// fichier "Variables.java"

public class Variables {
  int x = 5;
}

// ---------------------------------------------------------------------------

// fichier "Programme.java"

class Programme {
  public static void main(String[] args) {
    Variables monObj = new Variables();
    System.out.println(monObj.x);
  }
}

// retourne 5
```

### L’état : ensemble des attributs des classes

Une fois un objet a hérité des attributs, on peut les modifier comme suite :

```java
public class Programme {
  int x = 10;

  public static void main(String[] args) {
    Programme monObj = new Programme();
    monObj.x = 25; // x est désormais 25
    System.out.println(monObj.x);
  }
}

// retourne 25, pas 10
```

Si on ne veut pas que la variable soit modifiable, on utilise le mot clé `final`:

```java
public class Programme {
  final int x = 10;

  public static void main(String[] args) {
    Programme myObj = new Programme();
    monObj.x = 25; // <- erreur dans l'exécution du code !

		// il aura un erreur ici,
		// car on ne peut pas modifier la valeur de un variable **final**

    System.out.println(monObj.x);
  }
}

// retourne 25, pas 10
```

En outre, les variables globaux n’existent pas dans Java. Une variable forcément fait partie d’une classe, donc on ne peut pas créer une variable sans une classe, et finalement on déduit que toute variable appartient à une classe, donc elle est locale.

Il est possible d’en simuler créant une `class`, déclarant les variables là et puis les référencer dans d’autres `class`. Normalement, ce type de `class` est appelé *Globals,* *Reference* ou *Constants.*

```java
public class Globals {
  public static final int globalInt = 0;
	public static final double globalDouble; // déclaration sans valeur
}

public int Methode {
	System.out.println(Globals.globalInt);
}

// retourne 0
```

### L’interface : ensemble des méthodes des classes

Déjà, chaque fois qu’on appelle une classe, on doit écrire le nom de la méthode suivi des parenthèses `()`.

Après, les deux mots clés qui sont avant le nom d’une méthode sont `static`/`public` et le type de retourne (ou `void`, si elle ne retourne rien). Voyons la différence :

- Les méthodes `static` peuvent être appelés sans besoin d’un objet en concret.
- Les méthodes `public` forcément doivent faire partie d’un objet existent pour être appelées.

Donc, on verra des méthodes `public` uniquement dans le `main`, car c’est seulement dans le main où on peut créer des objets, qui sont nécessaires pour appelés les méthodes `public`.

```java
public class Principale {
  // méthode statique
  static void methStatique() {
    System.out.println("Coucou !");
  }

  // méthode publique
  public void methPublique() {
    System.out.println("Au revoir !");
  }

  // méthode principale ("main")
  public static void main(String[] args) {
    methStatique(); // appel la méthode statique
    // methPublique(); <- erreur! on n'est pas dans un objet

    Principale monObj = new Principale(); // creer un objet dans meth. main
    monObj.methPublique(); // appel la méthode publique dans l'objet crée
  }
}

// retourne "Coucou !"
// retourne "Au revoir !"
```

La méthode `main` est considérée la méthode la plus importante. En bref, elle est le corps principal du code, ce que fait le programme, utilisant d’autres méthodes et variables définies hors du `main`. Un programme java ne peut pas marcher si le `main` n’existe pas. Elle est toujours exécutée lors de l’exécution du programme.

### Constructeurs

Le constructeur est une méthode spéciale. Elle est utilisée pour “initialiser” des objets, c’est à dire, pour créer un objet et qu’il hérite des attributs et méthodes. On l’appelle chaque fois qu’on utilise l’opérateur `new` dans le `main`.

Normalement, si on ne déclare pas le constructeur, il est présent invisiblement. On peut ne pas le déclarer pour simplicité. En revanche, on le déclare pour initialiser un objet et changer les valeurs de ses primitives, car les valeurs par défaut ne conviennent pas. 

Ils existent deux manières d’utiliser un constructeur : par défaut et paramétrisé. Le constructeur par défaut agit de la même manière que comme si on ne le déclare pas. Le constructeur paramétrisé prend un paramètre pour fixer la valeur d’un attribut de l’objet.

Dans le paramétrisé, on utilise la syntaxe `this.` pour faire référence à l’attribut du même objet, ou aussi avec les méthodes.

```java
public class Demo {  
	int i;  // on pourrait écrire juste "int i = 100;", 
					// si on voulais omettre la déclaration du constructeur

	// constructeur par défaut   

	public demo() {  
		// ici, on fixe la valeur de l'attribut i  
		this.i = 100;  
	}  
}

// ----------------------------------------------------------------------

public class Demo {  
	int i;  

	// constructeur paramétrisé   

	public demo(int i) { // cette méthode prend i comme paramètre et...
		this.i = i; // fixe la attribut i de l'objet comme la valeur de param. i
	}
}
```

![untitled](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/ressources/01_java_untitled_1.png)

### Modificateurs

Les modificateurs sont des mots clés qui accompagnent les classes, attributs et méthodes dans leurs déclarations. Souvent, ils spécifient la capacité d’être accédés par d’autres classes, mais ils peuvent aussi spécifier d’autres fonctionnalités.

On les classifie par rapport à ses fonctionnalités: modificateurs d’accès et de non-accès.

- Modificateurs d’accès :
    - Pour les classes :
        - `public` : classe accessible par d’autre classes.
        - *default* : classe accessible seulement par d’autre classes dans le même package. Si on ne spécifie pas un modificateur d’accès dans la déclaration d’une classe, invisiblement on utilise *default*.
    - Pour les attributs et méthodes :
        - `public` : attribut/méthode accessible par d’autre classes.
        - `private` : attribut/méthode accessible seulement dans la classe présente.
        - *default* : attribut/méthode accessible seulement par d’autre classes dans le même package. Si on ne spécifie pas un modificateur d’accès dans la déclaration d’un attribut/méthode, invisiblement on utilise *default*.
        - `protected` : attribut/méthode accessible seulement par d’autre classe dans le même package et sous-classes.
- Modificateurs de non-accès :
    - Pour les classes :
        - `final` : classe pas utilisable pour créer d’autre classes.
        - `abstract` : classe pas utilisable pour créer d’autre objets.
        Pour l’accéder, il faut l’hériter d’une autre class.
    - Pour les attributs et méthodes :
        - `final` : les valeurs du attribut/méthode ne sont pas modifiables.
        - `static` : attribut/méthode appartient à une classe et pas à un objet.
        - `abstract` : la méthode hérite son corps de code d’une sous-classe.
        Seulement possible avec les méthodes, dans des class aussi abstract et le corps de la méthode doit être vide comme `abstract void test();`.
        - `transient` : attribut/méthode sont ignorés lors de la sérialisation de l’objet qui les contient.
        - `synchronized` : les méthodes peuvent seulement être accédés par un fil à la fois.
        - `volatile` : la valeur d’un attribut n’est pas gardé localement dans un fil de la mémoire, et est toujours lit dès la mémoire principale.

# Parcours et recherche dans les listes et tableaux

## Les tableaux

Un tableaux peut être vu comme une “liste de liste”. Les listes en Java sont appelées *Arrays*. Avant, voyons la liste simple. La syntaxe utilisé est la suivante :

```java
<type> [ ] <nom du tableau> = new <type> [<nombre d’éléments>];

String[] noms = new String[50]; // tableau initialisé avec 50 strings vides
String[] voitures = {"Volvo", "BMW", "Ford", "Mazda"}; // déf. par extension
```

Il est possible de référencier et changer la valeur dans une position dans l’`array`. Finalement, on peut obtenir la longueur de la liste avec la méthode `.length`.

```java
System.out.println(voitures[0]); // <- retourne "Volvo"
voitures[0] = "Audi"; // <- modification du valeur en position 0

System.out.println(voitures.length); // <- retourne 4
// note : la méthode ".length" ne finit pas avec parenthèses ()!
```

Finalement, on utilise deux fois les crochets `[][]` pour définir un tableau. On pourrait aussi définir un liste de listes de listes, avec les crochets trois fois, etc.

```java
// tableaux : listes à 2D
float[][] tab = new float [20][30];
```

## Schéma général de parcours

Un parcours est une procédure de traitement de données. On passe par chaque élément d’une séquence ou liste et applique une opération sur chaque élément de la liste jusqu’à arriver à la fin.

```java
**// Initialisation**
while (!FindeSequence) {
	// Traitement ElementCourant
	// Avancer
}

// **Schéma avec traitement séparé de la séquence vide**
if (SequenceVide) {
	// Traitement SequenceVide
}

else {
	// Initialisation
	do {
		// Traitement ElementCourant
		// Avancer
	} while (!FindeSequence)
}
```

## Schéma général de recherche

Pareil au parcours, une recherche est une procédure de traitement. La différence est que on s’arrête idéellement quand on trouve un élément désiré, ou si on arrive à la fin de la séquence ou liste sans trouver à celui-ci.

```java
// Initialisation
while (!FindeSequence) && (EC != ED) {
	// Avancer
}

// arrivés à ce point-ci, une des deux conditions est verifiée

if (!FindeSequence) { // si on n'est pas arrivé à la fin, élément désiré trouvé
	// Traitement ElementCourant
}

else { // sinon, élément désiré non trouvé dans la liste
	// Traitement si ElementDesiré non trouvé
}

```

## Éléments communs entre parcours et recherche

- ElémentCourant représente l’élément courant de la séquence.
- FindeSéquence représente l’expression logique qui caractérise la fin de la séquence.
- Initialisation représente la partie algorithmique consistant à se positionner sur le premier élément de la séquence.
- Avancer représente la partie algorithmique consistant à passer de l’élément courant au l’élément suivant.

# Les fichiers texte

## Lecture dans un fichier

La lecture d’un fichier se fait en définissant une variable de type `BufferedReader`. 
On doit lire le fichier texte ligne par ligne, donc, elle est déjà pareil au algo. de parcours.

Il y a deux conditions pour lire des fichiers :

- Il faut ajouter au début du programme l’instruction : `import [java.io](http://java.io/).*;`.
- Il faut indiquer à java qui gère les éventuelles erreurs (fichier inexistant, par exemple) en ajoutant à la fin de la ligne du main cette instruction : `throws IOException`.

On considère que la fin du fichier texte est atteint quand on arrive à lire `null`.

La méthode `.readLine()` est utilisé pour passer à la ligne suivante et garder la ligne sous la forme de `string` dans le `BufferedReader`. On voit les contenus de cette ligne en imprimant le `BufferedReader`.

Analogie entre parcours et lecture de fichiers texte :

![untitled](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/ressources/01_java_untitled_2.png)

Analogie entre recherche et lecture de fichiers texte :

![untitled](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/ressources/01_java_untitled_3.png)

## **Écriture dans un fichier**

Ici, on doit créer une variable de type `BufferedWriter`. Voici le schéma général d’écriture dans un fichier :

```java
BufferedWriter f;
String ch;

f = new BufferedWriter(new FileWriter ("<nom fichier>"));
ch = ...

f.write(ch);
f.newLine(); // analogue de "avancer"
…

f.close();
```

Si l’on veut ajouter les éléments à la fin d’un fichier existant, et non pas remplacer les anciennes valeurs, il faut créer le fichier avec un paramètre supplémentaire égale à `true` :

```java
f = new BufferedWriter(new FileWriter ("<nom fichier>", true));
```

# (*) Préparer Sublime Text pour écrire Java

## JRE, JDK et JVM

![untitled](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/ressources/01_java_untitled_4.png)

[https://www.javatpoint.com/difference-between-jdk-jre-and-jvm](https://www.javatpoint.com/difference-between-jdk-jre-and-jvm)

## Compilation et exécution (”building”)

- Compilation : c’est un sous-procès de l’exécution. Il s’agit de transformer le code source en code objet, traduire le code Java (lisible par l'homme) en bytecode, afin que la machine virtuelle le comprenne. Dans le contexte Java, c’est transformer les fichiers .java en fichiers .class.
- Liaison (”linking”) : l'acte de combiner du code objet avec des bibliothèques dans un exécutable brut. De nombreux compilateurs, dont Java, gèrent automatiquement l'étape de **liaison après la compilation du code source.**
- Exécution : la séquence composée de la **compilation** et de la **liaison**, avec éventuellement d'autres tâches telles que la création de l'installateur.

## Java dans Sublime Text

- En premier, on a besoin de créer un nouveau système d’exécution “RunJava”.
Tools → Build System → New Build System…
Il aura un nouveau onglet qui s’ouvrira. On va écrire le code suivant  et garder le fichier sous le nom “RunJava.sublime_build”.
[https://www.sublimetext.com/docs/build_systems.html](https://www.sublimetext.com/docs/build_systems.html)
    
    ```java
    {
    "target": "terminus_exec",
    "cancel": "terminus_cancel_build",
    "shell_cmd": "javac $file && java $file_base_name",
    "working_dir": "$file_path"
    "file_regex": "^(...*?):([0-9]*):?([0-9]*)"
    }
    ```
    
- Après, on installe les paquets Javatar et Terminus. Le dernier permet de faire inputs.
L’installateur s’ouvre avec Ctrl + Shift + P → “Package Controll: Install…”.
[https://javatar.readthedocs.io/en/latest/installation.html](https://javatar.readthedocs.io/en/latest/installation.html)
[https://forum.sublimetext.com/t/how-to-have-input-java/47826/9](https://forum.sublimetext.com/t/how-to-have-input-java/47826/9)
- J’avais un erreur chaque fois que j’essayais de run un script Java.
”Error: Could not find or load main class”. C’était un erreur avec javac.
**Il faut installer JDK (pas confondre avec JRE !)**, puis réparer le path and %JAVA_HOME% avec le tutoriel YouTube suivant.

[https://www.youtube.com/watch?v=104dNWmM6Rs&list=PLE9K8gXMCpUG5C1JarMA7p9cDcWtvi-0b&index=9](https://www.youtube.com/watch?v=104dNWmM6Rs&list=PLE9K8gXMCpUG5C1JarMA7p9cDcWtvi-0b&index=9)