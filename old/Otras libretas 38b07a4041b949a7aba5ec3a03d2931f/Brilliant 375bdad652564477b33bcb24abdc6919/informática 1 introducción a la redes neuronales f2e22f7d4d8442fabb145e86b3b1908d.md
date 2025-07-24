# informática 1 // introducción a la redes neuronales

Date de création: May 26, 2022 6:34 AM
Modifié: January 16, 2023 1:07 AM

- Una neurona es una célula cuya función es recibir, procesar y transmitir información a otras neuronas.
- Una red neuronal es una conexión de neuronas.
- Con la práctica de una actividad, las neuronas fortalecen su conexión con las que interactúan más y las cortan con las que menos.
- Como consecuencia, el cerebro aprende con la experiencia.
- Una red neuronal artificial es una colección de neuronas bajo una estructura que asimila la estructura cerebral de los mámales.
- La unidad fundamental aquí es la neurona artificial, la cual responde a inputs que nosotros les damos.
- La RNA hace predicciones basadas en sus inputs, siguiendo reglas mecánicamente para calcular outputs.
- Las RNAs aprenden, pero no piensan.

### Aspectos comunes del aprendizaje mecánico y humano

- Aprender requiere explorar nuevas acciones para completar una tarea.
    - Hacer lo mismo una y otra vez no nos lleva a aprender nada nuevo.
- Aprender es más rápido no solo cuando la respuesta nos dice que estamos mal, sino cuán mal estamos.
    
    

### Puntos importantes sobre las RNA

- Solo los humanos pueden extraer principios de sus experiencias.
- Las RNA hacen tareas difíciles haciendo cambios pequeños conforme recibe los resultados de un gran número de ensayos exploratorios.
- Una neurona artificial es una caja de decisiones:
    - Cada neurona tiene inputs asociados a ellas y un sesgo.
    - Los inputs son valores, normalmente entre 0 y 1.
    - El sesgo es una marca, también entre 0 y 1.
    - Si la suma de inputs >= sesgo, la neurona se activa. De lo contrario, permanece inactiva.
    - Colocar un límite de decisión es cómo una neurona, o una red neuronal, hace **predicciones** a partir de los datos.
        - 

### Neuronas como funciones

- 
- Las neuronas también pueden ser simplemente vistas como una función: le damos inputs, recibimos outputs.
- En el caso de una neurona binaria (la neurona siendo la imagen del input), la podemos representar como una función de "paso", como en la imagen.
- 
- Existe también otro tipo de neurona que permite activarse gradualmente, como se ve en la función de la imagen de arriba.
- Esta neurona se llama **neurona sigmoide**.
- 
- Si consideramos el peso, que es la barra sobre el input, la función se vuelve más pronunciada y parecida a la función paso (y se mueve a la derecha) al aumentar el peso.
- Similarmente, si disminuimos el peso, la función es más fluida, con una forma más de "s".
- Las neuronas sigmoides nos sirven para atribuir probabilidades al hecho de que un elemento pertenezca o no a una categoría.
- Un "**clasificador**" es un algoritmo que nos permite clasificar. Una neurona toma inputs y suelta como output una categoría.
- Una neurona binaria puede entonces funcionar como un clasificador.
- La fórmula de una función sigmoide es:
- Esta función no es nunca 0. Por lo tanto, una neurona sigmoide no puede nunca estar apagada o ser igual a 0.
- **Condición de activación de una neurona**: Itotal >= b, donde Itotal es la suma de inputs y b es el sesgo.
- Implica entonces que la neurona no está activada cuando Itotal < b.

## Múltiples capas

- Las fronteras de decisión de una neurona, -- que son líneas de probabilidad uniforme --, son líneas rectas en la nube de puntos.
- Entonces, los mejores de datos para una sola neurona son los datos que se separan en dos categorías con un línea recta, o aproximadamente.
- Por ejemplo, estos datos vienen de las posibles combinaciones de dos inputs para una puerta XOR.
- Puntos verdes son verdaderos, puntos rosas son falsos.
- No es posible clasificarla bien con una línea recta. Máximo tendremos 3 puntos bien clasificados y uno que no.
- Se vuelve posible, sin embargo, si ponemos una capa de neuronas en el medio hasta llegar a la neurona final.
- Cada neurona intermedia aporta una frontera de decisión (una recta), con esa exacta conexión establecida.
- Luego, si aplicamos una puerta OR, obtenemos una puerta XOR.
- El punto de añadir neuronas intermedias es luego aplicar lógica (OR, AND, NOT) a las neuronas intermedias para obtener un resultado en nuestra neurona final.

### Calzar curvas

- 
- El proceso de calzar curvas se hace bien con las RNA, especialmente si tienen varias neuronas intermedias.
- Por ejemplo, creamos una curva de aspecto normal al tomar una curva sigmoide (que corresponde a una neurona sigmoide intermedia) y substraerle otra.}
- Hasta ahora, sabemos que lo que hace una neurona es lo siguiente:
    - Tomamos un conjunto de "señales de entradas" o inputs (x).
    - Tomamos un conjunto de pesos (w).
    - Tomamos un umbral o sesgo (b).
    - Tomamos la suma ponderada de los inputs con los pesos y les restamos el umbral.
    - Esta última cantidad calculada la llamamos la diferencia.
- Una **neurona binaria** devuelve 1 o 0 si la diferencia es mayor que 0 o no, respectivamente.
- Una **neurona identidad** devuelve la misma diferencia, sin hacerla nada.
- Una **neurona sigmoide** toma la diferencia y la mete como input en una función sigmoide, devolviendo su imagen.
- Es fácil de ver nuevamente que una neurona simplemente es una función.
- De la misma manera, podemos construir funciones aproximándolas con rectángulos.
- Para ello, necesitas dos neuronas binarias intermedias que alimenten una neurona identidad.
- 
- El ancho del rectángulo se controla con los umbrales de las neuronas binarias intermedias o con el peso desde el input.
- El alto se controla con los pesos desde las neuronas intermedias.
- La posición se controla con los umbrales de las neuronas binarias intermedias.
- También hay que notar que, si los pesos desde una sigmoide hacia otra neurona sigmoide son muy fuertes, las sigmoides de llegada pueden actuar como binarias.
- "Entrenar" una RNA es simplemente configurar sus pesos y umbrales para que haga una determinada tarea.
- Finalmente, en el caso de RNA que son mapas de píxeles, podemos crear un mapa de pesos asociados a una neurona respuesta.
- Contexto :
- Lo que esta neurona hace es detectar asimetrías. Es activada por inputs en una mitad del mapa y desactivada por inputs en la otra mitad.