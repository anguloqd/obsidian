## 03 // le langage SQL DML : data manipulation language

[Slides de SQL 1](ressources/03_le_langage_sql_dml_data_manipulation_language_03.sql1.pdf)

[Slides de SQL 2](ressources/03_le_langage_sql_dml_data_manipulation_language_04.sql2.pdf)

## Premiers aspects

SQL signifie *Structured Query Language*. C’est une langage d’interrogation de SGBD à travers de requêtes, divisé en DDL (Data Definition Language) et DML (Data Manipulation Language).

Dans cette note, on va parler de SQL DML, qui comporte 2 grandes classes de fonctions : l’extraction de données et la modification de données.

## Requêtes élémentaires

### Instruction `SELECT`

L’instruction principal utilisée pour les deux buts (extraction/modification) est l’instruction `SELECT`. Bref, `SELECT` est en fait une suite de clause `SELECT-FROM-WHERE` :

- `SELECT` : précise les valeurs (nom des colonnes) qui constitue chaque ligne du résultat attendu
- `FROM` : indique la table ou les tables à partir desquels le résultat doit être extrait
- `WHERE` : spécifie la condition de sélection que doit être satisfaite par les lignes du résultat

Le résultat d’une requête `SELECT` ou SFW (`SELECT FROM WHERE`) est une table fictive qui sera considérée comme s’achant à l’écran.

### Requête simple

Une requête simple consiste à demander l’achage des valeurs de certaines colonnes $A$ des lignes d’une table $R$. En algèbre relationnelle, c’est simplement une projection $R[A]$.

```sql
SELECT NCLI, NOM, LOCALITE
FROM CLIENT ;

// SELECT * 
// si on veut tout selectionner
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled.png)

Si on ajoute la clause `WHERE`, on simule donc l’opération de sélection $R:C$ en algèbre relationnelle.

```sql
SELECT NCLI, NOM
FROM CLIENT
WHERE LOCALITE = 'Toulouse';
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_1.png)

> [!note]
> Problème : dans une requête monotable, ils se peuvent afficher autant de lignes qu’il y a des lignes vérifiant la condition, donc possiblement de lignes dupliquées. Pour l’éviter, on utiliser le mot clé `DISTINCT` après `SELECT`.
>
> Si la clause `SELECT` cite tous les composants d’un identifiant de la table, l’unicité des lignes résultats est garantie. Il est donc inutile d’utiliser `DISTINCT`.

### Conditions élémentaires

La formes des conditions qu’on peut spécifier dans la clause `WHERE` sont comme suit :

- La présence de valeur `NULL`

    ```sql
    CAT IS NULL
    CAT IS NOT NULL
    ```

- Appartenance aux colonnes d’une liste : `IN`

    ```sql
    CAT IN ( 'C1' , 'C2' , 'C3' )
    LOCALITE NOT IN ( 'Toulouse' , 'Namur' , 'Breda')
    ```

- Appartenance sur un intervalle (colonnes ou lignes) : `BETWEEN/AND`

    ```sql
    COMPTE BETWEEN 1000 AND 4000
    CAT NOT BETWEEN 'B2' AND 'C1'
    ```

- Présence de certain caractères dans une valeur : `LIKE`
Cette dernière utilise de “masques” : caractères spéciaux pour la recherche, similaire à regex. Dans ce cas, “`_`” est un caractère quelconque et “`%`” est une suite de caractères éventuellement vide.

    ```sql
    CAT LIKE '_1'
    ADRESSE LIKE '\%Neuve\%'
    ```

La condition de la clause `WHERE` peut être composée d’une expression booléenne : `AND`, `OR`, `NOT`. On peut faire des expressions plus complexes avec des parenthèses.

### Données extraites et données dérivées

Avec l’instruction `SELECT`, on peut afficher une nouvelle tables avec des colonnes qui n’existent pas dans la table originale. Les données de ces colonnes sont soit des constantes ou calculées à partir des données de la table originale.

```sql
SELECT 'TVA de' , NPRO,
	'=', 0,21*PRIX*QSTOCK
FROM PRODUIT
WHERE QSTOCK > 500 ;
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_2.png)

Par défaut, les colonnes du résultat prennent le nom utilisé dans la clause `SELECT`. Pour utiliser un autre nom ou alias il fait utiliser la clause `AS`.

```sql
SELECT NPRO AS PRODUIT,	0,21*PRIX*QSTOCK AS TVA
FROM PRODUIT
WHERE QSTOCK > 500 ;
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_3.png)

## Les fonctions SQL

