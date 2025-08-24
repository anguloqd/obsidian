## Guide API de TensorFlow

### Opérations TensorFlow de base

#### Création et manipulation de tenseurs

```python
import tensorflow as tf

# Création de tenseurs
tf.constant([1, 2, 3])
tf.zeros((3, 4))
tf.ones((2, 3))
tf.fill((2, 3), 7)
tf.eye(3)
tf.random.normal((3, 4))
tf.random.uniform((3, 4))
tf.range(10)
tf.linspace(0.0, 10.0, 100)

# Depuis numpy
tf.convert_to_tensor(numpy_array)

# Propriétés des tenseurs
tensor.shape
tensor.dtype
tensor.numpy()  # convertir en numpy
tf.rank(tensor)  # nombre de dimensions
tf.size(tensor)  # éléments totaux
```

#### Opérations sur les tenseurs

```python
# Opérations arithmétiques
tf.add(a, b)  # ou a + b
tf.subtract(a, b)  # ou a - b
tf.multiply(a, b)  # ou a * b
tf.divide(a, b)  # ou a / b
tf.pow(a, 2)  # ou a ** 2

# Fonctions mathématiques
tf.abs(tensor)
tf.sqrt(tensor)
tf.exp(tensor)
tf.log(tensor)
tf.sin(tensor)
tf.cos(tensor)
tf.round(tensor)
tf.floor(tensor)
tf.ceil(tensor)

# Opérations matricielles
tf.matmul(a, b)  # ou a @ b
tf.transpose(tensor)
tf.linalg.det(matrix)
tf.linalg.inv(matrix)
tf.linalg.eig(matrix)

# Opérations de réduction
tf.reduce_sum(tensor, axis=None)
tf.reduce_mean(tensor, axis=None)
tf.reduce_max(tensor, axis=None)
tf.reduce_min(tensor, axis=None)
tf.reduce_std(tensor, axis=None)

# Redimensionnement
tf.reshape(tensor, new_shape)
tf.expand_dims(tensor, axis)
tf.squeeze(tensor)
tf.tile(tensor, multiples)
```

### API Séquentielle de Keras

#### Création de modèles

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten

# Modèle séquentiel
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Syntaxe alternative
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

#### Compilation de modèles

```python
# Compilation de base
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Compilation personnalisée
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=[tf.keras.metrics.Accuracy(), tf.keras.metrics.TopKCategoricalAccuracy(k=5)]
)
```

#### Entraînement de modèles

```python
# Entraînement de base
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    verbose=1
)

# Entraînement avancé avec callbacks
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

callbacks = [
    EarlyStopping(patience=10, restore_best_weights=True),
    ModelCheckpoint('best_model.h5', save_best_only=True),
    ReduceLROnPlateau(patience=5, factor=0.5)
]

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=callbacks,
    shuffle=True
)
```

### API Fonctionnelle de Keras

#### Création de modèles

```python
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

# Couche d'entrée
inputs = Input(shape=(784,))

# Couches cachées
x = Dense(128, activation='relu')(inputs)
x = Dropout(0.2)(x)
x = Dense(64, activation='relu')(x)
outputs = Dense(10, activation='softmax')(x)

# Créer modèle
model = Model(inputs=inputs, outputs=outputs)

# Entrées/sorties multiples
input1 = Input(shape=(100,))
input2 = Input(shape=(50,))

x1 = Dense(64, activation='relu')(input1)
x2 = Dense(32, activation='relu')(input2)

merged = tf.keras.layers.concatenate([x1, x2])
output = Dense(1, activation='sigmoid')(merged)

model = Model(inputs=[input1, input2], outputs=output)
```

### Couches de base

#### Couches Denses

```python
from tensorflow.keras.layers import Dense

# Couche dense de base
Dense(units=64, activation='relu', use_bias=True)

# Avec régularisation
Dense(64, activation='relu', 
      kernel_regularizer=tf.keras.regularizers.l2(0.01),
      bias_regularizer=tf.keras.regularizers.l1(0.01))

# Avec initialisation
Dense(64, activation='relu',
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros')
```

