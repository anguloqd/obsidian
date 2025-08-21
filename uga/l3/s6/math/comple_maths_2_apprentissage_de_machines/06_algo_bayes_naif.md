# 06 // algo : bayes naïf

[lecture_naive_bayes_2.pdf](ressources/06_algo_bayes_naif_lecture_naive_bayes_2.pdf)

[bayes_usecase.pdf](ressources/06_algo_bayes_naif_bayes_usecase.pdf)

# Classification Naïve de Bayes

## Introduction aux Classificateurs Probabilistes

Les classificateurs probabilistes constituent une approche fondamentale en apprentissage automatique qui diffère des méthodes de classification traditionnelles par leur capacité à quantifier l'incertitude. Plutôt que d'assigner directement une classe à une observation donnée, ces algorithmes fournissent une distribution de probabilité sur l'ensemble des classes possibles.

Formellement, étant donné un vecteur d'observation $x = (x_1, x_2, ..., x_n) \in \mathbb{R}^n$ et un ensemble de labels $y_i \in Y$, un classificateur probabiliste estime $P(y_i|x)$ pour chaque classe $y_i \in Y$ et assigne l'étiquette la plus probable à l'observation $x$.

Cette approche probabiliste présente plusieurs avantages substantiels par rapport aux méthodes de classification binaire. Elle permet notamment d'évaluer la confiance dans les prédictions, de gérer l'incertitude inhérente aux données, et de prendre des décisions optimales en tenant compte des coûts associés aux différents types d'erreurs.

Les modèles probabilistes natifs incluent la régression logistique, certains sous-types de réseaux de neurones, et les classificateurs bayésiens. Les modèles non-probabilistes peuvent également être adaptés pour fournir des sorties probabilistes, notamment les machines à vecteurs de support (SVM) et les arbres de décision.

## Principe du Classificateur de Bayes

### Fondements Théoriques

Le classificateur naïf de Bayes repose sur l'application du théorème de Bayes avec une hypothèse d'indépendance conditionnelle entre les caractéristiques. Cette méthode probabiliste part du principe que chaque caractéristique contribue de manière indépendante à la probabilité de la classe, une simplification qui justifie l'adjectif "naïf" mais qui s'avère remarquablement efficace en pratique.

L'hypothèse fondamentale stipule que les caractéristiques sont conditionnellement indépendantes étant donnée la classe. Par exemple, dans un système de prédiction de race de chien, la taille et le poids du chien contribuent indépendamment à la détermination de sa race, une fois celle-ci connue.

### Cadre Mathématique

L'objectif principal consiste à estimer, pour chaque label $y_i \in Y$, la probabilité $P(y_i|x)$ qui représente la probabilité d'appartenir à la classe $y_i$ étant donnés les attributs observés.

Lorsque la dimension $n$ du vecteur de caractéristiques est importante, le calcul direct de cette probabilité devient informatiquement intraitable. La solution réside dans l'application de la définition des probabilités conditionnelles :

$$P(y_i|x) = \frac{P(y_i, x)}{P(x)}$$

Puisque $P(x)$ demeure constante pour une observation donnée $x$, il suffit de déterminer $P(y_i, x)$ pour comparer les probabilités des différentes classes.

En appliquant itérativement la définition des probabilités conditionnelles, nous obtenons :

$$P(y_i, x) = P(x_1, x_2, ..., x_n, y_i)$$
$$= P(x_1|x_2, x_3, ..., y_i) \times P(x_2, x_4, ..., y_i)$$
$$= P(x_1|x_2, x_3, ..., y_i) \times P(x_2|x_3, x_4, ..., y_i) \times P(x_3, x_4, ..., y_i)$$
$$= \ldots$$
$$= P(x_1|x_2, x_3, ..., y_i) \times P(x_2|x_3, x_4, ..., y_i) \times \ldots \times P(x_n|y_i) \times P(y_i)$$

### Hypothèse d'Indépendance Conditionnelle

L'indépendance conditionnelle décrit les situations où une observation devient non-informative en présence d'autres informations. Si $A$ représente l'hypothèse et $B$ et $C$ les observations, alors $P(A|B,C) = P(A|C)$ lorsque $B$ n'apporte aucune information supplémentaire sur $A$ une fois $C$ connue.

