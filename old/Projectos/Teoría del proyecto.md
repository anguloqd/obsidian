# Teoría del proyecto

<aside>
💡 Tabla de contenidos

</aside>

# 1. Modelos de algoritmos de AR

---

Para resolver un problema, un algoritmo de AR puede decidir usar tres métodos:

1. **Métodos del crítico**: son métodos concentrados en la función acción-valor.
Dada una política de base con resultados decentes, busca encontrar una mejor política basada en la expectativa de rendimientos de la política base. Hace esto buscando una política $\pi^*$ que maximice $v_{\pi^*}(s)$ para todo estado posible.
    - **Q-learning** busca la mejor política basándose en la función Q de acción valor.
    - **Deep Q-Learning** utiliza una red neuronal que toma como input un estado y suelta como output las estimaciones de Q con las acciones posibles.
    
    Un problema de los métodos del crítico es que solo funcionan con conjuntos de acciones y estados que sean finitos y discretos. 
    
2. **Métodos del actor**: son métodos en aprender la política óptima en vez de “caer sobre ella”, como lo hace el método del crítico.
    - **Búsqueda del gradiente de la política**: básicamente, imaginamos una política como una función de un vector de parámetros $\theta$. Luego, hacemos ascenso por gradiente de una función “rendimiento global” o por cada función estado-valor por cada estado $s$.
3. **Métodos del crítico y actor**: son métodos mixtos.
*En esencia, es la versión de diferencia temporal del gradiente de la política.* 
Basícamente, actualizamos simultáneamente la estimación de la función Q (crítico) y la estimación de los parámetros $\theta^*$ de la política o la distribución de probabilidad de las acciones óptima $\pi^*$ (actor).
Existen varias formas de definir la actualización de los gradientes de $\theta$, aquí hay algunos:
    
    ![Untitled](Teori%CC%81a%20del%20proyecto%207771eff31ff94be8b368ad15086276fe/Untitled.png)
    
    *(En esta escritura, $\pi_\theta(s,a)$ es la probabilidad de tomar acción $a$ en estado $s$)*
    

# 2. Algoritmos de AR utilizados

---

## A2C: Advantage Actor-Critic

---

Introduce una **función “ventaja”** para reducir la grandísima varianza que tiene el método de gradiente de política original. Es una analogía de la diferencia temporal. Intuitivamente, se interpreta como cuán mejor es, en estado $s$, tomar una acción específica en en vez de la acción que la política en expectativa regresaría. Al final, hacemos esto para reducir la variabilidad del gradiente de la política.

### Algoritmo

---

Notemos que $\theta$ es el vector parámetros de la política $\pi_\theta$ y $w$ es el vector parámetros de la función $Q_w(s,a)$.

