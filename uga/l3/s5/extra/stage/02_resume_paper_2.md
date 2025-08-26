## Détection de points de rupture dans les séries temporelles

> [!note]
> Lien vers l'article original : [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5464762/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5464762/)

### Introduction

La détection de points de rupture (Change Point Detection, CPD) constitue un problème fondamental en analyse de séries temporelles : identifier les moments où une propriété statistique de la série change brutalement. Cette problématique se retrouve sous diverses appellations selon le contexte - segmentation, détection de contours, détection d'événements ou détection d'anomalies - mais l'objectif reste identique : localiser les transitions entre différents régimes dans les données temporelles.

Contrairement à l'estimation de points de rupture qui cherche à modéliser et interpréter des changements déjà connus, la détection se concentre sur l'identification même de l'occurrence d'un changement. Cette distinction est cruciale car elle détermine l'approche méthodologique adoptée.

Les applications de la CPD couvrent un spectre remarquablement large. En médecine, elle permet la surveillance continue de l'état des patients. En climatologie, elle aide à identifier les changements climatiques dans les données météorologiques. Les systèmes de reconnaissance vocale l'utilisent pour segmenter la parole, tandis qu'en analyse d'images, elle facilite la détection de contours. L'analyse des activités humaines constitue également un domaine d'application privilégié, où la CPD permet de distinguer différents types de mouvements ou comportements.

### Fondements mathématiques

#### Séries temporelles et flux de données

Une série temporelle se définit comme une séquence de vecteurs de dimension $d$ contenant des observations à des instants successifs. Formellement, considérons un flux de données infini :

$$S=\{\mathbf{x}_1, \cdots, \mathbf{x}_i, \cdots\}$$

où chaque $\mathbf{x}_i$ représente une observation vectorielle au temps $i$.

#### Stationnarité et variables indépendantes identiquement distribuées

La stationnarité constitue une propriété fondamentale des processus stochastiques. Une série temporelle stationnaire présente des caractéristiques statistiques invariantes dans le temps : l'espérance, la variance (qui doit être finie) et l'auto-covariance ne dépendent pas de l'instant d'observation.

L'auto-covariance mesure la dépendance d'une variable aléatoire avec elle-même à différents instants :

$$\gamma(s,t)=\text{cov}(\mathbf{X}_s, \mathbf{X}_t)=E((\mathbf{X}_s-\mu_s)(\mathbf{X}_t-\mu_t)]$$

Dans le cas stationnaire, cette auto-covariance ne dépend que de l'écart temporel $|t_1 - t_2|$ et non des instants absolus.

Les variables indépendantes identiquement distribuées (i.i.d.) représentent un cas particulier de série stationnaire où les observations sont mutuellement indépendantes et proviennent de la même distribution de probabilité.

#### Matrice des fenêtres glissantes

Pour analyser les changements locaux, on extrait des sous-séquences de la série temporelle. Soit $T$ une sous-séquence de taille $m$ extraite du flux $S$. La matrice WM (Window Matrix) organise toutes les sous-séquences possibles de longueur $k$ en appliquant une fenêtre glissante sur $T$.

Chaque ligne $i$ de cette matrice contient la sous-séquence $W_{i,k}=\{\mathbf{X}_i, \mathbf{X}_{i+1}, \cdots, \mathbf{X}_{i+k-1}\}$ :

$$\begin{bmatrix}
W_{i,k} \\
W_{i+1,k} \\
\vdots \\
W_{i+n-1,k}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{X}_{i} & \mathbf{X}_{i+1} & \cdots & \mathbf{X}_{i+k-1} \\
\mathbf{X}_{i+1} & \mathbf{X}_{i+2} & \cdots & \mathbf{X}_{i+k} \\
\vdots & \vdots & \ddots & \cdots \\
\mathbf{X}_{i+n-1} & \mathbf{X}_{i+n} & \cdots & \mathbf{X}_{i+n+k-2}
\end{bmatrix}$$

