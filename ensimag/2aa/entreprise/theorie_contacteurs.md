## Test de durée de vie des contacteurs - Guide pas à pas

### Vue d'ensemble du test

Ce test vise à valider la **durée de vie électrique** des contacteurs en les soumettant à des cycles répétés de fermeture/ouverture jusqu'à défaillance. L'objectif est de vérifier que la durée de vie réelle correspond aux spécifications commerciales annoncées.

### Configuration du test

- **4 contacteurs identiques** testés simultanément
- Cycles automatisés de fermeture/ouverture
- Surveillance continue de multiples variables
- Test jusqu'à défaillance complète ou dégradation inacceptable

### Variables mesurées et leur évolution

#### 1. Courant de commande (bobine)

**Ce qu'on mesure :** Le courant nécessaire pour alimenter la bobine électromagnétique

**Évolution attendue :**
- **Début :** Courant stable et nominal (ex: 100mA)
- **Pendant les cycles :** Augmentation progressive due à l'échauffement et l'usure
- **Fin de vie :** Pic de courant à la fermeture, puis chute (bobine endommagée)

**Pourquoi ça change :**
- Échauffement des bobines → résistance augmente
- Usure mécanique → effort magnétique plus important
- Dégradation de l'isolant → courts-circuits internes

#### 2. Résistance de contact (circuit principal)

**Ce qu'on mesure :** La résistance électrique entre les contacts principaux fermés

**Évolution attendue :**
- **Début :** Très faible résistance (quelques milliohms)
- **Pendant les cycles :** Augmentation progressive et irrégulière
- **Fin de vie :** Résistance très élevée ou instable

**Pourquoi ça change :**
- Formation d'oxyde sur les contacts
- Érosion du métal des contacts (arcs électriques)
- Dépôt de carbone et impuretés
- Déformation mécanique des surfaces de contact

#### 3. Temps de fermeture/ouverture

**Ce qu'on mesure :** Durée entre la commande et l'action mécanique effective

**Évolution attendue :**
- **Début :** Temps constants et rapides (quelques millisecondes)
- **Pendant les cycles :** Augmentation progressive des temps
- **Fin de vie :** Temps très longs ou fermeture/ouverture incomplète

**Pourquoi ça change :**
- Usure des ressorts (perte d'élasticité)
- Friction accrue dans les mécanismes
- Dépôts et corrosion sur les parties mobiles
- Désalignement mécanique progressif

#### 4. Force d'actionnement

**Ce qu'on mesure :** Force magnétique générée par la bobine

**Évolution attendue :**
- **Début :** Force constante et suffisante
- **Pendant les cycles :** Diminution progressive
- **Fin de vie :** Force insuffisante pour maintenir la fermeture

**Pourquoi ça change :**
- Désaimantation partielle du noyau magnétique
- Augmentation de l'entrefer (usure mécanique)
- Dégradation de la bobine

#### 5. Température

**Ce qu'on mesure :** Température des contacts, bobine et boîtier

**Évolution attendue :**
- **Début :** Échauffement modéré et stable
- **Pendant les cycles :** Température moyenne en augmentation
- **Fin de vie :** Pics de température très élevés

**Pourquoi ça change :**
- Résistance de contact croissante → effet Joule
- Arcs électriques plus fréquents/intenses
- Dégradation de l'évacuation thermique

### Déroulement d'un cycle typique

#### Phase 1 : Commande de fermeture

1. **Signal électrique** envoyé à la bobine
2. **Création du champ magnétique** → attraction de l'armature
3. **Mouvement mécanique** → rapprochement des contacts
4. **Contact physique** → passage du courant principal
5. **Stabilisation** → maintien en position fermée

#### Phase 2 : Commande d'ouverture

1. **Coupure du signal** de commande
2. **Disparition du champ magnétique**
3. **Action du ressort** → séparation des contacts
4. **Arc électrique momentané** (si courant présent)
5. **Position ouverte stable**

### Critères de fin de vie

Le test s'arrête quand :

- **Résistance de contact > seuil** (ex: >50 milliohms)
- **Temps d'actionnement > limite** (ex: >20ms)
- **Soudure des contacts** (impossible d'ouvrir)
- **Température excessive** (>limite thermique)
- **Nombre de cycles atteint** (objectif commercial)

### Analyse des résultats

#### Graphiques typiques observés :

- **Résistance** : courbe croissante avec paliers
- **Temps d'actionnement** : augmentation exponentielle
- **Température** : pics de plus en plus fréquents
- **Courant bobine** : oscillations puis divergence

#### Validation :

- Si les 4 contacteurs atteignent ou dépassent le nombre de cycles spécifié → **VALIDÉ**
- Si dégradation prématurée → **Analyse des causes** et amélioration du design

### Analogie informatique

Ce test ressemble à un **test de stress** en informatique :

- On soumet le système à une charge répétitive intensive
- On surveille les métriques de performance (CPU, mémoire, temps de réponse)
- On identifie le point de défaillance et les modes de dégradation
- On valide que les spécifications sont tenues dans les conditions réelles d'usage
