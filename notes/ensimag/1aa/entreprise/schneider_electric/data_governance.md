Notes de la présentation de Lionel sur la Data Governance, 04/08/2025

![](ensimag/1aa/entreprise/schneider_electric/ressources/Data_Gov+Quick_LIMS_Intro.pptx)

---

F-Labs a plus de 100 ans !! Laboratoire d'essais
activites : test - verif - valid - certif
type d'essais ! mecaniques, diéletriques, CEM, court-circuit, endurance, electrique
F-Lab fait partie de "OneLabs" qui contient G-Lab, S-Lab, C-LAB, NA-Lab, I-Lab

-   Stéphanie : manageuse de F-Lab
    -   Marc: responsable HD (produits différentiels), equipe PTL: interface de demandeur d'essaie et le lab
    -   Geoffrey: Equipe PP. Produit plus gros (infra electriques plus gros)
    -   Laetita, équipe ClimVib: essaies dimmensionels, climatiques, vibrationnels, un peu de méca
    -   Alexandre, equipe fonctionnel: fonctionnement general des produites.
    -   Grégory, équipe puissance: court-circuits (technopole, labo volta)
    -   Nicolas, Digital Cluster: on fait pas des tests, essais de verif-valid
        -   Atol: permet de faire tourner des tests qui sont utilisés par les autres équipes
        -   Data: nous :)
        -   RDITS: partisants de la digitalisation

Dataflow:

## 1. Création
les donnees ont des metadata generique et des custom metadata. on utilise LabView ou TestStand (ce dernier pour Atol). National Insturments est le propietaire de ce deux softwar, ses fichiers sont en extension ".tdms".

## 2. Data collection
Les donnes vont du network test au datalake (raw_data). On utilise le software Labs Supervision. on peut definir un intervalle de collection en temps.

## 3. Data indexing, avec SystemLink
Prend les metadata des fichiers pour pouvoir faire des recherches avancées à travers d'une API. Utile avec des databases avec des TBs de données.
Pour des fichiers tdm ou tdms, ça se fait très vite. Pour les xls, il faut un peu plus de travail, utilisant un "DataPlugin"" pour faire identifier les metadata du xls.

## 4. Data consumption using the API 5accesibility
Self-explanatory. Using Lims aussi. or Labs Supervision (search engine feature: "one search").
Une requête sur la database est une pipeline de conditions boolénnes.

## 5. Data analysis
Data science project.

## 6. Data archiving
...


---

# LIMS: laboratory information management system

Dataflow to perform and specification test:
1. requester: client exterieur, create test specification (une test spec), this is a formulary, with ID like "SPECXXXXXX"
2. test manager: approve and plan the test, affects aSn operator to perform the test
3. test operator: performs the test, prepare, test, write the report (doing the dataflow from before)
4. test manager: approve test report 
5. requester: analyze the result

une syncronisation est le fait de prendre un fichier de la baie et l'envoyer au datacenter (datalake), utilisant Labs Supervision et les prises de réseau.