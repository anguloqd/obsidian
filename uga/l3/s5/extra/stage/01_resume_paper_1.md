# Analyse des séries temporelles de température de surface terrestre

[01_resume_paper_1_paper.pdf](ressources/00_les_papers_1_s2.0_s0034425722003285_main_compressed.pdf)

## Vocabulaire technique fondamental

La température de surface terrestre (LST, Land Surface Temperature) constitue l'indicateur principal étudié dans cette recherche. Cette mesure varie continuellement dans le temps et reflète les changements climatiques, l'utilisation des terres et les perturbations environnementales.

Les changements de couverture terrestre (LCC, Land Cover Change) représentent les modifications observées dans l'occupation du sol au fil du temps. Ces transformations, qu'elles soient d'origine naturelle ou anthropique, influencent directement les mesures de LST.

La décomposition d'une série temporelle consiste à exprimer une statistique comme la somme de trois composantes distinctes : $Y_t = T_t + S_t + e_t$. Chaque terme capture un aspect différent du comportement temporel des données.

La tendance ($T_t$) représente l'évolution graduelle à long terme d'une statistique, généralement modélisée par une fonction linéaire par morceaux. Dans le contexte de la LST, cette composante reflète l'impact du changement climatique, de la gestion des terres ou de la dégradation environnementale.

La saisonnalité ($S_t$) capture les variations périodiques régulières associées aux cycles naturels, typiquement représentée par une fonction harmonique par morceaux. Pour la LST, cette composante correspond aux variations saisonnières liées au cycle solaire annuel.

Le résidu ($e_t$) constitue la différence entre les observations réelles $Y_t$ et la somme des composantes modélisées $T_t + S_t$.

Les changements abrupts correspondent à des variations de grande amplitude qui se produisent sur une période de temps relativement courte. Ces ruptures peuvent affecter la tendance, la saisonnalité, ou les deux simultanément, et résultent généralement de perturbations naturelles ou anthropiques.

## Contexte et enjeux méthodologiques

Les approches antérieures d'analyse des séries temporelles de LST se concentraient principalement sur les données inter-annuelles pour caractériser les tendances et les changements abrupts à l'échelle annuelle. Cette approche présente cependant des limitations importantes car elle ignore la variabilité intra-annuelle de la LST et ne peut pas identifier le moment précis des changements abrupts.

L'utilisation de séries temporelles intra-annuelles, basées sur des données de 8 jours, 16 jours ou mensuelles, permet de capturer simultanément la tendance, la saisonnalité et les changements abrupts. Cette approche temporelle plus fine s'avère donc préférable aux données inter-annuelles pour une analyse complète.

Les méthodes d'analyse des séries intra-annuelles se divisent en deux catégories principales selon leur approche de modélisation des composantes.

### Détection de changements avec formes de composantes inconnues

Cette première catégorie estime itérativement la tendance et la saisonnalité, puis détecte les changements abrupts par segmentation. L'algorithme DBEST illustre parfaitement cette approche en décomposant d'abord les données avant d'identifier les points de rupture.

### Détection de changements avec formes de composantes connues

La seconde catégorie définit a priori la tendance par un modèle linéaire par morceaux et approxime la saisonnalité par un modèle harmonique. Les algorithmes BFAST et BEAST exemplifient cette approche structurée.

## Comparaison des algorithmes de référence

| Algorithme | Fonctionnalité | Avantages | Inconvénients | Applications |
|------------|----------------|-----------|---------------|--------------|
| DBEST | 1) Décomposition tendance-saisonnalité<br>2) Détection des changements abrupts dans la tendance | Caractérise les changements abrupts et non-abrupts dans la composante tendance | 1) Précision réduite en présence de variations haute fréquence<br>2) Nombreux seuils et paramètres pouvant affecter les performances<br>3) Incapable de traiter les données manquantes | Détection de changements de végétation basée sur les séries d'indices de végétation |
| BFAST | 1) Décomposition tendance-saisonnalité<br>2) Détection des changements abrupts dans tendance et saisonnalité | Distingue les changements abrupts de tendance et saisonniers | 1) Sensible à la spécification des paramètres<br>2) Incapable de traiter les données manquantes<br>3) Coûteux en calcul | Détection LCC, incendies, décomposition tendance-saisonnalité |
| BEAST | Même fonctionnalité que BFAST mais avec approche bayésienne | 1) Distingue les changements abrupts de tendance et saisonniers<br>2) Réduit l'incertitude par combinaison de modèles concurrents<br>3) Traite les valeurs manquantes<br>4) Fournit des statistiques diagnostiques riches | 1) Sensible aux paramètres<br>2) Coûteux en calcul | Détection LCC, tempêtes de glace, incendies, reconstruction de séries LST |

