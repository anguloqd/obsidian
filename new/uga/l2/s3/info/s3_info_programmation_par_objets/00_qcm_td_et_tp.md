# 00 // QCM, TD et TP

# QCM

## QCM 1

composition de classes aussi possible !

on pet ajouter des méthodes a une classes et rédefinir celles de sa super-classe, mais pas supprimer celles-ci

tout objet a un type, mais n’est pas un type.

ATTENTION AU LANGAGE !

## QCM 2

Déclaration de “`static` int i” vs juste “int i” dans une classe et l’impact lors de l’affectation d’une instance

- avec un static, les valeur sont stockes dans le contexte de la classe, pendant que sans static, les valeurs sont stockes dans le contexte de l’instance
- les méthodes de classe `static` peut seule acceder aux attributs de classe `static` et appeler seulement d’autre méthodes `static`. Sinon, on reçoit l’erreur “non-static variable/method cannot be referenced”.

Autre question : si on caste, on accepte explicitement une perte de données. on un va d’un type plut petit à a un plus grand, y’a aucun souci. pour faire l’inverse, il faut forcément faire un cast. sinon erreur !

int i = 2

byte b = (byte) b,

## QCM 3

Supposons :

```java
int[] t1 = new int[] {1}
int[] t2 = new int[] {1}
(t1 == t2) // true
```

Même si les valeurs de types simples (dans ce cas, int) sont alloués sur le tas, l’égalité == marche encore pour les comparer, donc pas besoin d’utiliser l’opérateur de comparaison pour objets non-simples .equals().

En plus, COMMANTAIRES WIKIDOOOOCCC. ils commencent avec /** mais finissent avec */

## QCM 5

Supposons un constructeur qui prend deux `doubles` en paramètres. Si on passe deux `int` (et s’il n’existe pas un constr. qui prend deux int), les `int` passés en paramètres seront castés. 

Autre question : on peut aussi initialiser des attributs dans les constructeurs. **Notons que “initialiser” veut dire de les donner finalement une valeur, pas de “*déclarer”* leur existence, qui est différent** !

## QCM 6

#1 : sous-classse avec constrct. vide → appele construc. de la super-classe par défaut.
S’il n’existe pas (on définit d’autres construct. différents de celui par défaut et du coup le constrct. défaut n’existe plus) on va planter !

En plus, super(z) doit être en première instruction !!

**#2 : relation d’instanciation → objet instance d’une classe, pas entre classes (composition). Voici la différence :**

```java
static class Bedroom { }
static class LivingRoom { }

static class House {

	// on jamais instancie Bedroom, on juste la déclare
	// par contre, on instance le LivingRoom
	
    Bedroom bedroom;
    LivingRoom livingRoom = new LivingRoom();
		
    House(Bedroom bedroom) {
				this.bedroom = bedroom;
    }
}
```

Il peut aider cette questionnaire :

> [!note]
> Questionnaire :
>
> 1. Le const. par défaut existe ou a été plutôt rédéfini et donc n’existe plus ?
> 2. On appelle le const. ? Dans la première ligne ?
> 3. On appelle le const. de la classe courante ou de la super-classe ?

#3 : private (méthode) ne peut pas être redéfini dans les sous-classes.

#4 : ce n’est pas surcharge s’il n’ya extends (héritage) !! 

## QCM 7

**Liaison dynamique** : elle est seulement possible si le type de la référence est super-classe du type de l’objet. Si c’est pas le cas, on a erreur de compilation !

```java
class A {}
class B extends A {}

A x = new B(); // ok. aucun souci. type ref super-classe de type objet.
B x = new A(); // erreur, type ref. est sous-classe de type objet.
```

**Classes `final`** : elle sont immodifiables termes de classes, mais leurs instances sont effectivement modifiables ! (leurs attributs, par exemple, tant qu’ils soient pas `final` eux-mêmes)**. Il est utile de rappeler que sont immodifiables en termes de classes et qu’elle sont pas héritables (étendables)**, mais qu’elles peuvent hériter ! 

**Attributs `final`** : les attributs `final` ne sont pas modifiables après leur initialisation. Cela dit, tout objet prend un valeur par défaut s’il est seulement déclaré sans initialiser. Cette valeur par défaut n’est pas une initialisation, donc on peut la modifier seulement une fois avec **l’initialisation DANS LE CONSTRUCTEUR**, et puis elle reste immodifiable.

