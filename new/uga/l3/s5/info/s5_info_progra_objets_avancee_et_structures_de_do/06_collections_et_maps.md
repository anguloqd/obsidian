# 06 // collections et maps

[INFF5-6.pdf](ressources/06_collections_et_maps_inff5-6.pdf)

> [!note]
> À connaître par cœur : les méthodes de Lists, ses méthodes héritées de Collection et Iterator et ListIterator. Les iterators sont moins importants.

> [!note]
> Par rapport au dernier TD, il faut determiner quelle type de liste est meilleure à utiliser : LinkedList ou ArrayList.

# Collections : listes et plus

## Interfaces

![Les flèches pointe une classe ou interface à son parent. Les bleues sont des interfaces, les blanches sont des classes. Voyons que tout commence avec l’interface `iterator<e>`.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/06_collections_et_maps_untitled.png)

Les flèches pointe une classe ou interface à son parent. Les bleues sont des interfaces, les blanches sont des classes. Voyons que tout commence avec l’interface `Iterator<E>`.

### Interface `Iterator<E>`

Un `Iterator` est un objet permettant d’effectuer un parcours des éléments d’une `Collection`. Ces méthodes sont comme suit :

- `boolean hasNext()`
retourne `true` si le parcours n’est pas terminé.
- `E next()`
retourne le prochain élément dans le parcours. Lève une `NoSuchElementException` si le parcours est terminé.
- `void remove()`
supprime le dernier élément retourné par `next()`. Lève une `IllegalStateException` si la méthode `next()` n’a jamais été appelée ou s’il y a déjà eu un `remove()` depuis le dernier `next()`. Méthode « optionnelle » : levée possible d’une `UnsupportedOperationException`.

### Interface `ListIterator` **(!)**

Un `ListIterator` est un `Iterator` permettant de parcourir une `List`. Le parcours avant-arrière est possible, de même que la possibilité d’obtenir des indices.

Cette interface contient des méthodes de parcours additionnelles (`hasNext()` et `next()` sont héritées pour le parcours avant) :

- `int nextIndex()`
retourne l’indice de l’élément qui serait retourné par un appel à `next()` ou -1 si fin du parcours avant.
- `boolean hasPrevious()`
retourne `true` si le parcours arrière n’est pas terminé.
- `E previous()`
retourne le prochain élément dans un parcours arrière. Lève une `NoSuchElementException` si le parcours arrière est terminé.
- `int previousIndex()`
retourne l’indice de l’élément qui serait retourné par un appel à `previous()` ou -1 si fin du parcours arrière.

En plus, l’interface contient aussi des méthodes de modification (nouvelle spécification pour `remove()` qui est héritée) :

- `void remove()`
supprime dans la liste parcourue le dernier élément retourné par `next()` ou `previous()`. Lève une `IllegalStateException` s’il n’y a pas encore eu d’appel ni de `next()`, ni de `previous()`, ou s’il y a déjà eu un `remove()` ou un `add()` depuis le dernier `next()` ou `previous()`. Méthode « optionnelle ».
- `void set(E e)`
remplace par e dans la liste parcourue le dernier élément retourné par `next()` ou `previous()`. Lève une `IllegalStateException` s’il n’y a pas encore eu d’appel ni de `next()`, ni de `previous()`, ou s’il y a déjà eu un `remove()` ou un `add()` depuis le dernier `next()` ou `previous()`. Méthode « optionnelle ».
- `void add(E e)`
insère `e` dans la liste parcourue juste l’avant l’élément d’indice `nextIndex()` s’il existe, et juste après l’élément d’indice `previousIndex()` s’il existe. Si la liste est vide `e` devient son unique élément. Méthode « optionnelle ».

### Interface `Iterable`

Un `Iterable` est un objet que l’on peut parcourir à l’aide d’un `Iterator`. Elle contient une méthode :

- `Iterator<E> iterator()`
retourne un `Iterator` permettant de parcourir `this`.

