# 01 // objets et classes

[INFF5-1-1.pdf](ressources/01_objets_et_classes_inff5-1-1.pdf)

# Introduction des concepts de la programmation par objets

![Notion d’un *objet*.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/01_objets_et_classes_untitled.png)

Notion d’un *objet*.

## Les *objets* et les classes

![Un *objet* est une collection de de données et operations.](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/01_java/untitled.png)

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

![untitled](new/uga/l1/s1/info/s1_info_informatique_et_algorithmique/01_java/untitled_1.png)

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

## Réutilisation de classes et sous-classes

Réutiliser des instructions est l’un des points forts de programmer.

- **Réutilisation de l’implémentation** : utiliser une instance d’une classe dans une autre classe.
- **Réutilisation de l’interface et polymorphisme** : recycler les méthodes d’une classe dans une autre sous-classe, ou on ajoute des nouvelles fonctions/méthodes.
Le *polymorphisme* est juste le principe d’utiliser un programme sur n’importe quel sous-type d’objet ou la “forme” ou “morphisme” de l’objet original (FormeGeo).

![untitled](new/uga/l2/s3/info/s3_info_programmation_par_objets/01_introduction_a_la_programmation_par_objets/untitled.png)

```java

// Par exemple, une fonction qui prends comme argument un objet FormeGeo f, peut prendre un objet de type Cercle ou Triangle.

void dessineEtAfficheAire(FormeGeo f) {
	f.dessine();
	System.out.println("aire"+f.aire());
}
```

Une sous-classe, c’est effectivement une classe dans une autre. Précisément, c’est une classe qui ***hérite*** les attributs et méthodes d’une autre classe, comme ça il n’y a pas besoin de les redéfinir.
Par exemple, si on a une classe comme la classe “Ford”, une sous-classe pourrait être “Mustang”. 

## Composition et héritage sur Java

**La hiérarchie de classe peut-être de composition ou de héritage**. La composition définit une classe comme la somme de ses parties (”loosely coupled”, car changer la superclasse n’est pas un fait délicat), tant que l’héritage dérive une classe d’une autre (”tightly coupled”, car changer la superclasse peut causer des problèmes).

Pour la composition, on s’intéresse à la relation “avoir” ou “en faire partie”. Par exemple, une voiture a une batterie, une personne a un cœur, une maison a une pièce de vie, etc. 

```java
public class ExempleComposition {

		// des subclasses exemple,
		// on ne s'intéresse pas à les définir en profondeur

		static class Bedroom { }
    static class LivingRoom { }

    static class House {

        Bedroom bedroom; // on crée un space vide pour une sousclasse Bedroom
        LivingRoom livingRoom; // similairement pour une sousclasse LivingRoom
				
				// l'appel au constructeur suivant aura des paramètres,
				// particulièrement une class Bedroom et LivingRoom
				
        House(Bedroom bedroom, LivingRoom livingRoom) {

            // le Bedroom passé sera le Bedroom de cette classe
						this.bedroom = bedroom;
						// pareil pour le LivingRoom
            this.livingRoom = livingRoom; 
        }
    }

    public static void main(String[] args) {
        new House(new Bedroom(), new LivingRoom());
        // on instancie la classe House et rempli ses attributs Bedroom
				// et LivingRoom avec une nouvelle instance de chaque classe
    }

}
```

Pour l’héritage (d’attributs et méthodes), on s’intéresse à la relation “être” entre un père et un fils. Par exemple, un chat est un animal, une voiture est un véhicule, etc. La sousclasse est une version “spécialisée” de la superclasse.

Sur Java, on utilise le mot clé `extends` pour appeler la superclasse (avec majuscule !):

```java
class Vehicle {
  protected String marque = "Ford";        // attribut de véhicle
  public void klaxonner() {                    // méthode de véhicle 
    System.out.println("Tuut, tuut!");
  }
}

class Voiture extends Vehicle {
  private String nomModel = "Mustang";    // attribut de voiture
  public static void main(String[] args) {

    // création de l'objet "maVoiture"
    Voiture maVoiture = new Voiture();

    // appel à la méthode klaxonner()
    maVoiture.klaxonner();

    // imprimer la marque de la class Vehicle et le nom de model de la class Voiture
    System.out.println(maVoiture.marque + " " + maVoiture.nomModel);
  }
}

-------

// Tuut, tuut!
// Ford Mustang
```

Parfois, dans l’héritage, on a besoin de spécialiser une méthode hérité à notre sousclasse. Une classe parent **déterminera la forme générale des méthodes utilisées** par toutes ses classes enfants en fusionnant les méthodes héritées et redéfinies. La méthode remplacé doit garder le même nom de méthode, type d’argument et nom d’argument dans la méthode. L’ensemble des 2 derniers s’appelle la “clé” ou “signature”. **On ne peut pas supprimer des méthodes de la super-classe**.

On le fait comme suite :