1. Empieza en un estado inicial s y toma una acción $a = \pi(a|s)$.
2. En el tiempo inicial t, samplea una recompensa $R(s,a)$ y un próximo estado $s’ \sim P(s’|s,a)$.
3. Luego samplea una próxima acción $a’$ a partir de tu política $\pi_\theta$.
4. Actualiza $\theta$ según el método de actualización Advantage. 
    
    $$
    \theta \leftarrow \theta + \alpha_\theta(\mathbb{E}_{\pi_\theta}[\nabla_\theta \log_{\pi_\theta}(s,a) \space \cdot \space A_w(s,a)],
    \newline
    A_w(s,a) = Q_w(s, a) - V(s,a)
    $$
    
5. Actualiza $w$ con un método similar al de $\theta$:
    
    $$
    w \leftarrow w + \alpha_w(\delta_t \space \cdot \space \nabla_wQ_w(s,a)),
    \newline
    \delta_t = r_t + \gamma Q_w(s',a')-Q_w(s,a)
    $$
    
6. Asigna $s \leftarrow s’, \ a \leftarrow a’$. Recomienza hasta terminar.

## DDPG: Deep Deterministic Policy Gradient

---

El actor **asigna directamente una acción determinística** a un estado, en vez de asignar una distribución de probabilidades de acciones (incluso si el espacio de acciones es continuo y no discreto). También usa dos redes “target” u objetivo, que son las redes para ayudar a las redes originales a ser optimizadas.

### Bases teóricas

---

Se introducen 4 aspectos para la base del algoritmo:

1. **Búfer de reproducción**: durante cada episodio, se van guardando tuplas de experiencia de la forma $\{s_t, a_t, r_t, s_{t+1}\}$ en un caché de tamaño finito. Luego, al actualizar los parámetros de las redes Q y de política, tomamos una muestra de nuestro caché y promediamos los gradientes de cada tupla de experiencia.

2. **Actualización de las redes originales**: para la red Q original, es parecida al modelo de diferencia temporal. SIn embargo, el “objetivo” en nuestra diferencia temporal (la dirección hacia donde se mueve nuestros parámetros) utiliza el Q de la red “target” Q.
    
    $$
    G_t = r_t + \gamma Q'(s_{t+1}, \space \mu(s_{t+1}|\theta^{\mu'})|\theta^{Q'})
    $$
    
    Luego, calculamos la función pérdida como la diferencias cuadradas del Q-objetivo temporal con respecto al antiguo Q. L es finalmente lo que queremos optimizar.
    
    $$
    L = \frac{1}{N} \sum_t (G_t-Q(s_i,a_i|\theta^Q))^2
    
    \newline
    
    \theta^Q \leftarrow \theta^Q - \alpha \nabla_{\theta^Q} L
    $$
    
    Para la red política, queremos maximizar $J(\theta) = \mathbb{E}[Q(s,a)|s=s_t, a_t = \mu(s_t)]$.
    El gradiente de un solo ejemplo sería:
    
    $$
    \nabla_{\theta^\mu} J(\theta) \approx \nabla_aQ(s_t,\mu(s_t)) \space \cdot \space \nabla_{\theta^\mu}\mu(s_t|\theta^\mu)
    $$
    
    Entonces, si los pasamos por varios ejemplos (las tuplas de experiencia del búfer de reproducción), el gradiente sería igual al promedio de los gradientes de cada tupla:
    
    $$
    \nabla_{\theta^\mu} J(\theta) \approx \frac{1}{N} \sum_t
    \nabla_aQ(s_t,\mu(s_t)) \space \cdot \space \nabla_{\theta^\mu}\mu(s_t|\theta^\mu)
    
    \newline
    
    \theta^\mu \leftarrow \theta^\mu + \alpha\nabla_{\theta^\mu} J
    
    \newline
    
    \phantom{0}
    $$
    
3. **Actualización de las redes “target”**: hacemos una copia de los parámetros de las redes target y que sigan por detrás lentamente a las redes originales.
    
    $$
    \theta^{Q'} \leftarrow \tau\theta^Q + (1-\tau)\theta^{Q'}
    
    \newline
    
    \theta^{\mu'} \leftarrow \tau\theta^\mu + (1-\tau)\theta^{\mu'}
    
    \newline
    
    \phantom{0.75}
    $$
    
4. **Exploración**: recordemos que el espacio de acciones es considerado continuo en este algoritmo. Por lo tanto, inyectaremos ruido a las acciones de la red target de acción.

$$
\mu'(s_t) = \mu(s_t|\theta_t^\mu) + \mathcal{N}
$$

### Algoritmo

---

Inicia los parámetros de las redes originales $\theta^Q$, $\theta^\mu$ , las redes target $\theta^{Q’}$, $\theta^{\mu’}$, el búfer de reproducción R. Por los momentos, los pesos de una red target son los mismos de su análogo original.

1. Empieza en un estado inicial $s_1$.
2. Selecciona una acción $a_1$ = $\mu(s_t|\theta^\mu) + \mathcal{N}_t$.
3. Guarda la transición $\{s_t, a_t, r_t, s_{t+1} \}$ en el búfer $R$.
4. Calcula la pérdida de la red crítica usando el error temporal con Qs cruzadas. Minimiza esta función y actualiza $\theta^Q$.
5. Samplea una muestra de $R$ y actualiza los parámetros $\theta^\mu$ con ascenso por gradiente de la función $J(\theta)$.
6. Actualiza los parámetros de las redes target $\theta^{Q’}$ y $\theta^{\mu’}$.
7. Recomienza hasta llegar al tiempo episodio terminal.

## PPO: Proximal Policy Optimization

---

Es un algoritmo para asegurar que las actualizaciones hechas a la política no sean tan volátiles. Está basado en la simplificación de otro algoritmo llamado Trust Region Policy Optimization (TRPO). Introduce un **término de “clip”** tal que las actualizaciones no sean más extremas que ese término. 

### Bases teóricas

---

### Problemas con el gradiente de política clásico y TRPO

---

El problema con la optimización de políticas clásica es que **actualiza los parámetros muy lejos de su valor original**, por lo que toma mucha tiempo, quizás nunca, en converger a los valores teóricamente óptimos. Tales actualizaciones de política son llamadas “actualizaciones de política destructivamente grandes”.

Particularmente, veamos la función $J(\theta)$ usando el término de “ventaja”. La varianza aquí viene de la estimación de valor contenida en el término de ventaja.

$$
J(\theta) = \mathbb{E}_t[\nabla_\theta \log(\pi_\theta(a_t|s_t)) \space \cdot \space Ât]

\newline

\dots
$$

Un intento para corregir este problema fue la introducción de Trust Region Policy Optimization (TRPO). Se introduce una función r(\theta), que se define así:

$$
r(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{viejo}}(a_t|s_t)}
$$

