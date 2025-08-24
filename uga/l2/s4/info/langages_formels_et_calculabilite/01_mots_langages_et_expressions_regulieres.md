## 01 // mots, langages et expressions régulières

[Slides du chapitre 1](ressources/01_mots_langages_et_expressions_regulieres_chapitre_1_compressed.pdf)

## Le cours : la théorie du calcul

Ils existent deux types de langage : le langage naturel de des humains et le langage machine. Ce dernier ne dépend pas d’une interprétation humaine ni du contexte, c’est “objectif”.

### Interprétation d’un texte machine

L’interpretation ou compilation d’un texte machine se décompose généralement en 3 étapes :

1. L’analyse lexicale est la décomposition d’un texte en entités unitaires et élémentaires, de la même manière qu’on décompose un casse-tête en pièce les plus petites. L’unité ici serait un lexème (un mot particulier), ou *token* en anglais.
2. L’analyse syntaxique est la décomposition d’un programme dans des grands morceaux, appelé entité syntaxiques, chacun étant la **combinaison** de plusieurs lexèmes.
3. L’analyse sémantique est la génération du code objet (normalement code binaire) à partir du texte langage.

Par exemple, prenons le morceau de texte en langage C :

```python
cpt = i + 3.14;
```

L’analyse lexicale classifie chaque caractère selon sa fonction : `cpt` et `i` sont des identificateurs de variables, `=` et `+` sont des opérateurs, `3.14` est une valeur réelle.

L’analyse syntaxique reconnait que cette combinaison de caractères represente une addition de `3.14` unités à la variable `i` et le stocker dans la variable `cpt`.

L’analyse sémantique vérifie que le bon typage des variables `cpt` et `i` et génère le code objet à la machine.

## Qu’est-ce qu’un langage ?

### Définition

Les langages naturels, comme le français, sont apparus spontanément et puis on a crée des regles sociaux sur ces langages **pour les expliquer et non pas pour les déterminer**. Tout cela peut changer et évoluer avec les temps.

Les langages formels sont vraiment soumis aux règles. Pour nous, un langage formel est simplement un ensemble de suite de lettres, appelées aussi mots ou chaînes de caractères.

## Alphabet et mots

### Définition intuitive

Un alphabet est un ensemble fini non-vide de caractères dont les éléments sont appelés des lettres. Un mot est une suite de ces lettres. Par exemple :

- $0010111100$ est un mot sur $\{0, 1\}$.
- $aaabbb$ est un mot sur $\{a, b\}$.

- $\text{SALUT}$ est un mot sur $\{A, \dots, Z\}$
- $\lambda \omicron \gamma \omicron \sigma$ est un mot sur $\{\alpha, \dots, \zeta\}$.

### Définition mathématique

Mathématiquement, on peut définir un mot de longueur $n$ (ici $n=3$) comme suit :

$$
A=\{"A",\dots,"Z"\}
\implies \text{"OUI"} \in M^3_A = A\times A\times A
 \\
\text{Où } M^3_A \text{ est l'ensemble de mots à 3 lettres dans l'alphabet }A
$$

Mais, dans ce cours, on utilisera une définition un peut plus compliquée. Elle serait la définition d’une fonction. À nouveau, pour le mot $\text{OUI}$, on définit la fonction $s_\text{OUI}$ :

$$
s_\text{OUI}: \{1,\dots,n\} \mapsto A^* \\
s_\text{OUI}(1) = \text{O}, s_\text{OUI}(2) = \text{U}, s_\text{OUI}(3) = \text{I}
$$

Notons que, dans cette fonction, on définit mathématiquement un mot **en définissant l’ensemble image de la fonction $s$**. Aussi, $n$ doit être le longueur du mot. Donc, il existe une unique fonction $s$ pour chaque mot.

## Propriétés des mots

### Longueur $n$ de mots

L’un des propriétés des mots est leur longueur, dénoté $n$. Pour “$OUI$”, la longueur est $3$. On peut voir aussi que la longueur est définie comme la quantité de lettres dans le mot, mais c’ést aussi équivalent à la position de la dernière lettre du mot. $s_\text{OUI}(3)=I$, mais $s_\text{OUI}(4)$ n’est pas défini.

Revenons maintenant à la première définition mathématique d’un alphabet et les mots de taille $n$:

