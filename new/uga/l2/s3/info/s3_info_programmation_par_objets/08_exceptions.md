# 08 // exceptions

[Slides de cours 8.pdf](ressources/08_exceptions_inff3-2223-cours8.pdf)

# Exceptions et Java

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

![Hiérarchie d’exceptions](new/uga/l2/s3/info/s3_info_programmation_par_objets/ressources/08_exceptions_untitled.png)

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

<aside>
✅ Il y a deux manières de lancer un message d’erreur intentionnellement (quand on attrape un erreur) :

- Faire un `try-catch`, et mettre un `System.err.println(”le message d’erreur”)`.
- Faire un `if` avec un `throw new Exception()/OutOfBoundsException()/NullPointerException()/etc` à l’intérieur.
    - Si c’est une `Exception` qui n’est pas `RuntimeException`, il faut la propager dans la déclaration de méthode : “`void maMethode() throws Exception {…}`”.
    - Sinon, on peut laisser la déclaration de méthode intouchée.
</aside>