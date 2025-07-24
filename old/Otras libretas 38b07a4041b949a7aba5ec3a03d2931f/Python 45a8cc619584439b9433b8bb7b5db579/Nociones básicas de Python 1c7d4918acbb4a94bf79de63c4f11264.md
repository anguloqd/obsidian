# Nociones básicas de Python

Date de création: December 5, 2020 11:03 PM
Modifié: August 26, 2022 10:47 PM

<aside>
💡 Tabla de contenidos

</aside>

# Variables

---

Son como "cajitas" en donde guardas información. En realidad, es un espacio en la memoria RAM. El valor asignado a guardar se hará con un símbolo de igualdad. Un ejemplo es: `x = 3`, donde ahora la variable `x` tiene el valor 3.

Las variables adquieren un "tipo", una clasificación, según su contenido. Existen varias, pero las básicas son:

- `str` (string): es una cadena de texto. Suele estar entre comillas simples o dobles.
- `int` (integer): números enteros.
- `float`: número decimal (los decimales se representan con puntos, no con comas).

Para saber el tipo de una variable, se puede usar la función type de la siguiente forma: `type(x)`. Asumiendo la misma variable de antes, la función debería devolver que es una variable `int`.

# Expresiones numéricas

---

Se pueden hacer operaciones matemáticas entre números y también variables. Sigue el orden matemático de PEMDAS.

- `+`: suma.
- `-`: resta.
- `*`: multiplicación.
- `/`: división.
- `**`: exponenciación.
- `%`: resto.

# Operaciones y propiedades de los textos (strings)

---

Se pueden hacer operaciones con las cadenas de texto. Algo que se debe saber es que, en Python, se empieza contando desde el número 0, no el 1. Supongamos:

```python
strej = "hola"
```

- **Acceso a carácter por su posición**. se usan corchetes después del nombre de la variable. Ej.: `strej[0]` nos devolvería `"h"`.
    - **Índices negativos**: también se pueden usar índices negativos (el número dentro de los corchetes) para acceder a un carácter de adelante para atrás. Ej.: `strej[-1]` devolvería `"a"`. Los índices positivos comienzan desde el 0, mientras que los índices negativos comienzan desde el -1.
- **Largo de un texto.** La función `len()` devuelve el largo de una variable (incluso si no es str.) EJ.: len(strej) devolvería 4.
- **Acceso a un rango de caracteres por posición.** Al igual que con los caracteres individuales, podemos acceder a rangos de caracteres. Ej.: `strej[0:2]` devolvería `"ho"`. Lo importante es que los corchetes representan un intervalo [a:b] semi-abierto: se empieza a contar desde a y se termina en b - 1, el carácter antes de b.
    - Si se escribe `[:b]`, entonces se empezará desde el primer carácter de la str.
    - Si se escribe `[a:]`, se terminará en el último carácter de la str.
    - `[:]` devuelve todos los caracteres.
    - Se pueden usar índices negativos en los rangos.
    - Se pueden anidar búsquedas: `strj[0:3][0:1]`.
- Se pueden concatenar strings con el signo `+`. Obviamente, todos los valores o variables presentes en la operación deben ser strings. Ej.: `"hola" + "chao"` devolverá `"holachao"`.
- El método `.lower()` devolverá la string en minúsculas, y el método `.upper()` en mayúsculas.

# Cambiar el tipo de variable

---

Para ello, se debe llamar al función que devolverá el tipo de variable de llegada. Son útiles para hacer operaciones con variables de tipos distintos que deben ser iguales.

- `str()` para cadenas de texto.
- `int()` para números enteros.
- `float()` para decimales.
- Y más. Cada tipo de variable tiene su función de conversión a ese tipo.

# Operaciones booleanas

---

Son operaciones que devuelven `true` o `false`. Los operadores a continuación hacen la preguntan y devuelven la respuesta.

- `==` pregunta si a es igual a b. (No confundir con `=`, que es para asignar valores a variables). Sirve con str y números.
- `>`, `<`, `>=`, `<=`.
- `!=` pregunta si a es desigual de b.
- Se puede preguntar si un carácter está presente en una cadena de texto. Ej.: `is "h" in strej` (”hola”) devolvería true.
- Se puede preguntar lo contrario con `not in`.

# Listas

---

Se pueden tomar varios valores o variables cualesquiera y hacer una lista con ellos. La lista se define como otra variable. Se pueden crear vacías o con elementos ya adentro. Supongamos:

```python
listaej0 = []
listaej1 = ["hola", "como estas", 1, 2, 3.14]
```

