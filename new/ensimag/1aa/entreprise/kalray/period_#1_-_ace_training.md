# Period #1 - ACE training

Date de création: October 30, 2024 2:45 PM
Modifié: November 20, 2024 11:51 AM

Install ACE on a concrete tag (5.3.1 rc2)
Install ACE submodules (kEnv, kann, kaf_applications) on that same tag

Three components must be on the same version: ACE, STM32, MPPA. If that’s the case, everything should work correctly.

Ctrl + R

```bash
rm -rf kaf # on commence dès zero
bash # deactive la toolchain 

git clone gerrit:software/tools/kaf
cd kaf
git branch
git log --oneline -1
git submodule update --init --recursive
git tag --list | grep ACE-
git reset --hard ACE-5.3.1-rc2
git log --oneline -1
git submodule update --init --recursive
git show d84c85b
# eventuellement ici on a du faire -i et kvx-board-program et sudo reboot
# sinon pour les ./run on a eu un erreur de detection
# (histoire de tags ou "planetes" non alignés)
./get_valid_packages.sh
source kEnv/kvxtools/.switch_env
echo $KALRAY_TOOLCHAIN_DIR
lspci
lspci | grep -i kalray
ls /mppa/board0/
cat /mppa/board0/archver
kvx-mppa --version
kvx-board-diag
kvx-board-program
cd kann
echo $WORKON_HOME
make -BC python sync-venv
source python/activate_venv.sh
cd ../.. # on se place en /work1/dangulo

git clone https://github.com/kalray/kann-models-zoo.git
cd kann-models-zoo/
git branch
git checkout -b
git checkout -b ace5.3 -t origin/ace5.3
git remove -v
git status
ls -l
pip install -r requirements.txt
cat WIKI.md | grep pip
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
./generate networks/classifiers/regnet-x-1.6g/onnx/network_f16.yaml -d r1.6
./run infer r1.6
# inside inference_r1.6.log
## /!\ WARNING WARNING WARNING /!\
## No MPPA device found please check PCIe driver installation or board plug
### (So, this meant we had to do "get_valid_package.sh -i")
./run demo r1.6 utils/sources/dog.jpg --no-replay --no-display -v
./run demo r1.6 utils/sources/dog.jpg --no-replay --no-display -v -d cpu
```

## ACE Training (Stéphane Gailhard)

dpu (definition): manycore, entre-sortie rapide, bloque hardcode,, calcul paralleles

network on chip du mma: communication ethernet externe (level 3) et entre processeurs

axi : communication avec la memoire ddr

dma : mini-core dont son travail est juste prefetch de donnes et envoi en dehors de cluster

secure mngm core: run l’os, sec mem est sa memore

crypt acc: pour faire du SHA.

simulation de muti-threading (pseudo-threading) : un cluster envoi un posxit vers le secure mngm core; puis lui il distribue à une autre coeur

kvx : kalray version x (k1, k2, k3, puis on en a eu marre)

arhitecture/processeur/jeu de’instructions: x86, arm, et celui de kalray propre qui est “kvx”

coprocesseur: un por chaque processeur, avec ses propres registres et instructions, c’est vraiment un processeur different de celui qui le contient. il contient de multiplication et accumulation (MAC), son opération principale

accesscore: le logiciel

AC middleware: AC Base

OpenMP: pragma (cache

OCUlink: carte rouge qui envoie le binaire à un cluster

nvidia fait du ddr → ddr accel → processeur (fait des traitements par pixels, tant que mppa fait SMEM → processeur (plutôt de traitement par lignes de pixels)