Un parcours total sur un `Iterable` (et aussi sur les tableaux) peut être réalisé grâce à un boucle `for`. En fait, le mot clé `for` va planter si on l’utilise avec un objet qui n’est pas `Iterable`.

### Interface `Collection` **(!)**

Une Collection est un objet pouvant contenir plusieurs éléments. Elle contient quelques méthodes générales (`iterator()` est hérité d’`Iterable`) :

- `int size()`
retourne le nombre d’éléments de `this`.
- `boolean isEmpty()`
retourne `true` si `this` n’a aucun élément.
- `boolean contains(Object obj)`
retourne `true` si `this` contient au moins un élément équivalent à `obj`. Lève une `ClassCastException` si le type d’`obj` est incompatible avec `E`. Lève une `NullPointerException` si `obj` est `null` et que `this` n’autorise pas d’élément `null`.
- `void clear()`
supprime tous les éléments de `this`.

L’interface est pleine de plusieurs méthodes. On pourrait mentionner quelques méthodes de modification :

- `boolean add(E e)`
ajoute `e` à `this` et retourne `true` si `this` a effectivement été modifié. Méthode « optionnelle ».
- `boolean remove(Object obj)`
supprime dans `this` un élément équivalent à `obj` et retourne `true` si `this` a effectivement été modifié. Méthode « optionnelle ».

Maintenant, voyons des méthodes “ ensemblistes “ :

- `boolean containsAll(Collection<?> c)`
retourne `true` si `this` contient tous les éléments de `c`.
- `boolean addAll(Collection<? extends E> c)`
ajoute tous les éléments de `c` à `this` et retourne `true` si `this` a effectivement été modifié. Méthode « optionnelle ».
- `boolean removeAll(Collection<?> c)`
supprime dans `this` tous les éléments équivalents à un élément de `c` et retourne `true` si `this` a effectivement été modifié. Méthode « optionnelle ».
- `boolean retainAll(Collection<?> c)`
supprime dans `this` tout élément qui n’est pas équivalent à au moins un élément de `c` et retourne `true` si `this` a effectivement été modifié. Méthode « optionnelle ».

Finalement, des méthodes d’export vers un tableau :

- `Object[] toArray()`
retourne un tableau contenant tous les éléments de `this`. Le tableau retourné est indépendant de `this`.
- `<T> T[] toArray(T[] tab)`
si `tab` a une taille suffisante, retourne `tab` après y avoir rangé (en début de tableau) tous les éléments de `this`. Si `tab` n’a pas une taille suffisante, retourne un tableau du même type que `tab` contenant exactement tous les éléments de `this`. Lève une `ArrayStoreException` si `E` est incompatible avec `T`. Lève une `NullPointerException` si `tab` vaut `null`.

### Interface `List` **(!)**

Une `List` est une `Collection` permettant l’accès indicé à ses éléments. Elle contient des méthodes générales additionnelles (`List` hérite de `Collection`) :

- `ListIterator<E> listIterator()`
retourne un `ListIterator` pour parcourir `this`.
- `ListIterator<E> listIterator(int i)`
retourne un `ListIterator` pour parcourir `this`, avec un curseur de lecture positionné juste avant l’élément d’indice `i`.
- `List<E> subList(int from, int to)`
retourne une « vue » de `this` limitée à ses éléments d’indice `from` inclus à `to` exclus. Toute modification de `this` indépendamment de la vue retournée peut rendre cette vue incohérente. Lève une `IndexOutOfBoundsException` si les valeurs de `from` et/ou `to` sont incorrectes.

On mentionnera des méthodes pour l’accès indicé. À noter que toutes ces méthodes lèvent une `IndexOutOfBoundsException` si la valeur de `i` est incorrecte.

- `E get(int i)`
retourne l’élément d’indice `i`.
- `E set(int i, E e)`
retourne l’élément d’indice `i` après l’avoir remplacé par `e` dans `this`. Méthode « optionnelle ».
- `void add(int i, E e)`
insère `e` dans `this` comme nouvel élément à l’indice `i`. Méthode « optionnelle ».
- `E remove(int i)`
retourne l’élément d’indice `i` après l’avoir supprimé de `this`. Méthode « optionnelle ».

