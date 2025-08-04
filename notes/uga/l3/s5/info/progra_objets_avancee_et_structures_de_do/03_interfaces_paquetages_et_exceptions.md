# 03 // interfaces, paquetages et exceptions

[INFF5_3.pdf](ressources/03_interfaces_paquetages_et_exceptions_inff5_3.pdf)

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

## Interfaces prédéfinies en Java

La première interface prédéfinie en Java est `Cloneable`. Sa définition est littéralement vide.

```java
public interface Cloneable {
}
```

L’intérêt de l’utiliser n’est pas de acquérir des méthodes, **mais d’acquérir le type** `Cloneable`. Il existe une fonction dans la classe mère `Object` appelé `.clone()`, utilisé pour cloner des objets. Si l’objet qu’on tente de cloner ne possède pas le type `Cloneable`, Java leve l’exception `CloneNotSupportedException`.

La deuxième interface prédéfinie de Java est `Comparable`. Sa définition inclut une seule méthode.

```java
public interface Comparable {
		public int compareTo(Object obj);
	}
```

Le type Comparable et la méthode `.compareTo(…)` sont les deux d’intérêt. Plusieurs d’autres méthodes se servent du type. Par exemple, la classe `Arrays` possède une méthode `.sort(Object[] t)` pour ordonner les objets d’une liste en ordre croissant, d’où le besoin de *comparer* et le type `Comparable`.

# Paquetages

## Espaces de noms et les *packages*

Les espaces de noms est une notion abstraite. Ils permet de regrouper des *choses* de la même *famille* et de lever les ambiguïtés de noms. **On pourrait les voir comme des dossiers**. 

Par exemple, le nom de famille est un espace de noms (donc ils ont tous une caractéristique commune : le nom de famille) permettant de discriminer les personnes ayant le même prénom (donc ils ont tous un caractéristique différente : le prénom).

Les packages sont finalement un regroupement sous le même espace de noms. `java.util` est un package ou **famille d’outils** qui contient les **intégrants de la famille** `Arrays`, `ArrayList`, `GregorianCalendar`, `Currency`, etc. Pour utiliser les packages, il y a deux manières :

```java
// on utilise son nom complet, càd., "nomDeFamille.Prénom"

class Test {
 public static void main(String[] args) {
	 java.util.ArrayList tab = new java.util.ArrayList();
 }
}

```

```java
// on importe la classe, puis on utilise son "prénom" ou nom simple

import java.util.ArrayList;
class Test {
 public static void main(String[] args) {
	 ArrayList tab = new ArrayList();
 }
}
```

Pour organiser les classes en package, on crée un dossier dans le dossier src qui aurait le nom du package, puis chaque fichier .java du dossier doit avoir en premier ligne un déclaration d’appartenance au package, **en plus d’être forcément `public`**, comme suite :

```java
package fr.upmf.miashs.inff3;
**public** class UneClasse {
}
```

C’est qui signifie que dans le dossier src, il y a un dossier “fr”, puis un dossier “upmf”, puis un dossier “miashs”, puis un dossier “inff3” où il y a finalement notre fichier `UneClasse`.

![untitled](ressources/05_flux_et_fichiers_untitled_2.png)

![untitled](ressources/05_flux_et_fichiers_untitled_3.png)

Par convention, les packages ne sont nommés qu’avec des lettres minuscules.
S’il y a deux classes dans le dossier src avec le même nom, et si elles appartiennent à deux paquets différents, il faut utiliser leur noms complets pour les importer. Si elles appartiennent au même paquet, on ne peut qu’utiliser l’une des deux classes dans le même projet.

## Paquetages, classes et espace disque

- Pour tout paquetage, il doit exister un répertoire de même nom sur le disque.
- Le répertoire correspondant à un sous-paquetage doit être un sous-répertoire dans le répertoire correspondant au paquetage englobant.
- Une classe `C` est définie dans un fichier C.java qui doit se trouver dans le répertoire qui correspond à son paquetage.

Par exemple, la classe `miashs.fractions.Fraction` doit être définie dans un fichier Fraction.java se trouvant dans un répertoire `fractions`, se trouvant dans un répertoire `miashs`.

## Directives `import`

Une directive import dans un fichier .java permet d'utiliser les éléments importés en les désignant par leur « nom court ». Par exemple, `import java.util.Scanner` permet d'utiliser la classe `Scanner` sans la désigner par `java.util.Scanner`.

### Le symbole `*`

On peut utiliser `*` pour importer toutes les classes d'un paquetage. Par exemple, `import java.util.*` permet d'utiliser en les désignant par leur nom court la classe `Scanner`, la classe `Arrays`, etc.

**L'utilisation de `*` ne permet pas d'importer les sous-paquetages**. Par exemple, `import java.util.*` importe toutes les classes de `java.util` mais pas celles du paquetage `java.util.regex`.

Il ne peut pas y avoir d'ambiguïté dans les importations (le compilateur veille). Par exemple, `import java.util.*` et `import java.sql.*` nécessite de désigner d'utiliser la classe `Date` en la désignant par `java.util.Date` ou `java.sql.Date`.

# Exceptions

## Erreurs et la solution

Une exception est une sorte de “condition exceptionnelle” : un problème qui empêche la continuation de la méthode ou du bloc courant, car l'on ne dispose pas d'information suffisante dans le contexte courant pour traiter ce problème. La solution à ces exceptions est de reléguer le problème au “niveau supérieur”, i.e. le bloc appelant.

**Note contextuelle**. L’ensemble d’erreurs qu’une méthode pourrait lever est dit ses “*throws*”.

## Les exceptions comme des objets

