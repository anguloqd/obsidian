# informática 2 // redes neuronales artificiales

Date de création: June 12, 2022 11:44 PM
Modifié: November 8, 2024 10:25 AM

[Artificial Neural Network | Brilliant Math & Science Wiki](https://brilliant.org/wiki/artificial-neural-network/)

[Backpropagation | Brilliant Math & Science Wiki](https://brilliant.org/wiki/backpropagation/)

[Neural networks and deep learning](http://neuralnetworksanddeeplearning.com/chap2.html)

# Introducción

---

## Contexto

- Hace falta decir que hay una infinidad de funciones que puede pasar por todos los pares ordenados, pero la mejor función es la que puede, además, hacer funciones.
- Las RNA (redes neuronales artificiales) son suficientemente flexibles para dos tipos de problemas:
    - **Clasificación**: predicción de clasificación de elementos que no tienen una relación numérica.
    - **Regresión**: variables con relación numérica.
- Un **algoritmo de aprendizaje no supervisado** es lo mismo que con aprendizaje supervisado, pero no utiliza ejemplos conocidos para llegar a la mejor función.
- Pueden usar dos tipos de aprendizaje (incluso ambos): aprendizaje por lotes o aprendizaje "en línea" o continuo.
    - **Aprendizaje por lotes (”batch learning”)**: utiliza un lote de información que será alimentada a la RNA.
    - **Aprendizaje en línea (”online learning”)**: utiliza información que va llegando continuamente a ella.

# Recordatorio de matemáticas

---

## Álgebra y cálculo básico

Lo siguiente son las bases de matemáticas necesarias utilizadas en el cuadro de redes neuronales:

- Tal como aprendimos antes, una neurona tiene una activación igual a $f(wx + b)$, donde cada input $x$ es ponderado con $w$, y a toda esa suma se le agrega el umbral $b$ y por último se le aplica una función $f$.
- La "magnitud" o módulo $|| \cdot ||$ de un vector (longitud desde el origen, magnitud en el sentido euclidiano) nos ayuda cuando tratamos tiempos de convergencia de entrenamiento.
    
    $$
    ||\bold x||_2 = ||(x_1, \dots, x_n)||_2 =\sqrt{\sum_{k=1}^n x^2_k}
    $$
    
- La normalización de un vector es el proceso de tomar un vector y luego crear un vector de magnitud 1 con la misma dirección que el vector original.
    
    $$
    \vec{p} = \left( \frac{a}{\sqrt{a^2 + b^2 + c^2}}, \frac{b}{\sqrt{a^2 + b^2 + c^2}}, \frac{c}{\sqrt{a^2 + b^2 + c^2}} \right)
    $$
    
- El **producto diádico** o **producto tensorial** (en inglés, *outer product*, aunque esa traducción no parece existir en español ni en francés), es una operación entre un vector columna y un vector fila, pero no se debe confundir con el **producto punto** entre una columna y un vector.

Teniendo dos vectores columnas, $\bold u$ y $\bold v$, tenemos que:
    
    $$
    \bold u = \begin{bmatrix} a \\ b \\ c \end{bmatrix} \quad , \quad \bold v = \begin{bmatrix} d \\ e \end{bmatrix} \implies \bold u \bold v^\mathsf{T} = \begin{bmatrix} a \\ b \\ c \end{bmatrix} \begin{bmatrix} d & e \end{bmatrix} = \begin{bmatrix} a \cdot d & a \cdot e \\ b \cdot d & b \cdot e \\ c \cdot d & c \cdot e \end{bmatrix}
    $$
    
- El **gradiente de una función** es el vector columna de todas la derivadas parciales con respecto a sus variables inputs.
    
    $$
    \nabla f(x,y, z) =
    \begin{bmatrix}
    \frac{\partial f}{\partial x}
    \\[5pt]
    \frac{\partial f}{\partial y}
    \\[5pt]
    \frac{\partial f}{\partial z}
    \end{bmatrix}
    $$
    
    - Si tomamos un punto en la función, el gradiente evaluado en ese punto muestra el vector con **origen en ese punto** tal que el valor de la función aumenta más.
    
    En la próxima imagen, empezamos arbitrariamente en el punto $(1,1)$, donde el valor de la función $C$ es igual $4$. Queremos saber hacia qué dirección el valor actual de la función aumenta lo mas posible.
        
        ![El gradiente de C es $\nabla C = \begin{bmatrix} 3x & y\end{bmatrix}^\mathsf{T}$, y luego es evaluado en el punto $(1,1)$, lo que nos dice que la dirección de mayor crecimiento es la dirección apuntada por el vector [3, 1].](informa%CC%81tica%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/image.png)
        
        El gradiente de C es $\nabla C = \begin{bmatrix} 3x & y\end{bmatrix}^\mathsf{T}$, y luego es evaluado en el punto $(1,1)$, lo que nos dice que la dirección de mayor crecimiento es la dirección apuntada por el vector [3, 1].
        
        ![Viendo el plot de $C(x,y) = \frac{3}{2}x^2 + \frac{1}{2}y^2$ (donde el eje $z$ son los valores de $C(x,y)$), si imaginamos el punto $p = (1,1,2)$ sobre la función y “plasmamos” el vector $[3,1]$ sobre el tejido de la función con origen en $p$ (es decir, el vector $[4,2]$), obtendremos la dirección mas directa al crecimiento del valor de $C$.](informa%CC%81tica%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/image%201.png)
        
        Viendo el plot de $C(x,y) = \frac{3}{2}x^2 + \frac{1}{2}y^2$ (donde el eje $z$ son los valores de $C(x,y)$), si imaginamos el punto $p = (1,1,2)$ sobre la función y “plasmamos” el vector $[3,1]$ sobre el tejido de la función con origen en $p$ (es decir, el vector $[4,2]$), obtendremos la dirección mas directa al crecimiento del valor de $C$.
        
    
    ![Los puntos azules son $(1,1)$, $(1,1,2)$, y el punto verde debería representar el vector gradiente $(4,2)$ o equivalentemente $[3,1]$ si tomamos como origen $(1,1)$.](60bbd781-439d-4829-8a10-e6abcae39adf.png)
    
    Los puntos azules son $(1,1)$, $(1,1,2)$, y el punto verde debería representar el vector gradiente $(4,2)$ o equivalentemente $[3,1]$ si tomamos como origen $(1,1)$.
    
    ![El punto verde sobre la función es la imagen del vector gradiente evaluado en $(1,1)$, es decir, $C(4,2)$, cuyo valor es $26$.](8edf9476-8d82-45c8-8b20-d67c803910a8.png)
    
    El punto verde sobre la función es la imagen del vector gradiente evaluado en $(1,1)$, es decir, $C(4,2)$, cuyo valor es $26$.
    
    - Lo interesante es que si multiplicamos por $-1$ el gradiente, obtenemos la dirección de mayor descenso.

## Descenso por gradiente, en la teoría

Normalmente, para optimizar una función, igualamos su derivada a $0$ y buscamos los valores de las variables. Sin embargo, este último paso suele ser imposible, por lo que tomamos una solución heurística: el descenso por gradiente.

El descenso por gradiente es un algoritmo iterativo para encontrar el mínimo de una función.

1. Empezamos en un punto $p$ aleatorio.
2. Computamos $\nabla G(p)$, que es el gradiente en ese punto.
3. Nos movemos al contrario de esa dirección un poco, es decir, $p_{t+1} = p_t - \varepsilon \nabla G(p)$, donde $\varepsilon$ es el tamaño del paso o formalmente llamada “tasa de aprendizaje”, y que en la practica suele ser un valor pequeño.
4. Comenzamos desde el paso 2.
5. Nos detenemos en un momento donde la diferencia abs. entre $p_{t+1}$ y $p_t$ sea arbitrariamente pequeña.

![image.png](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/image%202.png)

# Perceptrones

---

## Algoritmo de aprendizaje de un perceptrón

- Esta es una tarea de clasificación, por lo que los puntos forman parte de dos grupos: los llamaremos 1 y -1.
- Primero, queremos definir una función de "pérdida". Esta función de pérdida nos indica la suma de cuán lejos está la observación real yi de la proyección o frontera de decisión (w*xi + u), para cada dato de índice i.
    - Ejemplo: pensemos en un punto bien clasificado cuyo grupo es (1) y está por encima de la frontera de decisión. No nos importa cuán lejos esté el punto de la recta, sino que esté en el buen lado de la recta.
    - Por lo tanto, no nos interesa el valor numérico de la distancia [xi - (w*xi + u)], sino que sea positiva.
    - Similarmente, si xi pertenece al grupo (-1), queremos que esté por debajo de la frontera., sin importar cuán debajo. Entonces, queremos que la distancia [xi - (w*xi + u)] sea negativa.
    - Contamos un punto como malclasificado si, xi es grupo (1) y distancia es negativa, o si xi es grupo (-1) y distancia es positiva.
    - Finalmente, podemos simplificar si aplicamos la función signo() a la distancia [xi - (w*xi + b)]. El resultado sería:
        
        Notemos que lo que está dentro de los corchetes es una preposición. Los corchetes son una función indicación, que devuelve 1 si la prop. es verdadera y 0 si es falsa. De esa manera, contamos finalmente los puntos malclasificados.El algoritmo se va aplicar hasta que la función pérdida sea = 0.
        
- Xi sería el input. Eso sí, es un vector input, por lo que no es necesariamente un número, sino un vector columna de n dimensiones. Yi sería finalmente el color o grupo binario al que pertenece la observación.
- Para actualizar el peso y el umbral, la fórmula es la siguiente, aplicándola con el par (xi, yi) que fue malclasificado:
- El algoritmo es entonces el siguiente:
    1. Inicializamos el peso w y el umbral b. Por ejemplo, los igualamos ambos a 0.
    2. Luego, vamos a recorrer nuestro conjunto de puntos [(x1, y1), ..., (xn,yn)] y vamos aplicando el criterio de clasificación hasta que encontremos el primer punto malclasificado.
    3. Actualizamos el peso y el umbral con respecto a ese punto donde tuvimos un error. Luego recomenzamos desde ese punto i de 1 en 1 hasta el punto (i - 1). Puede ser que el mismo punto i vuelva a fallar, por lo que volvemos a calibrar w y b.
    4. Hemos encontrado una frontera de decisión válida cuando nuestra función de pérdida = 0 para ciertos parámetros w y b.
        
        (El GIF de ejemplo mantiene un umbral siempre = 0)
        
- ¡La frontera de decisión no es única! Hay una infinidad de líneas que separan dos grupos.

## Limitaciones y nueva función de pérdida

- Cuando los datos siguen una función de base que no es lineal, un clasificador lineal no actúa de la mejor manera. Hay un par de cambios que podemos hacer:
- Tomamos una nueva función pérdida llamada "pérdida conjunta" o "pérdida de eje". En vez de contar los errores, contamos la magnitud del error. Esto penaliza propocionalmente los puntos más lejos, e incluso puede penalizar los puntos bien clasificados pero muy cerca de la frontera de decisión.
- Luego, también queremos que el algoritmo sea robusto a los outliers. Los outliers aumentan considerablemente el tiempo de entrenamiento, pues modifican mucho w y b tal que los valores que ya estaban bien clasificados pasan a estar mal clasificados.
- La nueva función de pérdida definitiva, donde L es la pérdida de eje, sería entonces la siguente. Es conocido cono el algoritmo "pasivo-agresivo".
    
    
- **Dato**: agregar una capa intermedia de neuronas nos permite modelar fronteras de decisión no lineales.

# Retropropagación

---

## Ingredientes

La retropropagación es un método que nos permite encontrar el gradiente, tal que podemos aplicar el algoritmo de descenso por gradiente.

<aside>
💡 Se llama “retropropagación” porque, para calcular el gradiente y actualizar los parámetros, comenzamos calculando la derivada delos parámetros de la ultima capa $\bold w^{(L)}$.

Luego, la derivada de la capa $L-1$ depende de los valores de la derivada calculada en la capa $L$, y luego los valores de la capa $L-2$ dependen de los valores de la capa $L-1$, así hasta llegar a la primera capa oculta.

Así, vemos que los valores de las capas de neuronas frontales influencias los valores de las capas de neuronas traseras.

</aside>

### Dataset

El dataset X es una conjunto de pares input-output $(\vec x_i, \vec y_i)$, donde $\vec x_i$ es el input mientras que $\vec y_i$ es el output. Recordemos que cada vector es una lista de valores, entonces los inputs y los outputs pueden ser multidimensionales.

Tal conjunto de inputs-outputs de tamaño $N$ es notado como sigue :

$$
X = \big\{ (\vec x_i, \vec y_i), \dots, (\vec x_N, \vec y_N)\big\}
$$

### Red neuronal

Un poco obvio, pero evidentemente necesitamos una red neuronal. Lo importante es que sus parámetros—todos los pesos $w^l_{jk}$ y umbrales $b^l_j$—están contenidos en la variable $\theta$.

### Función de costo

Primero, necesitamos una función de costo. No la llamamos “error” puesto a que utilizamos el nombre “error” para otro término importante en la retropropagación. La función mas clásica utilizada es la función de costo cuadrático total $(C_1)$ o costo cuadrático medio $(C_2)$. 

$$
\begin{align*}
&C_1(X, \theta)= \frac{1}{2} \sum_{i=1}^N (\hat y_i - y_i)^2\\
&C_2(X, \theta)= \frac{1}{2N} \sum_{i=1}^N (\hat y_i - y_i)^2\\
\end{align*}
$$

La razón de por qué hay un coeficiente de $1/2$ en frente de la suma de costos, es porque, al derivar la suma de costos, el exponente $2$ que baja se cancela al multiplicarse con el $1/2$ que esta al frente. Esto es mas cómodo que si no tuviésemos ese coeficiente al frente.

Un punto importante es que, en este contexto, no utilizamos el nombre “error” para la función de costo, puesto a que utilizamos el nombre “error” para otro término importante en la retropropagación.

## La retropropagación en sí

### Primeras derivadas del costo

Lo que estamos buscando es aplicar una iteración de actualización de parámetros. Si aplicamos la teoría en la practica, lo que estamos buscando es :

$$
\theta_{t+1}=\theta_t-\alpha\frac{\partial C(X, \theta_t)}{\partial \theta_t}
$$

Recordemos que $\theta_t$ contiene los pesos $w^{(l)}_{jk}$ y umbrales $b^{(l)}_j$ en tiempo $t$. Ademas, denotaremos $C(X,\theta)$ como simplemente $C$. Si bien podemos derivar $C$ con respecto a $\theta_t$ directamente, es mejor derivar $C$ con respecto a $w^{(l)}_{jk}$ y $b^{(l)}_j$ de manera separada para poder aprender.

Recordemos algunas formulas:

$$
\begin{align*}
& z^{(l)}_j = w^{(l)}_{jk} a^{(l-1)}_j+b^{(l)}_j \\
& a^{(l)}_j= \sigma(z^{(l)}_j)
\end{align*}
$$

Donde $z^{(l)}_j$ es la suma ponderada o “suma intermedia”, y $a^{(l)}_j$ es la activación. $\sigma$ es una función de activación. Con esto, ya podemos empezar a derivar:

$$
\begin{align*}
& \frac{\partial C}{\partial w^{(l)}_{jk}} = 
\underbrace{
\frac{\partial C}{\partial a^{(l)}_j} \frac{\partial a^{(l)}_j}{\partial z^{(l)}_j} 
}_{\delta^{(l)}_j}
\frac{\partial z^{(l)}_j}{\partial w^{(l)}_{jk}}

\\[35pt]

& \frac{\partial C}{\partial b^{(l)}_{j}} = 
\underbrace{
\frac{\partial C}{\partial a^{(l)}_j} \frac{\partial a^{(l)}_j}{\partial z^{(l)}_j} 
}_{\delta^{(l)}_j}\frac{\partial z^{(l)}_j}{\partial b^{(l)}_{j}}
\end{align*}

\\[-10pt]
$$

Notemos que hay un factor común entre ambas derivadas parciales: $\delta^{(l)}_j$, también llamado el “error”. Concretamente, lo definimos como sigue:

$$
\delta_j^{(l)} \equiv
\frac{\partial C}{\partial z^{(l)}_j} =
\frac{\partial C}{\partial a^{(l)}_j} \frac{\partial a^{(l)}_j}{\partial z^{(l)}_j}
$$

Calcularemos exactamente lo que es $\delta_j^{(l)}$ mas tarde. Por los momentos, calcularemos solo las derivadas de la suma intermedia con respecto a los pesos $w^{(l)}_ {jk}$ y umbrales $b^{(l)}_j$.

$$
\frac{\partial z^{(l)}_j}{\partial w^{(l)}_{jk}} = a^{(l-1)}_k,\hspace{5pt} \frac{\partial z^{(l)}_j}{\partial b^{(l)}_{j}} = 1

\\[15pt]

\implies \frac{\partial C}{\partial w^{(l)}_{jk}}=\delta^{(l)}_ja^{(l-1)}_k,

\hspace{5pt}

\frac{\partial C}{\partial b^{(l)}_{j}} = \delta^{(l)}_j
$$

**Una cosa importante a saber es que derivamos los calculamos de la capa de salida de manera diferente que las capas ocultas.**

Es útil también escribir $\delta^{(L)}$ en forma matricial y no en forma componente:

$$
\bold \delta^{(L)}=\nabla_{\bold a^{(L)}}  C\odot \sigma^\prime(\bold z^{(L)}), \text{ donde }\nabla_{\bold a^{(L)}} C\equiv[\partial C/\partial a^{(L)}_j]^{\mathsf{T}}_{\forall j \in [1, n_L]}
$$

Y, dado que definimos $C$ como el error cuadrático, tenemos que:

$$
\delta^{(L)}=(\bold a^{(L)} - \bold y) \odot \sigma^\prime(\bold z^{(L)})
$$

### La capa de salida (outputs)

Suponiendo que hemos definido la función de error como $C(X, \theta)= \frac{1}{2} \sum_{i=1}^N (\hat y_i - y_i)^2$, calculando los otros términos y poniendo todo junto:

$$
\begin{align*}

&& \frac{\partial C}{\partial a^{(L)}_j} = (a^{(L)}_j-y_i),\hspace{5pt} \frac{\partial a^{(L)}_j}{\partial z^{(L)}_j} =\sigma^\prime(z^{(L)}_j)

\\[30pt]

& \implies & \delta^{(L)}_j=(a^{(L)}_j-y_i) \space \sigma^\prime(z^{(L)}_j)

\\[30pt]

& \implies & \frac{\partial C}{\partial w^{(L)}_{jk}} =(a^{(L)}_j-y_i) \space \sigma^\prime(z^{(L)}_j) a^{(L-1)}_j,

\\[15pt]

&& \text{ y también } \frac{\partial C}{\partial b^{(L)}_{j}}=(a^{(L)}_j-y_i) \space \sigma^\prime(z^{(L)}_j) 

\end{align*}

$$

### Las capas ocultas

Para las capas ocultas, nos sera muy útil la llamada “formula de retropropagación”. Recordemos que en las capas ocultas $l$, $1 < l < L$, donde $L$
 es la ultima capa de la red.

Trabajando desde la definición de $\delta^{(l)}_j$, tenemos que:

$$
\delta^{(l)}_j = 
\frac{\partial C}{\partial z^{(l)}_j} =
\sum_{i=1}^{n_{l+1}} \frac{\partial C}{\partial z^{(l+1)}_i}\frac{\partial z^{(l+1)}_i}{\partial z^{(l)}_j} =
\sum_{i=1}^{n_{l+1}} \delta^{(l+1)}_i\frac{\partial z^{(l+1)}_i}{\partial z^{(l)}_j}
$$

Si alguna vez no te acuerdas de por qué $\delta^{(l)}_j = 
\frac{\partial C}{\partial z^{(l)}_j} =
\sum_{i=1}^{n_{l+1}} \frac{\partial C}{\partial z^{(l+1)}_i}\frac{\partial z^{(l+1)}_i}{\partial z^{(l)}_j}$ , toma $\frac{\partial C}{\partial z^{(l)}_j}$ y reemplaza $C$ con su definición con una red neuronal simple sin capas ocultas, con un input y dos outputs, y trabaja desde ahí. La suma que te confunde mucho se presenta naturalmente.

Para determinar la segunda derivada parcial, recordemos que:

$$
z^{(l+1)}_j=\sum_{k=0}^{n_{l}}w^{(l+1)}_{jk}a_k^{(l)}+b^{(l+1)}_j=\sum_{k=0}^{n_{l}}w^{(l+1)}_{jk}\sigma(z_k^{(l)})+b^{(l+1)}_j
$$

Diferenciando, tenemos que:

$$
\frac{\partial z^{(l+1)}_i}{\partial z^{(l)}_j}=w^{(l+1)}_{jk}\sigma^\prime(z^{(l)}_j)
$$

Finalmente, volviendo a la definición de $\delta^{(l)}_j$, deducimos la popular formula recursiva de retropropagación:

$$
\delta^{(l)}_j=\sum_{i=1}^{n_{k+1}} \delta^{(l+1)}_i w^{(l+1)}_{jk}\sigma^\prime(z^{(l)}_j)
$$

La formula de retropropagación, también puede ser escrito en forma matricial y no en forma componente:

$$
\bold \delta^{(l)}=\left(\left(\bold w^{(l+1)}\right)^\mathsf{T} \bold \delta^{(l+1)} \right)\odot\sigma^\prime(\bold z^{(l)})
$$

## Descenso por gradiente, en la práctica

Finalmente, conectamos la retropropagación con el descenso por gradiente. Antes, recordemos lo que es un paso de descenso de gradiente para un vector de parámetros $\bold p$ con respecto a una función a optimizar $f$:

$$
\bold p \leftarrow \bold p - \eta \space \nabla_{\bold p}f
$$

Queremos hacer esto con $\bold w^{(l)}$ y $\bold b^{(l)}$, por cada capa $l$, por lo que necesitamos saber qué es $\nabla_{\bold w^{(l)}}C$ y $\nabla_{\bold b^{(l)}}C$ y, en consecuencia, saber qué son $\partial C / \partial w_{jk}^{(l)}$ y $\partial C / \partial b_{j}^{(l)}$. Una definición más general de estos últimos es:

$$
\frac{\partial C}{\partial w^{(l)}_{jk}} = 

\delta^{(l)}_j a^{(l-1)}_k,

\text{ y }

\frac{\partial C}{\partial b^{(l)}_j} = 

\delta^{(l)}_j
$$

Dado a que tomamos el gradiente de $C$ con respecto a los vectores $\bold w^{(l)}$ y $\bold b^{(l)}$, vale decir que la forma de estos gradientes, particularmente $\bold w^{(l)}$, es algo complicada e incómoda.

$$
\nabla_{\bold w^{(l)}} C
=
\delta^{(l)}(\bold a^{(l-1)})^\mathsf T
=
\begin{bmatrix}
\delta_1^{(l)} a_1^{(l-1)} & \delta_1^{(l)} a_2^{(l-1)} & \cdots & \delta_1^{(l)} a_n^{(l-1)} \\
\delta_2^{(l)} a_1^{(l-1)} & \delta_2^{(l)} a_2^{(l-1)} & \cdots & \delta_2^{(l)} a_n^{(l-1)} \\
\vdots & \vdots & \ddots & \vdots \\
\delta_m^{(l)} a_1^{(l-1)} & \delta_m^{(l)} a_2^{(l-1)} & \cdots & \delta_m^{(l)} a_n^{(l-1)}
\end{bmatrix}

\\[8pt]

\nabla_{\bold b^{(l)}} C = \delta^{(l)}
=
\begin{bmatrix}
\delta_1^{(l)} \\
\delta_2^{(l)} \\
\vdots \\
\delta_m^{(l)}
\end{bmatrix}

$$

Perfecto. Por ultimo, supongamos que tenemos $m$ ejemplo de entrenamiento y una tasa de aprendizaje $\eta$. Para actualizar los pesos y umbrales, tenemos que, por cada ejemplo de entrenamiento $x$, la siguiente es la regla de actualización, que es simplemente el promedio de los valores de los gradientes por cada ejemplo de entrenamiento.

$$
\bold w^{(l)} \leftarrow \bold w^{(l)} - \eta  \left( \frac 1 m \sum_x 
\underbrace{
\delta^{(x, l)} \left( \bold a^{(x, l-1)} \right)^\mathsf{T}
}_{\nabla_{\bold w^{(l)}}C^{(x)}}
\right)

\\[10pt]

\bold b^{(l)} \leftarrow \bold b^{(l)} - \eta
\left( \frac 1 m \sum_x \underbrace{\delta^{(x, l)}
}_{\nabla_{\bold b^{(l)}}C^{(x)}}
\right)
$$

Notemos que este es el caso ideal, pero no suele ser el caso más aplicable, pues toma demasiado tiempo y recursos computacionales. Piensa que el algoritmo debe usar *todos* los ejemplos de aprendizaje para solo hacer una iteración de ajuste de los parámetros, es decir, un paso en dirección al gradiente.

Una variante del descenso por gradiente es el **descenso por gradiente estocástico**:

- En vez de utilizar todos los ejemplos de aprendizaje en cada paso de optimización, separamos los ejemplos en lotes, cada lote de tamaño $m$.
- Luego, computamos un paso hacia el gradiente con *un* solo lote, lo que significa que ajustamos los todos los parámetros una sola vez.
- Finalmente, volvemos a pasar otro lote de ejemplos. Y así hasta que los usamos todos.

## Retropropagación como algoritmo

Finalmente, si quisiéramos implementar la retropropagación como algoritmo en un lenguaje de programación, el plan seria el siguiente:

1. Escoger al azar un mini-batch de ejemplos de entrenamiento
2. Por cada ejemplo de entrenamiento $x$: fijar el valor correspondiente de activation $\bold a^{(x,1)}$, y ejecutar los pasos siguientes:
    1. Evaluación hacia adelante (feedforward): para cada capa $l \in \{2, 3, \dots, L\}$, calcular
        
        $$
        \bold z^{(x,l)} = \bold w^{(l)} \bold a^{(x, l-1)} + \bold b^{(l)}
        
        \\
        
        \bold a^{(x,l)} = \sigma( \bold z^{(x, l)})
        $$
        
    2. Error: calcular el vector de error $\delta$
        
        $$
        \bold \delta^{(x,L)} = \nabla_{\bold a^{(L)}}  C^{(x)} \odot \sigma^\prime(\bold z^{(x, L)})
        $$
        
    3. Retropropagación del error: para cada capa $l \in \{L, L-1, L-2, \dots, 2\}$, calcular 
        
        $$
        \bold \delta^{(l)}=\left(\left(\bold w^{(l+1)}\right)^\mathsf{T} \bold \delta^{(l+1)} \right)\odot\sigma^\prime(\bold z^{(l)})
        $$
        
3. Para cada capa $l \in \{L, L-1, L-2, \dots, 2\}$, actualizar los pesos y umbrales con respecto a la regla siguiente:
    
    $$
    \bold w^{(l)} \leftarrow \bold w^{(l)} - \eta  \left( \frac 1 m \sum_x 
    \underbrace{
    \delta^{(x, l)} \left( \bold a^{(x, l-1)} \right)^\mathsf{T}
    }_{\nabla_{\bold w^{(l)}}C^{(x)}}
    \right)
    
    \\[10pt]
    
    \bold b^{(l)} \leftarrow \bold b^{(l)} - \eta
    \left( \frac 1 m \sum_x \underbrace{\delta^{(x, l)}
    }_{\nabla_{\bold b^{(l)}}C^{(x)}}
    \right)
    $$
    

# Redes neuronales convolucionales

---

[A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

Las RNC se basan en entrenar filtros (neuronas intermedias, por ejemplo) para reconocer rasgos "de base" en una imagen, como líneas, por ejemplo. Luego, podemos extraer un mapa de rasgos de cada filtro/neurona, para saber en qué partes de la imagen se encuentra determinado rasgo.

## Operaciones de base

Las operaciones de base son: convolución (convolution), relleno (padding) y zancada (stride).

### Convolución (convolution)

$$
Y_j = g \left( b_j + \sum_i K_{ij} \otimes Y_i \right)
$$

- $Y_j$ (matriz): activación de la neurona posterior $j$.
- $Y_i$ (matriz): activación de la neurona anterior $i$.
- $K_{ij}$ (matriz): neurona filtro.
- $g$: función no-lineal, normalmente ReLU.
- $\otimes$: operador de convolución (producto de Hadamard), donde se multiplican las entradas de mismo índice de dos matrices $K$ e $Y$.

Fíjate que es muy parecido a tomar la combinación linea de pesos con inputs y luego sumar el umbral.

Primero, se toma cada entrada de la matriz $Y_i$ y se multiplica por su correspondiente en $K$. Luego, tomas la suma de las entradas de la matriz resultante y le añades el umbral, por último aplicando la función $g$.

### Zancada (striding)

La convolución requiere una imagen y filtro de iguales dimensiones. Esto a veces no suele ser el caso. De hecho, regularmente, este no es el caso. El filtro suele ser mas pequeño que la imagen a la que aplicamos el filtro.

La zancada la utilizamos cuando nuestro filtro es más pequeño que nuestra imagen, lo que nos permite aplicar varias veces el filtro a la imagen.

![Aquí, la imagen es $\scriptstyle 3\times3$ y el filtro es $\scriptstyle 2\times2$.](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/image%203.png)

Aquí, la imagen es $\scriptstyle 3\times3$ y el filtro es $\scriptstyle 2\times2$.

En el ultimo ejemplo, la zancadilla de talla $\scriptstyle 1\times1$, la mas simple. Esto quiere decir que movemos el filtro una columna a la derecha hasta llegar al borde derecho de la imagen, y luego nos movemos una fila hacia abajo.

Suponiendo una zancadilla de talla $\scriptstyle 1\times1$, la cantidad de veces que podemos aplicar el filtro de dimensiones $\scriptstyle N\times N$ sobre una imagen $\scriptstyle M \times M$ es:

$$
\#\text{'s de aplicacion del filtro = } (M - N + 1)^2
$$

A veces, también queremos un cierto espacio entre dos posiciones. de un filtro sobre una imagen más grande. Es decir, una zancadilla más grande que $1$.

![La imagen es de talla $\scriptstyle 7\times7$, el filtro de talla $\scriptstyle 3\times3$ y la zancada de talla $\scriptstyle 2\times2$.](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/image%204.png)

La imagen es de talla $\scriptstyle 7\times7$, el filtro de talla $\scriptstyle 3\times3$ y la zancada de talla $\scriptstyle 2\times2$.

Las veces que podemos encajar un filtro sobre la dirección horizontal con una zancadilla horizontal de tamaño $S_\text{horiz}$ sería $\lfloor \frac{W-N}{S_\text{horiz}} \rfloor + 1$, $W$ siendo la dimension horizontal de la imagen. Lo mismo con $H$ como dimensión vertical de la imagen con una zancadilla vertical $S_\text{vert}$. El resultado final sería el producto de ambos, o sea:

$$
\#\text{'s de aplicacion del filtro =}\left( \left \lfloor \frac{W-N}{S_\text{horiz}} \right \rfloor + 1 \right)  \times \left( \left \lfloor \frac{H-N}{S_\text{vert}} \right \rfloor + 1 \right)
$$

### Relleno (padding)

Por último, puede ser el caso que tengamos una parte de un objeto presente en la imagen, pero no el objeto entero. Por ejemplo, fijémonos que esta cruz solamente está parcialmente presente en la imagen real.

![Filtro $\scriptstyle 3\times3$ de una cruz: los píxeles blancos tienen un valor de $1$ y los píxeles negros un valor de $0$.](24b3bfca-0a73-4faf-ad5b-c585453e4781.png)

Filtro $\scriptstyle 3\times3$ de una cruz: los píxeles blancos tienen un valor de $1$ y los píxeles negros un valor de $0$.

![Imagen $\scriptstyle 5\times5$ donde solo hay cruces parciales (falta siempre un píxel de cada cruz).](d6a6b3aa-73f7-4324-a6c2-400277055fde.png)

Imagen $\scriptstyle 5\times5$ donde solo hay cruces parciales (falta siempre un píxel de cada cruz).

Si intentamos pasar el filtro por la imagen, las activaciones no serían las mejores. Por activaciones, quiero decir donde el filtro ubica un píxel negro donde lo hay en la imagen, y lo mismo para los píxeles blancos.

Una forma de reducir esto es agregar un relleno a la imagen de la siguiente forma. El relleno $P$ es de tamaño $1$.

![Imagen original, habiendo aplicado un padding de $1$; aumentando sus dimensiones de $\scriptstyle 5\times5$ a $\scriptstyle 7\times7$.](b3092634-f8fb-4cce-b99a-a35ec9480299.png)

Imagen original, habiendo aplicado un padding de $1$; aumentando sus dimensiones de $\scriptstyle 5\times5$ a $\scriptstyle 7\times7$.

Esto es mejor, ya que si ubicamos el filtro de cruz donde hay cruces parciales, solo nos equivocamos en la activación de un píxel en cada una de las tres cruces parciales, lo que es considerablemente mejor.

La formula para la cantidad de veces que podemos pasar un filtro $\scriptstyle N\times N$ sobre una imagen $\scriptstyle W\times H$, con zancadas $\scriptstyle S_\text{horiz} \times S_\text{vert}$, y relleno $P$ sería:

$$
\#\text{'s de aplicacion del filtro = }

\\[10pt]

\left( \left \lfloor \frac{W - N + 2P}{S_\text{horiz}} \right \rfloor + 1 \right)  \times \left( \left \lfloor \frac{H - N + 2P}{S_\text{vert}} \right \rfloor + 1 \right)
$$

## Dimensiones

### Dimensiones de entrada

Comenzamos con una imagen cuadrada de talla $\scriptstyle N \times N$.

Cada pixel de la imagen puede estar compuesto de una combinación de colores, como por ejemplo RGB (Red, Green, Blue) o CYMK (Cyan, Yellow, Magenta, Key/Black). Esto agrega una tercera dimensión, y la talla de esta tercera dimensión seria la cantidad de colores considerados por píxel en la imagen. Si consideramos CYMK, entonces las dimensiones de nuestra imagen pasan a ser $\scriptstyle 4 \times N \times N$.

En el caso general, el nombre de la dimensión que cuenta los colores considerados por cada píxel recibe el nombre de “canales”, y la representación general de cada imagen es $\scriptstyle C\times N \times N$.

Finalmente, puede ser el caso de que estemos evaluando mas de una imagen. Por ejemplo, puede ser que estemos evaluando un video de un perro, y queremos detectar que raza de perro es con una RNC. Un video, como sabemos bien, es una secuencia de imágenes. Esto implica la introducción de una cuarta dimensión a nuestros datos, es decir $\scriptstyle I\times C\times N \times N$.

Las dimensiones $\scriptstyle I\times C\times N \times N$ representan entonces una secuencia de $I$ imágenes, compuestas cada una de $C$ colores/canales, y de tamaño $\scriptstyle N \times N$.

### Dimensiones de salida

Para cada imagen, le queremos aplicar varios filtros por cada paso convolucional, supongamos  $K$ filtros. Esto quiere decir que el resultado es una matriz con volumen $K$ y con largo y ancho descrito en la expresión anterior.

## Reducción de muestreo (pooling)

Por cuestiones de tiempo, queremos reducir el número de pasos convolucionales que realizamos. Una manera de hacer esto, al mismo tiempo que mantenemos el poder de identificación, es reducir la calidad de nuestra imagen, haciéndola más pequeña pero donde cada píxel conserva información más importante.

Notemos que una ventaja de esto es reducir el overfitting, porque estamos quedándonos con los rasgos importantes.

La manera en como el pooling funciona es, básicamente, tenemos una imagen de tamaño $\scriptstyle N\times N$ y la queremos reducir a $\scriptstyle M\times M$, donde $M < N$. Vamos a tomar una muestra de la imagen, y que también puede involucrar una zancadilla. Esto se aplica de la misma manera como cuando aplicamos un filtro.

El número de veces que podemos aplicar la muestra es nuevamente la fórmula anterior, con $P = 0$. Entonces:

$$
\#\text{'s de aplicacion de muestreo =}\left( \left \lfloor \frac{W-N}{S_\text{horiz}} \right \rfloor + 1 \right)  \times \left( \left \lfloor \frac{H-N}{S_\text{vert}} \right \rfloor + 1 \right)
$$

Luego, a esta muestra le vamos a aplicar una operación y, por último, la vamos a reunir en una imagen final. Esta operación puede ser una de dos:

- **Valor máximo**: tomamos el valor máximo de la matriz muestra y ese será su representante en la imagen reducida.
- **Valor promedio**: mismo principio, pero con el promedio.

En la práctica, la dimension de la matriz muestra suele ser $\scriptstyle 2\times 2$ o $\scriptstyle 3\times 3$, y cada valor máximo o valor promedio es mapeado sobre un solo píxel en la imagen reducida. La zancada suele ser $2$. No queremos hacer más grande la matriz muestra, puesto a que perderíamos rasgos importantes de la imagen.

![image(4).png](image(4).png)

Ejemplos de mapas de rasgos (feature maps) en la primera capa, con distintas imágenes.

![image(5).png](image(5).png)

# 6. Redes neuronales recurrentes

---

## Motivación

- Hasta ahora, hemos vistos dos tipos de RNA: las redes neuronales prealimentadas (feed-forward), y las redes neuronales convolucionales.
- Ambas de estas dos RNA están limitadas por su propia arquitectura. En particular, en dos aspectos:
    - El input debe tener siempre una misma dimensión fija.
    - Los inputs son considerados independientes.
- Una manera de incorporar estos dos aspectos es con una **red neuronal recurrente**.

- La manera más sencilla de incorporar secuencialidad y adaptación de tamaño es con la siguiente fórmula:
    
    $$
    h_t = f(h_{t-1}, x_t)
    $$
    
    - $h_t$ : vector oculto en tiempo t
    - $x_t$ : input en tiempo t
    - $f$ : función o transformación arbitraria. Suele ser definida como un tipo de producto matricial.

- Sin embargo, el mejor modelo para incorporar los dos aspectos importantes suele ser de la siguiente forma:

Recurrencia para el próximo vector oculto:
$h_t​=\tanh(W_{hh}​⋅h_{t−1​}+W_{hx}​⋅x_t​).$

Output en cada tiempo t:
$y_t = W_{hy}⋅h_t$
    - Mismas asignaciones para h, x y tanh.
    - $W_{ij}$ es una matriz de tamaño ixj, que guarda los valores de los parámetros análogos a pesos.
    - Suele también sumarse un umbral B dentro del tanh de la primera fórmula, pero se omite por simplicidad.

## Entrenamiento: retropropagación temporal

$$
\frac{\delta L}{\delta \theta} = \sum_{t=1}^{N} \frac{\delta L_t}{\delta \theta}
$$

- $L$ es la pérdida total
- $L_t$ es la pérdida en tiempo t
- $\theta$ es el conjunto de parámetros.
- N es un tiempo máximo hasta el que estamos dispuestos a llegar para actualizar nuestro conjunto de parámetros.

- **¿Por qué truncamos el tiempo en vez de ir desde el primer t al último t?** Porque sufrimos el problema de gradientes que desaparecen o explotan si llegásemos a tomar cada término desde el inicio del tiempo hasta el final del tiempo.

- Además, para cada $\frac{\delta L_t}{\delta \theta}$, la ecuación es la siguiente regla de cadena:

$$
\sum_{i=1}^t \frac{\delta L_t}{\delta y_t} \frac{\delta y_t}{\delta h_t} \frac{\delta h_t}{\delta h_i} \frac{\delta h_i}{\delta \theta}
$$

- Derivamos finalmente una fórmula para $\frac{\delta h_t}{\delta h_k}$, y aquí vemos de manifesto el problema de los gradientes: es un producto de razones, que eventualmente convergen a 0 o divergen al infinito. En la práctica, esto no le permite crear dependencias de largo plazo.

$$
\frac{\delta h_t}{\delta h_k} = \prod_{i=k+1}^t \frac{\delta h_i}{\delta h_{i-1}}
$$

- Ejemplo: una secuencia de inputs apta para la RNR sería “soy morena, por lo que el color de mi pelo es…”, pues sabría completar con “marrón”.

Pero si le damos “soy morena, **párrafo largo de por medio*,* por lo que el color de mi pelo es…”, la RNR tendrá más problemas para responder con “marrón”.

## Solución: memoria larga de corto plazo (LSTM)

- Una RNR de LSTM está compuesta con los mismos componentes de la RNR estándar, pero también añade otros componentes:
    - Una célula, la cual recuerda valores por cantidades de tiempo arbitrarias, lo que la hace buena para capturar dependencias de largo plazo. **Conserva sus dimensiones a lo largo de la secuencia de inputs**.
    - Una puerta de input, de output y de olvido. Estas controlan el flujo de información desde y hacia la célula. Todas estas puertas son RNAs.
    - **Para tareas basadas en tiempo, son RNRs muy útiles**.

- La operación de una LSTM es la siguiente:
    - Inicializa la célula $c_0 = 0$ y el vector oculto $h_0 = 0$.
    - Cada output $h_t$ es generado de la célula $c_t$.
    - Ahora sí:
        - Para un tiempo determinado t, concatenamos el input en tiempo t, $x_t$; y el output pasado , $h_{t-1}$, en una sola matriz, $[h_{t-1}, x_t]$.
        - Luego, aplicamos la siguiente fórmula: $C_t = f_t \circ c_{t-1} + i_t \circ \overline{C_t}$ . Cada multiplicación es un producto de Hamadard.
        - Por último, el output correspondiente a la célula $C_t$  sería igual a $h_t = o_t \circ \tanh(C_t)$ .
        - Para la siguiente recursión (determinación de $C_{t+1}$ y $h_{t+1}$, utilizamos el C y h del tiempo pasado, t.
        - La puerta de olvido (f), de input (i) y de output (o) tienen todas la misma forma: la forma del output de una neurona dado un input, que sería la matriz horizontal. Particularmente: $z_t = \sigma ( W_z \cdot [h_{t-1}, x_t] + b_z)$. Cambia z por la letra que necesites. Cada peso W y umbral b son diferentes por cada puerta.
        - La puerta de olvido tiene valores de 0 a 1, donde el valor en la posiciones del 0 serán mayormente olvidados y mayormente recordados si están en la posiciones del 1.
        - La puerta de input es casi lo mismo, tan solo es diferente para luego interactuar con $\overline{C_t}$, la cual permite crear nuevas adiciones a la célula.
        - $\overline{C_t}$ es igual = $\tanh ( W_{\overline{C}} \cdot [h_{t-1}, x_t] + b_{\overline{C}})$. A la base, es otra red neuronal.

# 7. Otras arquitecturas

---

## Redes neuronales estocásticas

- Hasta ahora solo hemos estudiado RNAs determinísticas: siempre devolverán el mismo output, dado el mismo input. Las redes neuronales estocásticas son más expresivas que esto.
- Un proceso estocástico es un proceso que no está solamente determinado por las condiciones iniciales o el estado inicial, sino que hay aleatoriedad involucrada.
- Todo el punto de la RNE es capturar relaciones significativas entre los inputs visibles, al igual que una RNA.
    
    ![Untitled](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/Untitled.png)
    

- La red neuronal estocástica es formalmente llamada la *máquina de Boltzmann restringida*.

Se basa en una red neuronal prealimentada, pero su cambio es la decisión de encender una neurona basada en un vector de inputs v. Específicamente, es la siguiente fórmula, donde m es la cantidad de neuronas visibles y h es la neurona oculta en posición j. También, los inputs están coleccionados en la matriz v y los pesos en la matriz W, donde $W_{ij}$ es el peso de la neurona en posición i a la posición j.

**Cabe destacar que todas las neuronas son perceptrones: solo toman valores 0 o 1.**

$$
P(h_j = 1|v) = \sigma(\sum_{i=1}^m W_{ij} \cdot v_i + b_j)
$$

- Se puede calcular la probabilidad en la dirección contraria: la probabilidad de que la neurona input v_i se encienda, dada la matriz de los valores de las neuronas oculta h. a_i es el umbral de la neurona v_i.
    
    $$
    P(v_i = 1|h) = \sigma(\sum_{i=1}^m W_{ij} \cdot h_j + a_i)
    $$
    
- El proceso de entrenamiento de una RNE es diferente.
    1. Utilizamos $v_0$ para construir las probabilidades de que las neuronas ocultas $h_j$ se enciendan. Tomamos una muestra de $h$ a partir de esta distribución de probabilidades lo que sería $h_0$.
    2. Luego, con $h_0$ intentamos reconstruir el vector de inputs original, intento que se llamará $v_1$. Lo reconstruimos al crear una distribución de probabilidad de cada neurona encendiéndose o no, y similarmente tomamos una muestra.
    3. Creamos otro conjunto de estados ocultos $h_1$ con $v_1$. Así sucesivamente. Este proceso se llama el muestreo de Gibbs.
    
    ![Untitled](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/Untitled%201.png)
    

- Para actualizar parámetros (pesos y umbrales), lo hacemos de la siguiente manera: primero estimamos los gradientes (no son exactos debido a la estocasticidad), luego actualizamos cada matriz de parámetros. $\epsilon$ es la tasa de aprendizaje.

$$
\Delta W = v_{(0)}h_{(0)}^T - v_{(1)}h_{(1)}^T
\newline
\Delta a = v_{(0)} - v_{(1)} 
\newline 
\Delta b = h_{(0)} - h_{(1)} 
$$

$$
W \Leftarrow W + \epsilon\Delta W
\newline
a \Leftarrow a + \epsilon\Delta a
\newline
b \Leftarrow b + \epsilon\Delta b
$$

- La intuición del aprendizaje de una RNE es que ajuste sus parámetros tal que determine la probabilidad de observar un vector de inputs v de los datos observados (muestras de ejemplo).
- [https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)

## Redes generadoras antagónicas

- Este modelo es extremadamente eficiente al momento de "rellenar" la información faltante, por lo que podría tener una infinidad de aplicaciones fuera de la video analítica.
- Básicamente, creamos dos redes neuronales: la generadora y la discriminadora, y las ponemos a competir en un juego de suma cero; es decir, la pérdida de una red es la ausencia de pérdida de la otra.
- Para la red generadora:
    1. Vamos a tomar muestras alatorias para cada input de manera normal, lo que termina creando una distribución multinomial gaussiana para cada combinación de inputs.
    2. Luego, creamos un resultado a partir de los inputs.
    3. Intuitivamente, la función de pérdida de esta red es cuán lejos de un resultado realístico es. Sin embargo, necesitamos entrenar una función para saber evaluar cuán realístico el resultado es.
    
- Para la red discriminadora:
    1. Sus inputs van a ser la unidad que estamos estudiando (imágenes, videos, etc.), y su output debe ser la probabilidad de que el input sea del mundo real y no generado.
    Esto implica que D(x) va de 0 a 1, porque es una probabilidad.
    2. La función de pérdida será entonces definida como $-\log (D(x))$.
    Notemos, para probabilidades de que el input sea real, D(x) estará cerca de 1, por lo que la pérdida estará cerca de 0.
    
- Con esto hecho, la función de pérdida de la red generadora será $\log(1-D(G(z))$. z es el input de la red generadora, que es tomado aleatoriamente input por input. (De hecho me salió mejor con log(D(G(z))).

### Pequeña mejora: InfoGAN

- InfoGAN es una variación de la RGA estándar.
    1. Crea una variable c que captura la “información importante de la estructura” del input.
    2. Redefinimos la generación como G(z, c), donde ahora la generación tendrá más en cuenta la estructura esencial del objeto de estudio.
    3. Finalmente, para mejor entrenar la generación, crea una función I(Input, c), la cual devuelve valores más grandes según la cantidad de información de c presente en el input. La nueva función de pérdida sería $\log(1-D(G(z)) - I(G(z,c), c)$.

## Auto-encodador variacional

- Un autoencodador es una función que toma un vector en dimensiones n y lo mapea a un vector en dimensiones m, donde m < n. Básicamente, la encodación reduce la dimensión del vector. 

No solo esto, sino que lo hace intentando mantener la mayor información posible del vector original, **para finalmente reconstruir el vector original de dim. n, que es el proceso de decodación.**

- El recorrido de la función autoencodación es el espacio latente, el espacio donde se puede mapear los vectores de mayor dimensión. Hay que tener en cuenta que no todo el espacio latente tiene una asignación de la encodación (la encodación no es superyectiva).

- Queremos hacer este proceso de decodación una función generadora. Es decir, queremos tener un universo de donde tomemos muestras que nos permitan generar un vector de dimensiones originales “realístico”.

Para ello, necesitamos restrigir nuestro espacio de muestreo a solamente las regiones de las m dimensiones donde se mapean los vectores de n dimensiones originales.

- Esta última tarea — encontrar la región donde se mapean los vectores originales — requiere saber la distribución real de los datos.

- Un auto-encodador variacional hace entonces lo siguiente:
    1. No mapea un valor real a un valor específico en el espacio latente, sino que mapea V a una distribución de vectores que, al ser reconstruidos, su resultado está cerca del vector original.
    
    Esta distribución de vectores dim. m es definida como multinomial gaussiana, con media $\mu$ y varianza $\sigma^2$. La encodación es entonces una función que devuelve $\mu$ y $\sigma^2$.  Inicializamos $\mu$ y $\sigma^2$, en el entrenamiento los afinaremos.
    
    2. Luego, para crear finalmente una encodación del vector V, tomamos una muestra de una multivariable normal estándar, la multiplicamos por $\sigma$ y le sumamos  $\mu$. Todo esto lo hacemos para tomar una muestra de la multinomial restante, lo que será finalmente la encodación W de nuestro vector original V. La distribución de la encodación W, dado el input V, es notada $q_W(V)$.
    
    3. Ahora, la decodadora va a tomar la encodación W para intentar reconstruir el vector original V.
        
        ![Untitled](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/Untitled%202.png)
        
    4. Luego, introducimos un término de **pérdida de latencia**, que indica cuánto de la distribución encontrada en la encodación, $(\mu, \sigma^2)$, diverge de la distribución multinomial gaussiana estándar $(0, 1)$. Esto se mide de la siguiente manera, donde la mano izquierda se conoce como la divergencia de Kullback-Leibler.
        
        $$
        D_{KL}(q_W(V)|| \space p_W)=
        \int_{- \infin}^\infin q_W(V)\log(\frac{q_W(V)}{p_W}) \space dx \newline
        $$
        
    5. Finalmente, buscamos $\mu$ y $\sigma^2$ que minimicen la función de pérdida. De esta manera, nos acercaremos más y más en cada retropropagación a la verdadera distribución de la encodación, $p_W$.
    

## Word2Vec

- Imaginemos que queremos crear una red neuronal que trate las palabras de un idioma. No es necesario comentar la enormísima cantidad de palabras que hay, lo mismo si decidimos representar cada palabra con un vector “one-hot”, es decir, con una entrada igual a 1 y el resto 0.

Por ello, querríamos aplicar una redución dimensión, como en el auto-encodador.
- Nos gustaría capturar la relación entre ciertas palabras con vectores, como por ejemplo:  $bueno = -malo$, o también $l_{reina} - l_{mujer} = l_{monarca}$, donde $l$ es la representación vectorial de una palabra.
- La primera capa sería la transformación de la palabra, la cuál sería una matriz de dimensiones MxN, donde M es la cantidad de palabras en el idioma, y N la dimensión del espacio donde nos gustaría mapear nuestras palabras. La encodación de la palabra de índice i estaría en la fila i de la matriz M.
- La segunda capa sería la predicción del contexto de las palabras. Definimos el contexto, en este caso, como el conjunto de las palabras alrededor de una palabra. Por ejemplo, el contexto de la palabra sandwich, una palabra hacia atrás y dos hacia adelante, en la frase “*le gustaba cenar un exquisito sándwich de jamón con zumo de piña y vodka fría*” sería {exquisito, de, jamón}.

Existen dos tipos de modelos de RNAs para incluir el contexto:

1. B**olsa continua de palabras (CBOW)**: es una red neuronal que tiene como output si una palabra pertecene a un contexto o no (clasificación). Su input es una cierta palabra (vector one-hot) y el promedio de los vectores que representan el contexto.

2. **Skip-gram**: su input es una palabra (vector one-hot) y su output es el vector con nuestro vocabulario, teniendo una probabilidad en cada entrada de palabra. Esta probabilidad es aquella de que tal palabra x esté cerca de nuestra palabra input en un texto.

- **Muestreo negativo**: supongamos que hablamos del modelo CBOW. Para entrenar una red neuronal, le mostramos ejemplos de clasificación correcta. El muestro positivo es enseñarle ejemplos de clasificaciones correctas, donde tales ejemplos son ya comprobados por humanos.

El muestro negativo es simplemente ejemplos de clasificaciones incorrectas, pero no necesitamos una comprobación humana, nada más es suficiente que tomar un contexto y una palabra aleatoria de nuestro vocabulario, la cual casi seguramente no tendrá sentido en el contexto, y la clasificamos como incorrecta.

Fijando un vector contexto (el promedio de los vectores de las palabras del contexto), supongamos que estamos en la fase de entrenamiento de clasificación, con un cierto dataset que vamos a alimentar a la red. Por cada ejemplo de clasificación correcta de nuestro dataset, queremos una cierta cantidad de clasificación incorrecta, ¡pero no para todas las palabras incorrectas en el contexto! Esto va a ayudar a mejorar nuestros tiempos de entrenamiento.

Si nuestro sub-dataset de ejemplos correctos es pequeño, queremos de 5 a 20 ejemplos de clasificación incorrecta por cada ejemplo de clasificación correcta. Si nuestra cantidad de ejemplos correctos es grande, con 2 a 5 ejemplos incorrectos por cada ejemplo correcto es suficiente. Esto es pare

## Aprendizaje reforzado

- El aprendizaje reforzado es un proceso de decisión de Markov que, a su vez, es una modificación de una cadena de Markov.
- **Cadena de Markov**: es un modelo estocástico donde la probabilidad de alcanzar un estado en un evento futuro t+1 depende solamente del estado donde se estaba en el evento pasado t (esta es su característica más importante: pérdida de memoria). 

Formalmente, es una 2-tupla, cuyos componentes son:
    - Un conjunto de estados: $S = \{s_1, s_2, … , s_n\}$.
    - Un conjunto de probabilidades de transición de estado i a estado j,
     $T = \{P_{0,0}, P_{0,1}, …, P_{i,j}\}$.
        
        ![Untitled](informa%CC%81tica%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/Untitled%203.png)
        

- **Proceso de decisión de Markov**: es una modificación de la cadena de Markov. 
Formalmente, es una 4-tupla, cuyos componentes son:
    - Un conjunto de estados, llamado “espacio de estados” y denotado $S$.
    - Un conjunto de acciones, llamado “espacio de acciones” y denotado $A$.
    - Un conjunto de probabilidades de transición de un estado a otro al haber tomado una cierta acción, denotado $T$.
    - Una función de recompensa por haber tomado una acción en cierto estado,
    $R:S \times A \rightarrow \R$
    - No necesariamente, pero aquí podemos incluir una función “política” que mapea un estado a una acción. Esto será útil para hablar del aprendizaje por refuerzo, pues aquí vemos las estrategias.
    
    Esta política puede ser determinística o probabilística. Si es determinística:
     $\pi: S \rightarrow A$
    
    De lo contrario, si es probabilística: notemos que podemos hacerla determinística con probabilidades absolutas de 0 y 1.
    $\pi:S \times A \rightarrow [0,1]$
    
    ![Untitled](informa%CC%81tica%202%20redes%20neuronales%20artificiales%200423ddd123fc4fac99c7432906f372dc/Untitled%204.png)
    
    - Finalmente, el **aprendizaje reforzado** es un procedo de decisión de Markov donde buscamos que el agente maximice el valor esperado de su recompensa ajustando su función de política.
    
    Notemos que esta función de recompensa se va acumulado con el tiempo. Queremos que el agente maximice su valor de recompensa al largo plazo y no en el corto plazo. Por lo tanto, el agente puede tomar decisiones de recompensa sub-óptima en el presente si el considera que puede alcanzar la recompensa óptima en el largo plazo.
    
    Al haber inicializado las probabilidades de acciones, se hacen muchas simulaciones, para que la red pueda explorar todas las combinaciones de recompensas disponibles. Finalmente, aplicamos ascenso por gradiente para maximizar la recompensa final de los juegos simulados.
    
    El agente también aprende la noción de “arrepentimiento” cuando observa la diferencia de su recompensa con la recompensa de un hipotético agente óptimo.
    
    Todo esto implica que el aprendizaje reforzado es un proceso bien apto para problemas donde hay disputas de largo plazo vs. corto plazo.
    - AlphaGo es una red neuronal que aplica aprendizaje por refuerzo. Notemos que para las redes neuronales, remplazamos la función de pérdida con la función de recompensa y procedemos a hacer ascenso por gradiente, en vez de descenso. Las diferencias con AlphaGo son:
        - Se entrena un modelo experto (no necesariamente una red neuronal) y buscamos que nuestra red original imite al experto a través de modificar nuestras probabilidades. Llegamos a un cierto conjunto de probabilidades que son aquellas del modelo experto.
        - Durante la simulación, la red juega contra una iteración previa de si misma, para evitar overfitting y quedarse estancados en locales máximos de la función de recompensa y posiblemente llegar al máximo global.
        - Se entrena un modelo de “valor” Este modelo toma como input un estado y devuelve el valor esperado desde ese estado en el futuro y siguiendo esa misma política. Formalmente,
        
        $$
        V^{\pi}(s)=E[R\space|\space s,\pi]
        $$
        
        - Finalmente, cuando AlphaGo debe tomar una decisión, realiza un árbol de búsqueda de Monte Carlo con una gran cantidad de simulaciones. Es una red con nodos y conexiones. Cada nodo representa un estado y contiene una valuación, mientras que cada conexión es la probabilidad de transición de ese estado a otro, y contiene una valuación inicializada a 0.
        
        En cada simulación, se empieza del nodo raíz y se sigue le conexión con el valor más alto de (probabilidad + valor de la acción), con una penalización por cada número de veces que se ha pasado por la conexión en simulaciones pasadas (con el objetivo de incentivar la exploración del árbol). Trazamos conexiones hasta llegar al final del juego.
        
        Se actualizan la valuación de las acciones con el promedio de las valuaciones de los nodos que estaban debajo de esa conexión en esa simulación. Volvemos a hacer otra simulación. Así sucesivamente, con la serie de simulaciones fijada a un límite de tiempo.
        
        La decisión final que toma AlphaGo es la acción que le conecta al nodo que fue más visitado durante la serie de simulaciones.