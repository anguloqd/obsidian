## 01 // rappels sur régression linéaire

[01_rappels_sur_regression_lineaire_l1_regressionlineaire_intro_1.pdf](ressources/01_rappels_sur_regression_lineaire_l1_regressionlineaire_intro_1.pdf)

### Introduction au problème d'identification

L'identification des paramètres d'un modèle économétrique constitue un défi fondamental dans l'analyse causale. Cette problématique émerge lorsque nous cherchons à estimer l'effet causal d'une variable explicative sur une variable dépendante, mais que les données observées ne permettent pas de distinguer clairement cette relation causale des simples corrélations statistiques.

Le problème central réside dans la distinction entre variables explicatives exogènes et endogènes. Une variable exogène est déterminée indépendamment du phénomène étudié, tandis qu'une variable endogène est influencée par les mêmes facteurs non observés qui affectent la variable dépendante. Cette distinction est cruciale car elle détermine si les méthodes de régression standard peuvent produire des estimations fiables des effets causaux.

#### Le cadre théorique

Dans un modèle de régression linéaire standard de la forme $y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$ avec $E[u_i] \equiv 0$, l'identification du paramètre $b_0$ dépend entièrement de la nature de la relation entre la variable explicative $\tilde{x}_i$ et le terme d'erreur $u_i$. Le terme d'erreur contient tous les facteurs non observés qui influencent la variable dépendante mais ne sont pas explicitement modélisés.

L'estimateur des moindres carrés ordinaires (MCO) ne converge vers la vraie valeur du paramètre $b_0$ que si la covariance entre la variable explicative et le terme d'erreur est nulle : $\text{Cov}(\tilde{x}_i, u_i) = 0$. Cette condition, appelée exogénéité, garantit que la variable explicative n'est pas corrélée avec les facteurs non observés qui affectent la variable dépendante.

### L'effet de la formation sur le salaire

#### Contexte et objectifs

L'estimation de l'effet causal de l'éducation supérieure sur les salaires représente un problème emblématique en économétrie du travail, ayant valu le prix Nobel à James Heckman en 2000. L'objectif consiste à mesurer l'effet moyen d'une formation BAC+5 par rapport à un BAC seul sur les revenus salariaux, soit l'effet causal $\tilde{x}_i \rightarrow y_i$ où $\tilde{x}_i$ représente le niveau de formation et $y_i$ le salaire.

Cette mesure constitue un indicateur de l'efficacité économique de l'enseignement supérieur. Cependant, l'estimation directe de cet effet à partir d'un échantillon de jeunes salariés avec différents niveaux de formation pose des défis méthodologiques considérables.

#### Le problème d'identification

Dans le modèle $y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$, le terme d'erreur $u_i$ inclut tous les facteurs non observés qui influencent le salaire : les aptitudes individuelles, la motivation, les opportunités, les réseaux sociaux, et autres caractéristiques personnelles. Le problème surgit car ces mêmes facteurs non observés influencent également la décision de poursuivre des études supérieures.

Un individu doté d'aptitudes supérieures à la moyenne aura tendance à la fois à poursuivre des études BAC+5 et à obtenir un salaire élevé, indépendamment de l'effet causal de la formation. Cette double influence génère une corrélation positive entre $\tilde{x}_i$ et $u_i$, violant la condition d'exogénéité nécessaire à l'identification.

La covariance $\text{Cov}(\tilde{x}_i, y_i) = V(\tilde{x}_i) b_0 + \text{Cov}(\tilde{x}_i, u_i)$ révèle que la corrélation observée entre formation et salaire contient deux composantes : l'effet causal recherché $b_0$ et un biais de sélection $\text{Cov}(\tilde{x}_i, u_i)$ qui ne peut être séparé sans information supplémentaire.

#### Implications méthodologiques

L'estimateur MCO $\hat{b}_{MCO}^N$ converge vers $b_0 + V(\tilde{x}_i)^{-1} \text{Cov}(\tilde{x}_i, u_i)$ plutôt que vers le vrai paramètre $b_0$. Le biais $V(\tilde{x}_i)^{-1} \text{Cov}(\tilde{x}_i, u_i)$ ne peut être estimé puisque le terme d'erreur $u_i$ n'est pas observable. Cette situation illustre un problème d'identification fondamental : les données disponibles ne contiennent pas suffisamment d'information pour séparer l'effet causal de la corrélation spurieuse.

