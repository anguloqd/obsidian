# 04 // sémantiques des BNFs et arbres d’analyse

Date de création: January 11, 2025 5:23 PM
Modifié: January 26, 2025 12:46 PM

[chap4-4up.pdf](chap4-4up.pdf)

## Exo 4.4

<aside>
❓

Pour chacun des mots suivants, dessiner l’ensemble de ses arbres d’analyse puis la propagation d’attributs sur ces arbres d’analyse.

1. `I-I-I`
2. `(I-I)-I`
3. `I-(I-I)`
</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%201.jpg)

## Exo 4.5

<aside>
❓

Donner tous les arbres d’analyse du mot `abbb` pour la BNF du langage $L$ suivante: `L ::= a L b | L b | ε`

</aside>

## Exo 4.6

<aside>
❓

Donner tous les arbres d’analyse du mot `abbb` pour la BNF du langage $L$ suivante: `L ::= L b | A`, `A ::= a A b | ε`

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%202.jpg)

## Exo 4.7

<aside>
❓

Même exercice que le précédent pour cette BNF alternative du langage $L$ :
`L ::= a L b | B, B ::= b B | ε`

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%203.jpg)

## Exo 4.8

<aside>
❓

Parenthésage explicite de “`− 1 | 2 & 3`” ?

</aside>

Je l’ai pas je crois.

## Exo 4.9

<aside>
❓

Avec ce système d’attributs, quel arbre d’analyse associer a “`I--I-I`” pour que le résultat corresponde à la convention usuelle.

![image.png](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/image.png)

</aside>

## Exo 4.10

<aside>
❓

La BNF étant ambiguë, dessiner tous les arbres possibles du mot ‘`x # - x #`’, avec la propagation d’attributs.

![image.png](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/image%201.png)

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%204.jpg)

## Exo 4.11

<aside>
❓

On considère que ‘`#`’ est prioritaire sur ‘`-`’ (qui est associatif a gauche). Quel est le résultat du calcul ?

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%205.jpg)

## Exo 4.12

<aside>
❓

Appliquer cette méthode sur les BNF suivantes. On se limitera à se convaincre “à la main” de la non-ambiguıté sur quelques exemples.

1. l’exemple de l’introduction.
2. la BNF de la section 6.1 du sujet de TP.
</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%206.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%207.jpg)

## Exo 4.13

<aside>
❓

Trouver une BNF pour le langage $A ∪ B$. Montrer que cette BNF est ambigue.

![image.png](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/image%202.png)

</aside>

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/04%20sémantiques%20des%20BNFs%20et%20arbres%20d’analyse/Untitled%208.jpg)