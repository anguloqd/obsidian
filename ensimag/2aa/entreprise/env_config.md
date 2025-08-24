## Liste de configurations pour mon environnement

-   Trellix : toujours "Quick settings > activer les groupes limités du Pare-feu", dans ta barre d'icônes

-   WSL2 : https://github.schneider-electric.com/RnDUtils/wsl_installer
    IL EST IMPERATIF D'INSTALLER LA VERSION ENTREPRISE AU LIEU DE FAIRE `wsl --install`,
    C'EST DEJA CONFIGURE EN TERMES D'ENVIRONNEMENT ET DE PROXY.
    Il ne faut pas cloner le repo, juste télécharger la release.
    Elle se trouve vers la droite de la page dans la section "releases" avec un nom comme "v0.1.0-rc.6"

-   Installer avec apt : dans "/etc/apt/apt.conf.d/95proxies", appender :

    ```
    Acquire::http::Proxy "http://SESA816159:brbxJ6g^hJPjqr@gateway.schneider.zscaler.net:80/";
    Acquire::https::Proxy "http://SESA816159:brbxJ6g^hJPjqr@gateway.schneider.zscaler.net:80/";
    ```

    -   python-is-python3
    -   python3-virtualenv
    -   virtualenv

-   Installer avec pip : `pip install --proxy http://gateway.schneider.zscaler.net:80/ <pkg>`
    - pandas (et fastparquet pour .parq, ne pas installer pyarrow !), matplotlib, seaborn

-   Configurer proxy dans git : `git config http.proxy http://gateway.schneider.zscaler.net:80/`

-   Configurer Git LFS :

    ```
    sudo apt update
    sudo apt install git-lfs
    git lfs install
    git lfs track "*.pptx"
    git add .gitattributes
    git rm --cached "ensimag/1aa/entreprise/schneider_electric/ressources/Data_Gov+Quick_LIMS_Intro.pptx"
    git add "ensimag/1aa/entreprise/schneider_electric/ressources/Data_Gov+Quick_LIMS_Intro.pptx"
    git commit -m "use git lfs for pptx files"
    git config lfs.https://github.com/anguloqd/obsidian.git/info/lfs.locksverify false
    git config lfs.locksverify false
    git push
    ```

- Configurer Copilot : deux pages à suivre. La premère est https://confluence.se.com/spaces/DXT/pages/479635159/Github+Copilot-+Getting+Started, puis elle pointe vers une deuxième page : https://confluence.se.com/spaces/DXT/pages/297784534/GitHub+Proxy+SetUp+for+the+Github+copilot
    - Dans la section "Steps to obtain a license", click dans le lien "**Create a ticket** as a Github Issue…", le titre de telle page étant "Developer Experience Application Issue".
    - Puis fait click dans le lien "To raise a License request related to applications under Developer Experience please click **Here**". Le titre de la nouvelle page devrait être "R&D Application License Change Request". Là tu peux faire la demande.
    - Après tout, si ça n'a pas marcher, verifier que WSL2 est bien installé (version entreprise, pas version proxy).
    Il faudrait suivre le document "WSL-Mirrored-Mode 6" et placer les fichier attachés dans des endroit spécifiques dans WSL file system.
    

- Configure accès à GitHub Schneider Electric : un owner doit donner accès.