Finalement, on a des méthodes des recherche :

- `int indexOf(Object obj)`
retourne l’indice du premier élément de `this` équivalent à `obj`, ou -1 si aucun élément de `this` est équivalent à `obj`.
- `int lastIndexOf(Object obj)`
retourne l’indice du dernier élément de `this` équivalent à `obj`, ou -1 si aucun élément de `this` est équivalent à `obj`.

### Interface `Set` **(!)**

Un `Set` est une `Collection` dans laquelle l’unicité des éléments est garantie.

- Il ne peut pas y avoir dans un `Set` deux éléments `e1` et `e2` tels que `e1.equals(e2)`.
- Si le `Set` accepte `null` comme élément, un seul de ses éléments peut être `null`.
- Si le `Set` accepte l’ajout de nouveaux éléments, la méthode `add(E e)` retourne `false` si le `Set` contient déjà un élément équivalent à `e`.
- Attention aux objets mutables utilisés comme éléments.
- Pas d’autres méthodes que celles héritées de `Collection`.

### Interface `SortedSet` **(!)**

Un `SortedSet` est un `Set` qui garantit que le parcours de ses éléments se fait dans l’ordre de ceux-ci. L’ordre des éléments est déterminé à la création du `SortedSet` :

- ordre « naturel » si les éléments sont des `Comparable`.
- ordre spécifique si un `Comparator` est fourni.

Elle est fourni aussi de méthodes additionnelles (`SortedSet` hérite de `Set`) :

- `Comparator<? super E> comparator()`
retourne le `Comparator` associé à `this` ou `null` si `this` n’est pas muni d’un `Comparator`.
- `SortedSet<E> subSet(E from, E to)`
retourne une vue de `this` limitée aux éléments compris entre `from` inclus et `to` exclus. Levée d’une `IllegalArgumentException` si les valeurs de `from` et/ou `to` sont incorrectes.
- `SortedSet<E> headSet(E to)`
retourne une vue de `this` limitée aux éléments strictement inférieurs à `to`.
- `SortedSet<E> tailSet(E from)`
retourne une vue de `this` limitée aux éléments supérieurs ou équivalents à `from`.
- `E first()`
retourne le premier (le plus petit) élément de `this`. Levée d’une `NoSuchElementException` si `this` est vide.
- `E last()`
retourne le dernier (le plus grand) élément de `this`. Levée d’une
`NoSuchElementException` si `this` est vide.

## Classes prédéfinies

![Maintenant, on se concentre sur les classes qui implémentent les interface ci-dessus.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/06_collections_et_maps_untitled_1.png)

Maintenant, on se concentre sur les classes qui implémentent les interface ci-dessus.

### Classe abstraite `AbstractCollection`

Classe abstraite racine de la hiérarchie d’héritage des collections, implémente `Collection<E>`. Elle n’a aucun attribut localement déclaré.

Voici son constructeur :

- `protected AbstractCollection()`

En plus, elle contient deux méthodes laissées abstraites :

- `public abstract Iterator<E> iterator()`
- `public abstract int size()`

Cela dit, elle implémente par défaut toutes les autres méthodes imposées par `Collection<E>` et redéfinit `toString()` :

- `public boolean contains(Object obj)`
- `public boolean isEmpty()`
- `public void clear()`
- `public boolean add(E e)`
- `public boolean remove(Object obj)`
- `public boolean containsAll(Collection<?> c)`
- `public boolean addAll(Collection<? extends E> c)`
- `public boolean removeAll(Collection<?> c)`
- `public boolean retainAll(Collection<?> c)`
- `public Object[] toArray()`
- `public <T> T[] toArray(T[] t)`
- La méthode `add(E e)` est laissée optionnelle
    
    ```java
    public boolean add(E e) {
    	throw new UnsupportedOperationException();
    }
    ```
    

