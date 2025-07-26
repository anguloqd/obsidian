# 06 // projet prolog : algo. pour jouer le dilemme des prisonniers

Date de création: April 28, 2023 2:59 PM
Modifié: June 10, 2023 12:47 PM

## Expliquant *graduel*

> Graduel joue “coopération” toujours au premier coup. Après, il continue à joue “coopération” jusqu’à ce qu’il est trahi pour la $n$-ième fois, dans ce cas il punira avec $n$ “trahisons” consécutives, puis il se relâchera avec deux coopérations consécutives inconditionnelles. Le nombre de trahisons dans les punissions augmente “graduellement”, d’où son nom.
> 

<aside>
💻 L’algorithme de graduel se décrit en trois états : normal, punir et relax. En état normal, graduelle attend une trahison pour punir, sinon il continue à coopérer. En état punir, il commence un suite consécutive de trahisons ($n$ trahisons s’il a été trahi pour la $n$-ième fois). En état relax, il “pardonne” a son adversaire avec deux coopérations consécutives, puis il revient en état normal.

$\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space \text{Algorithme : graduel}
\\
\text{}
\\$

1. Je suis au premier coup ?
Oui → coopération, rentre état normal
2. Je suis en état “normal” ? Oui →
    1. Lors du dernier coup, l’adversaire a coopéré ?
    Oui → coopération, garde état “normal”
    2. Lors du dernier coup, l’adversaire a trahi ?
    Oui → trahison, rentre état “punir”
3. Je suis en état “punir” ? Oui →
    1. Il manque plus d’une trahison à faire ?
    Oui → trahison, garde l’état “punir”
    2. Il ne manque qu’une trahison à faire ?
    Oui → trahison, rentre en état “relax”
4. Je suis en état “relax” ? Oui →
    1. Je n’ai pas coopéré le coup précédant ?
    Oui → coopération, garde l’état “relax”
    2. J’ai relâché (cooperé) aussi le coup précédant ?
    Oui → coopération, rentre en état “normal”
</aside>

## Le code : *graduel* (version .txt en lien pour copier-coller)

[graduel ANGULO.txt](graduel_angulo.txt)

```prolog
% prédicat principal
jouer(graduel, L, R) :- L=[], R=c;
    not(grEnEtatRelax(L)), not(grEnEtatPunir(L)), not(grVientDeTrahir(L)), R=c; % état normal
    not(grEnEtatRelax(L)), not(grEnEtatPunir(L)), grVientDeTrahir(L), R=t; % état punir : commence les punissions
    not(grEnEtatRelax(L)), grEnEtatPunir(L), grIlManquePunissions(L), R=t; % état punir : finit les punissions
    grEnEtatRelax(L), R=c. % etat relax

% prédicats supplémentaires
% sont marqués avec "gr" en prefixe pour "graduel"

% explication : le algo est en etat relax si...
grEnEtatRelax(L) :-
		% on était en etat punir mais il ne reste aucune trahison à jouer, donc on a fini
    grEnEtatPunir(L), not(grIlManquePunissions(L));
		% ou si on avait déjà rentré dans le état relax et on a coopéré une fois
    not(grEnEtatPunir(L)), grJaiRelacheUneFois(L).

% explication : il manque des punissions si...
grIlManquePunissions(L) :-
		% on compte les trahisons de le adversaire avant de ma dernier coopération
    grHistDepuisMaDernCoop(L, LaPartirDeDernC), grNbTrahisons(LaPartirDeDernC, NbTrahisonsAdvCumulees), 
    % on compte les punissions que jai donné jusque là
		grNbMesTrahisonsAvantMaDernCoop(L,NbMesTrahisonsEnCours),
    % si il elles ne sont pas encores les memes, il manque donc des punissions à jouer
		NbMesTrahisonsEnCours < NbTrahisonsAdvCumulees.

% explication : jai relaché une fois si mon dernier coup était coopération
grJaiRelacheUneFois([[A,_],[C,_]|_]) :- C=t, A=c.
% explication : je suis en état punir si mon dernier coup était trahison
grEnEtatPunir([[A,_]|_]) :- A=t.
% explication : adversaire vient de trahir si son dernier coup était trahison
grVientDeTrahir([[_,B]|_]) :- B=t.

% utilitaire : donnée une histoire L, compte le nombre de trahisions N de le adversaire
grNbTrahisons(L,N) :-
    L=[], fail;
    L=[[_c]], N=0;
    L=[[_t]], N=1;
    not(L=[[__]]), L=[[_,B]|Reste],
        grNbTrahisons([[_b]], NListeCourante), grNbTrahisons(Reste, NReste),
        N is (NListeCourante + NReste).

% utilitaire : donnée une histoire L1,
% retourne la histoire L2 du debut jusquà ma dernière coopération 
grHistDepuisMaDernCoop(L1, L2) :-
    L1 = [[c_]], L2 = [[c_]];
    L1 = [[t_]], L2 = [[]];
    not(L1=[[__]]), L1 = [[A,B]|Reste], A=c, L2=Sol, append([[ab]],Reste,Sol);
    not(L1=[[__]]), L1 = [[A,_]|Reste], A=t, L2=Sol, grHistDepuisMaDernCoop(Reste, Sol).

% utilitaire : donnée une histore L,
% retourne la quantité de trahisons N que jai fait avant ma dernière coopération
grNbMesTrahisonsAvantMaDernCoop(L, N) :-     
    L=[], N=0;
    L=[[c_]], N=0;
    L=[[t_]], N=1;
    L=[[A,_],[C,_]|Reste],
        (A=c, !, N=0;
        A=t, C=c, !, N=1;
        A=t, C=t, grNbMesTrahisonsAvantMaDernCoop(Reste, NReste), N is (2+NReste)).
```