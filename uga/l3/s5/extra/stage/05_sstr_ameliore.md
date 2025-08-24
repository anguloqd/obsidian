## 04 // sstr amelioré

## Proposition d'amélioration de SSTR

Ceci est une proposition pour une API plus propre et professionnelle.

### API

#### Classes de Configuration

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Literal, Union
import numpy as np

@dataclass
class TimeConfig:
    """Configuration temporelle de la série."""
    length_years: float = 50
    resolution: str = "1 months"
    start_date: Optional[datetime] = None
    use_dates_as_index: bool = False
    missing_data_proportion: float = 0
    
    def __post_init__(self):
        if self.start_date is None:
            self.start_date = datetime.today()
        self._validate()
    
    def _validate(self):
        """valide les paramètres temporels"""
        if self.length_years <= 0:
            raise ValueError("length_years doit être positif")
        
        if not (0 <= self.missing_data_proportion <= 1):
            raise ValueError("missing_data_proportion doit être entre 0 et 1")
        
        # validation du format de résolution
        parts = self.resolution.split()
        if len(parts) != 2 or parts[1] not in ["days", "weeks", "months", "years"]:
            raise ValueError("resolution doit être au format '1 months', '2 weeks', etc.")

@dataclass  
class TrendConfig:
    """Configuration de la composante de tendance."""
    initial_value: float = 0
    slopes: List[float] = field(default_factory=lambda: [0])
    break_positions: Optional[List[int]] = None
    break_magnitudes: Optional[List[float]] = None
    
    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        """valide les paramètres de tendance"""
        if self.break_positions and self.break_magnitudes:
            if len(self.break_positions) != len(self.break_magnitudes):
                raise ValueError("break_positions et break_magnitudes doivent avoir la même longueur")
            
            if len(self.slopes) != len(self.break_positions) + 1:
                raise ValueError("slopes doit avoir un élément de plus que break_positions")

@dataclass
class SeasonConfig:
    """Configuration de la composante saisonnière."""
    period: float = 12
    phase: float = 0
    harmonic_orders: List[int] = field(default_factory=lambda: [1])
    sin_amplitudes: Optional[np.ndarray] = None
    cos_amplitudes: Optional[np.ndarray] = None
    break_positions: Optional[List[int]] = None
    break_magnitudes: Optional[List[float]] = None
    
    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        """valide les paramètres saisonniers"""
        if self.period <= 0:
            raise ValueError("period doit être positif")
        
        if any(h <= 0 for h in self.harmonic_orders):
            raise ValueError("tous les ordres harmoniques doivent être positifs")
        
        if self.break_positions and self.break_magnitudes:
            if len(self.break_positions) != len(self.break_magnitudes):
                raise ValueError("break_positions et break_magnitudes doivent avoir la même longueur")

@dataclass
class NoiseConfig:
    """Configuration de la composante de bruit."""
    distribution: Literal["normal", "uniform"] = "normal"
    scale: float = 1.0  # sigma pour normal, half-range pour uniform
    
    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        """valide les paramètres de bruit"""
        if self.scale < 0:
            raise ValueError("scale doit être positif ou nul")
        
        if self.distribution not in ["normal", "uniform"]:
            raise ValueError("distribution doit être 'normal' ou 'uniform'")
```

#### Interface Principale Refactorisée

```python
import numpy as np
import pandas as pd
import warnings
from typing import Dict, Any, Tuple

