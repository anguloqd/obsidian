# stat. y proba. 3 // probabilidad aplicada

Date de création: July 14, 2021 3:55 PM
Modifié: January 16, 2023 1:07 AM

- Solo porque varios eventos representen la misma proporción de éxito/espacio muestral, no significa que sea igualmente probables todos.
- La regla del complemento P(A) = 1- P(Ac) puede ser útil cuando buscamos P(A) pero es más fácil computar la probabilidad de que Ano suceda.
- Recuerda que la intersección P(A U B) te la dan, normalmente no la sueles determinar, es una constante.
- Usando los coeficientes binomiales en un ejemplo de cara o sello, el coeficiente que recibes es uno de los dos estados. Si quieres saber cuántos lanzamientos de monedas X salen sea cara o sea sello, multiplica el coeficiente por 2.
- Modelando el precio de un título valor, si quisieras tomar la esperanza con probabilidades de este momento y los próximos momentos futuros, tendrías que evaluar todas las posibles combinaciones de subidas y bajadas porcentuales.
- Pon atención a cuando se trate de P(A)P(B|A) y solo P(B|A) (sin que A haya todavía pasado, especialmente indicadores verbales como "y").
- **Biyecciones**: es una forma distinta pero equivalente de ver el problema, equivalente en el sentido que cada solución de un problema se mapea a otro. Ejemplo: cómo distribuir 6 bolas en 6 urnas. Usar la idea de n-1 "separadores" para representar el elemento receptor de la distribución es especialmente útil.

### Teorema de Bayes: un proceso de actualización de creencias, basado en evidencia de hechos pasados

[](https://wikimedia.org/api/rest_v1/media/math/render/svg/87c061fe1c7430a5201eef3fa50f9d00eac78810)

- P(A), conocimiento a priori, es el grado de creencia inicial A.
- P(A|B), conocimiento a posteriori, es el grado de creencia en A suponiendo que la evidencia B es correcta.
- P(B|A) es la verosimilitud.
- El cociente P(B|A)/P(B) representa el soporte que B provee a A.
- P(B) es llamado "marginalización" también.

• "**Evidencia irrelevante no cambia nuestra hipótesis**":
    ◦ Supongamos que tomamos dos muestras: una muestra de la población general (A) y una muestra donde se cumple nuestra evidencia (B).
    ◦ Si la proporción de personas que cumplen con la hipótesis en la misma en A y en B, entonces decimos que la evidencia es irrelevante.
    ◦ Esto implicaría que P(E|H)/P(E) es igual a 1, o lo que es igual, que la proporción de la evidencia que se cumple donde la hipótesis es cierta es la misma proporción que en la población completa.
    ◦ En este caso, el soporte que la Evidencia provee a la Hipótesis no cambia nada, es nula.
**Relación de recursión**
• Un método avanzado contando y calculando probabilidades es la relación de recurrencia.
• La idea general es que escribas el número de resultados (o de probabilidad) después de n pasos como una función (an) de los resultados de los pasos previos, y de allí ir hacia atrás.
• Debes determinar los casos base necesarios, a1 y a veces a2, para poder empezar a usar la función.
• En situaciones de añadir pasos o elementos, abstractamente hablando, puedes contar desde un paso n y contar todas las formas que se puede tomar EL ÚLTIMO PASO antes de llegar a ese paso n. (No confundir con todas las formas de llegar a n pasos, eso no tiene sentido.)
• En situaciones donde tengas que moverte "hacia adelante y hacia atrás" (direcciones contrarias), también te puede servir calcular la distancia esperada en 1 paso.
• "¿Cómo relaciono los casos base (constantes) para obtener el primer caso no-base?"
• NO CONFUNDIR UNA RECURSIÓN PARA HALLAR EL VALOR ESPERADO CON UNA RECURSIÓN PARA ENCONTRAR LA PROB. DE ALGO.
• Los casos base no tienen por qué ser sucesivos, pueden haber dos casos base, uno donde el juego se gana (p=1) y otro donde el juego se pierde (p=0) y pueden estar separados.
**Cadenas de Markov**
• Sistema matemático que sufre transiciones de un estado a otro basado en reglas probabilísticas.
• Característica que la define: no importa cómo el sistema llegó hasta donde está, el futuro solo estará definido por el estado actual y cuánto tiempo o pasos dentro del futuro queremos dar.
**Funciones generadoras**
• La generación de funciones es una forma de asociar eventos con polinomios y reducir los cálculos de probabilidades a cálculos algebraicos. Se entienden mejor con un ejemplo: imagine lanzar un dado justo. La función generadora asociada con este evento es:
    ◦ p(x) = x^6 + x^5 + x^4 + x^3 + x^2 + x
    ◦ donde cada exponente corresponde a un posible resultado, y los coeficientes corresponden al número de formas en que ese resultado puede ocurrir.
• Para ver un ejemplo del poder de las funciones generadoras, considere lanzar dos dados y observar la suma. La función generadora para esto es:
    ◦ p(x) = (x^6 + x^5 + x^4 + x^3 + x^2 + x)^2
    ◦ porque multiplicar polinomios implica sumar los exponentes de los términos y estamos sumando los resultados de los dos dados.