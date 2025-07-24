# stat. y proba. 6 // estadística avanzada I

Date de création: November 1, 2021 10:21 PM
Modifié: June 21, 2023 12:30 AM

# Introducción a la estadística

- La estadística nos da las mejores herramientas para tomar decisiones con información limitada.
- **¡Nada se prueba en estadística!** Las hipótesis son consideradas probables o improbables según los datos conseguidos.
- La mayoría del análisis estadístico consiste en lo siguiente:
    1. Proponer una **hipótesis**, que es una suposición hecha antes de la experimentación.
    2. Decidir un **criterio que rechace la hipótesis** si los resultados experimentales son demasiado "extremos".
    3. **Reunir y analizar datos**, y luego **rechazar o no rechazar** la hipótesis en función de los resultados.
- **Parámetros de la población**: un número cuantificando una característica de toda la población.
    - ¡Obtener parámetros de la población es muy difícil es caro en recursos! Por lo que tendemos a estimar.
- **Estimador**: una regla para estimar una característica de la población desde los datos.
    - Los estimadores suelen tener un sombrero, p̂, mientras que los parámetros reales no tienen sombrero, como p.
- Estimar un parámetro con una cierta muestra A puede tener un valor distinto con otra cierta muestra B. Estas diferencias se llaman **fluctuaciones**.
- **Teorema central del límite**: la media de las muestras de una población se distribuyen normalmente, incluso si la población de base no se distribuye normalmente.
    - Una reformulación de esto es que la suma de una cantidad n de V.A. independientes se distribuye normalmente, conforme n crece.
    - Es una reformulación porque, si tomas una muestra de N V.A. independientes, las sumas y las divides por N (tomas su promedio), vuelves a la primera formulación, la cual también se distribuye normalmente.
- No es una exageración decir que las estadísticas, particularmente las pruebas de hipótesis, serían imposibles sin el TCL.
- Cada prueba de hipótesis que encontraremos implica una estadística, que es un número derivado de los datos que recopilamos mediante muestreo. Y muchas de esas estadísticas suelen ser sumas, por lo que el TCL nos dice cómo se deben distribuir (es decir, como una curva de campana).

# Muestreo de datos

- **Muestra**: conjunto de la población seleccionado bajo un proceso definido.
- Una muestra "*representativa*" busca reflejar la población entera.
- Un **sesgo** da una representación desproporcional a un subconjunto de la población.
- **Muestra aleatoria simple (M.A.S.)**: cada miembro de la población tiene igual posibilidad de ser seleccionado.
- **Muestreo sistemático**: cada elemento en posición n de cada cierto subgrupo es muestreado.
- **Muestreo por grupos**: la población se divide en grupos (sin una característica común en especial) y luego se seleccionan grupos aleatorios.
    - **En una etapa**: tomas grupos aleatorios y muestreas todos los elementos de ese grupo.
    - **En dos etapas**: tomas grupos aleatorios y tomas una M.A.S. de los grupos.
    - Es útil cuando se tienen recursos limitados.
- **Muestreo estratificado**: se divide la población en grupos según una cierta característica.
- Evitar sesgo es casi imposible, por lo que hay que vivir sabiendo que hay un sesgo e intentando minimizarlo lo más posible.
- Una ***estadística*** es una cantidad computada a partir de los elementos de muestra aleatoria.
- Una estadística sesgada sobrevalora o infravalora el verdadero valor del parámetro de la población que pretende estimar.
- Más rigurosamente, una estadística es no sesgada si y solo si $E[S] = s$, donde $S$ es una estimación de un parámetro y $s$ es el parámetro poblacional.

### Margen de error