La lógica de este término es medir la distancia la probabilidad de una acción bajo esta nueva distribución de probabilidades dependiente de $\theta$, comparada con los anteriores parámetros. Entre más cerca esté $r(\theta)$ de 1, menos es la distancia de las probabilidades bajo ambos parámetros. 

Finalmente, queremos proponer una nueva función a maximizar, que es la siguiente. La función KL es la divergencia de Kullback-Leiber. $\delta$ es arbitrariamente pequeño.

$$
\argmax_\theta \mathbb{E}_t[\nabla_\theta\frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{viejo}}(a_t|s_t)} \space \cdot \space Ât],

\newline
\phantom{0}
\newline

\text{sujeto a: } \mathbb{E}_t[\text{KL}[\pi_{\theta_{viejo}}(\cdot|s_t), \pi_{\theta_{viejo}}(\cdot|s_t)]] \le \delta.
$$

El único problema con esto es que puede añadir sobrecarga al proceso de optimización, lo que a veces lleva a un comportamiento de entrenamiento indeseable.

Para el algoritmo PPO, se introduce un nuevo término: **objetivo sustituto recortado** (clipped surrogate objective).

$$
J^{CLIP}(\theta) = \mathbb{E}_t[\min(r_t(\theta)\cdotÂ_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \cdot Â_t)]
$$

![Untitled](old/Projects%2091a38a7522204a1eaaeb87fd0f122308/Teoría%20del%20proyecto%207771eff31ff94be8b368ad15086276fe/Untitled%201.png)

Notemos que, si la ventaja para tal acción es positiva, no queremos alejarnos mucho de los que estamos haciendo actualmente. Sin embargo, si la ventaja para tal acción es negativa, no queremos quedarnos estancados allí, por lo que permitiremos pasos más grandes y así deshacemos errores en la política.

### Algoritmo

---

1. Inicia un episodio, un estado inicial $s_1$ y $N$ actores paralelos.
2. **Para cada actor**: ejecuta la política $\pi_{viejo}$ por $T$ pasos de tiempo.
3. Computa las estimaciones de ventaja $A_1, …, A_T$.
4. Optimiza $J_t^{CLIP}$, con muestras de tamaño $M \le NT$ y con $K$ épocas.
**Época**: cantidad de veces que pasas una muestra para actualizar el modelo.
5. Recomienza con otro episodio. Así hasta con el dataset de episodios.

# 3. Implementación

---

## Evaluación de rendimientos

---

Utilizamos la **razón de Sharpe** para evaluar nuestras operaciones. En esencia, la razón de Sharpe compara los rendimientos de una operación con respecto al riesgo de esa operación. 

$$
S = \frac{R_p - R_f}{\sigma_p}
$$

- $R_p$: rendimiento del portafolio/stock/mercado, etc.
- $R_f$: rendimiento sin riesgo (bonos de la tesorería).
- $\sigma_p$: volatilidad del portafolio (desviación estándar).

De otro lado, también utilizamos el **índice de turbulencia** para inducir aversión al riesgo. Este índice de turbulencia se define así:

