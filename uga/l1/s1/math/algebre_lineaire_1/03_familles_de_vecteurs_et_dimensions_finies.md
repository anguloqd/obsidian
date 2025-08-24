## 03 // familles de vecteurs et dimensions finies

## Familles de vecteurs

### Famille libre

Si un groupe ou "famille" de vecteurs $\{v_1, v_2, …, v_p\}$ sont tels que, la seule solution à l'équation : $λ_1v_1 + λ_2v_2 + ··· + λ_pv_p = 0$ est avec chaque scalaire posé égal $0$. Dans ce cas, $F$ est une famille libre.

Toute famille non libre est une famille liée. Ceci implique que, dans les familles liées, il y a au moins un vecteur qui peut s'exprimer comme la combinaison linéaire des autres vecteurs.

### Famille génératrice

Une famille $F$ de vecteurs $\{v_1, v_2, …, v_p\}$ appartenant à un espace vectoriel $E$ est dite "génératrice de $E$" si, pour tout vecteur de $E$, on peut l'exprimer comme le résultat d'une combinaison linéaire de la famille $F$.

- **Proposition.** Soit $F = \{v_1, v_2, …, v_p\}$ une famille génératrice de $E$. Alors $F' = \{v'_1, v'_2, …, v'_p\}$ est aussi une famille génératrice de $E$ si et seulement si tout vecteur de $F$ est une combinaison linéaire de vecteurs de $F'$.
- **Proposition.** Si dans une famille génératrice $F$, l'un des vecteurs là dedans est linéairement dépendant d'un autre vecteur, si on retire ce vecteur linéairement dépendant de la famille, la famille restante est toujours génératrice.

### Base

Une famille $F = \{v_1, v_2, …, v_p\}$ de vecteurs de $E$ est une base de $E$ si $B$ est une **famille libre et génératrice**.

- L'ordre est important ! Chaque scalaire doit être attaché à son vecteur correspondant.

Par conséquence, tout vecteur $v ∈ E$ s’exprime de façon unique comme combinaison linéaire d’éléments de $F$. $\{λ_1, … ,λ_n\}$ s’appellent les coordonnées du vecteur $v$ dans la base.

**Théorème d'existence d'une base.** Tout espace vectoriel admettant une famille finie génératrice admet une base.

**Théorème de la base incomplète.** Soit $E$ un $K$-espace vectoriel admettant une famille génératrice finie. Alors :

- Toute famille libre $L$ peut être complétée en une base.
- De toute famille génératrice $G$ on peut extraire une base de $E$.

**Théorème "encore plus général".** Soit $G$ une famille génératrice finie de $E$ et $L$ une famille libre de $E$. Alors il existe une famille $F$ de $G$ telle que $L ∪ F$ soit une base de $E$

## Dimensions finies

### Dimension d'un espace vectoriel

Un $K$-espace vectoriel $E$ admettant une base ayant un nombre fini d’éléments est dit de **dimension finie**. **Toutes les bases d’un espace vectoriel $E$ de dimension finie ont le même nombre d’éléments**.

La dimension d’un espace vectoriel de dimension finie $E$, notée $\text{dim}(E)$, est par définition le nombre d’éléments d’une base de $E$.

**Lemme.** Soit $E$ un espace vectoriel. Soit $L$ une famille libre et soit $G$ une famille génératrice finie de $E$. Alors $\text{Card}(L) \le \text{Card}(G)$.

**Proposition.** Soit $E$ un $K$-espace vectoriel admettant une base de $n$ éléments. Alors :

- Toute famille libre de $E$ a, au plus, $n$ éléments.
- Toute famille génératrice de $E$ a, au moins, $n$ éléments.

**Corollaire.** Si $E$ est un espace vectoriel admettant une base ayant $n$ éléments, alors toute base de $E$ possède $n$ éléments.

### Dimension d'un sous-espace vectoriel

Soit $E$ un $K$-espace vectoriel de dimension finie. Alors :

1. Tout sous-espace vectoriel $F$ de $E$ est de dimension finie.
2. $\text{dim}(F) \le \text{dim}(E)$
3. $F = E \iff \text{dim}(F) = \text{dim}(E)$.

Soient $F$ et $G$ deux sous-espaces vectoriels de $E$. On suppose que $F$ est de dimension finie et que $G ⊂ F$.

- Alors : $F = G$ $\iff \text{dim}(F) = \text{dim}(G)$
Autrement dit, sachant qu’un sous-espace est inclus dans un autre, alors pour montrer qu’ils sont égaux il suffit de montrer l’égalité des dimensions.

**Théorème des quatre dimensions**. Soient $E$ un espace vectoriel de dimension finie et $F$,$G$ des sous-espaces vectoriels de $E$. Alors :

- $\text{dim}(F + G) = \text{dim}(F) + \text{dim}(G) − \text{dim}(F ∩ G)$
- **Corollaire** : si $E = F ⊕ G$, alors $\text{dim}(E) = \text{dim}(F) + \text{dim}(G)$.
- Tout sous-espace vectoriel $F$ d’un espace vectoriel $E$ de dimension finie admet un supplémentaire.
