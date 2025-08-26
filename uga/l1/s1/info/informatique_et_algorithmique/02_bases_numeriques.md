## 02 // bases numériques

## Le codage binaire

### Le *bit*

- L’unité minimale de représentation de l’information correspond à un fil sur lequel il y a du courant ou il n’y a pas de courant.
- Ceci est appelé un bit: binary digit. Un bit d’information peut permet de coder deux informations.
- On groupe souvent les bits par 8 et on appelle cela un octet (byte en anglais).
    - Cela permet de représenter $256$ informations, puisque $2^8=256$.
    - Un octet permet donc de représenter tous les symboles de l’alphabet occidental et ce codage qui a été fait dans les années 1960 et qui est encore utilisé aujourd’hui.

## Bases

### Passer de base $10$ à base $b$

- C'est facile. Tenant la base b en tête, pour chaque chiffre en position p >= 0, (de droite à gauche) on fait la somme de tous le (chiffre * bp)possible.

### Passer de base $b$ à base $10$

- C'est le contraire du processus précédent, il faut faire plutôt attention aux restes et pas aux quotients (à exception du dernier). On divise, de droite à gauche, par la base b et on complète chaque chiffre avec le reste obtenu de droite à gauche.

### Passer de base $16$ à base $2$

- On sépare les chiffres du nombre en base 16 et, pour chaque chiffre, on utilise quatre bits pour représenter ce chiffre. Une fois fini, on colle tous le nombres en base 2 et on obtient la transformation.
- Pour la transformation inverse, on fait la même chose a l'inverse mais on doit s'assurer que la quantité de bits, de droite a gauche, est un multiple de 4. Sinon, compléter avec des zéros à gauche.

## Représentation des nombres décimaux

### Passer de base $10$ à base $2$, en décimaux

- C'est vraiment une extension de l'idée avec les entiers (diviser en priorisant le reste puis le quotient) mais on divise par 1/2 (qui est la même chose que multiplier par 2) et on soustrait 1 si possible, jusqu'à ce qu'on arrive à reste 0.
- Pour chaque chiffre à laquelle on a soustrait 1, on écrit 1 dans la position de ce chiffre, de gauche a droite à partir de la virgule. Si on n'a pas soustrait 1, on écrit 0.

### **Passer de base $10$ à base $b$, en décimaux**

- C'est exactement la même chose, mais on multiplie par la base et on soustrait la partie entière du produit et on recommence jusqu'à arriver à zéro.

## **Représentation des entiers négatifs**

### Écrire des négatifs comme des positifs : l**a méthode du *complément vrai*, en toutes bases**

> [!note]
> Le but de cette méthode est de, étant donné une base $b$ et une quantité de chiffres $n$ dans cette base, représenter des entiers entre $[-b^{n-1}, b^{n-1}-1]$ comme un entier positif.
>
> Une autre manière de le voir c’est comme une fonction bijective qui va de l’intervalle $[-b^{n-1},b^{n-1}-1]\mapsto[0,b^n]$  et, puisque c’est bijective, on peut le faire à l’inverse aussi.
>
> Attention : le but de cette méthode est de pouvoir représenter des entiers négatifs avec que des entiers positifs. On ne considère pas encore les réels.

- D'abord, notons que coder $−7$ sur $8$ bits ne donne pas le même résultat que sur $16$ bits. **La base change la représentation si on considère les négatifs !**
- On fixe une base et une quantité de chiffres dans la base.
Prenons base $10$ et quatre chiffres.
- Supposons que $-A$ est un nombre négatif. Alors $-A = (9999  - A + 1) - 10000$.
    - Le terme $(9999 - A + 1)$ est le “*complément vrai*".

- Pour renverser cette méthode, le processus est et d’additionner $(9999 - A + 1)$ au nombre codé. C'est à dire, si on applique la complément vrai deux fois, on arrive au même nombre.
- Notons finalement que, avec base $10$ et quatre chiffres:
    - Le nombre $5000$ est codé à $-5000$,
    - $5001$ est codé à $-4999$,
    - $5002$ est codé à $-4998$,
    - etc.
    - On arrive dès $0$ à $5000$ et, en réalité, c’est comme si on commence à compter de $-5000$ à $0$.

#### L’addition de deux entiers codés **avec le complément vrai**

- Essayons de additionner $4324$ (représenté par lui-même) et $-2817$ (représenté par $7183$). On garde encore la base $10$ et quatre chiffres, donc $[-5000,4999]$.
    - $4324 - 2817 = 1507$ (sans codage, une addition normale quoi)
    - $4324 + 7183 = 11507$ (avec codage)
- Notons que si on ignore la chiffre la plus à gauche du résultat de nombres codés ($11507$) on reste avec le résultat sans codage ($1507$).

#### Exemple avec base $2$ (le plus souvent en cours !)

