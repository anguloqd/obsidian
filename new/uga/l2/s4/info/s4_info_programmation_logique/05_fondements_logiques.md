# 05 // fondements logiques

[Slides de fondaments logiques](coursprologl2_6_(3).pdf)

# Logique des prédicats

La logique de premier ordre cherche à représenter des connaissances pour en inférer de nouvelles connaissances. Par exemple :

## Règles d’inférence

### Modus ponens

Le modus ponens reste le premier outil d’inférence.

> *Modus ponens* :
> 
> 1. Fait : $A \implies B$.
> 2. Fait : $A$ est vrai, ou simplement $A$.
> 3. Inférence : Donc, $B$ est vrai, ou $B$ tout court.

Pour la suite, notons qu’on peut réécrire $A \implies B$ comme $\lnot A \lor B$, et $A$ tout court comme $A \lor F$, où $F$ est une proposition fausse. En réécrivant, on a donc :

> *Modus ponens* :
> 
> 1. Fait : $\lnot A \lor B$
> 2. Fait : $A \lor F$
> 3. Inférence : $B \lor F.$

### Règle de résolution

La règle de résolution est une généralisation du Modus ponens. Il prend deux faut pour faire une inférence. Par contre, il faut que les deux faits soient de clauses disjonctives, est que l’une contienne une proposition $P$ et l’autre sa négation $\lnot P$.

> Principe de résolution :
> 
> 1. Fait : $P_1 \lor P_2 \lor \dots \lor P_n$
> 2. Fait: $\lnot P_1 \lor Q_2 \lor \dots \lor Q_n$
> 3. Inférence : $P_2 \lor \dots \lor P_n \lor Q_2 \lor \dots \lor Q_n$

L’utilite du principe de résolution est que l’inférence ne dépend plus ni de $P$ ni de $\lnot P_1$. On a “éliminé” d’une certaine façon $P_1$.

## Preuve par réfutation

C’est juste une forme de preuve par contradiction. Étant donné un ensemble de faits, on veut savoir si une certaine inférence $Q$ est vraie. On le fait supposant que $Q$ est fausse et donc $\lnot Q$ est vraie, et commençant à déduire les faits du système. Eventuellement on devrait arriver à une contradiction, donc on déduit que $\lnot Q$ est fausse et que $Q$ est finalement vraie.

## En Prolog

En Prolog, la définition d’une règle est une clause de Horn : une clause disjonctive qui a, au plus, un atome ou literal vrai.

$$
\begin{align*}
& &P_1 \lor \lnot P_2 \lor \dots \lor \lnot P_n
\\ &\iff &\lnot(\lnot P_2 \lor \dots \lor \lnot P_n) \implies P_1
\\ &\iff &P_2 \land \dots \land P_n \implies P_1
\\ &\iff &\underbrace{P_1 \text{ :- } P_2,\space \dots \space , P_n}_\text{En Prolog}
\end{align*}
$$