## Méthodes d'analyse détaillées

### Outil fondamental : STL

La procédure de décomposition saisonnière-tendance basée sur la régression pondérée localement (STL) constitue l'outil de base utilisé par DBEST et BFAST pour extraire la saisonnalité. Ces algorithmes modifient ensuite la composante tendance produite par STL selon leurs propres critères.

### Algorithme DBEST

DBEST obtient des segments linéaires de la composante tendance via estimation et segmentation. Le processus se décompose en plusieurs étapes méthodologiques.

#### Méthode d'estimation de tendance

L'estimation nécessite trois paramètres : $\theta_1$, $\theta_2$ et $D$. Le paramètre $\theta_1$ capture les différences absolues importantes entre un point $Y_t$ et le point suivant $Y_{t+1}$. Une fois un point $Y_t^*$ présentant une grande différence identifié, $\theta_2$ capture les différences importantes dans la valeur moyenne de $Y$ avant et après le temps $t$.

La différence $\Delta \bar Y_{t,D}$ compare la valeur moyenne de $Y$ sur l'intervalle $[t-D, t]$ (notée $\bar Y_{[t-D, t]}$) avec la valeur moyenne sur l'intervalle $[t, t+D]$ (notée $\bar Y_{[t, t+D]}$). Le paramètre $D$ définit la taille de la fenêtre pour calculer ces moyennes.

Un point $Y_t^*$ devient un "point candidat de changement de niveau" (LSP) s'il vérifie simultanément :
1. $\Delta Y_t > \theta_1$
2. $\Delta \bar Y_{t,D} > \theta_2$

Les LSP candidats sont classés par ordre décroissant de leur valeur $\Delta Y_t$, le premier étant le "LSP le plus important". Pour les LSP suivants, du plus précoce au plus tardif temporellement, l'algorithme vérifie que chaque LSP candidat maintient une distance temporelle d'au moins $D$ par rapport au LSP détecté précédent.

La liste définitive des LSP permet de diviser la série en segments, sur lesquels STL est appliqué séparément pour obtenir les fonctions de tendance et saisonnalité.

#### Méthode de segmentation : détection des points de retournement

L'analyse se concentre sur la fonction de tendance obtenue. Tous les points de la série temporelle sont classifiés comme "pic", "vallée" ou neutre. Un pic au temps $t$ correspond à un point où la fonction croissait de $t-1$ à $t$ puis décroît de $t$ à $t+1$. La définition analogique s'applique aux vallées. Ces points constituent les "points de retournement".

Un processus itératif implique une fonction de critère des points de retournement. Des lignes connectent chaque point de retournement au suivant. Pour chaque segment linéaire ainsi créé, l'algorithme détecte le point présentant la distance perpendiculaire maximale à la ligne, de chaque côté. Ces points deviennent des "candidats points de retournement".

Chaque candidat est évalué par une "fonction de point de retournement" $g_{(i)}$ qui retourne 1 si le point constitue un pic ou une vallée, ou si sa distance perpendiculaire à la ligne dépasse le paramètre $\varepsilon$. Sinon, la fonction retourne 0.

Lorsque la première itération se termine, l'ensemble incluant les points de retournement devient généralement plus large que l'ensemble initial contenant uniquement les pics et vallées. Le processus reprend depuis l'étape 1 jusqu'à ce qu'une itération ne génère aucun nouveau point de retournement.

L'ensemble final des points de retournement comprend le point initial de la série temporelle, tous les LSP, et tous les points satisfaisant le critère de point de retournement.

#### Méthode de segmentation : validation des points de retournement

Les "points de retournement valides" se définissent comme ceux qui réduisent significativement la somme des carrés des résidus d'un ajustement par moindres carrés à la série temporelle de tendance, sans provoquer de sur-ajustement.

