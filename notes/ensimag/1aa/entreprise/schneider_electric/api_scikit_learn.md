# Guide API de Scikit-Learn
## Prétraitement des données

### Mise à l'échelle des caractéristiques

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer

# StandardScaler (moyenne=0, écart-type=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)

# MinMaxScaler (0 à 1)
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# RobustScaler (médiane et IQR)
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

# Normalizer (norme unitaire)
normalizer = Normalizer(norm='l2')
X_normalized = normalizer.fit_transform(X)
```

### Encodage des variables catégorielles

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# Label Encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_decoded = le.inverse_transform(y_encoded)

# One-Hot Encoding
ohe = OneHotEncoder(sparse=False, drop='first')
X_encoded = ohe.fit_transform(X_categorical)
feature_names = ohe.get_feature_names_out()

# Ordinal Encoding
oe = OrdinalEncoder()
X_ordinal = oe.fit_transform(X_categorical)
```

### Sélection de caractéristiques

```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif, RFE, SelectFromModel

# Sélection univariée de caractéristiques
selector = SelectKBest(score_func=chi2, k=10)
X_selected = selector.fit_transform(X, y)
selected_features = selector.get_support()

# Élimination récursive de caractéristiques
from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression()
rfe = RFE(estimator, n_features_to_select=10)
X_rfe = rfe.fit_transform(X, y)

# Sélection basée sur modèle
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
selector = SelectFromModel(rf, threshold='median')
X_selected = selector.fit_transform(X, y)
```

### Division des données

```python
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

# Division train-test simple
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Division stratifiée
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_idx, test_idx in sss.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
```

## Apprentissage supervisé

### Modèles linéaires

```python
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet,
    LogisticRegression, SGDClassifier, SGDRegressor
)

# Régression Linéaire
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print(f"Coefficients: {lr.coef_}")
print(f"Intercept: {lr.intercept_}")

# Régression Ridge (régularisation L2)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Régression Lasso (régularisation L1)
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

# Elastic Net (régularisation L1 + L2)
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic.fit(X_train, y_train)

# Régression Logistique
log_reg = LogisticRegression(C=1.0, penalty='l2', max_iter=1000)
log_reg.fit(X_train, y_train)
y_proba = log_reg.predict_proba(X_test)
```

### Modèles basés sur les arbres

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor

# Arbre de Décision
dt = DecisionTreeClassifier(max_depth=5, min_samples_split=20, random_state=42)
dt.fit(X_train, y_train)

# Forêt Aléatoire
rf = RandomForestClassifier(
    n_estimators=100, max_depth=10, min_samples_split=5, random_state=42
)
rf.fit(X_train, y_train)
feature_importance = rf.feature_importances_

# Gradient Boosting
gb = GradientBoostingClassifier(
    n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42
)
gb.fit(X_train, y_train)
```

### Machines à vecteurs de support (SVM)

```python
from sklearn.svm import SVC, SVR

# Classification
svc = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True)
svc.fit(X_train, y_train)

# Régression
svr = SVR(kernel='rbf', C=1.0, gamma='scale')
svr.fit(X_train, y_train)
```

### Bayes naïf

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

# Naive Bayes Gaussien
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Naive Bayes Multinomial (pour données texte/comptage)
mnb = MultinomialNB(alpha=1.0)
mnb.fit(X_train, y_train)
```

### K plus proches voisins

```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# Classification
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform', metric='minkowski')
knn.fit(X_train, y_train)

# Régression
knn_reg = KNeighborsRegressor(n_neighbors=5, weights='distance')
knn_reg.fit(X_train, y_train)
```

## Apprentissage non supervisé

### Clustering

```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X)
cluster_centers = kmeans.cluster_centers_

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
cluster_labels = dbscan.fit_predict(X)

# Clustering Hiérarchique
agg_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
cluster_labels = agg_clustering.fit_predict(X)

# Modèle de Mélange Gaussien
gmm = GaussianMixture(n_components=3, random_state=42)
cluster_labels = gmm.fit_predict(X)
log_likelihood = gmm.score(X)
```

### Réduction de dimensionnalité

```python
from sklearn.decomposition import PCA, TruncatedSVD, NMF
from sklearn.manifold import TSNE

# Analyse en Composantes Principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_

# t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X)

# SVD Tronquée (pour matrices éparses)
svd = TruncatedSVD(n_components=50, random_state=42)
X_svd = svd.fit_transform(X_sparse)

# Factorisation de Matrices Non-négatives
nmf = NMF(n_components=10, random_state=42)
X_nmf = nmf.fit_transform(X)
```

## Sélection et validation de modèles

### Validation croisée

