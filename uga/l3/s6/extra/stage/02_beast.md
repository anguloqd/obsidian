## 02 // beast

[02_paper_de_beast.pdf](02_paper_de_beast.pdf)

## BEAST : Algorithme bayésien de détection de changements dans les séries temporelles

### Introduction à BEAST

BEAST (Bayesian Estimator of Abrupt change, Seasonal change, and Trend) représente une approche révolutionnaire pour l'analyse des séries temporelles satellitaires. Contrairement aux méthodes traditionnelles qui cherchent un unique "meilleur" modèle, BEAST embrasse l'incertitude inhérente à la modélisation en combinant de nombreux modèles concurrents.

L'algorithme traite une série temporelle comme la superposition de trois composantes principales : la saisonnalité (variations périodiques), la tendance (évolution à long terme), et les changements abrupts (perturbations, régimes shifts). Cette décomposition permet de révéler des dynamiques écologiques complexes souvent masquées par les approches conventionnelles.

### Fondements conceptuels

#### Le problème des méthodes traditionnelles

Les approches classiques d'analyse des séries temporelles souffrent de plusieurs limitations fondamentales. Elles privilégient la sélection d'un modèle unique basé sur des critères d'optimisation comme l'AIC ou le BIC. Cette stratégie ignore l'utilité des modèles alternatifs et néglige l'incertitude liée au choix du modèle.

Prenons l'exemple d'une série temporelle de végétation : un modèle linéaire simple pourrait révéler une tendance de verdissement global, tandis qu'un modèle avec points de rupture pourrait montrer des périodes distinctes de verdissement puis de brunissement. Les deux modèles peuvent s'ajuster correctement aux données, mais conduisent à des interprétations écologiques contradictoires.

#### L'approche bayésienne

BEAST adopte une philosophie différente : plutôt que de chercher le "vrai" modèle, il reconnaît que tous les modèles sont incorrects mais potentiellement utiles. L'inférence bayésienne permet de quantifier cette utilité en assignant une probabilité à chaque modèle candidat.

Le théorème de Bayes fournit le cadre mathématique :

$$
P(\text{modèle}|\text{données}) \propto P(\text{données}|\text{modèle}) \times P(\text{modèle})
$$

Cette formulation traite les paramètres et les structures de modèles comme des variables aléatoires, permettant une caractérisation complète de l'incertitude.

### Formulation mathématique de BEAST

#### Modèle de décomposition

BEAST modélise une série temporelle $\{t_i, y_i\}_{i=1}^n$ selon la décomposition additive :

$$
y_i = S(t_i; \Theta_s) + T(t_i; \Theta_T) + \varepsilon_i
$$

où :

- $S(t_i; \Theta_s)$ représente le signal saisonnier
- $T(t_i; \Theta_T)$ représente la tendance
- $\varepsilon_i$ est le bruit gaussien de variance $\sigma^2$

Les paramètres $\Theta_s$ et $\Theta_T$ encodent implicitement les changements abrupts sous forme de points de rupture.

#### Modélisation de la saisonnalité

Le signal saisonnier est modélisé comme une fonction harmonique par morceaux. Avec $p$ points de rupture aux temps $\xi_k$ ($k = 1, …, p$), la série est divisée en $(p+1)$ segments. Pour chaque segment $[\xi_k, \xi_{k+1}]$, la saisonnalité prend la forme :

$$
S(t) = \sum_{l=1}^{L_k} \left[ a_{k,l} \sin\left(\frac{2\pi lt}{P}\right) + b_{k,l} \cos\left(\frac{2\pi lt}{P}\right) \right]
$$

où $P$ est la période (typiquement une année), $L_k$ est l'ordre harmonique du segment $k$, et $\{a_{k,l}, b_{k,l}\}$ sont les coefficients harmoniques.

Cette formulation permet à la complexité saisonnière de varier dans le temps : un écosystème peut présenter une phénologie simple en conditions stables, puis développer des patterns plus complexes suite à des perturbations.

#### Modélisation de la tendance

La tendance est représentée par une fonction linéaire par morceaux avec $m$ points de rupture aux temps $\tau_j$ ($j = 1, …, m$). Sur chaque segment $[\tau_j, \tau_{j+1}]$, la tendance est :

