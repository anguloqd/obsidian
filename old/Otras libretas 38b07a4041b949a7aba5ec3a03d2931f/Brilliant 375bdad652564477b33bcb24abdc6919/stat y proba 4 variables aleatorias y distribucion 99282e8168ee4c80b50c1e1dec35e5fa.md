# stat. y proba. 4 // variables aleatorias y distribuciones

Date de création: July 31, 2021 10:51 PM
Modifié: January 16, 2023 1:07 AM

# Variables aleatorias

- Las VA son una FUNCIÓN que asigna un valor numérico a cada resultado de un experimento aleatorio. No son lo mismo que los experimentos que cuantifican.
- Por su parte, las distribuciones asignan una probabilidad a cada uno de los resultados posibles.
- Distribución "uniforme": distribución donde todos los valores posibles tienen exactamente la misma probabilidad de ser resultado.
- Esperanza usando la distribución binomial:
- Fórmula fácil para varianza: (E[X2] significa p * q2.) La probabilidad queda igual, las cantidades se elevan al cuadrado.
- 
- Aunque la fórmula de esperanza y varianza están ambas definidas en términos discretos, puedes reemplazar la sumatoria con un integral para obtener la versión continua, suponiendo que el rango de la variable aleatoria es continuo. Ambas funciones en versión continua funcionan igual de bien.
- Una variable discreta uniformemente distribuida no puede existir en un rango infinito (viola la regla de que la suma de probabilidades es igual a 1).

## Cosita sobre la independencia de variables

- Dos variables son **independientes** si: (prestar atención al "y")
- Y dos variables son **dependientes** si: (prestar atención al "o")
- Básicamente, si imaginas los conjuntos de cada variable, la independencia es cuando no hay elementos en común entre una variable y otra,
- Mientras que, con los eventos dependientes, si hay una solapa entre un evento y otro.
- Pensando en el problema de "si una familia tiene dos hijos y uno de ellos es macho, ¿cuál es la p. de que el otro hijo sea macho?"
    - Si filtraras las familias con dos hembras, y con las familias restantes seleccionaras una al azar, la p. de que ambos hijos de tal familia sean macho es 1/3.
    - Piensa en la idea de filtrar, y luego seleccionar al azar.

## Esperanza

- Esperanza de X: el valor promedio que X toma.
- Además de la linealidad de la esperanza, también existe E[XY] = E[X]*E[Y] **bajo la condición de que ambas variables sean independientes**.
- Hay casos se combina esperanza con distribución binomial. Es decir, x es el valor que puede tomar la VA y p sería de la forma de distribución binomial.
    - Es decir: (n escoge k)*(p. de éxito)^k*(p. de fracaso)^(n-k)
- Esperanza y varianza de VA de Bernoulli: p y p(1-p).
- Esperanza y varianza de VA Binomial: np y np(1-p).
- (Estas últimas dos se pueden derivar usando la linealidad de la esperanza y el hecho de que la VA Binomial es la suma de las VA de Bernoulli, asumiendo que los ensayos de Bernoulli son independientes)

## Esperanza condicional

- Esperanza de X, dado a que Y = y:
- Ley de la esperanza iterada: calcular E[X] con E[X|Y]:
- Si te confunde que una Esperanza esté metida dentro de otra, tienes que saber que E[X|Y] es una VA construida de otra VA.
- La primera imagen se lee "la esperanza de la esperanza condicionada de X dado Y". Operando de adentro hacia afuera, primero recorremos a X en su espacio muestral condicionado a Y, y luego recorremos Y en su espacio muestral.
- Piénsalo así, la esperanza puede tomar un valor de un conjunto de valores, y cada uno de estos depende de la condición que Y tomó, es decir, de cuál de los valores que Y puede tomar Y tomó.

# Distribuciones

## Cositas sobre Bernoulli y Distribución Binomial

- Una VA de Bernoulli es el tipo de VA más sencillo que existe. Básicamente, X solo puede tomar dos valores (los resultados de un ensayo de Bernoulli): éxito o fracaso, cada uno con su propia probabilidad, no necesariamente 50/50.
- Una VA binomial, por su parte, es una VA que cuenta el número de éxitos (x) en una cantidad (n) de ensayos sucesivos e independientes en un proceso de Bernoulli, al final es (n choose x).
- Solo para aclarar:
    - Un ensayo/experimento es una situación de donde se obtiene un evento/resultado (éxito/fracaso, por ejemplo, en el caso de los ensayos de Bernoulli).
    - Un proceso es una secuencia de ensayos idénticos. Es la generalización de un ensayo de Bernoulli.
