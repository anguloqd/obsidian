## 04 // gestion de ressources

[systemes_cours4_1819.pdf](ressources/04_gestion_de_ressources_systemes_cours4_1819.pdf)

## Gestion des ressources système

### Classification des ressources

Les systèmes informatiques gèrent différents types de ressources selon leur nature et leurs modalités d'accès. Cette classification permet de comprendre les mécanismes de partage et les contraintes associées à chaque type de ressource.

#### Ressources partageables simultanément

Certaines ressources peuvent être utilisées par plusieurs processus au même moment sans conflit. Le code réentrant constitue l'exemple le plus caractéristique de ce type de ressource. Un programme réentrant est conçu dès sa conception pour être exécuté simultanément par plusieurs processus sans altération de son comportement. Les fichiers ou zones mémoire en lecture seule appartiennent également à cette catégorie, ainsi que les périphériques partageables comme les disques.

#### Ressources banalisées

Les ressources banalisées forment un ensemble de ressources de même type pouvant être utilisées indifféremment les unes des autres. Cette équivalence fonctionnelle permet une allocation flexible selon la disponibilité. Les tampons mémoires (buffers), les dérouleurs de bande et les imprimantes identiques illustrent ce concept de banalisation des ressources.

#### Ressources réutilisables séquentiellement

Cette catégorie regroupe les ressources critiques du système qui ne peuvent être utilisées que par un seul processus à la fois. Le code non réentrant, toute zone mémoire en lecture/écriture, le processeur et les périphériques séquentiels comme les imprimantes ou dérouleurs de bande nécessitent un accès exclusif. Ces ressources constituent le cœur des problématiques de synchronisation.

#### Ressources virtuelles et réquisitionnables

Les systèmes modernes introduisent la notion de virtualisation des ressources, permettant de créer des abstractions de ressources physiques. Le disque virtuel et la mémoire virtuelle exemplifient cette approche. Certaines ressources peuvent également être réquisitionnables, c'est-à-dire reprises par le système d'exploitation selon les besoins.

### Problématique du partage de ressources

#### Exemple fondamental

Le partage d'une donnée en mémoire illustre parfaitement les défis du partage de ressources. Lorsque deux tâches A et B s'exécutent simultanément et doivent modifier la même donnée, chaque tâche doit effectuer trois opérations séquentielles : lire la donnée actuelle, calculer sa nouvelle valeur, puis mémoriser cette nouvelle valeur. L'exécution simultanée de ces tâches peut perturber les calculs et produire des résultats incohérents.

#### Sections critiques

Une section critique désigne une portion de code où un processus accède à une ressource partagée. L'accès à cette section doit être contrôlé pour éviter les conflits entre processus concurrents.

### Exclusion mutuelle

L'exclusion mutuelle constitue le mécanisme fondamental garantissant qu'une seule tâche peut accéder à une ressource critique à un moment donné.

#### Propriétés fondamentales

L'exclusion mutuelle repose sur quatre propriétés essentielles :

1. Une section critique ne peut être occupée que par une seule tâche à la fois, empêchant deux processus d'être simultanément dans la même section critique.

2. Aucune hypothèse ne doit être formulée sur la vitesse relative des tâches ni sur leur nombre, garantissant la robustesse du mécanisme.

3. Une tâche suspendue en dehors d'une section critique ne doit jamais empêcher une autre d'y entrer, évitant les situations d'interblocage.

4. Toute tâche doit attendre un temps fini devant une section critique, prévenant les phénomènes de famine.

#### Verrouillage par variable

Les processus peuvent partager des variables pour synchroniser leurs actions. Pour entrer dans une section critique, chaque processus consulte une variable booléenne unique, initialisée à faux, indiquant l'état d'occupation de la ressource critique. Si la variable vaut faux, le processus la positionne à vrai et accède à la section critique. Si le verrou est à vrai, le processus attend que la variable redevienne fausse.

### Méthodes d'attente active

#### Solution triviale

La solution la plus simple consiste à utiliser une variable de verrou partagée. Cependant, cette approche ne garantit pas l'exclusion mutuelle car deux processus peuvent lire simultanément la variable avant qu'elle ne soit modifiée.

