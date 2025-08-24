## 01 // prerequis beast

## Prérequis mathématiques pour l'algorithme BEAST

L'algorithme BEAST représente une confluence sophistiquée de plusieurs domaines mathématiques et statistiques. Pour comprendre pleinement son fonctionnement, il convient de maîtriser les fondements théoriques sur lesquels il repose. Ces concepts, bien qu'apparemment disparates, s'articulent harmonieusement pour créer un cadre d'analyse puissant des séries temporelles.

### Statistiques bayésiennes

#### Le paradigme bayésien

La statistique bayésienne repose sur une philosophie fondamentalement différente de l'approche fréquentiste classique. Plutôt que de considérer les paramètres comme des constantes inconnues à estimer, l'approche bayésienne les traite comme des variables aléatoires dotées de leurs propres distributions de probabilité.

Cette perspective révolutionnaire trouve ses racines dans le théorème de Bayes, énoncé au XVIIIe siècle par Thomas Bayes. Le théorème établit une relation fondamentale entre les probabilités conditionnelles, permettant de réviser nos croyances à mesure que de nouvelles informations deviennent disponibles.

#### Le théorème de Bayes

Le théorème de Bayes s'exprime mathématiquement sous la forme :

$$
P(\theta | \text{données}) = \frac{P(\text{données} | \theta) \times P(\theta)}{P(\text{données})}
$$

Cette équation apparemment simple encode une richesse conceptuelle considérable. Le terme $P(\theta | \text{données})$ représente notre connaissance a posteriori des paramètres après observation des données. Cette distribution a posteriori constitue l'objectif ultime de l'inférence bayésienne : elle quantifie notre incertitude résiduelle sur les paramètres en tenant compte de toute l'information disponible.

La vraisemblance $P(\text{données} | \theta)$ mesure la compatibilité entre les données observées et différentes valeurs possibles des paramètres. Cette fonction joue un rôle central dans l'ajustement du modèle aux observations empiriques.

La distribution a priori $P(\theta)$ encode nos croyances initiales sur les paramètres avant l'observation des données. Cette composante distingue fondamentalement l'approche bayésienne : elle permet d'incorporer explicitement des connaissances préalables dans l'analyse statistique.

#### Distributions a priori et leur signification

Le choix des distributions a priori constitue un aspect délicat de l'analyse bayésienne. Les prioris informatifs reflètent des connaissances substantielles préexistantes, tandis que les prioris peu informatifs ou "vagues" expriment une ignorance relative sur les paramètres.

Les prioris conjugués offrent un avantage computationnel particulier : ils produisent des distributions a posteriori de forme analytique connue. Par exemple, si la vraisemblance suit une distribution normale et le priori une distribution normale également, la distribution a posteriori sera également normale avec des paramètres mis à jour.

Cette propriété de conjugaison facilite grandement les calculs, mais elle ne doit pas contraindre artificiellement le choix des prioris. L'émergence des méthodes computationnelles modernes permet désormais d'utiliser des prioris non-conjugués lorsque cela se justifie scientifiquement.

#### Prédiction bayésienne

L'un des atouts majeurs de l'approche bayésienne réside dans sa capacité naturelle à effectuer des prédictions tout en quantifiant l'incertitude associée. La distribution prédictive a posteriori s'obtient en marginalisant sur tous les paramètres possibles :

$$
P(\tilde{y} | \text{données}) = \int P(\tilde{y} | \theta) P(\theta | \text{données}) d\theta
$$

Cette intégration capture l'incertitude paramétrique dans les prédictions, contrastant avec les approches fréquentistes qui utilisent typiquement des estimations ponctuelles des paramètres.

### Méthodes de Monte Carlo par chaînes de Markov (MCMC)

#### La nécessité computationnelle

L'inférence bayésienne se heurte souvent à des obstacles computationnels insurmontables. Le calcul de la distribution a posteriori requiert l'évaluation d'intégrales multidimensionnelles complexes, généralement analytiquement intractables pour des modèles réalistes.

Les méthodes de Monte Carlo par chaînes de Markov (MCMC) révolutionnent cette situation en proposant une approche d'échantillonnage stochastique. Plutôt que de calculer analytiquement les distributions a posteriori, ces méthodes génèrent des échantillons représentatifs de ces distributions.

#### Fondements théoriques des chaînes de Markov

Une chaîne de Markov constitue une séquence de variables aléatoires $\{X_0, X_1, X_2, …\}$ possédant la propriété markovienne : la distribution de l'état futur dépend uniquement de l'état présent, non de l'historique complet.

Formellement, cette propriété s'exprime par :