Le nombre de points de retournement valides se détermine en minimisant le critère d'information bayésien (BIC). Ce critère sélectionne le modèle optimal parmi un ensemble fini de modèles. L'ajout de points de retournement réduit la somme des carrés des résidus mais augmente le nombre de paramètres du modèle, risquant le sur-ajustement. Le BIC résout ce problème en introduisant un terme de pénalité proportionnel au nombre de paramètres.

Une "fonction de changement local de tendance" $h_{(i)}$ s'applique à tous les points. Pour un point de retournement au temps $t$, cette fonction calcule la différence $T_{t-1} - T_t$. Tous les points de retournement sont ensuite classés par ordre décroissant de la magnitude de leur changement local de tendance.

La régression linéaire sélectionne un sous-ensemble de taille $s$ parmi les $u$ points de retournement totaux, en priorisant ceux présentant les plus grands changements locaux de tendance. Le sous-ensemble minimisant le BIC définit les $s$ points comme "points de retournement valides" ou "points de rupture".

Une régression linéaire par morceaux s'applique à chaque intervalle délimité par les points de rupture. La régression résultante ne passe pas nécessairement par tous les points de rupture, et peut se limiter à $m$ points de rupture parmi les $s$ disponibles.

### Algorithme BFAST

BFAST produit la tendance et la saisonnalité ainsi que le nombre, le moment et les intervalles de confiance des changements abrupts dans les deux composantes.

L'algorithme utilise deux outils mathématiques principaux : le test OLS-MOSUM (Ordinary Least Squares residuals-based MOving SUM) et les moindres carrés pour déterminer le nombre et la position des points de rupture. Les coefficients des composantes sont estimés par régression robuste basée sur la M-estimation.

Le test OLS-MOSUM exigeant des données régulièrement espacées, BFAST ne peut traiter les séries temporelles avec valeurs manquantes.

L'algorithme procède selon les étapes suivantes :

1. Fixation des paramètres, tous ayant un impact important sur le résultat final :
   - Nombre maximum de points de rupture dans la tendance ($m$) et la saisonnalité ($q$) - paramètre le plus influent
   - Intervalle de séparation minimum $\phi$ entre points de rupture adjacents
   - Nombre maximum d'itérations

2. Extraction de la saisonnalité par STL

3. Détection des points de rupture de tendance par OLS-MOSUM

4. Estimation des coefficients de tendance $\alpha_i, \beta_i$ par régression robuste M-estimation, puis ajustement de la tendance précédente

5. Détection des points de rupture saisonniers par OLS-MOSUM

6. Estimation des coefficients de saisonnalité $\gamma_{j,h}, \delta_{j,h}$ par régression robuste M-estimation, puis ajustement de la saisonnalité précédente

7. Répétition des étapes 3 à 6 jusqu'à stabilisation du nombre et de la position des points de rupture

### Algorithme BEAST

BEAST infère simultanément le nombre et les positions des points de rupture ainsi que les coefficients de tendance et saisonnalité en une seule étape. Contrairement à BFAST, BEAST ne nécessite pas la spécification de l'ordre harmonique.

BEAST produit la tendance et saisonnalité, le nombre, moment, probabilité d'occurrence et intervalles de confiance des changements abrupts dans les deux composantes, ainsi que les ordres harmoniques saisonniers de la série temporelle.

Les paramètres d'entrée comprennent :
- Nombre maximum de points de rupture dans la tendance ($m$) et saisonnalité ($q$) - paramètre le plus influent
- Intervalle de séparation minimum $\phi$ entre points de rupture adjacents
- Ordre harmonique maximum ($H$) optionnel
- Nombre d'échantillons pour l'échantillonnage MCMC (Markov Chain Monte Carlo à saut réversible)

BEAST utilise un modèle bayésien pour déterminer les valeurs optimales et probabilités a posteriori des éléments suivants :

Les paramètres de structure du modèle $M$ incluent le nombre effectif et le moment des points de rupture dans la tendance et saisonnalité, ainsi que l'ordre harmonique. Pour le calcul des points de rupture, BEAST les infère par moyenne de modèles bayésiens (BMA).

Les paramètres de coefficients spécifiques aux segments $\varphi$ comprennent les coefficients de tendance $\{\alpha_i, \beta_i\}$ et les coefficients de saisonnalité $\{\gamma_{j,h}, \delta_{j,h}\}$.

