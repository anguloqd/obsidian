# 01 // introduction à la programmation par objets

[Slides de cours 1](inff3-2223-cours1.pdf)

# Programmes, langages de programmation et paradigmes

## Types de programmation et ses étapes

Un ***programme informatique*** est une séquence d'instructions qui spécifie étape par étape les opérations à effectuer pour obtenir un résultat.

Paradigmes de la programmation : impérative et déclarative.

- **Impérative**. Séquence d’instructions permettant de modifier l’état de la mémoire.
- **Déclarative**. Exprime la logique de contrôle sans utiliser une structure de contrôle.
    - **Fonctionnelle**. Basée sur l’évaluation de fonctions.
    - **Logique**. Basée sur des faits et règles de dérivation.

Dans ce cours, on s’intéresse à la programmation impérative. Ils existent 4 types d’instructions possibles :

- **Assignation**.
- **Branchement conditionnel** : instructions à réaliser si une condition est vérifiée.
- **Branchement inconditionnel** : appel d’instructions qui se trouve `un autre endroit du programme (une fonction définie avant, par exemple).
- **Boucles** : répétitions d’instructions jusqu’à vérifier une condition.

Pour créer un programme, on passe par quatre étapes :

1. Analyse et conception du programme. Penser aux données et algorithmes.
2. Codage.
3. Transformation du code source à code machine (compilation et interprétation).
4. Test et validation du programme.

**Extra** : l’ordinateur est composé de processeur et mémoire. le processeur exécute le programme, la mémoire stocke les données.

# Introduction des concepts de la programmation par objets

## Les classes et les objets : un cas des classes

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

# Cycle de vie des variables et stratégies de la gestion de mémoire

## Allocation statique

Se fait avant de l’exécution (à la compilation).
Au lancement du programme, le système réserve tout l’espace dont le programme aura besoin.
Il n’y a pas d’allocation de mémoire supplémentaire pendant l’exécution.
La mémoire est libérée à la fin du programme.

Elle va bien et vite  si on sait exactement la quantité de mémoire dont on aura besoin, sinon il se peut que l’espace alloué soit pas suffisant.

## Allocation dynamique sur la pile

Seulement la mémoire nécessaire à une procédure (ou fonction) est allouée lors de son exécution.
Les variables définies dans la procédure (bloc de code) sont allouées lors de l’entrée et libérées automatiquement à la sortie.

## Allocation dynamique sur le tas, utilisé par Java

La mémoire est allouée et désallouée au besoin au fur et à mesure du programme dans un pool de mémoire
C'est plus flexible, car on a pas besoin de savoir le # d’objets, leur type, etc.
A besoin de plus de ressources et de temps pour allouer de la mémoire.
Le programmeur doit libérer de la mémoire par un objet qui n’est plus utilisé (automatique avec le ramasse-miettes).

Java utilise principalement une **allocation dynamique sur le tas** pour les objets et dispose d'un ramasse-miette (Garbage Collector). Le programmeur n'a pas à se soucier de la libération de la mémoire.

À chaque fois que le programmeur veut créer un objet, il utilise le mot clé `new` pour allouer la mémoire.

# Traitement des erreurs

## “Si le programme plante, alors on prend une autre action”

L'exécution d'un programme peut générer des “erreurs”, comme division par 0 ou mémoire insuffisante.

Les types d’erreurs sont des syntaxes (pas possible de compiler ou exécuter), exécution (se plante lors de l’exécution) et sémantique (le script marche mais ne fait pas ce qu’on veut faire).

Java permet de gérer ces erreurs avec les objets `Exceptions`, qui son *lancés* de l’endroit où l’erreur s’est produite et *attrapés* par un intercepteur d’exception (comme si c’était du baseball).

Ceci permet d’écrire un code plus clair (la gestion d’exceptions est séparée du code “normal”) et est plus sûr.