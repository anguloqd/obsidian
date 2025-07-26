# 05 // théories de grammaires et du parsing

Date de création: January 11, 2025 5:24 PM
Modifié: January 26, 2025 3:47 PM

[chap5-4up.pdf](chap5-4up.pdf)

## Exo 5.3

<aside>
❓

Appliquer cette méthode sur la BNF :

- `S ::= X a | S X 
 X ::= b S | ϵ`
</aside>

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled.jpg)

## Exo 5.4

<aside>
❓

Idem en remplaçant l’équation de `S` ci-dessus par `S ::= X a | X`

</aside>

Facile à faire à partir de la réponse en haut.

## Exo 5.5

<aside>
❓

Pour chacune des 4 grammaires ci-dessous du langage $\{a^n b^m | 0 ≤ n ≤ m\}$. Calculer le directeur de chacune des règles. Quelles grammaires sont $LL(1)$ ?

1. `S → a S B | ϵ | B`
`B → b B | b`
2. `S → a S b B | B
B → b B | ϵ`
3. `S → a S b | B
B → b B | ϵ`
4. `S → A B
A → a A b | ϵ
B → b B | ϵ`
</aside>

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_1.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_2.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_3.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_4.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_5.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_6.jpg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/05_theories_de_grammaires_et_du_parsing/untitled_7.jpg)