#### Solution avec tableau de booléens

Une amélioration utilise un tableau de booléens indiquant quels processus souhaitent entrer en section critique :

```
Entrée_SC(Consulté i : entier)
    demande[i] ← VRAI
    tantque demande[3-i] faire
    ftq;

Sortie_SC(Consulté i : entier)
    demande[i] ← FAUX

Init_SC()
    demande[1] ← FAUX
    demande[2] ← FAUX
```

Cette solution assure l'exclusion mutuelle mais présente un risque d'interblocage si les deux processus positionnent simultanément leur indicateur.

#### Solution avec variable d'alternance

L'utilisation d'une variable entière `tour` permet d'assurer l'alternance :

```
Entrée_SC(Consulté i : entier)
    tantque (tour = 3-i) faire
    début fin;

Sortie_SC(Consulté i : entier)
    tour ← 3-i

Init_SC()
    tour ← 1
```

Cette approche garantit l'exclusion mutuelle mais peut provoquer des situations de famine si un processus ne souhaite plus accéder à la section critique.

#### Solution de Dekker-Peterson

L'algorithme de Dekker-Peterson combine les deux approches précédentes :

```
Entrée_SC(Consulté i : entier)
    demande[i] ← vrai
    tour ← 3-i
    tantque demande[3-i] et tour ≠ i
    début fin;

Sortie_SC(Consulté i : entier)
    demande[i] ← FAUX

Init_SC()
    demande[1] ← FAUX
    demande[2] ← FAUX
```

Cette solution résout les problèmes d'interblocage et de famine des méthodes précédentes.

### Mécanismes matériels

#### Mono-processeur

Sur les systèmes mono-processeur, l'exclusion mutuelle peut être réalisée par masquage des interruptions. L'entrée en section critique active le masquage, tandis que la sortie le désactive.

#### Multiprocesseurs

Les systèmes multiprocesseurs nécessitent des instructions atomiques spécialisées comme Test and Set Lock :

```
fonction Test_And_Set (Modifié occupée : booléen) → booléen
    booléen TAS
    TAS ← occupée
    occupée ← VRAI
    renvoyer(TAS)
```

Cette instruction atomique permet de tester et modifier une variable en une seule opération indivisible.

### Solutions à base d'attente passive

#### Problématique de l'attente active

Les solutions précédentes présentent un inconvénient majeur : le gaspillage de temps processeur dû à l'attente active. Les processus consomment inutilement des cycles en surveillant continuellement les conditions d'accès.

#### Principe de l'attente passive

L'attente passive résout ce problème en endormant les processus lorsque la section critique est verrouillée et en les réveillant lors de sa libération. Cette approche utilise des verrous sophistiqués.

#### Classe Verrou

```
Classe verrou
    privé ouvert : booléen;
    privé attente : liste de tâches;

public procédure init()
début
    ouvert ← vrai;
    attente ← vide;
fin init

public procédure verrouiller()
début
    si ouvert alors
        ouvert ← faux
    sinon
        Ajouter la tâche dans la liste attente
        dormir
    finsi;
fin verrouiller;

public procédure déverrouiller()
début
    si attente ≠ vide alors
        Sortir la première tâche de attente,
        La réveiller
    sinon
        ouvert ← vrai
    finsi;
fin déverrouiller;
```

#### Exemple d'utilisation : voie unique

```
Tâche TrainGauche (voie : verrou);
début
    rouler;
    voie.verrouiller();
    Passer;
    voie.déverrouiller();
    rouler;
fin TrainGauche;

Tâche TrainDroit (voie : verrou);
début
    rouler;
    voie.verrouiller();
    Passer;
    voie.déverrouiller();
    rouler;
fin TrainDroit;
```

### Sémaphores de Dijkstra

#### Concept fondamental

Les sémaphores constituent un mécanisme de synchronisation entre processus introduit par Dijkstra. Un sémaphore S est une variable entière manipulable uniquement par deux opérations atomiques : P (proberen, "tester") et V (verhogen, "incrémenter"), également appelées acquire et release.

#### Opérations sur les sémaphores

- `acquire(S)` : $S \leftarrow (S - 1)$. Si $S < 0$, le processus est mis en attente ; sinon, l'exécution se poursuit.

