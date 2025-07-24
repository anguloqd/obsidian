# stat. y proba. 5 // matemática para finanza cuantitativa

Date de création: August 16, 2021 6:58 PM
Modifié: January 16, 2023 1:07 AM

# Varianza, covarianza, correlación

- Si X e Y son dos VA:
    - Si te fijas, si ambas variables no tienen correlación linear (es decir, p = 0), entonces queda como si fuesen eventos independientes, Var(X + Y) = Var(X) + Var(Y).
- Diferencia entre **independencia** y **no-correlación**:
    - **Independencia**: la ocurrencia de un evento no afecta la ocurrencia de otro evento. (Recuerda: pelotas de Venn separadas sin intersección)
        
        Particularmente, Dos VAs, X e Y, son independientes si la distribución de probabilidad conjunta P(X, Y) se puede escribir como el producto de las dos distribuciones individuales.
        
        Es decir, P(X, Y / X∩Y) = P(X)*P(Y).
        
    - **No-correlación**: cuando una variable no tiene poder explicativo **linear** sobre otra variable. (Quizás una variable sí puede ayudar a predecir otra, pero no de manera linear)
        
        Particularmente, cuando Cov(X, Y) = 0.
        
    - **Independencia implica no-correlación, pero no-correlación no implica independencia**.
- La correlación es la forma normalizada de la covarianza.

Considere la siguiente quiniela.

Lanza una moneda justa para determinar el importe de tu apuesta: si sale cara, apuestas 1, si sale sello, apuestas 2. A continuación, vuelve a tirar: si sale cara, ganas el importe de tu apuesta, si sale cruz, lo pierdes. (Por ejemplo, si sale cara y luego cruz, pierdes 1, y si sale sello y luego sello, pierdes 2). Sea X es la cantidad que has apostado, y deja que Y sea su ganancia neta (negativa si has perdido).

X y Y tienen correlación cero. Esto se puede calcular explícitamente, pero es básicamente el hecho de que se está jugando un juego justo sin importar cuánto se apueste. Pero no son independientes; de hecho, si sabes Y Entonces ya sabes X (si Y=−2 por ejemplo, entonces X tiene que ser 2). Explícitamente, la probabilidad de que Y=−2 es 1/4 y la probabilidad de que X=2 es 1/2 pero la probabilidad de que ambos ocurran es 1/4 no 1/8. De hecho, en este juego, no hay ningún evento con probabilidad 1/8.

# VAs y Distribuciones

- Cuando sumas VAs, las medias y varianzas son aditivas, al menos en el caso de la Distribución Normal.
    - Puedes sumar dos distribuciones normales para formar una nueva. Supongamos N(m1, v1) - N(m2, v2) = N(m1 **** m2, v1 **+** v2).
    - Importante cuando quieres calcular la distribución normal de un portafolio.

# Estimación de parámetros