Comme un langage de programmation, SQL fourni aussi des fonctions prédéterminées. Déjà, on inclut les opérateurs arithmétiques `+`, `-`, `*` et `/`. Ils existent aussi des fonction math. plus compliquées, comme le log. ou la trigonométrie.

### Manipulation de strings

- `CHAR.LENGTH(s)` : donne le nombre de caractères de la chaîne s
- `POSITION(s1 IN s2)` : donne la position de la chaîne `s1` dans la chaîne `s2` ; retourne `1` si `s1` est vide et `0` si `s1` n’apparaît pas dans `s2`
- `s1 || s2` : construit une chaîne composée de la concaténation de `s1` et `s2`
- `LOWER(s)` : convertit la chaîne `s` en minuscule
- `UPPER(s)` : convertit la chaîne `s` en majuscule
- `SUBSTRING(s FROM I FOR L)` : construit une chaîne de longueur `L` a partir de la chaîne `s` débutant a l’indice `I`
- `TRIM(e c FROM s)` : supprime les caracteres `c` à l’extrémité `e` de la chaîne `s`; `e` peut prendre pour valeur `LEADING`, `TRAILING` et `BOTH`
- `BIT.LENGTH(s)` : donne le nombre de bits de la chaînes
- `OCTET.LENGTH(s)` : donne le nombre d’octets occupés par la chaîne de bits `s`

Les suivantes ne sert pas à manipuler les strings, mais souvent elles s’utilisent avec :

- `CAST(v AS t)` : convertit la valeur `v` selon le type `t`
- `EXTRACT(u FROM dt)` : donne, sous la forme numérique, le composant `u` de ma valeur **temporelle** `dt`; les valeurs de `u` sont : `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`

### Registres du système (temps et utilisateur)

- `CURRENT.USER` : l’utilisateur courant
- `CURRENT.DATE` : la date courante
- `CURRENT.TIME` : l’heure courante
- `CURRENT.TIMESTAMP` : date + heure courante

### Fonction agrégatives/statistiques

- `COUNT(*)` : donne le nombre de lignes sélectionnées
- `COUNT(colonne)` : donne le nombre de valeurs de la colonne
    - Peut recompter des valeurs dupliqués → On peut utiliser `DISTINCT` pour l’éviter
- `AVR(colonne)` : donne la moyenne des valeurs de la colonne
- `SUM(colonne)` : donne la somme des valeurs de la colonne
- `MIN(colonne)` : donne le minimum des valeurs de la colonne
- `MAX(colonne)` : donne le maximum des valeurs de la colonne

Remarque #1: la colonne peut être remplacée par une expression arithmétique entre deux colonnes. Par exemple `(c1 * c2)` serait une nouvelle colonne dérivée qui multiplie les valeurs des colonnes `c1` et `c2`.

Remarque #2 : si on donne une colonne vide, la fonction `COUNT` retournera `0` et les autres fonctions `null`.

## Les sous-requêtes

### Définition et exemples

À la fois de faire une requête simple sur une table et puis une deuxième requête sur la sous-table obtenue, on peut imbriquer de requêtes pour que ce soit plus pratique.

```sql
SELECT NCOM, DATECOM
FROM COMMANDE
WHERE NCLI IN (SELECT NCLI
								FROM CLIENT
								WHERE LOCALITE = 'Namur') ;
```

Quand on fait des sous-requêtes où on prend des colonnes de deux tableaux différents, il se peut qu’il y ait des colonnes avec le même nom dans les deux, ex.: la colonne `NPRO` dans le tableau `PRODUIT` et aussi dans le tableau `DETAIL`.

Dans ce cas, on peut référencier le tableau puis la colonne comme `PRODUIT.NPRO` ou bien utiliser un alias avec le mot clé `AS`.

```sql
SELECT P.NPRO
FROM PRODUIT AS P
WHERE P.NPRO IN (
			SELECT D.NPRO
			FROM DETAIL AS D)
```

Si la sous-requête renvoie une seule ligne, il est permis d’utiliser les opérateurs de comparaison classique.

```sql
SELECT *
FROM CLIENT
WHERE COMPTE > (SELECT COMPTE
								FROM CLIENT
								WHERE NCLI = 'C400') ;
```

## Quantificateurs ensemblistes

On peut utiliser les mots clés `EXISTS`, `ALL` et `ANY` dans la clause de condition `WHERE`.

### `EXISTS`

- `EXISTS` : est vraie s’il existe au moins une ligne dans le résultat d’une sous-requête.
**C’est plutôt une condition d’existence et différent des deux prochains**.

    ```sql
    SELECT NPRO, LIBELLE
    FROM PRODUIT AS P
    WHERE EXISTS (SELECT *
    							FROM DETAIL AS D
    							WHERE D.NPRO = P.NPRO) ;
    ```