- De esto se deriva que la VA Binomial es la suma de las VA de Bernoulli. Es decir, X = X1 + X2 ... + Xn. (Recuerda que X ya cuenta un resultado, como el número de caras, por ejemplo).

### Cosita sobre la distribución normal

- Las principales propiedades son que la distribución normal es simétrica con respecto a su mediana y disminuye en ambas direcciones desde ese punto. Aunque esto también es cierto para otras distribuciones, estas señales a menudo son suficientes para concluir que la distribución normal es una buena aproximación.

## Distribución de Poisson, comparaciones con Distribución Binomial

### Distribución de Poisson

- ¿Por qué se creó? **Para predecir los números de eventos que ocurrirán en el futuro**.
- Expresa, a partir de una razón de eventos promedios (eventos/intervalos de tiempo, **λ**), la probabilidad de que ocurra un número de eventos (k) durante un período de tiempo.
    - Concretamente, se especializa en la probabilidad de ocurrencia de sucesos con probabilidades muy pequeñas, o sucesos «raros».
- 
- Condiciones: BEIII.
    - **Binariedad**: un evento debe necesariamente ocurrir o no ocurrir (no existen "medios" eventos).
    - **Esperanza**: el número de eventos que se producen en promedio durante una ventana de tiempo (unidad: eventos/tiempo) es conocido y es **constante**.
    - **Independencia**: todos los eventos son independientes.
    - **Identicidad**: la probabilidad de que un evento suceda en una ventana de tiempo debe ser el mismo para el resto de ventanas de tiempos.
    - **Ilimitación**: no hay límite para el número de eventos que pueden ocurrir en una ventana de tiempo.
- Es una función que solo toma k como argumento, pues lambda será el promedio conocido. K será el número de eventos a observar.
- Poisson es tal que su promedio es **λ** y su varianza también es **λ**.

### Comparación con Distribución Binomial

[Untitled](Untitled%20654c60385600410f98e9e60d65f54ce7.csv)

- Poisson se deriva de la Binomial, bajo la limitación de esta última de solo poder contener un éxito o ningún éxito en una oportunidad (ensayo de Bernoulli).
- Lo que se quiere es aumentar la cantidad de ensayos de Bernoulli contemplados a cambio de reducir la probabilidad de un éxito ocurriendo en cada oportunidad.
    - Formalmente, n (cantidad de ensayos) va a tender al infinito. Como p = (cantidad de ensayos exitosos)/(cantidad de ensayos), es decir, p = **x/n**, entonces cuando n tiende al infinito, p tiende a 0.
    - Esto tiene sentido, pues si consideramos una probabilidad más pequeña de éxitos en una mayor cantidad de ensayos, en el práctica, deberíamos tener la misma cantidad de éxitos.
    - Al aumentar nuestra unidad de tiempo (cantidad de ensayos) dividiéndola en partes más pequeñas, **la cantidad de éxitos que puede contener la unidad de tiempo original se vuelve más y más grande**. Infinita, de hecho.
- Además, no necesitas saber el número de ensayos (n) ni la prob. de éxito (p) con Poisson, pero sí con la Binomial. Con Poisson solo necesitas saber el número de éxitos esperados (la esperanza de x, que es lo que se llama Lambda). **En la vida real, es más probable saber el número de éxitos esperados durante una unidad o intervalo de tiempo** que saber ambos n y p.

### Detalles de Poisson

- Aunque la distribución de Poisson modela eventos raros, la tasa **λ** puede ser cualquier número. No siempre tiene que ser pequeño.
- La distribución de Poisson es asimétrica: siempre está sesgada hacia la derecha. Porque está inhibido por la barrera de ocurrencia cero (no existe tal cosa como aplauso "menos uno") a la izquierda y es ilimitado en el otro lado.
- A medida que **λ** se vuelve más grande, el gráfico se parece más a una distribución normal.

