# (2) 08 // complexité

Date de création: December 11, 2024 10:50 AM
Modifié: February 6, 2025 10:29 PM

[Complexite-algo_Tris.pdf](Complexite-algo_Tris.pdf)

Performance → coût temporel / spatial

Lecture de l’algo

Opérations / instructions

- Opérations de base: logiques (logique simple, sans appeler des fonctions), affectations (y compris de operations de bits, décalages), arithmétiques. Pour les processeurs, ces opérations sont O(1), temps constant pour les calculer.
- Opérations d’itérations : boucles while-do (la boucle qui peut créer aussi do-while, for…). Les boucles peuvent être explicites (while, for) ou implicites (récursivité)
- Opérations conditionnelle : if… else. Proche de test de base.

Pour les conditionnelles:

if (cond) then I1,

else I2.

Dans le boolean `cond`, elle peut être en temps constant O(1), ou être en plus de temps, car le cond peut appeler des fonctions qui prennent plus de temps que O(1).

Le temps de ce if est evalué: `T(If) = T(cond) + max(T(I1), T(I2))` (cas pessimiste).  

```
i = 0                       ← T(initialisation).
while(i ≤ N) do {           ← T(cond)
     I_i (instruction i)    ← T(I_i) en boucle. Donc, N * [T(I_i) + T(cond)]
     i = i + 1
}

Finalement, le temps serait T(init) + N*[T(I_i) + T(cond)].
```

Remarque linguistique: les bouclés imbriqués sont plutôt des boucles “enboîtés”.

```
Imbriqué:
--
|
| ---
| |
--|
  |
  ---
  
Enboîté:

---
|
| ---
| |
| |
| |
| ---
|
---
```

—

exercice de generer des strings de longueur k toujours différente des strings generés:

1. genere un tableau avec toutes les $26^k-1$ combinaisons (O(n) en temporel, mais couteux en temporel).
2. genere un indice random de ce tableau
3. retourne le string choisi
4. supprime le string du tableau, puis prend l’entrée la plus à gauche et tu la copies sur le trou dans le tableau. note bien qu’on a pas besoin de décaler tous les elements à gauche de l’elément supprimé.
5. la prochaine fois, au lieu de tirer entre 0 et 26^k - 1, tire entre 0 et 26^k - 2. et tu actualises ton indice max de -1 comme ça à chaque fois que tu tires.

excercice pour compter le nb de caractères communs entre deux strings (alphabetiques).

- il existe une méthode O(l_1 * l_2)
- il existe deux méthodes O(l_1 + l_2): abcad et bcadz
- première méthode est de faire un premier boucle ayant cree un tableau de 0 à 25, toutes les entrées initialisés à 0. on incremente les entrés qui representent chaque lettre à son correspondant indice. Puis creer un autre tableau pareil, aussi initialisé à zéro aux entrées et on actualises ses indices selon le compte de lettres. finalement, case par case, on compare les chiffres. Si les deux sont sup à zéro, la lettre est présente dans le deux (la chiffre ne doit pas avoir forcément la même valeur dans les deux tableaux).
- Un autre c’est de commencer pareil avec un tableau pour la première string, mais… on crée un compteur et, lorsqu’on parcourt la deuxième, on reste encore sur le même tableau de la première string. on décrémente chaque lettre du premier tableau au fur et a mésure qu’elle apparaît dans la deuxième. chaque fois qu’on decrémente aussi, on actualise le compteur. le nb de lettres coïncidentes est le compteur.

puis; on a vu deux algos: algo de plus court chemin (dijkstra), et algo de fermeture transitive d’un graphe.