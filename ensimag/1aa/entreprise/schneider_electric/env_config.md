# Liste de configurations pour mon environnement

-   Trellix: toujours "Quick settings > activer les groupes limités du Pare-feu", dans ta barre d'icônes

-   Installer avec apt: dans "/etc/apt/apt.conf.d/95proxies", appender :
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