La résolution de ce problème nécessite l'introduction d'information supplémentaire, soit par l'utilisation d'instruments (variables qui affectent la formation mais pas directement le salaire), soit par des techniques de contrôle pour les variables omises, soit par l'exploitation de variations quasi-expérimentales.

### L'équilibre proie-prédateur

#### Le modèle écologique

L'analyse des écosystèmes proie-prédateur illustre un autre type de problème d'identification, celui de la simultanéité. L'objectif consiste à estimer le nombre de proies nécessaire à la survie d'un prédateur dans un écosystème en équilibre, soit le paramètre $b_0^{-1}$ dans le modèle $y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$ où $y_i$ représente le nombre de prédateurs et $\tilde{x}_i$ le nombre de proies dans l'écosystème $i$.

#### Le problème de simultanéité

Contrairement à l'exemple précédent où l'endogénéité résultait de facteurs omis, ici elle provient d'une causalité bidirectionnelle. Le nombre de proies détermine le nombre de prédateurs par un effet "nourriture disponible", mais simultanément, le nombre de prédateurs influence le nombre de proies par un effet "élimination par la chasse".

Cette détermination simultanée crée une corrélation négative entre $\tilde{x}_i$ et $u_i$ : un excès temporaire de prédateurs (contenu dans $u_i$) réduit le nombre de proies observé. La relation $\text{Cov}(\tilde{x}_i, u_i) < 0$ invalide l'hypothèse d'exogénéité et rend le paramètre $b_0$ non identifiable par les méthodes de régression standard.

Ce problème de simultanéité se retrouve fréquemment en économétrie, notamment dans l'analyse des marchés où prix et quantités se déterminent conjointement par l'équilibre de l'offre et de la demande.

### Formalisation générale du problème d'identification

#### Cadre théorique

Dans le modèle linéaire général $y_i = \mathbf{x}_i' \mathbf{a}_0 + u_i = \alpha_0 + \mathbf{\tilde{x}}_i' \mathbf{b}_0 + u_i$ avec $E[u_i] \equiv 0$, l'identification des paramètres repose sur l'estimation des covariances entre les variables observées. La covariance fondamentale s'écrit :

$$
\text{Cov}(y_i, \mathbf{\tilde{x}}_i) = V(\mathbf{\tilde{x}}_i) \mathbf{b}_0 + \text{Cov}(u_i, \mathbf{\tilde{x}}_i)
$$

Cette équation révèle que les covariances observables mélangent les paramètres d'intérêt $\mathbf{b}_0$ avec les covariances non observables entre variables explicatives et terme d'erreur.

#### Conditions d'identification

L'identification complète du vecteur de paramètres $\mathbf{a}_0 \equiv (\alpha_0, \mathbf{b}_0)$ requiert que toutes les variables explicatives soient exogènes, c'est-à-dire $\text{Cov}(u_i, \mathbf{\tilde{x}}_i) = \mathbf{0}$. Dans ce cas idéal, l'estimateur MCO converge vers les vraies valeurs des paramètres et constitue un modèle de régression proprement dit.

Inversement, si certaines variables explicatives sont endogènes ($\text{Cov}(\tilde{x}_{i,k}, u_i) \neq 0$ pour au moins un $k$), alors les paramètres ne sont plus identifiables par les méthodes standard. Cette situation nécessite des approches méthodologiques sophistiquées pour restaurer l'identification.

#### Définitions formelles

Une variable explicative $\tilde{x}_i$ est qualifiée d'**exogène** si $\text{Cov}(\tilde{x}_i, u_i) = 0$, garantissant que son effet peut être estimé de manière non biaisée. À l'inverse, elle est **endogène** si cette covariance est non nulle, créant un biais dans l'estimation.

Un **modèle de régression** est défini comme un modèle linéaire où toutes les variables explicatives sont exogènes, autorisant l'utilisation des méthodes de régression pour l'estimation des paramètres. Cette définition souligne que la validité d'une régression dépend fondamentalement des propriétés statistiques des données, non de la seule forme fonctionnelle du modèle.

### Convergence et propriétés asymptotiques

#### Analyse de la convergence

La démonstration formelle du problème d'identification repose sur l'analyse de la convergence de l'estimateur MCO. En utilisant la représentation $\hat{\mathbf{a}}_{MCO}^N = \mathbf{a}_0 + \left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{x}_i \mathbf{x}_i' \right)^{-1} \frac{1}{N} \sum_{i=1}^{N} \mathbf{x}_i u_i$, la loi des grands nombres implique que :

