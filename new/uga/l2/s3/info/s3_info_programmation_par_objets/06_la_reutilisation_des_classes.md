# 06 // la réutilisation des classes

[Slides de cours 6.pdf](inff3-2223-cours6.pdf)

# Composition, délégation et héritage

## Types de réutilisation de code

Java offre deux moyens pour réutiliser le code de classes existantes : la composition et l’héritage.

- Composition : on crée des instances de classes existantes dans des nouvelles classes.
- Héritage : on crée des classes qui reprennent le type d’une classe existante et on ajoute des fonctionnalités (sans modifier) le code existant.

En plus, on pourrait ajouter un autre moyen :

- Délégation : dans un objet de type A, on crée un objet de type B avec un méthode de A qui appelle une méthode de B. Ceci est pour simuler l’héritage juste d’une méthode de l’objet de type B à la fois de tout en hériter.

## Plus sur l’héritage

### Contenu utile du cours #1 : réutilisation de classes et sous-classes

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

### Contenu de ce cours

L'héritage est un des principaux concepts de la programmation par objet. En Java, on utilise toujours l'héritage lorsque l'on créé une classe, car toute classe est héritée de la classe plus général `Object`, qui contient aussi les méthodes `toString()`, `equals()`, etc.

Si on veut créer une classe enfant d’une classe parent différent de `Object`, on utilise le mot clé `extends`.

Dans l’héritage on peut ajouter des nouveaux membres, mais aussi redéfinir ceux qui existaient avant. Cela dit, redéfinir d’attributs n’est pas exactement utile, on va plutôt redéfinir de méthodes. On peut aussi surcharger les méthodes de la super-classe originale.

# Surcharge et redéfinition

## Leur différence

Notons qu’’il y a une différence entre la surcharge et redéfinition. Dans la surcharge, deux fonctions avec le même nom coexistent et se différencient par leur signatures.

### Initialisation dans la super-classe

Quand on instancie une super-classe, on appel le constructeur de sa super-classe avant d’appeler celui de la sous-classe. Cela peut s’enchaîner jusqu’à arriver à la super-classe mère `Object` dont son constructeur ne fait rien de spécial.

```jsx
class A {
	public A() {
		System.out.println("Dans le constructeur de A");
	}
}

class B extends A {
	public B() {
		System.out.println("Dans le constructeur de B");
	}
}

public class TestConstructeursEtHeritage {
	public static void main(String[] args) {
		B b = new B();
	}
}

-----

// Dans le constructeur de A
// Dans le constructeur de B
```

On peut aussi appeler des constructeur avec paramètres, de la même manière qu’on le fait pour la classe actuelle avec le mot clé `this`, mais dans ce cas on le fais avec le mot clé `super`. **Il doit être forcément la première instruction de la méthode**. `super` sert aussi pour acceder aux attributs et méthodes de la super-classe, mais il n’est pas nécessaire.

```jsx
class Personne {
	private String prenom;
	private String nom;
	public Personne(String p , String n) {
		nom=n;
		prenom=p;
	}
}

class Etudiant extends Personne {
	private double motivation;

	public Etudiant(String p, String n, double motiv) {
		super(p, n); // ici on appele le constructeur de la super-classe
		motivation=motiv;
	}

	public boolean seLeverPourAllerEnCours() {
		return Math.random()<motivation;
	}
}
```

## La délégation (”transmission”)

Parfois, on veut juste créer une classe qui hérite une ou quelques méthodes de la superclasse, et non toutes. La délégation est à mi-chemin de l’héritage et la composition, et elle tombe bien pour ce type de tâches.

```java
class RealPrinter {
    // the "delegate"
    void print()
    {
        System.out.println("The Delegate");
    }
}
 
class Printer {
    // the "delegator"
    RealPrinter p = new RealPrinter();
 
    // create the delegate
    void print()
    {
        p.print(); // delegation
    }
}
 
public class Tester {
 
    // To the outside world it looks like Printer actually prints.
public static void main(String[] args)
    {
        Printer printer = new Printer();
        printer.print();
    }
}
```

Basiquement, on commence avec deux classes A et B et on déclare un objet de A dans la classe B. Pour “hériter” de méthodes de A dans B, on crée de fonctions dans classe B qui appellent, à travers l’objet A, les méthodes de la classe A.

**La délégation est une relation d’*instantiation*, pas de *composition*, de deux classes !** (un objet `RealPrinter` instance dans une classe `Printer`). 

## Le modificateur `protected`

Le modificateur d’accès `protected` donne l’accès aux sous-classes et aux classes du même package. On les utilise principalement avec les méthodes : on définit des variables `private` dans une superclasse, et on y accès dans les sous-classes avec une méthode `protected`. 

# Transtypage ascendant

## Héritage de typage

L'aspect le plus important de l'héritage est la relation de typage : si A `extends` B alors toute instance de A possède également le type B.

Si une méthode ne prend que des paramètres de type A, on peut le passer un paramètre de type B. Par contre, le contraire ne marche pas.

## Composition, délégation ou héritage ?

- Composition : référence vers un objet dans une classe. Déclaration d’une classe dans une autre *sans l’instancier* !
- Délégation : **instanciation**, et on crée une méthode de classe courante qui appelle méthode de la classe instanciée.
- Héritage : importation du type, attributs et méthodes d’une classe à une autre.

L’héritage est à utiliser avec parcimonie ! La plupart du temps, on utilise la composition et on délègue certaines méthodes.

Pour décider, il faut se poser la question : 

- Ai-je besoin d'utiliser le **transtypage ascendant** ?
- Cela va t-il me permettre de factoriser du code ?