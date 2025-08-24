## 02 // héritage

[INFF5_2.pdf](ressources/02_heritage_inff5_2.pdf)

## Composition, délégation et héritage

### Types de réutilisation de code

Java offre deux moyens pour réutiliser le code de classes existantes : la composition et l’héritage.

- Composition : on crée des instances de classes existantes dans des nouvelles classes.
- Héritage : on crée des classes qui reprennent le type d’une classe existante et on ajoute des fonctionnalités (sans modifier) le code existant.

En plus, on pourrait ajouter un autre moyen :

- Délégation : dans un objet de type A, on crée un objet de type B avec un méthode de A qui appelle une méthode de B. Ceci est pour simuler l’héritage juste d’une méthode de l’objet de type B à la fois de tout en hériter.

### Plus sur l’héritage

#### Contenu utile du cours #1 : réutilisation de classes et sous-classes

Réutiliser des instructions est l’un des points forts de programmer.

- **Réutilisation de l’implémentation** : utiliser une instance d’une classe dans une autre classe.
- **Réutilisation de l’interface et polymorphisme** : recycler les méthodes d’une classe dans une autre sous-classe, ou on ajoute des nouvelles fonctions/méthodes.
Le *polymorphisme* est juste le principe d’utiliser un programme sur n’importe quel sous-type d’objet ou la “forme” ou “morphisme” de l’objet original (FormeGeo).

![untitled](ressources/01_objets_et_classes_untitled.png)

```java

// Par exemple, une fonction qui prends comme argument un objet FormeGeo f, peut prendre un objet de type Cercle ou Triangle.

void dessineEtAfficheAire(FormeGeo f) {
	f.dessine();
	System.out.println("aire"+f.aire());
}
```

Une sous-classe, c’est effectivement une classe dans une autre. Précisément, c’est une classe qui ***hérite*** les attributs et méthodes d’une autre classe, comme ça il n’y a pas besoin de les redéfinir.

Par exemple, si on a une classe comme la classe “Ford”, une sous-classe pourrait être “Mustang”.

### Composition et héritage sur Java

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

#### Contenu de ce cours

L'héritage est un des principaux concepts de la programmation par objet. En Java, on utilise toujours l'héritage lorsque l'on créé une classe, car toute classe est héritée de la classe plus général `Object`, qui contient aussi les méthodes `toString()`, `equals()`, etc.

Si on veut créer une classe enfant d’une classe parent différent de `Object`, on utilise le mot clé `extends`.

Dans l’héritage on peut ajouter des nouveaux membres, mais aussi redéfinir ceux qui existaient avant. Cela dit, redéfinir d’attributs n’est pas exactement utile, on va plutôt redéfinir de méthodes. On peut aussi surcharger les méthodes de la super-classe originale.

## Les super-classes

### `super` : appeler le constructeur d’une super-classe

La première instruction d'un constructeur est toujours l'appel d'un constructeur de la super-classe en utilisant la syntaxe `super(…)`, ou l'appel d'un autre constructeur de la classe en utilisant la syntaxe `this(…)`.

Si rien n'est indiqué, le compilateur Java considère par défaut un appel au constructeur sans paramètre de la super-classe, soit `super()`.

```java
public class A {
	protected int a;
	
	// rédefinition du constructeur par défaut de A
	// donc le constructeur par défaut A() n'existe plus !

	public A(int val) { 
		a = val;
	}
}

public class B extends A {
	public B(int val) {
		a = val;  // rien n'est indiqué si d'appeler this ou super
							// dans ce constructeur, donc on appele super
							// mais on a rédifini le constructeur par défaut de A
	}
}
```

À l'instanciation d'une classe, l'initialisation de la partie héritée de l'instance doit être effectuée avant celle de la partie localement définie. Un constructeur de la super-classe doit donc toujours être exécuté avant l'exécution d'un constructeur de la classe. Les constructeurs sont donc exécutés dans l'ordre des classes les plus générales aux plus spécifiques.

### Pseudo-variables

Il existe deux pseudo-variables que l'on peut utiliser dans les méthodes d'une classe :

- `this` référence l'instance courante
- `super` référence l'instance courante limitée à sa partie héritée

Elle sont appelées pseudo-variables car leur valeur change selon le contexte, on ne peut pas modifier leur valeur explicitement.

### `Object` : la classe mère des toutes les autres

`Object` est la racine de la hiérarchie d'héritage en Java : toute classe hérite (directement ou indirectement) de `Object`.

`Object` détient des définitions de méthodes exécutables sur tout objet Java, notamment :

- `public boolean equals(Object obj)`
- `public String toString()`
- `public Class getClass()`

### `instanceof` : vérifie l’héritage entre deux classes

L'opérateur `instanceof` permet de savoir si une référence possède un type donné.

```java
Object obj = new Point3D();
Point p = new Point();
System.out.println(obj instanceof Point); // affiche true
System.out.println(obj instanceof Object); // true
System.out.println(obj instanceof Point3D); // true
System.out.println(obj instanceof String); // false
System.out.println(p instanceof Point3D); // false
System.out.println(p instanceof String); // Erreur
```

## Polymorphisme

### Type de la référence et type réel, liaison dynamique

Les références (noms de variables) ont un type, et l’objet référencé a un type aussi. Avec l’héritage, on peut avoir un type différent pour chaque.

```java
class Point{
	private double x;
	private double y;

	void truc(){
		System.out.println("méthode de Point");
}

class Point3D extends Point{
	private double z;

		void truc(){
		System.out.println("méthode de Point3D");
}

public static void main(String[] args){
	Point p = new Point3D();
	p.truc();
}

---

// "méthode de Point3D"
```

