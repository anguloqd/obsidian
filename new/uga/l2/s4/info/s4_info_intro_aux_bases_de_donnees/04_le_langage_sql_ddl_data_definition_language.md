# 04 // le langage SQL DDL : data definition language

[Slides de SQL 3](05.sql3.pdf)

# Création d’un schéma

## `create schema`

Une base de données est définie par son schéma. SQL propose de créer ce schéma avant de définir ses composants :

```sql
create schema CLICOM ;
```

Cette instruction pourra être accompagné de divers paramètres spécifiant notamment les conditions d’autorisation d’acces. Les schémas sont rassemblés dans un catalogue qui représente un ensemble de bases de données.

# Création d’une table

## `create table`

L’opération ci-dessous produit une table (vide, i.e., sans lignes) dont le schéma est conforme aux indications données par la requête `create table`. On y spécifie le nom de la table et la description de ses colonnes, on spécifiera pour chaque colonne son nom et le type de ses valeurs.

```sql
create table CLIENT (
	NCLI char(10),
	NOM char(32),
	ADRESSE char(60),
	LOCALITE char(30),
	CAT char(2),
	COMPTE decimal(9,2)
) ;
```

Une table peut être supprimée. Elle sera inconnue du SGBD et son contenu sera perdu :

```sql
drop table COMMANDE ;
```

Les lignes d’une table sont préalablement supprimées avant sa suppression, la suppression des lignes d’une table est soumise aux contraintes référentielles. Par exemple, la suppression de la table COMMANDE pourrait entraîner la suppression de toutes les lignes de la table DETAIL (mais pas de la table).

Chaque table accepte un type de donnée, limité par son argument numérique :

- `SMALLINT` : entiers signés courts (16 bits)
- `INTEGER` : entiers signés longs (32 bits)
- `NUMERIC(p,q)` : nombres décimaux de `p` chiffres dont `q` après le point décimal ; si elle n’est pas mentionnée, la valeur de `q` est 0
- `FLOAT(p)` : nombres en virgule flottante d’au moins `p` bits significatifs (`p` est optionnel)
- `CHARACTER(p)` ou `CHAR(p)` : chaînes de caracteres de longueur fixe de `p` caractères
- `CHARACTER VARYING` ou `VARCHAR(p)` : chaînes des caracteres de longueur variable d’un plus `p` caractères
- `BIT(p)` : chaînes de longueur fixe de `p` bits
- `BIT VARYING (p)` : chaînes de longueur variable ou d’au plus `p` bits
- `DATE` : dates (années, mois, jours)
- `TIME` : instants (heures, minutes, secondes, éventuellement 1000e de seconde)
- `TIMESTAMP` : dates et temps
- `INTERVAL` : intervalles en années/mois/jours entre dates ou en heures/minutes/secondes entre instants

## Domaines de valeurs : `create domain`

On peut définir un domaine de valeurs, qui est une type de donnée déjà défini et qui est réutilisable dans la définition de plusieurs colonnes, ce qui rend la lecture plus aisée.

```sql
create domain MONTANT decimal(9,2) ;
create domain MATRICUL char(10) ;
create domain LIBELLE char(32) ;

create table CLIENT (
	NCLI MATRICULE,
	NOM LIBELLE ,
	ADRESSE char(60),
	LOCALITE LIBELLE ,
	CAT char(2),
	COMPTE MONTANT
) ;
```

## Valeurs par défaut : `default`

On peut aussi définir une valeur par défaut que le SGBD assignera automatiquement à une colonne (éventuellement via son domaine) lorsque l’utilisateur omettra d’en fournir une lors de la création d’une ligne.

```sql
create domain MONTANT decimal (9,2) default 0.0 ;
create CAT char (2) default 'AA' ;
create DATECOM date not null default current date ;
```

# Les identifiants

## Clauses `primary key`, `foreign key` et `unique`

On peut déclarer les clés principales, la clé étrangère et les valeurs uniques hors-clé (càd. autres identifiants) avec les clauses `primary key`, `foreign key` et `unique` respectivement.

