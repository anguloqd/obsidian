## 00 // tps

[cmdes_unix_desc.pdf](ressources/00_tps_cmdes_unix_desc.pdf)

[systemes_tp1_2324.pdf](ressources/00_tps_systemes_tp1_2324.pdf)

[systemes_tp2_2223.pdf](ressources/00_tps_systemes_tp2_2223.pdf)

[systemes_tp3_1819.pdf](ressources/00_tps_systemes_tp3_1819.pdf)

[systemes_tp4_1819.pdf](ressources/00_tps_systemes_tp4_1819.pdf)

## Travaux pratiques - Systèmes d'exploitation

### TP1 - Gestion de fichiers et commandes Unix

#### Gestion de fichiers et répertoires

La manipulation des fichiers et répertoires sous Unix s'effectue par un ensemble de commandes fondamentales permettant la création, la copie, le déplacement et la suppression d'éléments du système de fichiers.

**Création et navigation dans les répertoires :**
- `mkdir bin` : création d'un répertoire nommé "bin"
- `cp -r /media/commun/shell .` : copie récursive d'un répertoire avec préservation de l'arborescence
- `scp -pr login@server:/path .` : copie sécurisée via SSH avec préservation des permissions
- `cd shell`, `cd noms` : changement vers un répertoire spécifié
- `cd ..` : remontée vers le répertoire parent
- `cd ~`, `cd`, `cd $HOME` : retour au répertoire personnel

**Suppression d'éléments :**
- `rm -r ./shell/noms/*` : suppression récursive de tous les fichiers d'un répertoire
- `rmdir ./shell/noms` : suppression d'un répertoire vide

#### Manipulation de fichiers

Les opérations sur les fichiers incluent l'affichage de contenu, la création de copies et la redirection des flux d'entrée/sortie.

**Affichage et création :**
- `cat bravo.c` : affichage du contenu d'un fichier
- `cat m1 m2` : concaténation et affichage de plusieurs fichiers
- `cat m1 > m1bis` : création d'une copie par redirection de sortie
- `cat > toto` : création interactive d'un fichier (terminaison par Ctrl-D)

**Analyse du contenu :**
- `od -c bravo.c` : affichage en représentation caractère
- `od -x bravo.c` : affichage en représentation hexadécimale

**Redirections :**
- `./bravo > out` : redirection de la sortie standard vers un fichier
- `./bravo >> out` : ajout à un fichier existant
- `ls titi 2> err` : redirection de la sortie d'erreur
- `ls titi * > out` : redirection de la sortie standard avec expansion de motifs

#### Listing et filtrage de fichiers

Les commandes de listing permettent d'explorer le contenu des répertoires avec des critères de filtrage sophistiqués utilisant les métacaractères du shell.

**Commandes de base :**
- `ls -l noms` : listing détaillé avec informations sur la taille
- `ls *.c` : affichage des fichiers avec extension .c
- `ls [ag]*`, `ls a* g*` : fichiers commençant par 'a' ou 'g'
- `ls a*1` : fichiers commençant par 'a' et se terminant par '1'
- `ls ???` : fichiers avec exactement trois caractères
- `ls ~`, `ls $HOME` : contenu du répertoire personnel

#### Compilation et exécution

Le processus de compilation transforme le code source en programme exécutable.

**Méthodes de compilation :**
- `cc bravo.c` suivi de `./a.out` : compilation avec nom par défaut
- `cc bravo.c -o bravo` suivi de `./bravo` : compilation avec nom spécifié
- `cc boucle.c -o boucle` suivi de `./boucle` : exemple avec un autre programme

#### Environnement et processus

La gestion de l'environnement système et des processus constitue un aspect fondamental de l'administration Unix.

**Variables d'environnement :**
- `env` : affichage des variables globales
- `set` : affichage des variables locales et globales
- `export PS1="Nouveau prompt > "` : modification du prompt
- `echo 'echo -e "\\nBonjour\\n"' >> ~/.bashrc` : ajout de commandes au démarrage

**Gestion des processus :**
- `ps`, `ps -ef`, `ps -fU $LOGNAME` : liste des processus actifs
- `xterm -T nouveau &` : ouverture d'un terminal en arrière-plan
- `kill -KILL <PID>` : arrêt forcé d'un processus
- `ssh login@server` : connexion à un serveur distant

#### Commandes utilitaires

**Informations système :**
- `date` : affichage de la date et heure
- `who` : liste des utilisateurs connectés
- `wc` : comptage de lignes, mots et caractères

**Édition et permissions :**
- `nano essai`, `gedit essai` : ouverture dans un éditeur de texte
- `chmod +x essai` : attribution des droits d'exécution
- `export PATH=$PATH:/nouveau/chemin` : ajout d'un répertoire au PATH

