# Librería Selenium

Date de création: December 6, 2020 2:48 AM
Modifié: August 17, 2022 12:29 PM

Selenium es una librería para automatizar tareas interactuando con el navegador de internet.
Aquí voy a ir poniendo las cosas que voy descubriendo.

<aside>
💡 Tabla de contenidos

</aside>

# Ubicar elementos

Los elementos son los objetos HTML con los que interactúas. Más formalmente, son nodos del árbol de nodos o DOM (Document Object Model), un API (application programming interface) para HTML. Para ubicarlos, debes recurrir a una de las formas de ubicación que Selenium permite.

Primero, sin embargo, tenemos que tener ya una variable atajo definida para nuestro driver.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
```

Ok, ahora necesitamos localizar un elemento con las siguientes alternativas. La función principal es `driver.find_element(...).`También existe la versión plural: `driver.find_elements(...)`.

- **Nombre**. `driver.find_element(By.NAME, “”)` . Esta opción devolverá el primer objeto, de arriba para abajo, que coincida con el valor del atributo "name" entregado.
- **ID**. `driver.find_element(By.ID, “”)` . Devolverá la primera coincidencia de objeto con tal valor de atributo “ID”.
- **Texto de link**. `driver.find_element(By.LINK_TEXT, “”)` . Devolverá la primera coincidencia con tal valor en el nombre y que sea un link.
- **Texto de link parcial**. `driver.find_element(By.PARTIAL_LINK_TEXT, “”)` . Lo mismo que el anterior, pero puedes poner tan solo una parte del texto. **A veces sirve si se deja el argumento vacío** y simplemente asumirá que el texto es cualquiera, siempre y cuando el elemento tenga link, lo devolverá.
- **XPath**. `driver.find_element(By.XPATH, “”)` . **MUY IMPORTANTE.** Tienes que aprender a localizar por XPath.
- **Selector CSS**. `driver.find_element(By.CSS_SELECTOR, “”)` . Devuelve primera coincidencia del atributo "class" indicado. Se debe primero colocar el nombre del elemento como tal, un punto, y luego el nombre del atributo class. Ej.: ("div.round-button") donde "round-button" es el valor de class del objeto.
- **Nombre de tag**. `driver.find_element(By.TAGNAME, “”)` . Devuelve primera coincidencia del nombre de tag. El tag es el nombre de un objeto como tal (no confundir con sus atributos. Es la primera cosa que aparece en el objeto después de abrir corchetes, como <title>.
- **Nombre de clase**. `driver.find_element(By.CLASSNAME, “”)` . Devuelve primera coincidencia del nombre de "class". Muy similar al selector CSS.

## XPath

XPath es definitivamente el que más uso, aunque es el más lento también. Los XPath son cadenas de texto que siguen un cierto formato e indican en donde está un elemento en particular en el HTML.

En XPath hay 7 nodos: raíz, elemento, texto, atributo, espacio de nombre, instrucciones de proceso y comentarios.

- **Nodo raíz**. Es el primer "/" del documento. Lo que venga después, es el elemento raíz. El elemento raíz, entonces, está contenido en el nodo raíz.
- **Elemento**. Es el nombre de lo que viene después de la etiqueta de apertura. En "<title>", es "title".
- **Atributo**. Es una etiqueta incorporada al elemento que lo contiene. Tiene un nombre y un valor.
- **Texto**. Es lo que está entre la etiqueta de apertura y la etiqueta de cierre.
- **Comentario**. Son comentarios dejados en el código. Están entre comillas.
- El resto no importa para esto.

Los nodos tienen relaciones entre ellos:

- **Padre**. Todos los elementos tienen un padre excepto el nodo raíz (el elemento raíz es hijo del nodo raíz).
- **Hijo**. Los elementos pueden tener o no tener hijos.
- **Hermanos**. Son elementos con el mismo padre directo.
- **Ancestros**. Son elementos que vienen antes del padre: el padre del padre, el padre del abuelo, etc.
- **Descendientes**. Elementos que no son hijos directos de un padre: nietos, bisnietos, etc.

Las localizaciones pueden ser absolutas o relativas.

- **Absolutas**. Empiezan desde el nodo raíz "/". No se recomiendan porque, si la página cambiase su diseño, no funcionarían.
    - `/html/title`, por ejemplo.
    - `/html/title[3]` devolvería el tercer elemento hijo, de arriba a abajo, de la primera coincidencia de title.
        - En Selenium: `driver.find_element(By.XPATH, "/html/title[3]")`.
- **Relativas**. Leen el documento de arriba abajo buscando la primera coincidencia de lo otorgado. Se pueden combinar también con rutas absolutas.
    - `//title`, devolvería la primera coincidencia de un elemento title.
        - En Selenium: `driver.find_element(By.XPATH, "//title")`
    - Se puede, también, especificar un valor de atributo al elemento buscado.
    - `//title[@size='14px']`, devolvería el primer elemento title cuyo valor del atributo "size" sea "14px".
        - En Selenium: `driver.find_element(By.XPATH, "//title[@size='14px']")`. (Atención al uso de comillas simples y dobles simultáneamente, aunque el orden no importa)
    - Aun más, se puede buscar un X elemento hijo de un Y elemento padre, y que el elemento hijo tenga cierto valor de atributo.
        - En Selenium: `driver.find_element(By.XPATH, "//form[input/@name='emailId/mobileNo']")`. Buscará el elemento form que tenga elemento hijo input con atributo name y valor "emailId/mobileNo". **Se devuelve el elemento form, no el elemento input** (en este caso, al estar dentro de corchetes, funciona como un filtro de búsqueda).
    - Se pueden combinar con rutas absolutas.
        - En Selenium: `driver.find_element(By.XPATH, ("//form[@id='loginForm']/input[1]")`. Buscará el elemento form con atributo ID y valor 'loginForm', luego buscará el primer elemento hijo input allí. **Se devuelve el elemento /input[1], no el elemento form**.
    - Podrías usar una ruta relativa "//" dentro de otra ruta relativa "//".