```sql
create table DETAIL (
	NCOM char(12),
	NPRO char(15),
	QCOM decimal(8),
	primary key (NCOM, NPRO) ,
	foreign key (NCOM) references COMMANDE,
	foreign key (NPRO) references PRODUIT
);

create table ASSURE (
	NUM AFFIL char(10),
	NUM IDENT char(15),
	NOM char(35),
	primary key (NUM AFFIL),
	unique (NUM IDENT)
);
```

Par défaut, l’identifiant visé par la clé étrangère dans la table cible est l’identifiant primaire de celle-ci. Il est toujours possible de faire viser un identifiant secondaire de la table même si cela est déconseillé.

## Clause `match` pour les clés étrangères

Une clé étrangère comporte autant de colonnes que l’identifiant cible et ses colonnes sont de même type. Si au moins une des colonnes est facultative (càd. il est possible qu’elle contienne des valeurs non-remplies ou `null`), alors il est possible de préciser via la clause `match`, la manière dont l’intégrité référentielle sera vérifiée en présence de valeurs nulles.

- `match simple` : si toute les colonnes de la clé étrangère possedent une valeur, la contrainte référentielle est évaluée, sinon elle est ignorée
- `match full` : si les colonnes sont toutes nulles, la contrainte est ignorée. Si elles sont toutes non nulles (remplies), elle est évaluée. Dans les autres cas, elle n’est pas satisfaite
- `match partial` : la contrainte est évaluée pour les colonnes non nulles (remplies). La table cible doit contenir au moins une ligne dont l’identifiant comporte les valeurs non nulles de la clé étrangère

```sql
foreign key (NCLI , NFOURN) references
ACHAT(NCLI , NFOURN) match full
```

# Caractère d’une colonne : obligatoire/facultatif

## Clauses `null` et `not null`

Par défaut, i.e., si l’on ne spécifie rien, toute colonne est facultative. Le caractère obligatoire d’une colonne se déclare avec la clause `not null`.

```sql
create table OFFRE (
	NUMFL char(10) not null,
	NUMPL char(15) not null,
	PRIX decimal(8),
	primary key (NUMFL, NUMPL),
	foreign key (NUMFL) references FOURNISSEUR,
	foreign key (NUMPL) references PIECE
) ;
```

Il existe aussi une forme synthétique pour spécifier les contraintes :

```sql
create table COMMANDE (
	NCOM char (12) not null primary key
	NCLI char (10) not null references CLIENT, //on comprend que c'est foreign key
	DATECOM date not null
);
```

# Ajout/retrait de contraintes et colonnes

## Par rapport aux colonnes…

```sql
// ajoute colonne POIDS dont toutes les valeurs sont null
alter table PRODUIT add column POIDS smallint ;

// supprime colonne PRIX
alter table PRODUIT drop column PRIX ;

// modifie la valeur par defaut de colonne CAT
alter table CLIENT alter column CAT set default '00' ;
```

En plus, on peut utiliser alter et drop avec les domaines comme suit :

```sql
alter domain MONTANT set default -1.0 ; // modifie le domaine MONTANT
drop domain MATRICULE ; // supprime le domaine MATRICULE
```

## Par rapport aux contraintes (identifiants, facultativité)…

La clause alter table permet aussi d’ajouter ou retirer des contraintes d’intégrité à posteriori : 

```sql
alter table CLIENT add primary key (NCLI) ;
alter table CLIENT add unique (NOM,ADRESSE,LOCALITE) ;
alter table COMMANDE add foreign key (NCLI) references CLIENT ;
```

**Note** : la demande d’ajout d’un identifiant sera **refusée si** les données que la table contient déjà violent cette propriété.

D’ailleurs, une colonne obligatoire peut être déclarée facultative et inversement si les données le permettent :

```sql
alter table CLIENT alter CAT not null ; // n'accepte plus des nulls
alter table CLIENT alter ADRESSE null ; // desormais accepte des nulls
```