Cette matrice de dimensions $(m-k+1) \times k$ présente la structure particulière d'une matrice de Hankel, où les éléments sont constants le long des anti-diagonales.

Un intervalle $\chi_{t,n}$ correspond à l'extraction de $n$ lignes consécutives de la matrice WM à partir du temps $t$, permettant d'analyser l'évolution locale des données.

#### Formalisation des points de rupture

Un point de rupture représente une transition entre différents états du processus générateur de la série temporelle. Cette notion se formalise naturellement comme un test d'hypothèses :

- Hypothèse nulle $H_0$ : "Aucun changement n'a lieu"
- Hypothèse alternative $H_A$ : "Un changement a lieu"

Mathématiquement :

$$H_0: \mathbb{P}_{W_{i,(\cdot)}} = \cdots = \mathbb{P}_{W_{j,(\cdot)}} = \cdots = \mathbb{P}_{W_{k,(\cdot)}}$$

$$\text{contre}$$

$$H_A: \exists j^*, \quad \mathbb{P}_{W_{i,(\cdot)}} = \cdots = \mathbb{P}_{W_{j^*,(\cdot)}} \neq \mathbb{P}_{W_{j*+1,(\cdot)}} = \cdots = \mathbb{P}_{W_{k,(\cdot)}}$$

où $\mathbb{P}_{W_{i},(\cdot)}$ désigne la fonction de densité de probabilité de la fenêtre commençant au temps $i$, et $j^*$ correspond au point de rupture.

### Typologie des algorithmes

#### Classification temporelle : en ligne versus hors ligne

Les algorithmes de détection se distinguent fondamentalement par leur rapport au temps de traitement.

Les algorithmes hors ligne analysent l'intégralité du jeu de données de manière rétrospective. Leur objectif consiste à identifier tous les points de rupture d'une séquence en mode batch, sans contrainte temporelle. Cette approche permet une analyse exhaustive mais ne convient pas aux applications temps réel.

Les algorithmes en ligne opèrent simultanément avec le processus qu'ils surveillent, traitant chaque nouvelle observation dès sa disponibilité. L'objectif devient alors la détection la plus rapide possible d'un point de rupture après son occurrence, idéalement avant l'arrivée de la donnée suivante. En pratique, aucun algorithme ne fonctionne en temps réel parfait, car il doit examiner les nouvelles données avant de déterminer si un changement s'est produit.

La notion d'algorithme $\varepsilon$-temps réel caractérise les méthodes en ligne nécessitant au moins $\varepsilon$ échantillons dans le nouveau lot de données pour détecter un point de rupture. Un algorithme parfaitement temps réel correspondrait à $\varepsilon = 1$.

#### Complexité computationnelle et passage à l'échelle

Les méthodes de détection doivent être conçues de manière computationnellement efficace pour traiter des volumes massifs de données. La comparaison entre approches paramétriques et non-paramétriques offre un cadre d'analyse pertinent.

Les approches paramétriques spécifient une forme fonctionnelle particulière que le modèle doit apprendre, puis estiment les paramètres inconnus à partir de données d'entraînement étiquetées. Une fois le modèle entraîné, les exemples d'apprentissage peuvent être supprimés.

Les méthodes non-paramétriques ne posent aucune hypothèse sur la forme de la fonction sous-jacente. Le prix à payer consiste en la nécessité de conserver toutes les données disponibles lors de l'inférence. Paradoxalement, les approches non-paramétriques démontrent une efficacité supérieure sur les jeux de données massifs, particulièrement lorsque la dimensionnalité augmente.

#### Contraintes algorithmiques

Les approches de CPD se différencient également par les exigences imposées aux données d'entrée et aux algorithmes. Ces contraintes déterminent la sélection d'une technique appropriée pour une séquence de données spécifique.