Finalement, elle définit les méthodes suivantes :

- `remove(Object obj)`
    
    ```java
    public boolean remove(Object obj) {
    	Iterator<E> it = iterator();
    	if (obj == null) {
    		while (it.hasNext())
    			if (it.next() == null) {
    				it.remove();
    				return true;
    			}
    	} else {
    		while (it.hasNext())
    			if (obj.equals(it.next())) {
    				it.remove();
    				return true;
    			}
    		}
    	return false;
    }
    ```
    
- `addAll(Collection<? extends E> c)`
    
    ```java
    public boolean addAll(Collection<? extends E> c) {
    	boolean modified = false;
    	for (E e : c)
    		if (add(e))
    			modified = true;
    	return modified;
    }
    ```
    

### Classe abstraite `AbstractList`

Cette classe hérite d’`AbstractCollection<E>`, propose une implémentation de `List<E>` basique pouvant convenir à une structure sous-jacente à accès indicée (e.g. un tableau).

Elle contient un attribut localement déclaré pour la coordination des `Iterator`, mais aucun attribut dirigeant le stockage des éléments.

- `protected transient int modCount = 0`

Les méthodes laissées abstraites :

- `public abstract E get(int i)`
- `public abstract int size()`

 Méthodes optionnelles :

- `public void add(int i, E e)`
- `public E set(int i, E e)`
- `public E remove(int i)`

Finalement, deux classes imbriquées `Itr` et `ListItr` proposent des implémentations d’`Iterator` et `ListIterator`.

### Classe `ArrayList` **(!)**

Hérite d’`AbstractList<E>`, propose une implémentation de `List<E>` basée sur un tableau
et réalise aussi les interfaces `RandomAccess`, `Cloneable` et `java.io.Serializable`.

Le tableau est agrandi automatiquement si besoin (technique du buffer).

Elle contient deux attributs localement déclarés :

- `transient Object[] elementData`
- `private int size`

![Voyons que `elementData` est le tableau et `size` est la taille realisee.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/06_collections_et_maps_untitled_2.png)

Voyons que `elementData` est le tableau et `size` est la taille réalisée.

Voici ses constructeurs :

- `public ArrayList(int capInitiale)`
permet d’obtenir une `ArrayList` vide de capacité initiale `capInitiale`.
- `public ArrayList()`
équivalent à `ArrayList(10)`.
- public `ArrayList(Collection<? extends E> c)`
permet d’obtenir une `ArrayList` contenant initialement tous les éléments de `c`.

La classe `ArrayList` contient aussi trois classes imbriquées `Itr`, `ListItr` et `SubList`. Les deux premières proposent des implémentations d’`Iterator` et `ListIterator`. La plupart des méthodes héritées sont redéfinies pour assurer de meilleures performances.

Voyons la définition de `size()`, `get(int i)`, `add(E e)` et `add(int i, E e)`. Aussi, on verra la méthode utile `trimToSize()` qui réduit la taille réelle à la taille réalisée.

```java
// méthode size()
public int size() {
	return size;
}

// méthode get()
public E get(int i) { // simplifiée
	if (i < 0 || i >= size)
		throw new IndexOutOfBoundsException();
	return (E) elementData[i];
	}

// méthode utilitaire pour add()
private void ensureCapacity(int minCap) { // simplifiée
	modCount ++;
	if (minCap – elementData.length > 0)
		grow(minCap);
}

// méthode add(E e)
public boolean add(E e) {
	ensureCapacity(size + 1);
	elementData[size ++] = e;
	return true;
}

// méthode add(int i, E e)
public void add(int i, E e) { // simplifiée
	if (i < 0 || i > size)
		throw new IndexOutOfBoundsException();
	ensureCapacity(size + 1);
	System.arraycopy(elementData, i, elementData, i + 1, size – i);
	elementData[i] = e;
	size ++;
}

// méthode trimToSize()
private void trimToSize() { // simplifiée
	modCount ++;
	if (size < elementData.length)
		elementData = (size == 0)
		? new Object[0]
		: Arrays.copyOf(elementData, size);
}
```