En appliquant cette hypothèse aux caractéristiques $x_i$, nous supposons que chaque caractéristique ne dépend que de la classe $y_i$ :

$$P(x_1|x_2, x_3, ..., y_i) = P(x_1|y_i)$$

Cette simplification transforme l'expression complexe en :

$$P(y_i, x) = P(y_i) \prod_{j=1}^{n} P(x_j|y_i)$$

Par conséquent :

$$P(y_i|x) \propto P(y_i) \prod_{j=1}^{n} P(x_j|y_i)$$

La classe prédite correspond au maximum de cette expression :

$$\hat{y} = \arg\max_{i=1,...,k} \left(P(y_i) \prod_{j=1}^{n} P(x_j|y_i)\right)$$

### Estimation des Paramètres

L'implémentation du classificateur naïf de Bayes nécessite l'estimation de deux types de termes :

**Probabilités a priori $P(y_i)$** : Ces probabilités peuvent être estimées soit en supposant l'équiprobabilité des classes, soit en utilisant la fréquence d'occurrence de chaque classe dans l'ensemble d'entraînement.

**Probabilités conditionnelles $P(x_j|y_i)$** : L'estimation de ces termes dépend de la nature des variables :

Pour les **variables continues** ($x_j \in \mathbb{R}$), l'approche standard suppose une distribution gaussienne des valeurs au sein de chaque classe, paramétrée par une moyenne $\mu_i$ et une variance $\sigma_i^2$ :

$$f(v|y_i) = \frac{1}{\sqrt{2\pi\sigma_i^2}} e^{-\frac{(v-\mu_i)^2}{2\sigma_i^2}}$$

Pour les **variables catégorielles** ($x_j \in \{0, ..., K\}$), la probabilité s'estime comme la proportion des valeurs dans la classe :

$$P(x = j|y_i) = \frac{N_{ji}}{N_i}$$

où $N_{ji}$ représente le nombre d'occurrences de la valeur $j$ dans la classe $i$, et $N_i$ le nombre total d'exemples dans la classe $i$.

## Exemple Pratique : Prédiction de Race de Chien

### Données d'Entraînement

Considérons un ensemble de données pour la classification de chiens selon leur caractère légendaire :

| Hauteur | Poids | Queue | Label          |
| ------- | ----- | ----- | -------------- |
| 45      | 30    | 0     | Légendaire     |
| 30      | 25    | 1     | Légendaire     |
| 40      | 35    | 1     | Légendaire     |
| 20      | 15    | 0     | Non légendaire |
| 22      | 18    | 1     | Non légendaire |
| 25      | 20    | 1     | Non légendaire |

L'individu à classifier présente les caractéristiques suivantes : Hauteur = 25, Poids = 31, Queue = 1.

### Entraînement du Modèle

L'entraînement consiste à calculer les estimateurs statistiques pour chaque population.

**Population légendaire** :
- Hauteur : Moyenne = 38.33, Variance = 38.89
- Poids : Moyenne = 30, Variance = 16.67

**Population non légendaire** :
- Hauteur : Moyenne = 22.33, Variance = 4.22
- Poids : Moyenne = 17.66, Variance = 4.22

### Calcul des Probabilités

**Classification comme "Légendaire"** :

$$P(\text{légendaire}|\text{hauteur}=25, \text{poids}=31, \text{queue}=1)$$
$$\propto P(\text{légendaire}) \times P(\text{hauteur}=25|\text{légendaire})$$
$$\times P(\text{poids}=31|\text{légendaire}) \times P(\text{queue}=1|\text{légendaire})$$

Calculs détaillés :
- $P(\text{légendaire}) = \frac{1}{2}$
- $P(\text{hauteur}=25|\text{légendaire}) = \frac{1}{\sqrt{2\pi \times 38.89}} e^{-\frac{(25-38.33)^2}{2 \times 38.89}} = 0.006$
- $P(\text{poids}=31|\text{légendaire}) = \frac{1}{\sqrt{2\pi \times 16.67}} e^{-\frac{(31-30)^2}{2 \times 16.67}} = 0.09$
- $P(\text{queue}=1|\text{légendaire}) = \frac{2}{3}$

