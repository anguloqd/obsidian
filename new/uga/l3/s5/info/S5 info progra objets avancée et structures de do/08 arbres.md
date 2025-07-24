# 08 // arbres

[INFF5-8.pdf](INFF5-8.pdf)

# Généralités

## Définition et parties d’un arbre

On appelle généralement « arbre » en informatique ce que l’on appelle « arborescence » en théorie des graphes. Une arborescence est graphe orienté acyclique possédant une racine unique, c’est-à-dire, il existe un chemin unique de la racine vers n’importe quel sommet de l’arborescence.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled.png)

Les parties d’un arbre sont comme suit :

- Les sommets d’un arbre sont appelés « nœuds ».
- La « racine » d’un arbre est l’unique nœud n’ayant pas de parent (ou prédécesseur).
- Les « feuilles » de l’arbre sont les nœuds qui n’ont pas de descendants (ou successeurs).
- La « hauteur » (ou profondeur) d’un arbre est la longueur du plus long chemin menant de la racine à l’une de ses feuilles.
- Chaque « fils » (ou successeur) d’un nœud non feuille engendre un « sous-arbre » ayant pour racine ce fils.

## Parcours d’arbre

Il existent deux type de parcours classiques des arbres :

- Parcours en largeur (par niveaux de profondeur) : on considère la racine, puis les fils de la racine, puis les fils des fils de la racine, etc.
- Parcours en profondeur : on les a de deux manières…
    - **Préfixé** : un nœud est considéré avant de chacun de ses fils, récursivement.
    Comme astuce, c’est l’algorithme d’aller toujours le plus en bas et à gauche.
    - **Postfixé** : un nœud est considéré après chacun de ses fils, récursivement.
    Comme astuce, c’est l’algorithme d’aller toujours le plus en bas et à droite, puis inverser le chemin à la fin.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%201.png)

# Arbre binaire

## Définition et propriétés

Un arbre binaire est un arbre dans lequel les nœuds peuvent avoir au maximum deux fils. Ils vérifient deux propriétés remarquables :

- Un arbre binaire de $n$ nœuds a au plus $(n + 1) / 2$ feuilles.
- Un arbre binaire de $n$ nœuds a une hauteur $h$ telle que $\log_2 (n + 1) ≤ h ≤ n$.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%202.png)

## Parcours d’arbre binaire

Pour les arbres générales, on avait trois parcours : le parcours en largueur (on visite chaque niveau en entier, puis le suivant), le parcours préfixé et le parcours postfixé.

On ajoute, en plus, le parcours en profondeur infixé : pour chaque nœud, on explore avant son sous-arbre gauche, puis le nœud courant, puis son sous-arbre droite.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%203.png)

## Arbre binaires remarquables

### Arbre binaire dégénéré

Tous les nœuds sauf son unique feuille ont un seul fils. Il est entièrement constitué par un chemin allant de la racine vers son unique feuille. La hauteur est maximale.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%204.png)

### Arbre binaire complet

Il a exactement $2^h-1$ nœuds, dont $2^{h-1}$ feuilles. Tous les niveaux sont remplis, ses nœuds non feuilles ont tous exactement $2$ fils. La hauteur de l’arbre est minimale.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%205.png)

### Arbre binaire parfait

Tous les niveaux sauf éventuellement le dernier sont remplis, les feuilles du dernier niveau sont groupées à gauche.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%206.png)

### Arbre binaire homogène

Il est aussi appelé arbre localement complet. Tous ses nœuds non feuilles ont exactement deux fils.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%207.png)

## Les arbres binaires en programmation

Les arbres binaires peuvent être représentés de différentes façons. Les deux les plus courantes sont :

- La représentation contigüe : bien adaptée aux arbres complets ou parfaits.
- La représentation chaînée : adaptée à tous les types d’arbres.

### Représentation contigüe

Les nœuds sont stockés dans une structure indicée (tableau ou liste). La racine est stockée à l’indice $0$. Le fils gauche et le fils droit du nœud stocké à l’indice $i$ se trouvent respectivement à l’indice $(2i + 1)$ et $(2i + 2)$ s’ils existent. (et si le premier indice de l’arbre est 0, et non pas 1).

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%208.png)