#### Couches Convolutionnelles

```python
from tensorflow.keras.layers import Conv2D, Conv1D, MaxPooling2D, AveragePooling2D

# Convolution 2D
Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')

# Convolution 1D
Conv1D(filters=64, kernel_size=3, activation='relu')

# Couches de pooling
MaxPooling2D(pool_size=(2, 2), strides=2)
AveragePooling2D(pool_size=(2, 2))

# Pooling global
tf.keras.layers.GlobalMaxPooling2D()
tf.keras.layers.GlobalAveragePooling2D()
```

#### Couches Récurrentes

```python
from tensorflow.keras.layers import LSTM, GRU, SimpleRNN

# LSTM
LSTM(units=128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2)

# GRU
GRU(units=64, return_sequences=False)

# RNN Bidirectionnel
tf.keras.layers.Bidirectional(LSTM(128))

# Couches LSTM multiples
model = Sequential([
    LSTM(128, return_sequences=True),  # retourner séquences pour LSTM suivant
    LSTM(64, return_sequences=False),  # LSTM final ne retourne pas séquences
    Dense(1)
])
```

#### Normalisation et Régularisation

```python
from tensorflow.keras.layers import BatchNormalization, LayerNormalization, Dropout

# Normalisation par Lot
BatchNormalization(momentum=0.99, epsilon=0.001)

# Normalisation de Couche
LayerNormalization(epsilon=1e-6)

# Dropout
Dropout(rate=0.5)

# Dropout Spatial (pour CNN)
tf.keras.layers.SpatialDropout2D(rate=0.2)
```

### Architectures avancées

#### Apprentissage par transfert

```python
# Charger modèle pré-entraîné
base_model = tf.keras.applications.VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Geler modèle de base
base_model.trainable = False

# Ajouter tête personnalisée
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(num_classes, activation='softmax')
])

# Fine-tuning : dégeler certaines couches
base_model.trainable = True
for layer in base_model.layers[:-4]:
    layer.trainable = False
```

#### Couches personnalisées

```python
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, units=32):
        super(CustomLayer, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer='random_normal',
            trainable=True
        )
        self.b = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            trainable=True
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b

# Utilisation
model = Sequential([
    CustomLayer(64),
    Dense(10, activation='softmax')
])
```

#### Mécanismes d'attention

```python
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization

class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = Sequential([
            Dense(ff_dim, activation="relu"),
            Dense(embed_dim),
        ])
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)
```

### Pipeline de Données (tf.data)

#### Création de jeux de données

```python
# Depuis tenseurs
dataset = tf.data.Dataset.from_tensor_slices((X, y))

# Depuis générateur
def data_generator():
    for i in range(1000):
        yield (np.random.random((28, 28)), np.random.randint(0, 10))

dataset = tf.data.Dataset.from_generator(
    data_generator,
    output_signature=(
        tf.TensorSpec(shape=(28, 28), dtype=tf.float32),
        tf.TensorSpec(shape=(), dtype=tf.int32)
    )
)

# Depuis fichiers
dataset = tf.data.Dataset.list_files('path/to/images/*.jpg')
```

#### Transformations de jeux de données

```python
# Fonction map
def preprocess_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image)
    image = tf.image.resize(image, [224, 224])
    image = tf.cast(image, tf.float32) / 255.0
    return image

dataset = dataset.map(preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)

# Lot et mélange
dataset = dataset.shuffle(buffer_size=1000)
dataset = dataset.batch(32)
dataset = dataset.prefetch(tf.data.AUTOTUNE)

# Augmentation de données
def augment_image(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=0.1)
    return image, label

train_dataset = train_dataset.map(augment_image)
```

### Évaluation et prédiction de modèles

#### Évaluation

```python
# Évaluer sur données test
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

# Métriques personnalisées pendant évaluation
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy', 'sparse_top_k_categorical_accuracy']
)

# Évaluation détaillée
predictions = model.predict(X_test)
predicted_classes = tf.argmax(predictions, axis=1)
```

#### Callbacks

