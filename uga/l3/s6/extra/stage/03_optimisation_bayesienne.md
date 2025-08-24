## 03 // optimisation bayesienne

## Optimisation bayésienne

L'optimisation bayésienne représente une approche sophistiquée pour résoudre des problèmes d'optimisation globale lorsque l'évaluation de la fonction objectif s'avère coûteuse, bruitée, ou analytiquement intractable. Cette méthode trouve ses applications dans de nombreux domaines, de l'apprentissage automatique au réglage d'hyperparamètres d'algorithmes complexes, en passant par l'optimisation de processus industriels.

### Le défi de l'optimisation coûteuse

#### Problématique fondamentale

Dans de nombreuses situations pratiques, l'évaluation d'une fonction objectif nécessite des ressources computationnelles considérables ou des expérimentations physiques onéreuses. Considérons l'optimisation des paramètres d'un algorithme comme BEAST : chaque évaluation implique l'exécution complète de l'algorithme sur un ensemble de séries temporelles, processus potentiellement long et gourmand en ressources.

Les méthodes d'optimisation traditionnelles, telles que la recherche par grille ou les algorithmes évolutionnaires, deviennent impraticables dans ce contexte. Elles requièrent typiquement des milliers d'évaluations de la fonction objectif, rendant l'optimisation prohibitivement coûteuse.

L'optimisation bayésienne résout ce dilemme en construisant un modèle probabiliste de la fonction objectif, permettant de prendre des décisions d'échantillonnage informées. Plutôt que d'évaluer aveuglément de nombreux points, elle concentre les évaluations sur les régions les plus prometteuses de l'espace de recherche.

#### Caractéristiques des fonctions difficiles

Les fonctions objectifs rencontrées dans l'optimisation bayésienne présentent généralement plusieurs caractéristiques problématiques. Elles sont souvent non-convexes, avec de multiples optima locaux qui piègent les algorithmes d'optimisation locale. Leur évaluation peut être bruitée, introduisant de l'incertitude dans les mesures de performance.

Ces fonctions manquent fréquemment de forme analytique explicite, rendant impossible l'utilisation de méthodes basées sur le gradient. Leur paysage peut présenter des discontinuités ou des régions plates, compliquant davantage la recherche de l'optimum global.

L'absence d'informations structurelles a priori sur la fonction renforce la nécessité d'une approche adaptative capable d'apprendre la structure du problème au fur et à mesure de l'exploration.

### Fondements conceptuels

#### Philosophie bayésienne appliquée à l'optimisation

L'optimisation bayésienne transpose les principes de l'inférence bayésienne au problème d'optimisation. Elle traite la fonction objectif inconnue comme une variable aléatoire dotée d'une distribution de probabilité a priori, mise à jour séquentiellement à mesure que de nouvelles évaluations deviennent disponibles.

Cette perspective probabiliste transforme fondamentalement l'approche d'optimisation. Plutôt que de chercher déterministiquement l'optimum, l'algorithme maintient une croyance probabiliste sur la localisation des régions prometteuses et quantifie l'incertitude associée à ses prédictions.

Le processus d'optimisation devient alors un processus d'apprentissage séquentiel : chaque nouvelle évaluation réduit l'incertitude sur la fonction objectif et informe les décisions futures d'échantillonnage.

#### Équilibre exploration-exploitation

Le cœur de l'optimisation bayésienne réside dans la gestion de l'équilibre exploration-exploitation. L'exploitation consiste à échantillonner dans les régions où le modèle prédit les meilleures valeurs de la fonction objectif. L'exploration privilégie les régions de forte incertitude où des découvertes importantes pourraient être faites.

Cet équilibre évite les pièges des approches purement locales (exploitation excessive) et des méthodes purement aléatoires (exploration inefficace). La théorie de la décision bayésienne fournit un cadre principiel pour résoudre ce dilemme via l'optimisation de fonctions d'acquisition.

### Processus gaussiens comme modèles substituts

#### Introduction aux processus gaussiens

Les processus gaussiens constituent l'outil mathématique central de l'optimisation bayésienne. Un processus gaussien représente une généralisation des distributions gaussiennes multivariées à des espaces de fonctions. Formellement, un processus gaussien est une collection de variables aléatoires, dont tout sous-ensemble fini suit une distribution gaussienne multivariée.

