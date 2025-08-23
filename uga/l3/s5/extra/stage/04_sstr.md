# 04 // sstr

# SSTR : Synthetic Season-Trend-Residual, un module pour les séries synthétiques

Ce module SSTR permet de générer des séries temporelles synthétiques avec des composantes de tendance, saisonnalité et résidus contrôlées. Il est particulièrement utile pour tester les performances d'algorithmes de détection de ruptures comme BEAST, car on connaît la position exacte des vraies ruptures.

## API

### Classe `SSTR`

```python
import numpy as np
import pandas as pd
import warnings
from datetime import datetime
from typing import List, Optional, Union, Literal

class SSTR:
    """
    Générateur de séries temporelles synthétiques avec composantes de tendance, 
    saisonnalité et résidus contrôlées.
    
    Cette classe permet de créer des séries temporelles artificielles avec des 
    ruptures structurelles définies, utiles pour évaluer les performances 
    d'algorithmes de détection de changements.
    
    Attributes:
        t (pd.DataFrame): DataFrame contenant la série temporelle et ses composantes
        length_years (float): Durée de la série en années
        resolution (str): Résolution temporelle de la série
        start_date (datetime): Date de début de la série
        missing_data_proportion (float): Proportion de données manquantes
        trend (Trend): Composante de tendance
        season (Season): Composante saisonnière  
        residual (Residual): Composante résiduelle
    """
    
    def __init__(
        self,
        length_years: float = 50,
        resolution: str = "1 months",
        start_date: datetime = None,
        missing_data_proportion: float = 0,
        idx_as_date: bool = False,
        # paramètres saisonnalité
        season_period: float = 1,
        season_phase: float = 0,
        season_breaks_idx: Optional[List[int]] = None,
        season_breaks_mag: Optional[List[float]] = None,
        season_harm_ord: List[int] = [1],
        season_amp_sin: Optional[np.ndarray] = None,
        season_amp_cos: Optional[np.ndarray] = None,
        # paramètres tendance
        trend_initial_y: float = 0,
        trend_slp: List[float] = [0],
        trend_breaks_mag: Optional[List[float]] = None,
        trend_breaks_idx: Optional[List[int]] = None,
        # paramètres résidus
        res_dist: Literal["normal", "uniform"] = "normal",
        res_u: float = 0,
        res_sigma: float = 0
    ):
        """
        Initialise une série temporelle synthétique.
        
        Args:
            length_years: durée de la série en années
            resolution: résolution temporelle (ex: "1 months", "2 weeks")
            start_date: date de début (par défaut: aujourd'hui)
            missing_data_proportion: proportion de données manquantes [0,1]
            idx_as_date: si True, utilise des dates comme index
            season_period: période saisonnière
            season_phase: déphasage saisonnier
            season_breaks_idx: indices des ruptures saisonnières
            season_breaks_mag: magnitudes des ruptures saisonnières
            season_harm_ord: ordres harmoniques par segment
            season_amp_sin: amplitudes sinusoïdales
            season_amp_cos: amplitudes cosinusoïdales
            trend_initial_y: valeur initiale de la tendance
            trend_slp: pentes par segment de tendance
            trend_breaks_mag: magnitudes des ruptures de tendance
            trend_breaks_idx: indices des ruptures de tendance
            res_dist: distribution des résidus ("normal" ou "uniform")
            res_u: paramètre de plage pour distribution uniforme
            res_sigma: écart-type pour distribution normale
            
        Raises:
            ValueError: si les paramètres d'entrée sont invalides
        """
        # validation des paramètres d'entrée
        self._validate_inputs(length_years, resolution, missing_data_proportion)
        
        if start_date is None:
            start_date = datetime.today()
        
        # calcul de la longueur de série en points de données
        length = self._calculate_length(length_years, resolution)
        
        # génération des composantes
        self.season = Season(
            length=length,
            period=season_period,
            phase=season_phase,
            breaks_idx=season_breaks_idx,
            breaks_mag=season_breaks_mag,
            harm_ord=season_harm_ord,
            amp_sin=season_amp_sin,
            amp_cos=season_amp_cos
        )
        
        self.trend = Trend(
            length=length,
            initial_y=trend_initial_y,
            slp=trend_slp,
            breaks_mag=trend_breaks_mag,
            breaks_idx=trend_breaks_idx
        )
        
        self.residual = Residual(
            length=length,
            dist=res_dist,
            u=res_u,
            sigma=res_sigma
        )
        
        # combinaison des composantes
        y = self.season.y + self.trend.y + self.residual.y
        
        # introduction de données manquantes si spécifié
        if missing_data_proportion > 0:
            missing_idx = np.random.choice(
                length, 
                size=int(round(missing_data_proportion * length)), 
                replace=False
            )
            y[missing_idx] = np.nan
        
        # création du dataframe final
        self.t = pd.DataFrame({
            "y": y,
            "season": self.season.y,
            "trend": self.trend.y,
            "residual": self.residual.y
        })
        
        # conversion de l'index en dates si demandé
        if idx_as_date:
            self.t.index = self._create_date_index(start_date, length, resolution)
        
        # stockage des paramètres
        self.length_years = length_years
        self.resolution = resolution
        self.start_date = start_date
        self.missing_data_proportion = missing_data_proportion
    
    def _validate_inputs(
        self, 
        length_years: float, 
        resolution: str, 
        missing_data_proportion: float
    ) -> None:
        """valide les paramètres d'entrée principaux"""
        if not isinstance(length_years, (int, float)) or np.isnan(length_years) or length_years <= 0:
            raise ValueError("length_years doit être un nombre positif")
        
        if not isinstance(resolution, str):
            raise ValueError("resolution doit être une chaîne de caractères")
            
        resolution_parts = resolution.split(" ")
        if len(resolution_parts) != 2 or resolution_parts[1] not in ["days", "weeks", "months", "years"]:
            raise ValueError("resolution doit être au format '1 months', '2 weeks', etc.")
        
        try:
            float(resolution_parts[0])
        except ValueError:
            raise ValueError("la partie numérique de resolution doit être convertible en float")
        
        if not (0 <= missing_data_proportion <= 1):
            raise ValueError("missing_data_proportion doit être entre 0 et 1")
    
    def _calculate_length(self, length_years: float, resolution: str) -> int:
        """calcule la longueur de série en points de données"""
        resolution_parts = resolution.split(" ")
        resolution_num = float(resolution_parts[0])
        resolution_unit = resolution_parts[1]
        
        unit_multipliers = {"days": 365, "weeks": 52, "months": 12, "years": 1}
        return int(length_years * unit_multipliers[resolution_unit] / resolution_num)
    
    def _create_date_index(
        self, 
        start_date: datetime, 
        length: int, 
        resolution: str
    ) -> pd.DatetimeIndex:
        """crée un index de dates pour la série temporelle"""
        resolution_parts = resolution.split(" ")
        resolution_num = float(resolution_parts[0])
        resolution_unit = resolution_parts[1]
        
        freq_mapping = {
            "days": f"{resolution_num}D",
            "weeks": f"{int(resolution_num * 7)}D",
            "months": f"{int(resolution_num)}MS",
            "years": f"{int(resolution_num)}YS"
        }
        
        return pd.date_range(
            start=start_date,
            periods=length,
            freq=freq_mapping[resolution_unit]
        )
```

