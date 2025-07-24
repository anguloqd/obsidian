# 00 // TPs

# TP1

[17:22:19] Error while executing SQL query on database 'le_grand_bazard (1)': near ")": syntax error → Error escribiendo un nombre de una columna (columna no encontrada) o olvidaste importar la tabla de la columna

## #1

Donner les noms et couleurs de tous les produits.

R = PRODUIT[NOMP, COULEUR]

```sql
SELECT DISTINCT NOMP, COULEUR
FROM PRODUIT
```

## #2

Donner les noms et quantités en stock des produits de couleur rouge.

R = (PRODUIT: (COULEUR=‘rouge’))[NOMP, QTP]

```sql
SELECT NOMP, QTP
FROM PRODUIT
WHERE COULEUR = "rouge"
```

## #3

Donner les numéros de vente, le nom du client, la quantité vendue pour les ventes du
produit de nom « torchon », réalisées avant le 12/09/87 ;

R = (VENTE(NOMP=’*torchon*’, DATEV < '1987-09-12') $\bowtie$ PRODUIT)[NVEN,NOMC,QTV]

```sql
SELECT NVEN, NOMC, QTV
FROM VENTE, PRODUIT
WHERE (NPRV=NPRO) AND NOMP='torchon' AND DATEV < '1987-09-12'
```

## #4

Donner les noms des clients ayant acheté au moins un produit de couleur verte ;

R = (VENTE(COULEUR=’vert’) $\bowtie$ PRODUIT)[NOMC]

```sql
SELECT DISTINCT NOMC
FROM VENTE, PRODUIT
WHERE (NPRV=NPRO) AND COULEUR='vert'
```

## #5

Donner les noms des fournisseurs qui sont également des clients ;

R = (VENTE $\bowtie$ ACHAT)[NOMF]

```sql
SELECT DISTINCT NOMF
FROM VENTE, ACHAT
WHERE NOMF=NOMC
```

## #6

Donner les noms des fournisseurs qui fournissent les produits de couleur bleu et dont la
quantité en stock (actuellement) est inférieur à 100

R = (ACHAT(COULEUR=’bleu’, QTP<100) $\bowtie$ PRODUIT)[NOMF]

```sql
SELECT DISTINCT NOMF
FROM ACHAT, PRODUIT
WHERE NPRA=NPRO AND COULEUR='bleu' AND QTP<100
```

## #7

Donner le nom des fournisseurs avec lesquels aucune commande de produit n’a été réalisée depuis le 30/06/87 ;

$R_1$ = (ACHAT : (DATEA >= '1987-06-30'))[NOMF]

$R_2$ = (ACHAT : (NOMF $\notin$ $R_1$))[NOMF]

```sql
SELECT DISTINCT NOMF
FROM ACHAT
WHERE NOMF NOT IN (SELECT DISTINCT NOMF
                    FROM ACHAT
                    WHERE DATEA >= '1987-06-30')
```

// mmm, il semble que DISTINCT est comme un quant. existentiel

## #8

Donner pour chaque produit, les noms des fournisseurs du produit et les noms des clients
l’ayant acheté ;

$R$ = (ACHAT $\bowtie$ PRODUIT $\bowtie$ VENTE)[NOMP,NOMF,NOMC]

```sql
SELECT DISTINCT NOMP, NOMF, NOMC
FROM PRODUIT, ACHAT, VENTE
WHERE NPRO=NPRA AND NPRO=NPRV
```

## #9

Donner les noms des clients ayant acheté au moins une fois de tous les produits (actuellement) disponibles !!! (les produits une fois vendus peuvent être non-disponibles actuellement);

$R_1$ = (VENTE $\bowtie$ PRODUIT)[NOMC, NPRV]

$R_2$ = ((VENTE $\times$ PRODUIT) : ((NOMC, NPRO) $\notin R_1$))[NOMC]

$R_3$ = (VENTE : (NOMC $\notin R_2$))[NOMC]

```sql
SELECT DISTINCT NOMC
FROM VENTE
WHERE NOMC NOT IN (SELECT DISTINCT A.NOMC
                    FROM VENTE A, PRODUIT B
                    WHERE (A.NOMC, B.NPRO) NOT IN (SELECT DISTINCT NOMC, NPRV
                                                    FROM VENTE, PRODUIT
                                                    WHERE NPRV=NPRO))

// primero busco las ventas de productos que están ACTUALMENTE disponibles
// luego genero todas las parejas cartesianas (nomc,npro) que no están en las ventas de antes
// eso significa todas las ventas de productos actualmnt. dispo que NO sucederieron
// finalmente, busco los clientes que no están en en las compras no realizadas
// eso significa que ellos compraron todas los prod. actmnt. dispo
```

