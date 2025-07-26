# (2) 11 // tas (files de priorité), diviser-pour-régner, master theorem

[Cours_ArbresGénéraux_Tas.pdf](cours_arbresgnraux_tas.pdf)

[diviser_pour_regner_multiplication.pdf](revision_2425.pdf)

# Tas (files de priorité)

Tas: arbre binaire qui a un ordre vertical plutôt qu’horizontale. Les parents sont toujours plus grands ou plus petits que ses deux enfants.

```python
t = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

def entasser(t, i):
		# Les élements plus petits sont plus prioritaires
		# que les elements plus grands
		if (i >= t.length):
			return;
			
		pivot = 0;
		if (2*i+1 < t.length) and (t[2*i+1] < t[i]):
			pivot = t[i];
			t[i] = t[2*i+1];
			t[2*i+1] = pivot;
		if (t[2*i+2] < t.length) and (t[2*i+2] < t[i]):
			pivot = t[i];
			t[i] = t[2*i+2];
			t[2*i+2] = pivot;
			
		entasser(2*i+1);
		entasser(2*i+2);
		

# Sa solution (O(logk(n) selon moi)
def entasser(t, i):
    # Trouver les indices des enfants
    g = 2 * i + 1
    d = 2 * i + 2
    
    # Trouver l'index du plus grand parmi i, g et d
    max = i
    
    if g < len(t) and t[g] > t[max]:
        max = g
    
    if d < len(t) and t[d] > t[max]:
        max = d
    
    # Si l'élément à i n'est pas le plus grand, on échange
    if max != i:
        t[i], t[max] = t[max], t[i]  # Échange des éléments
        # Appel récursif pour continuer à entasser
        entasser(t, max)
        
# Sa solution (O(klogk(n)) selon moi)
def construire_tas(t):
	for (i = t.length // 2, i >= 0; i--):
		entasser(t,i);
```

Supposons un arbre `[1, 2, 3]`: $T(n) = 4O(1) + 3O(1) + T(n//2) + T(n//2)$, et $T(1) = O(1)$.

Donc, essayons pour plusieurs n:

- En récursif: $T(n) = T(n/2) + O(1)$, et $T(1) = O(1)$
- Lorsqu’on arrive au dernier appel récursif, il y aura un $k^\prime$ tel que $n // 2^{k^\prime} = 1$, et donc on arrive au cas de base $T(1) = O(1)$. En isolant $k^\prime$, on a donc que $k^\prime = \log_2(n)$.
- A la dernière récursion, on arrive donc a $k^\prime O(1) + O(1)$, et donc $\log_2(n)O(1) + O(1)$. Finalement, $T(n) = O(\log_2(n))$.

```python
t = [18, 17, 10, 19, 16, 9, 3, 2, 4, 1]

def entasser_total(t):
	last = t.length - 1; 
	last_parent = (last-1)//2;
	
	for (int i = last_parent; i > -1; i--):
		entasser(t, i); # utile pour la dernière couche de parents
										# mais après on va re entasser les fils qu'on a dejà entasser

# Sa solution
def construire_tas(t):
	for (i = t.length // 2, i >= 0; i--):
		entasser(t,i);
```

Le prochain algo je comprends pas trop…

```python
def trier_tas(t):
	entasser_total(t);
	for (i = t.length; i = 1; i--):
		swap(t, 1, i);
		t.length--;
		entasser(t,1);
```

# Diviser-pour-régner

Il y a deux algorithmes: `m2n1` et `m2n2`. A voir sur fiches.

# *Master theorem*

[Master theorem (analysis of algorithms)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))

## Algorithme de `m2n2`

```python
def multiplication_karatsuba(X, Y, n):
    # Cas de base : nombres à un chiffre
    if n == 1:
        return X * Y
    
    # Calculer la puissance de 10 pour diviser les nombres
    demi_n = n // 2
    diviseur = 10 ** demi_n
    
    # Décomposer X en a et b
    a = X // diviseur  # partie gauche
    b = X % diviseur   # partie droite
    
    # Décomposer Y en c et d
    c = Y // diviseur  # partie gauche
    d = Y % diviseur   # partie droite
    
    # Calculer les trois produits nécessaires
    ac = multiplication_karatsuba(a, c, demi_n)      # Calcul de ac
    bd = multiplication_karatsuba(b, d, demi_n)      # Calcul de bd
    sum_prod = multiplication_karatsuba((a + b), (c + d), demi_n)  # Calcul de (a+b)(c+d)
    
    # Calculer ad+bc en utilisant la formule (a+b)(c+d)-ac-bd
    ad_plus_bc = sum_prod - ac - bd
    
    # Combiner les résultats
    # XY = ac*10^n + ((a+b)(c+d)-ac-bd)*10^(n/2) + bd
    return (ac * (10 ** n)) + (ad_plus_bc * diviseur) + bd
```

## Algorithme de Tri Fusion

Le temps pour un arbre de taille $n$, pour le tri fusion, c’est $T(n) = 2T(n//2) + O(n)$.

Si on reprend la forme du master theorem,

- On identifie que facilement $a=2$, $b=2$. Puis on voit que le $f(n)$ du MT correspond à $O(n)$, d’où $c=1$ (et la variable auxiliaire $k=0$ pour faire disparaître le $\log$).
- On peut calculer que $c_\text{crit} = \log_b(a) = \log_2(2) = 1$.
- On compare avec $c$ : on voit que $c_\text{crit} = c$, d’où ça correspond au cas #2 du MT, et la forme serré du temps de tri fusion correspond donc à :
    
    $$
    T(n) = O\left(n^{c_\text{crit}} \cdot \log_2(n)^{k+1}\right) = O\left(n^1 \cdot \log_2(n)^{0+1}\right)=O\left(n\log_2(n)\right)
    $$