# (2) 09 // structure chaînées en java, algo récursifs

Pile d’appels : mécanisme intégré aux langage pour permettre la récursivité. “Empilement de l’environnement”.

n = (n + 1)!/(n + 1). c’est mathématique juste mais improgrammable.

Disons qu’il y a deux definitions de factoriel : n * (n-1)! et (n-1)! * n.

Le temps d’exécuter le factoriel de n, est aussi une formule recursive : T(n) = T(n-1) + O(1)

Le code de Hanoi est le suivant. On ne peut pas que bouger un disque à la fois, la fonction H étant un raccourci pour dire qu’on a fait le nécessaire pour pouvoir déplacer `n` disques de `orig` à `dest`.

```
H(n, orig, dest): // Fonction pour deplacer une pile de disques
	H(n-1, orig, dest); 
	Deplacer(orig, dest); // Fonction pour deplacer le disque le plus en haut
	H(n-1, inter, dest);
	
def H(n, orig, dest):
	if n != 0:
		H(n-1, orig, dest); 
		Deplacer(orig, dest);
		H(n-1, inter, dest);
	else Return
```

Algo recursive de Coin Problem:

```
coins = [2, 5, 7]
target = 20

def construct(coins, target):
	combinations = 0
	if target == 0 return 1;
	else:
		for c in coins:
			if c <= target:
				combinations += construct(coins, target - c);
	return combinations;
```

Problem : do it recursively while eliminating duplicates solutions like 9 = (2,2,5) (2,5,2) (5,2,2).

Solution sans duplications: pour chaque pièce, on divise target/coins[i], arrondissant vers le bas, donc pour target = 14 et coins = [2, 5, 7], on a quotients = [7, 2, 2]. Puis, pour chaque piece, on va faire de 0 à quotients[i] branches, en disant combien copies de coins[i] il y en a dans target. Donc, le premier étage de l’arborescence de 14 aura 8 branches allant de 0*2, 1*2, 2*2, …, 7*2. Puis, pour chaque branche, on fait trois branches allant de 0*5, 1*5, 2*5, et finalement pareil pour 7.

```
coins = [2, 5, 7]
target = 20

def construct(coins, target):
   quotients = []
   for i in range(len(coins)):
       quotients.append(target // coins[i])

   def construct_rec(remaining_target, coin_index):
       if coin_index >= len(coins):
           if remaining_target == 0:
               return 1
           return 0

       combinations = 0
       for copies in range(quotients[coin_index] + 1):
           new_target = remaining_target - (copies * coins[coin_index])
           if new_target >= 0:
               combinations += construct_rec(new_target, coin_index + 1)
               
       return combinations

   return construct_rec(target, 0)
```

# Arbres

Arbre: graphe connexe sans cycle.

Arborescence: arbre avec une racine.

Racine: noeud libellé pour être le “premier” noeud.

Pour transformer un arbre n-aire general à un arbre binaire: on utilise la technique 1er fils gauche, frères droits.

Pour implementer les arbres en Java avec des classes:

```java
// Première implementation
class ArbreBinaire {
	Noeud racine;
	// ...
}

class Noeud {
	int contenu;
	Noeud filsg;
	Noeud filsd;
}

// Deuxième implementation
class ArbreBinaire {
	Noeud racine;
	// ...
}

class Noeud {
	int contenu;
	ArbreBinaire filsg;
	ArbreBinaire filsd;
}
```

Pour la représentation contigüe, on stock l’arbre dans un tableau de sorte que pour le noeud en position i, ses fils se trouve en position 2i + 1 et 2i + 2. Pour aller du fils i au père, le père est en position floor((i-1)/2).

Pour les arbres k-aires, les fils de i sont k*i + 1, k*i + 2, …, k*i + k. Pour le père de i, c’est floor((i-1)/k).

## Parcours

On a des types de parcours : préfixe, infixe, post-fixe.

Disons que le traitement à faire est simplement “afficher(sommet)”.

```
def parcours(A):
	si A est fils: afficher(sommet)
	si A n'est pas vide:
		afficher(sommet) // préfixe
		parcours(Ag)
		parcours(Ad)
		
def parcours(A):
	si A est fils: afficher(sommet)
	si A n'est pas vide:
		parcours(Ag)
		afficher(sommet) // infixe
		parcours(Ad)
		
def parcours(A):
	si A est fils: afficher(sommet)
	si A n'est pas vide:
		parcours(Ag)
		parcours(Ad)
		afficher(sommet) // postfixe
```

Pour l’arbre suivant :

```
                            +
                           / \
                          /   \
                         1     *
                              / \
                             4   5
```

Les parcours sont: `+1*45` (préfixe), `1+4*5` (infixe), `145*+` (postfixe).

Pas tout arbre est un arbre binaire de recherche. Un ABR est un arbre binaire avec la propriété d’”invariant” que pour le fils de chaque sommet, le fils gauche est inférieur en valeur et le fils droite supérieur. Les ABR a une relation d’ordre partiel (pas totale). (filsg < pere ≤ filsd).

Arbre AVL (Adelson, Velski-Landis): ABR + k-équilibrage. Le k-équilibrage est la propriété que |h_ag - h_ad| ≤ 1, ou h_ag est l’hauteur du sous-arbre gauche. Ce genre d’arbres évite les structures “filaires”.

Algorithme de AVL : à la construction d’un arbre (et non pas en prenant un arbre déjà construit), on rééquilibre à chaque ajout de sommet si necéssaire. Il y a des patters en regardant les hauteurs (marqueurs) de chaque noeud pour savoir s’il faut faire une seule rotation droite, une rotation gauche, ou une rotation droite puis gauche, etc.

L’hauteur max d’un AVL avec h noueds est N(h) = 1 + N(h-1) + N(h-2), où N(0) = 1 et N(1) = 2. On peut modifier la série de Fibonacci original, particulièrement le cas de base, où F^\prime(0) sera 2 et F^{\prime\prime}(1) = 3. Ceci donne une borne supérieure de la quantité de noeuds qui peuvent être acceptés dans un arbre qui a priori est fixé à hauteur h. C’est la hauteur de l’arbre AVL le plus “desequilibré” en restant encore k-équilibré (avec k=1).