Si jamais on appelle une méthode de `p` de type super-classe `Point`, on va aller exécuter celle référencée par `Point3D`. Cela cause des différences si on l’a redéfinie dans la sous-classe, comme vu dans l’exemple précédent.

**Si la méthode appelée existe dans la sous-classe mais pas dans la super-classe, Java va planter. Ça implique aussi le constructeur !!!!!!!**

Une autre chose : **le cast ne transforme pas le type d’un objet**. Le cast est juste une indication au compilateur de “voir” l’objet comme le type casté. Notons que si on décide de voir un point `p` comme un `Point3D` ça pose pas de problème jusqu’à qu’on veut accéder au point `z` (parce que ce point n’existe pas, on n’a jamais appelé le constructeur pour initialiser le point `z`).

```java
class Test {
	public static void main(String[] args){
		Point p = new Point;
		Point3D p3D = new Point3D;
		
		p = p3D;
		p3D = p; // erreur
		p3D = (Point3D) p;
		System.out.println(p3D.z); // erreur : ClassCastException
	}
}
```

Finalement, le mot-clé `instanceof` va planter si on demande la relation entre deux classes qui n’ont pas une relation d’héritage comme père-fils, grandpère-grandfils, etc., mais plutôt de “frères”.

```java
class Test {
	public static void main(String[] args){

		Point obj = new Point();
		Point3D p3D = new Point3D();
		boolean a = obj instanceof Object; // true
		boolean b = obj instanceof Point3D; //false, c'est l'inverse
		boolean c = p3D instanceof String; // erreur, pas d'héritage,
		// ils sont de classes parallèles, de "frères"

	}
}
```

### Transtypage descendant

La transtypage ascendant est la situation ou le fils hérite le type de son père. Le transtypage descendant est un peu pareil : on force un père d’avoir le même type que son fils.

Cela seulement marche si deux classes, père et fils, sont en hiérarchie directe (fils, père, grand-père, etc.). Ça ne marche pas avec des “oncles” ou des “frères”, càd. deux classes qui n’ont pas une hiérarchie directe.

```java
class Point {
	private double x;
	private double y;
	public double getAbscisse() {
		return x;
	}
	public double getOrdonnee() {
		return y;
	}
	public boolean equals(Object o) {
		if (o instanceof Point) {

			// warning, ici on peut planter si o pas instance de point
			// mais pas de probleme car le if s'occupe du pire cas
			Point p = (Point) o; 

			return p.x==x && p.y==y;
		}
	return false;
	}
}
```

## Classes abstraites et finales

### `abstract` : des catégories trop générales

Pour rappeler, l’héritage nous permet de factoriser le code (sortir les parties “communes” des termes ou des éléments. Les éléments sont des classes, dans ce cas).

Quand on pense à plusieurs “choses” (classes), si on essaie de les regrouper dans une catégorie (super-classe), parfois cette super-classe peut être trop abstraite. Si on essaie de trouver les aspects en commun des classes pour les regrouper dans une super-classe, essayer de définir des méthodes communes est presque impossible.

```java
abstract class Forme {
	abstract public double aire() {
		//
	}
}

class Rectangle extends Forme {
	private int largeur;
	private int hauteur;
	public double aire() {
		return largeur*hauteur;
	}
}

class Cercle extends Forme {
	private int rayon;
	public double aire() {
		return Math.PI*rayon*rayon;
	}
}

class Dessin {
	private Forme[] formes;
	public double aireTotale() {
		double total=0;
		for (Forme f : formes) {
			total+=f.aire();
		}
		return total;
	}
}
```

Si une classe contient une méthode abstraite, la classe est automatiquement abstraite aussi. Par contre, une classe abstraite peut contenir une méthode concrète non-abstraite.

Ici, la classe `Forme` est trop abstraite, jusqu’au point que définir la méthode `aire()` est impossible. C’est ici ou on utilise le mot clé `abstract` pour les classes et méthodes. Pour les attributs, on les définis comme un méthode qui contient un calcul.

Les classes abstraite ne peuvent pas être instanciées. Les méthodes abstraites n’ont pas du contenu dedans, elles sont vides. Une classe qui possède au moins une méthode abstraite doit être déclaré abstraite.

### `final` : attribut ou méthode *immodifiable*

Il marche similairement aux modificateurs d’accès, et on peut l’utiliser avec des classes, attributs et méthodes. En général, il veut dire “cela ne peut pas être changé”.

Avec les attributs, normalement on les utilise avec les attributs qui sont aussi `static`, càd., qui sont des “constantes globales” parmi les objets d’une certaine classe ; mais on peut utiliser `final` tout seul aussi. Quand on utilise ce dernier, on ne peut pas changer la référence du nom d’attribut, mais effectivement on peut changer internement l’attribut.

```java
public classe CompteEuro {
	private final Personne titulaire; // la référence "titulaire" pointe
																		// définitivement à cet objet Personne
	private final String titulaire;   // erreur !
	titulaire.deposer(100);           // on change internement l'objet Personne
}
```

Une méthode `final` ne peut plus être redéfinie dans les sous-classes.

Une classe `final` ne peut pas être étendue, càd. on n’en peut pas hériter. Puisque on n’en peut pas hériter, toutes ses méthodes sont implicitement final aussi.

En règle générale, il faut avoir de bonnes raisons de déclarer des méthodes ou classes finales, car on ne peut rien changer après.
