# 6. Derivadas parciales e integrales dobles y triples

Date de création: January 23, 2021 8:03 AM
Modifié: March 2, 2021 10:39 AM

## Funciones multivariables

- Una función real de n variables es una correspondencia que asigna a cada (x1, x2, x3... xn), perteneciente a cierto conjunto, un único valor: u = f(x1, x2, x3... xn), y lo indicamos así:
    - f: Rn -> R.
- Las variables x1, x2, x3... xn se llaman variables independientes, y la variable u sería la variable dependiente.

## Curvas de nivel

- Las curvas de nivel son una proyección 2d de todas las intersecciones de un plano con valor constante en el eje Z con una gráfica en 3d de una función f(x,y). En pocas palabras, es una isocuanta, pero se suelen mostrar varias isocuantas sobre un mismo plano para distintos valores de Z.

**Derivadas parciales**
• En un modo muy simple, las derivadas parciales funcionan como cualquier otra derivada, tan solo que la función a derivar es una función de dos o más variables y se deriva con respecto a una sola variable nada más. Las otras variables independientes se ignoran como si fueran constantes.
**Derivadas de orden superior**Llamamos segundas derivadas parciales de una función z = f(x,y) a las derivadas parciales de las funciones ∂f/∂x, ∂f/∂y, que se denotan: 
**Extremos de funciones de varias variables**
• Se dice que f presenta en (a,b) un máximo relativo (o local) si se verifica que f(x,y) >= f(a,b) para todo (x,y) perteneciente a cierto disco centrado en (a,b) y de radio no nulo.
• Se dice que f presenta en (a,b) un mínimo relativo (o local) si se verifica que f(x,y) <= f(a,b) para todo (x,y) perteneciente a cierto disco centrado en (a,b) y de radio no nulo.
• Los máximos o mínimos relativos reciben el nombre de extremos relativos (o locales).
• Si fx(a,b) = 0 y fy(a,b) = 0, entonces el punto (a,b) ***PUEDE*** ser un punto extremo. (No necesariamente lo es, a lo menos es un extremo local)
• También es el mismo caso si fx(a,b) o fy(a,b) está indefinida en ese punto (a,b).
**Criterio de la segunda derivada**
• Ese es el hessiano de f. 
• Sea f una función definida en una región abierta R, con derivadas parciales primeras y segundas continuas en R; si (a,b) pertenece a R, con puntos críticos  fx(a,b) = 0 y fy(a,b) = 0, entonces:
**Integrales dobles y triples**
• Así como las integrales de funciones de una sola variable arrojaban el área entre una curva y el eje x, una integral doble arroja el volumen encerrado por una curva y el plano XY.
• Esta idea se puede generalizar a funciones de n variables con integrales triples, cuádruples, etc.
•  La idea es la siguiente: vamos a aproximar el área bajo la curva usando pequeños paralelepipedos, que son los análogos de los rectángulos pero en 3 dimensiones.
• Para ello, primero vamos a dividir el plano XY, que son todas las posibles combinaciones de las variables independientes (x,y), en un gran rectángulo. El área en gris de la imagen de arriba representa el dominio D para el cual la función f(x,y) está definida. El gran rectángulo debe abarcar todos los extremos de la región D.
• Luego, este rectángulo empezamos a dividirlo en rectángulos más pequeños, inifinitesimalmente más pequeños, de hecho. El área de cada sub-rectángulo conforman la partición P.
• **(Mientras más grande sea la partición P, menor es la norma de la partición ||P||)**
• (A(D) en este caso significa el área del dominio, es decir, el área de la área gris de la primera imagen.)
**Propiedades**
• Ayudado por las propiedades de una sumatoria, podemos enunciar:**Integrales iteradas**
• Debido a que calcular el límite de una sumatoria a través de manipulación algebraica es engorroso, también podemos resolver el problema de integrales dobles o triples con integrales iteradas.
• **Teorema de Fubini**: el orden de integración no importa, siempre se llega al mismo resultado.
**Tipos de regiones**Gracias, Fernando.