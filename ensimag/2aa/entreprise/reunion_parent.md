temps de o et f non classifié
pour certain prods il est très compliquée de determiner la ouverture, signature compliquée
signal de la tension bobine qui (algo non trouvée pour bien se posicioner le curseur pour calculer le temps d'ouverture). curseur est fixé après.
9 occurrences de ce problème

tensions qui trainent longtemps derriere (plus à droite dans une ligne temporelle) la vrai ouverture (fermeture?). 

produits: f150, f250, problèmes pareils
signales en tdms dans DIADEM : ubob1 (fin de tension de bobine, quelque part...), 6i1 (debut de courant), i1 (fin de courant), v1 (debut de tension bobine). Temps d'ouverture quand ça se : rebond de ubob1 - debut d'arc de i1 (mais on retourne 30 ms).

SUR DIADEM, LA COUPURE EST LE REBOND VISUEL de V1, VERS LA DROITE.

c'est l'energie magasiné dans une bobine après la fin de la commande qui nous retourne des temps d'ouverture négatifs. on peut voir ce comportement entre v1 et ubob1. c'est dû aux matériels de fabrication (diode) de la bobine.

durée d'arc o : si on depasse 50ms, on doit avoir un problème, peut-être un curseur mal positionné. c'est calculé I_E_PX - Va_S_PX.

energie_darc_o et _f : depend de la conception du produit, ne devraits pas forcément égaux.

energie de fermeture : ce qui différence un bon produit et un mauvais produit en AC3.

Proba de prediciton forte pour un défaut : intéraction v1 et 6i1.

Baie de mesure pour AC3 nous intéresse peu, plus intéressant pour AC1 et AC4.

Courbe de perte d'argent ? Evolution de d'ecrasements (milimètres de volume de pastille au début et fin, mésuré un baie de laser). On pourrait faire un estimation de la degradation des pastilles. Pensr en miligrames d'argent par maneouvre.

AUTOSYNCRONISATION DU PRODUIT. Rapport de Michel parent (pu9900048). Explique pourquoi un pôle suce plus qu'un autre.
Y'a de relation entre tension de commande et l'energie. Phase qui a l"energie la plus faible -> doit être le tension de commande. Normalement phase 1 dans nos essaies. Dans AC3 c'est plus tranquille. Dans AC4 ça marche bien.

Rapport (contacts electriques6-modif1). Parle de durabilité electrique (origine de l'érosion des contacts). GRaphique entre Erosion (mg/FO) et Io (A, Ampères ?), relation en linéaire en log-log.

Forme de la pastille : pas pour AC3, mais important pour AC4. Peut influence la mobilité de l'arc. Y'a des pastilles cilindriques, rectangulaires-coins-arrondies, aussi pas les mêmes diamètres ni épaisseurs. Ni le "bombai". Pas le même procédé d'obtention de pastille non plus, pas les mêmes aléages.

---

Bloquée à 30 ms -> Arc permanent !
Contact quand il est neuf : rebondit très peux. lorsque le rebond depasse 30ms, c en'est plus un rebond, c'est une reouverture (et ça refait un arc, un arc permanent !!). Temps de rebond donc dans les données ça devrait être 30ms. Et souvant ça arrive vers la fin de vie.
La limite de 30ms a été fixé lors du developpement des algorithmes.
Lors de la dernière manioevre, train de rebond se voit dans le signal v2, celui a provoqué la soudure, à trouvé lors d'une descente forte du v2.

---

plateforme : rdits-beec.se.com, cherche la spec.
journal d'évenemments (défauts, reprises...)
PCM fermé -> contacteur a soudé.

---

dure d'arc de rebond <= duree de train de rebond
6i : AC3
i : AC4
AC1 ?

6I_S_P1 - > 6i (courant), Start (fermeture), P1 (pôle 1)
V0_P3 -> enclenchements
Va_S_P1 -> debut d'arc (fin de courant - début coupure (short-cirucit))
Vr_E -> fin de tension de rebond, ouverture
Uc_S -> début de commande

Tension appliqué : f(début de courant) - f(20ms avant début de courant). Est souvent une moyenne, surtout en AC3
En AC3 tu as deux tensions différentes

La tension d'un pôle fermé est zéro. Il est soudé ! 
LE bon ordre des grpahes en diadem : ubob4, v1, 6i1, i1.
tension superieure à 17v -> banc pense que le pôle est ouvert.

Temps de commende : temps déduite de temps de fermeture et temps de montée, donc si ceux-là ont des erreurs, temps de tension de commande aussi.

Fin de rebond (à gauche) et début d'arc (à droite) se voit dans v1. il sont séparés par un temps où 6i1 et puis i1 sont actifs. ce temps 'éteint' est l'energie d'arc.

--------------

Ce qui coûte cher dans le produit est le cuivre et de l'argent.
Une bonne quantité d'argent permet d'aller plus loin dans la quantité de maneouvres (nb de cycles).
Argent graphite ne peut pas souder, utilisé dans les disjoncteur.
Poule de perlimpinpin : 12% oxide de tin, 88% argent (aléage d'argent).

Prendre les 200 première manioeuvres, prendre energie d'arc total sur 1000 maneouvres à partir de la 100e manouevre. Determine la pente des pastilles de "pintre???". Combien de temps ça prends la vie de pastilles ? La forme de pastilles va être important aussi. On doit voir AUSSI POURQUOI le contacteur est mort. 

En AC1 et AC4, le materiau plastique du boitier influence l'energie d'arc total. En AC3 non.

Loi de Weibull ????

Maintenant on s'arrête forcément quand on arrive à 150% de durée de vie.
Phase de commande est syncrone avec la phase 1. On coupe aleatoirement. "Autosyncronisation des bobines". On fait en sorte qu'on coupe toujours sur la même phase. ça arrive plus sur les bobines continus ou electroniques. 

instant_de_séprataion_des_contacts : lorsque ça arrive à 50ms, 80% de proba que le produit a soudé. Mais le boxplot de Daniela dit bien le contraire !

Quand on a de spoints abérrant, on doit regardes les 4 courbes. Oscillogramme !

Défaut durant puverture sur pôles 1 & 3 -> pôlé 2 a soudé. Pôle 2 est plus usé.

---

Doc: cahier des charges des algorithmes.

---

Finalement, variables à preioriser : quantité d'argent dans les pastilles, écrasement, P2 (pression de pôles).