On peut même nommer des contraintes avec la clause `constraint` : on voit que les contraintes sont des propositions par rapport aux identifiants et la facultativité des colonnes.

```sql
create table DETAIL (
	NCOM char(12) not null,
	NPRO char(15) constraint C1 not null,
	QCOM decimal(8),
	constraint C2 primary key (NCOM, NPRO),
	constraint C3 foreign key (NPRO) references PRODUIT
) ;

alter table CLIENT
	add constraint C_CLI_U unique (NOM, ADRESSE, LOCALITE) ;

alter table COMMANDE
	add constraint C5 foreign key (NCLI) references CLIENT ;

alter table DETAIL drop constraint C2 ; // ON EFFACE UNE CONTRAINTE COMME ÇA.
```

# Modification de données

## Introduction des données : `INSERT INTO/(VALUES, SFW)`

L’ajout d’une ligne s’effectue avec l’instruction `INSERT INTO/VALUES` comme suit :

```sql
INSERT INTO DETAIL VALUES ('30185' , 'PA45' , 12) ;
```

L’ordre des valeurs est celui de la d´eclaration des colonnes lors de la création de la table. Lorsque toutes les valeurs ne sont pas introduites, il faut préciser le nom et l’ordre des colonnes :

```sql
INSERT INTO CLIENT (NCLI , NOM, ADRESSE, COMPTE, LOCALITE)
	VALUES ('C402', 'BERNIER', '28 avenue de France' , -2500, 'Lausanne') ;
```

Deux notes à faire :

- Toute colonne non spécifiée, telle que CAT, prend la valeur nulle, ou la valeur par défaut
- Toute colonne obligatoire (`not null`) doit recevoir une valeur sauf si on lui a assigné une valeur par défaut

En plus, il est possible d’insérer dans une table existante des données extraites d’une autre table. Ces données sont obtenues par une expression `SFW` attachée à l’instruction `insert into/SFW`.

```sql
INSERT INTO CLIENT_TOULOUSE
	SELECT NCLI , NOM, ADRESSE
	FROM CLIENT
	WHERE LOCALITE = 'Toulouse' ;
```

**Note pratique** : on appelle parfois ses tables snapshot : c’est juste la même table CLIENT mais pour les clients de Toulouse. Elles sont utilisées pour distribuer l’information à partir d’une base de données centrale et pour constituer des systèmes d’aide à la décision (les entreprôts de données).

## Suppression de données : `DELETE FROM/WHERE`

L’ordre de suppression porte sur un sous-ensemble des lignes d’une table. Les lignes à supprimer sont désignées par la clause `WHERE` dont le format est le même que celui de l’instruction SFW :

```sql
// la commande supprime de CLIENT la ligne correspondant au client K111

DELETE FROM CLIENT
WHERE NCLI = 'K111' ;

// la commande supprime de la table DETAIL les lignes, quel qu’en soit le nombre,
// qui spécifient un produit en rupture de stock

DELETE FROM DETAIL WHERE NPRO IN
(SELECT NPRO FROM PRODUIT WHERE QSTOCK <= 0) ;
```

**Note** : après toute opération de suppression, la base de données doit être dans un état qui respecte les contraintes d’intégrité

## Modification de données : `UPDATE/SET/WHERE`

Comme la suppression, la modification est effectuée sur toutes lignes qui vérifient une condition de sélection :

```sql
UPDATE CLIENT
SET ADRESSE = '29, av. de la Magne' ,
LOCALITE = 'Niort'
WHERE NCLI = 'F011' ;

// les nouvelles valeurs peuvent être obtenues par une expression arithmétique

UPDATE PRODUIT
SET PRIX = PRIX * 1.05
WHERE LIBELLE like ’%SAPIN%’ ;
```

Et, tout égal qu’au cas de `DELETE`, les données modifiées peuvent provenir également de la base de données elle-même avec une requête `SFW` :