- Los parámetros de población mu y sigma son **constantes de valor ya fijado** que difícilmente podemos conocer por falta de recursos.
- Tomemos la expresión |X barra - mu|. Esa sería la diferencia entre la media muestral y la media real.
- Un margen de error de 5% significa que la diferencia |X barra - mu| < o = a 0.05, o 5%.
- También sabemos, por el TLC, que las medias muestrales se distribuyen normalmente con un n grande.
- Si estandarizamos las medias muestrales, conservamos todavía una distr. normal.
- Si conocemos entonces de alguna manera sigma y n, como también el valor z de nuestro interés, podemos calcular el margen de error de la diferencia absoluta.
- Tomando muchas muestras de la población, vamos a saber que 95% de las veces, la media real va a estar contenida en el intervalo [X barra - valor z * [std.dev](http://std.dev/)., X barra + valor z * [std.dev](http://std.dev/).] de la distribución normal de la media muestral.
- Ese intervalo se llama "intervalo de confianza a 95%".
- Si X barra es el promedio de una V.A. indicador (solo toma valores 0 y 1), el resultado está expresado en porcentaje (puntos porcentuales).
- Hay que decir también que la varianza de una variable indicador, si la variable sigue una distribución binomial (que la sigue), entonces sigma2 = mu - mu2.

### Sesgos

- **Sesgo de no-respuesta**: frecuentemente no se puede evitar.
- **Sesgo de respuesta voluntaria**: solo responden las personas con sentimientos fuertes hacia la pregunta que se les presenta.
- **Sesgo de cobertura limitada**: es una muestra que no fue extraída de la población entera.
- **Pregunta capciosa**: pregunta que implica que hay una respuesta correcta.
- **Pregunta cargada**: pregunta donde quien pregunta da una impresión fuerte de lo que quiere.
- **Preguntas de doble cañón**: pregunta que contiene dos preguntas y la respuesta respondería ambas al mismo tiempo.
- **Preguntas absolutas**: preguntas cerradas, donde se pierde la posibilidad de matiz.

### Varianza muestral

- **Grados de libertad**: valores en una estadística que son libres de variar.
- **Mejor definición**: valores que pueden ser asignados de forma arbitraria, antes de que el resto de variables tomen valor automáticamente.
- Ejemplo: si debes elegir entre 5 corbatas distintas para elegir una cada día de lunes a viernes, haces 4 elecciones, no 5.
- Aún más simple, si debes elegir 2 corbatas distintas para trabajar lunes y martes, haces solo una elección y no dos elecciones.
- Si puedes elegir un mismo elemento cuantas veces quisieras, con repetición, tendrías n elecciones posibles.
- Sin embargo, como no puedes repetir, tu corbata está decidida por tu penúltima elección.
- Si quisiéramos un margen de error, primero necesitamos una estimación de la varianza, y por ende necesitamos una estimación de la media.
- En ciertas condiciones, podríamos estimar la media intentando adivinar, a través de los que nos dice nuestro sentido común. Piensa, por ejemplo, en una votación de dos candidatos, que no sería loco asumir que se dividiría en 50/50.
- Después de que calculamos una media muestral para una muestra de cierto tamaño N, nos preguntamos cuáles combinaciones de valores entre las V.A. nos podrían dar ese resultado. Seleccionando los valores para cada V.A., nos damos cuenta de que las elecciones a hacer son n - 1. Es decir, la media muestral tiene n grados de libertad y la varianza muestral tiene n - 1 grados de libertad.
- En la media muestral, haces la suma de los valores y divides por los grados de libertad (n). En la varianza muestral, haces la suma de las distancias cuadradas y divides por los grados de libertad también (n - 1).
- Por supuesto, cuando fijas una media muestral, debe ser alcanzable con los posibles valores que tomen las V.A. Si no, vas a llegar a una contradicción, específicamente a una contradicción donde una V.A., para obtener el promedio deseado, toma un valor que no puede tomar, por lo tanto, la estimación de esa muestra es imposible.

## Recordatorio de hipótesis

- **Hipótesis**: es una afirmación que queremos chequear usando datos muestrales. Solemos tener dos hipótesis:
    - La hipótesis nula, H0, la cual intentaremos rechazar (o en su defecto, fallar en rechazar)
    - La hipótesis alternativa, HA, que es la negación directa de la hipótesis nula
- En la práctica, la hipótesis nula generalmente suele ser "no hubo ningún cambio" o "no sucedió nada".
- Si llegamos a fallar en rechazar la hipótesis nula, no significa que la hipótesis nula sea necesariamente cierta, sino que fallamos en proveer datos suficientes para rechazarla.
- Con esto dicho, **nunca "aceptamos" la hipótesis nula**: o la rechazamos, o fallamos en rechazarla.
- Pregunta crucial: "Si la hipótesis nula es cierta, ¿cuán extrema es nuestra muestra?"
    - Si nuestra muestra es muy improbable de obtener, entonces rechazamos H0.
    - El p valor es la probabilidad de observar un evento (o valor de nuestro estadístico) al menos tan extremo como el que nosotros observamos.

## El test Z y la estadística Z

- El test Z es un test de prueba de hipótesis que aplicamos cuando se cumplen dos condiciones:
    - Conocemos la varianza de la población (de la manera que sea), y
    - Nuestra variable aleatoria se distribuye normalmente.
- Lo aplicamos para saber cuán extremo es un resultado obtenido. Si es muy extremos, decidimos que nuestra hipótesis nula es falsa.
- La estadística Z nos ayuda a medir cuán extrema es nuestra muestra o, en otras palabras, cuán probable es que saquemos una muestra como la que sacamos.
- La estadística Z tiene la forma de:
    - Z = (alguna medida de la distancia entre la media muestral y la media de H0) * (algo que crece con el tamaño muestral).
    - Entre más grande se vuelva Z, más extrema es nuestra muestra (más improbable es obtener nuestra muestra).
- Para construir la estadística Z:
    - El valor esperado de nuestra media muestral es la media poblacional, que sería μ0.
    - La varianza de nuestra media muestral de tamaño n sería igual a σ2/n.
    - Finalmente, si X es nuestra media muestral de n variables aleatorias iid., entonces Z = (Xn - μ0) (sqrt(n) / σ) se aproxima a una distr. normal según crezca n.
    - Básicamente, estandarizamos nuestro estadístico, que es la media muestral y luego, usando nuestra tabla Z, buscamos cuán extremo es Z.
    - **Importante**: todos los p-valores que encontraremos dependen de que H0 sea cierta.
- **IMPORTANTE**: Teorema central del límite
    - Si tomamos una población con media mu y varianza sigma2, las medias muestrales se distribuyen aproximadamente de manera normal, incluso si la distribución de base no es normal, conforme crezca n.
    - Las aproximaciones aceptadas son con n > 30. Aunque si la distribución de base, la aproximación es normal también.
    - También sirven para aproximar distribuciones binomiales, usualmente con muchos n pues hacer tantos cálculos es tedioso, pero con la condición de que min(np, n(1-p))> 5. (Sin importar si n > 30 o no)
- **p-value**: es simplemente la probabilidad de observar un dato suponiendo que H0 es cierta.
    - ¡Esto no se limita a el area bajo la curva de las distribuciones normales! Tienes que encontrar la manera en cada situación de medir la extremidad de tu dato observado.
- **p-hacking**: mal uso del análisis de datos para llegar a una conclusión errónea, aumentando la probabilidad de un falso positivo.
    - Ex.: utilizar solo una muestra donde rechazamos H0 para rechazar H0 en el resto de las muestras y en general.
    - Ex.: solo reportar las muestras donde rechazamos H0 e ignorar las otras donde no.
- **Errores de tipo I y II**: fijemos alfa = 0,05.
    - **Error de tipo I**: es un falso positivo. Si H0 fuese verdadera, el error posible para nosotros es de rechazarla. Nos equivocaríamos entonces un 5% de las veces, que es alfa.
        - Una reformulación es que la probabilidad **condicional** de un falso positivo, suponiendo que H0 es cierta, es de alfa o 5%.
        - En ese caso, acertaríamos 95% de las veces, que es (1 - alfa).
        - (1 - alfa) es la probabilidad de correcto negativo.
    - **Error de tipo II**: es un falso negativo. Si H0 fuese falsa, el error posible para nosotros es de fallar en rechazarla. El valor de Beta depende del valor de Alfa. Si alfa crece, beta disminuye.
        - Notemos que un acierto para nosotros es rechazar H0 cuando efectivamente es falsa.
        - Si Beta es entonces la prob. de un falso negativo, (1 - Beta) es la prob. de un correcto positivo. **Un correcto positivo es finalmente lo que queremos, por eso es el "poder" de nuestro test**.
        - Beta depende de alfa, pero también depende de otros factores, como el tamaño de nuestra muestra o bien qué es exactamente HA.
    - Entre más grande sea la diferencia entre H0 y HA, mayor poder tiene nuestro test.
    - Similarmente, entre más grande sea nuestra muestra, mayor poder tiene el test.
    - Podemos aumentar (1 - Beta), el poder de nuestro test, aumentando alfa o aumentando nuestra muestra.
        - Al aumentar alfa, el riesgo de falso positivo, disminuimos beta, el riesgo de falso negativo, por lo que aumentamos finalmente (1 - Beta), la prob. de correcto positivo.
        - Sin embargo, queremos que alfa se mantenga pequeño.
        - Entonces, no aumentamos alfa, sino que nos concentramos en aumentar el tamaño muestral.
        - Es práctica estándar que el poder de un test sea mayor que 80%.
        - Un estudio tiene "poco poder" si no tiene un tamaño muestral suficiente que le permita llegar a un poder >= 80%.
- Intérvalos de confianza: manera de estimar parámetros poblacionales, como al media real.
    - Supongamos que vamos a tomar muestras de una población muchas veces.
    - Cada muestra tendrá una media. Vamos a tomar un intérvalo alrededor de esta media muestral.
    - A veces, puede ser que la media real se encuentre dentro de este intervalo que hemos definido. Otras veces, no.
    - Si el intervalo cubre el 95% de los valores alrededor de la media muestra, a izq. y der., la proporción de veces que la media real se encuentre dentro de nuestro intervalo es 95%.
    - Sin embargo, ¡notemos que la media real ya está definida! La media real no se define como un proceso aleatorio.

## Chi cuadrado

- A la estadística Z le podemos hacer algunas modificaciones importantes:
    - Primero, con X una V.A.N. estándar, si E[X] es muy pequeño (digamos, entre 0 y 1), entonces E[X] es aproximadamente igual a Var[X]. (Recordando que E[X] = np, y que Var[X] = npq. Con lo cual, q es aproximadamente 1, o la prob. de éxito p es casi 0)
    - Luego, notemos que la varianza de la estadística Z es igual a la estadística Z elevada al cuadrado.
- Finalmente, de esto pasamos a la estadística Z a la fórmula para chi cuadrado:
    - 
    - Oi es el valor observado y Ei es el valor esperado (dado que H0 sea cierto).
    - Esto se llama la estadística *χ*2 de Pearson, y mide la varianza de la estadística Z, o sea, la varianza de la medida de extremidad.
- E[*χ*2(k)] = k.
- Var(*χ*2(k)) 2k.
- Mientras más crecen los grados de libertad, más la distribución se asemeja a una distribución normal.
- Cuando necesitamos probar una hipótesis midiendo la distancia de los valores obtenidos a los valores esperados, chi cuadrado es muy buena.
- Cada restricción (ecuación que relacione las variables aleatorias) y cada punto de datos que haya sido estimado y, por consecuente, se convierta en una constante, reduce los grados de libertad por 1 unidad.
- La fórmula de grados de libertad es df = (l - 1)(c - 1), donde l es el número de filas y c el número de columnas.
- El resultado de chi-cuadrado también puede interpretarse como la "bondad de ajuste": entre más cerca de 0 sea la estadística, más se describe bien por la distribución de chi-cuadrado.

### Principio de máxima verosimilitud

- Nos permite estimar los parámetros de la población al maximizar la probabilidad de los datos observados cuando:
    - La distribución puede ser escrita directamente en términos de los parámetros incógnitos.
    - La distribución tiene un claro máximo.

### Tests de homogeneidad e independencia

- Los tests de homogeneidad observan dos poblaciones e intentan determinar si ambas poblaciones tienen la misma distribución.
- Los tests de independencia observan una sola población con dos variables o atributos, e intentan determinar si esos atributos son independientes o no.

# El t-test

- Un t-test es cualquier test donde el estadístico utilizado sigue una distribución T de Student bajo la hipótesis nula.
- Usos: cuando el tamaño de tu muestra es muy pequeño y no conocemos la varianza real tampoco...
    - Estimar una media real al determinar la distr. de la diferencia de la media muestral y la media real.
    - Determinar la distribución de la diferencia de las medias de dos poblaciones.
        - **t-test en parejas**: dos poblaciones donde se puede presumir que la misma varianza se mantiene. Ex.: población antes y después de un tratamiento médico, donde la media de la calidad de salud puede subir pero la varianza debería ser la misma. → Utiliza varianza agrupada.
        - **t-test no emparejado**: dos poblaciones donde las varianzas se creen diferentes. → Utiliza varianza desagrupada.
- Esquema general de la medida de dispersión entre dos medias:
    - Luego veremos que tiene la forma de una t-estadística, incluso si no es evidente ahora.
- EJERCICIO #1: DIFERENCIA DE PROPORCIONES CON UNA CARACTERÍSTICA DE DOS POBLACIONES DISTINTAS
- Usamos una hipótesis nula de que las medias de las proporciones ambas poblaciones son iguales, por lo que queremos finalmente demostrar que son diferentes.
- Usamos una estadística de extremidad con el mismo esquema o misma estructura a la estadística Z:
    - 
    - La diferencia entre las muestras es (p̂1 - p̂2)
    - La medida de dispersión sería la varianza. La varianza sería E[(X - E[X])2], es decir, E[((p̂1 - p̂2) - E[p̂1 - p̂2])2]
    - Esto se simplifica a E[((p̂1 - p̂2) - E[p̂1] + E[p̂2] )2], luego a E[(p̂1 - p̂2 - p1 + p2)2], luego a E[ ( [p̂1 - p1] - [p̂2 - p2] )2], luego a E[(p̂1 - p1)2 - ***2(p̂1 - p1)(p̂2 - p2)*** + (p̂2 - p2)2]
    - Por linealidad (solo nos concentramos en el término del medio, en cursivas y negritas): 2 * E[(p̂1 - p1)(p̂2 - p2)], luego a 2 * E[(p̂1 - p1)] * E[(p̂2 - p2)]...
        - Luego a 2 * (E[p̂1] - E[p1]) * (E[p̂2] - E[p2]), luego a 2*(p1 - p1)*(p2 - p2), luego a 2*0*0, finalmente a 0.
    - Entonces quedamos con E[(p̂1 - p1)2 + (p̂2 - p2)2], luego a E[(p̂1 - p1)2 ]+ E[(p̂2 - p2)2].
    - Notemos que cada uno de los dos términos es simplemente la varianza de p̂1 y p̂2, respectivamente.
    - Finalmente tenemos que **Var(p̂1 p̂2) = Var(p̂1) + Var(p̂2).**
- Por otro lado, tenemos que la varianza de n variables binomiales es np(1-p).
    - Sin embargo, si esta variable binomial la expresamos como una proporción total de los ensayos de Bernoulli hechos, tenemos que la varianza termina siendo Var(1/n * X) = 1/n2 * Var(X) = p(1-p)/n.
- Notemos, sin embargo, que esa última expresión depende de p, que es un parámetro poblacional que no conocemos.
- Lo que hacemos es estimar p como la media de p1 y p2, y luego estimamos p1 y p2 con sus respectivas medias muestrales, p̂1 y p̂2.
- Estimaríamos p entonces como (n1p̂1 + n2p̂2)/(n1 + n2). (NO DEBEMOS TOMAR LA MEDIA DE LAS MEDIAS, SINO PONDERARLAS CORRECTAMENTE)
- Notemos también que, en el caso de que una población tenga un tamaño más grande que la otra, esta población contribuirá más a la estimación de p.
- Esquema específico de la t-estadística en este ejercicio:
- EJERCICIO #2: T-VARIABLES
- **T-variables** : hay situaciones donde no conocemos ni la media real ni la varianza real, aún peor, tenemos un n muy pequeño para decir que nuestra media muestral está cerca de la media real.
    - De todas maneras, queremos estimar la media real con un margen de error.
        - **Margen de error**: unidades por encima y debajo de la media muestral donde tenemos un cierto % de confianza que cubra la media real.
    - Nuestra estadística será la estadística Z basada en las medias muestrales.
    - Primero, necesitamos estimar la varianza real, pero ni siquiera tenemos la media real.
    - Podemos utilizar la fórmula de varianza muestral para ello. Esta fórmula no necesita la media real, sino la media muestral, la cual sí conocemos. (La imagen es la desviación estándar muestral, pero ajá...)
    - Ahora, podemos transformar nuestra estadística Z en una variable T de Student.
    - Necesitamos que nuestra estadística siga este esquema:
        - En el numerador, una variable normal estándar.
        - En el denominador, la raíz de una chi2 dividida por n.
    - Primero, para ajustar el denominador, dejamos la varianza muestral sola allí.
        - La varianza muestral es casi la suma de los cuadrados de n V.A.N. Es, más específicamente, una chi2 de n-1 grados de libertad.
    - Ahora, para ajustar el numerador:
        - Nuestra estadística hasta este momento fue la media muestral.
        - Una media muestral es simplemente la media de los datos de una muestra, duh.
        - Ahora bien, consideremos que cada dato es, en realidad, una variable normal, y que nosotros solo observamos un dato de ella.
            - El ejemplo de Brilliant es que cada dato era la "cantidad de litros de combustible consumidos el año pasado". Y te daba valores como x1 = 99, x2, 101..., bien, ahora haz como si cada dato fuese una variable normal y esos valores los "recogiste" de la distribución de cada variable.
        - Una vez eso hecho, ahora queremos que la distribución de cada dato esté centrada a 0 y con desviación 1. Haremos de cuenta que conocemos la media y desv. de cada dato como para poder saber la distribución normal de cada dato, incluso si en realidad no la conocemos.
        - Bien. Ahora, tomemos la suma de cada dato. (∑ xi), esta suma tendría media 0 y varianza n (desv.: √n), según el TLC.
        - Luego, para llegar a la media muestral, tenemos que dividir la suma por n. → X barra = (∑ xi)/n.
        - Ahora tenemos una variable aleatoria, la media muestral, con media aún 0 pero con varianza 1/n (desv.: √n/n = 1/√n).
        - Finalmente, queremos normalizar nuestra media muestral, es decir, que la varianza y la desv. sean iguales a 1. Tenemos simplemente entonces que multiplicar la media muestral por √n.
        - Notemos, ¡**toda esta álgebra es posible con nuestro esquema de estadística Z**! Entonces, nuestra estadística desarrollada hasta ahora, (X barra - mu)/(s/√n), es una t-variable de Student. (Es la variable que encerré en el cuadrado verde)
- **Detalle**: al momento de normalizar la distribución de cada dato, puedes pensar que estamos hablando de "la diferencia con respecto de la media de ese dato observado, expresado en desv.".
    - Luego, la interpretación de la media muestral sería "la media de las diferencias con respecto a la media de cada dato, expresado en devs.".
    - Al final, la distribución de la t-variable está también expresada en devs.
    - Al calcular el valor t (análogo del valor z), tal que el área entre (-t) y (t) = 0.95, ese valor t está expresado en devs. Si, al final, multiplicas cada dato de la t-distribución por el error estándar de nuestra estadística, (s/√n), ahora sí tenemos una distribución donde desde el principio sabíamos la media y la desv. de cada distribución de cada dato.
        
        Por ejemplo, veamos una t-variable de 4 grados de libertad.
        
        El t valor que encerraría un 95% del ahora bajo la curva sería t = 2,56.Entonces, para que nuestra t-variable nos dé un 95% de confianza...La diferencia entre nuestra media muestral y la media real debe ser de 5.12 unidades.**¿Que pasa cuando multiplicas cada dato por tu error estándar, (s/√n)?** Cada dato (y, en este caso, la distribución de cada dato) es multiplicado también por el error estándar. De esa manera, no nos tenemos que preocupar de la varianza real de la distribución de cada dato que compone a la media muestral, porque ahora la distribución incorpora una varianza distinta de 1, es decir, una varianza "realista" en la práctica. (Esto es lo que hacemos al pasar de la primera línea a la segunda, multiplicar por el error estándar).**Sin embargo, la media igual es 0, lo cual no es realista en la práctica.** No nos importa, puesto a que no conocemos la media real de nuestra estadística, entonces queremos medir la distancia de la media muestral de la media real **en unidades** (y ya no en devs.). Es exactamente lo que queremos y lo que podemos hacer con este test: **saber la distancia de la media muestral a la media real.**
        
- ¡Listo! Ahora tenemos una variable T de Student.
- La distribución de una variable T ya ha sido estudiada. Existen tablas como la de z-valores de la Normal.
- **Distribución T de Student**: es la distribución de la T-variable. Nace de tratar de estimar la media real de una población con una muestra pequeña y varianza real desconocida.
- EJERCICIO #3 Y #4: VARIANZA AGRUPADA Y DESAGRUPADA
- En el estudio de comparar las medias de dos poblaciones, podemos utilizar una varianza agrupada o una varianza desagrupada.
    - **Varianza agrupada**: es una estimación de la varianza real cuando suponemos que la varianza real de ambas poblaciones es la misma, incluso si sus medias reales no lo son.
    - **Varianza desagrupada**: suponemos que las varianzas reales entre dos poblaciones no son la misma.
    - **Criterio estadístico**: s1 y s2 son las varianzas de muestras 1 y 2.
        
        (Esto no sale de ningún teorema. Es simplemente una recomendación estadística de la experiencia.)
        
        Si esta desigualdad se cumple, entonces los datos sugieren que sigma1 = sigma2 y podemos usar la varianza agrupada. Si no, se sugiere que las varianzas reales son diferentes.
        
    - En este ejercicio, nuestra hipótesis nula es que las medias de ambas poblaciones son las mismas. Entonces, nuestra estadística se convierte en lo siguiente. (¡Las medias poblacionales se cancelan!)
        
        **Varianza agrupada**Para agrupar finalmente ambas varianzas muestrales en una estimación de la varianza real, **simplemente tomamos el promedio de ambas**, suponiendo que las poblaciones son del mismo tamaño. En caso de que no, el método general es una media ponderada:(Si n1=n2 y lo llamamos n, esto se simplifica a [s1+s2]/2)En el caso de varianza agrupada entonces, nuestra t-variable o t-estadística es:Finalmente, ***en el caso general***, para usar una t-estadística: notemos que tiene (n1+n2-2) grados de libertad.
        **Varianza desagrupada**Finalmente, para comparar la diferencia de medias de dos poblaciones, la estadística sería:Dos detalles con respecto a esta estadística **que utiliza una varianza desagrupada**:
        
        - No es perfectamente una t-variable, pero es aproximadamente distribuida como una.
        - Los grados de libertad sería min{n1 -1, n21}.

## Regresiones lineales y ANOVA (análisis de varianzas)

- **ANOVA**: método para comparar las medias de más de dos poblaciones.
- **Lenguaje**:
    - **Variables independientes (categóricas)** → "factores".
    - **Variables dependientes** → "respuestas".
    - **Categorías** → "niveles".
- Cuando queremos comparar las medias de más de dos poblaciones, el t-test ya no es tan útil puesto a que el riesgo de falso positivo aumenta mucho, lo cual ANOVA evita.
    - Entre más aumentan nuestros niveles, más aumenta este riesgo.
- Recordatorio: la H0 suele ser "no hay ningún cambio o relación entre var. ind. y var. dep."
    - Se puede interpretar también como "las variaciones observadas en nuestros datos son completamente consecuencia de lo aleatorio, o 'ruido' de los datos. No tiene nada que ver con los predictories (var. inds.)".
- Regresión lineal de la forma Y = c:
    - El valor de c que minimiza la SEC (suma de errores cuadrados) es simplemente la media muestral.
- Regresión lineal de la forma Y = mx + c:
    - El valor de c óptimo sería c = y barra - m(x barra).
    - El valor de m óptimo sería m = Cov(X,Y)/Var(X).
- **F-estadística**: estadística construida para probarla contra la hipótesis nula que sería "el mejor modelo lineal para explicar tal variable es simplemente la media muestral".
    - Si la F-stat toma valores "ordinarios", entonces el mejor modelo es la media, por lo que fallamos en rechazar H0.
    - Si toma valores "extremos", existe un modelo lineal con m != 0, por lo que rechazamos H0.
- SST = SECRL: Suma de errores cuadrados con respecto al modelo lineal.
- SSE = SECC: Suma de errores cuadrados con respecto al modelo constante.
- Si (SST - SSE) es grande, es porque SST es más grande que SSE, lo que significa que el modelo lineal parece ser más preciso que el modelo constante.
- Si es pequeño, realmente entonces no hay mucha diferencia entre usar el modelo lineal y el modelo constante.
- Notemos que SSE tiene n-2 grados de libertad y SST tiene n-1.
- La varianza de SSE, ∆σ2, sería simplemente SSE/(n-2), que significaría el error cuadrado medio de cada punto con respecto al modelo lineal.
- Imaginemos una nube caótica de puntos. Inicialmente la modelamos con un modelo constante.
- Si pasamos de un modelo constante a uno lineal, perdemos un grado de libertad.
- Además, imaginemos que el modelo lineal realmente no explica los datos.
    - Un modelo lineal SIEMPRE tendrá un error más pequeño que un modelo constante.
    - Es decir, SST >= SSE.
- La consecuencia de esta acción es que simplemente perdemos un grado de libertad en nuestra suma de errores cuadrados. Es decir, nuestro SSE baja.
    - Eso sí, nuestro SSE baja en el valor esperado que cada punto contribuye al SSE. Es decir, nuevo error SST - SSE/(N-2) = SSE.
    - Si nuestro modelo lineal no parece explicar los datos → SST - SSE ≈ ∆σ2
    - Si nuestro modelo lineal SÍ parece explicar los datos → SST - SSE >> ∆σ2
        - En este caso, la diferencia entre el modelo constante y lineal es mayor que simplemente dejar caer una observación aleatoria del dataset. Es lo que expresa la expresión matemática.
    - Poniendo todo junto :
        - Si (SST - SSE)/∆σ2 >> 1, el modelo lineal es una buena opción.
        - Si (SST - SSE)/∆σ2 ≈ 1, el modelo lineal no es un buen modelo a usar.
        - Esta razón o ratio, (SST - SSE)/∆σ2, es nuestra estadística F.
    - No olvides que SST sigue una distr. chi2 con n-1 GdL, y SSE con n-2 GdL.
    - Introducimos un nuevo término, SSR, que es la suma de diferencias cuadradas entre el mejor modelo lineal y el mejor modelo constante.
        - También es simplemente SSR = SST - SSE.
        - Los grados de libertad de SSR son solamente 1.
- En el caso de múltiples variables independientes de predicción, el modelo lineal es un "hiperplano".
- Si Zi es nuestra variable respuesta de indice i, entonces:
    - 
    - Xi, Yi, Wi... son las variables predictivas. Hay una cantidad "g" de ellas.
    - En ese caso, la F-stat se convierte en:
- Si tomamos SSE, SST y SSR y las dividimos o "normalizamos" por sus grados de libertad tenemos, MSSE, MSST y MSSR, donde "M" significa "media".
- La segunda expresión de escribir F muestra MSSR/MSSE en el caso general multilinear.
    - También notemos que SSR y SSE son chi2 con g y (n-1-g) grados de libertad respectivamente.
- Notemos que podemos escribir MSSR = MSST - MSSE.
- Es aquí donde entendemos por qué se llama "ANOVA", analysis of variances, o análisis de varianzas.
- Cada error cuadrado medio es una varianza, por definición.
- La F-stat termina siendo la razón de dos varianzas, F = MSSR/MSSE, o también se puede escribir como F = (MSST - MSSE)/MSSE.
- Una **tabla ANOVA, para una reg. lin. de una sola variable ind.,** es lo siguiente:
    
    *(OJO: SSR=MSSR si los grados de libertad de SSR es 1, que es solo en el caso de una **reg. lin.** de una sola variable)*
    
- La variable sigue su propia distribución, la F-distribución. Es una razón de dos variables chi2.
- "F" viene de Ronald Fisher. Él estudió las variables aleatorias de la siguiente forma:
    
    Se llamaría "una F-variable con a y b grados de libertad".
    
- Recapitulación:
    - Cuando H0 es cierta, al pasar de un modelo constante a un modelo lineal, la caída en la suma de errores cuadrados al dejar caer un punto del modelo debería ser aprox. igual al valor medio que cada punto contribuye a la suma de errores cuadrados. → SST - SSE ≈ ∆σ2
    - Cuando H0 es falsa, la diferencia es considerablemente más grande. → SST - SSE >> ∆σ2
- **El método ANOVA usa la F-stat para comparar la media de varias poblaciones.**
- Primero, necesitamos transformar el problema de comparar las medias como un problema de regresión lineal.
- Nuestro modelo lineal tendría la siguiente forma: ANOVA Unidireccional
- Si tenemos 4 medias, por ejemplo, utilizamos un coeficiente libre y 3 otros coeficientes de variables. Nuestro modelo tendría entonces 4 términos.
- Los xi son variables indicadoras : tomar valor 1 si un punto de los datos pertenece a la categoría A, por ejemplo, y 0 sino.
- La fórmula general para l-1 términos sería:
- Normalmente, la hipótesis nula en los test ANOVA es que las medias reales de todas las categorías (niveles) son iguales: μ0 = μ1 = μ2 = ... = μl.
- Sin embargo, recuerda que estamos en un contexto de "regresión lineal", por lo que la H0 debería ser "la respuesta (var. dep.) no depende de los factores (var. ind.)". Y vamos a usar la F-stat para probar esto.
    - En un sentido práctico, diríamos entonces que todas las medias son iguales a μ0.

- Cada valor tendrá una desviación de la predicción hecha por el modelo. Esta desviación será épsilon.
- Épsilon es llamado también "ruido", puesto a que es lo que nuestro modelo no puede explicar con los factores que contempla.
- Pero notemos que podemos entonces escribir nuestra suma de errores cuadrados, SSE, como ∑ε2, puesto a que ε es, por definición, el error.
    - SSE tendría n-l grados de libertad. Si tenemos 4 categorías/niveles, tenemos n-4 GdL.
- Entonces, el MSSE sería SSE/(n-4).
- Similarmente, el MSST, el error medio cuadrado de cada dato con respecto a la Gran Media, sería SST/(n-l). (l: niveles)
    - El SST solo pierde un grado de libertado porque usamos la media de medias.
    - Atención, la media de medias no ponderada (lo que normalmente "no se debe hacer") se llama la "Gran Media", y es diferente de la media de medias ponderada.