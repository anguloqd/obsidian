# stat. y proba. 2 // fundamentos de la estadística

Date de création: July 21, 2021 6:53 PM
Modifié: January 16, 2023 1:07 AM

- En probabilidad, resolvemos *hacia adelante*. Comienza con una regla exacta y bien definida. Usamos esta regla para predecir lo *que* sucederá en el futuro. No conocemos los resultados, pero la probabilidad nos permite cuantificar lo que debería suceder.
- En estadística, resolvemos *hacia atrás*. Comienza con los resultados finales, conocidos como datos. Tomamos estos datos e intentamos determinar qué reglas bien definidas los crearon.

## Regresiones

- **Suma de los residuos cuadrados**: Σ(y - ŷ)2.
    - Es el grado de variabilidad de los puntos que la variable independiente x que no puede explicar.
- **Suma de los cuadrados totales**: Σ(y - ȳ)2.
    - Es el grado de variabilidad de la variable dependiente y en general.
- **Coeficiente de determinación (R2)**: 1 - (SRC/SCT).
    - Suponiendo que la variabilidad total de la variable y está compuesta de (variabilidad explicada + variabilidad no explicada), entonces si tomamos el complemento de SRC/SCT, obtenemos la variabilidad que sí es explicada de la variable y con la variable x.
    - A menos que R2 = 1, siempre habrá alguna variación en y que no se explica por x.
- **Regresión lineal**: la regresión lineal ajusta una línea a los puntos de datos para que los valores de salida se puedan predecir en función de los valores de entrada. La línea de mejor ajuste es la que optimiza R2.
    - En variables económicas y financieras, suele ser difícil conseguir un coeficiente de determinación mayor de un 30%.
- **Coeficiente de correlación de Pearson**: r, la raíz cuadrada de R2, es un número entre -1 y 1 que indica la fuerza con la que dos variables comparten una relación lineal.
    - Solo obtenemos r tomando la raíz cuadrada de R2 si la función de la que se tomaron los residuos cuadrados es lineal.

## Cosita sobre combinatorias

• Si tienes que pensar en caminos, divide en dos tipos de caminos (decisiones *binarias*) y recuerda que puedes cambiar el orden, pero debes mantener la misma cantidad.
**Sesgos**
• El **sesgo de muestreo** ocurre cuando una muestra se recolecta de tal manera que algunos miembros de la población prevista tienen una mayor probabilidad de ser muestreados que otros.
• El **sesgo estadístico** se refiere a la tendencia de un proceso de medición a sobreestimar o subestimar el valor de un parámetro de población.
• Un **estimador no-sesgado** es una estadística precisa cuyo valor esperado es el mismo que el valor que se está estimando. El valor esperado de un estimador sesgado **difiere** del valor real.
• En general, la varianza de la muestra es menor que la varianza de la población.
• No queremos utilizar la fórmula de la varianza de la población en una muestra porque es un estimador sesgado. En general, subestimará la varianza de la población, ya que las muestras tenderán a perder valores atípicos.
**Error estándar**
• Ok, empecemos primero con una estadística. Una **estadística** es cualquier cantidad calculada a partir de los valores de una muestra que se considera para un propósito estadístico.
• Luego, la **distribución muestral de una estadística** es una distribución de variable aleatoria (como la curva de Gauss) que se genera al tomar repetidas veces muestras de un cierto tamaño de la población, y luego calculando la estadística de allí. El resultado de ese cálculo luego se plotea, y se termina construyendo tal distribución al haber hecho este proceso muchas veces. La distribución de este estadístico también tiene su propio media y desviación estándar
    ◦ (si la distribución fuese de la media, esto significaría que habría una media de las medias muestrales y también una distribución estándar de las medias muestrales)
• El **error estándar** es la desviación estándar (real o estimada) del estadístico muestral. Si tal estadístico muestral es la media, entonces se denomina error estándar de la media.
• La relación entre el error estándar de la media y la desviación estándar es tal que, para un tamaño de muestra dado, el error estándar de la media es igual a la desviación estándar dividida por la raíz cuadrada del tamaño de la muestra.
    ◦ 
    ◦ La gran mayoría de veces, sin embargo, no se conoce la desviación estándar de toda la población. Por lo tanto, para estimar la desviación estándar del estadístico, se utiliza la desviación estándar del estadístico muestral.
    ◦ Esto se debe a que a medida que aumenta el tamaño de la muestra, las estadísticas de las muestras se agrupan más estrechamente alrededor de la estadística de la población.
• También hay otra fórmula para el error estándar:
• 
    ◦ p gorro es la probabilidad de éxito, q gorro es la probabilidad de fracaso.
