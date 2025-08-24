# 10 // la demande du marché

## De la demande individuelle à la demande de marché

- La demande agrégée est égale à la somme des demandes individuelles
- Puisque les revenus sont différents parmi les consommateurs, on analyse le marché comme s'il s'agissait d'un seul consommateur avec le revenu agrégé de tous les consommateurs

### Construction mathématique

Si $x_i(p_1, p_2, m_i)$ est la demande du consommateur $i$ pour le bien 1, la demande de marché est :
$$X(p_1, p_2, m_1, m_2, ..., m_n) = \sum_{i=1}^n x_i(p_1, p_2, m_i)$$

## La marge extensive et la marge intensive

- **Marge intensive** : variation de la quantité achetée par les consommateurs existants
- **Marge extensive** : entrée ou sortie de nouveaux consommateurs du marché

Imaginons un histogramme où chaque barre représente un consommateur et sa hauteur la quantité achetée :
- La marge intensive modifie la hauteur des barres
- La marge extensive modifie le nombre de barres

## L'élasticité

La mesure standard de l'élasticité d'une demande linéaire ($\Delta q/\Delta p$) change selon les unités de mesure de $q$. On utilise donc l'élasticité-prix relative.

>[!definition] Élasticité-prix
>$$\varepsilon = \frac{\Delta q/q}{\Delta p/p} = \frac{\partial q}{\partial p} \cdot \frac{p}{q}$$
>
>On considère généralement la valeur absolue de l'élasticité.

### Classification des demandes selon l'élasticité

- Demande **élastique** : $|\varepsilon| > 1$ (variation proportionnelle de la quantité supérieure à celle du prix)
- Demande **inélastique** : $|\varepsilon| < 1$ (variation proportionnelle de la quantité inférieure à celle du prix)
- Demande à **élasticité unitaire** : $|\varepsilon| = 1$ (variations proportionnelles égales)

## L'élasticité et la recette

**Recette** : $R = pq$

La variation de la recette en fonction du prix est :
$$\frac{dR}{dp} = q(1 + \varepsilon)$$

où $\varepsilon$ est négatif. On peut réécrire avec $\varepsilon$ en valeur absolue :
$$\frac{dR}{dp} = q(1 - |\varepsilon|)$$

>[!important] Relation entre recette et élasticité
>- Si $|\varepsilon| < 1$ (demande inélastique) : $\frac{dR}{dp} > 0$ (une hausse de prix augmente la recette)
>- Si $|\varepsilon| > 1$ (demande élastique) : $\frac{dR}{dp} < 0$ (une hausse de prix diminue la recette)
>- Si $|\varepsilon| = 1$ (élasticité unitaire) : $\frac{dR}{dp} = 0$ (la recette est maximale)

## Les demandes à élasticité constante

Une fonction de demande à élasticité constante prend la forme :
$$q = cp^{\varepsilon}$$

où $c$ est une constante positive et $\varepsilon$ est l'élasticité-prix relative (négative)

### Propriétés

- Si $\varepsilon = -1$ : hyperbole équilatère (la recette est constante quelle que soit la quantité)
- Si $\varepsilon < -1$ : demande élastique
- Si $\varepsilon > -1$ : demande inélastique

## L'élasticité et la recette marginale

**Recette marginale** : Variation de la recette par rapport à la quantité vendue :
$$\frac{dR}{dq} = p(1 + \frac{1}{\varepsilon})$$

Il faut exprimer $p$ comme une fonction de $q$ : $p(q)$.

Pour une demande linéaire $p = a - bq$ :
- La recette est $R = pq = (a - bq)q = aq - bq^2$
- La recette marginale est $\frac{dR}{dq} = a - 2bq$
- L'élasticité varie le long de la courbe