**Opérations sur fichiers :**
- `rm fichier` : suppression de fichiers
- `mv fichier1 fichier2` : déplacement ou renommage
- `touch toto` : création d'un fichier vide

### TP2 - Langage de commande Shell

#### Scripts shell fondamentaux

Un script shell constitue un programme permettant d'automatiser des tâches répétitives telles que l'administration système ou les sauvegardes. Ces fichiers texte, généralement sans extension ou avec l'extension `.sh` ou `.bash`, contiennent des commandes identiques à celles exécutées en ligne de commande, enrichies de structures de contrôle.

#### Exécution des scripts

L'exécution d'un script s'effectue par la commande `bash nomfichier` dans un terminal. L'interprète traite les commandes séquentiellement selon leur ordre d'apparition. Si le fichier possède les droits d'exécution et se trouve dans un répertoire défini par la variable PATH, il suffit de taper son nom pour l'exécuter.

#### Variables et paramètres

Les scripts peuvent être paramétrés grâce aux variables positionnelles `$1`, `$2`, … `$9`. Plusieurs variables spéciales facilitent la gestion des paramètres :

- `$#` : nombre de paramètres passés au script
- `$*` : ensemble de tous les paramètres
- `$1` : premier paramètre

#### Test des paramètres d'exécution

Le script `testparam` illustre la gestion basique des paramètres :

```bash
#!/bin/bash
if test $# -eq 0
then
    echo "Pas de parametre"
elif [ "$1" = "-h" ]
then
    echo "usage : testparm parametres"
else
    echo "Les parametres sont : $*"
fi
```

Ce script vérifie l'absence de paramètres avec `$# -eq 0` et teste la présence de l'option d'aide `-h` avec `[ $1 = "-h" ]`.

#### Test d'existence de fichiers

Le script `testfic` démontre la vérification d'existence de fichiers et répertoires :

```bash
#!/bin/bash
if test $# -eq 0 -o "$1" = "-h"; then
    echo "usage : testfic nomfichier"
elif [ -f $1 ] ; then
    echo "le fichier $1 existe"
elif [ -d $1 ] ; then
    echo "le repertoire $1 existe"
else
    echo $1 est absent !
fi
```

Les tests utilisent :

- `[ -f $1 ]` : vérification d'existence d'un fichier
- `[ -d $1 ]` : vérification d'existence d'un répertoire
- `-o` : opérateur logique OU

#### Commande de sauvegarde

La commande `sauver` automatise la sauvegarde de fichiers dans un répertoire dédié. Elle crée le répertoire `sauvegarde` s'il n'existe pas et affiche des messages d'erreur appropriés pour les répertoires ou fichiers absents.

#### Gestion des dates

Le script `datedujour` affiche la date sous une forme lisible : "Nous sommes le Xeme jour du Yeme mois de l'annee Z", en éliminant les zéros non significatifs et en gérant l'affichage "1er" pour le premier jour.

#### Manipulation de chaînes de caractères

L'extraction de sous-chaînes utilise la syntaxe `${nomvar:d:lg}` où :

- `nomvar` : nom de la variable
- `d` : indice de début (0 pour le premier caractère)
- `lg` : longueur de la sous-chaîne

Exemple : si `nomvar=tralala`, alors `${nomvar:1:3}` retourne "ral".

#### Calculs et algorithmes

##### Commande maximum

La commande `maximum` calcule et affiche le maximum d'une liste d'entiers. Elle utilise une boucle pour parcourir tous les paramètres et maintient la valeur maximale dans la variable `maxi`.

##### Commande categorie

La commande `categorie` détermine la catégorie d'âge d'un athlète selon son année de naissance, conformément aux règles d'athlétisme 2016/2017 :

| Catégorie | Année de naissance | Catégorie | Année de naissance |
|-----------|-------------------|-----------|-------------------|
| Masters | 1976 et avant | Minimes | 2001 et 2002 |
| Seniors | 1977 à 1993 | Benjamins | 2003 et 2004 |
| Espoirs | 1994 à 1996 | Poussins | 2005 et 2006 |
| Juniors | 1997 et 1998 | École d'Athlétisme | 2007 à 2009 |
| Cadets | 1999 et 2000 | Baby Athlé | 2010 et après |

##### Commande afficherresultat

Cette commande combine les fonctionnalités précédentes pour afficher la catégorie et le meilleur lancé d'un athlète. Elle accepte six paramètres : prénom, nom, date de naissance (format j-m-aaaa) et trois essais.

#### Traitement de fichiers avec awk

La commande `calculerresultats` traite un fichier d'athlètes au format CSV avec séparateur deux-points. Le fichier `athletes.txt` contient :