```java
class Animal {
    void emitSound() {
        System.out.println("L'animal a fait un son");
    }
}
class Cat extends Animal{
    void emitSound() {
        System.out.println("Meow");
    }
}
class Dog extends Animal {
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat(); 
        Animal dog = new Dog(); 
        Animal animal = new Animal();
        cat.emitSound();
        dog.emitSound();
        animal.emitSound();
    }
}

---

// Meow
// L'animal a fait un son
// L'animal a fait un son
```

# Initialisation des objets

## Le constructeur : une méthode spéciale

Chaque fois on initialise des objets, on fait un appel au constructeur. Le constructeur est une méthode spéciale automatiquement appelée à la création de l'objet (`new`), après allocation de la mémoire.

Il a exactement le même nom que la classe et elle n’a pas de type de retour, même pas de `void`. Si on fait `new Objet()`, cela va retourne l’adresse d’allocation de l’objet, mais c’est un retour du mot clé `new` et pas du constructeur.

```java
// initialisation commun (caché)
// jusqu'à ce point du cours

// cas du constructeur par défaut

class Point{
	double x;
	double y;
}

// ou aussi...
class Point{
	double x = 1.0;
	double y = 1.0;
}
```

```java
// initisialisation avec construct.

// cas du constructeur par défaut

class Point{
	double x;
	double y;

	Point(){
		x = 1.0;
		y = 1.0
	}
} 
```

```java
// initialisation avec des paramètres passés aux attributs
// on donne des valeurs à x et y à la même ligne qu'on déclare "new", donc plus vite

// ce n'est plus le constructeur par défaut, ici on la remplacé
// donc le constructeur par défaut n'existe plus, erreur si on essaie de l'appeler
// désormais il faut forcément appelé le constructeur paramétrisé

class Point{
	double x;
	double y;
	
	Point(double x, double y){
		this.x = x; // si je fais x = x (sans "this."), on prend deux fois le param. x
		this.y = y; // de même ici avec y
		}
}
```

Notons que si on utilise le constructeur pour fixer les valeurs des attributs, les attributs doivent être déclarés avant. Donc, l'initialisation au niveau de la déclaration est faite avant l'appel au constructeur.

## Surcharge de constructeurs (et de méthodes)

Surcharger est le fait de créer des méthodes différentes avec le même nom. Java fait la différence au moment de regarder les types d’input et leur ordre, ce qui s’appelle la “signature” de la méthode.

S’ils existent deux méthodes avec le même nom, les mêmes types d’inputs et dans le même ordre, Java va planter. L’ensemble de noms, types d’input et leur ordre est la *signature* de la méthode.

```java
class Test {
	public static void main(String[] args) {
		Cercle c1 = new Cercle();
		Cercle c2 = new Cercle(4);
		Cercle c3 = new Cercle(new Point(1,2));
		Cercle c4 = new Cercle(new Point(1,2),3);
	}
}

class Cercle {

	Point centre;
	int rayon;

	Cercle() {
	// sans paramètres, on retourne un cercle centré en 0,0 et de rayon 1
		centre=new Point(0,0);
		rayon=1;
	}
	Cercle(int r) {
	// si le param. est un int, on suppose que c'est le rayon
		centre=new Point(0,0);
		rayon=r;
	}

	Cercle(Point c) {
	// si le param est un objet de type Point, on suppose que c'est le centre
		centre=c;
		rayon=1;
	}

	Cercle(Point c, int r) {
	// si on donne un Point et un int,
	// on suppose le centre et le rayon,  dans cet ordre!!!

		centre=c;
		rayon=r;
	}

	double aire() {
		return Math.PI*rayon*rayon;
	}
}
```

## Mot clé `this`

Cette mot clé à 3 utilisations. Dans le code du début de la section “initialisation d’objets”, on a déjà vu une utilisation du mot clés `this` : pour lever les ambiguïtés de deux paramètres sous le même nom. `this`, plus formellement, appelle la classe où on se trouve.

On peut l’utiliser aussi pour passer comme paramètre une instance de la classe actuelle.

```java
class ZoneDessin {
	...
	void dessiner(Point p) { // méthode pour dessiner un point sur la zone
		...
	}
	...
}

class Point {
	...
	void dessinerSur(ZoneDessin d) {
				d.dessiner(this) ; // méthode pour qu'un objet Point
													 // appelle la méthode de la ZoneDessin
	 }
	 ...
}
```

En plus, on peut l’utiliser pour appeler un constructeur dans un autre constructeur. Quelques conditions si on le fait : on doit utiliser `this` seulement dans le constructeurs et pas dans d’autre méthodes, et **il doit être la première instruction**.

```java
class Point {
	double x;
	double y;

	Point(double x, double y) {
		this.x=x;
		this.y=y;
	}

	Point() {
		this(0.0,0.0); // appelle le constructeur Point
									 // avec deux paramètres
	}

}
```

# Organisation du code en package

## *Encapsulation* et contrôle d'accès

![Notion d’encapsulation.](new/uga/l2/s3/info/s3_info_programmation_par_objets/05_constructeurs_packages_et_modificateurs_d’acce/untitled.png)