```sql
// la requête déduit de la quantité en stock de chaque produit les quantités
// actuellement en commande

UPDATE PRODUIT P
SET QSTOCK = QSTOCK - (SELECT SUM(QCOM)
FROM DETAIL WHERE NPRO = P.NPRO)
WHERE EXISTS (SELECT * FROM DETAIL
WHERE NPRO = P.NPRO) ;
```

## Modes face à la suppression/modification de lignes

Une requête de suppression ou modification du contenu de la base de données (`INSERT`, `DELETE`, `UPDATE`, etc.) n’est exécutée que si le résultat respecte toutes les contraintes d’intégrité définies sur cette base. Une opération dont l’exécution laisse les données dans un état invalide est refusée.

Par exemple, prenons ces tables CLIENT et COMMANDE :

```sql
create table CLIENT (
	NCLI char(10) not null,
	...,
	primary key (NCLI)
);

create table COMMANDE (
	NCOM char(12) not null,
	NCLI char(10) not null,
	...,
	primary key (NCOM),
	foreign key (NCLI) references CLIENT
);
```

Lors de la suppression d’une ligne de la table CLIENT, trois types de comportements sont possibles : blocage (`no action`), propagation (`cascade`) ou découplage (`set null`).

Imaginons, pour les trois cas, on veut supprimer des lignes colonne NCLI de CLIENT

```sql
DELETE FROM CLIENT
WHERE (NCLI...);
```

**Note** : tout ce qu’on montrera pour une commande de suppression, applique aussi pour une commande de modification. Il suffit de changer “`on delete…`” par “`on update…`”.

### Blocage : `no action`

```sql
create table COMMANDE (
	NCOM char(12) not null,
	NCLI char(10) not null,
	...,
	primary key (NCOM),
	foreign key (NCLI) references CLIENT on delete no action
);
```

Lors qu’un blocage se produit, la suppression est refusée. Un blocage se produit s’il existe une ou plusieurs lignes de COMMANDE dépendantes, i.e., dont `COMMANDE.NCLI = CLIENT.NCLI`.

### Propagation : `cascade`

```sql
create table COMMANDE (
	NCOM char(12) not null,
	NCLI char(10) not null,
	...,
	primary key (NCOM),
	foreign key (NCLI) references CLIENT on delete cascade
);
```

Lors qu’une propagation se produit, la suppression est acceptée. Une propagation entraîne la suppression conjointe des lignes de COMMANDE dépendantes.

### Découplage : `set null`

```sql
create table COMMANDE (
	NCOM char(12) not null,
	NCLI char(10) not null,
	...,
	primary key (NCOM),
	foreign key (NCLI) references CLIENT on delete set null
);
```

Lors qu’un découplage se produit, la suppression est acceptée. Un découplage entraîne l’attribution de la valeur nulle à la colonne NCLI, i.e., les données sont rendues indépendantes. **Ce mode sera notamment utilisé pour les clés étrangères cycliques**.

### Interaction entre les modes

```sql
create table CLIENT (
	NCLI char(10) not null,
	...,
	primary key (NCLI)
);

create table COMMANDE (
	NCOM char(12) not null,
	NCLI char(10) not null,
	...,
	primary key (NCOM),
	foreign key (NCLI) references CLIENT on delete cascade
);

create table DETAIL (
	NCOM char(12) not null,
	NPRO char(15) not null,
	...,
	primary key (NCOM, NPRO),
	foreign key (NCOM) references COMMANDE on delete no action
);
```

1. Si on tente d’eliminer une ligne de CLIENT, le mode “`cascade`” de COMMANDE.NCLI tentera d’eliminer les lignes qui en dépendent.
2. Or, la table DETAIL depende des valeurs de la colonne COMMANDE.NCOM, et son mode est “`no action`”, donc elle refusera la suppression d’une ligne de COMMANDE.
3. La suppression original d’une ligne de CLIENT sera aussi refusée, même si le mode de COMMANDE était “`cascade`”.

De ce schéma, on déduit qu’on ne peut supprimer un client que s’il n’a aucune commande qui possède des détails.