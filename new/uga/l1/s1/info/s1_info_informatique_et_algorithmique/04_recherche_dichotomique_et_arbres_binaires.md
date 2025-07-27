# 04 // recherche dichotomique et arbres binaires

# Recherche dichotomique

## Définition

- Algorithme de recherche pour trouver la position d'un élément dans un tableau trié.
- Le principe est le suivant : comparer l'élément avec la valeur de la case au milieu du tableau ; si les valeurs sont égales, la tâche est accomplie, sinon on recommence dans **la moitié du tableau pertinente**.
- On répète ce processus jusqu'à arriver à l'élément désiré.

## En Java

```java
public int runBinarySearchIteratively(
  int[] sortedArray, int key, int low, int high) {
    int index = Integer.MAX_VALUE;
    
    while (low <= high) {
        int mid = low  + ((high - low) / 2);
        if (sortedArray[mid] < key) {
            low = mid + 1;
        } else if (sortedArray[mid] > key) {
            high = mid - 1;
        } else if (sortedArray[mid] == key) {
            index = mid;
            break;
        }
    }
    return index;
}
```

## Arbre binaire

## Définition

- **Arbre binaire** : structure de données qui peut se représenter sous la forme d'une *hiérarchie* dont chaque élément est appelé nœud, le nœud initial étant appelé racine.
    - Chaque noeud a, au plus, deux éléments (droit et gauche).
    - Un noeud sans sous-élément (ou fils) est appelé feuille.
    - La profondeur de l'arbre c'est la longueur du chemin d'éléments jusqu'à la racine.
    - La hauteur est la profondeur maximale d'un noeud.
- **Arbre binaire de recherche** : arbre binaire ou chaque noeud a une valeur numérique. Les fils à gauche de ce noeud sont de valeur inférieure et les fils à droite de valeur supérieure.
    - ABR complet : si tous les niveaux de l'arbre sont remplis.
    - ABR parfait : toutes les feuilles sont à la même hauteur.
    - ABR équilibré : tous les chemins de la racine aux feuilles ont la même longueur.
    - ABR dégénéré : chacun de ses nœuds a au plus un fils.

## Pseudo-code : recherche de présence d'un élément

> [!note]
> Je l’écris en pseudo-code et non pas en Java car on devrait explorer les notions le plus compliquées : classes, objets, etc ; pour pouvoir créer un arbre et puis une fonction pour l’explorer.

```java
fonction Recherche(A,e) // prend un arbre et un élément
	Si A = . // si arbre vide
		retourner Faux
	Sinon
		A = (x,FilsGauche,FilsDroit)

	Si x = e
		retourner Vrai
	Sinon si e < x
		retourner Recherche(FilsGauche,e)
	Sinon
		retourner Recherche(FilsDroit,e)
```