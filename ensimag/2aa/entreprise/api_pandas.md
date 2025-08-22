# Guide API de Pandas
## Création de structures de données

```python
# Series
pd.Series([1, 2, 3, 4])
pd.Series({'a': 1, 'b': 2})
pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c'])

# DataFrame
pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B'])
pd.DataFrame.from_dict(dict, orient='index')
pd.DataFrame.from_records(records)
```

## Chargement et sauvegarde de données

```python
# Lecture de fichiers
pd.read_csv('file.csv', sep=',', header=0, index_col=0, usecols=['A', 'B'])
pd.read_excel('file.xlsx', sheet_name='Sheet1', skiprows=1, nrows=100)
pd.read_json('file.json', orient='records')
pd.read_sql('SELECT * FROM table', connection)
pd.read_parquet('file.parquet')
pd.read_hdf('file.h5', key='data')
pd.read_pickle('file.pkl')

# Écriture de fichiers
df.to_csv('output.csv', index=False, sep='\t')
df.to_excel('output.xlsx', sheet_name='data', index=False)
df.to_json('output.json', orient='records')
df.to_sql('table_name', connection, if_exists='replace')
df.to_parquet('output.parquet')
df.to_pickle('output.pkl')
```

## Inspection et informations sur les données

```python
# Informations de base
df.head(n=5)
df.tail(n=5)
df.info()
df.describe()
df.shape
df.columns
df.index
df.dtypes

# Utilisation mémoire
df.memory_usage(deep=True)
df.select_dtypes(include=['number'])
df.select_dtypes(exclude=['object'])

# Valeurs uniques
df.nunique()
df['col'].unique()
df['col'].value_counts()
df['col'].value_counts(normalize=True)  # proportions
```

## Indexation et sélection

```python
# Sélection de colonnes
df['col']
df[['col1'_'col2']]
df.col  # accès par attribut

# Sélection de lignes par label
df.loc[row_label]
df.loc[row_start:row_end]
df.loc[row_list]
df.loc[boolean_mask]

# Sélection de lignes par position
df.iloc[0]
df.iloc[0:5]
df.iloc[[0_2_4]]
df.iloc[boolean_array]

# Sélection combinée
df.loc[row_indexer, col_indexer]
df.iloc[row_indexer, col_indexer]

# Indexation avancée
df.at[row_label, col_label]  # valeur unique par label
df.iat[row_pos, col_pos]     # valeur unique par position
df.query('col1 > 5 and col2 < 10')
df.eval('new_col = col1 + col2')
```

## Filtrage et indexation booléenne

```python
# Conditions
df[df['col'] > 5]
df[df['col'].isin([1, 2, 3])]
df[df['col'].between(1, 10)]
df[df['col'].str.contains('pattern')]
df[df['col'].str.startswith('prefix')]
df[df['col'].str.endswith('suffix')]

# Conditions multiples
df[(df['col1'] > 5) & (df['col2'] < 10)]
df[(df['col1'] > 5) | (df['col2'] < 10)]
df[~(df['col'] > 5)]  # négation

# Opérations sur chaînes
df['col'].str.len()
df['col'].str.upper()
df['col'].str.lower()
df['col'].str.replace('old', 'new')
df['col'].str.split('delimiter')
df['col'].str.extract('(\\d+)')  # groupes regex
df['col'].str.extractall('(\\d+)')
```

## Nettoyage de données et valeurs manquantes

```python
# Détection des valeurs manquantes
df.isna()
df.isnull()  # identique à isna()
df.notna()
df.notnull()  # identique à notna()
df.isna().sum()

# Gestion des valeurs manquantes
df.dropna()  # supprimer lignes avec NaN
df.dropna(axis=1)  # supprimer colonnes avec NaN
df.dropna(how='all')  # supprimer seulement si toutes valeurs sont NaN
df.dropna(thresh=2)  # supprimer si moins de 2 valeurs non-NaN
df.dropna(subset=['col1', 'col2'])

df.fillna(value)
df.fillna(method='ffill')  # remplissage avant
df.fillna(method='bfill')  # remplissage arrière
df.fillna(df.mean())  # remplir avec moyenne
df.interpolate()  # interpolation

# Doublons
df.duplicated()
df.drop_duplicates()
df.drop_duplicates(subset=['col1', 'col2'])
df.drop_duplicates(keep='last')
```

