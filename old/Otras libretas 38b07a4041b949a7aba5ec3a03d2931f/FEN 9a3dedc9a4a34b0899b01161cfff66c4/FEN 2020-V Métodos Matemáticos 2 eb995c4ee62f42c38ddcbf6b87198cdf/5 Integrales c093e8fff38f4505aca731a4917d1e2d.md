# 5. Integrales

Date de création: January 18, 2021 1:26 AM
Modifié: March 18, 2022 9:36 PM

- Un integral es la antiderivada de una función f(x). Es decir, si suponemos una función F(x) y la derivamos, nos quedamos con f(x). Por consiguiente, es el proceso contrario de derivar.

• Dos antiderivadas cualesquiera de una función difieren solo en una constante.
• Si se pide que la función derivada sea igual a un número para un cierto valor de x, entonces se puede determinar el valor de C. A esto se le llama **condición inicial**.
**Regla de la potencia para integración**
• Evidentemente, **también tienes que considerar a dx y du y cualquier diferencial en la substitución.**
• Deberías fijarte si en el integrando hay 2 polinomios distintos pero que los grados de sus términos están intercalados, pues puede que uno sea la derivada de otro después de un uso de la regla de la cadena (y con otra modificación de operación siguiente).
**Caso de integral de 1/x**
• Si intentáramos usar la regla anterior mencionada, entonces quedaríamos con (x^0)/0, lo cual es una indefinición.
• En concreto, la antiderivada de 1/x es ln(|x|). Las barras de valor absoluto son necesarias puesto a que el argumento de ln() debe ser siempre positivo.
**Técnicas de integración**
• División antes de la integración:
    ◦ Ya sea simplificando o usando división de polinomios.
• Funciones de la forma au:
    ◦ 
**Teorema del valor medio del cálculo integral**
• Si tenemos una función definida en un intervalo [a,b], el área limitada por la función y los rectas x=a y x=b es la siguiente:
• Pues bien, existe un punto c, entre los puntos a y b, donde la función en ese punto tiene un valor de f(c):
• Se puede formar un rectángulo cuya base es la longitud del intervalo [a,b], es decir, b-a y la altura es la longitud correspondiente al valor de la función en el punto c, es decir f(c)
• El área de este rectángulo es igual al área encerrada por la función y los puntos de abscisa a y b, por lo que:
• Donde (b-a).f(c) corresponde al área del triángulo y **f(c)** corresponde al **valor medio** de la función f(x) en ese intervalo (o también lo puedes encontrar como altura media) y el **punto c** es el punto donde se alcanza dicho valor.
**Teorema fundamental del cálculo**
• Normalmente a > b. En el caso de que b > a, entonces se invierten los extremos (límites de integración) y el resultado del final se multiplica por -1.
• El área bajo un punto es siempre igual a 0.
**Propiedades de las integrales definidas
Integración por partes (deshacer la regla del producto)**
• Si el función está difícil de integrar, quizá sea mejor integrar el int(vdu), que es todo el punto de la función.
• Esta fórmula expresa una integral, en términos de otra integral, que puede ser más fácil de integrar.
• Normalmente la función base suele ser un producto de funciones.  Especialmente cuando la derivada de una función *f'* está escrita en término de la función original *f*.
    ◦ De la forma y' = ky.
• Para aplicar la fórmula a una integral dada debemos escribir f(x) dx como el producto de dos factores (o partes) escogiendo una función u y una diferencial dv tales que f(x) dx=udv.
• Sin embargo, para que la fórmula sea útil, debemos ser capaces de integrar la parte seleccionada como dv.
**¿Integración U-Sub o por partes?**
• Como regla general, intenta siempre primero la u-sub y, si no, integra por partes.
• La u-sub se usa cuando el integrando contiene a una función de g(x) y tal función está multiplicada por g'(x). -> ∫f(g(x))g′(x)dx.
    ◦ Otra forma de verlo es que se usa para funciones que pueden ser reescritas como el producto de una segunda función con su derivada. -> ∫udu.
• La integración por partes se usa cuando se tienen dos funciones de x, una que se puede integrar y la otra que se puede diferenciar. (que es el ∫vdu del final)
    ◦ Otra forma de verlo es que se usa para funciones que pueden ser reescritas como el producto de una segunda función con la derivada de una tercera función. -> ∫udv.
**
Integración por medio de fracciones parciales**
• La integración con fracciones parciales se hace con funciones racionales propias (Grado del numerador menor al del denominador).
• Cuando separes en fracciones, **el grado(arriba) debe ser SIEMPRE un grado menor que grado(abajo)**.
• **Caso 1: fracción impropia. grado(arriba) >= grado(abajo).**
    ◦ Solución: haz división polinomial larga. DETENTE CUANDO GRADO(RESTO) < GRADO(ABAJO), luego el último término es resto/abajo. Finalmente, distribuye el integral entre los términos resultantes.
• **Caso 2: factores lineales distintos en el denominador.**
    ◦ Solución: separa la fracción en varios términos fraccionales con fracciones parciales haciendo un sistema de ecuaciones.
• **Caso 3: factor cuadrático en el denominador IRREDUCTIBLE.**
    ◦ Solución: separa la fracción en términos fraccionales y, el numerador con el denominador cuadrático, debe ser lineal y no constante. (Ax + B)
• **Caso 4: factores repetidos en el denominador (cuadráticos o mayores).**
    ◦ Solución: ve acumulando los factores del factor repetido. O, simplemente, el factor repetido lo separas en su fracción y su denominador debe ser un grado menor, luego separas tal fracción.
**Integrales impropias**
• Un integral impropio es simplemente un integral con un límite de integración que tiende al infinito o al menos infinito. Se toma el F(b) - F(a) y, suponiendo que el b tiende al infinito, se expresas como tal límite.
• Un integral del menos infinito al infinito puede expresarse como un integral del [-inf., 0] + [0, inf.].

![](https://ekuatio.com/wp-content/uploads/valor-medio-16-1.png)

![](https://ekuatio.com/wp-content/uploads/valor-medio-17-1.png)

![](https://ekuatio.com/wp-content/uploads/valor-medio-18-1.png)

![](https://ekuatio.com/wp-content/uploads/valor-medio-1-1.png)