# Period #2 - kann-models-zoo in kaf

```bash
# In kaf folder, with Quentin
git pull --rebase origin master
git rebase --abort
git reset --hard
git reset --hard origin/master
git submodule update --recursive

# kann-models-zoo folder now exists but it is empty
# Inside kaf/kann-models-zoo, do
git submodule update --init --recursive

# There was an incomptability with the toolchain's version (5.3.0) and kann's (5.5.0).
# So we need to update the toolchain
# From kaf :
./get_valid_packages.sh -v

# Now the ./run (...) command in kann-models-zoo works.
```

Context: the kann-models-zoo submodule has been migrated into kaf, whereas before it was a module/repo independent of kaf.