```
#Fichiers des athletes
#Nom:Prenom:dateNaissance:essai1:essai2:essai3
Galle:Martin:12-2-1991:94:87:93
Honnete:Marie:14-9-1982:82:91:93
Pleur:Jean:13-3-1976:93:79:72
```

L'outil `awk` facilite le traitement de fichiers structurés :

- Syntaxe : `awk [-Fseparateur] [-v variable] [-f fichier_commandes] [programme] fichier`
- Exemple : `awk -F: 'NR>2{print $2" "$1}' athletes.txt`
- Variables : `NR` (numéro de ligne), `$1` (première colonne), `$NF` (dernière colonne)

La variable `IFS=$'\n'` peut être définie pour utiliser le caractère de fin de ligne comme séparateur dans les boucles shell.

### TP3 - Processus en C

#### Fonctions système fondamentales

##### Fonction sleep

```c
#include <unistd.h>
unsigned int sleep(unsigned int s)
```

La fonction `sleep(5)` suspend l'exécution du processus pendant 5 secondes.

##### Fonction fork

```c
#include <unistd.h>
pid_t fork();
```

La fonction `fork()` crée un processus fils identique au processus père. Elle retourne :

- Le PID du fils dans le processus père
- 0 dans le processus fils
- -1 en cas d'erreur

Les fonctions `getpid()` et `getppid()` retournent respectivement le PID du processus actuel et de son père.

##### Fonction exit

```c
#include <stdlib.h>
void exit(int status)
```

La fonction `exit()` termine l'exécution du processus appelant. Le paramètre `status` constitue le code de terminaison transmis au processus père. Les constantes `EXIT_SUCCESS` et `EXIT_FAILURE` définissent les codes standards de réussite et d'échec.

##### Fonction wait

```c
#include <sys/types.h>
#include <sys/wait.h>
pid_t wait(int *stat_loc)
```

Cette fonction permet à un processus d'attendre la terminaison d'un de ses fils. Elle retourne :

- -1 si le processus n'a pas de fils ou si tous sont terminés
- Le PID du fils terminé sinon

L'appel `wait(NULL)` ignore le statut de terminaison, tandis que `wait(&status)` le récupère.

##### Fonction execlp

```c
#include <unistd.h>
int execlp(char *arg0, char *arg1, ..., char *argn, NULL)
```

Cette fonction remplace le code du processus courant par un programme exécutable. Elle ne retourne jamais en cas de succès, seulement en cas d'erreur (-1).

Exemples d'utilisation :

- `execlp("ls", "ls", "*.c", NULL)` : exécute la commande ls avec l'argument *.c
- `execlp("ps", "ps", "-l", NULL)` : exécute ps avec l'option -l
- `execlp("xterm", "xterm", NULL)` : lance un terminal

#### Exemple pratique : deux processus fils

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
    pid_t ident1;
    ident1 = fork();
    
    if (ident1 == -1)
    {
        perror("fork");
        return EXIT_FAILURE;
    }

    printf("Cette ligne sera affichée deux fois\n");
    
    if (ident1 == 0)
    {
        /* Code du fils 1 */
        sleep(8);
        printf("Je suis le fils 1, ident %d, pid %d, ppid %d.\n", 
               ident1, getpid(), getppid());
        exit(EXIT_SUCCESS);
    }
    else
    {
        /* Code du père */
        pid_t ident2;
        ident2 = fork();
        
        if (ident2 == -1)
        {
            perror("fork");
            return EXIT_FAILURE;
        }

        if (ident2 == 0)
        {
            /* Code du fils 2 */
            sleep(3);
            printf("Je suis le fils 2, ident %d, pid %d, ppid %d.\n", 
                   ident2, getpid(), getppid());
            exit(EXIT_SUCCESS);
        }
        else
        {
            /* Attente des fils par le père */
            pid_t child_pid;
            
            child_pid = wait(NULL);
            printf("Le premier fils en mourir est : %d\n", child_pid);
            
            child_pid = wait(NULL);
            printf("Le deuxième fils en mourir est : %d\n", child_pid);
        }
    }

    return EXIT_SUCCESS;
}
```

#### Exécution de commandes Unix

L'exemple suivant illustre l'utilisation d'`execlp` pour lancer la commande `ps -l` :

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid;

    pid = fork();
    if (pid == -1)
    {
        perror("fork");
        return EXIT_FAILURE;
    }

    if (pid == 0)
    {
        /* Code du fils */
        printf("Je suis le fils, pid %d, ppid %d.\n", getpid(), getppid());
        
        /* Lancement de ps -l */
        execlp("ps", "ps", "-l", NULL);
        
        /* Si on arrive ici, il y a eu une erreur */
        perror("execlp");
        exit(EXIT_FAILURE);
    }
    else
    {
        /* Code du père */
        printf("Je suis le père, pid %d, en attente de mon fils %d.\n", 
               getpid(), pid);
        wait(NULL);
        printf("Mon fils a terminé.\n");
    }

    return EXIT_SUCCESS;
}
```

