# 03 // mécanismes d’exécution

[systemes_cours3_2122.pdf](ressources/03_mecanismes_d’execution_systemes_cours3_2122.pdf)

# Mécanismes d'exécution - Processus et ordonnancement

## Concept de processus

La notion de processus constitue l'abstraction fondamentale des systèmes d'exploitation modernes. Un processus représente un programme en cours d'exécution, fournissant une vue virtualisée des ressources système. Cette abstraction permet de simuler des opérations concurrentes même sur une machine mono-processeur, créant l'illusion que plusieurs programmes s'exécutent simultanément.

Le processus offre une vision virtualisée de la mémoire et du processeur, permettant à chaque application de fonctionner comme si elle disposait de ressources dédiées. Cette virtualisation constitue le fondement de la multiprogrammation moderne.

## Principes de la multiprogrammation

### Exécution séquentielle

Sur un système mono-processeur, un seul processus s'exécute effectivement à un instant donné. L'illusion du parallélisme résulte du partage temporel du processeur entre différents processus selon des mécanismes d'ordonnancement sophistiqués.

L'exécution d'un processus ne s'effectue pas de manière continue. Le système doit pouvoir suspendre un processus, sauvegarder son état complet, puis le reprendre ultérieurement exactement au point d'interruption. Cette capacité nécessite des mécanismes précis de sauvegarde et de restauration du contexte d'exécution.

### Stratégies d'allocation

La répartition efficace du processeur entre les processus candidats constitue un enjeu majeur des systèmes d'exploitation. Les stratégies d'ordonnancement déterminent quel processus accède au processeur et pour quelle durée, influençant directement les performances perçues et l'équité du système.

## Architecture du processeur

### Modèle d'instructions

Le processeur exécute trois catégories principales d'instructions : les accès mémoire pour charger et stocker des données, les opérations arithmétiques et logiques pour les calculs, et les instructions de contrôle pour gérer les branchements et les boucles.

### Registres internes

L'**accumulateur** stocke les résultats des opérations de l'unité arithmétique et logique. Le **registre d'état (PSW - Program Status Word)** contient les indicateurs de condition tels que le bit zéro, la retenue arithmétique, le dépassement de capacité et le signe du résultat.

Le **registre d'instruction (IR)** contient l'instruction actuellement en cours d'exécution par le processeur. Le **compteur ordinal (PC - Program Counter)** stocke l'adresse de la prochaine instruction à charger depuis la mémoire.

Le **pointeur de pile (SP - Stack Pointer)** indique le prochain emplacement disponible dans la pile mémoire, zone critique pour la gestion des appels de fonctions et des variables locales.

## Structure mémoire d'un processus

### Organisation de l'espace d'adressage

L'image mémoire d'un processus s'organise en segments distincts ayant chacun un rôle spécifique. Cette organisation reflète les besoins différenciés du programme en termes de stockage et d'accès aux données.

Le **segment de code exécutable** contient les instructions du programme compilé, généralement en lecture seule pour des raisons de sécurité. Le **segment de données initialisées** stocke les variables globales ayant une valeur définie à la compilation.

Le **segment de données non initialisées (BSS - Block Started by Symbol)** réserve l'espace pour les variables globales déclarées mais non initialisées explicitement. Ce segment optimise l'utilisation de l'espace disque en ne stockant pas physiquement les zéros.

Le **tas (heap)** fournit l'espace pour l'allocation dynamique de mémoire via les fonctions comme `malloc()` en C. Cette zone croît vers les adresses hautes selon les besoins du programme.

La **pile (stack)** gère le stockage temporaire des paramètres de fonctions, des adresses de retour et des variables locales. Elle croît généralement vers les adresses basses, en direction opposée du tas.

### Exemple d'organisation mémoire

Un programme simple illustre cette répartition : les variables globales `nb` et `res` résident dans le segment de données initialisées. La variable locale `i` et le pointeur `tab` occupent la pile. L'allocation dynamique via `malloc()` crée un tableau dans le tas, démontrant l'utilisation conjointe de ces différentes zones mémoire.

## États et cycle de vie des processus

### Diagramme d'états

Un processus traverse plusieurs états au cours de son existence. L'état **nouveau** correspond à la phase de création et d'initialisation. L'état **prêt** indique que le processus attend l'allocation du processeur pour continuer son exécution.

L'état **actif** signifie que le processus utilise effectivement le processeur. L'état **bloqué** correspond aux périodes d'attente d'événements externes comme les entrées/sorties. L'état **terminé** marque la fin d'exécution du processus.

### Transitions d'états

L'**admission** fait passer un processus de l'état nouveau à l'état prêt. L'**allocation** du processeur transforme un processus prêt en processus actif. Une **interruption** peut suspendre un processus actif pour le remettre en état prêt.

Un processus actif devient **bloqué** lors d'une opération d'entrée/sortie ou en attente d'un événement. La **fin** de l'événement attendu ramène le processus de l'état bloqué à l'état prêt. La **terminaison** naturelle ou forcée conduit à l'état terminé.

## Bloc de contrôle de processus (PCB)

### Contenu du PCB

Le **Process Control Block** centralise toutes les informations nécessaires pour suspendre et reprendre l'exécution d'un processus. Cette structure de données critique contient l'identifiant unique du processus (PID), celui de son processus parent (PPID) et l'identifiant utilisateur (UID).

Le PCB sauvegarde les valeurs de tous les registres du processeur, incluant le compteur ordinal et le pointeur de pile. Il maintient une description complète de l'espace d'adressage virtuel du processus.

