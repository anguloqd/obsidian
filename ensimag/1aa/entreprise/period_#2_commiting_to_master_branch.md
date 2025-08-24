## Period #2 - Commiting to master branch

- Before anything, make sure you have configured your profile following the steps in Training slides.
- After that, in a new repo you just cloned, run `installCommitHook` for the first time.
- Create a branch `aci/dangulo/master` to the `kann-models-zoo` and `kaf` repos.
- Stage changes.
- Do `git commit`. It will open a nano editor where you enter the commit message. Write the message before the commented lines. Do not erase the commented lines. Save and exit.
    - Don’t forget to add the JIRA link to the concerned task.
- Do `kerrit -r qmuller -r lmahieu`.
    - This last step will add the “Link: link-to-gerrit.kalray.eu” automatically.

If you ever do modifications to that commit:

- Do the modifications to the concerned files.
- Do `git add -p` or stage changes directly.
- Do `git commit --amend`. You can choose to not change the commit message, just save and exit.
- Do `kerrit`.

Let’s say you did a mistake by committing files you did not want to commit. So :

```bash
# here, the file you want to remove from commit BUT not supress from local
git rm -cached unit_tests.py
git commit --amend --no-edit
git log -1 --stat | grep unit_tests # you shouldnt see the file
kerrit
```

Another thing : rebase (using pickups) and squash-ups (rebase using fix). We want each commit to represent a feature, and ideally we want them to be independent of one another. This independence allow us to reorder a history of commits and for it to work.

If we ever want to “merge” one commit into another, we use “rebase with fix”.

From kaf : `./integrate.rb kann-models-zoo` after the kerrit

---

creer une branche “release6.1”
