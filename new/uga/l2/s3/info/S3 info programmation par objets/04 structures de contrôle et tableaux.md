# 04 // structures de contrôle et tableaux

Date de création: September 22, 2022 11:25 AM
Modifié: June 10, 2023 10:18 PM

[Slides de cours 4.pdf](inff3-2223-cours4.pdf)

# Qu’est-ce que les structures de contrôle

## Motivation

Un programme n'est généralement pas limité à une séquence linéaire d'instructions car, au cours de son processus, il peut bifurquer, répéter du code ou contourner des sections.

Compte tenue, les structures de contrôle sont les blocs qui **analysent les variables et choisissent les directions** dans lesquelles aller en fonction de paramètres donnés.

# Les structures conditionnelles

## `If`-`else`

Elles exécutent un bloc de code si une telle condition est vérifiée.

```java
if (expression_booleenne) {
// instructions exécutées
// si expression_booleenne
// est évaluée à true
}

else {
// instructions exécutées
// si expression_booleenne
// est évaluée false
}

---

if (exp_1) {
// exp_1 est vrai
}
else if (exp_2) {
// exp_1 est faux mais exp_2 est vrai
}
else {
// exp_1 et exp2 sont faux
}
```

# Les structures itératives (boucles)

## Boucle `while` et `do`-`while`

Elles exécutent un bloc de code répétitivement jusqu’à une condition ne soit plus vérifiée.

```java
while (expression_booleenne) {
// instructions à exécuter
// tant que expression_booléenne
// est évaluée à true
}

---

do {
// instructions à exécuter
// tant que expression_booléenne
// est évaluée à true
} while (expression_booleenne);
```

## Boucle `for`

1. Elle exécute l’initialisation avant la première itération
2. Ensuite elle vérifie la condition
3. À la fin de chaque itération, l’instruction d’étape est réalisée

```java
for ( intialisation ; condition ; étape ) {
 // instructions à exécuter
 // tant que condition est évaluée à true
}
```

# Les branchements inconditionnels

## `break` et `continue`, utiles pour les boucles

Ils sont des instructions qui permettent de contrôler l’exécution d’une boucle.

- `break` permet de stopper l’exécution de la boucle la plus intérieure.
- `continue` stoppe l’itération courante et poursuit la prochaine itération.

Les instructions peuvent utiliser aussi des *labels* ou étiquettes. Mais il faut les éviter dans le cours le plus possible !

# Les structures de sélection

## `switch`

Elle permet de sélectionner des instructions à exécuter en fonction de la valeur d'une expression.

- L’expression est de type `int`, `short`, `char` ou `byte`.
- Le cas `default` est optionnel.

```java
switch (expression) {
	case valeur1 : // instructions si expression == valeur1
		break;
	case valeur2 : // instructions si expression == valeur2
		break;
	// ...
	default : // instructions si les cond. précedentes sont fausses
}
```

# Les tableaux

## Définition

Un tableau est une collection indicée d'objets ou de primitives appelés *éléments du tableau*. Les éléments d'un tableau ont tous le même type. Une référence de tableau est déclarée en utilisant le nom du type suivi de `[]` : `int[] monTableau;`.

Un tableau est un objet non-primitif. Il est donc manipulé par des références, et une référence de tableau est par défaut initialisée à `null`. Il faut donc allouer un espace mémoire (sur le tas).

```java
// un tableau de 3 entiers, initialisé avec les valeurs 1, 2 et 3
int[] monTableau = new int[] {1,2,3};

// créer un tableau de 5 entiers. Les éléments du tableaux sont initialisés avec la valeur par défaut des int, i.e. 0
int[] monTableau2 = new int[5];

---

int[] t = new double[2]; // erreur de compilation : int[], puis double[] ??
int[] ty = new int[] {1,1.0,2.1}; // erreur de compilation : la valeur 1.0 est double, pas int
double[] tx = new double[] {1,1.0,2.1}; // ok. les ints sont passés à doubles
```

## Tableaux et allocation mémoire

Chaque “casse” du tableau contient soit `null`, soit une référence vers l’objet dans le tas. **L’objet contenu n’est pas dans la casse du tableau**, mais “au même niveau” dans le tas. Souvent, quand un objet “contient” un autre, ce qui contient c’est plutôt une référence ver l’objet contenu, **à exception si l’objet contenu est de type simple, dans ce cas il est vraiment “contenu” dans une casse sur le tas**.

```java
String s1="truc";
String s2="upmf";
String[] t6=new String[] {s1,"bidule","chouette"};
String[] t7= new String[4];
String[] t8=new String[] {s1,s2};
```

![Untitled](new/uga/l2/s3/info/S3%20info%20programmation%20par%20objets/04%20structures%20de%20contrôle%20et%20tableaux/Untitled.png)

