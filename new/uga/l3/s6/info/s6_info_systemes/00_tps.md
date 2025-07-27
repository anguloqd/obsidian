# 00 // tps

[cmdes_unix_desc.pdf](ressources/00_tps_cmdes_unix_desc.pdf)

[systemes-tp1-2324.pdf](ressources/00_tps_systemes-tp1-2324.pdf)

[systemes-tp2-2223.pdf](ressources/00_tps_systemes-tp2-2223.pdf)

[systemes-tp3-1819.pdf](ressources/00_tps_systemes-tp3-1819.pdf)

[systemes-tp4-1819.pdf](ressources/00_tps_systemes-tp4-1819.pdf)

# TP1

## **Gestion de fichiers et de répertoires**

- Créer un répertoire : `mkdir bin`
- Copier le répertoire : `cp -r /media/commun/shell .` ou `scp -pr votrelogin@miashs-dc.u-ga.fr:/media/commun/shell .`
- Se placer dans le répertoire shell ou noms : `cd shell` ou `cd noms`
- Remonter au répertoire shell : `cd ..`
- Revenir au répertoire de travail par défaut : `cd ~`, `cd`, `cd $HOME`
- Supprimer tous les fichiers du répertoire `shell/noms` : `rm -r ./shell/noms/*`
- Supprimer le répertoire `shell/noms` : `rmdir ./shell/noms`

## **Manipulation de fichiers**

- Afficher le contenu du fichier bravo.c : `cat bravo.c`
- Afficher le contenu des fichiers m1 et m2 : `cat m1 m2`
- Créer une copie du fichier m1 : `cat m1 > m1bis`
- Créer un fichier toto : `cat > toto` (Terminer le texte par Ctrl-D.)
- Afficher le contenu du fichier bravo.c en caractères : `od -c bravo.c`
- Afficher le contenu du fichier bravo.c en hexadécimal : `od -x bravo.c`
- Lancer l’exécution de bravo en redirigeant la sortie standard : `./bravo > out`
- Ajouter la sortie de bravo à out : `./bravo >> out`
- Rediriger la sortie erreur de ls sur un fichier err : `ls titi 2> err`
- Rediriger la sortie standard : `ls titi * > out`

## **Liste des fichiers**

- Vérifier si les fichiers sont vides : `ls -l noms`
- Afficher tous les fichiers se terminant par .c : `ls *.c`
- Afficher tous les fichiers commençant par ‘a’ ou ‘g’ : `ls [ag]*` ou `ls a* g*`
- Afficher tous les fichiers commençant par ‘a’ et se terminant par 1 : `ls a*1`
- Afficher tous les fichiers avec exactement 3 caractères : `ls ???`
- Afficher le contenu du répertoire de travail : `ls ~` ou `ls $HOME`

## **Compilation et exécution**

- Compiler le programme C : `cc bravo.c` puis lancer l’exécution : `./a.out`
- Compiler avec l’option -o : `cc bravo.c -o bravo` puis lancer l’exécution : `./bravo`
- Compiler et exécuter boucle.c : `cc boucle.c -o boucle` puis `./boucle`

## **Environnement et processus**

- Afficher l’environnement : `env` (affiche les variables d’environnement globales), `set` (affiche les variables locales et globales)
- Modifier le prompt : `export PS1="Votre nouveau prompt > "`
- Ajouter une commande à la fin du fichier `~/.bashrc` : `echo 'echo -e "\\nBonjour\\n"' >> ~/.bashrc`
- Afficher la liste des processus actifs : `ps` ou `ps -ef` ou `ps -fU $LOGNAME`
- Ouvrir un nouveau terminal en arrière-plan : `xterm -T nouveau &`
- Arrêter un processus : `kill -KILL <PIDduProcessus>`
- Se connecter à un serveur distant : `ssh votrelogin@miashs-dc.u-ga.fr`

## **Autres**