$$
\hat{\mathbf{a}}_{MCO}^N \xrightarrow{p}_{N \rightarrow +\infty} \mathbf{a}_0 + E[\mathbf{x}_i \mathbf{x}_i']^{-1} E[\mathbf{x}_i u_i]
$$

Le terme $E[\mathbf{x}_i u_i]$ détermine la présence ou l'absence de biais asymptotique. Si ce terme est nul (exogénéité), l'estimateur converge vers la vraie valeur. Sinon, il converge vers une valeur biaisée, révélant l'impossibilité d'identifier les vrais paramètres.

#### Techniques d'estimation avancées

Trois procédures fondamentales sous-tendent l'estimation économétrique moderne. La première concerne l'estimation d'espérances mathématiques par leurs contreparties empiriques, exploitant la loi des grands nombres : $\frac{1}{N} \sum_{i=1}^{N} \mathbf{W}_i \xrightarrow{p} E[\mathbf{W}_i]$.

La seconde généralise cette approche aux fonctions paramétrées : si $\hat{\boldsymbol{\beta}}_N \xrightarrow{p} \boldsymbol{\beta}_0$, alors $\frac{1}{N} \sum_{i=1}^{N} g(\mathbf{w}_i, \hat{\boldsymbol{\beta}}_N) \xrightarrow{p} E[g(\mathbf{w}_i, \boldsymbol{\beta}_0)]$.

La troisième exploite la continuité des transformations : si les estimateurs des composantes convergent, alors l'estimateur de toute fonction continue de ces composantes converge également vers la fonction des vraies valeurs.

### Comparaison avec les données expérimentales

#### L'avantage expérimental

Les données expérimentales, couramment utilisées en médecine pour évaluer l'efficacité des traitements, résolvent naturellement le problème d'identification. L'assignation aléatoire des sujets aux groupes traitement et contrôle garantit que $\text{Cov}(\tilde{x}_i, u_i) = 0$ par construction, puisque le statut de traitement devient indépendant de tous les facteurs non observés.

Cette randomisation permet l'utilisation directe des méthodes de régression ou même de simples comparaisons de moyennes pour identifier l'effet causal. L'expérience est précisément conçue pour simplifier l'analyse causale en éliminant les sources potentielles de biais.

#### Limitations dans les sciences sociales

En économie et sciences sociales, les données sont généralement observationnelles plutôt qu'expérimentales. Les individus choisissent leurs niveaux d'éducation, leur participation au marché du travail, leurs décisions de consommation selon leurs préférences et contraintes personnelles. Cette auto-sélection crée systématiquement des corrélations entre les décisions observées et les caractéristiques non observées.

L'impossibilité pratique, éthique ou financière de mener des expérimentations contrôlées dans de nombreux domaines économiques nécessite le développement de techniques sophistiquées pour traiter l'endogénéité. Ces méthodes tentent de reproduire les conditions expérimentales idéales à partir de données observationnelles, exploitant des sources de variation quasi-expérimentale ou des restrictions d'identification théoriques.

### Perspectives et extensions

#### Hétérogénéité des effets

Le modèle linéaire standard $y_i = \alpha_0 + b_0 \tilde{x}_i + u_i$ suppose implicitement que l'effet de la variable explicative est homogène dans la population, mesuré par le paramètre fixe $b_0$. En pratique, les effets peuvent varier selon les individus, motivant l'utilisation de modèles à paramètres aléatoires de la forme $y_i = \alpha_i + b_i \tilde{x}_i + u_i$.

Cette extension reconnaît que l'effet de l'éducation sur le salaire peut différer selon les aptitudes, motivations, ou circonstances individuelles. L'analyse et l'estimation de tels modèles, qui constituent l'objectif d'extensions avancées du cours, requièrent des techniques statistiques plus sophistiquées mais offrent une représentation plus réaliste des phénomènes étudiés.

#### Solutions au problème d'identification

Le problème d'identification étant fondamentalement un déficit d'information, sa résolution nécessite l'apport d'informations supplémentaires au modèle. Plusieurs stratégies peuvent être employées : l'utilisation de variables instrumentales qui affectent la variable explicative endogène sans influencer directement la variable dépendante, l'exploitation de discontinuités dans les règles d'attribution, ou l'utilisation de données de panel permettant le contrôle des effets fixes individuels.

Chacune de ces approches repose sur des hypothèses d'identification spécifiques qui doivent être soigneusement justifiées selon le contexte d'application. Le choix de la méthode appropriée dépend de la nature du problème d'endogénéité et des données disponibles, soulignant l'importance d'une compréhension approfondie des mécanismes générateurs des données dans l'analyse économétrique.
