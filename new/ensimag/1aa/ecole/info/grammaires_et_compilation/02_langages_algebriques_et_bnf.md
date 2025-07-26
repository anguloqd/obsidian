# 02 // langages algébriques et BNF

Date de création: January 11, 2025 5:21 PM
Modifié: January 16, 2025 3:40 PM

[chap2-4up.pdf](chap2-4up.pdf)

## Exo 2.1

<aside>
❓

Soit $V$ un vocabulaire fini. Soient $A, B \subseteq V^*$. Quel est le plus petit ensemble $X \subseteq V^*$ tel que $X = A.X \cup B$ ?

</aside>

$X = A^*B$, d’après le lemme d’Arden.

## Exo 2.2

<aside>
❓

Dessiner le diagramme de Hasse de $P(\{1, 2, 3, 4\})$.

</aside>

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/02_langages_algebriques_et_bnf/untitled.jpg)

## Exo 2.8

<aside>
❓

Soit $f : X \rightarrow \{a\}.X.\{b\} \cup \{\epsilon\}$ (pour $X \subseteq \{a, b\}^*$). Que vaut $f^i(\emptyset)$ pour $i \in \mathbb{N}$ ? Que vaut $\bigcup_{i\in\mathbb{N}} f^i (\emptyset)$ ?

</aside>

Pour $i = 0$, $f^0(\empty) = \empty$. Pour $i=1, f(\empty) = \{\epsilon\}$. Pour $i=2$, $f^2(\empty) = \{ab\} \cup \{\epsilon\}$. Pour $i = 3$, $f^3(\empty] = \{\epsilon\} \cup \{ab\} \cup \{aabb\}$. 

Premier résultat: $f^n(\empty) = \left\{ a^i b^i : i < n \right\}$
Deuxième résultat: $\bigcup_{i\in\mathbb{N}} f^i (\emptyset) = \{a^n b^n : n \in \N \}$

## Exo 2.11 et 2.13

<aside>
❓

Soit $\mathbb{N}_1 = \mathbb{N} \setminus \{0\}$ et soit $V = \{-, \&, |, >, t, f\} \cup \mathbb{N}_1$.

Définir par plus petit point fixe, l'ensemble des mots de $V^*$ qui correspondent à la notation préfixe d'une formule propositionnelle (cf. syntaxe du TP). On doit trouver un $f$ tel que le langage recherché est $\lim_{h\rightarrow+\infty} f^h(\emptyset)$.

</aside>

Définition du problème :

Un mot sur l'alphabet $V$ représente une formule propositionnelle en notation préfixe si :

1. Une constante propositionnelle ou un entier de $\mathbb{N}_1$ est une formule valide.
2. Un opérateur unitaire ($-$) suivi d'une formule valide est une formule valide.
3. Un opérateur binaire ($\&$, $|$, $>$) suivi de deux formules valides est une formule valide.

On cherche une fonction $f : 2^{V^*} \to 2^{V^*}$ telle que le langage $L_{\text{préfixe}}$ est donné par le plus petit point fixe de $f$, i.e.,

$$
L_{\text{préfixe}} = \lim_{h \to +\infty} f^h(\emptyset)
$$

Définition de $f$ :
Soit $X \subseteq V^*$, $f(X)$ est défini comme l'ensemble des mots construits selon les règles suivantes :

1. Tout mot de longueur 1 correspondant à une constante propositionnelle ($t, f$) ou un entier ($n \in \mathbb{N}_1$) est dans $f(X)$ :
$\{t, f\} \cup \mathbb{N}_1 \subseteq f(X).$
2. Si $u \in X$ est une formule valide, alors $-u$ est une formule valide :
$\{-u \mid u \in X\} \subseteq f(X).$
3. Si $u, v \in X$ sont des formules valides, alors $ouv$ sont des formules valides pour tout $o \in \{\&, |, >\}$ :
$\{ouv \mid o \in \{\&, |, >\}, u \in X, v \in X\} \subseteq f(X).$

En résumé :

$$
f(X) = \{t, f\} \cup \mathbb{N}_1 \cup \{-u \mid u \in X\} \cup \{ouv \mid o \in \{\&, |, >\}, u, v \in X\}
$$

<aside>
❓

Définir par plus petit point fixe, l'ensemble des mots de $(V \cup \{(, )\})^*$ qui correspondent à la notation **infixe** d'une formule propositionnelle (cf. syntaxe du TP).