Un processus gaussien se caractérise entièrement par sa fonction de moyenne $m(x)$ et sa fonction de covariance $k(x, x')$ :

$$
f(x) \sim \mathcal{GP}(m(x), k(x, x'))
$$

Cette spécification définit la distribution a priori sur l'espace des fonctions, encodant nos croyances initiales sur la régularité et le comportement de la fonction objectif.

#### Fonction de moyenne

La fonction de moyenne $m(x) = \mathbb{E}[f(x)]$ représente notre prédiction a priori de la valeur de la fonction en tout point. Dans de nombreuses applications d'optimisation, on choisit une fonction de moyenne constante ou nulle, reflétant l'absence de connaissances préalables sur le niveau général de la fonction.

Cette simplicité apparente ne limite pas la flexibilité du modèle : les observations ajusteront automatiquement les prédictions indépendamment du choix initial de la fonction de moyenne, pourvu que la fonction de covariance soit appropriée.

#### Fonction de covariance et noyaux

La fonction de covariance $k(x, x') = \text{Cov}[f(x), f(x')]$ encode les hypothèses de régularité sur la fonction objectif. Elle détermine comment les valeurs de la fonction en des points différents sont corrélées, influençant directement la capacité d'interpolation et d'extrapolation du modèle.

Le choix du noyau reflète les propriétés attendues de la fonction objectif. Le noyau gaussien (RBF) :

$$
k_{\text{RBF}}(x, x') = \sigma_f^2 \exp\left(-\frac{||x - x'||^2}{2\ell^2}\right)
$$

assume des fonctions infiniment différentiables avec une corrélation qui décroît exponentiellement avec la distance. Le paramètre $\ell$ contrôle la longueur de corrélation, tandis que $\sigma_f^2$ détermine la variance marginale.

Le noyau de Matérn offre une alternative plus flexible :

$$
k_{\text{Matérn}}(x, x') = \sigma_f^2 \frac{2^{1-\nu}}{\Gamma(\nu)} \left(\frac{\sqrt{2\nu}||x - x'||}{\ell}\right)^\nu K_\nu\left(\frac{\sqrt{2\nu}||x - x'||}{\ell}\right)
$$

Le paramètre $\nu$ contrôle la différentiabilité : $\nu = 1/2$ produit des fonctions continues mais non-différentiables, tandis que $\nu \to \infty$ converge vers le noyau gaussien.

#### Inférence et prédiction

Après avoir observé $n$ points $\mathbf{X} = \{x_1, …, x_n\}$ avec leurs valeurs $\mathbf{y} = \{y_1, …, y_n\}$, la distribution a posteriori du processus gaussien reste gaussienne. La prédiction en un nouveau point $x^*$ suit une distribution normale :

$$
f(x^*) | \mathbf{X}, \mathbf{y} \sim \mathcal{N}(\mu(x^*), \sigma^2(x^*))
$$

où :

$$
\mu(x^*) = m(x^*) + k(x^*, \mathbf{X})[K + \sigma_n^2 I]^{-1}(\mathbf{y} - m(\mathbf{X}))
$$

$$
\sigma^2(x^*) = k(x^*, x^*) - k(x^*, \mathbf{X})[K + \sigma_n^2 I]^{-1}k(\mathbf{X}, x^*)
$$

La matrice $K$ contient les covariances entre tous les points observés, et $\sigma_n^2$ représente la variance du bruit d'observation.

Ces formules révèlent la beauté des processus gaussiens : la moyenne prédictive interpole entre les observations avec une pondération déterminée par les similarités encodées dans le noyau, tandis que la variance prédictive quantifie l'incertitude, diminuant près des observations et augmentant dans les régions inexplorées.

#### Traitement de l'incertitude

L'un des atouts majeurs des processus gaussiens réside dans leur quantification native de l'incertitude. Contrairement aux modèles déterministes qui fournissent des prédictions ponctuelles, les processus gaussiens produisent des distributions prédictives complètes.

Cette information d'incertitude s'avère cruciale pour l'optimisation bayésienne : elle guide les décisions d'échantillonnage en identifiant les régions où l'acquisition d'informations supplémentaires serait la plus bénéfique.

L'incertitude prédictive reflète deux sources d'ignorance : l'incertitude épistémique liée à la connaissance limitée de la fonction, et l'incertitude aléatoire due au bruit d'observation. Le processus gaussien sépare naturellement ces composantes.

### Fonctions d'acquisition

#### Principe général

Les fonctions d'acquisition constituent le mécanisme de décision de l'optimisation bayésienne. Elles transforment la distribution prédictive du processus gaussien en un critère scalaire guidant le choix du prochain point à évaluer.

Une fonction d'acquisition $\alpha(x)$ assigne à chaque point candidat $x$ une valeur reflétant l'utilité attendue de son évaluation. Le prochain point à échantillonner est celui maximisant cette utilité :

$$
x_{\text{next}} = \arg\max_x \alpha(x)
$$

Cette optimisation de la fonction d'acquisition s'effectue généralement par des méthodes conventionnelles, car les fonctions d'acquisition sont typiquement peu coûteuses à évaluer et analytiquement tractables.

#### Expected Improvement (EI)

L'Expected Improvement représente l'une des fonctions d'acquisition les plus intuitives et largement utilisées. Elle quantifie l'amélioration attendue par rapport au meilleur point observé jusqu'à présent.

Soit $f^* = \max_{i=1,…,n} y_i$ la meilleure valeur observée. L'amélioration en un point $x$ est définie par $I(x) = \max(0, f(x) - f^*)$. L'Expected Improvement s'écrit :

$$
\text{EI}(x) = \mathbb{E}[I(x)] = (\mu(x) - f^*)\Phi(Z) + \sigma(x)\phi(Z)
$$

où $Z = \frac{\mu(x) - f^*}{\sigma(x)}$, et $\Phi$ et $\phi$ sont respectivement la fonction de répartition et la densité de la loi normale standard.

Cette formulation révèle l'équilibre exploration-exploitation : le premier terme favorise les régions de forte moyenne prédictive (exploitation), tandis le second privilégie les zones d'incertitude élevée (exploration).

#### Probability of Improvement (PI)

La Probability of Improvement calcule la probabilité qu'un point améliore le meilleur résultat actuel :

$$
\text{PI}(x) = P(f(x) > f^*) = \Phi\left(\frac{\mu(x) - f^*}{\sigma(x)}\right)
$$

Bien que conceptuellement simple, cette fonction d'acquisition souffre d'une tendance excessive à l'exploitation. Elle peut converger prématurément vers des optima locaux en négligeant l'exploration de régions incertaines mais potentiellement prometteuses.

#### Upper Confidence Bound (UCB)

La fonction Upper Confidence Bound adopte une approche inspirée de la théorie des bandits multi-bras :

$$
\text{UCB}(x) = \mu(x) + \beta \sigma(x)
$$

Le paramètre $\beta$ contrôle l'équilibre exploration-exploitation : des valeurs élevées favorisent l'exploration, tandis que des valeurs faibles privilégient l'exploitation. La théorie suggère des choix de $\beta$ dépendant de l'horizon temporel et de la dimension du problème.

#### Entropy Search et ses variantes

Les méthodes basées sur l'entropie adoptent une perspective informationnelle. Elles cherchent à maximiser la réduction d'entropie de la distribution a posteriori sur la localisation de l'optimum global.

L'Entropy Search maximise la réduction d'entropie de $p(x^*)$, la distribution sur la localisation de l'optimum :

$$
\text{ES}(x) = H[p(x^*)] - \mathbb{E}_{y|x}[H[p(x^*|x, y)]]
$$

Cette approche présente l'avantage théorique de maximiser directement l'information acquise sur l'objectif d'optimisation, mais sa mise en œuvre s'avère computationnellement complexe.

#### Knowledge Gradient

La fonction Knowledge Gradient mesure l'amélioration attendue de la meilleure décision future après avoir observé un nouveau point :

$$
\text{KG}(x) = \mathbb{E}[V^{n+1} - V^n | x]
$$

où $V^n$ représente la valeur du meilleur point après $n$ observations. Cette approche intègre naturellement l'horizon temporel de l'optimisation et s'adapte aux budgets d'évaluation limités.

### Optimisation de la fonction d'acquisition

#### Défis computationnels

L'optimisation de la fonction d'acquisition constitue un sous-problème crucial de l'optimisation bayésienne. Bien que généralement moins coûteuse que l'évaluation de la fonction objectif originale, cette optimisation peut présenter ses propres défis.

Les fonctions d'acquisition peuvent être multimodales, particulièrement dans les espaces de grande dimension ou avec de nombreux points observés. Leur paysage peut présenter des plateaux ou des discontinuités compliquant l'optimisation par gradient.

#### Méthodes d'optimisation

L'optimisation de la fonction d'acquisition s'effectue typiquement par des méthodes d'optimisation globale. Les algorithmes évolutionnaires, tels que l'optimisation différentielle ou les stratégies d'évolution, offrent une robustesse face aux optima locaux.

Les méthodes basées sur le gradient, comme L-BFGS, peuvent s'avérer efficaces lorsque les dérivées de la fonction d'acquisition sont disponibles analytiquement. La plupart des fonctions d'acquisition standard admettent des dérivées en forme close, facilitant cette approche.

Les méthodes hybrides combinent recherche globale et raffinement local : une phase d'exploration globale identifie les régions prometteuses, suivie d'une optimisation locale pour la précision finale.

#### Initialisation et redémarrages multiples

La qualité de l'optimisation de la fonction d'acquisition influence directement l'efficacité de l'optimisation bayésienne. Des heuristiques d'initialisation intelligentes améliorent les performances : initialiser près des meilleurs points observés, dans les régions d'incertitude élevée, ou selon des designs expérimentaux optimaux.

Les redémarrages multiples avec des initialisations diversifiées réduisent le risque de convergence vers des optima locaux sous-optimaux de la fonction d'acquisition.

### Gestion des hyperparamètres

#### Optimisation des hyperparamètres du noyau

Les performances de l'optimisation bayésienne dépendent critiquement du choix des hyperparamètres du processus gaussien. Ces paramètres, tels que les longueurs de corrélation et la variance du noyau, déterminent les propriétés d'interpolation et d'extrapolation du modèle substitut.

L'optimisation de ces hyperparamètres s'effectue généralement par maximisation de la vraisemblance marginale :

$$
\log p(\mathbf{y} | \mathbf{X}, \boldsymbol{\theta}) = -\frac{1}{2}\mathbf{y}^T K_{\boldsymbol{\theta}}^{-1} \mathbf{y} - \frac{1}{2}\log |K_{\boldsymbol{\theta}}| - \frac{n}{2}\log(2\pi)
$$

Cette approche présente l'avantage de l'automatisation : les hyperparamètres s'ajustent automatiquement aux données observées sans intervention manuelle.

#### Approches bayésiennes complètes

L'inférence bayésienne complète place des prioris sur les hyperparamètres et marginalise leur incertitude. Cette approche évite le sur-ajustement aux hyperparamètres et fournit des prédictions plus robustes.

L'intégration analytique s'avérant généralement intractable, des méthodes d'échantillonnage telles que MCMC ou l'inférence variationnelle approximent la distribution a posteriori des hyperparamètres.

#### Validation et diagnostics

La validation des hyperparamètres s'effectue par validation croisée ou analyse des résidus. Les méthodes de validation croisée leave-one-out s'implémentent efficacement pour les processus gaussiens grâce aux formules analytiques des prédictions.

L'analyse des résidus révèle d'éventuelles inadéquations du modèle : autocorrélations résiduelles, hétéroscédasticité, ou non-normalité suggérant des modifications du noyau ou l'inclusion de bruit non-gaussien.

### Extensions et variants avancés

#### Optimisation multi-objectifs

L'optimisation bayésienne s'étend naturellement aux problèmes multi-objectifs où plusieurs critères conflictuels doivent être optimisés simultanément. L'approche ParEGO transforme le problème multi-objectif en une série de problèmes scalaires via des fonctions de scalarisation aléatoires.

Les méthodes basées sur l'Expected Hypervolume Improvement généralisent directement l'Expected Improvement aux espaces multi-objectifs. Elles maximisent l'amélioration attendue de l'hypervolume du front de Pareto.

#### Contraintes et optimisation conditionnelle

De nombreux problèmes d'optimisation pratiques impliquent des contraintes sur les variables ou des fonctions de faisabilité. L'optimisation bayésienne contrainte modélise les contraintes par des processus gaussiens séparés et modifie les fonctions d'acquisition pour pénaliser les régions non-faisables.

L'Expected Constrained Improvement pondère l'Expected Improvement par la probabilité de faisabilité :

$$
\text{ECI}(x) = \text{EI}(x) \times P(\text{faisable} | x)
$$

#### Espaces de recherche discrets et mixtes

L'extension aux variables discrètes ou catégorielles nécessite des noyaux adaptés. Les noyaux pour variables catégorielles mesurent la similarité entre catégories, tandis que les espaces mixtes combinent noyaux continus et discrets via des produits ou sommes pondérées.

Les méthodes d'optimisation de la fonction d'acquisition s'adaptent également : algorithmes génétiques pour les variables discrètes, optimisation en nombres entiers pour les variables mixtes.

#### Optimisation bayésienne distribuée

Les implémentations distribuées permettent l'évaluation parallèle de multiples points candidats. L'approche par lot (batch) sélectionne simultanément plusieurs points maximisant une fonction d'acquisition modifiée tenant compte des corrélations entre candidats.

Les stratégies asynchrones gèrent des évaluations de durées variables en mettant à jour le modèle dès qu'une évaluation se termine, maintenant un flux constant de nouveaux candidats.

### Applications pratiques et considérations

#### Réglage d'hyperparamètres en apprentissage automatique

L'optimisation bayésienne révolutionne le réglage d'hyperparamètres en apprentissage automatique. Elle automatise la recherche d'hyperparamètres optimaux pour des modèles complexes tels que les réseaux de neurones profonds ou les forêts aléatoires.

Cette application tire parti de la capacité de l'optimisation bayésienne à gérer des espaces de recherche de grande dimension avec des évaluations coûteuses. Chaque évaluation correspond à l'entraînement complet d'un modèle, processus potentiellement très long.

#### Optimisation de processus expérimentaux

Les sciences expérimentales bénéficient particulièrement de l'optimisation bayésienne pour la conception d'expériences. L'approche guide la sélection des conditions expérimentales maximisant l'information acquise tout en minimisant le coût expérimental.

La quantification d'incertitude native des processus gaussiens facilite l'identification des régions nécessitant des expériences supplémentaires, optimisant l'allocation des ressources expérimentales limitées.

#### Optimisation de paramètres d'algorithmes

L'optimisation des paramètres d'algorithmes complexes, comme BEAST, illustre parfaitement l'utilité de l'optimisation bayésienne. Chaque évaluation implique l'exécution de l'algorithme sur un ensemble de données, processus coûteux justifiant l'approche sophistiquée.

L'optimisation bayésienne adapte automatiquement sa stratégie d'exploration aux caractéristiques du paysage de performance, concentrant les évaluations sur les régions de paramètres les plus prometteuses.

#### Considérations pratiques

Le succès de l'optimisation bayésienne dépend de plusieurs facteurs pratiques. Le choix du noyau doit refléter les propriétés attendues de la fonction objectif : lissage pour des fonctions régulières, comportements périodiques pour des phénomènes cycliques.

La dimensionnalité de l'espace de recherche influence les performances : l'optimisation bayésienne excelle en dimensions faibles à modérées (typiquement < 20) mais peut peiner en très grande dimension sans adaptations spécifiques.

La définition de l'espace de recherche nécessite une attention particulière : des bornes trop restrictives peuvent exclure l'optimum global, tandis que des espaces trop vastes diluent l'efficacité de l'échantillonnage.

L'initialisation avec des points de départ judicieux accélère la convergence. Les designs expérimentaux optimaux, tels que les hypercubes latins, fournissent une couverture uniforme de l'espace initial.

La gestion de l'arrêt constitue un aspect crucial : critères de convergence basés sur l'amélioration attendue, budgets d'évaluation prédéfinis, ou détection de plateaux dans les performances.

### Limites et perspectives

#### Malédiction de la dimensionnalité

L'optimisation bayésienne souffre de la malédiction de la dimensionnalité : les performances se dégradent avec l'augmentation de la dimension de l'espace de recherche. Cette limitation découle de la nature des processus gaussiens et de la difficulté croissante d'optimiser les fonctions d'acquisition.

Des approches récentes tentent de contourner cette limitation : décompositions additives supposant une structure séparable, réductions de dimensionnalité par projections aléatoires, ou exploitation de structures particulières comme la parcimonie.

#### Hypothèses de régularité

L'efficacité des processus gaussiens repose sur des hypothèses de régularité de la fonction objectif. Les fonctions hautement discontinues, avec de nombreuses discontinuités ou comportements chaotiques, peuvent défier les capacités d'interpolation des noyaux standard.

Le développement de noyaux spécialisés et de modèles hybrides combinant processus gaussiens et autres techniques offre des perspectives d'amélioration pour ces cas difficiles.

#### Coût computationnel

La complexité computationnelle des processus gaussiens croît cubiquement avec le nombre d'observations, limitant l'applicabilité aux problèmes avec de très nombreuses évaluations. Des approximations telles que les processus gaussiens parcimonieux ou les méthodes d'induction réduisent cette complexité.

Les implémentations GPU et les algorithmes distribués ouvrent de nouvelles possibilités pour l'optimisation bayésienne à grande échelle.

#### Intégration avec l'apprentissage profond

L'intersection entre optimisation bayésienne et apprentissage profond génère des développements prometteurs. Les réseaux de neurones peuvent remplacer les processus gaussiens comme modèles substituts, apportant une meilleure scalabilité dimensionnelle.

Les réseaux de neurones bayésiens combinent la flexibilité représentationnelle des réseaux profonds avec la quantification d'incertitude nécessaire à l'optimisation bayésienne.

Ces avancées positionnent l'optimisation bayésienne comme un outil central pour l'optimisation intelligente dans un monde de plus en plus dominé par des systèmes complexes et coûteux à évaluer.