Pour un arbre binaire parfait, il n’y a pas de « trous » dans la structure indicée.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%209.png)

### Représentation chaînée (en classes) et plusieurs méthodes

Chaque nœud est représenté par au moins trois attributs : un pour la valeur (« étiquette ») et deux autres pour les fils gauche et droit.

```java
public class Arbre<T> {
	private Noeud<T> racine;
	// …
}

public class Noeud<T> {
	private T valeur;
	private Noeud<T> gauche;
	private Noeud<T> droit;
	// …
}
```

Les définitions pour les parcours serait comme suit :

```java
// parcours en largeur
public void largeur() {

	if (racine == null)
	return;

	List<Noeud<T>> l = new ArrayList<>();
	l.add(racine);

	for (int i = 0; i <l.size(); i ++) {
		Noeud<T> fGauche = l.get(i).getGauche();
		Noeud<T> fDroit = l.get(i).getDroit();
		if (fGauche != null)
			l.add(fGauche);
		if (fDroit != null)
			l.add(fDroit);
	}

	for (Noeud<T> n : l)
		System.out.print(n.getValeur + " ");
}

// parcours en profondeur préfixé
// préfixé : méthode à ajouter dans la classe Arbre

public class Arbre<T> {
	// …
	public void prefixe() {
		if (racine == null)
			return;
		racine.prefixe();
	}
}

// préfixé : méthode à ajouter dans la classe Noeud

public class Noeud<T> {
	//…
	public void prefixe() {
		System.out.print(valeur + " ");
		if (gauche != null)
			gauche.prefixe();
		if (droit != null)
			droit.prefixe();
	}
}

// parcours en profondeur postfixé
// postfixé : méthode à ajouter dans la classe Arbre

public class Arbre<T> {
	// …
	public void prefixe() {
		if (racine == null)
			return;
		racine.postfixe();
	}
}

// postfixé : méthode à ajouter dans la classe Noeud

public class Noeud<T> {
	//…
	public void postfixe() {
	if (gauche != null)
		gauche.postfixe();
	if (droit != null)
		droit.postfixe();
	System.out.print(valeur + " ");
	}
}

// parcours en profondeur infixé
// infixé : méthode à ajouter dans la classe Arbre

public class Arbre<T> {
	// …
	public void infixe() {
	if (racine == null)
		return;
	racine.infixe();
	}
}

// infixé : méthode à ajouter dans la classe Noeud

public class Noeud<T> {
	//…
	public void infixe() {
		if (gauche != null)
			gauche.infixe();
		System.out.print(valeur + " ");
		if (droit != null)
			droit.infixe();
	}
}
```

### Représentation chaînée : cas des arbres homogènes

Si l’arbre représenté est un arbre homogène, on peut définir une classe pour distinguer les feuilles.

```java
public class Arbre<T> {
	private NoeudAbstrait<T> racine;
	// …
}

public abstract class NoeudAbstrait<T> {
	private T valeur;
	// … comportement abstrait
}

public class Noeud<T> extends NoeudAbstrait<T> {
	private NoeudAbstrait<T> gauche;
	private NoeudAbstrait<T> droit;
	// … comportement d’un noeud
}

public class Feuille<T> extends NoeudAbstrait<T> {
	// … comportement d’une feuille
}
```

### Représentation chaînée : arbre binaire étendu

Pour la représentation chaînée d’un arbre binaire, on peut considérer un type de nœud spécial correspondant au nœud vide.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2010.png)

L’utilisation d’un type `NoeudVide` permet de s’affranchir de nombreux tests sur `null` : on s’appuie sur le polymorphisme.

```java
public class Arbre<T> { 
	NoeudAbstrait<T> racine;
	// …
}

public abstract class NoeudAbstrait<T> {
	// … comportement abstrait
}

public class Noeud<T> extends NoeudAbstrait<T> {
	private T valeur;
	private NoeudAbstrait<T> gauche;
	private NoeudAbstrait<T> droit;
	// … comportement d’un nœud
}

public class NoeudVide<T> extends NoeudAbstrait<T> {
	// … comportement d’une nœud vide « ne rien faire »
}
```

