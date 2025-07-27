# 03 //  opérateurs

[Slides de cours 3.pdf](ressources/03_operateurs_inff3-2223-cours3.pdf)

# Commentaires

## Trois types de commentaires

Ils existent 3 syntaxes pour les commentaires :

```java
/* Un commentaire
 * sur plusieurs
 * lignes
 */

// un commentaire sur une seule ligne

/**
Un commentaire de type javadoc.
@author : Daniel Angulo
@version : 1.0
Ceci deviendra un page html	sur le dossier "doc"
*/
```

Pour mieux explorer le commentaire Javadoc, aller au [TP1](https://miashs-www.u-ga.fr/~davidjer/inff3/inff3-2223-tp1.pdf) et aussi ce [lien](https://www.jmdoudoux.fr/java/dej/chap-javadoc.htm).

# Opérateurs

## Affichage

On a deux commandes pour afficher des donnés sur la console, `println()` et `print()`. Ils sont des méthodes de la classe `System.out`.

```java
System.out.println("coucou");
System.out.println(1);
System.out.println(true);
```

Ils sont définies les deux pour plusieurs types d’arguments.

## Affectation

Affecter c’est l’action de garder d’associer une valeur avec une référence.
L’opérateur d’affectation est `=`.

La affectation est triviale quand on garde des types primitifs dans une variable.

Par contre, quand on garde un objet non-primitif dans une variable, ils faut faire attention à quelques détails.

```java
class Ampoule {
	boolean allumee;
	int intensite;
}

public class ExampleAffectation {
	public static void main(String[] args) {
		Ampoule a = new Ampoule();
		a.allumee=true;
		a.intensite=50;

		Ampoule b = a ;
		b.intensite=30;

		System.out.println(a.intensite);
	}
}

---

// au moment qu'on a fait b = a, on réference le même objet dans la mémoire.
// notons, "b" et "a" ne sont pas deux objets différents. ils sont deux références différentes vers le même objet.
```

![untitled](new/uga/l2/s3/info/s3_info_programmation_par_objets/ressources/03_operateurs_untitled.png)

## Arithmétique

Rien de nouveau là. Ils existent les 4 opérations arithmétiques fondamentaux (somme, soustraction, multiplication, division) et l’opérateur modulo (`%`).

Par contre, on peut utiliser des raccourcis avec ces opérations arithmétiques. Avec ces raccourcis, on fait en premier l’opération, puis l’affectation.

```java
x+=4; // équiv. à x=x+4;
x-=5; // etc.
x*=3;
x/=2;
x%=2;
```

En plus, l’incrémentation `+=` et `-=` peut devenir plus complexe, avec la pre-incrémentation et la post-incrémentation.

```java
i = 1;
j = ++i; // j et i valent 2

---

i = 1;
j = i++; // j vaut 1, i vaut 2

---

i = 1;
j = --1; // j et i valent 0

---

i = 1;
j= i--; // j vaut 1, i vaut 0;
```

## Relations mathématiques et booléens

Ils évaluent un relation entre les opérandes et retournent un booléen. Retourne `true` si la relation entre opérande est satisfaite, et `false` sinon. On inclut tous les opérateur de comparaison des maths.

Aussi, les opérateurs de comparaison `==` et `!=` sont définis sur les objets, mais ils testent la référence ou adresse dans la mémoire des objets et pas leurs contenus  ! Pour teste l’égalité entre objets, il faut utiliser `a.equals(b);`, mais cela seulement marche avec les types primitifs et pas les objets qu’on a crées.

```java
public class Egalite {
	public static void main(String[] args) {
		String a=new String("toto");
		String b=new String("toto");
		System.out.println(a==b);

		a.equals(b);
	}
}

---

false
true
```

## Logique

Les opérateurs logiques sont ceux fondamentaux de la mathématique : et (`&&`), ou (`||`) et non (`!`). Ils retournent `true` ou `false` qualifiant la relation entre les opérandes.

**Propriété de *court-circuit***: l’évaluation des opérateurs logiques est interrompu quand les évaluations faites sont suffisantes pour déterminer le résultat.

- Si on a “`(a&&b)`” et a est faux, donc on n’évalue même pas b, on retourne `false`.
- Si on a “`(a||b)`” et a est vrai, donc on n’évalue même pas b, on retourne `true`.

## Représentation binaire

| OPÉRATEUR | DESCRIPTION | EXEMPLE | RÉSULTAT |
| --- | --- | --- | --- |
| ~ | Complément à 1 | ~1 |  |
| & | Et | 5&3 | 1 |
| | | Ou | 5|3 | 7 |
| ^ | Ou exclusif | 5^3 | 6 |
| << | Décalage à gauche | 5<<1 | 10 |
| >> | Décalage à droite | 5>>1 | 2 |
| >>> | Décalage à droite non signé |  |  |

## Concaténation

L’opérateur `+` peut aussi être utilisé pour concaténer des strings, s’il détecte au moins un string entre ses deux opérandes.

Les chaînes sont immuables. Quand on concatène deux chaînes, alors une autre
instance de chaîne est créée.

```java
String s = ""; // chaine vide

System.out.println((s+1)+3); // affiche 13
System.out.println(s+(1+3)); // affiche 4
System.out.println(s+1+3); // affiche 13
```