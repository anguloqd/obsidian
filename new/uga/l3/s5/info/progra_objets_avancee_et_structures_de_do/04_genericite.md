# 04 // généricité

[INFF5_4.pdf](ressources/04_genericite_inff5_4.pdf)

# Introduction

## Définition et motivation

Il s’agit d’un mécanisme qui permet la définition de programmes paramétrés par des types.

En Java, depuis la version 1.5, la généricité peut être utilisée dans la définition d'interfaces, de classes et de méthodes.

Regardons la prochaine classe :

```java
public class Paire {
	private int premier, second;

	public Paire(int a, int b) {
		premier = a; second = b;
	}
	public int getPremier() {
		return premier;
	}
	public int getSecond() {
		return second;
	}
}
```

Notons que le seuls paires admissibles sont des paires de `int`. Et si on veut pouvoir manipuler des paires de `String`, de `Point`, etc ?

```java
public class Paire {
	private Object premier, second;

	public Paire(Object a, Object b) {
		premier = a; second = b;
	}
	public Object getPremier() {
		return premier;
	}
	public Object getSecond() {
		return second;
	}
}

// exemples pour illustrer les problèmes ci-dessous hors du code

Paire p1 = new Paire("un", "deux");
Paire p2 = new Paire(1, 2);
```

L’avantage ici c’est qu’on peut créer des paires de tout : `string`, `int`, etc. Par contre, il y aura deux inconvénients :

1. Trans-typage obligatoire pour récupérer une valeur.
    
    ```java
    String s = (String)p1.getPremier();
    int i = (Integer)p2.getSecond();
    ```
    
2. Erreurs de trans-typage détectés à l'exécution et non à la compilation.
    
    ```java
    String s = (String)p2.getPremier(); // ClassCastException
    String s = "" + p2.getPremier(); // ceci marche mais ça appelle le "toString()"
    																 // du int mais ce n'est pas dans le espirit.
    ```
    
    Ici, il faudrait dire que **le cast/trans-typage ne change vraiment pas le type d’un objet, on change juste la manière que le compilateur voit l’objet**. **Le cast est seulement possible entre deux classes qui ont une relation d’héritage**, donc pas de “frères” ou “cousins”. C’est pour ça qu’on ne peut pas caster un `int` à un `String`.
    

# Classe paramétrée

## Définition et solution aux inconvenants précédents

On propose une autre définition de la classe Paire, avec un type passé comme paramètre :

```java
public class Paire<T> {

	private T premier, second;

	public Paire(T a, T b) {
		premier = a; second = b;
	}
	public T getPremier() {
		return premier;
	}
	public T getSecond() {
		return second;
	}
}
```

Ici, `T` est un type paramètre qui sera précise lors de l’instanciation. De cette manière, on garde les même avantages (pouvoir créer des paires pour tout typage) en nous libérant des deux inconvénients.

```java
// avantage conservé : on peut créer des paires pour tout
Paire<String> p1 = new Paire<String>("un", "deux");
Paire<Integer> p2 = new Paire<Integer>(1, 2)

// inconvénient 1 éliminé : plus besoin de trans-typage
String s = p1.getPremier();
int i = p2.getSecond();

// inconvénient 2 éliminé : erreurs de typage détectés à la compilation
String s = p2.getPremier();
```

## Prendre plus d’un type !

Effectivement, on pourrait aussi prendre deux types comme paramètres :

```java
public class Paire<T, U> {

	private T premier;
	private U second;

	public Paire(T a, U b) {
		premier = a; second = b;
	}
	public T getPremier() {
		return premier;
	}
	public U getSecond() {
		return second;
	}

}
```

# Méthode générique

## Le type paramètre n’est pas spécifié, mais *inféré*

Gardons en tête la classe Paire qui prend juste un type paramètre `T`. On va créer une classe qui contient deux méthodes comme suit :

```java
public class X {
	public <T> void affiche(Paire<T> p){ // ici est l'inférence ! mais on s'en sert pas.
		System.out.println(p);
	}
	public static <T> T choix(T a, T b){ // inférence puis fixation de type de retour
		return ((int)(Math.random()*2)) == 1 ? a : b;
	}
}

X x = new X();
x.affiche(p1); // "un, deux", supposant toString() défini pour Paire
x.affiche(p2); // "1, 2", supposant le même
```

Le `T` est inféré du type réel des paramètres effectifs. L’inférence prend lieu au moment de `public <T>…` La méthode `affiche()` va regarder le `T` effectif de Paire pour définir son type de retour.

Dans la première méthode `affiche()`, on a besoin d’écrire `<T>` même si on ne retourne rien, c’est pour indiquer à la méthode que, avant de l’exécuter, on a besoin d’aller connaître la valeur de `T`. Un `Paire<T>` où `T` est inconnu n’est pas un type, donc c’est un erreur. Mais un `Paire<T>` où on connaît le `T` est donc possible.