Comme fait divers, telle inclusion d’un nœud vide simplifie le parcours infixé. PDF - p. 29.

Étant donné que le nœud vide ne porte aucune information spécifique, il peut être instance unique d’une classe « Singleton » afin d’optimiser l’utilisation de la mémoire.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2011.png)

Pour s’assurer que `NoeudVide` a une instance unique, on rend son constructeur `private` et on prévoit un accesseur `static` vers l’instance unique.

```java
public class NoeudVide<T> extends NoeudAbstrait<T> {
	private static NoeudVide instance = new NoeudVide();

	private NoeudVide() {
	}

	public static NoeudVide getInstance() {
		return instance;
	}

	// … comportement d’une nœud vide « ne rien faire »
}
```

Dans les autres classes, on utilise l’appel à l’accesseur `static` plutôt qu’un appel au constructeur de `NoeudVide`.

```java
public class Arbre<T> {
	private NoeudAbstrait<T> racine;
	public Arbre() {
		racine = NoeudVide.getInstance();
}

public boolean isEmpty() {
	return racine instanceof NoeudVide;
	}
	// …
}
```

# Arbre binaire ordonné ou de recherche

## Des noeuds ayant des valeurs

S’il existe un ordre sur les valeurs de nœud, on peut construire un arbre binaire ordonné. Dans un arbre binaire ordonné (ou arbre binaire de recherche), tout nœud est tel que sa valeur est supérieure aux valeurs portés dans son sous-arbre gauche et inférieur aux valeurs portés par son sous-arbre droit.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2012.png)

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2013.png)

La recherche d’une valeur dépend uniquement de la hauteur : $\log_2(n + 1) ≤ h ≤ n$.

## Modifications d’un arbre et son code

### Code de l’arbre et les noeuds

On écrit nos classes de base en premier :

```java
// l'arbre ordonné
public class ArbreBinaireOrdonne<T extends Comparable<T>> {
	// …
	public boolean contient(T v) {
		racine.contient(v);
	}
}

// noeud abstrait pour les autre noeuds
public abstract class NoeudAbstrait<T extends Comparable<T>> {
	// …
	public abstract boolean contient(T v);
}

// noeud "normal"
public class Noeud<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public boolean contient(T v) {
		int comp = v.compareTo(valeur);
		if (comp == 0)
			return true;
		return (comp < 0) ? gauche.contient(v) : droit.contient(v);
	}
}

// noeud vide
public class NoeudVide<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public boolean contient(T v) {
		return false;
	}
}
```

### L’ajout

On commence dès la racine et, à chaque nœud, on se demande si le nœud à ajouter et plus grand et plus petit que le nœud courant, jusqu’à arriver au bas, où on ajoute finalement le nœud à ajouter.

![Untitled](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2014.png)

Pour l’implémenter en code, on ajoute des lignes dans chaque des quatre classes de base.

```java
public class ArbreBinaireOrdonne<T extends Comparable<T>> {
// …
	public void ajout(T v) { // nouvelles lignes
		racine = racine.ajout(v);
	}
}

public abstract class NoeudAbstrait<T extends Comparable<T>> {
	// …
	public abstract NoeudAbstrait<T> ajout(T v); // nouvelle ligne
}

public class Noeud<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public NoeudAbstrait<T> ajout(T v) { // nouvelles lignes 
		if (v.compareTo(valeur) < 0)
			gauche = gauche.ajout(v);
		droit = droit.ajout(v);
	}
}

public class NoeudVide<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public NoeudAbstrait<T> ajout(T v) { // nouvelles lignes
		return new Noeud(v, this, this);
	}
}
```

### La suppression

La suppression est, par contre, un action un peu plus délicate. Si on veut supprimer le nœud $N$, il existe trois cas :

- Si $N$ n’a pas de fils, on le supprime simplement sans problème.
- Si $N$ a exactement un fils, on le remplace par son fils
- Si $N$ a exactement deux fils, on le remplace par le nœud le plus à gauche dans son sous-arbre droit. Le nœud le plus à gauche est le nœud pour lequel il prend le plus de chemins à gauche pour atteindre.