[https://www.techbeamers.com/locate-elements-selenium-python](https://www.techbeamers.com/locate-elements-selenium-python)/

## Búsquedas en plural

Si se usa el método de buscar un elemento singular, arrojará error si no se encuentra. Si se usa el método plural, arrojará una lista vacía si ningún método se encuentra. **Esto es útil para no tener que hacer un bloque "try/except" con el método de búsqueda de elementos singular.**

[https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception/38023345](https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception/38023345)

## Urls

- Ir a una página. `driver.get()`.
- Obtener la url actual. `driver.current_url()`.

# Enviar tecla, clicks y mover el mouse

## Enviar teclas

```python
from selenium.webdriver.common.keys import Keys # 1er método
from selenium.webdriver.common.action_chains import ActionChains # 2do método
```

1. Se hace con el método `.send_keys` después de focalizar un elemento. Para acceder a teclas especiales, como Enter o Delete, se importa la función `Keys` y se accede, por ejemplo con `Keys.ENTER` o `Keys.DELETE`.
    
    ```python
    element.find_element_by_partial_link_text('').send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
    ```
    
2. También se puede hacer sin focalizar un elemento, aunque un poco más complicado.
    
    ```python
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    ```
    
    O más, simple creando un objeto `ActionChains` primero.
    
    ```python
    action = ActionChans(driver)
    action.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    ```
    
    Lo importante de este método es que puedes manipular si quieres dejar una tecla presionada (método `.key_down()`) y después soltarla (método `.key_up()`)
    

## Clicks

Sencillamente es tomar un elemento y llamar el método `.click()`.

```python
element.click()
```

Sin embargo, a veces este método simplemente no funciona. Es más consistente esta manera de hacer click:

```python
def click(xpath):
    driver.execute_script("arguments[0].click();", xpath)
```

## Mover el mouse

```python
from selenium.webdriver.common.action_chains import ActionChains
```

- **Para obtener la posición de un elemento**. `element.getLocation()`. Viene en formato (x,y).
    - `element.getLocation().x` devolvería solo la coordenada x.
    - `element.getLocation().y` devolvería solo la coordenada y.
- **Mover cursor a un elemento**. `webdriver.ActionChains(driver).move_to_element(elmnt)`. El cursor invisible se mueve a la posición del elemento. Solo se notará si tal elemento activa un efecto cuando tiene el mouse por encima de él.
- **Mover cursor en (x,y) unidades**. `webdriver.ActionChains(driver).move_by_offset(x, y)`. Aquí se mueve en posición relativa a la que se encuentra el mouse invisible de Selenium en ese momento. X positivo moverá píxeles hacia la derecha, negativo a la izquierda. Y positivo moverá píxeles hacia arriba, negativo hacia abajo.

[https://stackoverflow.com/questions/32167577/how-to-move-the-mouse-in-selenium](https://stackoverflow.com/questions/32167577/how-to-move-the-mouse-in-selenium)

# Abrir nueva pestaña en Chrome, cambiar pestaña y cerrarla

```python
from selenium.webdriver.common.keys import Keys # 1er método
from selenium.webdriver.common.action_chains import ActionChains # 2do método
```

Esto es una ladilla. Hay tres métodos de hacerlo:

1. `driver.find_element(By.TAGNAME, “body”).send_keys(Keys.CONTROL + 't')`. Esto mandará el comando *ctrl+t*, que es para abrir una nueva pestaña. Se necesita focalizar un elemento equis, no puedes enviar la acción si no se tiene focalizado un elemento. "Body" es un elemento muy genérico que debería funcionar.
    1. Si no funcionase. Podrías intentar cambiar el "+" dentro de `.send_keys` con una ",". O bien puedes cambiar la "t" con "str('\u0074')", que es el unicode para decir lo mismo.
2. `ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()`. Mismo concepto, pero no necesitas focalizar un elemento.
3. `driver.execute_script("window.open('http://www.ejemplo.com/');")`. Ejecuta un script de JavaScript. Este me funcionó pero es terrible lento.

Luego, para cambiar a esa pestaña:

```python
driver.switch_to.window(driver.window_handles[1])
```

El argumento de la función necesita de un ID especial que Selenium le da a las pestañas. Es un montón de números y letras que no te puedes aprender, pero puedes acceder a ellas con la función `driver.window_handles[nro. pestaña]` y poner el número de la pestaña de izquierda a derecha, y luego usar la primera función. Para cerrarla:

```python
driver.close()
driver.switch_to.window(driver.window_handles[0])
```

Necesariamente tienes que poner la segunda línea, pues el driver quedará atascado en la pestaña cerrada a menos a que le digas que cambie a la pestaña original. No puedes acceder a los elementos guardados en una pestaña si Selenium se encuentra en otra.

[https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python](https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python)

[https://medium.com/@pavel.tashev/python-and-selenium-open-focus-and-close-a-new-tab-4cc606b73388](https://medium.com/@pavel.tashev/python-and-selenium-open-focus-and-close-a-new-tab-4cc606b73388)

[https://python-forum.io/Thread-Need-Help-Opening-A-New-Tab-in-Selenium](https://python-forum.io/Thread-Need-Help-Opening-A-New-Tab-in-Selenium)

# Esperas o *waits*

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Con eso importado, la función ejemplo es la siguiente:

```python
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "rutaDeElemento"))
```

En la variable `element` se guardará un elemento que se encuentra en la ruta especificada en el argumento `"rutaDeElemento"`. Se va a chequear por durante 10 segundos hasta que se encuentre. Si no se encuentra nada, simplemente arrojará error.

Se puede usar la versión en plural con "elements" en vez de "element".

También se puede cambiar el método de localización del elemento por By.ID, By.NAME, etc.

[https://selenium-python.readthedocs.io/waits.html](https://selenium-python.readthedocs.io/waits.html)

# Obtener posición de driver y mover la ventana

Para obtener la posición y el tamaño de la ventana:

```python
driver.get_window_position()
driver.get_window_size()
```

Para cambiar posición y tamaño de la ventana.

```python
driver.set_window_position(x, y)
driver.set_window_size(x, y)
```