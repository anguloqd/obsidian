# 07 // hachage

[INFF5-7.pdf](ressources/07_hachage_inff5-7.pdf)

# Introduction

## Accélérer la recherche de clefs

Afin d’accélérer la recherche de clefs dans un dictionnaire (une `Map` en Java), une idée simple est d’utiliser un tableau pour stocker les associations clef-valeur.

Si le domaine des clefs (l’ensemble des valeurs possibles pour une clef) est **suffisamment petit**, on peut mettre en place de l’adressage direct : il suffit de disposer d’une fonction qui nous donne pour
chaque clef un indice unique dans le tableau. On peut alors vérifier la présence d’une clef dans le tableau par un simple accès indicé.

Par contre, si le domaine des clefs est **trop grand**, on peut mettre en place une technique de hachage et stocker les associations clef-valeur dans une table hachée.

# Dictionnaire à adressage direct

## Définition

![D’un domaine de clés $K$, on crée une table dont les éléments sont de classe `Entree<K,V>`, qui représente des couples $(k_i, v_i)$. On doit déterminer quelle valeur associer à chaque cle.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/07_hachage_untitled.png)

D’un domaine de clés $K$, on crée une table dont les éléments sont de classe `Entree<K,V>`, qui représente des couples $(k_i, v_i)$. On doit déterminer quelle valeur associer à chaque clé.

Les associations clef-valeur sont stockées dans une **table** à adressage direct. Le domaine des clefs doit être suffisamment petit car la taille de la table correspond à la taille du domaine des clefs.

On doit disposer d’une **fonction d’adressage** qui garantit l’unicité des adresses : deux clefs différentes doivent obligatoirement avoir des adresses différentes.

## Code

Un exemple de code pour un dictionnaire à adressage direct serait comme suit :

```java
public class DictionnaireAdressageDirect<K, V> {
	
	// attrbuts
	private Entree<K, V>[] table;
	private int taille;

	// constructeurs
	public DictionnaireAdressageDirect(int capacite) {
		if (capacite < 0)
			throw new IllegalArgumentException("capacité incorrecte");
		table = (Entree<K, V>[]) new Entree[capacite];
		taille = 0;
	}
	
	// classe imbriqué pour les entrées
	private class Entree<T, U> {

		T clef;
		U valeur;

		Entree(T clef, U valeur) {
			this.clef = clef;
			this.valeur = valeur;
		}

		public String toString() {
			return clef + "=" + valeur;
		}
	}

	// méthode : adressage (indice de la valeur)
	private int adresse(K clef) {
		int adresse;
	
		/* ici, il faudrait faire un calcul
		qui permet de donner une valeur à adresse
		en fonction de clef */
	
		if (adresse >= table.length)
			throw new IllegalArgumentException("clef interdite");
		
		// notons que la fonction retourne l'indice de la valeur (int)
		// et non pas la valeur elle-même !
		return adresse; 
	}

	// méthode : recherche
	public V get(K clef) {
		Entree<K, V> e = table[adresse(clef)];

		if (e == null)
			return null;

		return e.valeur;
	}

	// méthode : ajoute/modification (plutôt réécriture)
	public V put(K clef, V valeur) {
		int i = adresse(clef);
		Entree<K, V> e = table[i];
		table[i] = new Entree<K, V>(clef, valeur);
	
		if (e != null)
			return e.valeur;
		taille ++;
	
		return null;
	}
	
	// méthode : suppression
	public V remove(K clef) {
		int i = adresse(clef);
		Entree<K, V> e = table[i];
	
		if (e == null)
			return null;
	
		table[i] = null;
		taille --;
	
		return e.valeur;
	}

}
```

# Dictionnaire haché

## Définition

![D’un domaine de clés $K$, on crée une table dont les éléments sont de classe `Entree<K,V>`, qui représente des triplets $(k_i, v_i, e_i)$, où on détermine d’une certaine manière la valeur $v_i$ associée à chaque clé $k_i$, et le triplet “suivant” $e_i$.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/07_hachage_untitled_1.png)

D’un domaine de clés $K$, on crée une table dont les éléments sont de classe `Entree<K,V>`, qui représente des triplets $(k_i, v_i, e_i)$, où on détermine d’une certaine manière la valeur $v_i$ associée à chaque clé $k_i$, et le triplet “suivant” $e_i$.

Les associations clef-valeur sont stockées dans une table hachée. Le domaine des clefs peut être beaucoup plus grand que la taille de la table.