- Si on aurait écrit `public void affiche(…){}` sans “`<T>`” on aurait eu un erreur, car `Paire<T>` n’est pas un type si `T` inconnu !!!!!!!!!!

Une ligne de programme intéressante serait celle-ci :

```java
Number n = X.choix(new Integer(2), new Double(3.14159));
```

On voit qu’on a le premier objet de type `Integer` et le deuxième de type `Double`. On pourrait se dire qu’ils n’ont pas le même typage, mais en fait il doit forcément exister un type qu’ils partagent : le type `Objet`. **Après, Java infère et assigne le type le plus précis qui est à la fois super-type de `Integer` et de `Double` (qui est en fait le type `Number` et pas `Object`)**.

# Limites pour les types paramètres

## Le paramètre `T` peut hériter un type pour le *limiter*

On va créer une méthode dans la classe Paire pour voir le problème :

```java
public class Paire<T> {

	// ...
	
	public T min(){
		if (premier.compareTo(second) <= 0)
			return premier;
		else
			return second;
	}
}
```

Si on fait cela, on aura un erreur de compilation : méthode `compareTo` non définie pour le type `T`. Rappelons que `compareTo` est une méthode définie dans l’interface `Comparable`, et **pas tous les objets ont le type `Comparable`, donc il se peut que le type `T` ne l’ait pas**, et c’est donc pour ça que on reçoit cet erreur.

La solution est de restreindre les types effectifs possibles pour `T`, comme suit. Ceci ne veut pas dire que `T` est forcément de type `Comparable` pour tout objet de type `T`, mais que `T` a juste le type `Comparable` dans ce cas. La plupart de temps, on utilise ceci avec des interfaces, car l’un des intérêts des interfaces est de donner le type de l’interface.

```java
public class Paire<T extends Comparable> {

	// ...
	
	public T min(){
		if (premier.compareTo(second) <= 0)
			return premier;
		else
			return second;
	}
}
```

Le type limitant peut être une classe ou une interface, ou même plusieurs. Par exemple :

```java
public class Paire<T extends Number> {
	// ...
}

public class Paire<T extends A & Comparable> {
	// ...
}
```

# Effacement

## Un type a une forme brut et une forme paramétrée

Quand une classe est paramétrée, elle est compilée en un type « brut » qui est le seul existant à l’exécution des programmes. Les paramètres de type sont « effacés » . En conséquence :

```java
Paire<String> p = new Paire<String>("a", "b");
boolean b ;
b = p instanceof Paire; // OK
b = p instanceof Paire<String>; // Erreur à la compilation !
```

Le message d’erreur du compilateur indique qu’il faut utiliser la forme brute du type et non la forme paramétrée. En fait, `Paire<String>` est un type valide lors de la compilation, mais ce n’est plus le cas lors l’exécution, et `instanceof` voit juste les types existants lors de l’exécution, d’où l’erreur.

En fait, tant que la classe paramétrée est conservé dans la compilation, elle est modifiée entre après la compilation et avant l’exécution, de sorte que toutes les classes définies avec des types paramétrées assument tels type dans le corps de la classe. Comparons :

```java
// lors de la compilation
public class Paire<T> {

	private T premier, second;

	public Paire(T a, T b) {
		premier = a; second = b;
	}
	public T getPremier() {
		return premier;
	}
	public T getSecond() {
		return second;
	}
}
```

```java
// lors de l'exécution
public class Paire {

	private Object premier, second;

	public Paire(Object a, Object b) {
		premier = a; second = b;
	}
	public Object getPremier() {
		return premier;
	}
	public Object getSecond() {
		return second;
	}
}
```

On pourrait dire que d’écrire class `Paire<T>` serait le même que class `Paire<T extends Object>`.

Prenons un autre exemple : supposons que la classe Paire est `Paire<T extends A>`. Donc :

```java
// lors de la compilation
public class Paire<T extends A> {

	private T premier, second;

	public Paire(T a, T b) {
		premier = a; second = b;
	}
	public T getPremier() {
		return premier;
	}
	public T getSecond() {
		return second;
	}
}
```

```java
// lors de l'exécution
public class Paire {
	
	private A premier, second;
	
	public Paire(A a, A b) {
		premier = a; second = b;
	}
	public A getPremier() {
		return premier;
	}
	public A getSecond() {
		return second;
	}
}
```

Voyons ce qui suit. Pour `p2`, il est correct de ne pas spécifier le type dans `<>` mais Java va nous lancer un avertissement pour qu’on soit plus précis.

```java
Paire<String> p1 = new Paire<String>("un", "deux");
Paire p2 = new Paire("trois", "quatre");

p1=p2;
p2=p1;
```

# Généricité et héritage