## Transformation de données

```python
# Application de fonctions
df.apply(func)  # appliquer à chaque colonne
df.apply(func, axis=1)  # appliquer à chaque ligne
df.applymap(func)  # application élément par élément
df['col'].map(func)  # mapper valeurs dans Series
df['col'].map({old_val: new_val})  # dictionnaire de mapping

# Transform
df.transform(func)
df['col'].transform(lambda x: (x - x.mean()) / x.std())

# Assigner nouvelles colonnes
df.assign(new_col=lambda x: x['col1'] + x['col2'])
df['new_col'] = df['col1'] + df['col2']

# Remplacer valeurs
df.replace(old_value, new_value)
df.replace([val1, val2], [new_val1, new_val2])
df.replace(regex_dict)
```

## Agrégation et groupement

```python
# Agrégation de base
df.sum()
df.mean()
df.median()
df.std()
df.var()
df.min(), df.max()
df.count()
df.describe()

# Opérations GroupBy
grouped = df.groupby('col')
grouped = df.groupby(['col1', 'col2'])
grouped.size()  # comptage de chaque groupe
grouped.count()  # comptage non-null par colonne
grouped.sum()
grouped.mean()
grouped.agg(['sum', 'mean', 'count'])
grouped.agg({'col1': 'sum', 'col2': 'mean'})

# GroupBy avancé
grouped.apply(custom_function)
grouped.transform(lambda x: (x - x.mean()) / x.std())
grouped.filter(lambda x: len(x) > 5)
df.groupby('col').nth(0)  # première ligne de chaque groupe
df.groupby('col').head(2)  # 2 premières lignes de chaque groupe
```

## Fusion et jointure

```python
# Concaténation
pd.concat([df1, df2])  # empilement vertical
pd.concat([df1, df2], axis=1)  # empilement horizontal
pd.concat([df1, df2], ignore_index=True)
pd.concat([df1, df2], keys=['df1', 'df2'])

# Fusion
pd.merge(df1, df2, on='key')
pd.merge(df1, df2, left_on='key1', right_on='key2')
pd.merge(df1, df2, how='inner')  # inner, outer, left, right
pd.merge(df1, df2, left_index=True, right_index=True)
pd.merge(df1, df2, suffixes=('_left', '_right'))

# Méthodes DataFrame
df1.merge(df2, on='key')
df1.join(df2)  # jointure sur index
df1.join(df2, how='outer', lsuffix='_left', rsuffix='_right')
```

## Restructuration de données

```python
# Tableaux croisés dynamiques
pd.pivot_table(df, values='value', index='row', columns='col', aggfunc='mean')
df.pivot(index='row', columns='col', values='value')
df.pivot_table(index='row', columns='col', values='value', fill_value=0)

# Melt (dépivot)
pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])
pd.melt(df, id_vars=['id'], var_name='variable', value_name='value')

# Stack/Unstack
df.stack()  # pivoter colonnes vers lignes
df.unstack()  # pivoter lignes vers colonnes
df.unstack(level=0)
df.unstack(fill_value=0)

# Tableau croisé
pd.crosstab(df['col1'], df['col2'])
pd.crosstab(df['col1'], df['col2'], normalize='columns')
```

## Tri et classement

```python
# Tri
df.sort_values('col')
df.sort_values(['col1', 'col2'], ascending=[True, False])
df.sort_index()
df.sort_index(axis=1)  # trier colonnes

# Classement
df['col'].rank()
df['col'].rank(method='dense')  # dense, min, max, average, first
df.rank(axis=1)  # classer à travers colonnes
```

## Opérations sur les séries temporelles