### Classe abstraite `AbstractSequentialList`

Hérite d’`AbstractList<E>`, propose une implémentation de `List<E>` basique pouvant convenir à une structure sous-jacente à accès séquentiel. Elle n’a pas d’attribut localement déclaré.

- Elle contient quelques méthodes redéfinies pour fonctionner grâce à un `ListIterator` plutôt qu’un accès indicé.
- La méthode `size()` est héritée abstraite, la méthode `listIterator(int i)` est redéfinie abstraite, la méthode `get(int i)` est définie.

### Classe `LinkedList` **(!)**

Hérite d’`AbstractSequentialList<E>`, propose une implémentation de `List<E>` basée sur un double chaînage circulaire, et réalise aussi les interfaces `RandomAccess`, `Cloneable` et `java.io.Serializable`. Elle contient deux classes imbriquées : `ListItr` pour fournir les `ListIterator`, et la privée `Node<E>` pour définir les chaînons.

Trois attributs sont localement déclarés :

- `transient int size`
- `transient Node<E> first`, le premier chaînon
- `transient Node<E> last`, le dernier chaînon

![Si la taille de la `LinkedList` est 4, donc on aura 4 triplets de la forme $T=\{\text{item, prev, next}\}$. Le `prev` de chaque triplet pointe vers le triplet précédent (et non pas l’item du triplet précédent !), et de même pour `next`.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/06_collections_et_maps_untitled_3.png)

Si la taille de la `LinkedList` est 4, donc on aura 4 triplets de la forme $T=\{\text{item, prev, next}\}$. Le `prev` de chaque triplet pointe vers le triplet précédent (et non pas l’item du triplet précédent !), et de même pour `next`.

Les constructeurs sont comme suivent :

- `public LinkedList()`
permet d’obtenir une `LinkedList` vide.
- `public LinkedList(Collection<? extends E> c)`
permet d’obtenir une `LinkedList` contenant initialement tous les éléments de `c`.

Après, quelques méthodes sont finalement réalisées : `size()`, `listIterator(int i)` et `get(int i)`

```java
// méthode size
public int size() {
	return size;
}

// méthode listIterator
public ListIterator<E> listIterator(int i) {
	// simplifiée
	if (i < 0 || i > size)
		throw new IndexOutOfBoundsException();
	return new ListItr(i);
}

//méthode get
private E get(int i) { // adaptée

	if (i < 0 || i > size)
		throw new IndexOutOfBoundsException();

	if (i < (size >> 1)) {
		Node<E> x = first;
		for (int idx = 0; idx < i; idx ++)
			x = x.next;
		return x.item;

	} else {
		Node<E> x = last;
		for (int idx = size – 1; idx > i; i --)
			x = x.prev;
		return x.item;
	}
}
```

 Finalement, elle contient des méthodes spécifiques :

- `public E getFirst()`
retourne le premier élément de `this`. Lève une `NoSuchElementException` si `this` est vide.
- `public E getLast()`
retourne le dernier élément de `this`. Lève une `NoSuchElementException` si `this` est vide.
- `private E removeFirst()`
retourne le premier élément après l’avoir supprimé de `this`. Lève une `NoSuchElementException` si `this` est vide.
- `private E removeLast()`
retourne le dernier élément après l’avoir supprimé de `this`. Lève une `NoSuchElementException` si `this` est vide.
- `private void addFirst(E e)`
ajoute `e` au début de `this`.
- `private void addLast(E e)`
ajoute `e` à la fin de `this`.

### Classe abstraite `AbstractSet`

Hérite d’`AbstractCollection<E>` et propose une implémentation minimale de `Set<E>`. Elle n’a pas d’attribut localement déclaré. Seules les méthodes suivantes sont redéfinies :

- `public boolean equals(Object obj)`
- `public int hashCode()`
- `public boolean removeAll(Collection<?> c)`