$$
\begin{align*}
A = \{"A",\dots,"Z"\} \implies
&W_A^0=\varepsilon \\
&W_A^1=A \\
&W_A^2=A\times A \\
&W_A^3=A\times A\times A
\\ \vdots
\end{align*}
\\
L_A^n=\bigcup_{i=0}^n W_A^n : \text{le strate de mots de taille max. } n \text{ construit à partir de l'alphabet } A

\\
\Sigma^*_A = \lim_{n \rightarrow \infty} L_A^n : \text{l'ensemble de tous les mots possibles dans } A 
$$

**Précision**. $\varepsilon$ est la chaîne vide et est toujours inclus dans $L^n_A$, pour tout $n$. Sa longueur est $0$.

La *stratification* est le fait de creer un ensemble de mots de longueur $n$ dans un alphabet $A$, où on fixe un $n$ particulier. C’est basiquement la notation de $W_A^n$ qu’on avait introduit.

### Concaténation de mots

La concaténation est simplement une nouvelle fonction qui est une fonction par branches prenant les fonctions s de deux mots. Prenons $s_\text{BON}$ et $s_\text{JOUR}$, on note leur concaténation $s_\text{BON} \land s_\text{JOUR}$.

$$
s_\text{BON}\land s_\text{JOUR} : \{1, \dots, n_\text{BON}+n_\text{JOUR}\} \rightarrow A

\\
\text{}
\\

s_\text{BON}\land s_\text{JOUR}(n)=
\begin{cases}
s_\text{BON}(n), 1 \le n \le n_\text{BON}=3 \\
s_\text{JOUR}(n), n_\text{BON}+1 \le n \le n_\text{BON}+ n_\text{JOUR}=7 \\
\end{cases}
$$

La concaténation peut être vue comme une opération qui possède les propriétés d’associativité et neutralité, cette dernière avec la chaîne vide $\varepsilon$. **La concaténation n’est pas commutative !**

## Langages

### Définition

Ayant crée le strate global de **mots finis** $\Sigma^*_A$, on définit un langage comme une partie ou sous-ensemble de ce strate. Dans la vie réelle, le français est composé juste d’une partie de tous les mots qu’on peut créer avec l’alphabet latin. Notons qu’on peut créer le mot “abbaksl” avec l’alphabet latin mais ce n’est pas un mot en français. Quelques langages notables sont :

- $\empty$ : le langage vide.
- $\{\varepsilon\}$ : le langage réduit au mot vide.
- $A^*$ : le langage plein.

### Opérations de langages

Soit $L$ et $L’$ deux langages. L’union est une opération qui réunit les mots des deux langages.

$$
L \cup L' = \left\{u:u\in L \text{ ou } u \in L'\right\}
\\
L \cup L' = L' \cup L
$$

La concaténation ou produit est une opération retournant un langage qui contient la concaténation de tout possible choix de couples de mots préservant l’ordre. **Elle n’est pas commutative non plus !**

$$
L \cdot L' = \left\{w=u  \land v: u\in L \text{ et } v \in L'\right\}
\\
L\cdot L' \ne L' \cdot L
$$

### L’étoile de Kleene

On peut voir l’étoile de Kleene comme un extension d’un même langage. Si $L$ est un langage, $L^*$ est le langage élargit. Ce nouveau langage contient toute les possibles concaténations de zéro ou plusieurs mots du même langage. Par exemple :

$$
L=\{0,1\} \implies L^*=\{\varepsilon, 0, 1, 00, 01, 10, 11, 000,001, 010,011,\dots\}
$$

On en déduit que la définition de $L^*$ est l’union des toutes les concaténations dans un même alphabet de zéro mots, d’un mot, de deux mots, de trois mots, etc..  On a utilisé la notation $W^n_A = A^n$ pour l’ensemble de mots de longueur $n$. Il vient que la définition de $L^*_A$ est la suivante :

$$
L^*= \bigcup_{n=0}^\infty L^n=\{ \varepsilon \}\cup L\cup L^2 \cup L^3 \cup L^4 \dots, \text{ où } L^n=\underbrace{L\cdot L\cdot \space \dots \space \cdot L}_{n \text{ fois}}
$$

Puisque $L$ est une partie de toutes les posibles mots dans $A$, on peut choisir $L$ comme le mots de juste une lettre dans A, c’est-à-dire, $L=W_A^1=A$. Donc, cela impliquerait que $L^*=\Sigma^*_A=A^*$. Cela dit, $L$ n’est pas limité à être $A$.

### Propriétés des langages

La concaténation et union des langages est associative et distributive. Pour les langages $A$,$B$,$C$ :