## #10

Donner les noms des fournisseurs qui fournissent tous les produits ;

$R_1$ = ACHAT[NOMF, NPRA]

$R_2$ = ((ACHAT$_A$ $\times$ ACHAT$_B$) : ((NOMF, NPRA) $\notin R_1$))[NOMF]

$R_3$ = (ACHAT : (NOMF $\notin R_2$))[NOMF]

```sql
SELECT DISTINCT NOMF
FROM ACHAT
WHERE NOMF NOT IN
            (SELECT DISTINCT A.NOMF
            FROM ACHAT A, ACHAT B
            WHERE (A.NOMF, B.NPRA) NOT IN (SELECT DISTINCT NOMF, NPRA
                                            FROM ACHAT))

// un peu la même idée qu'avant
```

## #11

Donner, pour chaque couleur, le nombre de produits de cette couleur ;

Pas d’expression en algèbre relationnelle.

Somme de quantités individuelles ou juste la “version” de chaque article ? 

```sql
SELECT COULEUR, COUNT(COULEUR)
FROM PRODUIT
GROUP BY COULEUR

// on utilise souvent GROUP BY avec les fonction agrégatives comme COUNT
```

## #12

Donner le nom et le nombre des produits vendus lors de la plus grosse vente.

Pas d’expression en algèbre relationnelle.

```sql
SELECT NOMP, QTV
FROM PRODUIT, VENTE
WHERE DATEV = (SELECT DATEV
                FROM (SELECT DATEV, MAX(Q)
                    FROM (SELECT DATEV, SUM(QTV) AS Q
                            FROM VENTE
                            GROUP BY DATEV
                        )
                    )
                ) AND (NPRO=NPRV)

// WHERE : où la date est celle de la plus grosse vente et le produit a été
// effectivement vendu (sinon ça retourne un produit cartesien)

// bref montrer deux colonnes de 2 tableaux diff. sans faire jointure nous montre
// un produit cartesien !
```