La liste des descripteurs de fichiers ouverts permet de reconstituer l'environnement d'entrée/sortie. Les informations d'ordonnancement (priorité, temps d'exécution) guident les décisions du planificateur.

### Mécanisme de sauvegarde

Le PCB se sauvegarde automatiquement à chaque transition d'un processus actif vers les états prêt ou bloqué. La restauration s'effectue lors du passage de l'état prêt vers l'état actif, reconstituant fidèlement le contexte d'exécution.

## Création des processus

### Mécanismes de lancement

La création d'un processus correspond au lancement d'un programme, déclenchable par interaction utilisateur (clic, commande shell) ou automatiquement au démarrage système. Cette opération système s'exécute en mode noyau avec tous les privilèges nécessaires.

### L'appel système fork()

Sous UNIX, l'appel système `fork()` constitue le mécanisme principal de création de processus. Cette primitive crée un processus fils par clonage complet du processus père, incluant l'image mémoire et l'état des registres.

Bien que les deux processus possèdent initialement une image mémoire identique, ils évoluent indépendamment sans partage de données. La valeur de retour de `fork()` permet de distinguer le père (PID du fils) du fils (valeur zéro).

### Hiérarchie des processus

Chaque processus possède un processus père (sauf le processus init), formant une structure arborescente. Cette hiérarchie influence la transmission des signaux, l'héritage des variables d'environnement et la gestion des ressources.

## Exemple pratique de fork()

L'exemple suivant illustre l'utilisation typique de `fork()` : après la création, le processus père attend la terminaison du fils via `wait()`, tandis que le fils remplace son image par un nouveau programme via `execlp()`.

```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    pid = fork();
    
    if (pid < 0) {
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if (pid == 0) {
        fprintf(stdout, "Je suis le fils");
        execlp("/bin/ls","ls",NULL);
    }
    else {
        fprintf(stdout, "Je suis le père");
        wait(NULL);
        printf("Fils terminé");
    }
    return 0;
}
```

## Terminaison des processus

### Modes de terminaison

Un processus se termine naturellement après l'exécution de sa dernière instruction ou par appel explicite à `exit(n)` où n représente le code de retour. La terminaison libère automatiquement toutes les ressources allouées au processus.

### Gestion des codes de retour

Le code de retour se transmet au processus père qui le récupère via l'appel système `wait()`. Entre la terminaison effective et la récupération du code par le père, le processus devient un **zombie** : il ne possède plus d'image mémoire mais conserve son PCB pour stocker le code de retour.

## Gestion de l'exécution

### Commutation de contexte

Le **dispatcher** assure la commutation entre processus, sauvegardant le PCB du processus interrompu et chargeant celui du processus à exécuter. Cette opération s'effectue généralement par interruption matérielle.

La commutation introduit une latence système appelée **dispatcher latency**, représentant le temps nécessaire pour effectuer le changement de contexte.

### Files d'attente

Le système maintient plusieurs files d'attente pour organiser l'accès aux ressources : file des processus prêts pour le processeur, files d'attente pour les périphériques d'entrée/sortie. Ces structures de données permettent une gestion ordonnée et équitable des ressources.

### Ordonnancement

Le **scheduler** sélectionne le prochain processus à exécuter parmi ceux en état prêt. Cette décision critique influence directement les performances perçues et l'équité du système.

## Stratégies d'ordonnancement

### Ordonnancement non préemptif

Les algorithmes non préemptifs laissent un processus actif jusqu'à sa terminaison, son blocage volontaire ou son abandon explicite du processeur. Cette approche convient aux systèmes de traitement par lots (batch) où l'interactivité n'est pas critique.

L'algorithme **Premier Arrivé Premier Servi (FCFS)** exécute les processus dans leur ordre d'arrivée. Simple à implémenter, il peut pénaliser les processus courts placés après un processus long.

L'algorithme **Plus Court d'Abord (Shortest Job First)** privilégie les processus ayant le temps d'exécution le plus court. Théoriquement optimal, il nécessite une connaissance a priori des durées d'exécution, rarement disponible en pratique.

### Ordonnancement préemptif

Les algorithmes préemptifs limitent le temps d'exécution continu d'un processus, nécessitant une interruption d'horloge périodique. Cette approche garantit une meilleure réactivité dans les systèmes interactifs.

Le **Tourniquet (Round Robin)** constitue la version préemptive de FCFS, attribuant à chaque processus un quantum de temps (typiquement 10-100 millisecondes) avant rotation vers le processus suivant.

### Ordonnancement par priorité

L'**ordonnancement à priorité pure** sélectionne toujours le processus de priorité la plus élevée. Pour éviter la monopolisation du processeur, la priorité peut décroître à chaque interruption d'horloge, forçant la rotation après un temps donné.

### Approches hybrides

Les **files d'attente multi-niveau** combinent tourniquet et priorité, créant plusieurs files avec des priorités différentes. Chaque file peut utiliser son propre algorithme d'ordonnancement, permettant une adaptation fine aux caractéristiques des différents types de processus.

## Objectifs des algorithmes d'ordonnancement

### Équité et performance

L'équité entre processus constitue un objectif fondamental, évitant qu'un processus monopolise indûment les ressources. La maximisation de l'utilisation du processeur et du rendement (tâches terminées par unité de temps) vise l'efficacité globale du système.

### Optimisation des temps de réponse

La minimisation des temps d'exécution des tâches, des temps d'attente en état prêt, et des temps de réponse (particulièrement crucial pour les systèmes interactifs) détermine la qualité de l'expérience utilisateur. Ces métriques guident le choix et le paramétrage des algorithmes d'ordonnancement selon le contexte d'utilisation.