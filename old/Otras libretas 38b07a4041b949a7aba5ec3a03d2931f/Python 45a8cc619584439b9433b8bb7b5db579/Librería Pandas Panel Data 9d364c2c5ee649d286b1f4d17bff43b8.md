# Librería Pandas: Panel Data

Date de création: December 6, 2020 1:36 AM
Modifié: December 31, 2022 9:37 PM

<aside>
💡 Tabla de contenidos

</aside>

# Introducción y funciones básicas

---

Pandas es una librería o módulo que ofrece varias opciones para analizar datos, ordenarlos, etc. Pandas utiliza como su objeto principal los denominados **DataFrames**, los que pueden ser entendidos como un símil a lo que sería una hoja de cálculo Excel.

```python
import pandas as pd
```

Para crear un dataframe (df),  se necesitan 3 elementos: datos, encabezado (etiquetas de columnas) y índices (etiquetas de filas)

```python
numeros = [[1,2,3],[4,5,6],[7,8,9]]
df_A = pd.DataFrame(data=numeros, columns=["A","B","C"], index=["fila1","fila2","fila3"])
```

Esta tabla es lo que se devolverá:

[Untitled](Untitled%208b30e5435387464eb02bbc12a917dab4.csv)

Más rápidamente, se pudo haber creado con `df_B = pd.DataFrame(numeros)`. Cuando no se indican encabezado ni índices, se rellenan con números empezando desde el 0.

- El argumento de la función `pd.DataFrame()` necesita ser solo una lista. Para ello, necesitas hacer una lista de listas.
- **Acceder a los nombres de las columnas.** `pd.numeros.columns`
- **Acceder a los nombres de las filas.** `pd.numeros.index`
- **Acceder a los valores del df**. `pd.numeros.values`

# Leer archivos desde un Excel

---

Para leer un archivo .xlsx, debe estar primero en la misma carpeta que el archivo .py o .ipynb.

```python
df_credit = pd.read_excel("clientes_banco.xlsx", sheet_name=0)
```

Esto traería la siguiente tabla (de tener el archivo):

[Untitled](Untitled%20442a616cf4f040f3bdfa8f866cb99501.csv)

# Exportar a Excel

---

[Untitled](Untitled%20956aa45705874969b7715ad1bd101f4e.csv)

Si tuvieras el df ya preparado (`df_covid = pd.DataFrame(lista_de_listas)`) y quisieras exportarlo a un .xlsx, se haría con `df_covid.to_excel("covid.xlsx")`.

También puedes ver estadísticas descriptivas con `df_covid.describe`. Solo incluirá columnas con valores numéricos. Si se quiere algo más completo (incluyendo valores cuantitativos), se puede utilizar `df_credit.describe(include="all").`

[Untitled](Untitled%204cfb0bbaf06042d38cedfa4f0f6c3458.csv)

Se puede obtener solo una estadística aplicada a una columna con `df_credit["index"].mean()`, por ejemplo.

# Procesando y analizando DataFrames

---

## Ubicación de los datos

---

- **Índice o columna de un dato**. `.iloc` para ubicación con índices, `.loc` para ubicación con nombres de columnas.
- **Acceder solo a las primeras** `x` **filas**. `df_credit.head(x)`. Si argumento vacío, muestra las primeras 5 filas.
- **Acceder solo a las últimas** `x` **filas**. `df_credit.tail(x)`. Lo mismo con argumento vacío.
- Podemos usar los métodos `.head()` y `.tail()` de solo una columna si conocemos su nombre, `df_credit["Genero"].head(10)`.
- **Acceder a un dato por coordenada**. `df_credit.iloc[0,0]`, donde [fila, columna].
    - También se puede hacer con rangos, índices negativos e índices vacíos, `df_credit.iloc[2:5 , : ]` (traería filas de la 2 a la 4, y todas las columnas).
    - Se pueden referencias por nombres también, `df_credit.loc[:, "C"]` (donde se traería todas las filas de la **primera coincidencia** de la columna llamada "C").
    - También se puede hacer una lista con los nombres y usarla como rango, `df_credit.loc[:,["B","C"]]` (todas las filas de las columnas B y C).
- **Nuevo df tomando parte de un df anterior**. `df_ejemplo2 = df_credit["Genero"].head(10).`
- Se podría usar el método `.describe()` con solo una columna como `df_credit["Genero"]`.

## Editar valores de un DataFrame

---

- **Crear columna nueva**. `df_credit[Año] = "2020"`.Esto creará una columna en el último lugar del df cuyos datos serán "2020" hasta ocupar todas las filas.
- **Cambiar un dato en posición (x,y)**. Se hace con la lógica de asignación. `df_credit.loc[0, "Balance"] = 500000`.
- **Crear columnas con fórmulas basadas en otras columnas**. `df_credit["SaldoDisponible"] = df_credit["SueldoEstimado"] - df_credit["Balance"]`.
- **Borrar un elemento fila o columna**. Ocupamos drop e indicamos si la operación es de fila con `axis=0` (por defecto) o columna con `axis=1`. También funciona con `axis="rows"` o `axis="columns"`. `df_credit = df_credit.drop("Año", axis=1)`.

## Aplicando funciones al DataFrame

---

Supongamos que queremos una columna que ponga "1" si la persona tiene un hijo o más, y "0" si no.

```python
def casado_con_hijos(df):

""" esta función toma un df con una columna llamada Estado_Marital,y una columna llamada NroHijos y calcula el valor 1 si la persona está casada y tiene 1 hijo o más, o 0 en caso contrario """

	if df["Estado_Marital"]=="Casado" and df["NroHijos"]>0:
		return 1

	else:
		return 0

df_credit["Casado_con_hijos"] = df_credit.apply(casado_con_hijos, axis=1)
```

Esto añadiría una nueva columna con tal criterio.

## Gráficos

---

- **Histograma.** Se puede visualizar data de una columna en un histograma con `df_credit["Edad"].plot(kind="hist")`
- **Scatterplot.** También un diagrama de dispersión de sueldo contra balance con `df_credit.plot(x="SueldoEstimado",y="Balance", kind="scatter")`.
- **Escala logarítmitca.** `df_credit.plot(x="SueldoEstimado",y="Balance", kind="scatter", logy=True, logx=True)`

### **Estadística descriptiva avanzada**

Para esto, primero hay que instalar esto la librería Pandas Profiling.

```python
!pip install 
https://github.com/pandas-profiling/pandas-profiling/archive/master.zip
```

Luego importarla y asignar el df_credit:

```python
from pandas_profiling import ProfileReport
prof=ProfileReport(df_credit)
```

Esperamos unos minutos y tendremos un reporte completo. Se puede encontrar al final de aquí: [https://colab.research.google.com/drive/1hJtC90HkxC7N65QGbUeMluCaLaa-Ir9i?usp=sharing#scrollTo=cWl7KXkuyMcW](https://colab.research.google.com/drive/1hJtC90HkxC7N65QGbUeMluCaLaa-Ir9i?usp=sharing#scrollTo=cWl7KXkuyMcW)

También se puede montar en una página HTML.

```python
prof.to_file(output_file="reporte df credit.html")
```