![Suppression de $6$. Remplace simple.](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2015.png)

Suppression de $6$. Remplace simple.

![Suppression de $1$. On prend le sous-arbre droite de $1$ et, puis, on va le plus à gauche qu’on puisse jusqu’à arriver au bas, que c’est $3$ dans ce cas.](new/uga/l3/s5/info/S5%20info%20progra%20objets%20avancée%20et%20structures%20de%20do/08%20arbres/Untitled%2016.png)

Suppression de $1$. On prend le sous-arbre droite de $1$ et, puis, on va le plus à gauche qu’on puisse jusqu’à arriver au bas, que c’est $3$ dans ce cas.

Pour l’implémenter en code, on ajoute des lignes dans chaque des quatre classes de base.

```java
public class ArbreBinaireOrdonne<T extends Comparable<T>> {
	// …
	public void suppression(T v) { // nouvelles lignes
	racine = racine.suppression(v);
	}
}

public abstract class NoeudAbstrait<T extends Comparable<T>> {
	// …
	public abstract NoeudAbstrait<T> suppression(T v);
}

public class NoeudVide<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public NoeudAbstrait<T> suppression(T v) {
		return this; // v non trouvée
	}
}

public class Noeud<T extends Comparable<T>> extends NoeudAbstrait<T> {
	// …
	public NoeudAbstrait<T> suppression(T v) {
		int comp = v.compareTo(valeur);
		if (comp < 0) {
			gauche = gauche.suppression(v);
			return this;
		}
		if (comp > 0) {
			droit = droit.ajout(v);
			return this;
		}
		if (gauche instanceof NoeudVide)
			return droit;
		if (droit instanceof NoeudVide)
			return gauche;
		// v est portée par this et a 2 fils
		
		// …

		// v est portée par this qui a 2 fils, on le remplace par
		// le nœud le plus à gauche dans son sous-arbre droit
		Noeud<T> n = (Noeud<T>) droit, pere = this;
		while (!(n.gauche instanceof NoeudVide)) {
			pere = n;
			n = (Noeud<T>) n.gauche;
		}
		if (pere != this) {
			pere.gauche = n.droit;
			n.droit = droit;
		}
		n.gauche = gauche;
		return n;
	}
}
```

# Arbre binaire équilibré

## Une définition rigoureuse

Un arbre binaire équilibré est un arbre binaire ordonné dans lequel tout nœud admet pour ses deux sous-arbres engendrés une différence de hauteur au plus égale à un petit nombre $ε$ : $|h_g-h_d| \le \varepsilon$. **Souvent, on fixe $\varepsilon = 1$**.

Le temps de recherche dans un arbre binaire ordonné est proportionnel à la hauteur de l’arbre, mais dans le pire des cas (celui d’un arbre dégénéré), cette hauteur est égale au nombre de nœuds.

![Untitled](Untitled%2017.png)

Il faut noter que réaliser une recherche binaire sur un arbre devient plus efficace le plus la hauteur de l’arbre est optimisée. L’ajout ou la suppression de nœuds est également effectuée de façon similaire mais sont parfois suivis de ré-équilibrages. Il existe plusieurs techniques de ré-équilibrage :

- Arbres AVL (Adelson, Velskij, et Landis),
- Arbres rouge-noir (ou arbres bicolores).

## Rééquilibrage AVL

Lorsqu’un ajout a eu lieu dans le sous-arbre gauche $(A_g)$ d’un nœud $A$ (précédemment équilibré), plusieurs cas peuvent se poser :

1. La hauteur de $A_g$ n’augmente pas, $A$ reste équilibré.
2. La hauteur de $A_g$ augmente :
    1. La hauteur de $A_g$ était $1$ de moins que celle du sous-arbre droit $(A_d)$, $A$ est encore mieux équilibré.
    2. La hauteur de $A_g$ était égale à celle de $A_d$, $A$ reste équilibré.
    3. La hauteur de $A_g$ était $1$ de plus que celle de $A_d$, un rééquilibrage est nécessaire.

![Dans ces deux cas, aucun rééquilibrage est nécessaire, on considère qu’ils sont encore équilibrés.](Untitled%2018.png)