### Classe `Trend`

```python
class Trend:
    """
    Générateur de composante de tendance avec ruptures structurelles.
    
    Cette classe crée une composante de tendance linéaire par morceaux avec
    possibilité de ruptures de pente et de niveau.
    
    Attributes:
        y (np.ndarray): valeurs de la composante de tendance
        initial_y (float): valeur initiale
        segments (dict): informations sur les segments (pentes)
        breaks (dict): informations sur les ruptures (indices et magnitudes)
    """
    
    def __init__(
        self,
        length: int,
        initial_y: float = 0,
        slp: List[float] = [0],
        breaks_mag: Optional[List[float]] = None,
        breaks_idx: Optional[List[int]] = None
    ):
        """
        Initialise une composante de tendance.
        
        Args:
            length: longueur de la série
            initial_y: valeur initiale de la tendance
            slp: pentes de chaque segment
            breaks_mag: magnitudes des ruptures de niveau
            breaks_idx: indices des ruptures
            
        Raises:
            ValueError: si les paramètres sont incompatibles ou invalides
        """
        # validation des paramètres
        self._validate_inputs(length, initial_y, slp, breaks_mag, breaks_idx)
        
        # initialisation de la série temporelle
        t = np.arange(1, length + 1)
        y = np.full(length, initial_y, dtype=float)
        
        # ajout de la fin de série aux ruptures
        if breaks_idx is None:
            breaks_idx = []
        breaks_idx_extended = breaks_idx + [length]
        
        # génération des segments
        start_idx = 0
        for k, end_idx in enumerate(breaks_idx_extended):
            # application de la pente si disponible
            if k < len(slp):
                segment_indices = slice(start_idx, end_idx)
                y[segment_indices] = (
                    y[start_idx] + 
                    slp[k] * (t[segment_indices] - t[start_idx])
                )
            
            # application de la rupture de niveau
            if k > 0 and breaks_mag is not None and k-1 < len(breaks_mag):
                y[start_idx:end_idx] += breaks_mag[k-1]
            
            # préparation du segment suivant
            if k < len(breaks_idx_extended) - 1:
                if k < len(slp):
                    y[end_idx] = y[end_idx-1] + slp[k]
                if breaks_mag is not None and k < len(breaks_mag):
                    y[end_idx] += breaks_mag[k]
            
            start_idx = end_idx
        
        self.y = y
        self.initial_y = initial_y
        self.segments = {'slp': slp}
        self.breaks = {'idx': breaks_idx, 'mag': breaks_mag}
    
    def _validate_inputs(
        self,
        length: int,
        initial_y: float,
        slp: List[float],
        breaks_mag: Optional[List[float]],
        breaks_idx: Optional[List[int]]
    ) -> None:
        """valide les paramètres d'entrée"""
        if not isinstance(length, (int, np.integer)) or length <= 0:
            raise ValueError("length doit être un entier positif")
        
        if not isinstance(initial_y, (int, float)) or np.isnan(initial_y):
            raise ValueError("initial_y doit être un nombre valide")
        
        if not all(isinstance(s, (int, float)) and not np.isnan(s) for s in slp):
            raise ValueError("toutes les pentes dans slp doivent être des nombres valides")
        
        if breaks_mag is not None:
            if not all(isinstance(b, (int, float)) and not np.isnan(b) for b in breaks_mag):
                raise ValueError("toutes les magnitudes dans breaks_mag doivent être des nombres valides")
        
        if breaks_idx is not None:
            if not all(isinstance(b, (int, np.integer)) and 1 < b <= length for b in breaks_idx):
                raise ValueError("tous les indices dans breaks_idx doivent être des entiers entre 2 et length")
        
        # validation de la cohérence entre paramètres
        if breaks_idx is not None and breaks_mag is not None:
            if len(breaks_idx) != len(breaks_mag):
                raise ValueError("breaks_idx et breaks_mag doivent avoir la même longueur")
            
            if len(slp) != len(breaks_idx) + 1:
                raise ValueError("slp doit avoir un élément de plus que breaks_idx")
        
        # avertissements pour ruptures indétectables
        if breaks_idx is not None and breaks_mag is not None and len(slp) > 1:
            for i in range(len(breaks_idx)):
                if i < len(slp) - 1:
                    slope_change = slp[i+1] - slp[i]
                    magnitude = breaks_mag[i] if i < len(breaks_mag) else 0
                    if slope_change == 0 and magnitude == 0:
                        warnings.warn(f"rupture {i} indétectable (pas de changement de pente ni de niveau)")
```