Les contraintes liées à la nature des données temporelles peuvent provenir de la stationnarité, du caractère i.i.d., de la dimensionnalité ou de la continuité des données. Pour les méthodes paramétriques, la sensibilité au choix des valeurs initiales des paramètres constitue également un enjeu critique.

### Évaluation des performances

Les algorithmes de CPD génèrent différents types de sorties selon leur conception :

- Décisions binaires (point de rupture oui/non), transformant l'algorithme en classificateur binaire
- Identification de points de rupture avec différents niveaux de précision (le changement se produit dans un intervalle de $x$ unités de temps)
- Temps du prochain point de rupture ou de tous les points de rupture de la série

#### Métriques pour la classification binaire

Pour les deux premiers types d'algorithmes, l'établissement d'une matrice de confusion devient nécessaire :

| | Classifie comme point de rupture | Classifie comme non-point de rupture |
|---|---|---|
| Vrai point de rupture | $TP$ | $FN$ |
| Vrai non-point de rupture | $FP$ | $TN$ |

##### Précision et précision équilibrée

La précision traditionnelle se calcule comme le rapport des points correctement classifiés sur le total :

$$\text{Précision}=\frac{TP+TN}{TP+FP+FN+TN}$$

Cette mesure s'avère inefficace pour les jeux de données déséquilibrés, typiques de la détection de points de rupture. La précision équilibrée résout ce problème :

$$\text{Précision équilibrée}=\frac{TPR+TNR}{2}$$

##### Sensibilité et spécificité

La sensibilité (ou taux de vrais positifs) mesure la proportion de points de rupture correctement identifiés :

$$\text{Sensibilité}=\text{Rappel}=\text{Taux VP} =\frac{TP}{TP+FN}$$

##### Moyenne géométrique

La détection de points de rupture produit typiquement un problème d'apprentissage avec distribution déséquilibrée, car le ratio de changements par rapport au total des données reste faible. La moyenne géométrique (G-mean) des taux de vrais positifs et négatifs offre une mesure robuste :

$$\text{G-mean}=\sqrt{\text{Sensibilité}\times\text{Spécificité}}=\sqrt{\frac{TP}{TP+FN} \times \frac{TN}{TN+FP}}$$

##### Précision et mesure F

La précision se calcule comme le rapport des vrais positifs sur le total des points classifiés comme points de rupture :

$$\text{Précision}=\frac{TP}{TP+FP}$$

La mesure F combine précision et rappel :

$$F_\beta=\frac{(1+\beta)^2\times\text{Rappel}\times\text{Précision}}{(\beta^2\times\text{Rappel})+\text{Précision}}$$

Le paramètre $\beta$ indique l'importance relative accordée au rappel par rapport à la précision. La mesure $F_1$ ($\beta = 1$) pondère équitablement les deux métriques.

##### Courbe ROC et aire sous la courbe

L'analyse ROC facilite l'examen explicite du compromis entre taux de vrais positifs et taux de faux positifs. Cette représentation bidimensionnelle place le taux de faux positifs sur l'axe des abscisses et le taux de vrais positifs sur l'axe des ordonnées.

Un algorithme supérieur produit un point plus proche des coordonnées $(0,1)$ (coin supérieur gauche) que ses concurrents. L'aire sous la courbe ROC (AUC) évalue la performance globale : plus cette valeur approche 1, plus l'algorithme est performant.

Le taux d'erreur égale (EER) correspond au point où les taux de faux positifs et faux négatifs s'égalisent. Un algorithme robuste maintient cette valeur faible.

##### Courbe précision-rappel

La courbe précision-rappel (PRC) représente la précision en fonction du rappel. Contrairement à l'espace ROC où l'optimum se situe en haut à gauche, l'optimum dans l'espace PR se trouve en haut à droite. Cette analyse s'avère particulièrement pertinente lorsque la distribution des classes est fortement déséquilibrée.

#### Métriques pour la localisation temporelle

