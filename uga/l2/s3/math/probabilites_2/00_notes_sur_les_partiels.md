## 00 // notes sur les partiels

## Contrôles de l'année passée

### Évaluation d'une intégrale suite à IPP

**Erreur fréquente** : Lors de l'intégration par parties d'une intégrale définie, l'évaluation aux bornes s'applique à **toute** l'expression $uv - \int v \, du$, pas seulement à l'intégrale restante.

**Formule IPP** : $\int u \, dv = uv - \int v \, du$

$$\begin{align}
\text{Correct :} \quad &\int_0^\infty x^2e^x \, dx = \left[x^2e^x - 2\int x e^x \, dx\right]_0^\infty \\[0.5em]
\text{Incorrect :} \quad &\int_0^\infty x^2e^x \, dx = x^2e^x - 2\int_0^\infty x e^x \, dx
\end{align}$$

**Méthode correcte** :
1. Appliquer IPP pour obtenir l'expression complète
2. Évaluer **toute** l'expression aux bornes
3. Continuer avec les intégrales restantes si nécessaire

### Intégration des fonctions paires et impaires

Pour les intégrales définies sur des intervalles symétriques $[-a, a]$ :

**Fonction paire** : $f(-x) = f(x)$

$$\int_{-a}^a f(x) \, dx = 2\int_0^a f(x) \, dx$$

**Fonction impaire** : $f(-x) = -f(x)$

$$\int_{-a}^a f(x) \, dx = 0$$

**Justification géométrique** :
- Fonction paire : symétrie par rapport à l'axe des ordonnées → les aires se doublent
- Fonction impaire : symétrie par rapport à l'origine → les aires s'annulent

**Exemples** :
- $\cos(x)$, $x^2$, $|x|$ sont paires
- $\sin(x)$, $x^3$, $x$ sont impaires

### Relation entre LGN et TCL

Soit $\bar{X}_n$ la moyenne empirique de $n$ V.A. iid avec $\mathbb{E}[X_i] = \mu$ et $\text{Var}(X_i) = \sigma^2 < \infty$.

**Loi des Grands Nombres (LGN)** : Convergence de la moyenne vers l'espérance

$$\lim_{n\rightarrow\infty} P(|\bar{X}_n - \mu| \leq \epsilon) = 1, \quad \forall \epsilon > 0$$

**Théorème Central de la Limite (TCL)** : Vitesse de convergence et distribution limite

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \stackrel{d}{\rightarrow} \mathcal{N}(0,1)$$

#### Formulations équivalentes

**LGN** (convergence en probabilité) :

$$\bar{X}_n \stackrel{P}{\rightarrow} \mu$$

**TCL** (convergence en loi de la version normalisée) :

$$\sqrt{n}(\bar{X}_n - \mu) \stackrel{d}{\rightarrow} \mathcal{N}(0, \sigma^2)$$

#### Approximation pratique du TCL

Pour $n$ suffisamment grand (règle empirique : $n \geq 30$) :

$$\bar{X}_n \stackrel{approx}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

**Attention** : Cette approximation est valide pour $n$ fini mais grand. Si $n \rightarrow \infty$, la variance tend vers $0$ et on retrouve la convergence de la LGN.

#### Variables aléatoires dégénérées

Quand $n \rightarrow \infty$, la distribution de $(\bar{X}_n - \mu)$ devient **dégénérée** (concentrée en $0$).

**Fonction de répartition limite** :

$$F(x) = \begin{cases}
0, & x < 0 \\
1, & x \geq 0
\end{cases}$$

Cette fonction correspond à la **mesure de Dirac** $\delta_0$.

**Caractéristiques** :
- Toute la masse de probabilité est concentrée en un point
- Pas de densité au sens usuel
- Variance nulle

**Pourquoi la normalisation $\sqrt{n}$ ?**

La normalisation par $\sqrt{n}$ dans le TCL permet :

1. D'obtenir une limite non dégénérée
2. De révéler la vitesse de convergence : $O(1/\sqrt{n})$
3. De maintenir une variance finie et non nulle dans la limite

> [!important] **Point clé**
>
> La LGN et le TCL décrivent le même phénomène à des échelles différentes :
> - **LGN** : $\bar{X}_n \approx \mu$ (convergence de la moyenne)
> - **TCL** : $\bar{X}_n - \mu \approx \mathcal{N}(0, \sigma^2/n)$ (distribution des fluctuations)

## CC1

### Question 1.a : Test d'Alembert

Si le test d'Alembert $\lim_{n\rightarrow\infty} \left|\frac{u_{n+1}}{u_n}\right|$ ne converge pas ou converge vers $1$, le test est **inconclusif**. Il faut alors utiliser d'autres critères (Cauchy, comparaison, etc.).

### Question 2.a : Ré-indexation de séries

Pour simplifier une série, on peut **ré-indexer** en changeant la variable de sommation :

$$S = \sum_{k=0}^\infty \frac{k}{(k+1)!} = \sum_{k=1}^\infty \frac{k-1}{k!} = \sum_{k=1}^\infty \frac{k}{k!} - \sum_{k=1}^\infty \frac{1}{k!}$$

**Techniques utiles** :
- Décomposer en plusieurs séries
- Utiliser les propriétés d'exponentielles/factorielles
- Reconnaître des séries de Taylor connues

### Question 2.e : Séries de Taylor avec termes alternés

**Attention** : Certaines séries ont des termes alternés même si la série de Taylor de base n'est pas alternée.

**Exemple** :

$$e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$e^{-x} = \sum_{k=0}^\infty \frac{(-x)^k}{k!} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots$$

**Piège fréquent** : Si la série de Taylor commence à $k=0$, attention au terme constant lors des manipulations !

**Exemples utiles** :
- $\sin(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}$
- $\cos(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$
- $(1+x)^{\alpha} = \sum_{k=0}^\infty \binom{\alpha}{k} x^k$ pour $|x| < 1$

## CC2

### Conseil pratique

**Vitesse d'intégration** : Travailler l'efficacité dans le calcul d'intégrales. Mémoriser les primitives usuelles et maîtriser les techniques :

**Méthodes principales** :
- Changement de variable
- Intégration par parties
- Décomposition en éléments simples
- Fonctions paires/impaires
- Propriétés trigonométriques

**Primitives à connaître parfaitement** :
- $\int \frac{1}{x} dx = \ln|x| + C$
- $\int e^{ax} dx = \frac{1}{a}e^{ax} + C$
- $\int \sin(ax) dx = -\frac{1}{a}\cos(ax) + C$
- $\int \cos(ax) dx = \frac{1}{a}\sin(ax) + C$
- $\int \frac{1}{1+x^2} dx = \arctan(x) + C$
- $\int \frac{1}{\sqrt{1-x^2}} dx = \arcsin(x) + C$