## Données d'évaluation

### Données simulées

Une série temporelle LST a été simulée sur 10 années avec une période annuelle de 46 observations, correspondant à une résolution temporelle de 8 jours. La tendance, saisonnalité et résidu ont été simulés séparément, leur somme constituant la "série temporelle de base".

La tendance suit une fonction linéaire par morceaux changeant de pente (de $-0.14K$ à $0.14K$) à chaque décennie. L'ordonnée à l'origine (LST initiale à $t=0$) était fixée à $288K$.

La saisonnalité résulte d'une fonction harmonique d'ordre 1 ou 2. Les amplitudes varient de $20K$ à $40K$ et les phases de $1/9$ à $1/3$ de période.

Le résidu consiste en nombres aléatoires entre $-3K$ et $3K$ avec une moyenne de $0K$.

Les scénarios de données manquantes sont également simulés en supprimant aléatoirement des points avec certaines proportions (0-40%), imitant les discontinuités causées par les nuages, la neige ou l'algorithme de récupération LST.

Six jeux de données ont été créés à partir de la série de base :

- **Jeu 1** : série de base uniquement pour évaluer la décomposition des composantes
- **Jeu 2** : un changement abrupt dans la tendance avec différents moments, magnitudes (5-10K) et pentes après changement
- **Jeu 3** : deux changements abrupts dans la tendance
- **Jeu 4** : un changement saisonnier abrupt par modification des paramètres harmoniques
- **Jeu 5** : deux changements saisonniers abrupts
- **Jeu 6** : un changement abrupt de tendance et un saisonnier simultanés

### Données réelles MODIS

Les algorithmes ont été testés sur données réelles mondiales présentant des perturbations significantes, particulièrement les changements de couverture terrestre (LC) :

- Déforestation : forêt vers savane (SAV)
- Expansion agricole : terrain nu (BAR) vers culture (CRO)
- Abandon agricole : culture vers savane
- Urbanisation : prairie (GRA) vers zones urbaines (UBL)

## Protocole d'évaluation et critères

### Configuration des paramètres

Pour DBEST, les paramètres suivent les recommandations de Jamali et al. (2015) : $\theta_1=0.1$, $\theta_2=0.2$ et $D=2$ années. Les données manquantes sont interpolées.

Les paramètres communs à BFAST et BEAST sont : nombre maximum de points de rupture pour tendance ($m$) et saisonnalité ($q$), et intervalle de séparation minimum ($\phi$). Les valeurs retenues sont $m=q=3$ et $\phi = 0.5$ année.

Paramètres spécifiques :
- BFAST : nombre maximum d'itérations fixé à 5
- BEAST : ordre harmonique saisonnier maximum de 3 et 10 000 échantillons MCMC

### Métriques de performance

L'évaluation porte sur deux critères : précision de détection des changements abrupts et précision de décomposition des composantes. Ces critères sont mesurés différemment pour les données simulées et réelles.

#### Précision de détection des changements abrupts (données simulées)

Pour les jeux sans changements abrupts, l'erreur de commission (nombre de fausses détections divisé par le nombre total de jeux) compare les trois méthodes.

Pour les autres cas, deux indicateurs de performance sont utilisés : le score $F1$ et le $MAE_{\partial t}$.

Un point de rupture détecté dans la demi-période du point réel est considéré comme détection correcte, sinon comme fausse détection.

Le score $F1$ se calcule à partir de la précision utilisateur (UA) et producteur (PA) :

$$F1=2\times\frac{PA\times UA}{PA+UA},\quad PA=\frac{TD}{TN},\quad UA=\frac{TD}{DN}$$

où $PA$ représente les points de rupture corrects détectés sur tous les points réels, et $UA$ les points corrects sur toutes les détections. La valeur maximale de $F1$ est 1.0 (PA et UA parfaits), la minimale 0.0 (PA=0 ou UA=0).

Le second indicateur $MAE_{\partial t}$ correspond à la moyenne des distances temporelles absolues entre points détectés et réels :

$$MAE_{\partial t}=\frac{\sum_{i=1}^n\partial t_i}{n}, \quad \partial t_c=|t_{ref}-\hat t|$$

#### Précision de détection des changements abrupts (données réelles)