- Se pueden referenciar objetos en una lista al igual que en una str. Ej.: `listaej1[1]` devolvería `"como estas"`.
- Se pueden hacer listas de listas. Ej.: `listaej2 = [listaej0, listaej1]`.
- **Agregar objetos a listas**. Se hace con el método `.append`.  `listaej0.append("bien y tu?")` agregaría a `listaej0` el valor `"bien y tu"` al final de la lista.
- **Agregar objetos a listas en cierta posición**. Método `.insert`. `listaej0.insert(0, "buenos dias!")` devolvería `["bien y tu", "buenos dias!"]`.
- **Editar objeto de una lista**. Se hace con la lógica de la asignación. `listaej0[1] = "buenas noches!"` devolvería `["bien y tu", "buenas noches!"]`.
- **Encontrar el índice de un objeto**. Método `.index`.  `listaej0.index("buenas noches!")` devolvería 1.
- **Borrar objeto de la lista**. Función `del()`.  `del(listaej0[1])` devolvería `[”bien y tu”]`.

# Estructuras de control iterativo

---

"Iterar" significa repetir. En Python, se pueden hacer tareas repetitivas rápido. Dos herramientas son los ciclos o loops: loops `for` y loops `while`.

## Ciclos `for`

---

El ciclo `for` necesita de una lista para funcionar. Una estructura ejemplo es la siguiente:

```python
mercado = ["tomate", "cebolla", "lechuga"].
for elemento in mercado:
	# (definir acción aquí)
```

En este caso, el ciclo for creará en primer lugar una variable cuyo nombre es "elemento" y le asignará la string "tomate". Luego, empezará a hacer las acciones especificadas (deber estar indentadas). Cuando termine de hacer las acciones, el ciclo empezará de nuevo.

```python
**for** elemento **in** mercado: 
	a = 5
	b = 2
	print(a*b)
	print(elemento)
```

El ejemplo anterior, en cada iteración, asignará 5 a `a`, 2 a `b`, los multiplicará, los imprimirá y también imprimirá el valor que tomó `elemento` en esa iteración. No necesariamente se necesita usar la variable dinámica `elemento` en las acciones. Se puede repetir una acción las veces que se quiera sin usar la variable dinámica.

También se pueden usar la función `range` para hacer listas rápidamente sin tener que hacerlas antes.

- `range(20)` creará una lista con números del 0 al 19 (20 números en total).
- `range (5, 20)` creará una lista con números del 5 al 19.
- `range(5, 20, 5)` creará una lista con números del 5 al 19 saltando de 5 en 5 (es decir: 5, 10, 15. No se incluye el 20).

```python
**for** elemento **in** range(20):
**print("hola") # aquí se imprimirá "hola" 20 veces.
```

Otras cosas con respecto al ciclo `for`:

- Los ciclos `for` se pueden anidar.
- Una vez empiece el ciclo, y suponiendo que la lista estaba determinada antes (como la lista "mercado"), no podemos modificar los elementos de la lista durante las acciones dentro del ciclo. **Cuando comienza el ciclo, la lista de referencia es inmodificable**.
- Puedes hacer un ciclo `for` con dos variables dinámicas simultáneas que se mueven en una lista de listas, donde las sublistas tienen dos elementos. Por ejemplo:
    
    ```python
    for x, y in [[0,a], [1,b], [2,c]]:
    	# asignaría los números a "x" y las letras a "y", según el orden en el que se pongan en la keyword "for".
    ```
    

## Ciclos `while`

---

El ciclo `while` funciona al indicarle en primer lugar una condición (verdadero o falso) y luego ejecutando las acciones. Ejemplo:

```python
x = 4

while x < 10:
	print(x)
	x += 1
```

Estas instrucciones imprimirán el valor de `x` y luego le sumará 1. Esto se repetirá hasta que `x` ya no sea menor que 10, por lo que el ciclo se detendrá.

- **Cuidado**: el ciclo while puede seguir infinitamente si nunca se cumple la función.
- Sí se puede cambiar el valor de la variable indicada en la condición del ciclo, la variable “referencia” (en diferencia de la lista referencia en el ciclo `for`).
- Se pueden anidar los ciclos `while`.

## `Break`, `continue`, `pass` (*)

---

Estos comandos actúan con los ciclos mencionados, y también con otras afirmaciones como `try` y `except`.

- `break` hará que se rompa el ciclo.
    
    ```python
    for nro in lista:
    
    	if nro == 2:
    	break
    
    	print(nro)
    ```
    
    En estas instrucciones, cuando `nro` sea igual a "2", el ciclo se romperá y no continuará. En funciones anidadas, se romperá el ciclo más cercano a `break`.
    
- `continue` hará que se pase al caso siguiente del ciclo sin que se lleven a cabo las instrucciones después de él.
    
    ```python
    for nro in lista:
    	
    	if nro == 1:
    		continue
    
    	print(nro)
    ```
    
    Aquí solo se imprimirán "0" y "2", pues cuando llegue al valor "1", el condicional se activará y se pasará al siguiente caso del ciclo sin imprimirlo.
    
- `pass` simplemente es una función nula. No hace nada. Es útil para llenar afirmaciones que necesitan de una instrucción sí o sí y no pueden estar vacías, pero tampoco queremos que hagan nada.

# Estructuras condicionales

---

Son palabras claves que ejecutan una acción si y solamente si una proposition es verdadera. Las estructuras condicionales son `if`, `elif` y `else`. Otra estructura condicional un poco más avanzada es el bloque `try`, junto con las keywords `except`, `else` y `finally`.

