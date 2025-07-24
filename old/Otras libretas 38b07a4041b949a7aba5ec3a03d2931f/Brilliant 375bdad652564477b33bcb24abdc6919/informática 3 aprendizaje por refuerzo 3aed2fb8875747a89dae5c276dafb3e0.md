# informática 3 // aprendizaje por refuerzo

Date de création: June 23, 2022 11:58 PM
Modifié: March 10, 2024 1:29 AM

<aside>
💡 Tabla de contenidos

</aside>

# 1. Introducción

---

Los rasgos del AR son un **agente** que toma **decisiones** e **interactúa** con un **ambiente** (donde se presentan los estados y las recompensas). El agente busca lograr un **objetivo explícito** a pesar de la **incertidumbre** de los efectos de sus acciones sobre el ambiente.

Una decisión tomada por el agente puede verse como una función que corresponde un estado del ambiente a una acción. Esta función es llamada la política y se denota $\pi$. Puede ser determinística o estocástica. En esencia, la política es un sistema de decisiones.

- **Política determinística**: $\pi: S \rightarrow A$
- **Política estocástica**: $\pi:S \times A \rightarrow [0,1]$
- Notemos que una política determinística es una política estocástica donde la acción tomada tiene probabilidad 1 y el resto de acciones tiene probabilidad 0.

Luego, existe la función de **señal de recompensa $R_t$**, la cual le da puntos por cada estado alcanzado en tiempo t, negativos o positivos. Esta señal de recompensa busca guiar al agente a su objetivo explícito. El fin del AR es encontrar la política que maximice la esperanza de la recompensa acumulada al pasar por todos los estados futuros.

La transición entre estados sigue la **propiedad de Markov (pérdida de memoria)**: toda la información que determina el próximo estado está capturada únicamente en el estado y acción presente. Esta propiedad es conveniente para demostrar la convergencia de ciertos algoritmos para encontrar la política óptima.

# 2. Bases

---

- **Función retorno**: es la función de las recompensas futuras a partir de un tiempo t hasta un tiempo máximo T. $\gamma$ es una tasa de descuento. Si $\gamma < 1$, las recompensas del futuro lejano valen menos que las recompensas de futuro próximo. Es lo contrario si $\gamma > 1$.
La última línea es una identidad recursiva útil.

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3}... = \sum_{i=t}^T \gamma^{i-1} R_i

\newline

G_t = R_{t+1} + \gamma G_{t+1}
$$

- **Función valor-estado**: es el valor esperado cuando el agente sigue la política $\pi$ desde estado $s$. También tiene una identidad recursiva útil, particularmente cuando la usamos para ir del último estado hacia atrás, hasta llegar a los estados más lejanos.

$$
v_\pi(s) = \mathbb{E}_\pi[G_t | S=s_i]

\newline
\newline

v_\pi(s) = \mathbb{E}[R_{t+1} + \gamma v_\pi(S_{t+1}) | S= s_i]
$$

- En la práctica, los valores-estado están atados a grandes sistemas de ecuaciones, por lo que es difícil conseguir el valor de un solo estado aislado. Normalmente entonces, usamos una estimación del valor-estado.
- **Función valor-acción o función Q**: es el valor esperado de tomar una acción $a$, luego llegar al estado $s$ y seguir la política $\pi$ desde ahí. Es muy parecida a la función valor-estado. La segunda línea es una representación más simple usando la función valor-estado.

$$
q_\pi(s,a) = \mathbb{E}[G_t|S=s, A=a]

\newline