Pour les séries LST MODIS, compte tenu du faible volume de données et des perturbations sous-jacentes inconnues, l'évaluation se base sur la comparaison du nombre de détections correctes.

Considérant la complexité des perturbations réelles, un point de rupture détecté dans l'année suivant une perturbation LCC réelle ou dans les six mois d'une petite perturbation est considéré comme détection correcte.

#### Précision de décomposition des composantes (données simulées)

Les valeurs d'erreur quadratique moyenne (RMSE) et de coefficient de corrélation (R) entre chaque composante prédite et simulée mesurent la précision de décomposition. Le RMSE de la tendance prédite est noté $RMSE_{T_t}$ et celui de la saisonnalité $RMSE_{S_t}$.

#### Précision de décomposition des composantes (données réelles)

Les vraies tendance et saisonnalité étant inconnues dans les séries LST MODIS, le RMSE entre la somme des tendance et saisonnalité prédites et les observations $(RMSE_{T_t+S_t})$ mesure la précision d'ajustement globale.

## Résultats comparatifs sur données simulées

### Performance de détection des points de rupture

Les résultats révèlent qu'avec l'augmentation de la complexité des données, BEAST et DBEST présentent un $F1$ plus stable que BFAST. BFAST s'avère inefficace pour détecter les changements abrupts de tendance lorsque des changements saisonniers surviennent simultanément.

En l'absence de changements abrupts dans la tendance, BEAST performe également bien sur les deux composantes. BFAST estime correctement les ruptures saisonnières mais mal celles de tendance, suggérant une faible robustesse aux données complexes. DBEST obtient de mauvais résultats globalement, détectant particulièrement de faux points de rupture dans toutes les données simulées.

Concernant l'indicateur $MAE_{\partial t}$, BEAST présente les meilleures performances dans tous les cas. BFAST obtient des résultats comparables à BEAST sur les jeux sans points de rupture de tendance, et des résultats dégradés mais acceptables avec points de rupture de tendance. DBEST présente également les moins bonnes performances.

### Précision de décomposition

BEAST affiche les meilleures performances avec les plus faibles RMSE ($0.28K$ et $0.27K$) et les meilleurs $R$ pour tendance et saisonnalité respectivement : $0.90$ et $0.99$.

DBEST obtient une décomposition intermédiaire avec des RMSE de $0.64K$ et $1.37K$ et des $R$ de $0.78$ et $0.98$ pour tendance et saisonnalité.

BFAST présente les résultats globalement les moins bons avec des RMSE de $1.34K$ et $1.46K$ et des valeurs $R$ de $0.69$ et $0.97$ respectivement.

Pour les jeux 1, 2 et 3, BFAST surpasse DBEST. Pour les jeux 4, 5 et 6, BFAST exhibe des RMSE plus élevés et des valeurs $R$ plus faibles que DBEST.

Cette réduction de précision suggère que BFAST est inefficace pour les données présentant de fortes variations saisonnières. Les valeurs $R$ des composantes de tendance sont inférieures à celles des composantes saisonnières, principalement car la forte saisonnalité de la LST produit une corrélation artificielle entre composantes saisonnières prédites et réelles.

## Amélioration de BEAST : développement d'iBEAST

### Problèmes identifiés et modifications

Malgré sa précision significativement supérieure, BEAST présente des erreurs de commission non négligeables pour la détection de points de rupture de tendance (valeur moyenne sur données simulées : $18.6\%$). Pour décrire précisément les variations à long terme de LST, l'élimination des faux points de rupture détectés par BEAST s'avère nécessaire.

Les vrais changements abrupts s'accompagnent toujours d'augmentations ou diminutions soudaines de $T_t$ ou de changements significatifs dans la pente de $T_t$. BEAST fournit la probabilité d'occurrence du point de rupture et le résidu $(e_t)$. Une probabilité élevée indique une forte vraisemblance du point de rupture. Les $e_t$ anormaux tendent à survenir lors de vrais changements abrupts.

Quatre caractéristiques décrivent ces propriétés :
- Magnitude du changement des changements abrupts de tendance $(\Delta\text{trend})$
- Changements dans la pente de tendance avant et après le changement abrupt, mesurés par l'angle entre les deux tendances $(\text{angle})$
- Probabilité d'occurrence des points de rupture détectés $(\text{Prob})$
- Proportion de résidus anormaux dans l'intervalle de confiance du changement abrupt $(\text{Pp})$. Un résidu anormal est détecté si le résidu dépasse trois fois le $RMSE_{T_t+S_t}$