Lorsque la différence temporelle entre le point de rupture détecté et le point réel constitue la mesure de performance, les métriques précédentes deviennent inappropriées. Plusieurs mesures spécialisées existent, où $n$ représente le nombre de points de rupture réels et prédits.

##### Erreur absolue moyenne

$$MAE=\frac{1}{n}\sum_{i=1}^n|\text{Prédit}(CP_i)-\text{Réel}(CP_i)|$$

##### Erreur quadratique moyenne

Cette métrique pénalise davantage les points de rupture aberrants :

$$MSE=\frac{1}{n}\sum_{i=1}^n\Big(\text{Prédit}(CP_i)-\text{Réel}(CP_i)\Big)^2$$

##### Différence signée moyenne

Cet indicateur révèle la direction générale des erreurs de prédiction :

$$MSD=\frac{1}{n}\sum_{i=1}^n(\text{Prédit}(CP_i)-\text{Réel}(CP_i))$$

##### Erreur quadratique moyenne normalisée

La normalisation facilite la comparaison entre jeux de données ou modèles d'échelles différentes :

$$NRMSE=\frac{RMSE}{ACP_{max}-ACP_{min}}\text{ ou }NRMSE=\frac{RMSE}{\overline{ACP}}$$

où $ACP$ désigne les points de rupture réels.

### Méthodes supervisées

Les algorithmes d'apprentissage supervisé apprennent une correspondance entre données d'entrée et attribut cible, généralement une étiquette de classe. Pour la détection de points de rupture, ces approches peuvent être entraînées comme classificateurs binaires ou multi-classes.

#### Classification multi-classes

Cette approche détecte chaque classe (état) séparément, fournissant suffisamment d'informations pour identifier la nature et l'ampleur du changement détecté. Les techniques incluent les arbres de décision, Naive Bayes, réseaux bayésiens, machines à vecteurs de support, plus proches voisins, modèles de Markov cachés, champs aléatoires conditionnels et modèles de mélange gaussien.

#### Classification binaire

Cette méthode traite la détection comme un problème à deux classes : les séquences de transition entre états (points de rupture) constituent une classe, tandis que les séquences intra-états forment la seconde classe. Bien que seulement deux classes nécessitent un apprentissage, ce problème devient complexe si le nombre de types de transitions possibles est important.

#### Classificateur virtuel

Cette approche innovante prend deux fenêtres adjacentes temporellement où un changement est suspecté. Les points de la première fenêtre reçoivent l'étiquette (-1), ceux de la seconde (+1). Un classificateur multi-classes apprend à distinguer les nouveaux points selon leur appartenance à l'une ou l'autre fenêtre.

Si un changement réel s'est produit entre les fenêtres, le classificateur devrait atteindre une précision significativement supérieure au hasard. Un test statistique (test z) vérifie si la précision observée $p$ diffère significativement de la précision aléatoire $0.5$.

### Méthodes non supervisées

Contrairement aux méthodes supervisées, les approches non supervisées découvrent des motifs sans accès à des données étiquetées. Elles regroupent et étiquettent les données en explorant les caractéristiques des séries temporelles, segmentant naturellement la série selon les différents états identifiés.

#### Méthodes de rapport de vraisemblance

La formulation statistique typique de la détection de points de rupture analyse les distributions de probabilité des données avant et après un point de rupture candidat. Une différence significative entre ces deux probabilités indique un point de rupture.

##### CUSUM (Somme cumulative)

CUSUM accumule les déviations relatives à une cible spécifiée pour les mesures entrantes et signale un point de rupture lorsque la somme cumulative dépasse un seuil défini.

##### Change Finder

Cette méthode calcule les densités de probabilité de chaque point de données, puis dérive un "score" pour chaque point. Un modèle auto-régressif appliqué aux données score-contre-temps permet d'obtenir de nouvelles densités. La fonction de score, réappliquée avec ces nouvelles densités, produit un "score final". Un score final élevé indique généralement une probabilité élevée d'être un point de rupture.

