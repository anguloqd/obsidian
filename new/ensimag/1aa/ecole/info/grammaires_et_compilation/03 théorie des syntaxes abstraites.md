# 03 // théorie des syntaxes abstraites

Date de création: January 11, 2025 5:22 PM
Modifié: January 25, 2025 8:10 PM

[chap3-4up.pdf](chap3-4up.pdf)

## Exo 3.1

<aside>
❓

Dessiner l’AST de l’expression régulière “$b + (a.a.(ϵ + a)^∗)$”. Coder cet AST en notation préfixe (suite d’appels des constructeurs sans parenthèse).

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled.jpg)

## Exo 3.2

<aside>
❓

Dessiner l’AST encodé par le mot “`star u dot a b a`”, en “notation naturelle”, puis en “notation étendue”, où chaque nœud est un type d’AST et a un enfant supplémentaire (a gauche) : le nom du constructeur.

</aside>

En notation naturelle, pour chaque opération binaire, les deux mots suivants sont leurs arguments. Pareil pour les opérations unaires.

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%201.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%202.jpg)

## Exo 3.3

<aside>
❓

Donner une BNF qui définit cette notation préfixe d’AST (la notation étendue de Rexp dans l’exo précédent).

</aside>

`Rexp ::= void | epsilon | a | b | star.Rexp | u.Rexp.Rexp | dot.Rexp.Rexp` 

## Exo 3.4

<aside>
❓

Appliquer cette idée avec :

- $D = \mathcal P(V^∗)$ pour la sémantique des $\bold{Rexp}$ (comme ensemble de mots)
- $D =$ ensemble des automates finis (non-déterministes avec $ϵ$-transitions) pour générer l’automate associé à une $\bold{Rexp}$. Calculer l’automate de $A_\text{dot}(A_a, A_a)$ avec vos définitions
</aside>

![WhatsApp Image 2025-01-12 at 19.49.07.jpeg](WhatsApp_Image_2025-01-12_at_19.49.07.jpeg)

![WhatsApp Image 2025-01-12 at 19.53.50.jpeg](WhatsApp_Image_2025-01-12_at_19.53.50.jpeg)

![WhatsApp Image 2025-01-12 at 19.54.32.jpeg](WhatsApp_Image_2025-01-12_at_19.54.32.jpeg)

![WhatsApp Image 2025-01-12 at 19.55.00.jpeg](WhatsApp_Image_2025-01-12_at_19.55.00.jpeg)

![WhatsApp Image 2025-01-12 at 19.55.21.jpeg](WhatsApp_Image_2025-01-12_at_19.55.21.jpeg)

![WhatsApp Image 2025-01-12 at 19.55.35.jpeg](WhatsApp_Image_2025-01-12_at_19.55.35.jpeg)

## Exo 3.5

<aside>
❓

Dessiner la propagation de l’attribut sur l’AST (en notation étendue) encodé par le mot “`star u dot a b a`”

</aside>

![WhatsApp Image 2025-01-12 at 19.56.50.jpeg](WhatsApp_Image_2025-01-12_at_19.56.50.jpeg)

![WhatsApp Image 2025-01-12 at 19.56.50(1).jpeg](WhatsApp_Image_2025-01-12_at_19.56.50(1).jpeg)

![WhatsApp Image 2025-01-12 at 19.56.49(2).jpeg](WhatsApp_Image_2025-01-12_at_19.56.49(2).jpeg)

![WhatsApp Image 2025-01-12 at 19.56.49.jpeg](WhatsApp_Image_2025-01-12_at_19.56.49.jpeg)

![WhatsApp Image 2025-01-12 at 19.56.49(1).jpeg](WhatsApp_Image_2025-01-12_at_19.56.49(1).jpeg)

![WhatsApp Image 2025-01-12 at 19.56.49(3).jpeg](WhatsApp_Image_2025-01-12_at_19.56.49(3).jpeg)

## Exo 3.6

<aside>
❓

Soient les arbres binaires de sorte $B$ engendrés par constructeurs “$l : B$” et “$n : B × B → B$”.

Dans chacun des cas ci-dessous, définir système d’attributs qui :
— compte le nombre de feuilles (noeuds `l`) dans l’arbre.
— indique si toutes les feuilles de l’arbre sont à une profondeur $h$ ou $h − 1$, avec $h$ paramètre donné (par convention, feuille est de hauteur $0$).

Appliquer les algorithmes sous-jacents sur les exemples ci-dessous en dessinant la propagation d’attributs sur chaque nœuds (les exos en format String sont écrit en notation naturelle, et les résultats doivent être en arbre étendu) :
— `n l n n l l n l l`
— `n n l l n n l l n l l`

pour Q2, on prendra $h$ valant à la racine $2$, puis ensuite $3$.

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%203.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%204.jpg)

## Exo 3.7

<aside>
❓

On considère le système donné à la tâche 4 du TP.

1. Soit $p$ l’AST “`and var 1 neg var 2`”.
Calculer le r retourné une dérivation de “`p↓1↑r` ”.
2. Calculer la NNF attendue pour “`-(((t&1)>(-2|f))&3)`”.
</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%205.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%206.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%207.jpg)

## Exo 3.9

<aside>
❓

Donner le système d’équations algébrique associé a cette signature $Σ_{TP}$ . Exprimer ce système en syntaxe BNF avec attributs : pour se ramener a un ensemble fini de constructeurs, on placera $\N\backslash{0}$ en attribut synthétisé du constructeur $var$.

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/03%20théorie%20des%20syntaxes%20abstraites/Untitled%208.jpg)

## Exo 3.10

<aside>
❓

Définir une signature pour NNF avec sortes Nnf et Ncst, puis la BNF associée

</aside>

![Untitled.jpg](Untitled%209.jpg)

## Exo 3.13

<aside>
❓

Pouvez-vous construire le terme sur $Σ_{AST}$ associé aux mots suivants en notation préfixe :

1. `& & - & 1 - 2 | - 2 3 | t - 3`
2. `& & - & 1 - 2 | - 2 3`
</aside>

![Untitled.jpg](Untitled%2010.jpg)

## Exo 3.14

<aside>
❓

Calculer la suite des tokens pour :

1. `123&27|-4_t_6_5_`
2. `___tx2`
</aside>

(J’ai pas pris des photos ?)

## Exo 3.15 et 3.16

<aside>
❓

Donner la suite token attribuées `de “&_-_&_123_-_2|_-_2_3`” puis en construire l’arbre d’analyse Parse avec propagation d’attributs.

Dessiner l’arbre des appels récursifs de `parse_rec` sur le mot “`& - & 123 - 2 | - 2 3`”.

</aside>

![Untitled.jpg](Untitled%2011.jpg)