$$
T(t) = a_j + b_j \cdot t
$$

Les coefficients $a_j$ et $b_j$ déterminent l'ordonnée à l'origine et la pente de chaque segment. Cette représentation capture les changements de régime : un écosystème peut passer d'une phase de croissance rapide à une phase de déclin, chaque transition étant marquée par un point de rupture.

#### Reformulation matricielle

L'ensemble peut être reformulé sous forme matricielle standard :

$$
y = X_M \beta_M + \varepsilon
$$

où :

- $X_M$ est la matrice de design dépendant de la structure $M$
- $\beta_M$ contient tous les coefficients du modèle
- $M$ encode la structure : nombre et position des points de rupture, ordres harmoniques

Cette formulation révèle que BEAST est essentiellement un modèle linéaire généralisé bayésien avec sélection de structure.

### Inférence bayésienne

#### Spécification des distributions a priori

BEAST adopte des distributions a priori peu informatives pour refléter l'ignorance initiale sur les paramètres. Les coefficients $\beta_M$ suivent une distribution normale-gamma inverse, tandis que la structure $M$ (nombres et positions des points de rupture) suit des distributions uniformes discrètes.

Cette approche évite d'imposer des contraintes trop restrictives tout en maintenant la régularisation nécessaire pour éviter le surajustement.

#### Algorithme MCMC hybride

L'inférence s'effectue via un algorithme MCMC sophistiqué combinant :

1. **Échantillonnage de Gibbs** pour les paramètres à dimension fixe
2. **Reverse-Jump MCMC** pour les changements de structure

L'algorithme alterne entre trois étapes :

1. Échantillonnage de la structure $M$ (nombre et position des points de rupture)
2. Échantillonnage des coefficients $\beta_M$ et de la variance $\sigma^2$
3. Échantillonnage du paramètre de dispersion $v$

Cette approche permet d'explorer efficacement un espace de modèles de dimension variable, chose impossible avec les méthodes conventionnelles.

#### Moyennage bayésien de modèles

Plutôt que de sélectionner un modèle unique, BEAST combine tous les modèles échantillonnés via moyennage bayésien. L'estimation finale est :

$$
\hat{y}(t) = \frac{1}{N} \sum_{i=1}^N X_{M^{(i)}}(t) \beta_{M^{(i)}}
$$

Cette combinaison permet d'approximer des signaux non-linéaires complexes tout en préservant l'information d'incertitude.

#### Hyperparamètres et robustesse

BEAST utilise une hiérarchie de distributions avec hyperparamètres fixés empiriquement :

- Paramètres de régularisation : $a = b = 0.01$, $c = d = 0.02$
- Séparation minimale entre points de rupture : $\bar{h}_{tcp} = \bar{h}_{scp} = 1$ année
- Nombre maximal de points de rupture : $\bar{M}_{tcp} = \bar{M}_{scp} = \max(n/P, 30)$
- Ordres harmoniques : $\bar{L}_{min} = 0$, $\bar{L}_{max} = 10$

Ces choix reflètent des compromis pratiques entre flexibilité du modèle et stabilité numérique. La robustesse de BEAST aux variations de ces hyperparamètres a été vérifiée empiriquement.

### Inférence des dynamiques écologiques

#### Détection des points de rupture

BEAST quantifie la probabilité d'occurrence d'un point de rupture à tout instant :