```python
from sklearn.model_selection import (
    cross_val_score, cross_validate, StratifiedKFold, 
    KFold, LeaveOneOut, TimeSeriesSplit
)

# Validation croisée simple
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# K-Fold Stratifié
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in skf.split(X, y):
    X_train_fold, X_val_fold = X[train_idx], X[val_idx]
    y_train_fold, y_val_fold = y[train_idx], y[val_idx]

# Validation Croisée Séries Temporelles
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, val_idx in tscv.split(X):
    # Division respectant l'ordre temporel
    pass

# Validation croisée avec métriques multiples
scoring = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(model, X, y, cv=5, scoring=scoring)
```

### Réglage des hyperparamètres

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Recherche en Grille
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(
    RandomForestClassifier(), param_grid, cv=5, scoring='accuracy', n_jobs=-1
)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_score = grid_search.best_score_

# Recherche Aléatoire
from scipy.stats import randint, uniform
param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20)
}
random_search = RandomizedSearchCV(
    RandomForestClassifier(), param_dist, n_iter=100, cv=5, random_state=42
)
random_search.fit(X_train, y_train)
```

## Évaluation de modèles

### Métriques de classification

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score,
    precision_recall_curve, roc_curve
)

# Métriques de base
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

# Rapport complet
report = classification_report(y_true, y_pred, target_names=class_names)

# Matrice de Confusion
cm = confusion_matrix(y_true, y_pred)

# ROC AUC
auc = roc_auc_score(y_true, y_proba[:, 1])  # pour classification binaire
auc_multiclass = roc_auc_score(y_true, y_proba, multi_class='ovr')

# Courbe Précision-Rappel
precision, recall, _ = precision_recall_curve(y_true, y_proba[:, 1])

# Courbe ROC
fpr, tpr, _ = roc_curve(y_true, y_proba[:, 1])
```

### Métriques de régression

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    mean_squared_log_error, mean_absolute_percentage_error
)

# Métriques de régression de base
mse = mean_squared_error(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
mape = mean_absolute_percentage_error(y_true, y_pred)
```

## Pipelines

```python
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

# Pipeline Simple
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Transformateur de Colonnes (prétraitement différent pour différentes colonnes)
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])
```

## Techniques avancées

### Méthodes d'ensemble

```python
from sklearn.ensemble import VotingClassifier, BaggingClassifier, AdaBoostClassifier

# Classificateur de Vote
voting_clf = VotingClassifier([
    ('rf', RandomForestClassifier()),
    ('svc', SVC(probability=True)),
    ('lr', LogisticRegression())
], voting='soft')

# Bagging
bagging = BaggingClassifier(
    DecisionTreeClassifier(), n_estimators=100, random_state=42
)

# AdaBoost
ada_boost = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), n_estimators=100
)
```

### Données déséquilibrées

```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.utils.class_weight import compute_class_weight

# Sur-échantillonnage SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Poids de classes
class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
model = RandomForestClassifier(class_weight='balanced')
```

### Transformateurs personnalisés

```python
from sklearn.base import BaseEstimator, TransformerMixin

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, feature_names):
        self.feature_names = feature_names
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Logique de transformation personnalisée
        return X_transformed
```

## Modèles courants de LeetCode

```python
# Framework de comparaison de modèles
def compare_models(models_dict, X_train, X_test, y_train, y_test):
    results = {}
    for name, model in models_dict.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results[name] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
    return results

# Analyse d'importance des caractéristiques
def get_feature_importance(model, feature_names):
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
    elif hasattr(model, 'coef_'):
        importance = abs(model.coef_[0])
    else:
        return None
    
    return pd.DataFrame({
        'feature': feature_names,
        'importance': importance
    }).sort_values('importance', ascending=False)

# Analyse de courbe d'apprentissage
from sklearn.model_selection import learning_curve

def plot_learning_curve(model, X, y):
    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
    )
    return train_sizes, train_scores, val_scores

# Courbe de validation pour réglage hyperparamètres
from sklearn.model_selection import validation_curve

def plot_validation_curve(model, X, y, param_name, param_range):
    train_scores, val_scores = validation_curve(
        model, X, y, param_name=param_name, param_range=param_range, cv=5
    )
    return train_scores, val_scores
```

## Optimisation des performances

```python
# Traitement parallèle
model = RandomForestClassifier(n_jobs=-1)  # Utiliser tous les cœurs

# Optimisation mémoire
from sklearn.externals import joblib
joblib.dump(model, 'model.pkl')  # Sauvegarder modèle
model = joblib.load('model.pkl')  # Charger modèle

# Apprentissage incrémental pour gros jeux de données
from sklearn.linear_model import SGDClassifier
sgd = SGDClassifier()
for chunk in data_chunks:
    sgd.partial_fit(chunk_X, chunk_y)
```