Établissons nos classes d’exemple :

```java
class Parachute {
	public void ouvrir() {}
}

class Parapentiste {

	private Parachute parachute;

	public void ajouterParachute(Parachute p) {
		parachute=p;
	}

	public void sauter() {
		
		if (parachute==null) {
			throw new RuntimeException("Aie !!!"); // <--------- exception
		}

		parachute.ouvrir();
	}

}

class Concours{
	public void parade(Parapentiste[] participants) {
		for (Parapentiste p : participants) {
			p.sauter();
		}
	}
}
```

En Java, les exceptions sont des objets qui se manipulent avec deux mots clés :

- `throw` : on “lève” une `Exception` ou condition exceptionnelle à la méthode appelante.
- `catch` : on fourni des instructions “correctives” suite à la levée d’un erreur ou `Exception`.

Une exception est interceptée (abordée) ou pas interceptée. Si elle n’est jamais interceptée, elle montre l’erreur sur la console qui est indiqué par le mot-clé `throw`. Si elle est interceptée, elle fait tout ce qu’indique la clause `catch` et essaie de continuer avec le programme.

La méthode qui contient le `throw` enverra ou “propagera” ce message à toutes les méthodes qui l’avaient appelé avant tant qu’elle n’est pas interceptée. C’est le principe de la patate chaude. Si la propagation de l’exception arrive à la méthode main, la trace de la pile des appels (i.e. ordre d’appel de méthodes) est affiché et le programme s’arrête. 

```java
public class IntroExceptions {
	public static void main(String[] args) {

		Parapentiste casseCou = new Parapentiste();
		Parapentiste inconscient = new Parapentiste();
		Parapentiste prevoyant = new Parapentiste();
		Parapentiste[] participants = new Parapentiste[] {prevoyant,casseCou,inconscient};
		Concours c = new Concours();

		c.parade(participants);
	}
}

---

/*
Exception in thread "main" java.lang.RuntimeException: Aie !!!
at cours9.Parapentiste.sauter(IntroExceptions.java:60)
at cours9.CoupeIcare.parade(IntroExceptions.java:70)
at cours9.IntroExceptions.main(IntroExceptions.java:85)
*/
```

## Interception d’exceptions

Pour intercepter cet exception, on utilise un bloc `try-catch`.

```java
public class IntroExceptions {
	public static void main(String[] args) {

		Parapentiste casseCou = new Parapentiste();
		Parapentiste inconscient = new Parapentiste();
		Parapentiste prevoyant = new Parapentiste();
		Parapentiste[] participants = new Parapentiste[] {prevoyant,casseCou,inconscient};
		Concours c = new Concours();
		
		try {
			c.parade(participants);
		}

		catch (RuntimeException e) {
			System.err.println("Il faut appeler les secours !");
		}

	}
}

---

// Il faut appeler les secours !
```

On peut ajouter plusieurs `catch` à un seule bloc `try`. Le bloc `finally` toujours s’exécute.

```java
try {
// code susceptible de lever une exception
}
catch (TypeException1 e1) {
// code permettant de traiter une exception
// du type Exception1
}
catch (TypeException2 e2) {
// code permettant de traiter une exception
// du type Exception2
}
finally {
// action qui s'exécute toujours, même si aucun erreur a été levé. 
}
```

## L’objet `Throwable` et hiérarchie d’exceptions

On avait dit que toute exception est un objet. Ils existent de différents types d’exceptions, mais le type le plus basique est la classe `Throwable`.

![Hiérarchie d’exceptions](ressources/01_objets_et_classes_untitled.png)

Hiérarchie d’exceptions

- `Error` : situations externes à l'application qu'on ne peut pas anticiper et corriger.
- `Exception` ou exceptions “vérifiées” : situations exceptionnelles qu’un programme bien fait doit anticiper et “corriger”. (Comme des `if` mais on spécifie que c’est un erreur).
- `RuntimeException` ou exceptions non “vérifiées” : situations qu’un programme ne peut pas anticiper et corriger.  Elle indiquent généralement une mauvaise utilisation de la méthode appelée (bug).
    - Ici, on a les exceptions `ArrayIndexOutOfBoundsException` et `NullPointerException`.

### L’obligation d’interception et propagation explicite

Si jamais on lance une exception de type `Exception` (exception vérifiée) qui n’est pas `RuntimeException`, **on doit forcément la propager explicitement ou l’intercepter, ou les deux**. La propagation explicite se fait à la ligne de la déclaration de la méthode, et l’interception se fait dans une des méthodes appelantes.

```java
// propagation explicite
public void sauter() throws Exception { // "<--- on ajoute la prop. expl."

	 if (parachute==null) {
		 throw new Exception("Aie !!!");
	 }

	 parachute.ouvrir();
}

// interception (ici, dans la méthode parade() de la classe Concours)
public void parade(Parapentiste[] participants) {
	for (Parapentiste p : participants) {
		
		try {
			p.sauter();
		}
		
		catch (Exception e) {
			System.err.println(e.getMessage());
			// appeler les secours !
		}
	}
}
```

> [!note]
> Il y a deux manières de lancer un message d’erreur intentionnellement (quand on attrape un erreur) :
>
> - Faire un `try-catch`, et mettre un `System.err.println(”le message d’erreur”)`.
> - Faire un `if` avec un `throw new Exception()/OutOfBoundsException()/NullPointerException()/etc` à l’intérieur.
> - Si c’est une `Exception` qui n’est pas `RuntimeException`, il faut la propager dans la déclaration de méthode : “`void maMethode() throws Exception {…}`”.
> - Sinon, on peut laisser la déclaration de méthode intouchée.