Dans ces deux cas, aucun rééquilibrage est nécessaire, on considère qu’ils sont encore équilibrés.

Ce sera seulement pour le cas 2.c qu’on aura besoin d’un rééquilibrage (la différence entre les deux hauteurs des sous-arbres est plus grand que $1$). Voyons un exemple :

![Untitled](Untitled%2019.png)

Dans ce cas, **supposons qu’on parle d’un ajout à gauche**, on marque la racine de l’arbre $A_g$ comme $B$ . On verra deux sous-cas de 2.c :

![Si $h(B_g) > h(B_d)$ après ajout, on met de côté à $B$ et $B_g$, puis on rend $B$ père de $A$ toujours en gardant $B_g$.](Untitled%2020.png)

Si $h(B_g) > h(B_d)$ après ajout, on met de côté à $B$ et $B_g$, puis on rend $B$ père de $A$ toujours en gardant $B_g$.

![Si $h(B_d) > h(B_g)$, on répète la procédure faite : on prend la racine de $B_d$ comme $C$, puis on veille à que l’ajout restera dans $C_g$.

Finalement, on rend $C$ la racine de $A$ de tout l’arbre et père de $A$ et $B$, $C_g$ à la place de $B_d$ et $C_d$ à la place de $A_g$.](08%20arbres/Untitled%2021.png)

Si $h(B_d) > h(B_g)$, on répète la procédure faite : on prend la racine de $B_d$ comme $C$, puis on veille à que l’ajout restera dans $C_g$.

Finalement, on rend $C$ la racine de $A$ de tout l’arbre et père de $A$ et $B$, $C_g$ à la place de $B_d$ et $C_d$ à la place de $A_g$.

**Les rééquilibrages après ajout à droite sont considérés de manière symétrique aux rééquilibrages après ajout à gauche**. Des rééquilibrages peuvent être aussi nécessaires après suppression.

Les opérations d’ajout et de suppression consistent essentiellement à déterminer si la modification intervient à gauche ou à droite d’un nœud, puis à invoquer les méthodes de rééquilibrages correspondantes.

Comme astuce, on peut ajouter à la représentation d’un nœud un attribut correspondant à la différence (soit $-1$, $0$, ou $1$) entre la hauteur de son sous-arbre gauche engendré et celle de son sous-arbre droit engendré pour plus d’efficacité.

# Arbre $n$-aire

## Définition

Un arbre $n$-aire est un arbre dans lequel les nœuds peuvent avoir jusqu’à n fils. On le représente généralement en utilisant l’une des deux techniques suivantes :

- les fils d’un nœud sont stockés dans une structure séquentielle (tableau, liste, …).
- l’arbre n-aire n’est pas directement représenté, mais un arbre binaire équivalent est représenté.

Optionnellement, on peut aussi référencer le nœud père d’un nœud (qu’il s’agisse d’un arbre binaire ou d’un arbre n-aire).

## Implémentation et équivalence à arbre binaire

Chaque nœud est représenté par au moins deux attributs : attributs pour la valeur (« étiquette ») et attributs pour la liste de ses fils.

```java
public class Arbre<T> {
	private Nœud<T> racine;
	// …
}

public class Noeud<T> {
	private T valeur;
	private List<Noeud<T>> enfants;
	private Noeud<T> père; // optionnel
	// …
}
```

On pourrait voir un arbre n-aire comme un arbre binaire, par contre, **ce sera un peu différent de l’arbre binaire qu’on a étudie**. L’arbre binaire de base a, au plus, deux fils. Ce nouveau ***arbre binaire général*** aura, au plus, deux “connections”, dont les connections peuvent être de père à fils ou de frère à frère. Voyons que c’est une généralisation du premier modèle d’arbre binaire.

![Untitled](Untitled%2022.png)

Le code pour un arbre $n$-aire changerait. Voici le nouveau code :

```java
public class Arbre<T> { // inchangé
	private Noeud<T> racine;
	// …
}

public class Noeud<T> {
	private T valeur;
	private Noeud<T> premierFils; // changement
	private Noeud<T> frereSuivant;
	private Noeud<T> père; // optionnel
	// …
}
```