### Classe `HashSet` **(!)**

Hérite d’`AbstractSet<E>` et propose une implémentation de `Set<E>` basée sur une `HashMap<E, Object>`, et réalise les interfaces `Cloneable` et `java.io.Serializable`.

Elle contient un attribut localement déclaré :

- `private transient HashMap<E, Object> map`

La plupart des méthodes héritées sont redéfinies par délégation explicite vers `map`.

Ses constructeurs sont les suivants :

- `public HashSet(int initCap, float loadFactor)`
permet d’obtenir un `HashSet` vide de capacité initiale `initCap` et de facteur de charge `loadFactor`.
- `public HashSet(int initCap)`
équivalent à `HashSet(initCap, 0.75f)`.
- `public HashSet()`
équivalent à `HashSet(16, 0.75f)`.
- `public HashSet(Collection<? extends E> c)`
permet d’obtenir un `HashSet` de facteur de charge 0.75 et contenant tous les éléments de `c`.

Finalement, la méthode `size` est réalisée :

```java
public int size() {
	return map.size();
}
```

### Classe `TreeSet` **(!)**

Hérite d’`AbstractSet<E>` et propose une implémentation de `SortedSet<E>` basée sur une
`TreeMap<E, Object>`, et réalise les interfaces `Cloneable` et `java.io.Serializable`.

Elle contient un attribut localement déclaré :

- `private transient TreeMap<E, Object> map`

La plupart des méthodes héritées sont redéfinies par délégation explicite vers `map`.

Ses constructeurs sont les suivants :

- `public TreeSet()`
permet d’obtenir un `TreeSet` vide dont l’ordre des éléments est l’ordre « naturel ».
- `public TreeSet(Comparator<? super E> comp)`
permet d’obtenir un `TreeSet` vide dont l’ordre des éléments est celui de `comp`.
- `public TreeSet(Collection<? extends E> c)`
permet d’obtenir un `TreeSet`, contenant tous les éléments de `c`, dans leur ordre « naturel ».
- `public TreeSet(SortedSet<E> s)`
permet d’obtenir un `TreeSet` contenant les mêmes éléments et utilisant le même ordre que `s`.

Finalement, la méthode `size` est réalisée :

```java
public int size() {
	return map.size();
}
```

# Maps : notion des dictionnaires

![Les flèches pointe une classe ou interface à son parent. Les bleues sont des interfaces, les blanches sont des classes. Voyons que tout commence avec l’interface `map<kv>`.](new/uga/l3/s5/info/s5_info_progra_objets_avancee_et_structures_de_do/ressources/06_collections_et_maps_untitled_4.png)

Les flèches pointe une classe ou interface à son parent. Les bleues sont des interfaces, les blanches sont des classes. Voyons que tout commence avec l’interface `Map<K,V>`.

## Interfaces et classes prédéfinies

### Interface `Map` **(!)**

Une `Map` (parfois appelée table d’association ou encore dictionnaire) est un objet pouvant regrouper des associations clef-valeur.  A l’instar d’un « dictionnaire » pour un langage naturel, la recherche d’une clef (un « mot ») est optimisée, mais pas la recherche d’une valeur (une « définition »).

L’unicité des clefs est garantie dans une `Map` : il ne peut pas y avoir dans une `Map` deux associations `(k1, v1)` et `(k2, v2)` telles que `k1.equals(k2)` (`v1.equals(v2)` est par contre acceptable). Attention à l’utilisation d’objets mutables pour les clefs.

Chaque association de la `Map` est du type `Entry<K, V>`, une interface imbriquée.

L’interface est pleine de plusieurs méthodes, dont générales, de modification, de recherche et de vue. Pour les méthodes générales :

- `int size()`
retourne le nombre d’associations de `this`.
- `boolean isEmpty()`
retourne `true` si `this` est vide.
- `V get(Object obj)`
retourne la valeur associée à la clef équivalente à `obj` si cette clef est présente dans `this`, `null` sinon.

Pour les méthodes de modification :

