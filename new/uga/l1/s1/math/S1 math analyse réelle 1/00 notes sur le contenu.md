# 00 //  notes sur le contenu

Date de création: December 23, 2021 12:20 AM
Modifié: May 30, 2023 2:03 AM

## #2 : les nombres réels

- Définir N en termes de ε :
    - Max() ou Min()
    - Abs()
    - E(f(ε))
    - Fonction par branches
    - etc.

## #3 : suites réelles

- Multiplier par l'expression conjuguée.
    - Même si l'expression avec racine est dans le numérateur !
- Rappel que tu peux fixer ton $N$ dépendant si ton minorant/majorant ("... pour tout $m$ réel") est positif ou négatif (disjonction de cas). Ça simplifie la vie.

## #4 : convergence des suites

- **RÉPOND EXACTEMENT CE QU'ON TE DEMANDE !**
- Preuve directe : manipulation algébrique -> tautologie.
- Preuve par récurrence :
    - **Utilise l'hypothèse de récurrence !!!**
    - **Même, utilise-la au milieu de la manip. alg.**
    - Transitivité d'inégalités pour les termes et limites.
    - Théorème des gendarmes.
- Preuve de la contraposée.
- Preuve par l'absurde.
- Limites :
    - "Par somme", "par quotient", "par différence", "par composition"...
    - Factorise des termines qui n'existent pas dans les racines.
    - Pour les suites récurrentes :
        - Définir grand $N$ est inutile. Il faut plutôt utiliser le fait que c'est une suite croissante/décroissante, construire $u_{n+1}$, ou d'autres infos.
        - Si tu dois montrer convergence, rappel aussi d'utiliser le fait de **(bornée + croissante/décroissante)**.
        - Ok, définir grand $N$ n'est pas tout le temps inutile. Parfois, si on définit $N = E(f(\varepsilon))$, on termine avec $N \le f(\varepsilon) \le N + 1$, c'est qui est utile pour lier $N$ avec $U_n$.
- Convergence :
    - Si $(u_n)$ croissante et sa borne est positive, alors il y aura un certain $n$ pour lequel $n = M$.
    - C'est un bon fait de savoir si $u_n > n$ ou le contraire.
    - C'est la même chose si $(u_n)$ décroissante et sa borne est négative, donc il y aura un certain $n$ pour lequel $-n = m$.