- Afficher la date et l’heure actuelles : `date`
- Afficher la liste des utilisateurs actuellement connectés : `who`
- Compter le nombre de lignes, de mots et de caractères dans les fichiers : `wc`
- Ouvrir un fichier dans un éditeur de texte (nano ou gedit) : `nano essai` ou `gedit essai`
- Rendre un fichier exécutable : `chmod +x essai`
- Ajouter un répertoire à la variable d’environnement PATH : `export PATH=$PATH:/chemin/vers/le/repertoire`
- Modifier des variables d’environnement à chaque ouverture de terminal : Éditer le fichier `~/.bashrc`
- Supprimer des fichiers : `rm fichier`
- Déplacer ou renommer des fichiers : `mv fichier1 fichier2` ou `mv fichier /chemin/vers/repertoire/`
- Créer un nouveau fichier vide : `touch toto`

# TP2

…

# TP3

## Fonctions

```c
#include <unistd.h>
unsigned int sleep(unsigned int s)

sleep(5);  /* s'utilise comme ça */

---

#include <unistd.h>
pid_t fork();

pid_t ident;    /* s'utilise comme ça */
ident = fork(); /* pour le pere c'est le pid du fils,
								pour le fils c'est 0 car il n'a pas de fils */

pid_t getpid();  /* pid du procesus actuel */
pid_t getppid(); /* pid du processus père */

---

#include <stdlib.h>
void exit(int status)

/* Le processus appelant met fin à son exécution.
Un appel exit(status) est équivalent à un return
status dans la fonction main d’un programme C.
L’entier status est un code de terminaison et est
rendu au processus père si celui-ci attend la fin
de son fils (voir wait) */

exit(EXIT_SUCCESS);
exit(EXIT_FAILURE);

---

#include <sys/types.h>
#include <sys/wait.h>
pid_t wait(int *stat loc)

/* Cette fonction permet à un processus d’attendre
la mort d’un de ses fils. Si le processus n’a pas eu
de fils, ou si tous les fils sont morts au moment de
l’appel de wait, la fonction rend -1.
Si un fils est déjà mort, la fonction rend le numéro
d’identification de ce fils. Sinon le processus est
bloqué jusqu’au décès d’un fils (le premier qui meurt)
et rend son numéro (cette attente n’est donc pas 
sélective). */

wait(NULL) /* attend la mort d'un fils et retourne son pid */

int status;
wait(&status); /* retourne plutot un entier décrivant un status */

---

#include <unistd.h>
int execlp(char *arg0, char *arg1, ..., char *argn, NULL)

/* Un processus peut lancer un programme exécutable
qui se trouve dans un fichier sur disque en utilisant
un des appels système exec(). Le code du programme
sur disque remplace le code du processus en cours
et donc un appel à exec() ne retourne jamais, sauf en
cas d’erreur où il retourne -1 et positionne la variable
système errno */

/* La syntaxe est normalement execlp("programme", arg1, arg2, ..., NULL).
Par convention, arg1 est aussi le même nom du programme, puis
les autres paramètres sont passés. La liste est delimitée par NULL
pour marquer la  */

execlp("ls", "ls", "*.c", NULL) /*exécute la commande "ls"
																passant l'argument "*.c"
																pour trouver tous les fichiers
																avec l'extension ".c"*/

execlp("ps", "ps", "-l", NULL); /*exécute la commande "ps"
																passant l'argument "-l"
																pour lister les processus*/

																 
execlp("xterm", "xterm", NULL); /* exécute la commande "xterm"
																sans passer d'arguments */
```

## Deux fils, démo basique

```bash
#include <stdio.h>		/* Pour perror */
#include <stdlib.h>		/* Pour exit */
#include <unistd.h>		/* Pour fork, getpid, getppid, sleep */
#include <sys/types.h>		/* Pour pid_t (fork, getpid, getppid) */
#include <sys/wait.h>		/* Pour wait */

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
    /* Code exécuté uniquement par le fils */
    sleep(8);
    printf("Je suis le fils 1, ident %d, pid %d, ppid %d.\n", ident1, getpid(), getppid());
    exit(EXIT_SUCCESS);
  }
  
  else
  {
    /* Code exécuté uniquement par le pere */
    pid_t ident2;
    ident2 = fork();
    
    if (ident2 == -1)
    {
      perror("fork");
      return EXIT_FAILURE;
    }

    if (ident2 == 0)
    {
      sleep(3);
      printf("Je suis le fils 2, ident %d, pid %d, ppid %d.\n", ident2, getpid(), getppid());
      exit(EXIT_SUCCESS);
    }

    else
    {
    	pid_t child_pid;
		
			child_pid = wait(NULL);
			printf("Le premier fils en mourir est : %d", child_pid);
    	
    	child_pid = wait(NULL);
			printf("Le deuxieme fils en mourir est : %d", child_pid);
    }
  }

  return EXIT_SUCCESS;
}
```