## `if`, `elif` y `else`

---

Los condicionales llevan a cabo ciertas instrucciones si se cumple una condición. Principalmente se hace con `if`, y se complemente con `elif` y `else`.

```python
x = 4

if x == 4:
	print(x)
```

Aquí simplemente se imprimirá "4" porque se cumple con la condición. Si x = 5, no se imprimiría.

Los complementos condicionales `elif` y `else` se usan así:

```python
x = "str"

if x == 4:
	print(x)

elif x < 5:
	print("menor a 5")

elif x > 5:
	print("mayor a 5")

else:
	print("error!")
```

Esas instrucciones terminarán imprimiendo `"error!"` porque `x` no es igual a 4, ni menor, ni tampoco mayor.

- En los condicionales, solo puede haber un comando `if` y `else`, aunque sí pueden haber varios comandos elif.
- `elif` requiere que se especifique otra condición, mientras que else simplemente funciona cuando ninguna de las condiciones anteriores se cumplió.
- Si se llegasen a cumplir dos condiciones con comando `elif`, solo la primera condición `elif` de arriba hacia abajo se activaría, la segunda ni las subsiguientes no.
- Se pueden usar conectores lógicos en el comando `if` y `elif` como `and`, `or`, `is`, `not`, etc.

## `try`, `except`, `else` y `finally` (*)

---

El bloque `try` ejecutará un código específicado. Si el código arroja un error, se empezará a ejecutar el bloque `except`. Si no tira un error y todo fluye bien, se ejecutará el bloque `else`. Finalmente, independientemente de si se ejecutó `except` o `else`, se ejecutará el bloque `finally`.

```python
x = 1

try:
	print(x)
	
except:
	print("hubo un error: la variable no estaba definida")

else:
	print("todo bien!")

finally:
	print("fin!!")
```

El bloque `except` será el único que no se ejecutará en este ejemplo, el resto sí, pues no hubo error.

- El bloque `except` también puede activarse con solo un tipo de error en vez de un error cualquiera. Por ejemplo, `except TypeError:` solo se activaría con un error del tipo `TypeError`.
- También puedes arbitrariamente soltar un error fuera de una estructura condicional `try` y con una `if`. La función `raise x`, donde `x` es el nombre de un tipo de error, arrojará un error si se cumple la condición del If de arriba. Ej.: `raise TypeError("el input no puede ser float")`.

# Definir funciones propias

---

Python normalmente funciona con funciones ya integradas ("built-in functions") a menos a que definamos nosotros funciones propias. Para hacerlo, recurrimos al comando `def`. Funciona así:

```python
def mifuncion(x, y):
	nro0 = x*5
	nro1 = y*2
	nro2 = x + y
	return nro2
```

Esta función tiene dos argumentos, `x` e `y`. Tales variables tomarán los valores que se pongan ahí cuando se llame la función. Luego procederá a hacer las acciones especificadas y devolverá lo que se especifique con el comando `return`.

En la función de ejemplo, puede haber un error si se especifica una string, por ejemplo, por lo que hay que manejar ese tipo de situaciones.

Para argumentos opcionales, se tendrían que especificar como `mifuncion(x, y, z)` y, si z está vacío o `null`, asignarle un valor predeterminado.

# (*) Clases y objetos

---

- **Objeto**: una colección de propiedades que pueden ser expresadas como variables (*instances variables* o *attributes*) y funciones (*methods*) que ya tienen valores asignados. Con tal colección, un objeto busca representar una "cosa". Las funciones en la colección buscan demostrar qué es lo que esa "cosa" puede hacer (accionar como caminar, dormir, hablar, etc.)
- **Clase**: es la “estructura” del `objeto` **sin** valores asignados (o el "plano" como en una analogía de una estructura arquitectónica ej.: una casa). Se utiliza para crear "cosas" parecidas y del mismo tipo a una "cosa" ya creada, pero con distintos valores en sus propiedades/atributos/variables.
- **Constructor**: es una función que permite construir la estructura de las variables de un objeto.

```python
class comida:

	def __init__(self, color, sabor):
		self.color = color
		self.sabor = sabor
	
	def esRico(self):
		if self.sabor == "dulce":
			print("Rico! :)")
		else:
			print("No rico :(")
```

- En Python, `__init__` es la función constructor (en la terminología de object-oriented languages), y es una función interna (o método) reservada especialmente en Python para inicializar los atributos de la clase. (init significa initialize)
- Una vez definida la clase, **se puede usar como función y guardar los valores otorgados en una variable**. Por ejemplo:

```python
manzana = comida("rojo", "dulce")

# NO COMETER ERROR: manzana.__init__("rojo", "dulce"). El método __init__ es tácito si solo se utiliza el nombre de la clase como función, el método no es necesario.

manzana.color() -> "rojo"
manzana.sabor() -> "dulce"
manzana.esRico() -> "Rico! :)"
```