```python
from tensorflow.keras.callbacks import *

# Arrêt précoce
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

# Points de contrôle du modèle
checkpoint = ModelCheckpoint(
    filepath='best_model.h5',
    monitor='val_accuracy',
    save_best_only=True,
    save_weights_only=False
)

# Planification du taux d'apprentissage
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.2,
    patience=5,
    min_lr=0.001
)

# Callback personnalisé
class CustomCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') > 0.95:
            print(f"\nAtteint 95% précision à l'époque {epoch+1}")
            self.model.stop_training = True
```

### Optimiseurs

```python
from tensorflow.keras.optimizers import Adam, SGD, RMSprop, Adagrad

# Optimiseur Adam
optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)

# SGD avec momentum
optimizer = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

# RMSprop
optimizer = RMSprop(learning_rate=0.001, rho=0.9)

# Planification personnalisée du taux d'apprentissage
def scheduler(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * tf.math.exp(-0.1)

lr_callback = tf.keras.callbacks.LearningRateScheduler(scheduler)
```

### Fonctions de perte

```python
from tensorflow.keras.losses import *

# Pertes de classification
SparseCategoricalCrossentropy()
CategoricalCrossentropy()
BinaryCrossentropy()

# Pertes de régression
MeanSquaredError()
MeanAbsoluteError()
Huber()

# Fonction de perte personnalisée
def custom_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

model.compile(optimizer='adam', loss=custom_loss)
```

### Métriques

```python
from tensorflow.keras.metrics import *

# Métriques de classification
Accuracy()
Precision()
Recall()
AUC()
TopKCategoricalAccuracy(k=5)

# Métriques de régression
MeanSquaredError()
MeanAbsoluteError()
RootMeanSquaredError()

# Métrique personnalisée
class CustomMetric(tf.keras.metrics.Metric):
    def __init__(self, name='custom_metric', **kwargs):
        super(CustomMetric, self).__init__(name=name, **kwargs)
        self.total = self.add_weight(name='total', initializer='zeros')
        self.count = self.add_weight(name='count', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        values = tf.cast(tf.equal(y_true, tf.round(y_pred)), tf.float32)
        self.total.assign_add(tf.reduce_sum(values))
        self.count.assign_add(tf.cast(tf.size(values), tf.float32))

    def result(self):
        return self.total / self.count
```

### Sauvegarde et chargement de modèles

```python
# Sauvegarder modèle entier
model.save('my_model.h5')
model.save('my_model')  # format SavedModel

# Charger modèle
loaded_model = tf.keras.models.load_model('my_model.h5')

# Sauvegarder/charger poids seulement
model.save_weights('model_weights.h5')
model.load_weights('model_weights.h5')

# Sauvegarder architecture du modèle
model_json = model.to_json()
with open('model_architecture.json', 'w') as json_file:
    json_file.write(model_json)
```

### Techniques d'entraînement avancées

#### Entraînement en précision mixte

```python
# Activer précision mixte
policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

# Modèle avec précision mixte
model = Sequential([
    Dense(128, activation='relu'),
    Dense(10, activation='softmax', dtype='float32')  # garder softmax en float32
])
```

#### Gradient tape (entraînement personnalisé)

```python
@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_function(y, predictions)
    
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    train_accuracy.update_state(y, predictions)
    return loss

# Boucle d'entraînement personnalisée
for epoch in range(epochs):
    for x_batch, y_batch in train_dataset:
        loss = train_step(x_batch, y_batch)
```

### Modèles courants de LeetCode

```python
# Modèle de classification binaire
def create_binary_classifier(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_dim,)),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

# Classification multi-classes
def create_multiclass_classifier(input_dim, num_classes):
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_dim,)),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Prédiction de séries temporelles
def create_lstm_model(sequence_length, n_features):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(sequence_length, n_features)),
        LSTM(50, return_sequences=False),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# CNN pour classification d'images
def create_cnn_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Ensemble de modèles
def create_ensemble_model(models):
    inputs = Input(shape=input_shape)
    outputs = [model(inputs) for model in models]
    averaged = tf.keras.layers.Average()(outputs)
    ensemble_model = Model(inputs=inputs, outputs=averaged)
    return ensemble_model
```