$$
P(X_{n+1} | X_0, X_1, ..., X_n) = P(X_{n+1} | X_n)
$$

Cette propriété d'absence de mémoire simplifie considérablement l'analyse mathématique des chaînes tout en préservant une richesse comportementale suffisante pour les applications statistiques.

#### Distribution stationnaire et convergence

Le concept fondamental sous-tendant l'efficacité des méthodes MCMC est celui de distribution stationnaire. Une distribution $\pi$ est stationnaire pour une chaîne de Markov si elle reste invariante sous l'opération de transition :

$$
\pi(x) = \int \pi(y) P(x | y) dy
$$

Sous certaines conditions de régularité (ergodicité, apériodicité, récurrence positive), une chaîne de Markov converge vers sa distribution stationnaire indépendamment de l'état initial. Cette propriété de convergence garantit que les échantillons générés par la chaîne représentent asymptotiquement la distribution cible.

Le théorème ergodique assure que les moyennes empiriques des échantillons convergent vers les espérances théoriques sous la distribution stationnaire :

$$
\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n f(X_i) = \mathbb{E}_\pi[f(X)]
$$

Cette convergence justifie l'utilisation des échantillons MCMC pour l'estimation des moments et quantiles des distributions a posteriori.

#### L'algorithme Metropolis-Hastings

L'algorithme Metropolis-Hastings constitue la pierre angulaire des méthodes MCMC. Il construit une chaîne de Markov dont la distribution stationnaire coïncide avec la distribution cible (typiquement la distribution a posteriori).

L'algorithme procède itérativement selon le schéma suivant :

1. À partir de l'état actuel $\theta^{(t)}$, proposer un nouvel état $\theta^*$ selon une distribution de proposition $q(\theta^* | \theta^{(t)})$
2. Calculer le ratio d'acceptation :

   $$

\alpha = \min\left(1, \frac{\pi(\theta^*) q(\theta^{(t)} | \theta^*)}{\pi(\theta^{(t)}) q(\theta^* | \theta^{(t)})}\right)

$$
3. Accepter la proposition avec probabilité $\alpha$ : si acceptée, $\theta^{(t+1)} = \theta^*$, sinon $\theta^{(t+1)} = \theta^{(t)}$

Cette règle d'acceptation garantit que la chaîne résultante admet $\pi$ comme distribution stationnaire, même si la distribution de proposition $q$ est choisie de manière sous-optimale.

Le choix de la distribution de proposition influence crucially l'efficacité de l'échantillonnage. Des propositions trop conservatrices (faible variance) génèrent des chaînes à mixing lent, tandis que des propositions trop audacieuses (forte variance) subissent des taux de rejet élevés.

### L'échantillonneur de Gibbs

L'échantillonneur de Gibbs représente un cas particulier de l'algorithme Metropolis-Hastings particulièrement adapté aux distributions multivariées. Il exploite la décomposition de la distribution jointe en distributions conditionnelles complètes.

Pour un vecteur de paramètres $\theta = (\theta_1, ..., \theta_k)$, l'algorithme cycle séquentiellement à travers les composantes, échantillonnant chacune conditionnellement aux autres :
$$

\theta_i^{(t+1)} \sim P(\theta_i | \theta_1^{(t+1)}, …, \theta_{i-1}^{(t+1)}, \theta_{i+1}^{(t)}, …, \theta_k^{(t)}, \text{données})

$$
Cette approche présente l'avantage d'éviter la spécification d'une distribution de proposition et garantit un taux d'acceptation de 100%. Cependant, elle nécessite la capacité d'échantillonner directement les distributions conditionnelles complètes.

### Reverse-Jump MCMC

Les méthodes MCMC conventionnelles opèrent dans des espaces de paramètres de dimension fixe. Le Reverse-Jump MCMC étend cette capacité aux espaces de dimension variable, permettant de comparer des modèles de complexités différentes.

Cette extension s'avère cruciale pour des problèmes comme la détection de points de rupture, où le nombre de ruptures constitue lui-même un paramètre inconnu. L'algorithme propose des mouvements trans-dimensionnels : ajout ou suppression de paramètres, modifiant la dimension de l'espace d'état.

La règle d'acceptation se généralise pour tenir compte des changements dimensionnels :
$$

\alpha = \min\left(1, \frac{\pi(\theta^*) q(\theta^{(t)} | \theta^*)}{\pi(\theta^{(t)}) q(\theta^* | \theta^{(t)})} \left| \frac{\partial \theta^*}{\partial (\theta^{(t)}, u)} \right|\right)