### `ALL`

- `ALL` : est vraie si la condition à gauche est vérifié avec tous les éléments de la sous-requête.
S’utilise après un opérateur et avant une sous-requête.

    ```sql
    SELECT DISTNCT NCOM
    FROM DETAIL
    WHERE QCOM <= ALL (SELECT QCOM
    										FROM DETAIL
    										WHERE NPRO = 'PA60')
    										AND NPRO = 'PA60' ;
    ```

### `ANY`

- `ANY` : est vraie si la condition à gauche est vérifié avec au moins un élément de la sous-requête.
S’utilise après un opérateur et avant une sous-requête.

    ```sql
    SELECT *
    FROM DETAIL
    WHERE QCOM > ANY (SELECT QCOM
    									FROM DETAIL
    									WHERE NPRO = 'PA60')
    									AND NPRO = 'PA60' ;
    ```

## Les opérateurs ensemblistes

### Rappel : définition d’un ensemble

Au sens mathématique, un ensemble est une collection d’éléments *distincts*. En SQL, un ensemble de lignes ne peut donc contenir deux lignes dont les attributs, considérés 2 à 2, ont la même valeur.

Une collection de lignes où les éléments ne sont pas distincts constitue un multi-ensemble. Une requête dont la liste d’éléments de la clause `SELECT` n’inclut pas tous les éléments d’un identifiant renvoie un multi-ensemble. Une requête dont la liste d’éléments de la clause `SELECT` n’inclut pas tous les éléments d’un identifiant renvoie un multi-ensemble. Il peut se réduire à un ensemble par le modifieur `DISTINCT`.

Avec tout cela dit, on peut présenter les opérateurs ensemblistes. Ils s’utilisent au milieu de deux tableaux résultats de deux requêtes.

### `UNION`

Produit une collection de lignes distinctes à partir d’un ensemble de deux collections de lignes, même s’il y a des lignes répétées (si les arguments sont des multi-ensembles). UNION ALL conserve les lignes répétées.

```sql
SELECT LOCALITE FROM CLIENT WHERE CAT = 'C1';
UNION
SELECT LOCALITE FROM CLIENT WHERE COMPTE <0;
```

### `INTERSECT`

Construit l’ensemble des éléments simultanément présents dans deux collections. `INTERSECT ALL` garde des lignes répétées. À noter qu’on pourrait arriver au même résultat avec une simple jointure.

### `EXCEPT`

C’est l’opérateur de différence ensembliste. Construit l’ensemble d’éléments appartenant à la première collection mais pas à la seconde. À noter qu’on pourrait arriver au même résultat avec le prédicat “requeteTable1 `NOT IN` sousrequeteTable2”.

### Produit cartésien/relationnel

Il n’existe pas une syntaxe pour le produit cartésien, plutôt on utilise une **jointure sans condition de jointure** (clause `WHERE` avec une égalité). Elle risque d’être cependant coûteuse et, sans justification, il faudra la considérer comme une erreur.

### Auto-jointure et données cycliques

On qualifie de cyclique une structure de données qui fait, directement ou indirectement, référence à elle. Il est normalement d’intérêt de faire une requête en joignant la table à elle-même, donc une auto-jointure. Par exemple :

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_4.png)

La table `PERSONNE` nous montre, pour chaque identifiant, son nom et l’identifiant de son responsable. On voudrait avoir plutôt, pour chaque identifiant, l’identifiant de son responsable et le nom de son responsable.

```sql
SELECT S.NPERS, R.NPERS, R.NOM
FROM PERSONNE S, PERSONNE R
WHERE S.RESPONSABLE = R.NPERS ;
```

Exemple intéressant : donner, pour chaque personne subordonnée à la personne de numéro p4,

son numéro et son nom. On ignorera les personnes qui n’ont pas de responsable.

```sql
SELECT SS.NPERS, SS.NOM
FROM PERSONNE R, PERSONNE.S, PERSONNE SS
WHERE R.NPERS = 'p4'
	AND R.NPERS = S.RESPONSABLE // on obtient les subordonées direct
	AND S.NPERS = SS.RESPONSABLE ; // ici les subs direct des subordonées
```

Si on voit le diagramme de hiérarchie, on verra que les subordonnés direct de p4 sont p5 et p6, et l’indirect et p7. On obtient les subordonnés directes avec la première jointure, et puis les subs. directs des subs. directs avec la deuxième jointure. Malhereusement, il est impossible d’effectuer des jointures récursivement en SQL.

## Compléments sur les jointures