- `V put(K k, V v)`
associe à la clef `k` la valeur v dans `this` et retourne la valeur précédemment associée à `k`. Si `k` n’était pas présente dans `this`, une association est créée et `null` est retourné. Méthode « optionnelle ».
- `V remove(Object obj)`
supprime dans `this` l’association ayant une clef équivalente à `obj` et retourne la valeur de cette association. Si aucune clef n’est équivalente à `obj` dans `this`, `null` est retourné. Méthode « optionnelle ».
- `void putAll(Map<? extends K, ? extends V> m)`
ajoute toutes les associations de `m` à `this`. Si des clefs de `this` sont aussi présentes dans `m`, les associations correspondantes sont écrasées. Méthode « optionnelle ».
- `void clear()`
supprime toutes les associations de `this`. Méthode « optionnelle ».

Pour les méthodes de recherche :

- `V get(Object obj)`
retourne la valeur associée à la clef équivalente à `obj` si cette clef est présente dans `this`, `null` sinon.
- `boolean containsKey(Object obj)`
retourne `true` si une clef équivalente à `obj` est présente dans `this`.
- `boolean containsValue(Object obj)`
retourne `true` si au moins une valeur équivalente à `obj` est présente dans `this`. Attention, la recherche de valeurs n’est pas optimisée.

Finalement, pour les méthodes fournissant des vues :

- `Set<K> keySet()`
retourne une vue `Set` des clefs présentes dans `this`.
- `Collection<V> values()`
retourne une vue `Collection` des valeurs présentes dans `this`.
- `Set<Map.Entry<K, V>> entrySet()`
retourne une vue `Set` des associations présentes dans `this`.

### Interface `Map.Entry` **(!)**

C’est une interface imbriquée dans `Map` pour représenter les associations, avec les méthodes suivantes :

- `K getKey()`
retourne la clef de l’association.
- `V getValue()`
retourne la valeur de l’association.
- `V setValue(V v)`
remplace la valeur de l’association par `v` et retourne la valeur remplacée.

### Interface `SortedMap` **(!)**

Une `SortedMap` est une `Map` dans la laquelle les associations sont ordonnées (l’ordre est bien sûr défini sur les clefs).

L’ordre des associations est déterminé à la création de la `SortedMap` :

- ordre « naturel » si les clefs sont des `Comparable`.
- ordre spécifique si un `Comparator` est fourni.

Elle est fournie des méthodes additionnelles (`SortedMap` hérite de `Map`) :

- `Comparator<? super K> comparator()`
retourne le `Comparator` associé à `this` ou `null` si `this` n’est pas muni d’un `Comparator`.
- `SortedMap<K> subMap(K from, K to)`
retourne une vue de `this` limitée aux associations dont la clef est comprise entre `from` inclus et `to` exclus. Levée d’une `IllegalArgumentException` si les valeurs de `from` et/ou `to` sont incorrectes.
- `SortedMap<K, V> headMap(K to)`
retourne une vue de `this` limitée aux associations de clef strictement inférieure à `to`.
- `SortedMap<K> tailMap(K from)`
retourne une vue de `this` limitée aux associations de clef supérieure ou équivalente
à `from`.
- `K firstKey()`
retourne la première (la plus petite) clef de `this`. Levée d’une `NoSuchElementException` si `this` est vide.
- `K lastKey()`
retourne la dernière (la plus grande) clef de `this`. Levée d’une `NoSuchElementException` si `this` est vide.

### Classe abstraite `AbstractMap`

Classe abstraite racine de la hiérarchie d’héritage des `Map`, implémente `Map<K, V>`. Elle fournit une implémentation de base pour une `Map`. Aucun choix n’est fixé pour le stockage des associations : les recherches de clefs ne sont donc pas optimisées.

Elle possède un constructeur :

- `protected AbstractMap()`

En plus, une seule méthode est laissée abstraite :

- `public abstract Set<Entry<K, V>> entrySet()`

