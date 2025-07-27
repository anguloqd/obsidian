# 07 // un pas de plus vers l’abstraction

[Slides de cours 7.pdf](ressources/07_un_pas_de_plus_vers_l’abstraction_inff3-2223-cours7.pdf)

# Le mot-clé `final`

## `final` : attribut ou méthode *immodifiable*

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

# Polymorphisme

Après le notions de classes et d'héritage, le polymorphisme est la plus importante notion. Le polymorphisme est la capacité d'un code à être utilisé avec différents types, conséquence de l’héritage.

## Type de la référence et type réel, liaison dynamique

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

## Transtypage descendant

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

# Classes et méthodes abstraites

## `abstract` : des catégories trop générales

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

# Interfaces

## `interface` : une sorte de classe que de méthodes/constantes

Pensons à la notion de “héritage multiple”. Imaginons deux classes A et B avec une seule méthode truc(), et maintenant C va hériter (`extends`) au même temps de A et B, mais lequel méthode ? truc() de A ou truc() de B ? C’est pour ça que l’héritage multiple n’existe pas.

Pour une abstraction plus grande, et pour simuler l’héritage multiple, il existe la notion d’interface : on défini les signatures de méthodes et des constantes.

Une interface est une **classe abstraite** (collection d’attributs `static final` et signatures de méthodes sans corps) qu’on ajoute à une autre classe. Il peut être vue comme un type aussi, et la classe à la quelle l'interface est ajoutée prend aussi le type de l’interface.

```java
abstract class Animal {
	abstract void crier();
}

interface Compagnon {
	void jouer();
	void faireDesCalins();
}

// on étend Animal et on implemente Compagnon

class Chat extends Animal implements Compagnon {
 void crier() {
	 System.out.println("Miaou");
 }
 void faireDesCalins() {
	 // ...
 }
 void jouer() {
	 // ...
 }
}

class Chien extends Animal implements Compagnon {
 void crier() {
	 System.out.println("Whouaf");
 }
 void faireDesCalins() {
	 // ...
 }
 void jouer() {
	 // ...
 }
}

// on crée une personne

class Personne {
	Compagnon[] mesCompagnons; // ici, "Compagnon" est utilisé comme un type
	
	void quandOnSEnnuie() {
		for (Compagnon c : mesCompagnons) {
		c.jouer();
		}
	}
}
```

## Généralités sur les interfaces et les classes abstraites

Une interface peut seulement contenir des signatures de méthodes (**pas de corps ni de constructeurs**) et, plus rarement, des constantes (attributs **forcément déclarés `static final`**).

Les interfaces aussi peuvent hériter d’autres interfaces, mais pas d’autre classes. Similairement, l’héritage faite par une interface peut être multiple, et l’implémentation d’une classe faite par une classe aussi peut être multiple.

L’héritage “multiple” est seulement permis entre les interfaces !

```java
interface A {
	void m1();
}

interface B {
	void m2();
}

interface C extends A,B { // héritage multiple, seulement pour interfaces
	void m3();
}

class M implements A, B { // implementation multiple

	public void m2() {
	// corps de méthode
	}

	public void m1() {
	// corps de méthode
	}

}
```

Il faudrait mentionner quelques faits par rapport aux interfaces contres les classes abstraites :

- Dans une interface, toutes les méthodes sont abstraites.
- Une interface ne peut pas détenir d'attributs d'instances.
- Une interface n'a pas de constructeur.
- Une interface peut être implémentée par une ou plusieurs classes.
- Une interface ne peut pas hériter d'une classe.

## Types d’interfaces

Ils existent deux utilisations des interfaces :

- Interfaces classiques : vraiment ajoutent la signature des méthodes, comme `Comparable` (qui ajoute la signature de `.compareTo()`).
- Interfaces de “balisage” : sont des interface vide qui juste indique à travers leurs noms et leurs type hérités une propriété des classes qui l’implémentent, comme `Cloneable` (qui indique qu’il est légal d’utiliser `.clone()` avec telle classe),

# Sur l’abstraction et l’implémentation...

## “Non finies”

Les classes abstraites et interfaces sont “non-finies”. Si on déclare une classe “finie” il faut que les méthodes des abstraites et interfaces soient définitivement définis !!