### Classe `Season`

```python
class Season:
    """
    Générateur de composante saisonnière avec ruptures harmoniques.
    
    Cette classe crée une composante saisonnière basée sur des harmoniques
    avec possibilité de ruptures dans les ordres harmoniques et amplitudes.
    
    Attributes:
        y (np.ndarray): valeurs de la composante saisonnière
        period (float): période saisonnière
        phase (float): déphasage
        segments (dict): informations sur les segments (ordres et amplitudes)
        breaks (dict): informations sur les ruptures
    """
    
    def __init__(
        self,
        length: int,
        period: float = 1,
        phase: float = 0,
        breaks_idx: Optional[List[int]] = None,
        breaks_mag: Optional[List[float]] = None,
        harm_ord: List[int] = [1],
        amp_sin: Optional[np.ndarray] = None,
        amp_cos: Optional[np.ndarray] = None
    ):
        """
        Initialise une composante saisonnière.
        
        Args:
            length: longueur de la série
            period: période saisonnière
            phase: déphasage saisonnier
            breaks_idx: indices des ruptures saisonnières
            breaks_mag: magnitudes des ruptures de niveau
            harm_ord: ordres harmoniques par segment
            amp_sin: amplitudes sinusoïdales [segments x harmoniques]
            amp_cos: amplitudes cosinusoïdales [segments x harmoniques]
            
        Raises:
            ValueError: si les paramètres sont incompatibles ou invalides
        """
        # validation des paramètres
        self._validate_inputs(
            length, period, phase, breaks_idx, breaks_mag, 
            harm_ord, amp_sin, amp_cos
        )
        
        # préparation des paramètres par défaut
        n_segments = len(breaks_idx) + 1 if breaks_idx else 1
        max_harmonic = max(harm_ord) if harm_ord else 1
        
        if amp_sin is None:
            amp_sin = np.ones((n_segments, max_harmonic))
        if amp_cos is None:
            amp_cos = np.zeros((n_segments, max_harmonic))
        
        # conversion en arrays numpy
        amp_sin = np.asarray(amp_sin)
        amp_cos = np.asarray(amp_cos)
        
        # initialisation de la série temporelle
        t = np.arange(1, length + 1)
        y = np.zeros(length)
        
        # ajout de la fin de série aux ruptures
        breaks_idx_extended = (breaks_idx or []) + [length]
        breaks_mag_extended = [0] + (breaks_mag or [])
        
        # génération des segments
        start_idx = 0
        for k, end_idx in enumerate(breaks_idx_extended):
            segment_slice = slice(start_idx, end_idx)
            
            # application des harmoniques pour ce segment
            if k < len(harm_ord):
                for harmonic in range(1, harm_ord[k] + 1):
                    # calcul des composantes sin et cos
                    sin_component = (
                        amp_sin[k, harmonic-1] * 
                        np.sin(2 * np.pi * harmonic * t[segment_slice] / period - phase)
                    )
                    cos_component = (
                        amp_cos[k, harmonic-1] * 
                        np.cos(2 * np.pi * harmonic * t[segment_slice] / period - phase)
                    )
                    
                    y[segment_slice] += sin_component + cos_component
            
            # application de la magnitude de rupture
            if k < len(breaks_mag_extended):
                y[segment_slice] += breaks_mag_extended[k]
            
            start_idx = end_idx
        
        self.y = y
        self.period = period
        self.phase = phase
        self.segments = {'harm_ord': harm_ord, 'amp_sin': amp_sin, 'amp_cos': amp_cos}
        self.breaks = {'idx': breaks_idx, 'mag': breaks_mag}
    
    def _validate_inputs(
        self,
        length: int,
        period: float,
        phase: float,
        breaks_idx: Optional[List[int]],
        breaks_mag: Optional[List[float]],
        harm_ord: List[int],
        amp_sin: Optional[np.ndarray],
        amp_cos: Optional[np.ndarray]
    ) -> None:
        """valide les paramètres d'entrée"""
        if not isinstance(length, (int, np.integer)) or length <= 0:
            raise ValueError("length doit être un entier positif")
        
        if not isinstance(period, (int, float)) or period <= 0:
            raise ValueError("period doit être un nombre positif")
        
        if not isinstance(phase, (int, float)) or np.isnan(phase):
            raise ValueError("phase doit être un nombre valide")
        
        if breaks_idx is not None:
            if not all(isinstance(b, (int, np.integer)) and 1 < b <= length for b in breaks_idx):
                raise ValueError("tous les indices dans breaks_idx doivent être entre 2 et length")
        
        if breaks_mag is not None:
            if not all(isinstance(b, (int, float)) and not np.isnan(b) for b in breaks_mag):
                raise ValueError("toutes les magnitudes dans breaks_mag doivent être des nombres valides")
        
        if not all(isinstance(h, (int, np.integer)) and h > 0 for h in harm_ord):
            raise ValueError("tous les ordres harmoniques doivent être des entiers positifs")
        
        # validation de cohérence entre paramètres
        if breaks_idx is not None and breaks_mag is not None:
            if len(breaks_idx) != len(breaks_mag):
                raise ValueError("breaks_idx et breaks_mag doivent avoir la même longueur")
            
            if len(harm_ord) != len(breaks_idx) + 1:
                raise ValueError("harm_ord doit avoir un élément de plus que breaks_idx")
        
        if amp_sin is not None:
            amp_sin = np.asarray(amp_sin)
            expected_segments = len(breaks_idx) + 1 if breaks_idx else 1
            if amp_sin.shape[0] != expected_segments:
                raise ValueError("amp_sin doit avoir autant de lignes que de segments")
        
        if amp_cos is not None:
            amp_cos = np.asarray(amp_cos)
            expected_segments = len(breaks_idx) + 1 if breaks_idx else 1
            if amp_cos.shape[0] != expected_segments:
                raise ValueError("amp_cos doit avoir autant de lignes que de segments")
```

