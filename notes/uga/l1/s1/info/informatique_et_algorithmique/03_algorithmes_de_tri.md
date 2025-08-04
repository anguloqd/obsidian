# 03 // algorithmes de tri

# Tri-bulle (Bubble sort) ou tri par propagation

## L’algorithme

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Sorting_bubblesort_anim.gif/260px-Sorting_bubblesort_anim.gif)

- Pivot : l'élément qui sera comparé avec l'élément suivant.
    - Si le pivot est plus grand que l'élément suivant, on change les places, de telle manière que le pivot se déplace à droite.
    - Si l'élément suivant est plus grand que le pivot, le pivot deviens encore cet élément suivant.
- Il doit son nom au fait qu'il déplace rapidement les plus grands éléments en fin de tableau, comme des bulles d'air qui remonteraient rapidement à la surface d'un liquide.
- C'est le plus lent des algorithmes de tri communément enseignés, et il n'est donc guère utilisé en pratique.

## En Java

```java
for(int i = 0;i < n; i++){
    for(int j=0;j < n - 1; j++){
        if(arr[j] > arr[j+1]){
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
       }
    }
}
```

# Tri par insertion

## L’algorithme

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Insertion-sort-example-300px.gif/220px-Insertion-sort-example-300px.gif)

- Le tri par insertion considère chaque élément du tableau et l'insère à la bonne place parmi les éléments déjà triés.
- Ainsi, au moment où on considère un élément, les éléments qui le précèdent sont déjà triés, tandis que les éléments qui le suivent ne sont pas encore triés.

## En Java

```java
for(int i = 1;i < n; i++) {
    int j = i;
    while(j > 0 && arr[j] < arr[j-1]) {
        int temp = arr[j];
        arr[j] = arr[j-1];
        arr[j-1] = temp;
        j--;
    }
}
```

# Tri rapide (Quick-sort)

## L’algorithme

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Sorting_quicksort_anim.gif/260px-Sorting_quicksort_anim.gif)

1. On fixe un pivot. Normalement, au début, c'est l'élément plus à droite.
2. Après, on se fixe sur l'élément plus à gauche et il sera le premier élément marqué.
    1. Après, on commence à comparer le pivot avec celui à droite de l'élément marqué.
        1. Si 2ème E.M. < Pivot, on échange de place le marqué et le deuxième marqué et on reprend à avec ce dernier et celui à sa droite.
        2. Si non, on passe au suivant.
    2. On répète ce processus jusqu'à ce qu'on arrive à l'élément à gauche du pivot.
        
        À ce point, on échange le pivot et le deuxième élément marqué si pivot < deuxième élément.
        
    3. Après, on partitionne le tableau à droite et à gauche d'où le pivot est tombé et on répète le processus.

## En Java

```java
public static void quicksort(int[] arr, int low, int high) {
    if(low >= high) return;
    int pivotPosition = partition(arr, low, high);
    quicksort(arr,low, pivotPosition-1);
    quicksort(arr, pivotPosition+1, high);
}

public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int left = low, right = high-1;
    while(left < right) {
       while(arr[left]<pivot) {
            left++;
       }
       while(arr[right]>pivot) {
            right--; 
       }
       if(left >= right) {
            break;
       }
       int temp = arr[left];
       arr[left] = arr[right];
       arr[right] = temp;
    }
    int temp = arr[left];
    arr[left] = arr[high];
    arr[high] = temp;
    return left;
}
```