class SyntheticTimeSeries:
    """
    Générateur de séries temporelles synthétiques.
    
    Interface simplifiée utilisant des objets de configuration pour une meilleure
    lisibilité et maintenabilité du code.
    
    Attributes:
        data (pd.DataFrame): série temporelle et ses composantes
        config (dict): configuration utilisée pour la génération
        components (dict): composantes individuelles (trend, season, noise)
    """
    
    def __init__(
        self,
        time_config: Optional[TimeConfig] = None,
        trend_config: Optional[TrendConfig] = None, 
        season_config: Optional[SeasonConfig] = None,
        noise_config: Optional[NoiseConfig] = None,
        random_seed: Optional[int] = None
    ):
        """
        Initialise une série temporelle synthétique.
        
        Args:
            time_config: configuration temporelle
            trend_config: configuration de tendance
            season_config: configuration saisonnière
            noise_config: configuration du bruit
            random_seed: graine pour la reproductibilité
        """
        # initialisation des configurations par défaut
        self.time_config = time_config or TimeConfig()
        self.trend_config = trend_config or TrendConfig()
        self.season_config = season_config or SeasonConfig()
        self.noise_config = noise_config or NoiseConfig()
        
        # définition de la graine aléatoire si fournie
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # génération de la série
        self._generate_series()
    
    def _generate_series(self) -> None:
        """génère la série temporelle complète"""
        # calcul de la longueur en points de données
        length = self._calculate_length()
        
        # génération des composantes
        trend_component = self._generate_trend(length)
        season_component = self._generate_season(length)
        noise_component = self._generate_noise(length)
        
        # combinaison des composantes
        total_series = trend_component + season_component + noise_component
        
        # introduction de données manquantes
        if self.time_config.missing_data_proportion > 0:
            total_series = self._add_missing_data(total_series)
        
        # création du dataframe
        self.data = pd.DataFrame({
            'value': total_series,
            'trend': trend_component,
            'seasonal': season_component,
            'noise': noise_component
        })
        
        # ajout d'index de dates si demandé
        if self.time_config.use_dates_as_index:
            self.data.index = self._create_date_index(length)
        
        # stockage des composantes pour accès externe
        self.components = {
            'trend': TrendComponent(trend_component, self.trend_config),
            'seasonal': SeasonalComponent(season_component, self.season_config),
            'noise': NoiseComponent(noise_component, self.noise_config)
        }
    
    def _calculate_length(self) -> int:
        """calcule la longueur en points de données"""
        parts = self.time_config.resolution.split()
        resolution_value = float(parts[0])
        resolution_unit = parts[1]
        
        multipliers = {"days": 365, "weeks": 52, "months": 12, "years": 1}
        return int(self.time_config.length_years * multipliers[resolution_unit] / resolution_value)
    
    def _generate_trend(self, length: int) -> np.ndarray:
        """génère la composante de tendance"""
        generator = TrendGenerator(self.trend_config)
        return generator.generate(length)
    
    def _generate_season(self, length: int) -> np.ndarray:
        """génère la composante saisonnière"""
        generator = SeasonalGenerator(self.season_config)
        return generator.generate(length)
    
    def _generate_noise(self, length: int) -> np.ndarray:
        """génère la composante de bruit"""
        generator = NoiseGenerator(self.noise_config)
        return generator.generate(length)
    
    def _add_missing_data(self, series: np.ndarray) -> np.ndarray:
        """ajoute des données manquantes de façon aléatoire"""
        n_missing = int(len(series) * self.time_config.missing_data_proportion)
        missing_indices = np.random.choice(len(series), n_missing, replace=False)
        series = series.copy()
        series[missing_indices] = np.nan
        return series
    
    def _create_date_index(self, length: int) -> pd.DatetimeIndex:
        """crée un index de dates"""
        parts = self.time_config.resolution.split()
        resolution_value = float(parts[0])
        resolution_unit = parts[1]
        
        freq_map = {
            "days": f"{resolution_value}D",
            "weeks": f"{int(resolution_value * 7)}D", 
            "months": f"{int(resolution_value)}MS",
            "years": f"{int(resolution_value)}YS"
        }
        
        return pd.date_range(
            start=self.time_config.start_date,
            periods=length,
            freq=freq_map[resolution_unit]
        )
    
    def plot(self, components: List[str] = None, figsize: Tuple[int, int] = (12, 8)) -> None:
        """
        Visualise la série et ses composantes.
        
        Args:
            components: liste des composantes à afficher ['value', 'trend', 'seasonal', 'noise']
            figsize: taille de la figure
        """
        import matplotlib.pyplot as plt
        
        if components is None:
            components = ['value', 'trend', 'seasonal', 'noise']
        
        n_plots = len(components)
        fig, axes = plt.subplots(n_plots, 1, figsize=figsize, sharex=True)
        
        if n_plots == 1:
            axes = [axes]
        
        titles = {
            'value': 'Série Complète',
            'trend': 'Tendance', 
            'seasonal': 'Saisonnalité',
            'noise': 'Bruit'
        }
        
        for i, component in enumerate(components):
            self.data[component].plot(ax=axes[i], title=titles.get(component, component))
            
            # ajout des lignes de ruptures si disponibles
            if hasattr(self.trend_config, 'break_positions') and self.trend_config.break_positions:
                for break_pos in self.trend_config.break_positions:
                    axes[i].axvline(x=break_pos-1, color='red', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()
    
    def summary(self) -> Dict[str, Any]:
        """retourne un résumé statistique de la série"""
        stats = {}
        for col in self.data.columns:
            stats[col] = {
                'mean': float(self.data[col].mean()),
                'std': float(self.data[col].std()),
                'min': float(self.data[col].min()),
                'max': float(self.data[col].max()),
                'missing_count': int(self.data[col].isna().sum())
            }
        return stats
    
    @classmethod
    def create_simple_series(
        cls,
        length_years: float = 10,
        trend_slope: float = 0.1,
        seasonal_amplitude: float = 5.0,
        noise_level: float = 1.0,
        **kwargs
    ) -> 'SyntheticTimeSeries':
        """
        Créateur de série simple avec paramètres intuitifs.
        
        Args:
            length_years: durée en années
            trend_slope: pente de tendance
            seasonal_amplitude: amplitude saisonnière
            noise_level: niveau de bruit
            **kwargs: autres paramètres pour les configs
            
        Returns:
            instance de SyntheticTimeSeries
        """
        time_config = TimeConfig(length_years=length_years, **kwargs)
        trend_config = TrendConfig(slopes=[trend_slope])
        season_config = SeasonConfig(
            sin_amplitudes=np.array([[seasonal_amplitude]]),
            cos_amplitudes=np.array([[0]])
        )
        noise_config = NoiseConfig(scale=noise_level)
        
        return cls(time_config, trend_config, season_config, noise_config)
    
    @classmethod
    def create_with_breaks(
        cls,
        length_years: float,
        break_positions: List[int],
        trend_slopes: List[float],
        trend_magnitudes: List[float] = None,
        seasonal_changes: List[float] = None,
        **kwargs
    ) -> 'SyntheticTimeSeries':
        """
        Créateur de série avec ruptures structurelles.
        
        Args:
            length_years: durée en années
            break_positions: positions des ruptures
            trend_slopes: pentes par segment
            trend_magnitudes: sauts de niveau
            seasonal_changes: changements saisonniers
            **kwargs: autres paramètres
            
        Returns:
            instance de SyntheticTimeSeries
        """
        time_config = TimeConfig(length_years=length_years, **kwargs)
        trend_config = TrendConfig(
            slopes=trend_slopes,
            break_positions=break_positions,
            break_magnitudes=trend_magnitudes
        )
        season_config = SeasonConfig(
            break_positions=break_positions if seasonal_changes else None,
            break_magnitudes=seasonal_changes
        )
        noise_config = NoiseConfig()
        
        return cls(time_config, trend_config, season_config, noise_config)
```

#### Générateurs de Composantes Refactorisés

```python
class ComponentGenerator:
    """classe de base pour les générateurs de composantes"""
    
    def __init__(self, config):
        self.config = config
    
    def generate(self, length: int) -> np.ndarray:
        """génère une composante de longueur donnée"""
        raise NotImplementedError

class TrendGenerator(ComponentGenerator):
    """générateur de tendance optimisé"""
    
    def generate(self, length: int) -> np.ndarray:
        """génère une tendance linéaire par morceaux"""
        t = np.arange(1, length + 1)
        y = np.full(length, self.config.initial_value, dtype=float)
        
        # définition des segments
        break_points = (self.config.break_positions or []) + [length]
        
        start_idx = 0
        for i, end_idx in enumerate(break_points):
            if i < len(self.config.slopes):
                segment = slice(start_idx, end_idx)
                y[segment] = y[start_idx] + self.config.slopes[i] * (t[segment] - t[start_idx])
            
            # application des sauts de niveau
            if (i > 0 and self.config.break_magnitudes 
                and i-1 < len(self.config.break_magnitudes)):
                y[start_idx:end_idx] += self.config.break_magnitudes[i-1]
            
            # préparation du segment suivant
            if i < len(break_points) - 1:
                if i < len(self.config.slopes):
                    y[end_idx] = y[end_idx-1] + self.config.slopes[i]
                if (self.config.break_magnitudes and i < len(self.config.break_magnitudes)):
                    y[end_idx] += self.config.break_magnitudes[i]
            
            start_idx = end_idx
        
        return y

class SeasonalGenerator(ComponentGenerator):
    """générateur de saisonnalité harmonique"""
    
    def generate(self, length: int) -> np.ndarray:
        """génère une saisonnalité harmonique"""
        t = np.arange(1, length + 1)
        y = np.zeros(length)
        
        # préparation des amplitudes par défaut
        n_segments = len(self.config.break_positions) + 1 if self.config.break_positions else 1
        max_harmonic = max(self.config.harmonic_orders)
        
        sin_amps = self.config.sin_amplitudes
        if sin_amps is None:
            sin_amps = np.ones((n_segments, max_harmonic))
        
        cos_amps = self.config.cos_amplitudes  
        if cos_amps is None:
            cos_amps = np.zeros((n_segments, max_harmonic))
        
        # génération par segments
        break_points = (self.config.break_positions or []) + [length]
        break_mags = [0] + (self.config.break_magnitudes or [])
        
        start_idx = 0
        for i, end_idx in enumerate(break_points):
            segment = slice(start_idx, end_idx)
            
            # application des harmoniques
            if i < len(self.config.harmonic_orders):
                for h in range(1, self.config.harmonic_orders[i] + 1):
                    sin_component = (sin_amps[i, h-1] * 
                                   np.sin(2 * np.pi * h * t[segment] / self.config.period - self.config.phase))
                    cos_component = (cos_amps[i, h-1] * 
                                   np.cos(2 * np.pi * h * t[segment] / self.config.period - self.config.phase))
                    y[segment] += sin_component + cos_component
            
            # ajout des sauts de niveau saisonniers
            if i < len(break_mags):
                y[segment] += break_mags[i]
            
            start_idx = end_idx
        
        return y

class NoiseGenerator(ComponentGenerator):
    """générateur de bruit blanc"""
    
    def generate(self, length: int) -> np.ndarray:
        """génère du bruit selon la distribution configurée"""
        if self.config.distribution == "normal":
            return np.random.normal(0, self.config.scale, length)
        elif self.config.distribution == "uniform":
            return np.random.uniform(-self.config.scale, self.config.scale, length)
        else:
            raise ValueError(f"Distribution non supportée: {self.config.distribution}")

class TrendComponent:
    """conteneur pour composante de tendance avec métadonnées"""
    def __init__(self, values: np.ndarray, config: TrendConfig):
        self.values = values
        self.config = config
        self.break_positions = config.break_positions or []
        self.break_magnitudes = config.break_magnitudes or []

class SeasonalComponent:
    """conteneur pour composante saisonnière avec métadonnées"""  
    def __init__(self, values: np.ndarray, config: SeasonConfig):
        self.values = values
        self.config = config
        self.break_positions = config.break_positions or []
        self.break_magnitudes = config.break_magnitudes or []

class NoiseComponent:
    """conteneur pour composante de bruit avec métadonnées"""
    def __init__(self, values: np.ndarray, config: NoiseConfig):
        self.values = values  
        self.config = config
```

### Démo avec la Nouvelle Interface

```python
import numpy as np
from datetime import datetime

# définition de la graine pour reproductibilité
np.random.seed(42)

# exemple 1: interface simplifiée

# création d'une série simple avec l'interface intuitive
simple_series = SyntheticTimeSeries.create_simple_series(
    length_years=5,
    trend_slope=0.2,
    seasonal_amplitude=8.0,
    noise_level=2.0
)

print(f"Série simple générée: {len(simple_series.data)} points")
print("Statistiques:", simple_series.summary()['value'])

# exemple 2: configuration avancée

# configuration détaillée avec objets de configuration
time_config = TimeConfig(
    length_years=10,
    resolution="1 months",
    start_date=datetime(2020, 1, 1),
    use_dates_as_index=True,
    missing_data_proportion=0.02
)

trend_config = TrendConfig(
    initial_value=100,
    slopes=[0.1, 0.5, -0.2],
    break_positions=[40, 80],
    break_magnitudes=[10, -15]
)

season_config = SeasonConfig(
    period=12,
    harmonic_orders=[2, 3, 1],
    sin_amplitudes=np.array([
        [5, 2],
        [8, 3, 1], 
        [12, 0]
    ]),
    cos_amplitudes=np.array([
        [2, 1],
        [1, 2, 0.5],
        [3, 0]
    ]),
    break_positions=[40, 80],
    break_magnitudes=[5, -8]
)

noise_config = NoiseConfig(
    distribution="normal",
    scale=3.0
)

advanced_series = SyntheticTimeSeries(
    time_config=time_config,
    trend_config=trend_config,
    season_config=season_config,
    noise_config=noise_config,
    random_seed=123
)

print(f"Série avancée générée: {len(advanced_series.data)} points")
print(f"Ruptures aux positions: {trend_config.break_positions}")
print(f"Données manquantes: {advanced_series.data['value'].isna().sum()}")

# exemple 3: série avec ruptures

# création rapide de série avec ruptures
break_series = SyntheticTimeSeries.create_with_breaks(
    length_years=8,
    break_positions=[30, 60, 90],
    trend_slopes=[0.0, 0.3, 0.1, -0.1],
    trend_magnitudes=[0, 5, -3],
    seasonal_changes=[2, -4, 1],
    resolution="1 months",
    use_dates_as_index=True
)

print(f"Série avec ruptures: {len(break_series.data)} points")
print("Résumé des composantes:")
for comp, stats in break_series.summary().items():
    print(f"  {comp}: moyenne={stats['mean']:.2f}, std={stats['std']:.2f}")
