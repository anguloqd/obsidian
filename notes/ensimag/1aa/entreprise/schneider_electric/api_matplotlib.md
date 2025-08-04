# Guide API de Matplotlib

## Configuration de base

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Configuration globale
plt.style.use('seaborn-v0_8')  # style par défaut
mpl.rcParams['figure.figsize'] = (10, 6)
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.grid'] = True
```

## Création de figures et axes

### Interface pyplot (procédurale)

```python
# Figure simple
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

# Sous-graphiques
plt.subplot(2, 2, 1)  # 2x2 grid, position 1
plt.plot(x, y1)

plt.subplot(2, 2, 2)
plt.plot(x, y2)

# Avec subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(x, y3)
axes[1, 1].hist(data)
```

### Interface orientée objet (recommandée)

```python
# Figure et axes
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='données')
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_title('Mon Graphique')
ax.legend()

# Multiples axes
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Axes avec ratios personnalisés
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), 
                               gridspec_kw={'width_ratios': [2, 1]})
```

## Types de graphiques essentiels

### Graphiques en ligne

```python
# Graphique simple
ax.plot(x, y, color='blue', linewidth=2, linestyle='-', marker='o')

# Styles de ligne
ax.plot(x, y1, '-', label='solide')      # ligne solide
ax.plot(x, y2, '--', label='tirets')     # tirets
ax.plot(x, y3, '-.', label='tiret-point') # tiret-point
ax.plot(x, y4, ':', label='pointillés')  # pointillés

# Marqueurs
ax.plot(x, y, marker='o', markersize=8, markerfacecolor='red', markeredgecolor='black')

# Multiples séries
for i, data in enumerate(datasets):
    ax.plot(x, data, label=f'Série {i+1}')
ax.legend()
```

### Nuages de points

```python
# Scatter plot basique
ax.scatter(x, y, c='blue', s=50, alpha=0.7)

# Avec couleurs variables
ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(label='Valeur')

# Avec annotations
for i, txt in enumerate(labels):
    ax.annotate(txt, (x[i], y[i]), xytext=(5, 5), textcoords='offset points')
```

### Graphiques en barres

```python
# Barres verticales
ax.bar(categories, values, color='skyblue', alpha=0.8)

# Barres horizontales
ax.barh(categories, values, color='lightgreen')

# Barres groupées
width = 0.35
x_pos = np.arange(len(categories))
ax.bar(x_pos - width/2, values1, width, label='Groupe 1')
ax.bar(x_pos + width/2, values2, width, label='Groupe 2')
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)

# Barres empilées
ax.bar(categories, values1, label='Partie 1')
ax.bar(categories, values2, bottom=values1, label='Partie 2')
```

### Histogrammes

```python
# Histogramme simple
ax.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')

# Histogrammes multiples
ax.hist([data1, data2], bins=20, alpha=0.7, label=['Groupe 1', 'Groupe 2'])

# Histogramme 2D
ax.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar()

# Avec statistiques
n, bins, patches = ax.hist(data, bins=30)
```

### Boîtes à moustaches

```python
# Boxplot simple
ax.boxplot(data)

# Multiples groupes
ax.boxplot([data1, data2, data3], labels=['Groupe 1', 'Groupe 2', 'Groupe 3'])

# Personnalisation
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True)
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')
```

## Personnalisation avancée

### Axes et échelles

```python
# Limites des axes
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

# Échelles logarithmiques
ax.set_xscale('log')
ax.set_yscale('log')

# Ticks personnalisés
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['Zéro', 'Deux', 'Quatre', 'Six', 'Huit', 'Dix'])

# Rotation des labels
ax.tick_params(axis='x', rotation=45)

# Axe secondaire
ax2 = ax.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Axe Y secondaire', color='r')
```

### Couleurs et styles

```python
# Palettes de couleurs
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
colors = ['#FF5733', '#33FF57', '#3357FF']  # couleurs hexadécimales

# Cartes de couleurs (colormaps)
im = ax.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(im, ax=ax)

# Styles de graphiques prédéfinis
plt.style.use('ggplot')
plt.style.use('seaborn-v0_8')
plt.style.use('dark_background')
```

### Annotations et texte

```python
# Texte simple
ax.text(x, y, 'Mon texte', fontsize=12, ha='center', va='center')

# Annotations avec flèches
ax.annotate('Point important', xy=(x_point, y_point), xytext=(x_text, y_text),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Équations LaTeX
ax.text(0.5, 0.5, r'$\alpha = \beta^2 + \gamma$', transform=ax.transAxes,
        fontsize=16, ha='center')

# Légendes personnalisées
ax.legend(loc='upper right', frameon=True, shadow=True, ncol=2)
```

## Graphiques spécialisés

### Cartes de chaleur

```python
# Heatmap avec imshow
im = ax.imshow(matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(im)

# Avec annotations
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        text = ax.text(j, i, matrix[i, j], ha="center", va="center", color="w")
```

### Graphiques polaires

```python
# Configuration polaire
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))