Partie : Travaux Pratique. Pour chacune des requêtes précédentes donner les lignes résultats obtenues. La base de données est téléchargeable sur le page du cours. Le fichier s’appelle « le grand [bazard.bd](http://bazard.bd/) ». 

# TP2

file:///C:/Users/Daniel/Downloads/tp02.pdf

## #1

Donner le nom de tous les employés.

```sql
SELECT ENAME
FROM EMP;
```

## #2

Donner le nom et la date d’embauche des employés du département 20

```sql
SELECT ENAME, HIREDATE
FROM EMP
WHERE DEPTNO='20';
```

## #3

Donner tous les salaires perçus par les employés de l’entreprise.

```sql
SELECT DISTINCT SAL
FROM EMP;
```

## #4

Donner le nom et le numéro du département des employés travaillant à Dallas.

! : fais gaffe à “,” a la fin de clause from, ça pose de problèmes

```sql
SELECT ENAME, DEPTNO
FROM EMP E, DEPT D
WHERE (E.DEPTNO = D.DEPTNO) AND LOC='DALLAS';
```

## #5

Donner le nom et le salaire des employés dont le nom commence par un ’M’ et dont le
salaire est supérieur à 1290$.

```sql
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 1290 AND ENAME LIKE 'M%';
```

## #6

Donner les départements employant des CLERK, SALESMAN **et** des ANALYST.

! : J’ai consideré utiliser EXISTS, mais pas besoin

! : C’est les trois jobs à la fois, pas au moins un

```sql
// pour au moins un des trois jobs
SELECT DISTINCT DEPTNO, DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO AND JOB IN ('ANALYST', 'CLERK', 'SALESMAN')

// pour strictement les trois jobs simultanés
WITH subq AS (
  SELECT DISTINCT D.DEPTNO, JOB, DNAME
  FROM EMP E, DEPT D
  WHERE E.DEPTNO = D.DEPTNO
)

SELECT DISTINCT DEPTNO, DNAME
FROM subq
WHERE (DEPTNO, 'CLERK') IN (SELECT DEPTNO, JOB FROM subq)
AND (DEPTNO, 'SALESMAN') IN (SELECT DEPTNO, JOB FROM subq)
AND (DEPTNO, 'ANALYST') IN (SELECT DEPTNO, JOB FROM subq)
```

! : puedes usar una couple porque estás preguntando si la couple está en una tabla de couples, incluso si en el from principal es una tabla de triplets

Parece ser que IN no toma tablas nombradas en la misma query

## #7

Donner le nom des chefs dont les employés perçoivent des commissions.

! : le chef peut être chef de plusieurs employés, donc DISTINCT pour éviter répetition

! : données cycliques → auto-jointure

```sql
SELECT DISTINCT B.EMPNO, B.ENAME
FROM EMP A, EMP B
WHERE A.MGR = B.EMPNO AND A.COMM > 0;
```

## #8

Donner le nom et le salaire des employés des départements de Chicago et Dallas dont le
salaire est supérieur à 1000$.

[09:55:23] Error while executing SQL query on database 'les_employes': near ")": syntax error

Normalement erreur sur un nom d’une colonne

Aussi, noms des villes (chaînes quoi) en majuscule !

```sql
SELECT ENAME, SAL
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO AND LOC IN ('CHICAGO', 'DALLAS') AND SAL > 1000
```

## #9

Donner le nom des employés qui gagnent plus que leur chef.

! : attention à quel tableau tu en tire les colonnes, si B.EMPNO ou A.EMPNO !!!

```sql
SELECT DISTINCT B.EMPNO, B.ENAME
FROM EMP A, EMP B
WHERE A.MGR = B.EMPNO AND A.SAL > B.SAL
```

## #10

Donner la hiérarchie de l’entreprise. ORDER BY et tableau SALGRADE, on associe un grand salaire a une grande niveau dans la hiérarchie

HIERARCHIE(ENAME, NIVEAU)

```sql
WITH

NIV1 AS
(SELECT EMPNO, ENAME, '1' AS NIVEAU
FROM EMP
WHERE MGR IS NULL),

NIV2 AS
(SELECT EMPNO, ENAME, '2' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV1)),

NIV3 AS
(SELECT EMPNO, ENAME, '3' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV2)),

NIV4 AS
(SELECT EMPNO, ENAME, '4' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV3))

SELECT * FROM NIV1
UNION
SELECT * FROM NIV2
UNION 
SELECT * FROM NIV3
UNION
SELECT * FROM NIV4

ORDER BY NIVEAU
```

## #11

Donner le nombre d’employés par niveau de hiérarchie.

```sql
WITH

NIV1 AS
(SELECT EMPNO, ENAME, '1' AS NIVEAU
FROM EMP
WHERE MGR IS NULL),

NIV2 AS
(SELECT EMPNO, ENAME, '2' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV1)),

NIV3 AS
(SELECT EMPNO, ENAME, '3' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV2)),

NIV4 AS
(SELECT EMPNO, ENAME, '4' AS NIVEAU
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV3))

SELECT NIVEAU, COUNT(*) FROM NIV1
UNION
SELECT NIVEAU, COUNT(*) FROM NIV2
UNION 
SELECT NIVEAU, COUNT(*) FROM NIV3
UNION
SELECT NIVEAU, COUNT(*) FROM NIV4
```

## #12

Donner la moyenne des salaires par niveau de hiérarchie.

Noter qu’on ajouter SAL aux colonnes de chaque tableau des niveaux 

```sql
WITH

NIV1 AS
(SELECT EMPNO, ENAME, '1' AS NIVEAU, SAL
FROM EMP
WHERE MGR IS NULL),

NIV2 AS
(SELECT EMPNO, ENAME, '2' AS NIVEAU, SAL
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV1)),

NIV3 AS
(SELECT EMPNO, ENAME, '3' AS NIVEAU, SAL
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV2)),

NIV4 AS
(SELECT EMPNO, ENAME, '4' AS NIVEAU, SAL
FROM EMP
WHERE MGR IN (SELECT EMPNO FROM NIV3))

SELECT NIVEAU, AVG(SAL) FROM NIV1
UNION
SELECT NIVEAU, AVG(SAL) FROM NIV2
UNION 
SELECT NIVEAU, AVG(SAL) FROM NIV3
UNION
SELECT NIVEAU, AVG(SAL) FROM NIV4
```

# TP3

(Les requêtes commencent de la question 5)

Q6 : Donner le nom des clients qui ne visitent **aucun** monument.
”Aucun” monument = tous les clients - clients qui visitent au moins un monument

**TOUS = AUCUN (NOT(EGALITE))+ AU MOINS UN (EGALITE SIMPLE)**

Q10 : pour filtrer des valeurs de une table de la forme (clé, non-clé) où on s’intéresse à des clés avec n valeurs différentes de non-clé, on peut utiliser GROUP BY CLE HAVING COUNT(DISTINCT NONCLE) = n, même si faire GROUP BY CLE est inutile, ça nous donne accès à HAVING.

```sql
SELECT *
FROM T
GROUP BY CLE
HAVING COUNT(DISTINCT NONCLE) < 2
```