La jointure est un opérateur fondamental en ce qu’il permet de naviguer parmi les données. Étant donné ça, on va expliquer quelques choses importantes par rapport à la jointure :

### Conditions d’association et non association

Une association est la coïncidence d’une valeur d’une colonne dans une autre (peut-être aussi de la même table). Il pourrait sembler évidant que c’est ce que la jointure, par contre et, effectivement, avec la jointure on peut trouver des valeurs qui existent simultanément dans deux colonnes. Par contre, avec une requête imbriquée, on peut aussi exprimer de conditions d’association et, en plus, de non association. Voyons la différence :

```sql
SELECT DISTINCT COMMANDE.NCOM, DATECOM, NCLI
FROM COMMANDE, DETAIL
WHERE COMMANDE.NCOM = DETAIL.NCOM AND NPRO <> 'PA60' ;
```

Ici, on utilise une jointure simple. On cherche toute les (n° commande, date de commande, n° client) où l’attribut (n° produit $\in$ DETAIL) n’est pas ‘PA60’.

```sql
SELECT NCOM, DATECOM, NCLI
FROM COMMANDE
WHERE NCOM NOT IN (SELECT NCOM
										FROM DETAIL
										WHERE NPRO = 'PA60') ;
```

Ici, on utilise une requête imbriquée. On cherche toute les (n° commande, date de commande, n° client) de COMMANDE où le n° commande n’est pas présent dans les n° commandes dont le produit commandé est ‘PA60’.

La différence est difficile à voir, mais le détail important c’est que NCOM est une clé de COMMANDE et une clé étrangère de DETAIL, donc **toutes les valeurs NCOM existent et sont mentionnés dans COMMANDE, mais pas forcément sont mentionnés dans DETAIL**. Les valeurs d’une clé étrangère sont un sous-ensemble (propre ou non) des valeurs d’une clé.

Particulièrement, la première requête va donner tous les NCOM qui existent et sont présents dans les deux tableaux, tant que la deuxième commande va donner les NCOM qui existent dans COMMANDE et non pas dans DETAIL.

Exemple : si la valeur de NCOM ‘1234’ existe dans COMMANDE mais pas dans DETAIL, elle ne sera pas affichée dans la première requête. Ceci ne vas jamais arriver si tous les valeurs de NCOM dans COMMANDE sont mentionnées au moins une fois dans DETAIL.

> [!note]
> Prenons ce schéma :
>
> - TA(IA, DA).
> - TB(IB, RA, DB).
>
> Il est à noter que toutes les valeurs de IA sont mentionnées dans TA. Toutes les valeurs de RA existent dans IA. Pas forcément toute valeur de IA existe dans RA.

Le point à retenir c’est que les conditions de non-association ne sont généralement exprimables que pas des sous-requêtes, ainsi que par la forme `NOT EXISTS`.

### Quantités extraites de plusieurs tables

Le raisonnement est simple : la jointure constitue des lignes fictives dont la clause `SELECT` extrait des valeurs comme elle le ferait d’une ligne réelle issue d’une table.

```sql
SELECT NCOM, D.NPRO, QCOM*PRIX
FROM DETAIL D, PRODUIT P
WHERE D.NPRO = P.NPRO ;
```

### Jointure $\theta$ : condition différente de l’égalité

La jointure où la condition est un test d’égalité est simplement une jointure “naturelle”. On voudrait explorer les jointure $\theta$, où la condition n’est pas un test d’égalité.

Prenons ce schéma :

- TA(IA, DA).
- TB(IB, RA, DB).

Il est à noter que toutes les valeurs de IA sont mentionnées dans TA. Toutes les valeurs de RA existent dans IA. Pas forcément toute valeur de IA existe dans RA.

Prenons aussi cette requête :

```sql
SELECT *
FROM TA, TB
WHERE TA.IA = TB.RA ;
```

La résultat d’une jointure simple comme celle-ci représentent des entités de la table contenant la clé étrangère. Puisque le tableau final contient IA mais aussi RA et RA permet des valeurs répétées (car la colonne n’est pas identifiant de TB) qui conduit à des valeurs répétés sur IA, donc la seule clé du tableau final est IB.

Si la clé primaire n’est pas reprise dans la clause `SELECT`, le résultat n’as pas d’identifiant.

```sql
SELECT IA, DA, RA, DB // sans l'identifiant IB, donc résultat sans identifiant
FROM TA, TB
WHERE TA.IA = TB.RA ;
```

### Interpréter les lignes d’une jointure

Les lignes d’un tableau de base représentent quelque chose : une entité. Ce qui resulte d’une jointure est aussi un tableau, donc il faut savoir bien interpréter ses lignes. Par exemple :