Les méthodes qui suivent, imposées par `Map<K, V>` ont une implémentation par défaut et redéfinition de `toString()` :

- `public int size()`
- `public boolean isEmpty()`
- `public void clear()`
- `public boolean containsKey(Object k)`
- `public boolean containsValue(Object v)`
- `public V get(Object k)`
- `public V put(K k, V v)`
- `public V remove(Object k)`
- `public void putAll(Map<? extends K, ? extends V> m)`
- `public Set<K> keySet()`
- `public Collection<V> values()`

La méthode `put(K k, V v)` est laissée optionnelle…

```java
public V put(K k, V v) {
	throw new UnsupportedOperationException();
}
```

Les autres méthodes de modification (`clear()`, `remove(Object k)`, `putAll(K k, V v)`) reposent toutes sur l’utilisation de `entrySet()`.

### Classe `HashMap` **(!)**

Hérite d’`AbstractMap<K, V>`, propose une implémentation de `Map<K, V>` basée sur une table de hachage et réalise aussi les interfaces `Cloneable` et `java.io.Serializable`. La table de hachage est automatiquement agrandie si besoin.

Elle contient six attributs localement déclarés :

- `transient Node<K, V>[] table`
- `transient Set<Map.Entry<K, V>> entrySet`
- `transient int size`
- `transient int modCount`
- `int threshold`
- `final float loadFactor`

Ses constructeurs sont les suivants :

- `public HashMap(int initialCapacity, float loadFactor)`
permet d’obtenir une `HashMap` vide de capacité initiale `initialCapacity` et de facteur de charge `loadFactor`.
- `public HashMap(int initialCapacity)`
équivalent à `HashMap(initialCapacity, 0.75f)`.
- `public HashMap()`
équivalent à `HashMap(16, 0.75f)`.
- `public HashMap(Map<? extends K, ? extends V> m)`
permet d’obtenir une `HashMap` contenant initialement toutes les associations de `m`. Son facteur de charge est `0.75`.

Finalement, il faut dire qu’elle contient une classe imbriquée :

```java
static class Node<K, V> implements Map.Entry<K, V> {
	final int hash;
	final K key;
	V value;
	Node<K, V> next;

	Node(int hash, K key, V value, Node<K, V> next) {
		//…
	}

	public final K getKey() { return key; }
	public final V getValue() { return value; }
	public final String toString() {
		return key + "=" + value;
	}
	
	public final V setValue(V newValue) {
		V oldValue = value;
		value = newValue;
		return oldValue;
	}

	// …

}
```

### Classe `TreeMap` **(!)**

Hérite d’`AbstractMap<K, V>`, propose une implémentation de `SortedMap<K, V>` (plus spécifiquement `NavigableMap<K, V>` depuis Java 1.6) basée sur un arbre binaire ordonné
équilibré et réalise aussi les interfaces `Cloneable` et `java.io.Serializable`. Elle contient de nombreuses classes imbriquées dont `Entry<K, V>` qui implémente `Map.Entry<K, V>`.

Elle contient quatre attributs localement déclarés :

- `private final Comparator<? super K> comparator`
- `private transient Entry<K, V> root`
- `private transient int size`
- `private transient int modCount`

Finalement, elle contient quatre constructeurs :

- `public TreeMap()`
permet d’obtenir une `TreeMap` vide basée sur l’ordre « naturel » de ses clefs. Toutes ses clés devront être des Comparable.
- `public TreeMap(Comparator<? super K> comp)`
permet d’obtenir une `TreeMap` vide basée sur `comp` pour l’ordre de ses clefs.
- `public TreeMap(Map<? extends K, ? extends V> m)`
permet d’obtenir une `TreeMap` contenant initialement toutes les associations de `m`, et basée sur l’ordre naturel de ses clefs. Toutes ses clés devront être des `Comparable`.
- `public TreeMap(SortedMap<? extends K, ? extends V> m)`
permet d’obtenir une `TreeMap` contenant initialement toutes les associations de `m`, et basée sur le même ordre que `m`.