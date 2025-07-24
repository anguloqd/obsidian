# aci

Date de création: July 2, 2025 4:31 PM
Modifié: July 17, 2025 10:14 AM

pas besoin de branche dirty si tu ne modifies pas ton code de aci/dangulo/main

rebuild avec jenkins pour relancer les tests d’aci

si commit de “updated submodules” dans kaf : git reset —hard vers un sha1 précedent
(ceci se provoque quand tu fais un pull rebase de kmz avant de kaf)

pour effacer une branche : git push origin :<branch-a-effacer>

---

si tu as ce message lors de `./integrate.rb kann-models-zoo`:

```bash
┌─[dangulo@coolup92]─[/work1/dangulo/kaf] ± aci/dangulo/eval-json
└─▶ ./integrate.rb kann-models-zoo
BRANCH is aci/dangulo/eval-json
Destination branch is eval-json
Nothing to integrate. Add submodules to index first
```

faire donc `git reset —hard origin/main` à partir de kaf, une fois on a effacé les branches remotes avant.