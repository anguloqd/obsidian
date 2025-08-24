## 08 // les choix intertemporels

### La contrainte budgétaire

On considère un individu et deux périodes :

- Le présent (période 1)
- Le futur (période 2)

On considère aussi deux actions :

- Consommer
- Épargner/emprunter

La consommation est notée $c_1$ et $c_2$, le revenu est noté $m_1$ et $m_2$.

#### Formulation générale

La contrainte budgétaire s'écrit :

$$
p_1c_1 + p_2c_2 = p_1m_1 + p_2m_2
$$

#### Cas sans inflation

S'il n'y a pas d'inflation, la contrainte budgétaire est standard :

$$
p_1c_1 + p_2c_2 = m
$$

#### Cas avec inflation

Si l'inflation existe, on peut réécrire la contrainte budgétaire de deux manières :

1. **Perspective présente** : $p_1 = 1$ et $p_2 = \frac{1}{1+r}$
   - Le prix du présent est l'unité
   - $c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r}$

2. **Perspective future** : $p_1 = (1+r)$ et $p_2 = 1$
   - Le prix du futur est l'unité
   - $(1+r)c_1 + c_2 = (1+r)m_1 + m_2$

#### Représentation graphique

La contrainte budgétaire a une pente de $-(1+r)$ (ou $-\frac{1}{1+r}$ selon la perspective).

- Le point d'intersection avec l'axe horizontal est $m_1 + \frac{m_2}{1+r}$ (valeur présente des revenus)
- Le point d'intersection avec l'axe vertical est $(1+r)m_1 + m_2$ (valeur future des revenus)

### Statique comparative

Effets d'une variation du taux d'intérêt :

- Si consommateur est prêteur et $r$ augmente, sa satisfaction augmente
- Si consommateur est emprunteur et $r$ diminue, sa satisfaction augmente
- Si consommateur reste prêteur et $r$ diminue, sa satisfaction diminue
- Si consommateur reste emprunteur et $r$ augmente, sa satisfaction diminue

#### Représentation graphique

Une augmentation du taux d'intérêt fait pivoter la droite de budget autour du point $(m_1, m_2)$, rendant la pente plus raide.

### L'inflation

Jusqu'à présent, on avait considéré que les prix de consommation présente et future restaient constants. Considérons maintenant le cas où il y a inflation.

- $p_1$ est toujours égal à l'unité
- $p_2 = 1 + \pi$ où $\pi$ est le taux d'inflation

#### Le taux d'intérêt réel

>[!definition] Taux d'intérêt réel
>Le taux d'intérêt réel $\rho$ est défini comme :
>
>$$
>(1 + \rho) = \frac{1 + r}{1 + \pi}
>$$
>
>On substitue $(1 + \rho)$ où il y avait $(1 + r)$ précédemment.

Si le taux d'inflation est faible, on peut approximer $\rho \approx r - \pi$

#### Impact sur les choix intertemporels

Avec inflation, la contrainte budgétaire devient :

$$
c_1 + \frac{c_2}{(1 + \rho)(1 + \pi)} = m_1 + \frac{m_2}{(1 + \rho)(1 + \pi)}
$$

Ou, en simplifiant :

$$
c_1 + \frac{c_2}{1 + \rho} = m_1 + \frac{m_2}{1 + \rho}
$$

>[!important]
>C'est le taux d'intérêt réel, et non le taux nominal, qui gouverne les décisions intertemporelles de consommation.
