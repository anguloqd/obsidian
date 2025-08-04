# Guide API de NumPy
## Création de tableaux

```python
# Création de base
np.array([1, 2, 3])
np.zeros((3, 4))
np.ones((2, 3))
np.full((2, 3), 7)
np.empty((2, 3))
np.eye(3)  # matrice identité
np.identity(3)

# Création de séquences
np.arange(start, stop, step)
np.linspace(start, stop, num)
np.logspace(start, stop, num, base=10)

# Tableaux aléatoires
np.random.random((3, 4))
np.random.randn(3, 4)  # normale standard
np.random.randint(low, high, size=(3, 4))
np.random.choice([1, 2, 3, 4], size=10)
np.random.seed(42)

# À partir de données existantes
np.asarray(list_or_tuple)
np.copy(array)
np.array(data, dtype=np.float32)
```

## Propriétés et inspection des tableaux

```python
arr.shape
arr.size
arr.ndim
arr.dtype
arr.itemsize
arr.nbytes
arr.strides

# Vérification de type
isinstance(arr, np.ndarray)
np.isscalar(value)
```

## Indexation et découpage

```python
# Indexation de base
arr[0]
arr[-1]
arr[1:4]   # 4eme element non inclus
arr[::2]   # garder que chaque deux elements
arr[:, 1]  # toutes lignes, colonne 1
arr[0, :]  # ligne 0, toutes colonnes

# Indexation avancée
arr[[1_2_4]]  # indexation fantaisie
arr[arr > 5]    # indexation booléenne
np.where(condition, x, y)
np.select(conditions_list, choices_list)

# Multi-dimensionnel
arr[1:3, 2:5]
arr[[0, 2], [1, 3]]  # éléments aux positions (0,1) et (2,3)
```

## Manipulation de tableaux

```python
# Redimensionnement
arr.reshape(new_shape)
arr.resize(new_shape)  # en place
arr.flatten()
arr.ravel()
arr.squeeze()  # supprime dimensions unitaires
np.expand_dims(arr, axis)

# Jointure/Division
np.concatenate([arr1, arr2], axis=0)
np.vstack([arr1, arr2])  # empilement vertical
np.hstack([arr1, arr2])  # empilement horizontal
np.dstack([arr1, arr2])  # empilement en profondeur
np.split(arr, sections, axis=0)
np.hsplit(arr, sections)
np.vsplit(arr, sections)

# Transposition
arr.T
arr.transpose()
np.swapaxes(arr, axis1, axis2)
np.moveaxis(arr, source, destination)
```

## Opérations mathématiques

```python
# Opérations élément par élément
np.add(arr1, arr2)
np.subtract(arr1, arr2)
np.multiply(arr1, arr2)
np.divide(arr1, arr2)
np.power(arr, 2)
np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.log10(arr)
np.sin(arr), np.cos(arr), np.tan(arr)

# Opérations de comparaison
np.equal(arr1, arr2)
np.not_equal(arr1, arr2)
np.greater(arr1, arr2)
np.less(arr1, arr2)
np.logical_and(arr1, arr2)
np.logical_or(arr1, arr2)
np.logical_not(arr)

# Arrondissement
np.round(arr, decimals=2)
np.floor(arr)
np.ceil(arr)
np.trunc(arr)
```

## Fonctions d'agrégation

```python
# Statistiques de base
np.sum(arr, axis=None)
np.mean(arr, axis=None)
np.median(arr, axis=None)
np.std(arr, axis=None)
np.var(arr, axis=None)
np.min(arr), np.max(arr)
np.argmin(arr), np.argmax(arr)
np.percentile(arr, q, axis=None)
np.quantile(arr, q, axis=None)

# Statistiques avancées
np.corrcoef(arr)
np.cov(arr)
np.histogram(arr, bins=10)
np.bincount(arr)
np.unique(arr, return_counts=True)

# Opérations cumulatives
np.cumsum(arr, axis=None)
np.cumprod(arr, axis=None)
np.cummax(arr, axis=None)
np.cummin(arr, axis=None)
```

## Algèbre linéaire (np.linalg)

```python
# Opérations matricielles
np.dot(arr1, arr2)
np.matmul(arr1, arr2)  # ou arr1 @ arr2
np.inner(arr1, arr2)
np.outer(arr1, arr2)
np.cross(arr1, arr2)

# Propriétés matricielles
np.linalg.det(matrix)
np.linalg.inv(matrix)
np.linalg.pinv(matrix)  # pseudo-inverse
np.linalg.norm(vector, ord=2)
np.trace(matrix)

# Décompositions
np.linalg.eig(matrix)  # valeurs et vecteurs propres
np.linalg.svd(matrix)  # décomposition en valeurs singulières
np.linalg.qr(matrix)   # décomposition QR
np.linalg.cholesky(matrix)

# Résolution de systèmes linéaires
np.linalg.solve(A, b)  # résout Ax = b
np.linalg.lstsq(A, b)  # solution des moindres carrés
```

## Recherche et tri de tableaux

```python
# Tri
np.sort(arr, axis=-1)
np.argsort(arr, axis=-1)
np.lexsort(keys)
np.partition(arr, kth)
np.argpartition(arr, kth)

# Recherche
np.searchsorted(arr, values)
np.where(condition)
np.nonzero(arr)
np.flatnonzero(arr)
np.argwhere(arr)

# Opérations sur ensembles
np.intersect1d(arr1, arr2)
np.union1d(arr1, arr2)
np.setdiff1d(arr1, arr2)
np.in1d(arr1, arr2)
```

## Diffusion et fonctions universelles

```python
# Compréhension des règles de diffusion
# (3, 4) + (4,) → (3, 4)
# (3, 1) + (1, 4) → (3, 4)

# Fonctions universelles (ufuncs)
np.vectorize(python_function)
np.frompyfunc(func, nin, nout)

# Réduction le long des axes
np.sum(arr, axis=0, keepdims=True)
np.any(arr, axis=1)
np.all(arr, axis=1)
```

## Mémoire et performance

```python
# Vues vs copies
arr.view()
arr.copy()
arr.base  # vérifie si c'est une vue

# Disposition en mémoire
arr.flags
np.ascontiguousarray(arr)
np.asfortranarray(arr)

# Types de données
np.int8, np.int16, np.int32, np.int64
np.uint8, np.uint16, np.uint32, np.uint64
np.float16, np.float32, np.float64
np.complex64, np.complex128
arr.astype(np.float32)
```

## Modèles courants de LeetCode

```python
# Maximum de fenêtre glissante
def sliding_window_max(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        result.append(np.max(arr[i:i+k]))
    return np.array(result)

# Rotation de matrice
def rotate_matrix_90(matrix):
    return np.rot90(matrix, k=-1)

# Trouver les doublons
def find_duplicates(arr):
    unique, counts = np.unique(arr, return_counts=True)
    return unique[counts > 1]

# Somme de deux avec indices
def two_sum_indices(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]
        mask = arr == complement
        indices = np.where(mask)[0]
        for j in indices:
            if i != j:
                return [i, j]
    return []
```

## Techniques avancées

```python
# Tableaux structurés
dt = np.dtype([('name', 'S10'), ('age', 'i4')])
arr = np.array([('Alice', 25), ('Bob', 30)], dtype=dt)

# Mappage mémoire pour gros fichiers
np.memmap('large_file.dat', dtype='float32', mode='r')

# Astuces d'indexation avancées
# Utilise np.ix_ pour produits croisés d'indices
np.ix_([1, 3], [2, 4])

# Opérations conditionnelles efficaces
np.choose(indices, choices)
np.piecewise(arr, conditions, functions)
```
