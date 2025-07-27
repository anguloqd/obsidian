# 02 // l’algèbre relationnelle

[Slides d’algèbre relationnelle](ressources/02_l’algebre_relationnelle_02.algebre.pdf)

# L’algèbre relationnelle

## Rappel d’algèbre

Une algebre est un ensemble d’opérateurs de base formellement définis, qui peuvent être combinés à souhait pour construire des expressions algébriques. Par exemple :

- Les opérateurs arithmétiques : $+$ ,$-$ , $\times$, $/$, etc.
- Les opérateurs logiques :  $\land \space$, $\lor$, $\neg$.

Chaque opérateur a une arité, càd. une quantité d’éléments avec lesquels faire l’opération, appelés *opérandes* :

- Opérateurs binaires : $+$ ,$-$ , $\times$, $/$
- Opérateurs unaires : $\neg$

Ils existent aussi des règles intuitives de constructions des opérateurs, ou simplement des *axiomes* :

- Pour $+$ et $\times$ : associativité, commutativité, distributivité.
- Pour $\land$ et $\lor$ : lois de Morgan

Finalement, une algèbre est dite *fermée* si le résultat de toute opération est du même type que les opérandes (ce qui est indispensable pour construire des expressions).

## Le cas de “l’algèbre de tableaux”

L’algèbre relationnelle est une collection d’opérateurs algébriques unaires ou binaires qui peuvent se combiner entre eux. Un requête relationnelle est la composition d’un nombre fini d’opérateurs algébriques. Il faut noter que l’ordre d’évaluation des opérateurs a un impact sur le temps de réponse du SGBD.

## Opérateurs

### Opérateurs ensemblistes

### L’union $R \cup S$

Supposant deux tables avec les même schéma (même composition d’attributs ou colonnes), leur union $R\cup S$ est simplement une nouvelle table avec les entrées de $R$, puis celles de $S$. Il n’y pas des entrées dupliquées dans la table finale $T$.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled.png)

### L’intersection $R \cap S$

Pareil avec l’intersection, supposant deux tables avec le même schéma, leur intersection sont les entrées qui apparaissent dans $R$ et $S$ aussi.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_1.png)

### La différence $R - S$

Encore avec la différence, avec deux tables similaires, la différence de $R$ avec $S$ sont les entrées qui apparaissent dans $R$ et pas dans $S$.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_2.png)

### Le complément $-R$

Finalement, prenant une table $R$, son complément $-R$ sont toutes les possibles combinaisons de valeurs qui apparaissent dans chaque attribut de $R$, mais qui ne constituent pas une tuple dans $R$.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_3.png)

### Opérateurs proprement relationnels

### La projection $R[A]$

C’est une opération qui prend comme argument une table $R$, un ensemble d’attributs (colonnes) $A$ et retourne la relation (table) réduite à ces colonnes.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_4.png)

### La sélection $R : C$

Cette opération prend une table $R$, une condition ou proposition $C$ et retourne la table seulement avec les lignes qui vérifient la condition.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_5.png)

Si aucune ligne vérifie la condition, on peut retourne la table vide. Par exemple, supposons que $C$ est (Nom $=$ “Marie” $\land$ Salaire $<$ 3000 $\land$ Adresse $≠$ “St-Egrève”) :

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_6.png)

### Le produit cartésien $R \times S$

L’opérateur prend deux tables $R$ et $S$ et retourne une table $T=R \times S$ qui concatène, gardant l’ordre de gauche à droite. chaque $n$-ième ligne de $R$ avec la $n$-ième ligne de $S$.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_7.png)

### La jointure $R(C) \times S$

C’est tout simplement la concaténation des lignes en ordre de $R$ et $S$ telles qu’elles vérifient la condition $C$. Notons que c’est exactement la même chose que $(R \times S) : C$.

![untitled](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_8.png)

Par exemple, la jointure “Employee $\bowtie$ Dept” pourrait se décrire de deux manières : $E(\text{E.DeptName} = \text{D.DeptName}) \times D$ ou aussi $E \times D : (\text{E.DeptName} = \text{D.DeptName})$.

Il existent deux types de jointure : la jointure *naturelle* ($\bowtie$), quand la condition $C$ est un test d’égalité ; où la jointure $\theta$ ($\bowtie_\theta$) pour tout autre test ou condition différent d’une égalité. La jointure de l’exemple en-dessus est une jointure naturelle.

### La division $R / S$

Cette opération peut être divisée en deux étapes. On prend deux tables $R$ et $S$ :

1. Les attributs de $T = R/S$ seront les attributs de $R$ qui ne sont pas dans $S$.
2. Les lignes ou entrées de $T$ seront tels tuples dont toutes les possibles combinaisons avec les tuples de $S$ sont présentes dans la table de départ $R$.

![Seulement X=1 a des combinaisons avec les pairs de Y et Z (2,3) et (56).](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_9.png)

Seulement X=1 a des combinaisons avec les pairs de Y et Z (2,3) et (5,6).

![Seulement Fred et Sarah ont de combinaisons avec les deux Database1 et Database2 dans la table completed.](new/uga/l2/s4/info/s4_info_intro_aux_bases_de_donnees/ressources/02_l’algebre_relationnelle_untitled_10.png)

Seulement Fred et Sarah ont de combinaisons avec les deux Database1 et Database2 dans la table Completed.

## Optimisation des requêtes avec des opérations

L’ordre dans lequel s’effectue les opérateurs ont un impact sur les performances des SGBD. Le standard c’est de les effectuer suivant cet ordre :

1. Sélections (qui diminuent beaucoup la taille des tables)
2. Projections (qui diminuent un peu la taille des tables)
3. Jointures et produits (qui augmentent beaucoup la taille des tables)