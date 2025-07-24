# 4. TVM, Polinomios de Taylor y L'Hôpital

Date de création: January 10, 2021 9:13 PM
Modifié: January 12, 2021 3:04 AM

## Teorema del valor medio

- Supongamos una función f que es continua en el intervalo [a,b], y que existe un valor c entre a y b. Entonces, f(c) estará entre f(a) y f(b).
- **Corolario 1**: si f(a) es positivo y f(b) es negativo, o viceversa, entonces existe un valor c entre [a,b] tal que f(c) = 0.
- **Corolario 2**: si *f*  es continua en un intervalo cerrado y acotado [a,b] y derivable en (a,b), existe al menos un épsilon E en (a,b) tal que f'(E) = (f(b) - f(a))/(b -a)

### Teorema de los valores extremos

- Los puntos óptimos de una función son sus máximos y sus mínimos.
- Si *c* es el máximo de *f*, entonces *f(x)* <= *f(c)* siempre.
- Si *c* es el mínimo de *f*, entonces *f(x)* => *f(c)* siempre.

### Teorema de los valores óptimos

- Una función *f* continua en un intervalo [a,b] cerrado y acotado, tiene en él un máximo o mínimo.
    - Si f es discontinua en un punto, no tiene un máximo o mínimo.
    - Si f está definida en (a,b) (no es acotada) y continua, no existe punto máximo ni mínimo.
    - Si f está definida en [a, inf.) y continua, no tiene máximo.
- Si *I* es un intervalo y *c* es un punto interior de *I* (no es ninguno de los extremos) y es un punto óptimo de *f*, y si existe *f'(c)*, entonces *f'(c)* = 0.
    - Los puntos en los que f'(c) = 0 se llaman **puntos estacionarios**.

## Polinomios de Taylor

• Son polinomios basadas en funciones no polinómicas. Los polinomios de Taylor buscan aproximar valores de la función base en un cierto intervalo, alrededor de un cierto valor. Son más fáciles de evaluar, derivar, integrar, etc. Casi siempre el valor deseado es alrededor de x = 0 (y la explicación siguiente va a asumir que es así).
• Los coeficientes de cada término son los "grados de libertad". El grado de libertad "n" del Polinomio de Taylor, de menor a mayor grado de términos,  debe ser tal que el valor de la derivada de grado "n-1" del polinomio sea igual al valor de la derivada de grado "n-1" de la función base en  x = 0 (o en x = valor deseado).
• Añadir nuevos términos de grado mayor a los ya existentes no los cambia.
• Cada derivada de un polinomio en x=0 es controlada por uno y solo uno de los coeficientes.
• Si se tiene un valor deseado distinto de 0, digamos *a*, entonces el polinomio debe escribirse en términos de (x-a) en vez de en términos de x.
**Regla de L'Hôpital**
• Para la forma indeterminada "0/0":
• Errores más comunes:
    ◦ Comprobar que se tiene realmente una forma indeterminada; si no es así, el método da normalmente un resultado equivocado.
    ◦ No debe derivarse f/g como una fracción, sino que se debe calcular f'/g'
• Para formas indeterminadas 0 * inf.:
    ◦ Suponiendo la forma f*g, convertir en f/(1/g). Esto debe quedar en 0/0 o inf/inf.
• Para formas indeterminadas inf.^0, 0^0, 1^inf.:
    ◦ Suponiendo la forma y = f^g, toma el logaritmo natural en ambos miembros de la igualdad y baja el exponente g.
• Para formas indeterminadas inf. - inf.:
    ◦ Suponiendo f - g, convertir en (1/g - 1/f)/(1/fg).