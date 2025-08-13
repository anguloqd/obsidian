Reunion avec Lionel, 11/08/2025

---

ça concerne Paul Galvin, qui réalise les essaies court-circuits.
fichier court_circuitv5.2.xls, demande arrive par LIMS
faire des specs à partir de templates natives à lims, section "test parameters" à la colonne gauche de lims. normalement les mêmes champs que la fiche excel.

Postman

requete API juste fourni les infos de la première colonne.
ecrire la requete API dans l'excel

flow: LIMS (selectionne template, replit les metadata, click sur "ACTION") ->  Paul recoit la fiche Excel, doit remplit les infos à la main depuis Lims sur la fiche.

Probleme de template : a la base y'avait pas un reglage "number of columns" pour les multi colonnes. Sauf que le formulaie classique ne prend que la première colonne, section "Specification des essais" de la fiche.

---

Workflow de Paul :

Emplacement Reseaux : RDITS-ALPETTE : 1-Geston Enregistrement Essai... et 2-Station de Court-circuit
POINT DE VIGILANCE; **TOUTES** les macros doivent marcher ; les données rentrés par l'utilisateur doit être en numérique lorsque c'est necessaire (e.G. Tension Essai en V: 7500 et non pas sept-mille cinq cent; Courant Essai en A... Cos-phi pas necessaire). VERIFIER la compatibiliter des macros avec la version d'Excel, que ça marche avec Windows 11 ou Windows 7... puisque les macros sont très vielles.

1-Gestion-Enrigistrement-Essai (lien réseau windows RDITS-ALPETTE) -> on trouve la fiche court-circuit v5.2
Lorsque le client save le fichier, il est gardé dans un autre dir: "Station de Court-circuit -> Demandes d'essais non validées", puis que le client fasse copier et le coller dans LIMS.

(Dans lims on peut faire mieux: utilise "création de speification d'éssai" -> "à partir du template")

INFO IMPORTANT: NUMERO PLATEFORME E.G. CC2_2025_052. C le nombre de l'essai dans le logiciel CC.

Après au debut du spec, qqun vient reviser que tout est en ordre, puis click sur "valider la demande d'essai", puis on remplit les "informations testeur" dans la fiche