![](https://miro.medium.com/max/650/0*0yOpVu-XurirwRz0.png)

### Derivación de Poisson a partir de la Binomial

![](https://miro.medium.com/max/1400/1*rpKNeMOa958cxXphXmVorQ.png)

![](https://miro.medium.com/max/788/1*95iTlzLQlC5yf_6WY9cPlA.png)

## Distribución Exponencial

- ¿Por qué se creó? **Para predecir el tiempo que va a pasar hasta conseguir el siguiente éxito.**
- Si los números de éxitos en una unidad de tiempo siguen una distribución de Poisson, entonces el tiempo entre un evento y otro sigue una distribución Exponencial.
- X ~ Exp(**λ**), donde **λ** es el número de eventos por unidad de tiempo, lo mismo que con Poisson.
- 
- Sin embargo, cuando la variable x de Poisson va a tomar el valor de cantidad de eventos, la variable y en la Exponencial va a tomar el valor de cantidad de unidades de tiempo.
- La inversa de **λ es importante en la Exponencial.**  λ suele expresar una razón (eventos/unidad de tiempo) en términos de **eventos**, mientras que 1/λ expresa una razón (unidad de tiempo/eventos) en términos de tiempo.
    - Si suelen pasar 5 carros por hora en una autopista, quiere decir que suelen pasar 0.2 horas por cada carro que pasa en la autopista.
- La variable y tiene que estar en términos de la media λ (pues la media contiene la unidad de tiempo), es decir, λ = 1 y la variable y será una fracción (propia o impropia) de λ.

### Detalles de la exponencial

- Media o esperanza: 1/λ
- Varianza: 1/(λ^2)
- Probabilidad de distribución acumulada: 1 - e^(-λy)
- Posee la propiedad de pérdida de memoria. Es decir, no importa cuanto tiempo haya pasado sin un éxito, la P(éxito) será siendo la misma. OJO, si un evento a modelar no cumple con la propiedad de pérdida de memoria, no deberías modelarla con la exponencial.
- Es un **caso especial de la distribución gamma**.
- Es la versión continua de la distribución geométrica, donde el "tiempo" allí son los casos de fracaso antes del primer (y único) éxito.

### Derivación de la exponencial a partir de Poisson

- Primero, debemos darnos cuenta de que la cantidad de tiempo *antes* de que el evento ocurra (sin contar el intervalo de tiempo cuando ocurre) es lo mismo que la cantidad de tiempo durante el cual no ha habido ningún éxito. Es decir, donde el k en la distribución de Poisson es 0, sin haber fijado λ.
    
    ![](https://miro.medium.com/max/1400/1*K10vrJHBdWAqxdKBQD5xJw.png)
    
- Luego, hay que aclarar que el tiempo en el que k eventos de Poisson suceden (en este caso, 0 eventos de Poisson), es considerado 1 unidad de tiempo. Puede ser una hora, un día, un año, etc.
- Con esto dicho, si queremos modelar "nada sucede durante una duración de tiempo t", podemos romper "t" en términos de nuestra unidad de tiempo.
    - Es decir, P(nada sucede durante unidad de tiempo #1) * P(nada sucede durante unidad de tiempo #2) ... P(nada sucede durante unidad de tiempo #t).
    - Cada uno de esos términos es simplemente igual a e^(-λ), y todos juntos son igual a e^(-λt).
    - Esto también asume que, durante todas las unidades de tiempo contempladas, λ es exactamente el mismo y no cambia.
- Entonces, si P(haya un éxito en cualquier momento después de t unidades de tiempo) = P(ningún éxito durante t unidades de tiempo) = e^(-λt), entonces 1 - e^(-λt) es P(haya un éxito en t unidades de tiempo o menos). Esta última probabilidad es la que nos importa.
- Luego, podemos ver que 1 - e^(-λt) es una función de probabilidad acumulada, por lo que su derivada es la función de distribución de probabilidad que nos importa.
    
    ![](https://miro.medium.com/max/788/1*oMbmNib0eyFgmK5ByPSM2w.png)
    

## Distribución Gamma

- ¿Por qué se creó? **Para predecir el tiempo que va a pasar hasta conseguir el éxito k-ésimo.**
- La diferencia con la distribución Exponencial es que esta modela la P. del tiempo hasta el próximo éxito o evento, mientras que Gamma modela la P. del tiempo hasta el éxito #k, el cual incluye el primer éxito.
- Al igual que la Exponencial, la variable independiente en Gamma indica cantidad en unidades de tiempo.
- 
- Ambas parametrizaciones son válidas. (parámetro de forma, parámetro de escala)
    - (k, θ) es preferida en Brilliant, donde θ es el recíproco de **λ**, es decir, 1/λ, la razón de tiempo sobre eventos. k es el k-ésimo evento a alcanzar.
    - (α, β) usa λ tal cual como es concebida en los procesos de Poisson (razón de eventos), pero bajo el nombre de β. α es el k-ésimo evento a alcanzar. Es también más fácil de integrar.
    - Los nombres (parámetro de forma, parámetro de escala) son malos nombres, pues ambos parámetros afectan la "forma" y la "escala".
    - Es mejor pensar en ellos como (n° de eventos, razón de eventos).
- La función Gamma en el denominador es equivalente a (k-1)!. Es más compacto escribir Gamma.
- 
- Por otro lado, la función "omega" es realmente la función Gamma incompleta en el límite superior, donde s es el número de eventos a observar y x es la razón de eventos.
- 
    
    [](https://wikimedia.org/api/rest_v1/media/math/render/svg/7abac264da34df925741f2bcd2f6cd3d4d3fdd69)
    

### "Forma" y "escala"

![](https://miro.medium.com/max/720/1*nrE_-jIF55z7HeLfk2LwBw.png)

- Si fijamos λ y jugamos con k (α), un mayor k-ésimo evento a esperar moverá la "joroba" de la curva a la derecha, pues hay que esperar más tiempo para observarlo y una razón de eventos constante eventualmente será abrumada y se convertirá poco en comparación a k.

![](https://miro.medium.com/max/1280/1*ubzNdUoZxANPABlfBrBEWQ.png)

- Si fijamos k (α) y jugamos con λ, hacer más grande a λ (razón de eventos por unidad de tiempo) reducirá el número de espera para observar k eventos, por lo que se moverá la joroba de la curva a la izquierda.

### Detalles de la Gamma

- Media: kθ
- Varianza: kθ2
- Cuando el k-ésimo evento a observar es un número natural, obtenemos una "Distribución de Erlang". La razón de eventos puede seguir siendo real.
- Gamma(1, λ) = Exponencial(λ).

### Derivación de la Gamma

- Sea T una VA representando la cantidad de tiempo que toma para que k eventos ocurran. Empezamos desde la función de probabilidad acumulada.

![](https://miro.medium.com/max/788/1*V6m8vlPMzIG9pmFdcNZ26Q.png)

- Procedemos ahora a diferenciar:

![](https://miro.medium.com/max/1400/1*2X-mPjWyKOtdH9wn6Pc2Fg.png)

![](https://miro.medium.com/max/788/1*EHfLw-nfB3pRfW4qb2GCow.png)

## Distribución Log-Normal

• Si una variable aleatoria X se distribuye de tal manera que, al tomar el logaritmo de cada valor de X, obtenemos una distribución normal, entonces X se distribuye de manera log-normal.
• La forma (μ + σZ) es la inversa de la fórmula de estandarización de valores, (Z-μ)/σ. Si la segunda expresión se utiliza para transformar un valor de una dist. normal (μ, σ2) a una normal (0, 1), la primera hace lo contrario. Es una forma más fácil de expresar una distribución normal sin la mega formulota.
**Detalles de la Log-Normal**
• Media o esperanza: exp(μ + σ2/2)
• Varianza: [exp(σ2) - 1]*exp(2μ + σ2) // o bien [exp(σ2) - 1]*E[X]2
• 50% de los datos (área bajo la curva) estará siempre entre 0 y 1.
• Mover μ moverá la "joroba" de la curve hacia la derecha, y un σ más grande o más pequeño hará la curva más dispersa o más concentrada, respectivamente.
• Distribución usualmente usada para modelar los precios de una acción o título valor.
**Derivación de la Log-Normal**
• Empecemos tomando muestras de la distribución normal. Esta puede ser estándar o no. Se escribe de la forma (μ + σZ), donde Z es estrictamente una VA normal estándar.
    ◦ (Nota que, si quisiéramos samplear directamente desde una ~N(0,1), establecemos (μ = 0, σ = 1) y quedaríamos solamente con Z.
• Luego, tomamos cada observación de la muestra y los pasamos por la función ex.
• Nota que, como nuestra muestra puede ir de (-inf., +inf), cuando reemplazamos en ex, en teoría, el valor que podríamos tener podría ser tan grande como quiera, pero lo más pequeño que puede ser es casi 0. **Mira las fotos abajo para apreciar la condensación**.
• Todos los valores negativos de nuestra muestra normal estarán condensados en el recorrido de ex en (0, 1).
• Todos los valores positivos, por su parte, irán desde (1. +inf.).
• Una vez hayamos pasado todos las observaciones, hacemos un gráfico y veremos que el gráfico se distribuye lognormalmente.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Lognormal_Distribution.svg/1280px-Lognormal_Distribution.svg.png)

![](https://miro.medium.com/max/1314/1*Z2bA1Bzwc9r4EYu09nu9tg.png)

![](https://miro.medium.com/max/1314/1*PBpTfoOFxrileU5we1-iOw.png)

![](https://miro.medium.com/max/1314/1*YVCiC7DLCf_Rr1zo-nxm1Q.png)

![](https://miro.medium.com/max/1314/1*P_E4Wr7Q4ohJhGj2UhWwiA.png)