</aside>

Très pareil à l’exo précédent, mais on change deux choses :

- Pour les expressions d’arité 2, on va mettre l’opérateur au milieu, plutôt qu’au début. $\{uov \mid o \in \{\&, |, >\}, u \in X, v \in X\} \subseteq f(X)$
- Une autre formule devient valide: $\{ (u) \mid u \in X\}$

D’où, la fonction $f$ est telle que :

$$
⁍
$$

## Exo 2.14 et 2.15

<aside>
💡

**Lemme de commutation**. Pour $k \in \{1, 2\}$, soient $f_k$ applications continues de $P(E_k) \rightarrow P(E_k)$, et $g$ application de $P(E_1) \rightarrow P(E_2)$ telle que $g \circ f_1 = f_2 \circ g$. Si $f_2$ a un unique point-fixe ou si $g$ continue et $g(\emptyset) = \emptyset$, alors :

$$
g\left(\lim_{i\rightarrow+\infty} f^i_1(\emptyset)\right) = \lim_{i\rightarrow+\infty} f^i_2(\emptyset)
$$

</aside>

<aside>
❓

Soient $A, B \subseteq V^*$ et $E_1 = V^*$. Pour $f_1(X) = A.X.B \cup B^*$ et $g(X) = \{\epsilon\}\setminus X$, montrer $g(\lim_{i\rightarrow+\infty} f^i_1(\emptyset)) = \emptyset$.

</aside>

**Preuve :**

1. D'après la définition de $f_1$ :
    - $f_1(X) = A.X.B \cup B^*$.
    - Le point fixe de $f_1$ est $\lim_{i \to +\infty} f^i_1(\emptyset) = A^*.B^*$.
2. Définissons $g(X) = \{\epsilon\} \setminus X$. Clairement, $g(\emptyset) = \{\epsilon\}$ et $g$ est continue.
3. Vérifions la commutation de $g$ avec $f_1$ et $f_2$ :
    - Soit $f_2(Y) = g(f_1(g^{-1}(Y)))$
    - Cela implique que $f_2(\{\epsilon\}) = g(f_1(\emptyset)) = \emptyset$ car $f_1(\emptyset) = B^*$ *et* $g(B^*) = \emptyset$
4. Par le lemme de commutation, comme $g$ est continue et $g(\emptyset) = \emptyset$, on a :
$g(\lim_{i \to +\infty} f^i_1(\emptyset)) = \lim_{i \to +\infty} f^i_2(\emptyset) = \emptyset$

**Conclusion :** $g(\lim_{i \to +\infty} f^i_1(\emptyset)) = \emptyset.$

<aside>
❓