## `Paire<T>` est incompatible à l’assignation avec `Paire<U>`

En plus, examinons le suivant programme qui est intéressant :

```java
Paire<String> p1 = new Paire<String>("un", "deux");
Paire p2 = new Paire("trois", "quatre");
p1 = p2;
p2 = p1;
```

Regardons que si on veut mettre p2 dans la boîte prédestinée pour p1, c’est possible, et l’inverse aussi. En fait, il y aura pas d’erreur mais des avertissements à la deuxième et à la troisième ligne (sécurité de type et référence à un type brut, resp.).

Le compilateur peut inférer de `p2` le type de ses deux arguments, et donc déduire le `T` qui a été omis.

Voyons, par contre, que ceci ne marche pas avec deux types différents, **même s’ils ont une relation d’héritage**.

```java
Paire<Point3D> pp3 = new Paire<Point3D>(new Point3D(), new Point3D());
Paire<Point> pp = new Paire<Point>(new Point(), new Point());
pp = pp3;

---

// error: incompatible types: Paire<Point3D> cannot be converted to Paire<Point>
```

Selon le prof, l’explication est trop compliquée, il vaut mieux de ne pas chercher la raison.

## Joker

Le joker `?` peut nous aider dans le dernier code. Voyons une autre méthode :

```java
public class X {

// ...

	public static void affiche2(Paire<Point> p) {
		System.out.println(p);
	}
	
	public static void affiche3(Paire<?> p) {
		System.out.println(p);
	}

}

// ---- DANS LE MAIN ----

Paire<Point> pp = new Paire<Point>(...);
Paire<Point3D> pp3 = new Paire<Point3D>(...);

X.affiche2(pp); // OK
X.affiche2(pp3); // NON : pp3 (Paire<Point3D>) n’est pas le type de Paire<Point>

X.affiche3(pp); // OK
X.affiche3(pp3); // OK
```

Avec `?`, la méthode peut-être appliquée à une Paire dont les éléments ont n’importe quel type. Si on veut se limiter à une Paire dont les éléments sont au moins des Point, on peut écrire comme suit :

```java
	public static void affiche3(Paire<? extends Point> p) {
		System.out.println(p);
	}
```

On peut limiter le joker par le haut de la hiérarchie d’héritage (intérêt par les descendants) avec `extends` ou par le bas (intérêt par les ascendants) avec `super`. Voyons ces image, où **les fils pointent vers leurs père**.

![Joker avec `extends` : le type paramètre est un `Point` ou plus specifique.](ressources/04_genericite_untitled.png)

Joker avec `extends` : le type paramètre est un `Point` ou plus spécifique.

![Joker avec `super` : le type paramètre est un `Point3D` ou plus generale.](ressources/04_genericite_untitled_1.png)

Joker avec `super` : le type paramètre est un `Point3D` ou plus générale.

Si `<? extends Point>` accepte un `Point` et plus spécifique, et `<? super Point3D>` accepte un `Point3D` ou plus générale, `<?>` accepte tout.

Dans la première ligne, on voudrait penser que `Paire<Point>` est un père de `Paire<Point3D>` et ça n’est pas possible ! De même, dans la deuxième image, on voudrait penser que `Paire<Objet>` est un père des autres deux à sa droite, mais en fait non.

`Object` est père de `Point` qui est père de `Point3D`, mais `Paire<Object>` n’est pas père de `Paire<Point>` qui n’est pas non plus père de `Paire<Point3D>`. “Pas d’héritage sur l’horizontale !”.

# Takeaways

Prenons l’exemple : (1) `public <T> void affiche(Paire<T> p)` et (2) `public static <T> T choix(T a, T b)`.

- L’inférence prend lieu en `public … <T> …`.  Elle signale d’aller regarder le type paramétré de `p`.
- Dans les méthodes comme (2) qui acceptent deux objets de type `T`, le type inféré est la classe la plus précise qui est père des deux objets. Pour `T choix(int a, double b)`, `T` est la classe `Number`.
- `Paire<T>` existe comme un type à la compilation mais à l’exécution il ne reste que la classe Paire.
    - On pourrait voir `Paire<T>` comme `Paire<T extends Object>`.
    - Tout occurrence de `T` dans le corps de classe est remplacé par la classe qu’elle étend.
    - `instanceof` juste voit les types qui restent à l’exécution.
- `Paire(Point3D)` n’est pas fils de `Paire(Point)`. 
Donc, méthodes pour le dernier ne marchent pas pour le premier. Ni vice-versa.
Assigner `pp3` à `pp` pose un problème aussi ! (`incompatible types`)
- Le joker `?` s’utilise dans les méthodes.
Méthodes qui prennent un paramètre `Paire<?>` marchent avec tout type `T` dans les chevrons. On peut utiliser `extends` et `super` dans les chevrons.