## Deux fils, exécution d’une commande Unix

Voici le cas de `execlp`:

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
    /* Code exécuté uniquement par le fils */
    printf("Je suis le fils, pid %d, ppid %d.\n", getpid(), getppid());

    /* Lancez la commande 'ps -l' */
    execlp("ps", "ps", "-l", NULL);

    /* Si execlp retourne, c'est qu'il y a eu une erreur */
    perror("execlp");
    exit(EXIT_FAILURE);
  }
  else
  {
    /* Code exécuté uniquement par le père */
    printf("Je suis le père, pid %d, en attente de la fin de mon fils %d.\n", getpid(), pid);
    wait(NULL);
    printf("Mon fils a terminé.\n");
  }

  return EXIT_SUCCESS;
}
```

Voici le cas de `xterm` :

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

  if (ident1 == 0)
  {
    /* Code exécuté uniquement par le fils 1 */
    execlp("xterm", "xterm", NULL);
    perror("execlp"); /* Si on arrive ici, c'est qu'il y a eu une erreur */
    exit(EXIT_FAILURE);
  }
  else
  {
    /* Code exécuté uniquement par le père */
    pid_t ident2;

    ident2 = fork();
    if (ident2 == -1)
    {
      perror("fork");
      return EXIT_FAILURE;
    }

    if (ident2 == 0)
    {
      /* Code exécuté uniquement par le fils 2 */
      execlp("xterm", "xterm", NULL);
      perror("execlp"); /* Si on arrive ici, c'est qu'il y a eu une erreur */
      exit(EXIT_FAILURE);
    }
    else
    {
      /* Code exécuté uniquement par le père */
      pid_t child_pid;
      
      child_pid = wait(NULL);
      printf("Le premier fils en mourir est : %d\n", child_pid);
      
      child_pid = wait(NULL);
      printf("Le deuxieme fils en mourir est : %d\n", child_pid);
    }
  }

  return EXIT_SUCCESS;
}

```

# TP4

## Méthodes de Threads et Sémaphores

![untitled](new/uga/l3/s6/info/s6_info_systemes/ressources/00_tps_untitled.png)

![untitled](new/uga/l3/s6/info/s6_info_systemes/ressources/00_tps_untitled_1.png)

- Thread :
    - run() (à redéfinir)
    - start()
    - wait(), wait(long milisec)
    - notify()
    - notifyAll()
    - join() : comme t1.join(), bloque le thread appelant (t2) tant que t1 n’est pas terminé. Bien sur, t1.join() se trouve dans le run() de t2.
    - Static, sleep(long milisec)
    - Static, currentThread() : retourne le thread courant
    - Static, yield() : le thread t passe son tour pour être exécuté

## Sémaphores, exo #1

<aside>
❓  Q4. “Utiliser votre implémentation de la classe Semaphore pour compléter les classes Main, ThreadA, ThreadB et ThreadC fournies. Les classes ThreadA, ThreadB et ThreadC sont des threads qui ont pour but d’afficher respectivement cinq ‘A’, cinq ‘B’ et cinq ‘C’. Il s’agit de synchroniser les threads de sorte que l’affichage corresponde à : ABCABCABCABCABC.“

</aside>

Quelques choses à remarquer :

- Il y a trois sémaphores pour trois threads, **un pour chaque, et non pas un sémaphore pour tous**.
- Quand un sémaphore se relâche, il permet de continuer à l’un d’autres utilisateurs **du même sémaphore**, et non pas des autres.

Voyons la définition de Sémaphore :

