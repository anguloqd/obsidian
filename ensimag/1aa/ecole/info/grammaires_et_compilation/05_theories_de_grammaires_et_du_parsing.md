## 05 // théories de grammaires et du parsing

[chap5_4up.pdf](ressources/05_theories_de_grammaires_et_du_parsing_chap5_4up.pdf)

### Exo 5.3

> [!question] ❓
>
> Appliquer cette méthode sur la BNF :
>
> - `S ::= X a | S X
> X ::= b S | ϵ`

![untitled.jpg](ressources/02_langages_algebriques_et_bnf_untitled.jpg)

### Exo 5.4

> [!question] ❓
>
> Idem en remplaçant l’équation de `S` ci-dessus par `S ::= X a | X`

Facile à faire à partir de la réponse en haut.

### Exo 5.5

> [!question] ❓
>
> Pour chacune des 4 grammaires ci-dessous du langage $\{a^n b^m | 0 ≤ n ≤ m\}$. Calculer le directeur de chacune des règles. Quelles grammaires sont $LL(1)$ ?
>
> 1. `S → a S B | ϵ | B`
> `B → b B | b`
> 2. `S → a S b B | B
> B → b B | ϵ`
> 3. `S → a S b | B
> B → b B | ϵ`
> 4. `S → A B
> A → a A b | ϵ
> B → b B | ϵ`

![untitled.jpg](ressources/02_langages_algebriques_et_bnf_untitled_1.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_2.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_3.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_4.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_5.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_6.jpg)

![untitled.jpg](ressources/03_theorie_des_syntaxes_abstraites_untitled_7.jpg)