Notion d’encapsulation.

La programmation par objets met l'accent sur la réutilisation du code par d'autre programmeurs. On distingue donc le créateur d’une classe et son utilisateur.

Le créateur d’une classe voudrait contrôler l’accès aux attributs (pour maintenir les valeurs prédéfinies) et aux méthodes (car celles qui existent ne sont pas définis pour l’utilisateur mais pour le même créateur de la classe, il n’y a pas donc besoin de les appeler dehors de l’objet).

Java permet de modifier la “visibilité” des attributs et méthodes avec le mot clés `private`, `protected`, *(rien)* et `public`. En plus, Java permet d’organiser les classes en *packages* ou paquets, qui son un ensemble de classes rangées dans un même espace de noms.

On peut appliquer aussi les modificateurs sur les classes. Normalement on utilise que `public` et rien. `public` pour pouvoir accéder à la classe partout, et (rien) pour qu’elle soit accessible par les autres fichiers dans le même dossier/package de la classe. On peut “imbriquer” de packages. Par fichier Java, on peut avoir plusieurs classes mais seulement une seule classe publique, et elle doit avoir le même nom du fichier Java où elle est écrite.

# Modificateurs d’accès

## Restriction des méthodes

Ils peuvent être places devant une déclaration de classe, méthode ou d’attribut (d’instance ou de classe).

![untitled](new/uga/l2/s3/info/s3_info_programmation_par_objets/05_constructeurs_packages_et_modificateurs_d’acce/untitled_1.png)

Principes pour choisir un modificateur :

- Quand on a le choix, ce serait le mieux de choisir le modificateur le plus restrictif.
- Éviter d'utiliser public sur les attributs (sauf pour les constantes globaux).
Pour donner un accès en lecture ou modification, on les fait avec des méthodes. C’est qui s’appelle l’encapsulation.
- Les membres publics définissent l'interface exposée de la classe. Les modifier pourrait entraîner d’erreurs de compilation.
- On ne peut avoir qu'une classe publique par fichier .java.

# Chaînes de caractères en Java

## La classe `String` et `StringBuffer`

Il existe plusieurs classes en Java permettant de créer et manipuler des chaînes de caractères. Les deux classes principalement utilisées sont :

- la classe `String` admet des instances immuables,
- la classe `StringBuffer` admet des instances dont on peut changer les valeurs.

On verra que `StringBuffer` a plus de fonctionnalité que `String`.

## `StringBuffer` : constructeur, variables et méthodes

### Constructeurs

- `StringBuffer(String s)` : permet d'obtenir une chaîne avec les mêmes caractères
que `s`.
- `StringBuffer(int c)` : permet d'obtenir une chaîne vide de capacité c.
- `StringBuffer()` : permet d'obtenir une chaîne vide de capacité 16.

### Méthodes générales

- `int length()` : retourne comme la longueur (nombre de caractères) de la chaîne.
- `int capacity()` : retourne la capacité de `this`, l’objet ou instance courante.

### Méthodes de concaténation (à la fin)

- `StringBuffer append(String s)` : ajoute en fin de chaîne les caractères de `s`. Modifie
`this` et le retourne en résultat (permet l'activation de méthodes en cascade).
- `StringBuffer append(int i)` : ajoute en fin de chaîne i converti en chaîne. Modifie
`this` et le retourne en résultat.
- Il existe de nombreuses autres signatures pour `append`.

### Méthodes de caractère et sous-chaîne

- `char charAt(int i)` : retourne le caractère d'indice i dans la chaîne.
- `String substring(int i)` : retourne le suffixe de la chaîne à partir de l'indice i.
- `String substring(int i, int j)` : retourne la sous-chaîne de longueur `j - i` commençant à l'indice `i`.
- Ces méthodes sont susceptibles de lever une `StringIndexOutOfBoundsException`.

### Méthodes de suppression

- `StringBuffer delete(int i, int j)` : supprime les caractères d'indices `i` à `j – 1`. Modifie `this` et le retourne.
- `StringBuffer deleteCharAt(int i)` : supprime le caractère d'indice i. Modifie `this` et le retourne en résultat.

### Méthodes d’insertion

- `StringBuffer insert(int i, String s)` : insère `s` à l'indice `i`. Modifie `this` et le retourne.
- `StringBuffer insert(int i, char c)` : insère `c` à l'indice `i`. Modifie `this` et le retourne en résultat.
- Il existe de nombreuses autres signatures pour `insert`.

### Méthodes de remplacement

- `StringBuffer replace(int i, int j, String s)` : remplace les caractères d'indices `i` (inclus) à `j` (exclus) par tous ceux de `s`. Modifie `this` et le retourne.
- `void setCharAt(int i, char c)` : remplace le caractère d'indice `i` par `c`.

### Méthodes de conversion à `String`

- `String toString()` : retourne une `String` contenant les mêmes caractères que `this`.
- La conversion inverse se fait par le constructeur `StringBuffer(String s)`.