##### Méthodes de ratio de densité direct

Plutôt que de calculer individuellement les densités, ces méthodes estiment directement le ratio de densités entre intervalles consécutifs $\chi$ et $\chi'$ via un modèle à noyau gaussien. Une mesure de dissimilarité quantifie la différence entre intervalles : plus le résultat est élevé, plus un changement est probable.

- **KLIEP** utilise la divergence de Kullback-Leibler
- **uLSIF** utilise la divergence de Pearson
- **RuLSIF** utilise la divergence de Pearson $\alpha$-relative lorsque le ratio de densité est non borné
- **SPLL** suppose que les données $W_1$ proviennent d'un mélange gaussien, dérivant le critère de détection via une borne supérieure de la log-vraisemblance des données dans $W_2$

#### Méthodes de sous-espaces

Ces approches utilisent la notion de sous-espaces pour identifier les changements, s'appuyant sur l'identification de systèmes issue de la théorie du contrôle.

##### Identification de sous-espaces (SI)

Cette méthode propose des équations paramétriques où $x(t)$ représente l'état interne du système observé et $y(t)$ la sortie observée :

$$\begin{align}
&x(t+1)=Ax(t)+Ke(t) \\
&y(t)=Cx(t)+e(t)
\end{align}$$

L'objectif consiste à estimer la matrice d'observabilité étendue, qui mesure la capacité d'inférer les états internes $x(t)$ à partir des sorties externes $y(t)$ :

$$O_k=\begin{bmatrix} C^T & (CA)^T & \cdots&(CA^{k-1})^T \end{bmatrix}$$

#### Transformation du spectre singulier (SST)

SST prend la matrice de Hankel de la série temporelle avec une fenêtre de taille $L$ fixée. Cette matrice trajectoire se décompose en sous-matrices via la décomposition en valeurs singulières (SVD). Une mesure de distance compare les spectres singuliers de deux matrices trajectoires consécutives.

### Méthodes probabilistes

#### Détection bayésienne de points de rupture (BCPD)

BCPD applique les principes bayésiens en supposant qu'une séquence d'observations peut se diviser en états non chevauchants, les données de chaque état suivant une distribution i.i.d. $P(x_t|\eta_\tau)$.

La méthode introduit une variable auxiliaire "longueur de course" $r_t$, indiquant le temps écoulé depuis le dernier point de rupture. Cette variable se remet à zéro au temps $t$ si un changement d'état se produit, sinon elle augmente d'une unité temporelle. Un changement est détecté lorsque la distribution de $r_t$ atteint sa probabilité maximale.

#### Processus gaussien (GP)

Les processus gaussiens constituent une méthode probabiliste pour l'analyse et la prédiction de séries temporelles stationnaires. Ils généralisent la distribution gaussienne et se définissent comme une collection de variables aléatoires dont tout sous-ensemble fini suit une distribution gaussienne jointe.

Les observations se définissent comme une version bruitée des valeurs de fonction gaussienne :

$$x_t=f(t)+\varepsilon_t$$

où $\varepsilon_t\sim\mathcal N(0,\sigma^2_n)$ et $f(t)\sim GP(0,K)$.

L'algorithme estime la distribution prédictive au temps $t$ en utilisant les observations disponibles jusqu'au temps $(t-1)$, puis calcule la p-valeur pour l'observation réelle $y_t$ sous la distribution de référence $\mathcal N(\hat y_t,\hat{\sigma^2})$.

### Méthodes à base de noyaux

Ces méthodes projettent les observations dans un espace de Hilbert à noyau reproduisant associé à un noyau reproduisant $k(.,.)$ et une application $\Phi(X) = k(X,.)$. Elles utilisent ensuite une statistique de test basée sur le ratio discriminant de Fisher à noyau comme mesure d'homogénéité entre fenêtres.

Les fenêtres passent par un noyau, puis leurs moyennes et covariances se calculent :

