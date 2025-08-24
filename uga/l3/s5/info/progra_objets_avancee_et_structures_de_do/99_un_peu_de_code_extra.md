## 99 // un peu de code extra

```java
public class PrepFinal {
    public static void main(String[] args) {
    	
    	// 1. List and ArrayList
    	List<String> list = new ArrayList<>();
    	list.addAll(Arrays.asList("element1", "element2")); // add multiple elements
    	Collections.sort(list); // sort the list
    	Collections.reverse(list); // reverse the list
    	Collections.shuffle(list); // randomly permute the list
    	Collections.fill(list, "newElement"); // replace all elements with a specified element

    	// 2. LinkedList
    	LinkedList<String> linkedList = new LinkedList<>();
    	linkedList.offerFirst("element"); // insert the specified element at the front of this list
    	linkedList.offerLast("element"); // insert the specified element at the end of this list
    	linkedList.peekFirst(); // retrieve, but do not remove, the first element of this list
    	linkedList.peekLast(); // retrieve, but do not remove, the last element of this list

    	// 3. ListIterator
    	ListIterator<String> iterator = list.listIterator(list.size());
    	while(iterator.hasPrevious()) {
    	    String element = iterator.previous(); // get the previous element
    	    iterator.add("element"); // add an element after the current element
    	}

    	// 4. Set and HashSet
    	Set<String> set = new HashSet<>();
    	set.add(null); // add a null element
    	set.isEmpty(); // check if the set is empty
    	set.iterator(); // return an iterator over the elements in this set

    	// 5. TreeSet
    	SortedSet<String> treeSet = new TreeSet<>();
    	treeSet.lower("element"); // returns the greatest element in this set strictly less than the given element
    	treeSet.higher("element"); // returns the least element in this set strictly greater than the given element

    	// 6. Map and HashMap
    	Map<String, String> map = new HashMap<>();
    	map.replace("key", "newValue"); // replace the entry for the specified key only if it is currently mapped to some value
    	map.isEmpty(); // check if the map is empty
    	map.clear(); // remove all mappings

    	// 7. TreeMap
    	SortedMap<String, String> treeMap = new TreeMap<>();
    	treeMap.lowerKey("key"); // get the greatest key strictly less than the given key
    	treeMap.higherKey("key"); // get the least key strictly greater than the given key

    	// 8. Entry
    	for(Map.Entry<String, String> entry : map.entrySet()) {
    	    entry.setValue(entry.getValue().toUpperCase()); // convert the value to uppercase
    	}
    }
}
```