```java
public class Main {
    public static void main(String args[]) {
        Semaphore mutexA = new Semaphore(1);
        Semaphore mutexB = new Semaphore(0);
        Semaphore mutexC = new Semaphore(0);

        new ThreadA(mutexA, mutexB).start();
        new ThreadB(mutexB, mutexC).start();
        new ThreadC(mutexC, mutexA).start();
    }
}

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

Exemple de définition d’un thread pour nos objectifs : (les autres threads, `threadB` et `threadC` étant différents)

```java
class ThreadA extends Thread {
    Semaphore mutexA;
    Semaphore mutexB;
    
    public ThreadA(Semaphore mutexA, Semaphore mutexB) {
        this.mutexA = mutexA;
        this.mutexB = mutexB;
    }
        
    public void run() {
        
        for (int i = 0; i < 5; i++) {
            try {
                mutexA.acquire();
                System.out.print("A");
                mutexB.release();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

## `CarPark` : synchronisation sans sémaphores

Quelques choses à remarquer :

- Mettre le mot clé `synchronized` dans la signature d’une fonction permet d’accéder à des fonctions comme `wait()`, `notify()`, `notifyAll()`, etc. Pas besoin de faire `synchronized(o){…}` sur un objet.
- `wait()` doit toujours être dans un try-catch, et c’est mieux qu’il soir dans un `while(cond){...}` que dans un `if(cond){...}`

```java
public class CarPark {
    private int capacity;
    
    public CarPark(int capacity) {
        this.capacity = capacity;
    }
    
    public synchronized void arrive() {
        System.out.println(Thread.currentThread().getName() + " essaye d'arriver");
        
        while (capacity == 0) { // Si il n'y a pas de places disponibles dans le parking...
             System.out.println(Thread.currentThread().getName() + " attend...");
             try {
                 wait(); // La voiture se met en attente jusqu'à ce qu'une place se libère.
             } catch (InterruptedException e) {}
        }
        
        capacity--; // Une place est prise.
        System.out.println(Thread.currentThread().getName() + " entre dans le parking [il reste " + capacity + " place(s)]");
    }
    
    public synchronized void depart() {
        System.out.println(Thread.currentThread().getName()
            + " repart");
            
        capacity++;
        notify(); // Verifier : Cette voiture libère une place pour une autre voiture
    }
    
    public static void main(String args[]) { // Commente ce code
        CarPark carpark = new CarPark(4);
        Random r = new Random();
        
        for (int i=0; i<100; i++) {
            
            try {
            Thread.sleep(r.nextInt(5) * 1000);
            } catch (InterruptedException e) {}
            
            new Thread(new Cars("voiture"+i, carpark)).start();
        }
    }
}
```

## `CarPark` : sémaphores, exo #2

- Deux manières d’utiliser les threads et surtout la méthode start() pour paralléliser :
    - On crée une classe qui hérite de Thread, puis on redéfinit la méthode run() qui sera appelée lors de l’appel **start() sur le thread**;
    - On crée une classe qui implémente l’interface runnable, et on redéfinit sa méthode run. Finalement, on utilise l’instance de classe pour initialiser un Thread et **on appelle start() sur le thread**.
    - La capacité est remplacé par un sémaphore. C’est comme si le jetons du sémaphore déterminent la capacité.
- Cette implémentation ne contrôle pas quel voiture rentre après une place se libère.

```java
import java.util.Random;
import java.util.concurrent.Semaphore;

public class CarPark {
    private Semaphore places;
    
    public CarPark(int capacity) {
        this.places = new Semaphore(capacity);
    }
    
    public void arrive() {
        System.out.println(Thread.currentThread().getName() + " essaye d'arriver");
        
        try {
            places.acquire(); // La voiture tente de prendre une place.
            System.out.println(Thread.currentThread().getName() + " entre dans le parking [il reste " + places.availablePermits() + " place(s)]");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    public void depart() {
        System.out.println(Thread.currentThread().getName() + " repart");
        places.release(); // La voiture libère une place.
    }
    
    public static void main(String args[]) {
        CarPark carpark = new CarPark(4);
        Random r = new Random();
        
        for (int i=0; i<100; i++) {
            try {
                Thread.sleep(r.nextInt(5) * 1000);
            } catch (InterruptedException e) {}
            
            new Thread(new Cars("voiture"+i, carpark)).start();
        }
    }
}
```