### TP4 - Threads et sémaphores en Java

#### Méthodes des threads Java

Les threads Java disposent de plusieurs méthodes pour contrôler leur exécution et leur synchronisation :

**Méthodes d'instance :**
- `run()` : méthode à redéfinir contenant le code du thread
- `start()` : démarre l'exécution du thread
- `join()` : bloque le thread appelant jusqu'à la terminaison du thread cible
- `wait()`, `wait(long millisec)` : met le thread en attente
- `notify()`, `notifyAll()` : réveil des threads en attente

**Méthodes statiques :**
- `Thread.sleep(long millisec)` : endort le thread courant
- `Thread.currentThread()` : retourne une référence au thread courant
- `Thread.yield()` : cède le tour d'exécution

#### Synchronisation avec sémaphores

##### Implémentation basique d'un sémaphore

```java
class Semaphore {
    private int permits;

    public Semaphore(int initialPermits) {
        permits = initialPermits;
    }

    public synchronized void acquire() throws InterruptedException {
        if (permits <= 0) {
            wait();
        }
        permits--;
    }

    public synchronized void release() {
        permits++;
        notify();
    }
}
```

##### Exemple de synchronisation ABC

Le défi consiste à synchroniser trois threads pour afficher la séquence "ABCABCABCABCABC". La solution utilise trois sémaphores, un pour chaque thread :

```java
public class Main {
    public static void main(String args[]) {
        Semaphore mutexA = new Semaphore(1);  // A peut commencer
        Semaphore mutexB = new Semaphore(0);  // B attend
        Semaphore mutexC = new Semaphore(0);  // C attend

        new ThreadA(mutexA, mutexB).start();
        new ThreadB(mutexB, mutexC).start();
        new ThreadC(mutexC, mutexA).start();
    }
}

class ThreadA extends Thread {
    Semaphore mutexA, mutexB;
    
    public ThreadA(Semaphore mutexA, Semaphore mutexB) {
        this.mutexA = mutexA;
        this.mutexB = mutexB;
    }
        
    public void run() {
        for (int i = 0; i < 5; i++) {
            try {
                mutexA.acquire();  // Attendre son tour
                System.out.print("A");
                mutexB.release();  // Autoriser B
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

#### Exemple CarPark : synchronisation par moniteurs

##### Version avec wait/notify

```java
public class CarPark {
    private int capacity;
    
    public CarPark(int capacity) {
        this.capacity = capacity;
    }
    
    public synchronized void arrive() {
        System.out.println(Thread.currentThread().getName() + " essaye d'arriver");
        
        while (capacity == 0) {
             System.out.println(Thread.currentThread().getName() + " attend...");
             try {
                 wait();
             } catch (InterruptedException e) {}
        }
        
        capacity--;
        System.out.println(Thread.currentThread().getName() + 
                          " entre dans le parking [il reste " + capacity + " place(s)]");
    }
    
    public synchronized void depart() {
        System.out.println(Thread.currentThread().getName() + " repart");
        capacity++;
        notify();
    }
}
```

##### Version avec sémaphores Java

```java
import java.util.concurrent.Semaphore;

public class CarPark {
    private Semaphore places;
    
    public CarPark(int capacity) {
        this.places = new Semaphore(capacity);
    }
    
    public void arrive() {
        System.out.println(Thread.currentThread().getName() + " essaye d'arriver");
        
        try {
            places.acquire();
            System.out.println(Thread.currentThread().getName() + 
                              " entre dans le parking [il reste " + 
                              places.availablePermits() + " place(s)]");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    public void depart() {
        System.out.println(Thread.currentThread().getName() + " repart");
        places.release();
    }
}
```

#### Bonnes pratiques

**Gestion des threads :**
- Utiliser `synchronized` dans la signature d'une méthode pour accéder aux méthodes `wait()`, `notify()`, `notifyAll()`
- Placer `wait()` dans un bloc try-catch et préférer une boucle `while` à un simple `if`
- Les sémaphores Java offrent des méthodes comme `tryAcquire()` pour les acquisitions non bloquantes

**Création de threads :**
- Deux approches : hériter de `Thread` ou implémenter `Runnable`
- Toujours appeler `start()` sur l'objet thread, jamais directement `run()`
- La méthode `availablePermits()` des sémaphores Java permet de connaître le nombre de jetons disponibles
