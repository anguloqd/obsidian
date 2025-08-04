# (2) 07 // introduction à Java

Histoire:

| Binaire
Assambleur |  |
| --- | --- |
| Cobol / Fortran | Impếratif |
| Basic | (Entre les deux) |
| Smalltalk | Procédural |
| C / Pascal | Procédural |
| C++ | Objet |
| Java | Objet |

Tout est objet.

Constructeur: il initialise les attributs d’instance, il N’INSTANCIE PAS la classe. C’est le mot “new” qui instancie la classe. Initialiser c’est de remplir pour la première fois les casses vides qui ont été crées dans l’allocation mémoire faite par “new”.

```jsx
// Déclaration: juste la création d'un pointeur, qui pointe à rien pour l'instant
Point p; 

// Trois étapes : je crée avec "new" des allocations mémoires pour les attributs
// de points (x et y), puis l'affectation permet à "p" ("référent" en Java) de pointer 
// vers les attributs de l'objet, puis finalement les attributs sont initialisés, i.e.
// les attributs prennent la valeur de la donnée desirée.
p = new Point(x, y)
```

Il y a trois types des constructeurs classiques: constructeur par défaut, constructeur par les données, et constructeur par recopie. new est equivalent à malloc(). le free() est le garbage collector.

```jsx
class Point {
	// Attributs
	int x;
	int y;
	
	// Méthodes (dont les constructeurs)
	Point() {
		x = 0; y = 0; // Constructeur par défaut
	}
	
	Point(int a, int b) {
		x = a; y = b; // Constructeur par les données
	}
	
	Point(Point q) {
		x = q.x; y = q.y; // Constructeur par recopie
	}
}
```

Modifications d’attributs. Deux manières de faire: modification in-place et modification par recopie (créer un nouveau objet). Le problème de la première manière c’est qu’elle peut causer des effets de bord. La deuxième manière crée un nouveau objet et c’est plus couteuse.

```jsx
void deplacer(int dx, int dy) {
	x += dx; y += dy;
}

Point deplacer(int x, int y){
...
}
```

On doit avoir un fichier par classe. La classe Point créera un fichier [Point.java](http://Point.java). Le compilateur java est “javac”, pareil à “gcc”. Le javac prend le fichier Point.java pour le transformer point.class, qui est un fichier avec des instructions en langage “byte-code” qui sera après executer par la Java Virtual Machine. On ne passe jamais par du vrai “binaire”, le byte-code est un peu l’équivalent de binaire ici, mais pas la même chose.

Il vaut mieux avoir une classe “executable” en Java. C’est pas exactement pas la même chose que main. Le main est une méthode dans la classe Executable. On peut aussi mettre des méthodes mains dans les autres classes, comme Point.

```jsx
class Executable {
	void main(...) {
		Point p, p1, p2;
		p = new Point(1,2);
		p1 = new Point(p);
		p2 = new Deplacer(3, 5);
	}
}
```

Pour les tableaux:

```jsx
Point[] tabp; // Creer le pointeur à un tableau tabp
tabp = new Point[10]; // lire en bas
for (int i = 0; i <= 9; i++)
	tabp[i] = new Point();
```

La deuxième ligne instancie ou crée les casses dans la mémoire pour un tableau de taille 10 (new…). Ici aucun constructeur a été appelé. Puis, le pointeur `tabp` est lié à pointer sur le tableau. Finalement, on appelé le constructeur pour chaque casse.

```jsx
class Rectangle {
	Point p1, p2;
	
	Rectangle(Point p1, Point p2) {
		this.p1 = p1; this.p2 = p2;
	}
	
	Rectangle(Rectangle r) {
		p1 = r.p1; p2 = r.p2;
	}
	
	void deplacer(int dx, int dy) {
		p1.deplacer(dx, dy);
		p2.deplacer(dx, dy);
	}
}

class EnsRectangle {
	
	Rectangle[] tabr;
	int size;
	
	// Par la donnée
	EnsRectangle(int size){
		tabr = new Rectangle[size];
		this.size = size;
	}
	
	// Par la donnée
	EnsRectangle(Rectangle[] tabr, int size){
		this.tabr = ...; // how to copy tabr ? without clone or other library ?
		this.size = size;
	}
	
	EnsRectangle(EnsRectangle er) {
		this.tabr = er.copier();
		this.size = er.size;
	}
	
	void ajouter(Rectangle r) {
		tabr.append(r);
		size++;
	}
	
	void private copier(){
		Rectangle[] copie;
		for (int i = 0; i < size; i++){
			copie[i] = tabr[i];
		}
	}
	
	void deplacer(int dx, int dy){
		for (int i = 0; i < size; i++){
			tabr[i] = r.deplacer(dx, dy);
		}
	}
}
```