On se repose sur une **fonction de hachage** qui ne garantit pas l’unicité des adresses : deux clefs différentes peuvent avoir la même adresse donnée par la fonction de hachage. On peut gérer les collisions (inévitables en théorie) par chaînage des entrées.

## Paramètres

Un dictionnaire haché a des paramètres :

- $C$ : la capacité ou taille maximale de la table.
- $N$ : la taille réalisée, le nombre d’éléments présents dans la table.
- $F$ : le facteur de charge maximum.
On appelle facteur de charge le rapport *nombre d’éléments - capacité* : $F=\frac N C$.
- $S$ : le seuil, le nombre maximum d’éléments pouvant être présents dans la table avant redimensionnement (re-hachage). $S = C \cdot F$. On considère que $0.75$ est une bonne valeur pour $F$ :
    - si $F$ est trop petit, on risque de faire des re-hachages trop fréquents,
    - si $F$ est trop grand, on risque d’avoir trop de collisions.

## Code

Un exemple de code pour un dictionnaire à adressage direct serait comme suit :

```java
public class DictionnaireHache<K, V> {
	
	// attributs
	private Entree<K, V>[] table;
	private int taille;
	private int seuil;
	private float facteurDeCharge;
	
	// constructeur
	public DictionnaireHache(int capacite, float facteurDeCharge) {
		// gestion des valeurs incorrectes
		table = (Entree<K, V>[]) new Entree[capacite];
		taille = 0;
		seuil = (int) (capacite * facteurDeCharge);
		this.facteurDeCharge = facteurDeCharge;
	}
	
	// classe imbriquée pour les entrées
	private class Entree<T, U> {
		T clef;
		U valeur;
		Entree<T, U> suivant;

		Entree(T clef, U valeur, Entree<T, U> suivant) {
			this.clef = clef;
			this.valeur = valeur;
			this.suivant = suivant;
		}

		public String toString() {
			return clef + "=" + valeur;
		}
	}
	
	// méthode : hachage (assigne un indice à une clé)
	private int hachage(K clef) {
		if (clef == null)
			return 0;
		return (clef.hashCode() & 0x7FFFFFFF) % table.length;
	}

	// méthode : obtenir entrée à partir d'une clé
	private Entree<K, V> getEntree(K clef) {
		int index = hachage(clef);

		for(Entree<K, V> e = table[index]; e != null; e = e.suivant)
			if ((clef == null && e.clef == null)||(clef != null && clef.equals(e.clef)))
			return e;

		return null;
	}

	// méthode : recherche, obtenir valeur à partir de clé
	public V get(K clef) {
		Entree<K, V> e = getEntree(clef);

		if (e == null)
			return null;

		return e.valeur;
	}
	
	// méthode : ajout/modification (plutôt réecriture)	
	public V put(K clef, V valeur) {
		int i = hachage(clef);
		Entree<K, V> e = getEntree(clef);

		if (e != null) { // clef déjà présente, modification
			V res = e.valeur;
			e.valeur = valeur;
			return res;
		}

		// clef absente, ajout
		if (taille >= seuil) {
			rehachage();
			i = hachage(clef);
		}

		table[i] = new Entree<K, V>(clef, valeur, table[i]);
		taille ++;
		return null;
	}

	// méthode : rehachage, agradissement de la table (de n à 2n+1)
	private void rehachage() {
		int ancienneCap = table.length;
		int nouvelleCap = ancienneCap * 2 + 1;
		Entree<K, V>[] ancienneTable = table;
		table = (Entree<K, V>[]) new Entree[nouvelleCap];
		seuil = (int) (nouvelleCap * facteurDeCharge);

		for (int i = 0; i < ancienneCap; i ++)
			for (Entree<K, V> e = ancienneTable[i]; e != null; ) {
				Entree<K, V> mobile = e;
				e = e.suivant;
				int index = hachage(mobile.clef);
				mobile.suivant = table[index];
				table[index] = mobile;
			}
	}

	// méthode : suppression
	public V remove(K clef) {
		int i = hachage(clef);

		for (Entree<K, V> e = table[i], precedent = null;
					e != null; precedent = e, e = e.suivant) {

			if ((clef == null && e.clef == null) ||
				(clef != null && clef.equals(e.clef))) {

				if (precedent == null)
					table[i] = e.suivant;

				else
					precedent.suivant = e.suivant;

				taille --;
				return e.valeur;
			} // fermeture if exterieur

		return null;

		} // fermeture for exterieur
	} // fermeture méthode suppression
```