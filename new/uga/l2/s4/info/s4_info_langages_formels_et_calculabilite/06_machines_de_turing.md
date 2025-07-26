# 06 // machines de Turing

Date de création: April 17, 2023 3:04 PM
Modifié: June 10, 2023 12:34 PM

[Slides du chapitre 6](chapitre_6_compressed.pdf)

# Définition intuitive

## C’est quoi le but ?

Elle est basée sur l'idée d'une personne exécutant une procédure bien définie qui change le contenu d'un ruban de papier infini, qui est divisé en cases, chaque case contenant un symbole issu d'un ensemble fini de symboles.

Les Machines de Turing n’étaient pas supposées être une technologie informatique opérationnelle, pratique et performante, mais plutôt **une étude des limites du calcul mécanique**, donc elles n’ont pas réellement été construites. Cependant, l'étude des propriétés abstraites des Machines de Turing aide à comprendre des aspects de l'informatique et de la théorie de la complexité.

# Similarités et différences entre MT et AEF/AAP

## Similarités

Une Machine de Turing garde plusieurs similitudes avec les AEF :

- Un ruban fini à gauche et infini vers la droite
- Une tête de lecture
- $Q$ : ensemble fini d’états
- $\Gamma$ : un alphabet fini de symboles à lire
- $q_0$ : un état initial

## Différences

Les différences avec les AEF/AAP sont :

- Par rapport aux états :
    - Un seul état d’arrêt (”halt”) $h\in Q$, forcément différent de l’état initial $q_0$, qui forcément finit le processus une fois atteint
        - Pour les AEF/AAP, les état d’arrêt peuvent être plusieurs, inclure l’état initial et même continuer à lire si on rentre sur un état d’arrêt (l’arrêt est optionnel)
- Par rapport au déplacement sur la bande :
    - La capacité d’écrire sur la bande, en plus de lire
    - La capacité de se déplacer vers la gauche sur le ruban, ainsi qu’à droite
- Par rapport aux symboles :
    - L’ensemble des symboles du ruban $\Gamma$ inclut tous les symboles que la machine peut écrire $\Sigma$ et aussi le symbole vide $\#$. La machine ne peut pas écrire le symbole vide.

Le fait de pouvoir écrire sur la bande rend une pile de stockage innecéssaire : la bande sert de moyen de lecture et de stockage auxiliaire. 

# Transitions dans une Machine de Turing

## Opérations

Les Machines de Turing ont seulement deux types d’opération : l’écriture et le déplacement.

- Écriture : remplacer un symbole sur le ruban ET changer d’état.
- Déplacement : déplacer d’une cellule à droite/gauche et changer d’état.

Donc, si la machine a changé d’état, elle a effectué l’une de ces deux opérations. L’action suivante de la machine est determiné par **l’état actuel $q_A$** et **le symbole actuel** $x_A$ sous la tête de lecture, càd. l’action suivante est la correspondance d’une fonction qui prend des couples $(q_A, x_A)$.

## Fonction de transition $\delta$

Il existent deux versions pour l’écrire : les “quintuplets”, où on correspond une couple avec un triplet ; et les “quadruplets”, où on correspond une couple à une autre couple. Je préfère les quadruplets, mais le résultat est le même.

$$
\delta : \left\{(Q-\{h\})\times \Gamma\right\} \mapsto \left\{Q\times (\Gamma\cup\{G,D\})\right\}
$$

Ici, $G$ et $D$ ne sont pas de symboles de $\Gamma$ mais des déplacement à gauche et droite, respectivement. Il existe trois possibilités de correspondance alors :

1. $(q_1, x_1) \mapsto (q_2, x_2)$ : dans l’état $q_1$ et lisant le symbole $x_1$, on remplace le symbole $x_1$ avec le symbole $x_2$ et on passe à l’état $q_2$.
2. $(q_1, x_1) \mapsto (q_2, G)$ : dans l’état $q_1$ et lisant le symbole $x_1$, on se déplace une cellule/case à **gauche** et on passe à l’état $q_2$. 
3. $(q_1, x_1) \mapsto (q_2, D)$ : dans l’état $q_1$ et lisant le symbole $x_1$, on se déplace une cellule/case à **droite** et on passe à l’état $q_2$.

**Note** : pour arriver à l’état final, on note $(q_1,x_1) \mapsto (h,a)$, où $a$ est une action quelle conque. On peut écrire un symbole avant d’arrêter la machine, on peut aussi déplacer avant de l’arrêter.

# Diagrammes de transition pour les Machines de Turing

## Quadruplets et quintuplets

Il existe également deux notations différentes, qu’on trouve en tant qu’étiquettes des arcs :

1. $x/a$ (quadruplets) : $x$ est le symbole sous la tête de lecture, $a$ est l’action à effectuer
2. $x/y/d$ (quintuplets) : $x$ est le symbole sous le tête de lecture, $y$ est le symbole à écrire sur la case, $d$ est le déplacement. Pour cette notation, on peut faire un déplacement sans écriture en reécrivant le même symbole, donc $x/x/d$.

![Exemple avec la notation $x/a$. Cette machine ne fais que lire (aucune écriture) des ‘a’ et ‘b’ en se déplaçant à droite après chaque lecture, jusqu’à ce qu’elle rencontre un vide $\#$, où elle rentre dans l’état final et elle s’arrete.](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/06_machines_de_turing/untitled.png)

Exemple avec la notation $x/a$. Cette machine ne fais que lire (aucune écriture) des ‘a’ et ‘b’ en se déplaçant à droite après chaque lecture, jusqu’à ce qu’elle rencontre un vide $\#$, où elle rentre dans l’état final et elle s’arrête.

![Exemple avec la notation $x/y/d$.](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/06_machines_de_turing/untitled_1.png)

Exemple avec la notation $x/y/d$.

# Définition formelle

## Définition et notes

Formellement, une Machine de Turing $T$ est donc :

$$
T=\{Q, q_0\in Q, h\in Q, \Gamma,\Sigma,\delta\}
$$

Normalement, une Machine de Turing démarre dans son état initial et exécute des transitions jusqu'à ce que son état d'arrêt soit atteint. **Deux notes importantes sont à faire :**

1. L’état d’arrêt peut ne jamais être atteint : il se peut que la machine entre dans une boucle infini.
2. La machine peut terminer anormalement si elle essaye de déplacer la tête de lecture au-delà de l’extrémité gauche du ruban.

## Grammaires et automates

![untitled](new/uga/l2/s4/info/s4_info_langages_formels_et_calculabilite/06_machines_de_turing/untitled_2.png)

# Conclusion

## Un peu d’histoire

Turing a présenté ces idées sur les machines de calcul en 1936. Ce travail **précède** les travaux sur les automates finis et automates à piles. À différence de ce cours, il n'essayait pas d'étendre des modèles plus simples (comme nous), mais il essayait d'exprimer de la manière la plus simple l'essence même du calcul. Le modèle de Turing était celui d’un humain essayant, avec un crayon et du papier, d'effectuer un calcul.

Personne n'a encore découvert de modèle de calcul plus puissant et le consensus est qu'il n'en existe pas. La **thèse de Turing** est que la puissance de calcul des Machines de Turing est au moins égale à celle de tout système de calcul possible.