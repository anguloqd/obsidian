# 02 // objets, types primitifs, classes

[Slides de cours 2.pdf](inff3-2223-cours2.pdf)

# Référence et valeurs

## Le modèle de *pile et tas*

Les objets non-primitifs sont “manipulés” vie des références, c’est-à-dire, que le nom de variable sur la pile va s’adresser vers l’objet sur le tas. Les types simples (ceux qui commencent par minuscule) sont “manipulés” par des valeurs, c’est-à-dire que le nom de variable et sa valeur son les deux gardés sur la pile, sans aucune référence.

```java
String s; // s est une référence de type String
					// mais s n'est pas un objet

s="Licence Miashs"; // s maintenant référence un objet String

-----

String s ="Licence Miashs"; // Une bonne pratique est d'initialiser
														// systématiquement les références
```

Pour créer des objets d’une certaine classe, on utilise le mot clé `new`.

```java
String s=new String("Licence Miashs");
String t=new String("Cours de programmation");
String u=s ;
```

Il existent deux endroits où on garde les références (noms des variables) et les valeurs des objets : la pile et le tas, respectivement.

![Dans cette image, u fait référence à la valeur qui fait référence s, “Licence Miashs”. ATTENTION : on crée pas, DANS CE CAS, un autre objet string de valeur “Licence Miashs”, mais c’est possible aussi !](new/uga/l2/s3/info/s3_info_programmation_par_objets/02_objets_types_primitifs_classes/untitled.png)

Dans cette image, u fait référence à la valeur qui fait référence s, “Licence Miashs”. ATTENTION : on crée pas, DANS CE CAS, un autre objet string de valeur “Licence Miashs”, mais c’est possible aussi !

Si on juste initialise la référence ou variable, et on ne le donne pas un objet ou valeur, le résultat est comme suit :
(Pour les tableaux, la valeur par défaut est `null` !)

![`null` n’est pas une valeur !](new/uga/l2/s3/info/s3_info_programmation_par_objets/02_objets_types_primitifs_classes/untitled_1.png)

`null` n’est pas une valeur !

# L’allocation des types primitifs sur Java

## Sur la pile, normalement

L'allocation dynamique sur le tas est pratique mais n'est pas très efficace.
Java traite les types de données très fréquents, i.e. les types primitifs de manière différente.

![Les types primitifs sont alloues dans la pile, **A EXCEPTION DU `STRING` !**](new/uga/l2/s3/info/s3_info_programmation_par_objets/02_objets_types_primitifs_classes/untitled_2.png)

Les types primitifs sont alloues dans la pile, **A EXCEPTION DU `STRING` !**

```java
String s=new String("Licence Miashs");
int i = 3;  // i n'est pas une référence vers 3,
						// elle contient la valeur 3
```

On peut convertir une valeur d’un type primitif à un autre. Ils existent deux types de conversions :

- **Élargissant (promotion)** : on va d’un type plus “large” en termes de capacité de mémoire, donc il n’y a une perte d’info.
- **Restrictive (transtypage, cast)** : il y a une possible perte d’information.

Avec le mot clé `new`, on peut aussi représenter des types primitifs par des objets. 

```java
int e = 33;
Integer f = new Integer(e);
Integer g = new Integer(33);
```

# Visibilité des variables

## Définition d’une variable exclusivement dans un bloc de code

En Java, ils n’existe pas de variables globaux. Chaque définition de variable est lié à un bloc et ses sous-blocs. Les blocs de code sont délimités par les accolades, `{` et `}`.

À la sortie d’un bloc, toutes les variables déclarées depuis l’entrée dans ce bloc sont dépilées. Si c’était de types primitifs, leurs valeurs d’objet sont aussi dépilées.

```java
{
	int i=3;
	// i est visible
	{
		int j=4;
		//i et j sont visibles
	}
	// seulement i est visible
}
// ni i, ni j sont visibles
```

Par contre, les objets non-primitifs gardent leur valeurs dans la mémoire et c’est **seulement leurs références dans la pile** qui seront effacées.

Puisque la mémoire est finie, éventuellement on doit libérer de la mémoire. Java s’occupe de cela automatiquement avec le ***ramasse-miettes***.

Le ramasse-miettes supprime les objets créés par `new` qui ne sont plus référencés (ou visibles, hors de portée)

# Attributs et méthodes

## Des objets “synchronisés” à la classe

Normalement, on parle d’attributs d’un objet (une valeur et fonction particulière). On juste crée des attributs vides dans la construction de la classe, comme “`int i`” à la fois de “`int i = 3`” dans la classe.

Cela dit, on peut créer des attributs particuliers dans une classe. Ces derniers s’appellent attributs et méthodes statiques ou `static`.

En plus, quand on crée des instances d’une classe, on peut changer la valeur d’un attribut qui appartiennent à toutes les instances en changeant celle de la classe.

```java
class UneClasse {
	static int i=0;
}

class Programme{
	public static void main(String[] args){
		UneClasse c = new UneClasse();
		UneClasse d = new UneClasse();
		c.i=34; // seul c.i change à 34
		d.i=85; // seul d.i change à 85
		UneClasse.i=21; // tous les attributs i hérités de la classe UneClasse valent 21, incluse la classe même
	}
}

---

// touts les attributs "i" des objets (et de la classe "UneClasse") sont désormais égaux à 21.
```

Par contre, si on appelle des méthodes des objets (et même pas de la classe !) qui agissent sur les attributs statiques, on va changer tous les attributs de toutes les instances de la classe ET aussi de la même classe.

```java
class UneClasse {
	static int i=0;
	static void incremente() {
		i++;//idem que i=i+1;
	}
}

class Programme{
	public static void main(String[] args){
		UneClasse c = new UneClasse();
		UneClasse d = new UneClasse();

		c.incremente(); // tous les attributs i sont incrémentés par 1, même la classe de base, et même si on appele un objet et pas la classe de base
		d.incremente(); // idem
		UneClasse.incremente(); // idem

	}
}

---

// touts les attributs "i" des objets (et de la classe "UneClasse") sont désormais égaux à 3.
```

**Note extra**. Une méthode est une “message” car on envoie des arguments à la machine.