### Classe `Residual`

```python
class Residual:
    """
    Générateur de composante résiduelle avec différentes distributions.
    
    Cette classe crée une composante de bruit blanc selon une distribution
    normale ou uniforme.
    
    Attributes:
        y (np.ndarray): valeurs de la composante résiduelle
        dist (str): type de distribution utilisé
        u (float): paramètre de plage pour distribution uniforme
        sigma (float): écart-type pour distribution normale
    """
    
    def __init__(
        self,
        length: int,
        dist: Literal["normal", "uniform"] = "normal",
        u: float = 0,
        sigma: float = 0
    ):
        """
        Initialise une composante résiduelle.
        
        Args:
            length: longueur de la série
            dist: distribution ("normal" ou "uniform")
            u: demi-plage pour distribution uniforme [-u, u]
            sigma: écart-type pour distribution normale
            
        Raises:
            ValueError: si les paramètres sont invalides
        """
        # validation des paramètres
        self._validate_inputs(length, dist, u, sigma)
        
        # génération des résidus selon la distribution
        if dist == "uniform":
            self.y = np.random.uniform(low=-u, high=u, size=length)
            self.u = u
        elif dist == "normal":
            self.y = np.random.normal(loc=0, scale=sigma, size=length)
            self.sigma = sigma
        
        self.dist = dist
    
    def _validate_inputs(
        self,
        length: int,
        dist: str,
        u: float,
        sigma: float
    ) -> None:
        """valide les paramètres d'entrée"""
        if not isinstance(length, (int, np.integer)) or length <= 0:
            raise ValueError("length doit être un entier positif")
        
        if dist not in ["uniform", "normal"]:
            raise ValueError("dist doit être 'uniform' ou 'normal'")
        
        if not isinstance(u, (int, float)) or np.isnan(u):
            raise ValueError("u doit être un nombre valide")
        
        if not isinstance(sigma, (int, float)) or np.isnan(sigma) or sigma < 0:
            raise ValueError("sigma doit être un nombre positif ou nul")
```