$$\hat\mu=\frac 1 n \sum_{\ell=1}^n k(X_\ell,\cdot)$$

$$\hat\Sigma=\frac 1 n \sum_{\ell=1}^n(k(X_\ell,.)-\hat\mu)\otimes(k(X_\ell,.)-\hat\mu)$$

Le ratio discriminant de Fisher à noyau entre deux échantillons se définit comme :

$$KFDR(X_1^{\text{longueur }n_1},X_2^{\text{longueur }n_2})=\frac{n_1n_2}{n_1+n_2}\langle\hat\mu_2-\hat\mu_1,(\hat\Sigma_w+\gamma I)^{-1}(\hat\mu_2-\hat\mu_1)\rangle_\mathcal{H}$$

L'inconvénient principal réside dans la dépendance forte au choix de la fonction noyau et de ses paramètres, problème aggravé dans les espaces de dimension modérée à élevée.

### Méthodes basées sur les graphes

Le graphe découle généralement d'une distance ou dissimilarité généralisée sur l'espace des échantillons, avec les observations temporelles comme nœuds et les arêtes connectant les observations selon leur distance.

Pour un temps $t^*$ où un changement pourrait se produire, les données se divisent en deux fenêtres, avant et après $t^*$. Ceci revient à créer deux sous-ensembles de nœuds correspondant aux points des fenêtres 1 et 2.

La mesure $R_G$ compte le nombre d'arêtes connectant les nœuds de $W_1$ aux nœuds de $W_2$, indépendamment de leur distance. Intuitivement, un faible nombre d'arêtes connectant les fenêtres (petit $R_G$) suggère un changement.

Différents couples de fenêtres produisent différentes valeurs de $R_G$. Une z-statistique dérivée de $R_G$ identifie sa valeur maximale dans le jeu de données comme point de rupture potentiel.

### Méthodes de clustering

Le problème de détection de points de rupture peut se considérer comme un problème de clustering à nombre connu ou inconnu de clusters, où les observations intra-cluster sont identiquement distribuées et les observations entre clusters adjacents ne le sont pas.

#### Bottom-up

Si une série temporelle a une longueur $n$, bottom-up commence par proposer $\lfloor n/2 \rfloor$ segments. Pour tous les segments, il calcule le coût de fusion potentielle. En commençant par le coût le plus faible, il fusionne les segments puis recalcule les coûts, jusqu'à ce que le coût de la prochaine fusion dépasse une erreur maximale $e$.

#### SWAB (Fenêtre glissante et bottom-up)

SWAB s'appuie sur bottom-up. Il prend toute la série temporelle $T$ et une fenêtre $W$ suffisamment longue pour contenir 5 segments. Bottom-up s'applique aux données de la fenêtre, conservant le segment le plus à gauche comme définitif.

#### Longueur de description minimale (MDL)

MDL définit la "longueur de description d'une série temporelle $T$" notée $DL(T)$ comme le nombre total de bits requis pour représenter la série :

$$DL(T)=m\times H(T)$$

où $m$ est la longueur de $T$ et $H(T)$ son entropie.

L'algorithme crée des clusters et les modifie en lisant les données. À chaque point, il choisit l'option réduisant le plus le nombre de bits nécessaire pour décrire tous les clusters.

#### Méthode des shapelets

Cette méthode crée un "shapelet" - un petit motif dans $T$ - beaucoup plus proche d'une partie de $T$ que du reste selon une définition de distance donnée. Elle crée itérativement des shapelets associés à quelques points de données, les retirant ensuite de $T$ jusqu'à ce que toutes les données soient clustérisées.

#### Ajustement de modèle

Cette approche détecte un changement lorsqu'un nouvel élément ou bloc de données ne s'ajuste à aucun cluster existant :

$$\text{Changement}=\bigwedge_{j=1}^k [d(x_{i+1}, \text{centre}(C_j))>\text{rayon}(C_j)]$$