q_\pi(s,a) = R(s,a) + v_\pi(s')
$$

- En la práctica, usamos la función valor-estado para evaluar la calidad de la política, mientras que utilizamos la función valor-acción para mejorar la política.

## Teorema de mejora de política

> Antes de explicar el teorema, tenemos que explicar un poco la notación.

Particularmente, notemos que $v_\pi(s) = q_\pi(s,\pi(s))$. Es decir, “el valor esperado de seguir $\pi$ empezando desde $s$, es lo mismo que el valor esperado de empezar desde $s$, tomar la acción a que nos dicta la política $\pi$ en el estado $s$, y luego continuar la política $\pi$”.

La escritura de la izquierda es más simple que la de la derecha, por lo que queremos usarla cuando podamos. 

Entonces, realmente queremos usar $q_\pi$ cuando estamos en un estado y vamos a tomar una decisión diferente de la decisión que nos dicta la política para ese estado $s$, luego continuamos con la política. Un ejemplo sería $q_\pi(s, \pi'(s))$ para una política $\pi’$ con una acción diferente en ese estado.
> 

Si existe una acción alternativa $a’$ tal que $q_\pi(s_i, a’) ≥ v_\pi(s)$, entonces podemos crear una política alternativa $\pi$’ tal que realice $a’$ en estado $s_i$ y $\pi(s)$ para el resto de estados $s’$.

Por ende, $v_{\pi’}(s) ≥ v_\pi$, por lo tanto, $\pi’$ es una mejora sobre $\pi$.

## Métodos de Monte Carlo

Son algoritmos para estimar cantidades numéricas a partir de una muestreos aleatorios. Es un modelo de algoritmo, no un determinado algoritmo en particular. Normalmente, el algoritmo sigue el siguiente patrón:

1. Define un dominio de donde tomar valores aleatorios.
2. Toma la muestra aleatoria.
3. Pasa los valores aleatorios por una computación determinística (una función, por ejemplo)
4. Agrega los resultados.

Se aplica al AR porque no es necesario conocer las probabilidades de transición para poder estimar la mejor política, sea estimando la función **valor-estado** o **acción-estado**. Particularmente, el método de Monte Carlo aplicado para estimar el valor de un estado bajo una cierta política es el siguiente:

1. Fijamos un estado de inicio $s$ y una política $\pi$ determinística o estocástica.
2. Tomamos varias simulaciones siguiendo nuestra política, sin necesidad de saber las probabilidades de transición. 
3. Tomamos las recompensas acumulativas $R$ al llegar a un estado terminal.
4. Finalmente, después de todas las simulaciones, tomamos un promedio de las recompensas acumuladas de cada simulación. Ese será la estimación de $v_\pi(s)$.

Sin embargo, hay un problema. Puede que volvamos a regresar al estado s después de haber comenzado la simulación. Por ello, existen dos tipos de MC: primera visita y varias visitas:

- **MC de primera visita**: solo cuenta la recompensa acumulada desde la primera vez que se visita el estado de partida.
- **MC de varias visitas**: se toma la recompensa acumulada a contar por cada vez que se visitó un estado, y finalmente se hace un promedio de ellas.
- MC de primera visita es un estimador no-sesgado. Si el # de simulaciones es pequeño, el error cuadrado medio de MCVV será más pequeño. Si el # de simulaciones es grande, el ECM de MCPV será más pequeño. Ambas convergen al mismo valor cuando el # de simulaciones tiende al infinito.

Otro caso a considerar es cuando no tenemos un modelo de transición (no sabemos las conexiones entre estados). En ese caso, conviene más calcular la función Q de acción-estado. La estimación de $q_\pi(s, a)$ se denota $Q(s,a)$.

- **Control de MC**: método para encontrar la política óptima, alternando el paso de evaluación y el paso de mejora.
    - **Paso de evaluación (E)**: los valores de acción Q son evaluados para la política actual.
    Puedes hacer un montón de simulaciones y luego promediar sus Q empíricos.
    Alternativamente, puedes actualizar Q con cada nueva simulación. La fórmula sería esencialmente la primera, aunque la segunda es la que se utiliza en la práctica y se llama **Q-learning**. (Aquí $G_t$ cuenta también la recompensa actual t con las futuras).
    
    $$
    Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[G_t - Q(s_t,a_t)]
    $$
    
    $$
    Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[r_t + \gamma \max_a Q(s_{t+1}, a) - Q(s_t,a_t)]
    $$
    
    - **Paso de mejora ($I$)**: se actualiza la política actual con la mejor acción encontrada tal que aumenta $Q(S_t, A_t)$.
    
    $$
    \pi(S_t) = \argmax_{A_t} Q(S_t, A_t)
    $$
    
    - Finalmente, el control de MC toma la siguiente forma:
        
        $$
        \pi_0 \xrightarrow{E}
        q_{\pi_0} \xrightarrow{I}
        \pi_1 \xrightarrow{E}
        q_{\pi_1} \xrightarrow{I}
        \pi_2 \xrightarrow{E}
        q_{\pi_2} \xrightarrow{I}
        ... \space
        \pi^* \xrightarrow{E}
        q_{\pi}^*
        $$
        

## Codicia épsilon ($\epsilon$-greedy)

Con este **control de MC** explicado, decimos que el algoritmo se vuelve “codicioso” con respecto a una acción en estado $s$ cuando la implementa determinísticamente en su política. El problema con esto es que puede ser que no se estime bien todas las posibles combinaciones de $Q(s,a)$ porque la política siempre va a preferir una cierta acción sobre las otras. Esto se evita con el algoritmo codicia épsilon. Existen dos maneras: 

- **Aleatoriedad incluida la política (on-policy)**: cada vez que se va a tomar una acción, la mitad de las veces se sigue la política y la otra mitad se decide tomar una acción al azar (incluso incluida la opción determinística preferida por la política).
- **Aleatoriedad** **fuera de la política (off-policy)**: se entrenan dos políticas, llamadas **políticas de comportamiento** $b$ ****y **de objetivo $\pi'$**. La de comportamiento es épsilon-codiciosa, mientras que la de objetivo evalúa y mejora la política original $\pi$.

Con este último diseño, la política de comportamiento explora acciones diferentes de la óptima hasta al momento. Así, la política objetivo aprende de las malas decisiones mientras que guarda en memoria las buenas decisiones. Finalmente, esto resuelve bien el dilema de exploración y explotación. 

# 3. Extensiones

---

## Diferencia temporal

Los métodos de Monte Carlo utilizados aquí presentan problemas. Particularmente:

1. Las simulaciones o “episodios” necesitan ser “completos” para poder calcular los retornos y actualizar los retornos, especialmente en los episodios que toman mucho tiempo en terminar o simplemente no terminan.
2. Debido a que la estimación de Q es un promedio de variables aleatorias, su varianza es grande, y debemos hacer muchas simulaciones de MC para finalmente converger.

Sin embargo, podemos calcular los retornos sin necesidad de completar una simulación. Un método que actualiza Q con cada paso de tiempo es denotado de “diferencia temporal” o DT.

Recordemos la fórmula modelo de actualización de Q:
No olvidemos que, en este modelo, $G_t$ añade la recompensa del tiempo actual t con las recompensas de tiempos futuros t+1, t+2… etc.

$$
Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[G_t - Q(s_t,a_t)]
$$

En esta fórmula, $G_t$ es una función objetivo. Es decir, la dirección del cambio va a depender de $G_t$, mientras que el tamaño del cambio será regulado por $\alpha$.

Con eso explicado, este modelo debe esperar a terminan el episodio. La fórmula de DT más simple es la siguiente.

$$
Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[(R_t + V(S_{t+1})) - Q(s_t,a_t)]
$$

Notemos que la función objetivo cambió de $G_t$ a $(R_t + V(S_{t+1})$. No necesitamos llegar al t final para esta actualización, puesto a que vamos a tomar una estimación (valor esperado) de los retornos a partir del estado $S_{t+1}.$

Hay dos métodos de diferencia temporal principales: necesitamos los pares estado-acción de dos tiempos subsecuentes, t y t+1.

- **Sarsa**: el nombre viene de que necesita 5 elementos, que son $\{s_t, a_t, r_t, s_{t+1}, a_{t+1}\}$.

$$
Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[R_t + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t,a_t)]
$$

- **Q-learning (Sarsa max)**: parecido a Sarsa, pero utiliza el máximo posible de $Q(s_{t+1}, a)$.
    
    $$
    Q^{nuevo}(s_t,a_t) = Q(s_t,a_t) + \alpha[r_t + \gamma \max_{A^*} Q(s_{t+1}, A^*) - Q(s_t,a_t)]
    $$
    
- La distinción entre ambos algoritmos es que Sarsa es $\epsilon$-greedy sobre la política mientras que Q-learning es fuera de la política. Es decir, Sarsa utiliza una política $\epsilon$-greedy para $a_t$ y $a_{t+1}$, mientras que Q-learning utiliza una política $\epsilon$-greedy de comportamiento b para $a_t$ y una política greedy $\pi$ para $A^*$. Si fijamos $\epsilon = 0$, Sarsa y Q-learning son lo mismo.
- **Al aplicar estos métodos, se debe pasar o *loopear* por todos los estados**

Nota: la diferencia entre la **función objetivo** y **el valor actual de Q** dentro de los corchetes es llamado el error de diferecia temporal o TD-Error.

### Sesgo de maximización y Q-learning doble

Un problema notable con DT, especialmente Q-learning es el sesgo de maximización. Es complicado de explicar, por lo que usaremos un ejemplo.

![Untitled](old/Otras%20libretas%2038b07a4041b949a7aba5ec3a03d2931f/Brilliant%20375bdad652564477b33bcb24abdc6919/informática%203%20aprendizaje%20por%20refuerzo%203aed2fb8875747a89dae5c276dafb3e0/Untitled.png)

Notemos que $Q(A, \rightarrow) =0$ y $Q(A, \leftarrow) = -0.1$.

Sin embargo, supongamos que por la varianza de las recompensas, nuestras primeras estimaciones de $Q(B, \leftarrow)$ nos llevaron a pensar que el valor esperado de ir a B era mejor que de ir a la derecha.

Ahora, dependemos de que la suerte se nos corrija y tengamos malos resultados del sampleo de las recompensas para corregir y bajar $Q(B, \leftarrow)$ para finalmente llegar al óptimo teórico $Q(A, \rightarrow)$. Y, sin embargo, hay situaciones donde no hay suerte en las recompensas y podemos quedarnos atrapados permanentemente en la decisión sub-óptima.

La solución a este problemas son distintos tipos de **Q-learning doble**. Usaremos el Q-learning original, en donde se crean dos funciones Q, Cuando actualicemos $Q_1$, utilizaremos el $\max Q$  indicado por $Q_2$, y viceversa (invirtiendo los índices en la expresión de abajo). Escogemos quién será la función actualizada y la función maximizadora al azar, con 50% de probabilidad.

$$
Q_1^{nuevo}(s_t,a_t)= Q_1(s_t,a_t) + \alpha[r_t + \max_a Q_2(s_{t+1},a_{t+1}) - Q_1(s_t,a_t)]
$$

Esta solución ayuda porque es muy difícil que ambas Q sobre-estimen la misma acción simultáneamente. E incluso si es el caso, es más fácil que ambas se desatoren.

## Método de gradiente de políticas

Con todo, los métodos de DT tienen dos problemas: requieren un espacio de acciones discreto y no aprendren las probabilidades de elección que serían las óptimos en una política $\epsilon$-greedy.

Además, los métodos de DT son **métodos basados en el valor**, los cuales mantienen una estimación de Q para la política óptima. Sin embargo, los **métodos basadas en políticas** aprenden directamente sin una estimación de valor.

> **Recordatorio**: el gradiente es la matriz columna tal que, desde un cierto punto input $p$, nos indica el vector output tal que muestra el mayor aumento de la función.
> 
> 
> $$
> \nabla_\theta J(\theta) =
> \begin{bmatrix}
> \frac{\partial J}{\partial w_1}(p) \\
> \frac{\partial J}{\partial w_2}(p) \\
> \vdots \\
> \frac{\partial J}{\partial w_n}(p) \\
> \end{bmatrix},
> \space
> \theta =
> \begin{bmatrix}
> w_1 \\
> w_2 \\
> \vdots \\
> w_n
> \end{bmatrix}
> $$
> 
> La dirección del gradiente indica la dirección de mayor crecimiento de la función $J(\theta)$, a partir de $p$, mientras que la magnitud del vector es la razón de cambio, que es la mayor derivada direccional absoluta.
> 

Sea $\theta$  un vector de parámetros, entonces el método del gradiente sería:

$$
\theta \leftarrow \theta + \alpha  \nabla _\theta J(\theta)
$$

Este proceso hace para entrada en $\theta$ moverse en una dirección tal que aumente el valor esperado $J(\theta) = v_{\pi_\theta}(s_0)$. Realmente, porque fijamos $s_0$, $v$ termina siendo más bien una función de $\theta$: $v_{s_0}(\pi_\theta)$.

Para entrenar esto, a cada peso debemos pasarle todos los episodios de nuestro dataset, ver el promedio de los cambios que cada ejemplo del dataset sugiere, y hacer ese mismo proceso con todos los pesos.
Sin embargo, poder generar todos los episodios a partir de un cierto estado, y luego hacer lo mismo para todos los estados, es casi imposible y costoso. Al igual que las RNA, hacemos **ascenso por gradiente estocástico**: solo tomamos una muestra de los episodios, actualizamos los parámetros con ascenso por gradiente, y repetimos con una muestra distinta de episodios.