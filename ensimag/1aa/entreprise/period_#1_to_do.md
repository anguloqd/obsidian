## Period #1 - To-Do

## Normal To-Do

- [ ]  NVidia Jetson (for AGX Orin):
    - [x]  Add args for dla-cores and --allowGPUFallback to:
        - [ ]  valid/benchmark.py
        - [x]  valid/gpu/benchmark.py
            - [x]  Calling and passing to [build.sh](http://build.sh)
            - [x]  Calling and passing to run.sh
            - [x]  Creating DLA_CORES column to .csv column
        - [x]  [build.sh](http://build.sh) itself
        - [x]  [run.sh](http://run.sh) itself
    - [ ]  Add columns for NN class in the valid/gpu/benchmark.py .csv output
    - [ ]  Explain the times received.

- [ ]  (kann-models-zoo) read [WIKI.md](http://WIKI.md) and [README.md](http://README.md)
- [ ]  KaNN Training pptx
    - [ ]  KAF examples
    - [ ]  opencl_whitebox_example.cpp
    
- [x]  How To:
    - [x]  `KANN_BUILD_DIR_CV2=/work1/$USER/kaf/kann/build_local_CV2` ?
        - [x]  This is for the client, not for the developper. the .pocl is in another place. Check aliases in terminal.
    - [x]  `KANN_POCL_FILE=$KANN_BUILD_DIR_CV2/opencl_kernels/mppa_kann_opencl.cl.pocl` ?
        - [x]  Same answer.

## Newcomers Checklist

[https://kalrayinc.sharepoint.com/:p:/r/sites/Embedded-ComputeApps/_layouts/15/doc2.aspx?sourcedoc=%7BBE439A1B-74D2-41A8-A739-9D0E72D4DBEA%7D&file=Compute%20apps%20-%20new%20comers%20-%20Daniel.pptx&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&action=edit&mobileredirect=true](https://kalrayinc.sharepoint.com/:p:/r/sites/Embedded-ComputeApps/_layouts/15/doc2.aspx?sourcedoc=%7BBE439A1B-74D2-41A8-A739-9D0E72D4DBEA%7D&file=Compute%20apps%20-%20new%20comers%20-%20Daniel.pptx&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&action=edit&mobileredirect=true)

## Objectives

[Objectifs_periode_1_Daniel_angulo.pdf](ressources/period_#1_to_do_objectifs_periode_1_daniel_angulo_1.pdf)

### Missions

Au cours de la première période, l’apprenti devra :

1/ Acquérir les connaissances et compétences nécessaires à son environnement de travail

2/ Participer à l’évaluation technique de produits concurrents

3/ Participer au développement de nouvelles fonctionnalités

### Objectifs pédagogiques et activités prévues

Pour se faire, nous organisons le temps de travail de Daniel sur :

- 2 semaines ramp-up : formations internes sur les outils, process, produits Kalray (utilisation du SDK pour l’inférence de réseau de neurone). Nous tiendrons compte des retours de Daniel pour une future amélioration de la documentation ou possible incohérence.
- 4 semaines de travail réparties sur 2 tâches :
    - Priorité 1 :
    ▪ Prendre en main les outils d’inférence NVIDIA pour les kits de Jetson (1 semaine)
    ▪ Evaluer les performances atteintes d’un produit concurrent (NVIDIA Jetson Orin) sur un ensemble d’algorithmes de réseau de neurone (CNN) (1 semaine)
    - Priorité 2 :
    ▪ Ecrire un script d’évaluation de précision (mAP-50) pour un CNN de type « Object- detection » sur le dataset COCO-128 (128 images / classes) (1 semaine)
    ▪ Evaluer et améliorer le script (1 semaine)

### Autres éléments de description complémentaires

Pas de résultats sur objectifs attendus. On reste modulaire et progressif en fonction des compétences de Daniel. Les seules priorités de cette 1e phase en entreprise sont :

- De comprendre l’environnement et les flux de travail
- L’utilisation et le fonctionnement d’un réseau de neurone dans un écosystème complexe (Kalray ou concurrent).
