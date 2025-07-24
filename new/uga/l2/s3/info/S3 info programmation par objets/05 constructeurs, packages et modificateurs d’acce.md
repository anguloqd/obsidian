# 05 // constructeurs, packages et modificateurs d’accès

Date de création: September 29, 2022 11:30 AM
Modifié: July 1, 2023 12:02 PM

[Slides de cours 5.pdf](inff3-2223-cours5.pdf)

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

![Notion d’encapsulation.](new/uga/l2/s3/info/S3%20info%20programmation%20par%20objets/05%20constructeurs,%20packages%20et%20modificateurs%20d’acce/Untitled.png)

Notion d’encapsulation.

La programmation par objets met l'accent sur la réutilisation du code par d'autre programmeurs. On distingue donc le créateur d’une classe et son utilisateur.

Le créateur d’une classe voudrait contrôler l’accès aux attributs (pour maintenir les valeurs prédéfinies) et aux méthodes (car celles qui existent ne sont pas définis pour l’utilisateur mais pour le même créateur de la classe, il n’y a pas donc besoin de les appeler dehors de l’objet).

Java permet de modifier la “visibilité” des attributs et méthodes avec le mot clés `private`, `protected`, *(rien)* et `public`. En plus, Java permet d’organiser les classes en *packages* ou paquets, qui son un ensemble de classes rangées dans un même espace de noms.

On peut appliquer aussi les modificateurs sur les classes. Normalement on utilise que `public` et rien. `public` pour pouvoir accéder à la classe partout, et (rien) pour qu’elle soit accessible par les autres fichiers dans le même dossier/package de la classe. On peut “imbriquer” de packages. Par fichier Java, on peut avoir plusieurs classes mais seulement une seule classe publique, et elle doit avoir le même nom du fichier Java où elle est écrite.

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

![Untitled](new/uga/l2/s3/info/S3%20info%20programmation%20par%20objets/05%20constructeurs,%20packages%20et%20modificateurs%20d’acce/Untitled%202.png)

![Untitled](new/uga/l2/s3/info/S3%20info%20programmation%20par%20objets/05%20constructeurs,%20packages%20et%20modificateurs%20d’acce/Untitled%203.png)

Par convention, les packages ne sont nommés qu’avec des lettres minuscules.
S’il y a deux classes dans le dossier src avec le même nom, et si elles appartiennent à deux paquets différents, il faut utiliser leur noms complets pour les importer. Si elles appartiennent au même paquet, on ne peut qu’utiliser l’une des deux classes dans le même projet.

# Modificateurs d’accès

## Restriction des méthodes

Ils peuvent être places devant une déclaration de classe, méthode ou d’attribut (d’instance ou de classe).

![Untitled](new/uga/l2/s3/info/S3%20info%20programmation%20par%20objets/05%20constructeurs,%20packages%20et%20modificateurs%20d’acce/Untitled%201.png)

Principes pour choisir un modificateur :

- Quand on a le choix, ce serait le mieux de choisir le modificateur le plus restrictif.
- Éviter d'utiliser public sur les attributs (sauf pour les constantes globaux).
Pour donner un accès en lecture ou modification, on les fait avec des méthodes. C’est qui s’appelle l’encapsulation.
- Les membres publics définissent l'interface exposée de la classe. Les modifier pourrait entraîner d’erreurs de compilation.
- On ne peut avoir qu'une classe publique par fichier .java.