**Classes et méthodes `abstract`** : une classe abstraite peut contenir une méthode non-abstraite ! Mais le contraire est faux ! Aussi, definir le corps d’une méthode abstract n’est pas possible. 

**Similitude de `final` et `abstract`** : une classe finale/abstraite peut contenir une méthode qui ne l’est pas. Seulement dans le cas `final`, la méthode est implicitement `final` aussi !

## QCM 8

Tu ne peux pas laisser une méthode implémentée d’une interface sans finir dans une classe. Rappel : une classe propre (non-abstraite) doit avoir des méthodes finalisées, donc définir celles qui viennent des classes abstraites et des interfaces !

Une interface peut étendre d’autre interfaces (multiples). Les méthodes à l’intérieur d’une interface sont “abstraites” au sens qu’elle n’especifient pas un corps. Cela dit, dans les classes abstraites, on peut avoir une méthode finalisée avec corpe qui n’est pas marquée `abstract`.

Autre : si un tableau est initialisée, sa valeur par défaut est null. Mais si on initialises ses cases, les cases prend la valeur par défaut dy type de tableau.

```java
int[] a; // a est null
int[] b = new int[3];// b est [0,0,0]
int[] c = new int[];  // erreur ! 
											// on a besoins forcément d'un nombre dans les crochets
```

# TD

## TD 1

[https://miashs-www.u-ga.fr/~davidjer/inff3/inff3-2223-td1.pdf](https://miashs-www.u-ga.fr/~davidjer/inff3/inff3-2223-td1.pdf)

Diagramme de classe de UML :

![](new/uga/l2/s3/info/s3_info_programmation_par_objets/ressources/00_qcm_td_et_tp_untitled.png)

« une voiture est composée d'un moteur et de plusieurs roues » (*=plusieurs).
« une roue est associée une et une seule voiture ».
Nom : diagramme de classes d’UML.

## TD 2

[https://miashs-www.u-ga.fr/~davidjer/inff3/inff3-2223-td2.pdf](https://miashs-www.u-ga.fr/~davidjer/inff3/inff3-2223-td2.pdf)

- Exo 2 : chaque fois qu’on crée une classe et qui sera le type d’argument d’une fonction, la déclaration du type du paramètre doit être écrit avec majuscule.

```java
void sAjouter(temp t){ // ERROR ! "temp" doit être en maj.
		v = v + t.v;
	}
```

```java
void sAjouter(Temp t){ // OK.
		v = v + t.v;
	}
```

- Exo 3 : si on change dans un bloc de code la valeur d’une variable (non-attribut) extérieur à lui, on la change pour TOUT le programme `main`. On ne la change pas dans les classes, par contre.
    
    ```java
    public class Portee {
    	public static void main(String[] args) {
    
    		String s1 = new String("chaîne 1");
    
    		{
    			String s2 = new String("chaîne 2");
    			String s3 = new String("chaîne 3");
    			s1=s3; // ON MODIFIE LA VALEUR, MEME DEHORS LE BLOC
    		}
    
    		String s4 = new String("chaîne 4");
    
    		{
    			System.out.println("coucou");
    			//commentaire
    		}
    	}
    }
    ```
    

TD2 : REVISE DANS LE PHOTOS. CHAQUE FOIS ON APPELLE UNE FONCTION, ON RENTRE DANS LE CONTEXTE DE LA CLASS:

AUSSI; METHODE `toString()` Generale, appartient à la classe `Objet` la plus générale. si on fait sop(p) où p est une personne, implicitement on va appeler sa méthode `toString()` pour pouvoir l’imprimer. sinon, erreur !

Pour les méthodes classique, on peut acceder aux attributs classiques et statiques. pour les méthodes statiques, on seulement peut acceder aux attributs statiques. Donc les méthodes classiques sont plus flexibles et ouverts.

L’analogie d’une variable globale dans java est de utiliser static dans la superclasse. si on veut qu’une valeur constante soit le même sur les instances de la classe, on la declare static dans la classe.

la seule class d’un fichier qui peut avoir le mot cle public est la classe principal qui contient le main !!!!!!!! on peut pas mettre le mot cle public par toute les classes.

# TP