```sql
SELECT C.NCLI , NOM, LOCALITE
FROM CLIENT C, COMMANDE M
WHERE M.NCLI = C.NCLI ;
```

Le tableau résultat a pour lignes des tuples (n° client, nom, localité). Il faudrait déduire que ceci répresente une commande.

## Extraction de données groupées

### Clause `GROUP BY`

Pour toute cette section, on gardera comme référence cet tableau :

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_5.png)

Grouper les données c’est de prendre une colonnes dont les valeurs sont répétées, et faire d’opérations agrégées avec les lignes, et de rendre uniques les lignes les valeurs répétées. Par exemple :

```sql
SELECT LOCALITE,
	COUNT(*) AS NOMBRE CLIENT,
	AVG(COMPTE) AS MOYENNE COMPTE
FROM CLIENT
GROUP BY LOCALITE ;
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_6.png)

On agrège les nombres de clients, on prend la moyenne de leurs comptes et on le classifie par localité (qui était la valeur répétée).

On peut, en plus, appliquer des filtres au tableau qui en résulte sous une condition. C’est comme la clause `WHERE` mais appliqué a un tableau résultant de `GROUP BY` : la clause `HAVING`. Elle vient toujours après `GROUP BY` ! Telle condition HAVING peut porter sur les éléments cités dans la clause `SELECT` mais aussi sur les fonctions d’agrégation.

```sql
SELECT LOCALITE, COUNT(*), AVG(COMPTE)
FROM CLIENT
GROUP BY LOCALITE
HAVING COUNT(*) >= 3 ;
```

![untitled](ressources/03_le_langage_sql_dml_data_manipulation_language_untitled_7.png)

Il y a deux remarques à faire :

- Le critère de groupement peut inclure plusieurs noms de colonne
- L’ordre des colonnes est indifférent
- Le critère de groupement peut aussi inclure une expression de calcul quelconque

## Ordre des lignes d’un résultat

### Clauses `ORDER BY`, `ASC`, `DESC`

Par construction, l’ordre des lignes d’une table est arbitraire, on ne peut pas supposer que les lignes sont stockées dans un ordre déterminé. Par principe, l’ordre des lignes du résultat d’une requête est aussi arbitraire. Il est possible d’imposer un ordre de présentation en utilisant la clause `ORDER BY`.

```sql
SELECT *
FROM CLIENT
ORDER BY LOCALITE, CAT ;
```

Les clients vont apparaître classés par localité, puis dans chaque localité classés par catégorie. Attention : l’ordre a une importance.

Il est possible de modifier l’ordre utilisé pour le tri

- La clause `ASC` pour le tri ascendant (option par défaut)
- La clause `DESC` pour le trie descendant

Si on crée une colonne avec un calcul ou une fonction d’agrégation, il faudrait le mettre un nom avec la clause `AS` pour après la référencier dans la clause `ORDER BY`.

```sql
SELECT LOCALITE,
	COUNT(*) AS POPULATION,
	SUM(COMPTE)
FROM CLIENT
GROUP BY LOCALITE
ORDER BY POPULATION DESC
```

Finalement, il est possible aussi d’utiliser des critère qui ne sont pas dans la clause `SELECT`.

```sql
SELECT NCOM, NPRO, QCOM
FROM DETAIL D, PRODUIT P
WHERE D.NPRO = P.NPRO
ORDER BY NCOM, QCOM*PRIX DESC ;
```

## Interprétation d’une requête

Ces lignes sont utiles pour lire le code d’une requête et la comprendre :

### Requête monotable

- On considère la table spécifiée dans la clause `FROM`
- On s´electionne les lignes sur la base de la clause `WHERE`
- On classe ces lignes en groupes comme spécifié dans la clause `GROUP BY`
- On ne retient que les lignes qui vérifient la clause `HAVING`
- Les lignes des groupes sont ordonnées selon la clause `ORDER BY` éventuellement
- De chacune des lignes, on extrait les valeurs demandées dans la clause `SELECT`

### Requête multitable

- On considere les tables spécifiées dans la clause `FROM`
- On e↵ectue la jointure de ces tables selon le critere de jointure de la clause `WHERE`
- On sélectionne les lignes de la jointure sur la base des autres conditions de
la clause `WHERE`
- On classe ces lignes en groupes comme spécifié dans la clause `GROUP BY`
- On ne retient que les groupes qui vérifient la clause `HAVING`
- Les lignes des groupes sont ordonnées selon la clause `ORDER BY` évetuellement
- De chacune des lignes, on extrait les valeurs demandées dans la clause `SELECT`