## Manipulation des tableaux

On peut accéder aux éléments d'un tableau en donnant leur indice (position dans le tableau). Le 1er élément est `t[0]`, est le n-ème élément est `t[n-1]`.

Tout tableau possède un attribut donnant sa taille : `t.length`. **Il n’est pas modifiable !**

Accéder à un élément hors des limite lève une exception : `ArrayIndexOutOfBoundsException`

### Boucle for-each

Forme succincte du `for` pour le parcours de tableaux (ou autres collections). Ne permet que l'accès en lecture, c’est-à-dire, on ne peut pas modifier les valeurs du tableau.

```java
double[] tab = new double[]{1,2,3};
	for (double element : tab) {
	System.out.println(element);
}
```

## Tableaux multidimensionnels

Ce sont des tableaux de tableaux, i.e. un tableau dont les éléments sont des tableaux. Le nombre de dimensions n’est pas limité.

```java
// création

// en une fois
int[][] matrice = new int[10][20] ; // un tableau de 10 sous-tableau, chacun à 20 ints initialisées à 0

// en plusieurs fois
int[][] matrice2 = new int[10][] ;
matrice2[2] = new int[2] ;
matrice2[0] = new int[3] ;

// avec initialisation des éléments (ON MET PAS DES NOMBRES DANS LES CROCHETS)
int[][] matrice = new int[][]{ {1,2,3} , {1,2,3} } ;
// ce dernier est égal [[1,2,3], [1,2,3]]
```

Note : **tous les tableaux de tableaux doivent être du même type**. Si on veut avoirs des types différents, on devra faire un tableau de type `Object[]`, qui est la classe la plus générale.

## Utilitaires sur les tableaux

La classe `java.util.Arrays` fournit de nombreuses procédures utilitaires. Il faut l’importer.
Le package `Arrays` ne contient que de méthodes pour les tableaux utilitaires, il ne faut pas l’instancier.

```java
// par exemple, représenter en chaîne de caractères de tableaux :

int[] tab = new int[]{3,5,1,6};
System.out.println(Arrays.toString(tab)); // cas tableau à une dimension

int[][] tab = new int[][]{ {1,2,3} , {3,4,5} };
System.out.println(Arrays.deepToString(tab)); // cas tableau 2 dimensions ou plus. si on essaie avec un tableu 1d, erreur !
```

### Egalité de tableaux

Rappel que l'opérateur `==` appliqué à deux variables de type tableau retourne l'égalité des références. Dans ce cas, et différent des `Strings`, la méthode `.equals()` fait la même chose que `==` !

Donc, pour comparer leur contenu, `Arrays.equals()` pour un tableau de 1 dimension, et `Arrays.deepEquals()` pour 2 ou plus de dimensions. Il faut que les deux tableaux ont la même taille. Les références sont comparées via `.equals()` et les valeurs via `==`.

### Remplir un tableau

On peut remplir les casses d’un tableau avec une valeur ou une référence donnée.

```java
Arrays.fill(leTableau,v) // remplit toutes les casses avec la valeur v
Arrays.fill(leTableau, idxDebut, idxFin, v) // rempli dès iDebut jusqu'à (iFin-1) avec la valeur v

---

int[] leTableau = new int[10];
Arrays.fill(leTableau, 1, 5, 99); 
System.out.println(Arrays.toString(leTableau));
```

### Trier et chercher

Pour trier un tableau, `Arrays.sort(monTableau)`. Les éléments doivent être comparables par cardinalité (nombres) ou ordre alphabétique (`String` ou `char`).

```java
int[] tab = new int[]{3,5,1,6,2};
Arrays.sort(tab);
System.out.println(Arrays.toString(tab));
```

Pour cherches dans un tableau, il faut qu’il soit déjà trié.

```java
Arrays.binarySearch(monTableau, element); // retourne l'indice de 1ème occurrence.
// si l'élément n'est pas trouvé, il retourne un nombre négatif, usuellement -1

---

int idx= Arrays.binarySearch(tab 5);
if (idx>-1) {
	System.out.println("5 est dans le tableau à la position "+idx);
}
else {
	System.out.println("5 n'est pas dans le tableau");
}
```

### Créer une copie d'un tableau

On utilise la méthode `.copyOf()` ou `.copyOfRange()`.

```java
int[] tab = new int[]{3,5,1,6};
int[] copie = Arrays.copyOf(tab,2); // args: t original, taille copie
System.out.println(Arrays.toString(copie));

int[] copie2 = Arrays.copyOfRange(tab,1,3); //args : t original, iebut, iFin-1 !!!
System.out.println(Arrays.toString(copie2));
```