## Period #3 - Update kaf submodules

```bash
  437  ssh ws2405
  438  clear
  439  cd /work1/dangulo/
  440  cd kaf/
  441  git fetch
  442  git remote -v
  443  git reset --hard origin/main
  444  git submodule update --init --recursive
  445  ./get_valid_packages.sh -v
  446  clear
  447  source kEnv/kvxtools/.switch_env
  448  kvx-board-diag
  449  clear
  450  cd kann
  451  source python/activate_venv.sh
  452  pip list
  453  git fetch
  454  git remote -v
  455  git status
  456  git checkout -b aci/dangulo/main -t origin/main
  457  git checkout aci/dangulo/main
  458  git reset --hard origin/main
  459  kann -v
  460  cd ..
  461  cd kann-models-zoo/
  462  clear
  463  git status
  464  git checkout aci/dangulo/main
  465  git checkout -b aci/dangulo/main -t origin/main
  466  git log --oneline -10
```