Quatre critères jugent les faux points de rupture : $\Delta\text{trend} < T1$, $\text{angle} < T2$, $\text{Prob}<T3$ et $\text{Pp}<T4$. Les seuils sont définis empiriquement en observant les données où de faux points de rupture sont détectés.

La plupart des faux points de rupture présentent $\Delta\text{trend}<1K$, $\text{angle}<0.3°$, $\text{Prob}<0.5$, et $\text{Pp}\approx 0$.

L'optimisation des paramètres révèle qu'un $F1$ plus élevé peut résulter en un $TD$ plus faible. Les paramètres finaux constituent un compromis entre $F1$ et $TD$ tout en évitant des conditions de seuil excessivement strictes : $\Delta\text{trend}\leq1K$, $\text{angle}<1°$, $\text{Prob}<0.5$, et $\text{Pp}\leq 1\%$.

Ces modifications génèrent une amélioration générale du $F1$ de $0.03$ et une réduction de l'erreur de commission de $13.23$ points de pourcentage.

## Application d'iBEAST sur données réelles

### Validation de la correction

Les algorithmes ont été appliqués aux données LST MODIS avec trois types de LCC : déforestation, urbanisation, et gain/perte forestière.

BEAST surpasse BFAST et DBEST. iBEAST réduit très significativement les faux positifs de BEAST, mais manque seulement deux vrais points de rupture détectés par BEAST original. iBEAST présente néanmoins un meilleur $F1$ que BEAST dans toutes les catégories.

BEAST présente le meilleur ratio de points de rupture détectés sur perturbations réelles. DBEST obtient un ratio supérieur à BFAST.

Les trois méthodes exhibent une efficacité de détection médiocre pour les petites perturbations (incendies, canicules, froid, etc.).

Concernant le $RMSE_{T_t+S_t}$, DBEST présente la valeur la plus faible des quatre méthodes par une faible marge. Ceci ne signifie pas que les composantes obtenues par DBEST sont précises, mais résulte du fait que la tendance et saisonnalité décomposées par DBEST tendent à contenir de nombreuses fluctuations détaillées et points de retournement dénués de sens.

## Conclusions

### Hiérarchisation des performances

**BEAST** exhibe la précision de détection la plus élevée pour les changements abrupts dans la tendance $(F1 = 0.83)$ et saisonnalité $(F1 = 0.95)$, et peut caractériser le processus des changements abrupts. De plus, il décompose précisément les données de séries temporelles en tendance et saisonnalité, avec des valeurs RMSE moyennes de $0.28K$ et $0.27K$ respectivement.

Cependant, BEAST manque de sensibilité aux changements subtils avec des erreurs d'omission non négligeables dans les données simulées et environ $50\%$ de précision pour les perturbations de faible magnitude et courte durée.

**BFAST** démontre des performances inférieures à BEAST, avec des $F1$ moyens plus faibles pour les points de rupture ($0.56$ et $0.52$ pour tendance et saisonnalité respectivement) et des RMSE plus élevés pour les composantes ($1.34K$ et $1.46K$ pour les deux composantes respectivement) sur données simulées. Cette méthode apparaît plus affectée par les complexités des données. De plus, BFAST tend à détecter des dynamiques de tendance incorrectes lorsque les données de séries temporelles présentent des lacunes prolongées.

**DBEST** présente la précision la plus faible des trois dans les données LST simulées : le $F1$ moyen était $0.37$ et les RMSE moyens de tendance et saisonnalité étaient $0.64K$ et $1.37K$ respectivement. La trajectoire de tendance estimée par DBEST contient une quantité d'informations de changement non essentielles, et ne peut détecter les changements abrupts saisonniers.

**iBEAST** améliore significativement la précision utilisateur de BEAST de $13.9\%$ dans les données simulées, résultant en une augmentation du $F1$ de $0.04$, et élimine 15 faux points de rupture (sur 53 détections totales) dans les séries LST MODIS.

La version améliorée de BEAST constitue la meilleure des quatre pour détecter les changements dans les séries temporelles LST. De plus, l'ordre harmonique saisonnier optimal est déterminé dans iBEAST.