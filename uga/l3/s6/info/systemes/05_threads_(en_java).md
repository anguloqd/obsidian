## 05 // threads (en Java)

[systemes_cours5_2223.pdf](ressources/05_threads_(en_java)_systemes-cours5-2223.pdf)

## Threads et synchronisation en Java

### Introduction aux threads

#### Concept fondamental

Un thread, également appelé « processus léger », constitue une unité d'exécution au sein d'un processus. Un processus peut contenir plusieurs threads qui partagent tous le même espace mémoire, permettant ainsi un accès commun aux données et ressources du processus parent. Chaque thread possède néanmoins son propre pointeur d'exécution (Program Counter), lui conférant une progression indépendante dans le code.

#### Parallélisation des traitements

Les threads permettent de paralléliser des traitements au sein d'une application. Par défaut, toute application Java s'exécute avec au moins un thread principal et un ou plusieurs threads dédiés au ramasse-miettes (garbage collector). Cette approche présente l'avantage de permettre l'exécution simultanée de plusieurs tâches, mais consomme davantage de ressources système.

### Structure et contenu d'un thread

#### Composants essentiels

Chaque thread contient du code ou un algorithme à exécuter, défini dans la méthode `public void run()`. Cette méthode doit être redéfinie selon les besoins spécifiques du thread. Le démarrage s'effectue par l'appel de la méthode `public void start()`.

#### Cycle de vie

Un thread vit jusqu'à la fin de l'exécution de sa méthode `run()`. Plusieurs mécanismes permettent de contrôler son état d'exécution :

- `void sleep(int millisec)` endort temporairement le thread
- `void wait()` met le thread en attente jusqu'à réveil explicite

### Création des threads

#### Dérivation de la classe Thread

La première approche consiste à dériver la classe `Thread` et redéfinir la méthode `run()` :

```java
class MonThread extends Thread {
    public MonThread() {
        // initialisation
    }
    
    public void run() {
        // le code de l'action du thread
    }
}

MonThread t = new MonThread();
t.start(); // exécute la méthode run() en parallèle
```

#### Implémentation de l'interface Runnable

La seconde approche implémente l'interface `Runnable` :

```java
class MaTache implements Runnable {
    public MaTache() {
        // initialisation
    }
    
    public void run() {
        // le code de l'action du thread
    }
}

MaTache tache = new MaTache();
Thread t = new Thread(tache);
t.start(); // exécute la méthode run() de MaTache en parallèle
```

### Méthodes de la classe Thread

#### Méthodes statiques

Les méthodes statiques agissent sur le thread qui les exécute :

- `Thread.sleep(long millisec)` endort le thread courant pour la durée spécifiée
- `Thread.currentThread()` retourne une référence vers le thread courant
- `Thread.yield()` indique au planificateur que le thread peut céder son tour d'exécution

#### Méthodes d'instance

Les méthodes d'instance permettent de contrôler un thread spécifique :

- `t.start()` démarre le thread de manière non bloquante et exécute le contenu de `run()` en parallèle
- `t.join()` bloque le thread appelant jusqu'à la terminaison du thread `t`
- `t.yield()` indique que le thread `t` peut céder son tour d'exécution

### Cycle de vie d'un thread

Les threads traversent plusieurs états durant leur existence :

1. **Création** : l'objet thread est instancié via `new`
2. **Exécutable** : après appel de `start()`, le thread peut être sélectionné pour exécution
3. **En cours d'exécution** : le thread s'exécute effectivement
4. **En attente** : le thread attend un événement (via `wait()`, `join()`, `sleep()`)
5. **Mort** : fin de l'exécution de la méthode `run()`

Les transitions entre états s'effectuent par :

- `yield()` : passage d'en cours d'exécution à exécutable
- `wait()`, `join()`, `sleep()` : passage vers l'état en attente
- `notify()`, `notifyAll()`, fin du délai : réveil vers l'état exécutable

### Synchronisation par moniteurs

#### Concept de moniteur

La synchronisation s'effectue par le moniteur d'un objet, structure composée d'un verrou et d'une liste d'attente. Tout objet Java possède un moniteur intrinsèque.

#### Méthodes de synchronisation

Pour un objet `o` donné :

- `o.wait()` bloque le thread appelant et le place dans la file d'attente du moniteur de `o`
- `o.notify()` réveille un thread en attente (choix non déterministe)
- `o.notifyAll()` réveille tous les threads en attente

Ces méthodes peuvent lever une `InterruptedException` et doivent être appelées dans un contexte synchronisé.

### Interruption des tâches

Un thread bloqué peut être interrompu via la méthode `void interrupt()`. Cette interruption génère une `InterruptedException` dans les méthodes bloquantes :

```java
class MonThread extends Thread {
    public void run() {
        try {
            Thread.sleep(100);
            System.out.println("Je me suis réveillé tout seul");
        } catch (InterruptedException e) {
            System.out.println("On m'a réveillé :-(");
        }
    }
}

MonThread t = new MonThread();
t.start();
Thread.sleep((long) (Math.random()*200));
t.interrupt();
```

### Exclusion mutuelle avec synchronized

#### Principe fondamental

Le mot-clé `synchronized` garantit l'exclusion mutuelle en verrouillant l'accès à une ressource partagée :