$$
Le terme jacobien $\left| \frac{\partial \theta^*}{\partial (\theta^{(t)}, u)} \right|$ assure la conservation des probabilités lors des transformations dimensionnelles.

### Diagnostic de convergence

L'efficacité des méthodes MCMC dépend critiquement de la convergence de la chaîne vers la distribution stationnaire. Plusieurs outils diagnostiques permettent d'évaluer cette convergence.

Les graphiques de trace visualisent l'évolution temporelle des échantillons, révélant d'éventuels problèmes de mixing ou de convergence. Une chaîne bien mélangée présente des oscillations rapides autour de la région de haute densité de la distribution cible.

Le critère de Gelman-Rubin compare la variance intra-chaîne à la variance inter-chaînes pour des chaînes multiples initialisées différemment. La convergence est suggérée lorsque ce ratio approche l'unité.

Les tailles d'échantillon efficaces quantifient l'information contenue dans les échantillons corrélés. L'autocorrélation réduit l'efficacité de l'échantillonnage, nécessitant des chaînes plus longues pour atteindre une précision donnée.

## Analyse des séries temporelles

### Décomposition temporelle

L'analyse des séries temporelles repose sur la décomposition du signal observé en composantes interprétables. Cette décomposition révèle les structures sous-jacentes masquées par la complexité apparente des données brutes.

La décomposition additive classique s'écrit :
$$

y_t = T_t + S_t + \varepsilon_t

$$
où $T_t$ représente la tendance à long terme, $S_t$ la composante saisonnière, et $\varepsilon_t$ le bruit aléatoire. Cette formulation suppose l'indépendance des composantes et l'additivité de leurs effets.

La composante de tendance capture l'évolution directionnelle globale de la série. Elle reflète des changements structurels graduels ou des shifts de régime. L'estimation de la tendance nécessite de séparer les variations persistantes des fluctuations transitoires.

### Modélisation de la saisonnalité

La saisonnalité manifeste des patterns répétitifs liés à des cycles naturels ou institutionnels. Dans le contexte écologique, la saisonnalité reflète les cycles phénologiques : germination printanière, croissance estivale, sénescence automnale, dormance hivernale.

Les modèles harmoniques offrent une représentation parcimonieuse de la saisonnalité via des combinaisons de fonctions trigonométriques :
$$

S_t = \sum_{k=1}^K \left[ a_k \sin\left(\frac{2\pi k t}{P}\right) + b_k \cos\left(\frac{2\pi k t}{P}\right) \right]

$$
Cette formulation permet d'adapter la complexité du pattern saisonnier en ajustant l'ordre harmonique $K$. Les écosystèmes simples peuvent être adéquatement décrits par quelques harmoniques, tandis que les systèmes complexes nécessitent des ordres supérieurs.

### Points de rupture et changements structurels

Les points de rupture marquent des discontinuités dans le comportement de la série temporelle. Ces discontinuités peuvent affecter différentes composantes : changements de niveau, changements de pente, changements de variance, ou modifications de la structure saisonnière.

La détection des points de rupture présente des défis statistiques considérables. Les vraies ruptures doivent être distinguées des fluctuations stochastiques naturelles. Cette distinction nécessite des tests statistiques robustes tenant compte de la multiplicité des comparaisons.

Les modèles de régression par segments offrent un cadre flexible pour modéliser les séries avec ruptures :
$$

y_t = \sum_{j=1}^m \mathbf{1}(\tau_{j-1} < t \leq \tau_j) \left( \alpha_j + \beta_j t + \varepsilon_t \right)

$$
Cette formulation permet des changements simultanés de niveau et de pente aux points de rupture $\tau_j$.

### Modèles linéaires par morceaux

Les modèles linéaires par morceaux généralisent la régression linéaire simple en permettant des changements de régime. Chaque segment présente sa propre relation linéaire, créant une approximation flexible des relations non-linéaires.

Cette approche présente l'avantage de préserver l'interprétabilité des modèles linéaires tout en capturant des dynamiques complexes. La combinaison de multiples segments linéaires peut approximer virtuellement toute fonction continue, justifiant théoriquement la puissance de ces modèles.

L'estimation simultanée des points de rupture et des paramètres de régression constitue un problème d'optimisation non-linéaire complexe. Les méthodes bayésiennes offrent un cadre naturel pour cette estimation conjointe en traitant tous les paramètres comme des variables aléatoires.

## Sélection de modèles

### Le problème de la complexité

La sélection de modèles confronte le dilemme fondamental entre ajustement aux données et complexité du modèle. Des modèles complexes s'ajustent mieux aux données d'entraînement mais risquent le surajustement, dégradant les performances prédictives.

