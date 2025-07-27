# 04 // sémantiques des BNFs et arbres d’analyse

[chap4-4up.pdf](ressources/04_semantiques_des_bnfs_et_arbres_d’analyse_chap4-4up.pdf)

## Exo 4.4

<aside>
❓

Pour chacun des mots suivants, dessiner l’ensemble de ses arbres d’analyse puis la propagation d’attributs sur ces arbres d’analyse.

1. `I-I-I`
2. `(I-I)-I`
3. `I-(I-I)`
</aside>

![untitled.jpg](ressources/02_langages_algebriques_et_bnf_untitled.jpg)

![untitled.jpg](ressources/02_langages_algebriques_et_bnf_untitled_1.jpg)

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

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_2.jpg)

## Exo 4.7

<aside>
❓

Même exercice que le précédent pour cette BNF alternative du langage $L$ :
`L ::= a L b | B, B ::= b B | ε`

</aside>

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_3.jpg)

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

![image.png](ressources/04_semantiques_des_bnfs_et_arbres_d’analyse_image.png)

</aside>

## Exo 4.10

<aside>
❓

La BNF étant ambiguë, dessiner tous les arbres possibles du mot ‘`x # - x #`’, avec la propagation d’attributs.

![image.png](ressources/04_semantiques_des_bnfs_et_arbres_d’analyse_image_1.png)

</aside>

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_4.jpg)

## Exo 4.11

<aside>
❓

On considère que ‘`#`’ est prioritaire sur ‘`-`’ (qui est associatif a gauche). Quel est le résultat du calcul ?

</aside>

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_5.jpg)

## Exo 4.12

<aside>
❓

Appliquer cette méthode sur les BNF suivantes. On se limitera à se convaincre “à la main” de la non-ambiguıté sur quelques exemples.

1. l’exemple de l’introduction.
2. la BNF de la section 6.1 du sujet de TP.
</aside>

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_6.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_7.jpg)

## Exo 4.13

<aside>
❓

Trouver une BNF pour le langage $A ∪ B$. Montrer que cette BNF est ambigue.

![image.png](ressources/04_semantiques_des_bnfs_et_arbres_d’analyse_image_2.png)

</aside>

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_8.jpg)