```python
# Conversion DateTime
pd.to_datetime(df['date_col'])
pd.to_datetime('2023-01-01')
pd.to_datetime(['2023-01-01', '2023-01-02'])

# Création de plages de dates
pd.date_range('2023-01-01', '2023-12-31', freq='D')
pd.date_range('2023-01-01', periods=365, freq='D')
pd.bdate_range('2023-01-01', '2023-12-31')  # jours ouvrables

# Indexation DateTime
df.set_index('date_col')
df.loc['2023']
df.loc['2023-01':'2023-06']
df.between_time('09:00', '17:00')
df.at_time('15:30')

# Rééchantillonnage
df.resample('M').mean()  # moyenne mensuelle
df.resample('Q').sum()   # somme trimestrielle
df.resample('W').last()  # dernière valeur hebdomadaire
df.resample('D').interpolate()

# Opérations roulantes
df.rolling(window=7).mean()
df.rolling(window=30).std()
df.expanding().mean()  # fenêtre expansive
df.ewm(span=10).mean()  # moyenne pondérée exponentiellement

# Gestion des fuseaux horaires
df.tz_localize('UTC')
df.tz_convert('US/Eastern')

# Lag/Lead
df.shift(1)   # décalage de 1 période
df.shift(-1)  # avance de 1 période
df.diff()     # première différence
df.pct_change()  # changement en pourcentage

# Propriétés datetime
df['date'].dt.year
df['date'].dt.month
df['date'].dt.day
df['date'].dt.dayofweek
df['date'].dt.dayname()
df['date'].dt.quarter
df['date'].dt.to_period('M')
```

## Séries temporelles avancées

```python
# Conversion de fréquence
df.asfreq('D')
df.asfreq('M', method='ffill')

# Opérations de période
pd.PeriodIndex(['2023-01', '2023-02'], freq='M')
df.to_period('M')
df.to_timestamp()

# Durées temporelles
pd.Timedelta('1 days')
pd.to_timedelta(['1 days', '2 hours'])
df['duration'] = df['end_time'] - df['start_time']

# Logique métier
from pandas.tseries.offsets import BDay
df.index + BDay(1)  # ajouter 1 jour ouvrable
```

## Données catégorielles

```python
# Créer catégoriel
df['cat_col'] = pd.Categorical(df['col'], categories=['A', 'B', 'C'])
df['cat_col'] = df['col'].astype('category')

# Opérations catégorielles
df['cat_col'].cat.categories
df['cat_col'].cat.codes
df['cat_col'].cat.add_categories(['D'])
df['cat_col'].cat.remove_categories(['A'])
df['cat_col'].cat.reorder_categories(['C', 'A', 'B'])
```

## Opérations MultiIndex

```python
# Création MultiIndex
pd.MultiIndex.from_arrays([['A', 'A', 'B'], [1, 2, 1]])
pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1)])
pd.MultiIndex.from_product([['A', 'B'], [1, 2]])

# Opérations DataFrame MultiIndex
df.set_index(['col1', 'col2'])
df.reset_index()
df.swaplevel()
df.reorder_levels([1, 0])

# Sélection avec MultiIndex
df.loc[('A', 1)]
df.loc[pd.IndexSlice['A', :], :]
df.xs('A', level=0)
```

## Modèles courants de LeetCode

```python
# Trouver top N dans chaque groupe
def top_n_per_group(df, group_col, value_col, n=3):
    return df.groupby(group_col)[value_col].nlargest(n)

# Totaux cumulés
def running_total(df, col):
    return df[col].cumsum()

# Fonctions de fenêtre
def rank_within_group(df, group_col, rank_col):
    return df.groupby(group_col)[rank_col].rank(ascending=False)

# Pivot avec agrégation
def pivot_with_agg(df, index_col, column_col, value_col, agg_func='sum'):
    return df.pivot_table(
        index=index_col, 
        columns=column_col, 
        values=value_col, 
        aggfunc=agg_func, 
        fill_value=0
    )

# Trouver séquences consécutives
def consecutive_groups(df, col):
    return (df[col] != df[col].shift()).cumsum()

# Changement en pourcentage entre périodes
def period_over_period_change(df, date_col, value_col, periods=1):
    df_sorted = df.sort_values(date_col)
    return df_sorted[value_col].pct_change(periods=periods)
```

## Optimisation des performances

```python
# Opérations efficaces
df.query('col > 5')  # plus rapide que df[df.col > 5] pour gros données
df.eval('new_col = col1 + col2')  # plus rapide que df['new_col'] = df['col1'] + df['col2']

# Optimisation mémoire
df.info(memory_usage='deep')
pd.DataFrame.sparse.from_coo(sparse_matrix)  # tableaux épars

# Chunking pour gros fichiers
chunk_iter = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunk_iter:
    process_chunk(chunk)
```