• Por último, **todas estas fórmulas para errores estándar son APROXIMACIONES**. La condición para que esta aproximación sea aceptable es que el tamaño de la población sea 20 veces más grande que el tamaño de las muestras tomadas.
**Hipótesis Nula**
• Supongamos que tenemos una hipótesis que queremos probar. A ella, la vamos a llamar H1, la hipótesis alternativa.
• Luego, vamos a tomar la afirmación de la hipótesis a probar y la vamos a negar, es decir, vamos a llegar a la hipótesis contraria. A esta hipótesis la vamos a llamar H0, la hipótesis nula.
• Para probar nuestra hipótesis original, una forma de hacerlo es mostrar que la hipótesis nula es falsa, cuya consecuencia inmediata sería que nuestra hipótesis original es cierta. Más específicamente, lo que hacemos es **suponer que la hipótesis nula es cierta**, y luego encontrar una contradicción. Esto es básicamente reducción al absurdo.
• El p-valor se define como la probabilidad de que el resultado obtenido sea igual o aún más extremo. Formalmente, P( Obtener los datos observados | H0 es cierta ), tomados de la distribución nula (la distribución que resulta si la hipótesis nula es cierta).
• Alpha se define como la probabilidad establecida tal que, si el resultado obtenido es tan extremo o más extremo que alpha, el resultado es entonces improbable y se rechaza la hipótesis nula.
• Básicamente entonces, se rechaza H0 si p-valor <= alpha. Se acepta la hipótesis nula si p-valor > alpha.
• El alpha más tradicional es 0.05. Es decir, si la probabilidad de  que hayamos obtenido tal resultado de nuestro experimento es de 1 en 20. También se aproxima a 2 desviaciones estándar, asumiendo una distribución normal de la estadística.
• **ESPECIFICACIÓN**: solemos usar un valor exacto y concreto (o un rango de valores concreto) para nuestra hipótesis nula. Al rechazar la hipótesis nula, y si la hipótesis alternativa es también un rango, entonces descartamos los valores o rangos de H0, pero no podemos decir si le realidad es más arriba o más abajo. Ejemplo: H0 es que los estudiantes necesitan 10 minutos en promedio para hacer su tarea. **Rechazar la hipótesis nula no nos da un valor concreto como verdadero**. Puede ser 8 minutos de promedio, o 12 minutos de promedio.
**Errores de Tipo I y Tipo II**
• Tipo I: falso positivo, creemos que detectamos un efecto cuando en realidad no lo hay. Específicamente, cuando rechazamos H0 pero en realidad no debimos haberla rechazada.
    ◦ Alpha, el p-valor, es también la probabilidad de que tengamos un falso positivo.
• Tipo II: falso negativo, sí hay un efecto pero no lo vimo. Específicamente, cuando nuestra hipótesis original es cierta, pero no tenemos evidencia suficiente para rechazar H0.
    ◦ Beta se denomina como la probabilidad de un falso negativo.
    ◦ Calcular β es más difícil: aunque podemos calcular la probabilidad de un error de Tipo II para cualquier valor específico de la hipótesis alternativa, nunca sabemos exactamente cuál será el verdadero efecto del experimento (o de lo contrario no estaríamos haciendo un experimento!).
    ◦ La "potencia" de un experimento es la probabilidad de que pueda encontrar el efecto que busca, asumiendo que el efecto está ahí. Si conociéramos β, podríamos calcular la potencia con precisión, ya que es el complemento de 1 - β.
    ◦ "La ausencia de evidencia no significa la evidencia de ausencia".
• **LAS ÁREAS SOLAPADAS ENTRE AMBAS HIPÓTESIS ES IMPORTANTE**. La área compartida en la distribución de H0 es la área de falsos positivos, es decir, el p-valor o alpha. La área solapada en la distribución de H1 es la área de falsos negativos, es decir, Beta.
    ◦ Si reduces tu alpha, entonces aumentas tu beta, y viceversa.
    ◦ Piensa en el ejemplo de las alarmas de fuego: si una cierta cantidad de humo es detectada, al aumentar tu alpha (la sensitividad al humo: la cantidad de humo desde la cuál dices que hay un fuego), sueles tener más alarmas falsas, pero automáticamente reduces el riesgo de que sí haya un fuego y que la alarma no lo detecte, es decir, un falso negativo.
    ◦ De esto último también podemos inferir que **hay casos donde preferimos un tipo de error sobre otro**.
    ◦ Entre más área solapada haya entre ambas distribuciones, menos poder estatístico habrá. Piensa: si la cantidad de humo emitida cuando estoy cocinando y cuando hay un fuego es casi la misma, es más difícil discernir entre uno y otro.
    ◦ **Hay dos formas de reducir la área solapada de dos distribuciones**: separar las medias de ambas distribuciones más o bien hacer las distribuciones más concentradas hacia su propia media (es decir, reducir su distribución).
    ◦ La distancia entre la media de ambas distribuciones de llama "tamaño del efecto".
    ◦ Separar ambas medias suele ser casi imposible. Sin embargo, hacer las distribuciones más concentradas es más fácil, pues desde el teorema del límite central sabemos que con mayor tamaño de nuestras muestras, la estadística tenderá más hacia la estadística real de la población. Por ende, mayor tamaño de datos, mayor información.
    ◦ Se considera un buen experimento algo que tenga poder estadístico de 80%. Los diseñadores de experimentos escogen un tamaño de muestra tal que el poder llegue a 80%.

[](https://wikimedia.org/api/rest_v1/media/math/render/svg/f9dac77577c2717cbb973388e4d6563915705742)