## Démo

```python
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# définition des paramètres pour la démo
np.random.seed(42)  # pour la reproductibilité

# exemple 1: série simple avec tendance et saisonnalité
sstr_simple = SSTR(
    length_years=10,
    resolution="1 months",
    start_date=datetime(2020, 1, 1),
    idx_as_date=True,
    # tendance croissante simple
    trend_initial_y=100,
    trend_slp=[0.5],
    # saisonnalité annuelle
    season_period=12,
    season_harm_ord=[2],
    season_amp_sin=np.array([[3, 1]]),  # harmonique 1 et 2
    season_amp_cos=np.array([[1, 0.5]]),
    # bruit blanc
    res_dist="normal",
    res_sigma=2
)

print(f"Série générée: {len(sstr_simple.t)} points")
print(f"Plage de valeurs: [{sstr_simple.t['y'].min():.2f}, {sstr_simple.t['y'].max():.2f}]")
print(f"Première date: {sstr_simple.t.index[0]}")
print(f"Dernière date: {sstr_simple.t.index[-1]}")

# exemple 2: série complexe avec ruptures multiples
sstr_complex = SSTR(
    length_years=15,
    resolution="1 months",
    start_date=datetime(2015, 1, 1),
    idx_as_date=True,
    # tendance avec ruptures de pente et niveau
    trend_initial_y=50,
    trend_slp=[0.2, 0.8, -0.1],  # 3 segments
    trend_breaks_idx=[60, 120],   # ruptures à 5 et 10 ans
    trend_breaks_mag=[10, -5],    # sauts de niveau
    # saisonnalité avec changement d'amplitude
    season_period=12,
    season_harm_ord=[1, 2, 1],  # ordre harmonique par segment
    season_amp_sin=np.array([
        [4, 0],    # segment 1: forte saisonnalité
        [2, 1],    # segment 2: saisonnalité complexe
        [6, 0]     # segment 3: saisonnalité très forte
    ]),
    season_amp_cos=np.array([
        [1, 0],
        [0.5, 0.5],
        [2, 0]
    ]),
    season_breaks_idx=[60, 120],
    season_breaks_mag=[5, -10],
    # résidus avec plus de variabilité
    res_dist="normal",
    res_sigma=3,
    # quelques données manquantes
    missing_data_proportion=0.05
)

print(f"Série complexe générée: {len(sstr_complex.t)} points")
print(f"Données manquantes: {sstr_complex.t['y'].isna().sum()}")
print(f"Ruptures de tendance aux indices: {sstr_complex.trend.breaks['idx']}")
print(f"Ruptures saisonnières aux indices: {sstr_complex.season.breaks['idx']}")

# exemple 3: analyse des composantes
sstr_analysis = SSTR(
    length_years=5,
    resolution="1 weeks",
    # tendance quadratique simulée avec segments linéaires
    trend_initial_y=0,
    trend_slp=[0, 0.1, 0.2, 0.05],
    trend_breaks_idx=[65, 130, 195],
    trend_breaks_mag=[0, 2, -1],
    # saisonnalité forte
    season_period=52,  # saisonnalité annuelle hebdomadaire
    season_harm_ord=[3],
    season_amp_sin=np.array([[5, 2, 1]]),
    season_amp_cos=np.array([[0, 1, 0.5]]),
    # résidus uniformes
    res_dist="uniform",
    res_u=1.5
)

# statistiques descriptives par composante
components = ['trend', 'season', 'residual', 'y']
for comp in components:
    values = sstr_analysis.t[comp]
    print(f"{comp.capitalize()}:")
    print(f"  Moyenne: {values.mean():.3f}")
    print(f"  Écart-type: {values.std():.3f}")
    print(f"  Min/Max: {values.min():.3f} / {values.max():.3f}")

# extra : visualisation
import matplotlib.pyplot as plt

# graphique des composantes
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
components = ['y', 'trend', 'season', 'residual']
titles = ['Série complète', 'Tendance', 'Saisonnalité', 'Résidus']

for i, (comp, title) in enumerate(zip(components, titles)):
    sstr_simple.t[comp].plot(ax=axes[i], title=title)
    if sstr_simple.trend.breaks['idx']:
        for break_idx in sstr_simple.trend.breaks['idx']:
            axes[i].axvline(x=sstr_simple.t.index[break_idx-1], 
                          color='red', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# comparaison des séries
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sstr_simple.t['y'].plot(title='Série simple')
plt.subplot(1, 2, 2)
sstr_complex.t['y'].plot(title='Série complexe avec ruptures')
for break_idx in sstr_complex.trend.breaks['idx']:
    plt.axvline(x=sstr_complex.t.index[break_idx-1], 
               color='red', linestyle='--', alpha=0.7, label='Ruptures')
plt.legend()
plt.tight_layout()
plt.show()
```

## Documentation technique

### Architecture du module

Le module SSTR suit une architecture modulaire avec séparation claire des responsabilités:

- **SSTR**: classe principale orchestrant la génération
- **Trend**: composante de tendance linéaire par morceaux  
- **Season**: composante saisonnière harmonique
- **Residual**: composante de bruit blanc

### Validation des paramètres

Chaque classe implémente une validation rigoureuse:
- Vérification des types de données
- Validation des plages de valeurs
- Contrôle de cohérence entre paramètres
- Messages d'erreur explicites en français

### Gestion des ruptures

Les ruptures sont définies par:
- **breaks_idx**: positions des ruptures (indices > 1)
- **breaks_mag**: magnitudes des sauts de niveau
- Le nombre de segments = nombre de ruptures + 1

### Extensions possibles

- Tendances non-linéaires (polynomial, exponentiel)
- Résidus autocorrélés (AR, MA, ARMA)
- Saisonnalités multiples
- Ruptures graduelles vs abruptes
- Export vers formats standards (CSV, JSON, HDF5) 