# 00 // notes interrogation

# Première interrogation

- j’ai oublié de spécifier la significativité du test de fisher dans le commentaire des résultats (5%, elle la donne) et aussi “sous respect des hypothèses”
    - Aussi j’ai oublié rédiger une phrase plus économique “la relation n’est pas significative”.
- J’ai oublié la formule de la statistique de fisher avec $R^2$ directement
    
    $$
    F=\frac{SCE/k}{SCR/\big(n-(k+1)\big)}=\frac{R^2/k}{(1-R^2)/\big(n-(k+1)\big)}\sim \mathcal F(v_1=k,v_2=n-k-1)
    $$
    
- Signe du coefficient du facteur prix (y= cigs, x_1=prix). Il se peut que ce signe soit contre-intuitif. Tu peux rester tranquille si la qualité d’ajustement est très faible, donc les coefficients sont “cacahuètes”.
- Quand on passe de regression simple à multiple et que le signe d’un facteur change…..
- Comment comparer deux modèles différents ? → Avec le $R^2$ ajusté !
- Comment on pourrait faire mieux pour une regression multiple?