- Prenons un nombre base 2 à transformer. Ceci sera -A.
- Prenons une base (qui est toujours base 2) et une quantité de chiffres. Disons 8 chiffres, alors 8 bits (alors 1 byte).
- On va faire alors (nombre plus grande possible en 8 bits - A + 1).
    ◦ C'est à dire (11111111 - A + 00000001). (A doit être écrit sur sa version positive)

- **Une manière plus facile** : part de la droite à la gauche en recopiant tous les zéros (s'ils existent) et juste le première 1. Après, inverse toutes les chiffres jusqu'à la fin.

****

#### Notes sur l’addition de deux entiers en base $2$

- Notons que, avec la méthode du complément vrai et **seulement en base $2$**, la chiffre la plus à gauche indique si le nombre codé est positif ou négatif :
    - $0$ si le nombre est positif
    - $1$ si le nombre est négatif.
- Alors, si on additionne deux positifs et le résultat a $1$ sur la position plus à gauche (est négatif), on l’appelle ***débordement***.
    - De même si on additionne deux négatifs et le résultat a un $0$ sur la position plus à gauche (est positif).
- Le débordement implique l'addition de chiffres obtenus ne peut pas être représenté avec la quantité de chiffres donnée.
- Additionner un positif et un négatif JAMAIS cause du débordement. Si on à une chiffre à gauche de plus, on appelle cela ***report***, mais on l'ignore et on reste avec le $n$ bits qu'on avait fixé.
- **Attention à ne pas confondre le $n^\text{ième}$ bit qui permet de repérer un débordement et le $(n+1)^\text{ième}$ bit qui est juste un report.**

## **Représentation des réels (*float*, *double*)**

### Passer de base $10$ à base $2$**, mais maintenant avec des réels**

[Explication plus complète en anglais.pdf](ressources/02_bases_numeriques_ieee_float.pdf)

- La représentation de réels en base $2$ est composée de trois segments de chiffres :
    - Le bit du signe, celui le plus a gauche, qui sera $0$ pour le positifs et $1$ pour les négatifs.
    - La mantisse, qui sont les premières chiffres "relevantes" du nombre.
        - La première chiffre à gauche doit être toujours $1$ et non $0$, et ce $1$ est suivi d'une virgule. Tout comme la notation scientifique. C'est pour cela qu'on omet le $1$ à gauche et on part tout de suite à la partie décimale, mais on la lit de gauche à droite.
    - L'exposant, qui serait la puissance de la base par laquelle on multiplie. Pense à la notation scientifique.
        - **Méthode de l'excédent** : on ajoute $2^{n-1}-1$ (la partie supérieure de l'intervalle) à notre exposant.
        - On remarque que, cette fois-ci, les négatifs ont un 0 sur le bit le plus à gauche et les positifs un 1.

#### Exemple pour tout clarifier : $23.75$ avec la méthode de l’exposant

#### Préparation

- On transforme $23.75$ à binaire, donc $10111.11$.
- Mettre en forme de notation scientifique : on décale la virgule jusqu'à qu'elle est devant le premier $1$, alors $1.011111$ (*forme de float*). On garde en compte la quantité de places décalées ($4$ dans ce cas) et donc on peut dire finalement que $23.75=(1.011111 \times 2^4)_2$

#### Conversion

- Le bit du signe est positif, alors $0$.
- Pour la mantisse, on ignore la première chiffre, de gauche a droite, de notre nombre réel en decimal (voir préparation), donc $1.011111 \mapsto 011111$.
- Pour l’excedent, on code la quantité de position qu'on a décalée (4 positions) dans l'exposant, avec la méthode de l'exposant. Alors, $\underbrace{00000100}_4 + \underbrace{01111111}_{(2^{n-1}-1 = 127)} = 10000011$. Ce dernier est notre ***excedent*** (à ne pas confondre avec exposant).

- On met tout ensemble :

$$\underbrace{0.}_\text{signe} - \underbrace{10000011}_\text{excedent} - \underbrace{(1.)011111}_\text{mantisse}$$

- On remplit le zéros à gauche selon la quantité de bits choisie pour la mantisse,  $0 - 10000011 - (1.)011111100000000000000000$.

### Deux cas particuliers avec l'exposant

- L'exposant $2^{n-1}$ (le nombre $111…111$ en binaire, tous $1$) est l'infini si la mantisse est nulle et NaN si la mantisse est non nulle.
- L'exposant $0$ est $0$ (qui ne peut pas s’écrire sous la forme 1,… ×2 …).

### Représentation des réels communes

- Le float : utilise 4 octets, dont 1 bit de signe, 8 bits d’exposant, 23 bits de mantisse.
- Le double : utilise 8 octets, dont 1 bit de signe, 11 bits d’exposant, 52 bits de mantisse
- Avec un float qui dispose de 8 bits pour l’exposant, on pourra donc représenter des exposants de −27 -2 à 27 -1, c’est-à-dire de −126 à +127.
- Si vous voulez représenter des nombres plus petits ou plus grands, il faudra choisir un double et non un float.