```java
public class ExclusionMutuelle {
    public static void main(String[] args) throws InterruptedException {
        Compte c = new Compte();
        Thread[] lesThreads = new Thread[10];
        
        for (int i = 0; i < lesThreads.length; i++) {
            lesThreads[i] = new Thread() {
                public void run() {
                    for (int j = 0; j < 1000; j++) {
                        c.deposerUnEuros();
                    }
                }
            };
            lesThreads[i].start();
        }
        
        for (Thread x : lesThreads) {
            x.join();
        }
        
        System.out.println(c.value);
    }
}

class Compte {
    public volatile int value;
    
    // méthode appelée en exclusion mutuelle
    public synchronized void deposerUnEuros() {
        value += 1;
    }
}
```

#### Utilisations du mot-clé synchronized

Le mot-clé `synchronized` peut s'utiliser de deux manières :

**Devant une méthode** (verrouille l'objet sur lequel est appelée la méthode) :

```java
class Compte {
    public volatile int value;
    public synchronized void deposerUnEuros() { 
        value += 1; 
    }
}
```

**En tant que bloc** :

```java
class Compte {
    public volatile int value;
    public Object lock = new Object();
    
    public void deposerUnEuros() {
        synchronized(lock) { 
            value += 1;
        }
    }
}
```

### Problème d'interblocage

L'imbrication de blocs synchronisés peut créer des situations d'interblocage. L'exemple suivant illustre ce risque :

```java
class MonThread1 extends Thread {
    public void run() {
        synchronized(a) {
            // ...
            synchronized(b) {
                // ...
            }
        }
    }
}

class MonThread2 extends Thread {
    public void run() {
        synchronized(b) {
            // ...
            synchronized(a) {
                // ...
            }
        }
    }
}
```

Si `MonThread1` acquiert le verrou `a` tandis que `MonThread2` acquiert le verrou `b`, les deux threads se retrouvent en attente mutuelle.

### Attente passive

#### Mécanisme wait/notify

La méthode `wait()` appelée sur un objet `o` met le thread appelant en attente. Cette méthode doit être appelée en exclusion mutuelle, typiquement dans un bloc `synchronized(o)`. Elle peut lever une `InterruptedException`.

Pour réveiller un thread en attente, un autre thread doit appeler :

- `o.notify()` : réveille un thread en attente (choix non contrôlable)
- `o.notifyAll()` : réveille tous les threads en attente

### Sémaphores en Java

Java fournit une classe `java.util.concurrent.Semaphore` pour implémenter des sémaphores :

```java
Semaphore sem = new Semaphore(int nbJetons);

// Pour prendre un jeton avec attente si non disponible
sem.acquire();

// Prendre un jeton si disponible sans attendre
boolean res = sem.tryAcquire();

// Relâcher un jeton
sem.release();
```

La méthode `tryAcquire()` accepte également un délai d'attente en paramètre.

### Limites du mécanisme synchronized

#### Contraintes structurelles

Le mécanisme `synchronized` présente plusieurs limitations :

1. **Portée limitée** : ne peut verrouiller que sur une méthode maximum, empêchant le verrouillage dans une méthode et le déverrouillage dans une autre

2. **Ordre de relâchement** : les verrous se relâchent dans l'ordre opposé à leur acquisition (premier obtenu, dernier relâché)

3. **File d'attente unique** : un seul moniteur par objet, donc une seule file d'attente

4. **Absence de gestion d'équité** : le thread attendant depuis le plus longtemps n'est pas nécessairement servi en premier

### ReentrantLock

#### Extension des capacités de synchronisation

La classe `ReentrantLock` offre des fonctionnalités étendues par rapport aux moniteurs et au mot-clé `synchronized` :

```java
class X {
    private final ReentrantLock lock = new ReentrantLock();
    
    public void m() {
        lock.lock(); // prise de verrou bloquante
        try {
            // ... code en exclusion mutuelle
        } finally {
            lock.unlock(); // relâche le verrou
        }
    }
}
```

Cette approche équivaut fonctionnellement à :

```java
class Y {
    private final Object lock = new Object();
    
    public void m() {
        synchronized(lock) { // prise de verrou bloquante
            // ... code en exclusion mutuelle
        } // relâche le verrou
    }
}
```

#### Conditions multiples

`ReentrantLock` permet d'obtenir plusieurs conditions (files d'attente) sur un même verrou :

```java
class Z {
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition cond = lock.newCondition();
    
    public void arriveeRDV() throws InterruptedException {
        lock.lock();
        try {
            cond.await(); // attendre
        } finally {
            lock.unlock();
        }
    }
    
    public void debloquerRDV() throws InterruptedException {
        lock.lock();
        try {
            cond.signal(); // réveiller un thread
            // cond.signalAll(); // réveiller tous les threads
        } finally {
            lock.unlock();
        }
    }
}
```

### Autres mécanismes de synchronisation

#### Barrières de synchronisation

Java propose des classes spécialisées pour des patterns de synchronisation avancés :

- **CyclicBarrier** : bloque des threads en un point jusqu'à ce qu'un nombre requis de threads aient atteint ce point
- **CountDownLatch** : permet à un ou plusieurs threads d'attendre qu'un ensemble d'opérations se termine dans d'autres threads

Ces mécanismes facilitent la coordination de threads dans des scénarios complexes de programmation concurrente.