- **EMV (Estimación de máxima verosimilitud)**: método de estimación de parámetros de una distribución. Esta maximiza la posibilidad de observar los datos observados.
    
    [](https://wikimedia.org/api/rest_v1/media/math/render/svg/1121f3a9973642f0400c804404b494fb25825944)
    
- **EAP (Estimación a posteriori)**: método para calcular la probabilidad a posteriori utilizando la probabilidad a priori y la EMV. Es un método más riguroso que la EMV.
    
    [](https://wikimedia.org/api/rest_v1/media/math/render/svg/c4ec23389625499b89966517dfb0d20f052dd78a)
    
    [](https://wikimedia.org/api/rest_v1/media/math/render/svg/b5fa5c75aaba1c4d37900f681b37dee739008677)
    
- Aquí, el denominador puede ser ignorado, pues no depende de la variable theta.
- Phi es el dominio de g y ésta es la distribución a priori de theta.
- El denominador termina siendo una especie de P(Evidencia).
- Todo junto, EMV/Denominador termina siendo un poco el soporte que x da a theta.
- El denominador es como la prob. de x.
- La EMV tiene problemas de parcialidad. Considera usar Minimum-variance unbiased estimator (MVUE).

## Álgebra linear

- **Matriz**: es una colección de números en una lista de dimensiones a x b, donde a y b son números positivos.
- **Vector**: segmento de una recta, es un elemento de un espacio vectorial que cumple con 3 propiedades.
    - **Módulo**: su longitud.
    - **Dirección**: la recta que lo contiene.
    - **Sentido**: hacia cuál de los dos extremos de la recta se dirige. Solo dos opciones son posibles.
- Los vectores casi, casi siempre van a tener su núcleo en el origen.
- Los vectores 2D pueden representarse con una matriz 2 x 1, es decir, dos filas y una columna. La primera entrada es la coordenada x, la segunda entrada es la coordenada y.
- Cada tópico en álgebra linear se centra en dos operaciones simples: suma de matrices y multiplicación por un escalar.
    - **Suma de matrices**:
        - Selecciona dos vectores.
        - Toma uno de ellos y fija su cola en el origen.
        - Luego toma el segundo de ellos y fija su cola en la punta del primer vector.
        - El resultado final es un vector desde el origen hasta la punta del segundo vector.
    - **Multiplicación por un escalar**:
        - Es simplemente estirar, encoger y ocasionalmente invertir el sentido de un vector, todo depende de la constante por la que se multiplique el vector.
- Los números que representan las abscisas y las ordenadas pueden ser vistos como escalares de los vectores base.
    - En el caso del plano cartesiano, los vectores base con **i-sombrero** (1, 0) y **j-sombrero** (0, 1).
    - Los vectores base pueden ser distintos de aquellos del plano cartesiano.
    - La gran mayoría de pares de vectores base pueden alcanzar cualquier punto en su plano, excepto en dos casos.
        - Si un vector base puede ser expresado como el otro vector base escalado, por lo cual pueden alcanzar los puntos de una línea. Esto se llama "**dependencia linear**".
        - Si ambos vectores son (0.0), por lo que se quedan atascados en ese punto.
- Una **combinación linear** es un vector que resulta de la suma de los vectores base, escalados o no por cualquier número real.
    - Particularmente: av + bw, donde v y w son vectores y a y b son escalares que recorren los reales.
    - El sistema generador de dos vectores, v y w, es el conjunto de TODOS los vectores que puedes generar aplicando las operaciones de suma y escalar a v y w.
- **Transformación linear**: es una función que toma un vector como input y suelta un vector como output.
    - Se le llama "*transformación*" porque se asocia con el movimiento: el vector de entrada se mueve a la ubicación del vector de salida.
    - **Debe cumplir dos condiciones**:
        - Todas las líneas que sean posibles trazar permanecen siendo líneas (las líneas guías son paralelas y con la misma distancia entre ellas).
        - El origen debe mantenerse en (0,0).
    - La transformación lineal tiene la **propiedad de linearidad**.
    - El proceso de mover el vector de entrada al de salida se da multiplicando el vector dado por los vectores base de la transformación.
        - La información de los vectores base de la transformación, que son 2 vectores en 2D, suele estar codificada en una matriz 2x2. La primera columna es i-sombrero y la segunda es j-sombrero.
        - Para tomar un vector del plano cartesiano y aplicarle una transformación hacia un nuevo plano con nuevos vectores base, multiplicas el vector DE DERECHA A IZQUIERDA con los vectores base.
- **Multiplicación de matrices**: es una operación que puede ser usada con un vector * dos vectores base, o con el producto de dos matrices de dos vectores base.
    - La matriz resultante, llamada matriz producto o la composición, tiene el número de filas de la primera matriz y el número de columnas de la segunda matriz.
    - Para que esta operación sea posible, hay un requisito, lo contrario de lo anterior: la primera matriz debe tener el mismo número de columnas que el número de filas de la segunda matriz.
    - **Propiedades** de la multiplicación de matrices:
        - **No-conmutativa**
        - Asociativa
        - Distributiva
        - Producto por un escalar
        - Distribución de la transposición
    - Cada entrada de la matriz es el producto punto de cierta fila con cierta columna.
- **Determinante de una matriz**: es el factor por el cual se escala el área del cuadrilátero dado por i-sombrero * j-sombrero.
    - La fórmula es det(M) = ad - bc, para una matriz ([a, c], [b, d]).
    - det(M1M2) = det(M1) * det(M2)
    - Si el determinante es 0, significa que todo el espacio fue reducido en una línea o incluso en un punto.
        - Esto implica que también que los vectores son linearmente dependientes.
    - Los determinantes pueden ser negativos. Esto depende de la orientación, básicamente.
        - Normalmente j-sombrero está a la izquierda de i-sombrero. Si después de una transformación lineal, j-sombrero está a la derecha de i-sombrero, se ha invertido el plano.
- **Matriz identidad**: la matriz que describe el plano cartesiano normal, es decir, [(1, 0), (0, 1)]. Se denota I.
- **Rango**: es el número de dimensiones que una transformación lineal tiene como resultado. Se dice que una matriz tiene rango 2 si su resultado vive en un plano.
    - Si una matriz toma un espacio de X-dimensiones y lo transforma a otro espacio de X-dimensiones, se dice que la matriz es de **rango completo**.
- **Sistema de ecuaciones lineal**:
- 
    - Las matrices nos permiten resolver ciertos tipos de sistema de ecuaciones, particularmente los lineales:
        - En cada ecuación, cada variable debe ser escalada y cada variable escalada debe ser sumada o restada. La típica forma de un sistema de ecuaciones lineal.
        - Esto descarta exponentes, funciones sofisticadas y multiplicación entre variables.
    - Si det(M) = 0, **suele no haber solución**. (Sin embargo, cuando no hay solución, necesariamente det(M) = 0)
        - Si el determinante de la matriz transformación es 0, la única forma de que haya una solución es que tal solución (vector v) viva en la línea o plano en la cual se encogió el espacio.
    - 
- **Inversa de una matriz**: matriz tal que, si M es una transformación linear, entonces M1M = I.
    - Si una transformación lineal encoge todo el espacio en una o más dimensiones, no existe transformación lineal inversa que deshaga esa operación.
    - O sea, sí existe, pero no sería una función en el sentido de una sola imagen, sino que deberías tomar un vector de la linea resultante y mapearla a toda una linea de vectores.
- **Espacio nulo**: es el conjunto de todos los vectores de un espacio que son mapeados al vector nulo después de una transformación que reduce 1 o más dimensiones.
    - Para 2D: si el espacio se encoge a una línea, hay otra línea que se mapea entera al origen.
    - Para 3D:
        - Si se encoge a un plano, hay una línea que se mapea al origen.
        - Si se encoge a una línea, hay un plano entero que se mapea al origen.
- **Matrices no cuadradas**: toma un vector de una dimensión y lo transporta a otra dimesión distinta.
    - Una matriz de 3x2 toma un vector en 2 dimensiones y lo mapea a un vector en 3 dimensiones.
    - El número de filas es la dimensión destino, y el número de columnas es la dimensión de partida.
- **Inversa de una matriz**: es una matriz A1 tal que, si multiplicada por su versión original, obtenemos la matriz identidad. A1A = I. Necesariamente **debe ser una matriz cuadrada**.
    - Se consigue a través de la **eliminación de Gauss-Jordan**.
    - Primero, debes conocer las **operaciones elementales de filas**:
        - **Tipo 1**: cambiar la posición de dos filas
        - **Tipo 2**: multiplicar una fila por un escalar no-cero
        - **Tipo 3**: sumar una fila, escalada o no, a otra
        - Si la matriz está asociada a un sistema lineal de ecuaciones, estas operaciones no cambiaar el conjunto solución.
    - **Matriz aumentada**: es una matriz que anexa las columnas de dos matrices en un sola con un separador vertical de por medio. Se emplea con el fin de aplicar las mismas operaciones de fila a todas las entradas de ambas matrices.
    - Luego, debes conocer **la forma de filas en escalones** (row echelon form):
        - En la fila de más abajo, debe estar las filas cuyas entradas sean todas cero.
        - Luego, debes ordenar las siguientes filas, de abajo hacia arriba, de tal forma que los coeficientes líderes sean el contorno de una escalera, de izquierda a derecha, formada por los 0 que quedan abajo y a la izquierda de esos coeficientes (**user tipo 3**).
    - La **forma reducida de filas en escalones** (reduced row echelon form), además:
        - Implica que todos los coeficientes líderes son 0 (**usar tipo 2**)
        - Cada columna que contenga un coeficiente líder, tiene el resto de entradas igual a 0 (básicamente como un vector base) (**usar tipo 3**).
    - La **eliminación de Gauss-Jordan** toma una matriz aumentada que expresa un sistema de ecuaciones a la derecha de la matriz identidad para dejarla en la forma REDUCIDA de filas en escalones. La matriz resultante a la derecha, lo que antes era la matriz identidad, es la matriz inversa.
    - Para obtener la forma reducida de una matrix 2x2:
        - Cambia las posiciones de a y d,
        - Pon signos negativos en frente de b y c,
        - Divide todo por el determinante: ad - bc.
        - A veces, no suele haber inversa.
    - **Propiedades** de la inversa:
        - (**A**−1)−1 = **A**;
        - (*k***A**)−1 = *k*−1**A**−1, mientras el escalar k no sea 0;
        - (**A**T)−1 = (**A**−1)T;
        - (**AB**)−1 = **B**−1**A**−1.
            - Más generalmente: (**A**1**A**2⋯**A***k*−1**A***k*)−1 = **A**−1*k***A**−1*k*−1⋯**A**−12**A**−11;
        - det **A**−1 = (det **A**)−1.
    - **Truco**: puedes factorizar inversas de matrices. -> A1+B1 = A1(A+B)B1

### Matriz de covarianza

- **Vector aleatorio**: una lista de colección (matriz) de variables aleatorias Xn que todavía no han tomado un valor, ya sea porque no ha ocurrido un valor o porque el conocimiento sobre el valor es imperfecto.
- Las **matrices de covarianza** capturan información sobre relaciones entre elementos del vector o matriz.
- La matriz de covarianza es siempre simétrica.
- var(A + B) = 1TSigma*1, donde 1 es el vector horizontal ([1], [1]) y Sigma es la matriz de covarianza de dos variables A y B.

# Cadenas de Markov

- Una Cadena de Markov es un sistema matemático que evoluciona con el tiempo.
- Consiste de un conjunto de "estados" y una matriz que contiene las probabilidades de pasar de un estado a otro.
    - La **matriz de transición** marca el estado actual con las filas y el estado futuro con las columnas.
- En cada unidad de tiempo, la cadena pasa de un estado a otro, haciendo el estado en el que está la cadena en un momento dado una variable aleatoria.
- Puedes volver un proceso donde la memoria importa a un proceso sin memoria **al capturar en cada estado sus estados pasados**. De esta forma, podemos modelar muchísimos procesos estocásticos generales en cadenas de Markov. Eso sí, esto complicaría la cantidad de estados que tenemos
- Propiedades:
    - **Homogeneidad temporal:** la probabilidad de pasar de un estado a otro es independiente del tiempo. (Es fija, básicamente)
        - También puede haber inhomogeneidad, o básicamente una distribución no-estacionaria, en la cual las prob. cambian con el tiempo.
    - **Pérdida de memoria**. <- (La **propiedad de Markov**, es la más importante)
- Propiedades de los estados:
    - **Periodicidad**: si un estado puede volver a si mismo en **una sola** cantidad fija y regular de pasos. Es aperiódico si el estado puede volver en sí mismo en un número no fijo de veces. (https://stats.stackexchange.com/questions/48838/intuitive-explanation-for-periodicity-in-markov-chains)
    - **Irreducibilidad**: posibilidad de pasar de cualquier estado a cualquier otro estado.
    - **Absorción**: si un estado tiene una probabilidad 1 de volver a sí mismo.
    - **Recurrencia o transciencia**: un estado es recurrente si tiene la **posibilidad** de eventualmente volver a sí mismo infinitas veces (¡no confundir con **el número de pasos** esperados para volver a sí mismo!). Si no, es transciente.
        - Recurrencia positiva: vuelve a sí mismo en un número esperado de pasos finito.
        - Recurrencia nula: vuelve a sí mismo en un número esperado de pasos infinito.
    - **Ergodicismo**: recurrencia y aperiodicidad. **Las cadenas ergódicas tienen una distribución estacionaria única**. En cierto sentido, tienen el “mejor” comportamiento.
- "La fracción de los días en los que habrá estado x": x = Px,x * x + Py,x * y, con x + y = 1.
- **Distribuciones estacionarias**: es una distribución de probabilidad que permanece sin cambios con el pasar del tiempo en la cadena.
    - Si *π* es una matriz fila cuyas entradas suman 1, y P es la matriz de transición, entonces $*π =πP^T*$.
    - En otras palabras, *π* es el valor propio desde la izquierda.
    - Para que una cadena tenga una distribución estacionaria, debe ser ergódica. Si es periódica, puede que tenga o no tenga.
    - Si P es una matriz de transición, entonces $P^2$ será la matriz de transición en 2 pasos, y así generalizado para n pasos.
- **Cadenas de Markov absorbentes**: cadenas de markov donde hay al menos un estado absorbente y puedes ir de cualquier estado al estado absorbente en un número finito de pasos.
    - **La matriz fundamental (N)**: https://en.wikipedia.org/wiki/Absorbing_Markov_chain
    
    [](https://wikimedia.org/api/rest_v1/media/math/render/svg/97645f614d72a3fdcd42763e4fd74b1817f2e5bc)
    
    - P es la matriz de transición.
    - Para conseguir los pasos esperados antes de tocar primera vez un estado X, tratamos al estado X como un estado absorbente (incluso si no lo es).
    - Si Q es la matriz de transición de un estado transciente a otro, entonces **N** = (I - Q)1 será la suma de Qk desde 0 al infinito. Esta es la **matriz fundamental**.
    - N contendrá entonces los pasos esperados para ir de estado i a estado j en la entrada (i,j).
    - R es la matriz representando la probabilidad de ir de un estado transciente a un estado absorbente.
    - Además, podemos conseguir la probabilidad de que un estado i sea absorbido por un estado j tomando la entrada (i, j) de Pinfinito o, al menos, de algún valor muy grande del exponente. También se expresa como B, siendo igual a B = NR.
    - **Truco**: si una distribución estacionaria existe de la cadena, el valor de cuánto tiempo le toma a un estado i a volver a si mismo es **el recíproco de su valor** en la distribución estacionaria.