Soient $f_1(X) = A.X \cup \{\epsilon\}$ et $f_2(Y) = A.Y \cup B$. Par définition $A^* = \lim_{i\rightarrow+\infty} f^i_1(\emptyset)$. En appliquant le lemme de commutation, redémontrer $A^*.B = \lim_{i\rightarrow+\infty} f^i_2(\emptyset)$ (lemme d'Arden).

</aside>

**Preuve :**

1. D'après la définition de $f_1$ et $A^*$ :
    - $f_1(X) = A.X \cup \{\epsilon\}$.
    - Par récurrence, $f^i_1(\emptyset)$ génère des éléments de la forme $A^i$.
    - Le point fixe est $\lim_{i \to +\infty} f^i_1(\emptyset) = A^*$.
2. D'après la définition de $f_2$, on a :
    - $f_2(Y) = A.Y \cup B$.
    - Par récurrence, $f^i_2(\emptyset)$ génère des éléments de la forme $A^i.B$.
    - Le point fixe est $\lim_{i \to +\infty} f^i_2(\emptyset) = A^*.B$.
3. Définissons $g(X) = X.B$. Vérifions que $g$ commute avec $f_1$ et $f_2$ :
    - $g(f_1(X)) = g(A.X \cup \{\epsilon\}) = A.(X.B) \cup B = f_2(g(X)).$
4. Par le lemme de commutation :
$g\left(\lim_{i \to +\infty} f^i_1(\emptyset)\right) = \lim_{i \to +\infty} f^i_2(\emptyset).$
5. Comme $g(X) = X.B$ et $\lim_{i \to +\infty} f^i_1(\emptyset) = A^*$*,* on a : $g(A^*) = A^*.B.$
6. Ainsi : $A^*.B = \lim_{i \to +\infty} f^i_2(\emptyset).$

**Conclusion :**
En appliquant le lemme de commutation, on a redémontré que $A^*.B = \lim_{i \to +\infty} f^i_2(\emptyset)$.

## Exo 2.16

<aside>
❓

Soit le système suivant sur $\{a, b\}^* \times \{a, b\}^*$ :
$X_1 = \{b\} \cup X_2.X_2$
$X_2 = \{a\}.X_1$
Calculer $f^4(\emptyset, \emptyset)$

</aside>

**Définition de** $f$ **:**
La fonction $f$ agit sur des couples $(X_1, X_2)$, et est définie comme : $f(X_1, X_2) = \left( \{b\} \cup X_2.X_2, \{a\}.X_1 \right)$.

On calcule les itérations de $f$ à partir du couple initial $(\emptyset, \emptyset)$.

**Calcul de** $f^1(\emptyset, \emptyset)$ **:**
$f^1(\emptyset, \emptyset) = \left( \{b\} \cup \emptyset.\emptyset, \{a\}.\emptyset \right).$
$f^1(\emptyset, \emptyset) = \left( \{b\}, \emptyset \right)$

**Calcul de** $f^2(\emptyset, \emptyset)$ **:**
$f^2(\emptyset, \emptyset) = f(f^1(\emptyset, \emptyset)) = f(\{b\}, \emptyset)$

Pour $X_1 = \{b\}$ et $X_2 = \emptyset$ :
$f(\{b\}, \emptyset) = \left( \{b\} \cup \emptyset.\emptyset, \{a\}.\{b\} \right)$
$f^2(\emptyset, \emptyset) = \left( \{b\}, \{ab\} \right)$

**Calcul de** $f^3(\emptyset, \emptyset)$ **:**
$f^3(\emptyset, \emptyset) = f(f^2(\emptyset, \emptyset)) = f(\{b\}, \{ab\})$

Pour $X_1 = \{b\}$ et $X_2 = \{ab\}$ :
$f(\{b\}, \{ab\}) = \left( \{b\} \cup \{ab\}.\{ab\}, \{a\}.\{b\} \right)$

Calculons chaque terme :

- $\{ab\}.\{ab\} = \{abab\}$
- $\{b\} \cup \{abab\} = \{b, abab\}$
- $\{a\}.\{b\} = \{ab\}$
Donc :
$f^3(\emptyset, \emptyset) = \left( \{b, abab\}, \{ab\} \right)$

**Calcul de** $f^4(\emptyset, \emptyset)$ **:**
$f^4(\emptyset, \emptyset) = f(f^3(\emptyset, \emptyset)) = f(\{b, abab\}, \{ab\})$

Pour $X_1 = \{b, abab\}$ et $X_2 = \{ab\}$ :
$f(\{b, abab\}, \{ab\}) = \left( \{b\} \cup \{ab\}.\{ab\}, \{a\}.\{b, abab\} \right)$
Calculons chaque terme :

- $\{ab\}.\{ab\} = \{abab\}$
- $\{b\} \cup \{abab\} = \{b, abab\}$
- $\{a\}.\{b, abab\} = \{ab, aabab\}$
Donc :
$f^4(\emptyset, \emptyset) = \left( \{b, abab\}, \{ab, aabab\} \right)$

---

**Conclusion :**
$f^4(\emptyset, \emptyset) = \left( \{b, abab\}, \{ab, aabab\} \right)$

## Exo 2.17

<aside>
❓

Montrer que les langages définis dans le TP (`Prop`, `Nnf` en notations préfixes ou infixes) sont algébriques.

</aside>

$\bold{Prop}$ est un ensemble défini de manière récursive. Avant de parler de Prop, on définit une function telle que $\lim f^n(\empty) = \bold{Prop}$. On peut déjà utiliser la fonction de l’exo 2.13

$$
f(X) = \{t, f\} \cup \mathbb{N}_1 \cup \{ (u) \mid u \in X\} \cup \{-u \mid u \in X\} \cup \{uov \mid o \in \{\&, |, >\}, u, v \in X\}
$$

On peut écrire $f^1(\empty)$, $f^2(\empty)$, $f^3(\empty)$ et on pourra se convaincre que $\lim f^n(\empty) = \bold{Prop}$, ce dernier étant définit donc comme:

$$
\bold{Prop} = \{t, f\} \space\cup\space \mathbb{N}_1 \space\cup\space -\bold{Prop} \space\cup\space \bold{Prop} . \{\&, |, >\}.\bold{Prop} \space\cup\space \{(\}.\bold{Prop}.\{)\}
$$

L’argument à faire pour démontrer que c’est un langage algébrique est de dire que $f$ constitue un système d’équations algébrique (à 1 équation), où le membre droit de l’équation est constitué d’opérateurs ensemblistes (union), concaténation, le mot vide (pas le cas ici en fait, mais bon) et des constantes (ici $t$, $f$, $($, $)$ et les variables représentées avec $\N_1$). Et donc que $\lim f^i(X)$ est le plus petit point fixe (assuré par un théorème vu en cours), et que c’est justement $\bold{Prop}$. Finalement, $\bold{Prop}$ est algébrique.

---

Pour $\bold{Nnf}$, l’argument est similaire. Donc, j’écris juste le système d’équations où les fonctions $f_1$, $f_2$, $f_3$ sont déjà évalués à leur limite à l’infini et donc on tombe sur les plus petits points, montrant que $\bold{Nnf}$ est un langage algébrique (la première équation étant toujours le langage algébrique d’intérêt):

$$
\begin{cases}
\bold{Nnf}= \{t, f\} \cup \bold{Ncst} \\
\bold{Ncst} = \bold{NNInt} \cup \{\&, \mid \}.\bold{Ncst}.\bold{Ncst} \\
\bold{NNInt} = \N_1 \cup \{-\}.\N_1
\end{cases}
$$

## Exo 2.18

<aside>
❓

Pour $V = \{a, b, c\}$, donner une BNF pour chacun des langages suivants.

</aside>

1. $\{a^nb^n | n \in \mathbb{N}\} \to$  `L ::= a L b | ε`
2. $\{a^nb^p | n \geq p \geq 0\} \to$ 
`A ::= BC` , `B ::= aB | ε`, `C ::= a C b | ε`.
Une autre solution pourrait être `L ::= aL | aLb | ε` 
3. $\{a^nb^p | n \neq p\} \to$
`A ::= aA | B, B ::= a B b | ε`
4. $\{a^nb^p | 2p \geq n \geq p\} \to$
On utilise une fonction de substitution $\sigma$ sur la première réponse. 
    
    $$
    \sigma:\begin{cases}
     a \to a|aa = A \\
    b \to b
    \end{cases}
    
    \\[10pt]
    
    \sigma(L_1) = \sigma(aL_1b\mid \epsilon) = \sigma(a).\sigma(L_1).\sigma(b)\mid \sigma(\epsilon) = A.\sigma(L_1).b \mid \epsilon
    $$
    
    D’où, `L ::= A.L.b | ε`, `A ::= aa|a`
    
5. $\{a^nb^pc^q | n + p = q\} \to$ 
`L ::= aLc | X, X ::= bXc | ε`
6. $\{w \in \{a, b\}^* | w = \overline{w}\}$ où $\overline{w}$ est le renversé de $w$. Exemple de renversé : $aaba = abaa$. NB : un mot égal à son renversé s'appelle un palindrome. Exemples de palindromes : "aba" et "abba".
`L = ε | aLa | bLb | a | b`

## Exo 2.19

<aside>
❓

Donner une BNF sur $\{0, 1\}$ qui définit le langage des mots ayant un nombre pair de 0 et un nombre impair de 1.

</aside>

Le flow à suivre dans cette exercise est de savoir qu’on peut partir d’un automate fini, puis créer un système d’équations régulières, finalement en déduisant l’expression régulière qui est facilement transformable en BNF. Le dernier automate est le produit des deux premiers.

![WhatsApp Image 2025-01-12 at 15.18.50(1).jpeg](whatsapp_image_2025-01-12_at_15.18.50(1).jpeg)

![untitled.jpg](ensimag/first_year/ecole/1aa_info_grammaires_et_compilation/02_langages_algebriques_et_bnf/untitled_1.jpg)

## Exo 2.20

<aside>
❓

Montrer que tout langage régulier peut être défini par une BNF. Réciproquement, à quelles conditions (suffisantes) une BNF définit-elle un langage régulier ?

</aside>

Soir L un langage défini par une BNF. L est régulier si:

- toutes les équations de la BNF sont uniquement linéaires à droite
- toutes les équations sont uniquement linéaires à gauche