# Graphique radar
theta = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
ax.plot(theta, values, 'o-', linewidth=2)
ax.fill(theta, values, alpha=0.25)
ax.set_xticks(theta)
ax.set_xticklabels(categories)
```

### Graphiques 3D

```python
from mpl_toolkits.mplot3d import Axes3D

# Surface 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Nuage de points 3D
ax.scatter(x, y, z, c=colors, s=50)

# Courbe 3D
ax.plot(x, y, z, label='courbe 3D')
```

## Gestion des figures

### Sauvegarde

```python
# Formats multiples
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
plt.savefig('graph.pdf', bbox_inches='tight')
plt.savefig('graph.svg', bbox_inches='tight')

# Avec transparence
plt.savefig('graph.png', transparent=True, facecolor='none')

# Qualité haute résolution
plt.savefig('graph.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
```

### Mise en page

```python
# Ajustement automatique
plt.tight_layout()

# Espacement manuel
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, 
                   wspace=0.4, hspace=0.4)

# GridSpec pour layouts complexes
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])    # première ligne complète
ax2 = plt.subplot(gs[1, :-1])  # deuxième ligne sans dernière colonne
ax3 = plt.subplot(gs[1:, -1])  # dernière colonne, deux dernières lignes
ax4 = plt.subplot(gs[-1, 0])   # coin inférieur gauche
ax5 = plt.subplot(gs[-1, -2])  # avant-dernière colonne, dernière ligne
```

## Animation

### Animation simple

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

def animate(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame/10)
    line.set_data(x, y)
    return line,

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.1, 1.1)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=200, 
                   interval=50, blit=True)

# Sauvegarde animation
ani.save('animation.gif', writer='pillow')
ani.save('animation.mp4', writer='ffmpeg')
```

## Interactivité

### Widgets

```python
from matplotlib.widgets import Slider, Button

# Slider interactif
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(ax_slider, 'Fréquence', 0.1, 10.0, valinit=1)

def update(val):
    freq = slider.val
    # Mise à jour du graphique
    ax.clear()
    ax.plot(x, np.sin(2*np.pi*freq*x))
    plt.draw()

slider.on_changed(update)
```

### Événements

```python
# Détection de clics
def onclick(event):
    if event.inaxes == ax:
        print(f'Clic en ({event.xdata:.2f}, {event.ydata:.2f})')

fig.canvas.mpl_connect('button_press_event', onclick)

# Détection de survol
def onhover(event):
    if event.inaxes == ax:
        # Logique de survol
        pass

fig.canvas.mpl_connect('motion_notify_event', onhover)
```

## Optimisation et performance

### Graphiques performants

```python
# Pour de grandes quantités de données
ax.plot(x, y, rasterized=True)  # rastérisation pour PDF/SVG

# Réduction du nombre de points
from matplotlib.path import Path
# Simplification automatique des courbes

# Collections pour multiples objets
from matplotlib.collections import LineCollection
lines = [list(zip(x, y)) for y in y_data]
lc = LineCollection(lines, colors=colors)
ax.add_collection(lc)
```

### Mémoire et ressources

```python
# Nettoyage de figures
plt.close('all')  # fermer toutes les figures
plt.close(fig)    # fermer une figure spécifique

# Gestion explicite de la mémoire
fig.clear()
ax.clear()
```

## Modèles courants de LeetCode

```python
# Visualisation de séries temporelles
def plot_time_series(dates, values, title="Série Temporelle"):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, values, linewidth=2)
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    return fig, ax

# Comparaison de distributions
def compare_distributions(data_list, labels, title="Comparaison"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data_list, bins=30, alpha=0.7, label=labels)
    ax.legend()
    ax.set_title(title)
    return fig, ax

# Matrice de corrélation
def correlation_matrix(corr_matrix, labels):
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.set_yticklabels(labels)
    
    # Annotations
    for i in range(len(labels)):
        for j in range(len(labels)):
            text = ax.text(j, i, f'{corr_matrix[i, j]:.2f}', 
                          ha="center", va="center")
    
    plt.colorbar(im)
    plt.tight_layout()
    return fig, ax

# Dashboard multi-graphiques
def create_dashboard(data_dict):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Graphique 1: Ligne
    axes[0, 0].plot(data_dict['x'], data_dict['y1'])
    axes[0, 0].set_title('Évolution temporelle')
    
    # Graphique 2: Barres
    axes[0, 1].bar(data_dict['categories'], data_dict['values'])
    axes[0, 1].set_title('Répartition par catégorie')
    
    # Graphique 3: Scatter
    axes[1, 0].scatter(data_dict['x_scatter'], data_dict['y_scatter'])
    axes[1, 0].set_title('Corrélation')
    
    # Graphique 4: Histogramme
    axes[1, 1].hist(data_dict['distribution'], bins=20)
    axes[1, 1].set_title('Distribution')
    
    plt.tight_layout()
    return fig, axes
```