$$
\mathcal{d}_t = \bold{({y_t} - \mu) \Sigma^{-1} ({y_t} - \mu)'}
$$

- $d_t$: turbulencia de un bien para tiempo t.
- $\bold{y_t}$: vector de los rendimientos de los bienes en tiempo t.
- $\bold{\mu}$: vector de rendimientos promedios históricos del bienes en tiempo t.
- $\bold{\Sigma}$: matriz de covarianza de rendimientos promedios históricos de los bienes en tiempo t.

## Creando una máquina de RL para trading

---

### Datos

---

Se toman los datos del Dow Jones, desde el 01/01/2009 hasta el 08/05/2020. Luego, se divide de esta manera:

1. **Entrenamiento**: del 01/01/2009 al 31/12/2014.
2. **Validación**: del 01/10/2015 al 31/12/2015.
3. **Trading**: del 01/01/2016 al 08/05/2020.

### Trading visto como un proceso de decisión de Markov

---

- **Estados** $s = [\bold{p, h}, b]$: $\bold{p}$ es el vector con los precios, $\bold{h}$ el vector con la cantidad de stocks disponibles y $b$ el balance.
- **Acción $a$**: un vector de acciones sobre los stocks. Las acciones disponibles por cada stock son comprar, vender y holdear, lo que resulta en aumentar, disminuir o dejar identico la cantidad de stocks $h$, respectivamente.
- **Recompensa $r(s,a,s’)$**: recompensa directa de tomar acción $a$ en estado $s$ y llegar a estado $s’$.
- **Política $\pi(s)$**: distribución de probabilidad de acciones en estado $s$.
- **Q-Valor $Q^\pi(s,a)$**: valor esperado de tomar acción $a$ en estado $s$, y luego continuar según la política $\pi$.

![Untitled](old/Projects%2091a38a7522204a1eaaeb87fd0f122308/Teoría%20del%20proyecto%207771eff31ff94be8b368ad15086276fe/Untitled%202.png)

### Restricciones

---

- **Liquidez de mercado**: asumimos que el mercado de acciones no será afectado por nuestro agente.
- **Balance no-negativo**: las acciones permitidas no pueden resultar en balance negativo.
- **Costo de transacciones**: aumismo que el costo de transacción es 1/1000 del valor de cada transacción, sea compra o venta.
- **Aversión al riesgo a la quiebra de mercado**: utilizamos el índice de turbulencia que mide movimientos de precios extremos en títulos valores.

### Objetivo: maximización de rendimientos

---

La función de recompensa se define como el cambio en el valor del portafolio cuando se toma acción $a$ en estado $s$ y se llega a estado $s+1$.

El objetivo entonces conseguir la política que maximice el cambio en el cambio del valor del portafolio $r(s_t, a_t, s_{t+1})$. 

### Definición del espacio de estados y acciones

---

- **Espacio de estados**: utilizamos un vector de 181 dimensiones. Por cada stock, consideramos su precio, la cantidad disponible, MACD, RSI, CCI y ADX. Son 30 stocks, por lo que son 180 inputs. Finalmente, agregamos un último input para nuestro balance.
- **Espacio de acciones**: para un stock determinado, el espacio de acciones es $\{-k,\dots,-1,0,1,\dots,k\}$, donde $k$ y $-k$ representa los stocks que podemos comprar y vender respectivamente. Agregamos la condición de $k \le h_{max}$, este último es un parámetro predefinido para una cantidad máxima de compra de un stock.

Deducimos entonces que para múltiples stocks, el tamaño del espacio de acciones es $(2k+1)^{30}$.

Normalizamos finalmente el el espacio de acción a $[-1, 1]$. Esto ya que A2C y PPO definen la política direcctamente en una distribución gaussiana, por lo que necesita ser normalizada y simétrica.

## Estrategia de trading

---

Basícamente, se utilizan los tres agentes mencionados (A2C, DDPG y PPO) en paralelo.

1. **Durante el subconjunto de entrenamiento**: usamos una ventana de n meses que alimentamos a nuestros agentes para entrenar, esto se hace cada 3 meses. Es decir, se entrenan los agentes en los primeros 3 meses, luego se entrenan los agentes con los primeros 6 meses, luego con los primeros 9 meses, así hasta llegar al final del subconjunto de entrenamiento.
2. **Durante el subconjunto de validación**: utilizamos una ventana móvil de 3 meses para evaluar y ajustar parámetros de cada agente.
3. **Durante el trading**: tomamos el agente que actuó mejor en los últimos 3 meses (según el mayor ratio de Sharpe) y lo seleccionamos para tradear en los próximos 3 meses.

# 4. Links relevantes

---

[Deep Reinforcement Learning for Automated Stock Trading](https://towardsdatascience.com/deep-reinforcement-learning-for-automated-stock-trading-f1dad0126a02)

[Deriving Policy Gradients and Implementing REINFORCE](https://medium.com/@thechrisyoon/deriving-policy-gradients-and-implementing-reinforce-f887949bd63)

[Deep Q-Network (DQN)-II](https://towardsdatascience.com/deep-q-network-dqn-ii-b6bf911b6b2c)

[Understanding Actor Critic Methods](https://towardsdatascience.com/understanding-actor-critic-methods-931b97b6df3f)

[Deep Deterministic Policy Gradients Explained](https://towardsdatascience.com/deep-deterministic-policy-gradients-explained-2d94655a9b7b)

[Deep Deterministic Policy Gradient(DDPG) - an off-policy Reinforcement Learning algorithm](https://medium.com/intro-to-artificial-intelligence/deep-deterministic-policy-gradient-ddpg-an-off-policy-reinforcement-learning-algorithm-38ca8698131b)

[Understanding and Implementing Proximal Policy Optimization (Schulman et al., 2017)](https://towardsdatascience.com/understanding-and-implementing-proximal-policy-optimization-schulman-et-al-2017-9523078521ce)

[Sharpe Ratio Definition](https://www.investopedia.com/terms/s/sharperatio.asp)

[Measuring Financial Turbulence and Systemic Risk](https://towardsdatascience.com/measuring-financial-turbulence-and-systemic-risk-9d9688f6eec1)