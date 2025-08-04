# start from a new coolup

```bash
# starting from HOME DIR (~)...

# create your user folder
mkdir /work1/$USER
cd /work1/$USER
# clone kaf
git clone gerrit:software/tools/kaf
cd kaf
# default branch is master. checkout main.
git checkout main
git pull --rebase origin main
# dont work directly on main, make your own copy of main, usually aci/$USER/main
git checkout -b aci/dangulo/main -t origin/main
# now, get the toolchain and source it: stack software por compiler/utilser software kalray
# -i pour desintaller et reinstaller les drivers pci
/get_valid.packages.sh -i -v
source kEnv/kvxtools/.switch-env
# now, make the python venv and source it
cd kann
make -BC python sync-venv
cd ..
source kann/python/activate_venv.sh
# having activated the python venv, install requirements from kmz
cd kann-models-zoo
pip install -r requirements.txt
# lien entre carte-host machine passe par un pci, gestion de l'env de la puce se fait vie un petit processeur
# pour gerer l'env proprement, board management doit être aligné avec la stack software/drivers
#  flasher le board-management aligné à la stack software
# le board-management est celui au milieu du processeur et l'environnement du processeur
kvx-board-program
sudo reboot -i
```