où $k$ est le nombre de clusters et le rayon se définit comme :

$$\text{rayon}(C)=\sqrt{\frac{\sum_{i=1}^n(x_i-\mu)^2}{n}}$$

### Analyse comparative et discussion

#### Performance temporelle

L'analyse des performances temporelles révèle des différences significatives entre familles d'algorithmes :

- Les méthodes supervisées sont n-temps réel (vérifient s'il y a un point de rupture dans la fenêtre courante)
- Les méthodes de rapport de vraisemblance sont (n+k)-temps réel (fenêtre courante de longueur n plus sous-séquence rétrospective de longueur k)
- Les modèles de sous-espaces sont également (n+k)-temps réel
- Les modèles probabilistes sont n-temps réel
- Les méthodes à base de noyaux sont (n+k)-temps réel
- Les méthodes basées sur les graphes sont n-temps réel
- Pour les méthodes de clustering : SWAB est w-temps réel (w = longueur du tampon), MDL et Shapelet sont infini-temps réel (hors ligne), l'ajustement de modèle est n-temps réel

#### Scalabilité computationnelle

La scalabilité varie considérablement selon les familles d'algorithmes. Généralement, lorsque la dimension des séries temporelles augmente, les méthodes non-paramétriques gagnent en efficacité computationnelle et deviennent moins coûteuses que les méthodes paramétriques.

Les méthodes supervisées présentent une complexité généralement polynomiale, tandis que les approches de rapport de vraisemblance varient selon l'implémentation spécifique. Les méthodes probabilistes offrent souvent une complexité linéaire favorable aux applications temps réel.

#### Contraintes d'apprentissage et robustesse

Les approches supervisées supposent qu'une période de transition peut être détectée indépendamment de l'état actuel de la série temporelle, tandis que les algorithmes non supervisés supposent que la distribution des données change avant et après chaque point de rupture.

Les approches supervisées surpassent fréquemment les méthodes non supervisées pour la détection de points de rupture, mais dépendent de données d'entraînement de qualité et quantité suffisantes, pas toujours accessibles pour les données réelles. Les algorithmes supervisés multi-classes nécessitent également la connaissance du nombre d'états possibles.

Les méthodes non-paramétriques démontrent une robustesse supérieure aux approches paramétriques, ces dernières dépendant fortement du choix des paramètres. La complexité du problème CPD augmente pour les méthodes paramétriques lorsque les données présentent une dimensionnalité modérée à élevée.

#### Performance empirique

L'évaluation objective comparative des différentes méthodes CPD reste difficile en raison de l'utilisation de jeux de données différents. Les études portent sur des domaines variés : reconnaissance vocale, ECG, interfaces cerveau-ordinateur, données NDVI de biomasse agricole, données de capteurs domestiques intelligents, et analyses d'activité humaine.

Les méthodes supervisées tendent à être plus précises que les méthodes non supervisées si suffisamment de données d'entraînement existent et si la série est stationnaire. Lorsque ces conditions ne sont pas remplies, les méthodes non supervisées s'avèrent plus utiles.

Parmi les méthodes non supervisées, RuLSIF démontre constamment une forte précision. Les méthodes paramétriques n'exhibent pas de bonnes performances pour les données bruitées ou les systèmes hautement dynamiques.

Pour les séries temporelles haute dimension, les méthodes de rapport de vraisemblance et les modèles de sous-espaces ne constituent pas les meilleurs choix car ils ne peuvent traiter directement les données multidimensionnelles. Les méthodes basées sur les graphes ou probabilistes s'avèrent plus prometteuses dans ce contexte.

### Défis futurs et perspectives

Plusieurs axes de recherche émergent pour améliorer les capacités de détection de points de rupture dans les années à venir.

#### Développement d'algorithmes en ligne

Le besoin de développement d'algorithmes véritablement temps réel demeure critique. Les applications modernes exigent des réponses quasi-instantanées, nécessitant des algorithmes capables de traiter les flux de données en continu sans accumulation de retard. Cette exigence pousse vers des architectures algorithmiques fondamentalement différentes, privilégiant l'efficacité computationnelle à la précision exhaustive.

#### Analyse formelle de robustesse

L'absence d'analyse formelle de robustesse constitue une lacune majeure. L'assertion selon laquelle "les méthodes non-paramétriques sont plus robustes que les méthodes paramétriques" manque de rigueur mathématique. Une caractérisation formelle des garanties de robustesse, incluant les bornes d'erreur et les conditions de convergence, permettrait une sélection plus éclairée des algorithmes selon les contraintes applicatives.

#### Fenêtres adaptatifs et taille variable

Les algorithmes utilisant des fenêtres se heurtent au dilemme taille-profondeur : des fenêtres plus petites ne permettent pas d'examiner suffisamment loin dans le futur, tandis que des fenêtres plus grandes introduisent des retards inacceptables. Le développement de fenêtres de taille variable, s'adaptant dynamiquement aux caractéristiques locales des données, représente une voie prometteuse pour résoudre ce compromis.

#### Évaluation de significativité statistique

L'évaluation de la significativité d'un candidat point de rupture reste un problème ouvert pour les méthodes non supervisées. L'établissement de tests statistiques robustes, tenant compte de la structure temporelle des données et des corrélations locales, permettrait de réduire les faux positifs tout en maintenant une sensibilité élevée.

#### Traitement des séries non-stationnaires

Les méthodes de gestion des séries temporelles non-stationnaires nécessitent un développement approfondi. Les applications réelles génèrent fréquemment des données dont les propriétés statistiques évoluent graduellement, compliquant la distinction entre changements graduels et points de rupture discrets. L'intégration de modèles adaptatifs capables de distinguer ces deux types de variations constitue un défi méthodologique majeur.

#### Détection multi-échelle et hiérarchique

L'extension vers la détection multi-échelle permettrait d'identifier simultanément des changements à différents horizons temporels. Certains phénomènes présentent des ruptures à court terme superposées à des tendances de long terme, nécessitant une approche hiérarchique de la détection.

#### Intégration de connaissances a priori

L'incorporation de connaissances domaine-spécifiques dans les algorithmes de détection reste largement sous-exploitée. L'intégration de contraintes physiques, de modèles causaux ou de connaissances expertes pourrait améliorer significativement la précision et réduire les faux positifs.

### Conclusion

La détection de points de rupture dans les séries temporelles constitue un domaine riche et en évolution rapide, avec des applications transversales dans de nombreux secteurs. La diversité des approches méthodologiques - supervisées, non supervisées, paramétriques, non-paramétriques - reflète la complexité inhérente du problème et l'absence de solution universelle.

Les méthodes supervisées excellent lorsque des données d'entraînement de qualité sont disponibles, mais leur dépendance aux données étiquetées limite leur applicabilité. Les approches non supervisées offrent une flexibilité supérieure au prix d'une précision parfois moindre, avec des méthodes comme RuLSIF démontrant des performances particulièrement prometteuses.

Le choix d'une méthode dépend fondamentalement des contraintes applicatives : exigences temps réel, dimensionnalité des données, stationnarité, volume de données et ressources computationnelles disponibles. Les applications futures devront probablement combiner plusieurs approches pour exploiter leurs forces complémentaires.

L'évolution vers des systèmes adaptatifs, intégrant apprentissage en ligne et détection temps réel, représente l'horizon naturel de cette discipline. Les défis méthodologiques identifiés - robustesse formelle, fenêtres adaptatifs, séries non-stationnaires - constituent autant d'opportunités pour des avancées significatives dans les années à venir.

La convergence entre théorie statistique rigoureuse et implémentations computationnellement efficaces demeure l'objectif central, permettant de transformer les avancées académiques en solutions industrielles robustes et déployables à grande échelle.