- `release(S)` : $S \leftarrow (S + 1)$ et réveil d'un processus en attente.

L'opération `acquire(S)` correspond à une tentative de franchissement. En l'absence de jeton pour la section critique, le processus attend ; sinon, il prend un jeton et entre dans la section critique. Chaque dépôt de jeton via `release(S)` autorise un passage, permettant le dépôt anticipé de jetons.

#### Implémentation de la classe Sémaphore

```
Classe Sémaphore
    privé val : entier;
    privé attente : liste de tâches;

public procédure init_sémaphore(consulté v : entier);
début
    val ← v
    attente ← vide
fin init_sémaphore

public procédure acquire()
début
    val ← val - 1
    si val < 0 alors
        Ajouter la tâche dans la liste attente
        dormir
    finsi
fin acquire

public procédure release();
début
    val ← val + 1;
    si val ≤ 0 alors
        Sortir la première tâche de attente
        La réveiller
    finsi;
fin release;
```

#### Exemple d'application : voie unique

```
Tâche TrainGauche (modifié voie : sémaphore);
début
    rouler;
    voie.acquire();
    Passer;
    voie.release();
    rouler;
fin TrainGauche;

Tâche TrainDroit (modifié voie : sémaphore);
début
    rouler;
    voie.acquire();
    Passer;
    voie.release();
    rouler;
fin TrainDroit;

voie.init_sémaphore(1)
```

### Difficultés liées au partage de ressources

#### Interblocage (deadlock)

L'interblocage constitue une situation critique où plusieurs processus s'attendent mutuellement, créant une impasse. Un exemple typique avec des sémaphores :

```
Tâche A                    Tâche B
mutex1.acquire() (1a)      mutex2.acquire() (1b)
mutex2.acquire() (2a)      mutex1.acquire() (2b)
...                        ...
mutex2.release()           mutex1.release()
mutex1.release()           mutex2.release()
```

L'ordre d'exécution (1a) (1b) (2a) (2b) crée un interblocage.

#### Conditions nécessaires à l'interblocage

L'interblocage nécessite quatre conditions simultanées :

1. Existence de ressources non partageables
2. Processus conservant des ressources déjà obtenues tout en attendant d'autres ressources
3. Demandes de ressources bloquantes sans possibilité de préemption
4. Existence d'une chaîne circulaire de processus où chacun réclame les ressources possédées par le suivant

### Solutions au problème de l'interblocage

#### Prévention

##### Allocation globale des ressources

Cette méthode supprime la condition 2 en allouant toutes les ressources nécessaires à une tâche avant son exécution. Cependant, elle provoque une immobilisation non productive des ressources et une perte significative du parallélisme.

##### Méthode des classes ordonnées

Les ressources sont organisées en classes $C_0 … C_M$. L'allocation des ressources de la classe $k$ n'est autorisée que si la tâche possède déjà les ressources de la classe $k-1$. L'ordre d'allocation identique pour toutes les tâches élimine la condition 4 en supprimant les cycles dans les besoins et allocations.

##### Algorithme du banquier

Cet algorithme repose sur trois principes :

- Annonce préalable des besoins par les processus
- Réévaluation du risque à chaque allocation de manière complètement centralisée
- Maintien d'un état fiable permettant l'exécution sans interblocage même dans l'hypothèse la plus pessimiste

#### Détection

La détection d'interblocage utilise l'algorithme déterminant si un état est fiable ou non, permettant d'identifier les situations problématiques avant qu'elles ne se produisent.

#### Guérison

La guérison nécessite un retour à un état fiable par deux méthodes principales :

1. Destruction successive des tâches interbloquées jusqu'à obtention d'un état fiable
2. Sauvegarde périodique de l'état des tâches dans des états fiables, créant des points de reprise

#### Approche pratique

En pratique, les systèmes évitent généralement la détection et la guérison. Ils organisent plutôt le système pour limiter les risques au maximum et renvoient le programmeur à ses responsabilités. Tous les appels système susceptibles de bloquer une tâche sont implémentés avec des délais d'attente au-delà desquels l'appel retourne un code d'erreur, évitant les blocages indéfinis.
