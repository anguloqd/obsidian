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

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled.jpg)

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

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%201.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%202.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%203.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%204.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%205.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%206.jpg)

![Untitled.jpg](ensimag/first_year/école/1AA%20info%20grammaires%20et%20compilation/05%20théories%20de%20grammaires%20et%20du%20parsing/Untitled%207.jpg)