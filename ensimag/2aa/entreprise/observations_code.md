-   jupyter notbeooks ne peuvent pas gerer les import relatifs par elles mêmes,
    il faut ajouter le root dir dans le python path:
    `sys.path.append(os.path.join(os.getcwd(), '..'))`
    Ou là où il se trouve le root dir par rapport à la notebook

-   df existe. Si on fait df['column'], cela s'appelle une "view".
    Une view est juste une reference filtré vers le df existant.
    Ce n'est surtout pas une copie du df original, juste une ref.

-   df.loc[] permet de selectionner une ou plusieurs cellules dans un df en specifiant des labels de rows/columns ou des
    booleans arrays. Example :

    ```
    mask = df['id_produit'] == i
    df.loc[mask, 'color'] = 'red'
    ```

-   pd.cut() est utile pour prendre la colonne d'un df et de mettre ses valeurs dans des bins discrets.

    ```
    pd.cut(
        df.loc[mask, 'phase1_temps_de_fermeture'],
        bins=[-float('inf')] + cutoffs + [float('inf')],
        labels=colors
    )
    ```