Ce compromis biais-variance sous-tend la plupart des critères de sélection. Les modèles simples présentent un biais élevé mais une variance faible, tandis que les modèles complexes montrent l'inverse. L'objectif consiste à trouver le point optimal de ce compromis.

### Critères d'information

Les critères d'information pénalisent la vraisemblance du modèle par sa complexité. Le critère d'information d'Akaike (AIC) s'exprime par :
$$

\text{AIC} = -2 \log L + 2k

$$
où $L$ représente la vraisemblance maximale et $k$ le nombre de paramètres. Cette pénalisation linéaire reflète l'augmentation attendue de la variance avec la complexité du modèle.

Le critère d'information bayésien (BIC) impose une pénalité plus sévère :
$$

\text{BIC} = -2 \log L + k \log n

$$
Cette pénalisation logarithmique en la taille d'échantillon $n$ favorise davantage les modèles parcimonieux, particulièrement pour de grands échantillons.

### Moyennage bayésien de modèles

Le moyennage bayésien de modèles (BMA) révolutionne l'approche traditionnelle de sélection en évitant le choix d'un modèle unique. Cette méthode combine les prédictions de multiples modèles pondérées par leurs probabilités a posteriori.

La prédiction BMA s'écrit :
$$

P(\tilde{y} | \text{données}) = \sum_{m=1}^M P(\tilde{y} | M_m, \text{données}) P(M_m | \text{données})

$$
Cette approche capture l'incertitude liée au choix du modèle, souvent négligée par les méthodes conventionnelles. L'incertitude totale se décompose en incertitude intra-modèle et inter-modèles.

Le BMA présente des avantages prédictifs démontrés empiriquement : il produit généralement des prédictions plus précises et mieux calibrées que la sélection d'un modèle unique. Cette supériorité découle de l'effet de "sagesse des foules" : les erreurs de modèles individuels tendent à se compenser mutuellement.

### Validation croisée

La validation croisée évalue les performances prédictives en utilisant des partitions indépendantes des données. Cette approche contourne les biais d'estimation liés à l'utilisation des mêmes données pour l'ajustement et l'évaluation.

La validation croisée leave-one-out (LOO-CV) estime l'erreur prédictive en laissant successivement chaque observation hors de l'ensemble d'entraînement :
$$

\text{LOO-CV} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_{-i})^2

$$
Cette méthode fournit une estimation quasi-non biaisée de l'erreur de généralisation mais peut s'avérer computationnellement coûteuse pour de grands échantillons.

## Modèles linéaires généralisés

### Extension du cadre linéaire

Les modèles linéaires généralisés (GLM) étendent la régression linéaire classique à des distributions d'erreur non-gaussiennes et des relations non-linéaires entre prédicteurs et variable réponse.

Cette généralisation s'appuie sur trois composantes : une distribution de la famille exponentielle pour la variable réponse, une fonction de lien reliant l'espérance à la combinaison linéaire des prédicteurs, et la combinaison linéaire elle-même.

La fonction de lien $g$ transforme l'espérance conditionnelle :
$$

g(\mathbb{E}[Y | X]) = X\beta

$$

Cette transformation permet de modéliser des relations non-linéaires tout en préservant la structure linéaire dans l'espace transformé.

### Estimation et inférence

L'estimation des paramètres dans les GLM s'effectue généralement par maximum de vraisemblance. L'algorithme IRLS (Iteratively Reweighted Least Squares) fournit une méthode computationnelle efficace basée sur des approximations successives de Newton-Raphson.

La matrice de design $X$ organise les variables explicatives selon une structure permettant l'application des méthodes d'algèbre linéaire standard. Cette organisation facilite l'estimation et l'inférence statistique.

Les propriétés asymptotiques des estimateurs du maximum de vraisemblance garantissent la normalité asymptotique et l'efficacité, justifiant l'utilisation de tests et intervalles de confiance basés sur la distribution normale.

### Applications aux séries temporelles

Les GLM s'appliquent naturellement à l'analyse des séries temporelles en incorporant le temps comme variable explicative. Cette approche permet de modéliser des tendances non-linéaires et des changements structurels.

L'extension aux modèles mixtes incorpore des effets aléatoires pour capturer la corrélation temporelle. Ces modèles offrent un compromis entre flexibilité et parcimonie, particulièrement adapté aux séries temporelles longues avec structures de dépendance complexes.

La régularisation via des prioris informatifs prévient le surajustement tout en préservant la flexibilité du modèle. Cette approche s'avère particulièrement pertinente pour les séries temporelles courtes où le nombre de paramètres peut approcher le nombre d'observations.