Résultat : $P(\text{légendaire}|\text{données}) \propto 0.00017$

**Classification comme "Non légendaire"** :

$$P(\text{non-légendaire}|\text{hauteur}=25, \text{poids}=31, \text{queue}=1)$$
$$\propto P(\text{non-légendaire}) \times P(\text{hauteur}=25|\text{non-légendaire})$$
$$\times P(\text{poids}=31|\text{non-légendaire}) \times P(\text{queue}=1|\text{non-légendaire})$$

Calculs détaillés :
- $P(\text{non-légendaire}) = \frac{1}{2}$
- $P(\text{hauteur}=25|\text{non-légendaire}) = \frac{1}{\sqrt{2\pi \times 4.22}} e^{-\frac{(25-22.33)^2}{2 \times 4.22}} = 0.08$
- $P(\text{poids}=31|\text{non-légendaire}) = \frac{1}{\sqrt{2\pi \times 4.22}} e^{-\frac{(31-17.66)^2}{2 \times 4.22}} = 1.31 \times 10^{-11}$
- $P(\text{queue}=1|\text{non-légendaire}) = \frac{2}{3}$

Résultat : $P(\text{non-légendaire}|\text{données}) \propto 7 \times 10^{-13}$

La probabilité pour la classe "Légendaire" étant significativement plus élevée, l'individu serait classifié comme légendaire.

## Hyperparamètres

Le classificateur naïf de Bayes se distingue par sa simplicité paramétrique. Les principaux hyperparamètres concernent :

- **Type de distribution** : Le choix de la loi de probabilité pour modéliser les caractéristiques continues (gaussienne, multinomiale, etc.)
- **Lissage** : L'application de techniques de lissage (comme le lissage de Laplace) pour éviter les probabilités nulles
- **Sélection des caractéristiques** : La détermination des variables les plus pertinentes pour la classification

Cette parcimonie en hyperparamètres constitue un avantage notable, réduisant le risque de sur-apprentissage et simplifiant la validation croisée.

## Avantages et Limitations

### Limitations

**Hypothèse d'indépendance forte** : L'assumption d'indépendance conditionnelle entre les caractéristiques constitue une simplification souvent irréaliste. Paradoxalement, cette limitation théorique n'empêche pas le classificateur naïf de Bayes d'obtenir de bonnes performances pratiques dans de nombreux domaines.

**Gestion des valeurs inconnues** : L'algorithme ne peut pas classifier des instances présentant des combinaisons de caractéristiques non observées dans l'ensemble d'entraînement, assignant automatiquement une probabilité nulle à de tels cas (sauf dans le cas d'équiprobabilité artificielle).

### Avantages

**Extension naturelle au multi-classe** : Contrairement à certains algorithmes binaires nécessitant des stratégies spécifiques (un-contre-tous, un-contre-un), le classificateur naïf de Bayes gère intrinsèquement la classification multi-classe.

**Traitement des variables catégorielles** : L'algorithme manipule naturellement les variables catégorielles sans nécessiter d'encodage complexe ou de transformations préalables.

**Efficacité computationnelle** : La simplicité du modèle permet un entraînement et une prédiction rapides, particulièrement avantageux pour les grands ensembles de données.

**Robustesse au sur-apprentissage** : La parcimonie du modèle limite les risques de sur-ajustement, particulièrement bénéfique lorsque la taille de l'ensemble d'entraînement est limitée.

## Algorithmes Connexes

### Régression Logistique

La régression logistique représente un autre classificateur probabiliste majeur où la distribution de probabilité s'exprime comme le logit de la combinaison linéaire des caractéristiques. Contrairement au classificateur naïf de Bayes, elle ne suppose pas l'indépendance des variables et modélise directement la probabilité conditionnelle.

### Réseaux de Neurones avec Softmax

L'utilisation de la fonction softmax comme couche d'activation finale dans les réseaux de neurones transforme les sorties en distribution de probabilité. Cette fonction calcule $K$ probabilités proportionnelles aux exponentielles des valeurs d'entrée, garantissant que la somme des probabilités égale l'unité.

La fonction softmax s'exprime comme :

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

Cette approche combine la puissance représentationnelle des réseaux de neurones avec la capacité de quantification de l'incertitude des modèles probabilistes.