$$
A\cdot(B \cdot C) = (A \cdot B) \cdot C \text{ et } A\cup(B \cup C) = (A \cup B) \cup C
\\
A\cdot(B\cup C) = (A\cdot B) \cup (A \cdot C)
$$

En plus, il y a d’autres technicalités et conventions :

- $L \cdot \empty = \empty$  : concaténer les mots avec “rien” (ce n’est pas $\varepsilon$ !) retourne rien.
- $L \cup \empty = L$ : réunir les mots d’un langage avec rien retourne le même langage.
- $L \cdot \{ \varepsilon \} = L$  : concaténer les mots avec la chaîne vide $\varepsilon$ retourne le même langage.
- $\empty^* = \{ \varepsilon \}$. C’est une convention.
- $\{ \varepsilon \} \cup (L \cdot L^*) = L^*$.
    - Pour cette dernière, retournons à $L^* = \{ \varepsilon \} \cup L \cup L^2 \dots$
    On concatène par la gauche avec $L$ : $L \cdot L^* = \underbrace{L\cdot\{ \varepsilon \}}_{L^1} \cup \underbrace{L\cdot L}_{L^2} \cup \underbrace{L\cdot L^2}_{L^3} \dots = L^* \setminus \{ \varepsilon\}$
    On a fait disparaître $\{ \varepsilon \}$ ! Donc on peut le réunir à la nouvelle expression et on arrivera au point de départ : $\{ \varepsilon \} \cup (L^* \setminus \{ \varepsilon \} ) = L^*$.

## Langages réguliers

### Définition

Un langage régulier sur un alphabet $A$ est l’un des suivants :

1. $\empty$
2. $\{ \varepsilon \}$
3. $\{ x \}, x \in A$ : un langage composé d’une seule lettre de $A$.
4. L’union ou concaténation de deux langages réguliers sur $A$.
5. L’étoile de Kleene d’un langage régulier.

Notons qu’on utilise les trois premiers pour construire les langages réguliers plus compliqués.

### Exemples

**Exemple**. Prenons un alphabet $A =\{a, b\}$. Les suivants sont des langages réguliers :

- $\{a\} \cup \{b\} = \{a, b\}$  : on a simplement crée un langage $L$ identique à $A$, càd. $L=A$.
- $( \{a\} \cup \{ b \} )^* = (\{a, b\})^*$  : tous les mots constructibles dans $A$.
- $\{a\} \cdot \{a\} \cdot \{a\} = \{aaa\}$  : le langage qui contient $aaa$ comme son seul mot.
- $\{aaa\} \cdot (\{a\} \cup \{b\})^*$ : tous les mots dans $A$ qui commencent avec $aaa$.
- $(\{ \varepsilon \} \cup \{aa\})^*$ : les mots qui contiennent un nombre pair de $a$, même zéro $a$.
- $(\{ \varepsilon \} \cup \{aa\})^* \cdot \{bbb\} \cdot (\{ a \} \cup \{ b \})^*$ : l’ensemble de mots dans $A$ qui commencent avec un nombre pair de $a$, puis suivis de trois $b$.

## Expressions régulières (regex)

### Définition

Si on voit le dernier exemple de langage régulier, la notion qui le représente est assez compliquée. L’expressions réguliers nous permet de représenter des langages réguliers de manière compacte.

Déjà, $\empty$, $\{ \varepsilon \}$ et $\{x\}, x\in A$ sont des expression régulières de base. En plus, pour $\alpha$ et $\beta$ regex  :

- $\alpha + \beta$ est aussi une regex, où $+$ est l’union $\cup$.
- $\alpha \beta$ est aussi une regex, où l’absence d’opérateur est simplement la concaténation $\cdot$.
- $(\alpha)^*$ est une regex.

### Exemples

On peut réécrire tous les langages réguliers en-dessus avec cette notation, toujours $A=\{a,b\}$ :

- $a+b = \{a, b\}$
- $(a+b)^* = (\{a,b\})^*$.
- $aaa = \{aaa\} = \{a\}\cdot\{a\}\cdot\{a\}$
- $aaa(a+b)^*$ : tous les mots dans A qui commencent avec aaa.
- $(\varepsilon + aa)^*$ : tous les mots composés seulement d’un nombre pair de a, zéro a inclus.
- $(\varepsilon + aa)^*bbb(a+b)^*$ : tous les mots dans $A$ qui commencent avec un nombre pair de $a$ suivis de trois $b$.

**Propriétés**. Les regex ont les mêmes propriétés que les langages régulières, juste réécrites.