$$
P(\text{point de rupture à } t_s | \text{données}) = \frac{\text{nombre d'échantillons contenant } t_s}{N}
$$

Cette approche probabiliste dépasse les méthodes binaires (rupture/pas rupture) en fournissant des mesures de confiance graduées.

#### Analyse des tendances non-linéaires

La combinaison de modèles linéaires par morceaux génère des tendances non-linéaires lisses. BEAST peut également calculer la probabilité d'avoir une tendance positive (verdissement) à tout moment :

$$
P(\text{verdissement à } t | \text{données}) = P\left(\frac{d\hat{y}}{dt}(t) > 0\right)
$$

Cette information est cruciale pour distinguer les changements significatifs du bruit.

#### Évolution de la complexité saisonnière

BEAST estime l'ordre harmonique optimal pour chaque période :

$$
\bar{L}(t) = \frac{1}{N} \sum_{i=1}^N L_k^{(i)} \text{ sujet à } t \in [\xi_k^{(i)}, \xi_{k+1}^{(i)}]
$$

Cette capacité d'adaptation révèle les changements phénologiques : un écosystème perturbé peut développer des patterns saisonniers plus complexes durant sa phase de récupération.

#### Traitement de l'incertitude structurelle

BEAST caractérise explicitement plusieurs sources d'incertitude :

- **Incertitude paramétrique** : distribution a posteriori des coefficients $\beta_M$
- **Incertitude structurelle** : distribution sur le nombre et la position des points de rupture
- **Incertitude prédictive** : propagation des incertitudes précédentes vers les prédictions

Cette approche globale contraste avec les méthodes fréquentistes qui ignorent souvent l'incertitude structurelle, pourtant dominante dans l'analyse de séries temporelles écologiques.

#### Approximation universelle

La théorie mathématique garantit que BEAST peut approximer toute fonction continue par moyennage de ses modèles linéaires par morceaux. Cette propriété d'approximateur universel explique sa capacité à capturer des dynamiques écologiques complexes sans spécification a priori de leur forme fonctionnelle.

### Évaluation sur données simulées

#### Génération de références contrôlées

Pour valider rigoureusement BEAST, les chercheurs ont généré 110 000 séries temporelles synthétiques avec des paramètres connus. Chaque série combine :

- Un signal de tendance avec 0 à 10 points de rupture
- Une composante saisonnière périodique
- Du bruit gaussien d'amplitude variable (5% à 20%)
- Une longueur temporelle aléatoire entre 200 et 500 observations

Cette approche contrôlée permet d'évaluer précisément la capacité de récupération des vraies dynamiques, impossible avec des données réelles où la vérité terrain reste inconnue.

#### Performance de reconstruction

BEAST démontre une robustesse remarquable face au bruit. La corrélation entre les tendances estimées et les tendances vraies atteint 0,931 en moyenne, même avec des niveaux de bruit élevés (rapport signal/bruit de 5,0 maintient une corrélation de 0,923).

La détection des points de rupture montre une sensibilité attendue à l'intensité relative des signaux. Lorsque la tendance ne représente que 5% de l'amplitude saisonnière, la corrélation chute à 0,67. Cette limitation reflète une réalité physique : aucun algorithme ne peut détecter des changements noyés dans des variations plus importantes.

### Applications à données satellitaires denses

#### Analyse Landsat haute résolution temporelle

L'étude de 495 images Landsat TM5/ETM+ sur le sud des États-Unis révèle les subtilités de l'interprétation algorithmique. Trois analystes experts ont identifié manuellement 368 points de rupture comme référence, distinguant 190 événements de perturbation (déclin NDVI) et 178 événements de récupération (hausse NDVI).

BEAST détecte respectivement 217 et 197 événements, générant des erreurs d'omission de 17,7% et de commission de 26,8%. Cette apparente divergence cache une réalité plus nuancée : l'algorithme capture des changements subtils invisibles à l'œil humain mais écologiquement significatifs.

#### Granularité temporelle supérieure

Un exemple illustratif montre BEAST identifiant quatre points de rupture de tendance et deux saisonniers sur une parcelle forestière, là où les experts n'ont détecté qu'un seul événement de coupe. L'algorithme révèle les stades successifs de récupération post-perturbation, démontrant sa capacité à décomposer des processus écologiques complexes en phases distinctes.

### Validation par événements connus

#### Tempête de verglas et incendie en Ohio

La forêt d'État de Shawnee offre un laboratoire naturel avec deux perturbations majeures documentées : une tempête de verglas en février 2003 et un incendie en avril 2009. BEAST appliqué aux données MODIS EVI révèle des patterns spatio-temporels cohérents avec l'historique des perturbations.

L'algorithme détecte précisément les dates et localisations des deux événements. Plus subtilement, il distingue leurs impacts différentiels : la tempête de verglas ne génère aucun point de rupture saisonnière, reflétant des dommages limités (bris de branches), tandis que l'incendie destructeur modifie localement la phénologie.

#### Corrélation avec indices de sévérité

La probabilité de point de rupture estimée par BEAST corrèle significativement (r = 0,66) avec l'indice dNBR dérivé de Landsat, validant indépendamment la capacité de l'algorithme à quantifier l'intensité des perturbations sur un continuum plutôt qu'en termes binaires.

### Capacités prédictives et interpolation

#### Comblement de lacunes temporelles

BEAST excelle dans la prédiction de valeurs manquantes grâce à sa modélisation globale de la série temporelle. La validation croisée "leave-one-out" sur des données MODIS atteint un R² de 0,91, démontrant une fidélité remarquable aux observations réelles.

Cette propriété découle de la décomposition additive : une fois les composantes de tendance et saisonnière estimées, l'algorithme peut extrapoler ou interpoler avec confiance dans les gaps de données, une capacité particulièrement précieuse pour les séries satellitaires affectées par la couverture nuageuse.

#### Ajustement global des séries

Contrairement aux approches heuristiques qui analysent segments par segments, BEAST ajuste simultanément l'ensemble de la série temporelle. Cette approche globale produit des corrélations moyennes de 0,943 entre observations et prédictions sur l'ensemble des pixels analysés, soulignant la cohérence du modèle statistique sous-jacent.

### Détection probabiliste des changements

#### Au-delà des seuils binaires

La plupart des algorithmes existants fonctionnent par détection de seuils : un changement est déclaré si certains critères dépassent des valeurs prédéfinies. BEAST rompt avec cette logique en quantifiant la probabilité d'occurrence de changements.

Cette approche probabiliste capture les changements subtils souvent manqués par les détecteurs rigides. Un pixel peut présenter une probabilité de 30% d'avoir subi un changement, information nuancée reflétant l'incertitude inhérente aux données bruitées.

#### Hiérarchisation des événements

Les probabilités permettent une hiérarchisation naturelle des changements détectés. Les gestionnaires peuvent ainsi prioriser leur attention sur les zones à haute probabilité tout en gardant conscience des changements potentiels moins certains, offrant une gestion adaptative des ressources d'investigation.

### Limites et considérations pratiques

#### Attribution causale

BEAST détecte les changements mais n'identifie pas leurs causes. Un déclin NDVI peut résulter d'un incendie, d'une sécheresse, d'une coupe forestière ou d'une infestation d'insectes. L'algorithme quantifie le "quand" et le "combien" mais pas le "pourquoi", nécessitant l'intégration d'informations auxiliaires pour l'attribution causale.

#### Échelle spatiale et hétérogénéité

L'interprétation des probabilités dépend de l'échelle d'analyse. Une probabilité de changement de 5% peut refléter soit une perturbation légère sur l'ensemble du pixel, soit une perturbation sévère sur une fraction minime de celui-ci. Cette ambiguïté se résout par l'utilisation de données à résolution spatiale plus fine.

#### Invariance d'échelle des tendances

Contrairement à la détection de points de rupture, l'estimation des tendances présente une propriété d'invariance d'échelle. Agréger d'abord les pixels puis appliquer BEAST produit la même tendance globale qu'appliquer BEAST individuellement puis agréger les résultats, facilitant l'analyse multi-échelle.

### Perspectives computationnelles

#### Coût algorithmique

L'inférence bayésienne par échantillonnage Monte Carlo exige davantage de calculs que les approches déterministes. Cette complexité computationnelle recommande l'usage de BEAST pour des analyses globales à résolution grossière ou locales à haute résolution, plutôt que pour des applications globales haute résolution nécessitant un traitement temps réel.

#### Parallélisation et optimisation

La nature indépendante de l'analyse pixel par pixel se prête naturellement à la parallélisation. Les architectures de calcul moderne permettent de distribuer efficacement les calculs, rendant BEAST applicable à des jeux de données de taille substantielle malgré sa complexité intrinsèque.

Cette flexibilité computationnelle, combinée à la richesse des informations extraites, positionne BEAST comme un outil précieux pour l'analyse approfondie des dynamiques écosystémiques à partir des archives satellitaires croissantes.
