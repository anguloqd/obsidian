# Period #1 - Tools & Methods training

organigramme simple 

N1: HW (Dolomites), Core SW (Dolo, CV1 et CV2) (Contient equipe board, low level, linux, toolchain, ethernet)

N2, fils de core SW: équipe Data Center (CV1), équipe Compute Kann (CV2)

On peut faire SSH à travers VSCODE

Disque local par convention /work1

NFS rentre en panne de temps en temps

System architecture:

HLR: high level requirement (initiative de marketing et exigences des clients)

SLR: system level requirement

Epic: grande tâche qui devra être decoupe en petites taches, normalement prend tu temps:

- story: tâche pour le client
- task: tâche plutôt interne

Kalray Projects

k1Env: outils pour développer des outils Kalray.

csw (core software) : configurer notre puce. libraries low level. board management. docs.

benchmarks : utilise par equipes low level et compilation. benchmark de performances.

ACR_libraries: projet de la 5G. AccesCore Radio. Pas des clients concrets, plutôt de la prospection.

Linux_toolchain: le linux a installer sur le cluster “central” de mppa. les autres clusters utilisent un clusterOS.

board_testsuite: equipe board. AccessCore Production.

custom_board: equipe board. 

rust: equipe lowlevel

compute_apps: applications orienté clients, permet aussi de valider les release de kaf.

Release plan & process:::

codedrop: snapshot du code, souvant pas intéressant. parfois les codedrops peuvent se retrouver dans les mains des clients. ça arrive e.g. quand on vient de sortir un nouvelle puce.

release candidate: toutes les features y sont, il faut juste corriger des bugs.

Gerrit: projet Google, serveur Git. Mecanique pour faire du code review. 

```
ssh gerrit gerrit
ssh gerrit gerrit ls-projects
```

Structure of a Kalray Git Repo

disons qu’on est à csw, qui est un repo. il contient des submodules.
metabuild.
jenkinsfile: permet l’integration jenkins.
valid/hudson/rev_files: contient de quelque sorte les dépendences de ce module.

git fetch peut nous rammener plusieurs branches qui sont temporaires. si on veut eviter ça, on fait “git fetch --prune” pour eviter de cloner des branches temporaires. une fois par semaine.

(Gerrit Training) kerrit (pas confondre avec gerrit) est necessaire pour soumettre en code review avec les autres.

gerrit review note: de -2 à +2. -2 remporte sur tout, refus absolu. un +2 est necessaire pour passer le code. Deux +1 ne font pas un +2. seuls les “approuvers” peuvent donner un +2 et -2.

Pass machines hudson d’integrations: LA2405wg.
L’integration se fait sur /work1/hudson/workspace.