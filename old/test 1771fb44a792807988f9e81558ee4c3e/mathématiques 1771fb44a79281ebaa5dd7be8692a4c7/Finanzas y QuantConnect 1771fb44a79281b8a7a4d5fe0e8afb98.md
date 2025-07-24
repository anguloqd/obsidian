# Finanzas y QuantConnect

Date de création: January 10, 2025 11:44 AM
Modifié: January 10, 2025 11:44 AM

# Finanzas

Conceptos de finanzas entrelazados con la plataforma de QuantConnect:

- **Barras**:
    - Son el componente principal de los gráficos. Cada barra tiene marcas de cotización, específicamente el High/Low (precio más alto y más bajo) y el Open/Close (precio de apertura y de cierre).
    - El Bid/Ask es el precio más alto que alguien está dispuesto a pagar y el precio más bajo al que alguien está dispuesto a vender, en ese orden.
- **Compañías de corretaje ("Brokerage")**:
    - Compañías que se encargan de ejecutar las órdenes de compra y venta de seguridades que ellos poseen para sus clientes.
- **Fill price**:
    - Es el precio real en la práctica de un título valor, en contraste al precio en la teoría.
- **Fondo cotizado ("Exchange-traded fund" o ETF)**:
    - Es una canasta de títulos de valor que pertenecen a una compañía de corretaje para que sus clientes puedan mandar sus órdenes de comprar y vender.
- **Patrimonio ("Equity")**:
    - El valor de las acciones emitidas por una empresa. También puede ser la propiedad de bienes que pueden tener deudas. Cuando del valor se deducen sus deudas, se encuentra el patrimonio (A - P = C).
- **Palanca ("Leverage")**:
    - Es la estrategia de pedir dinero prestado para invertirlo. También es la razón de las deudas sobre el valor de sus acciones.
- **Tamaños de órdenes ("Lot sizes")**:
    - Normalmente los títulos valores se suelen transar en "paquetes" o Lot Sizes. Eso sí, la cantidad de unidades que trae este paquete depende del broker como también del título valor en sí. Para Forex, por ejemplo, hay 3 tipos de Lot Sizes.
- **Valor ("Security")**:
    - Término paraguas para referirse a instrumentos financieros que sean acciones o deuda.

---

# QuantConnect

La estructura de QuantConnect difiere de la común de Python.

1. Lo primero que debes saber es que el algoritmo que escribas es una extensión de la clase del algoritmo de QuantConnect. Dentro de esta clase, hay dos métodos: Initialize(self) y OnData(self, data).
    - **Initialize(self)**: es el análogo de __init__ en Python (leer: nociones básicas). Es el constructor de clases de esta versión de Python en QC. Más particularmente, en él se pueden establecer variables tales como:
        1. Los datos de un valor (security).
        2. La resolución de tales datos.
        3. Fecha de inicio y final de los datos
        4. La cantidad de dinero ficticio a transar (si aplica).
    - **OnData(self, data)**: es el lugar donde se encuentran las instrucciones del programa y donde el programa tiene acceso a las líneas de comando. Es un método llamado cada vez que el algoritmo recibe nueva información, para luego saber cómo proceder con ella. No necesariamente tienes que utilizarlo para hacer funcionar a tu algoritmo. Puedes hacer un plot con él, eso sí.
    - **OnOrderEvent(self, orderEvent)**:

## Herramientas en Initialize(self):

- **: no se debe guardar en una variable tipo self.variable.

### Relativo al tiempo

- **SetStartDate**(año, mes, día)***: para establecer la fecha de inicio de los datos.
- **SetEndDate**(año, mes, día)***: para establecer la fecha de fin de los datos.

### Añadir securities

- **AddEquity**("ticker", Resolution.X): para agregar un ***objeto*** de acción a tu diccionarios de Securities[] y Portfolio[] con el nombre del ticker. En Resolution (enum), se puede establecer el intervalo de tiempo de resolución de los datos en Tick, Second, Minute, Hour, Daily (reemplaza la X).
- **AddForex**("par de tickers", Resolution.X, Market.Y): similar al anterior pero con Forex. El argumento Y por defecto es Market.FXCM pero también puedes usar Market.Oanda.

### Agrupaciones de securities

- **Securities**["symbol" o "ticker"]: es un diccionario con los valores importados de la base de datos de QC con el método AddSecurity. Puedes acceder a los datos de cada valor con simplemente poner su ticker entre los corchetes. Submétodos serían:
    - .SymbolProperties.LotSize: muestra el tamaño de pedido permitido por el broker seleccionado. Depende del título valor y del broker.
- **Portfolio**["ticker"]: es un diccionario relativo a los valores, pero no a los datos históricos sino a tus posiciones actuales. Las entradas en el diccionario Portfolio son objetos de tipo "SecurityHolding". Puedes acceder a varios submétodos como:
    - .Invested (True or False, general)
    - .TotalUnrealizedProfit
    - TotalPortfolioValue
    - TotalMarginUsed
    - Quantity (de un security especificado)
    - AveragePrice (de un security especificado)
    - UnrealizedProfit (específico a un título valor),
    - Y más propiedades útiles de tus posiciones con ciertos valores.

### Ajustes a los datos

- **Securities**["ticker"].**SetDataNormalizationMode**(DataNormalizationMode.X)***: en QC, los valores históricos vienen ajustados por defecto teniendo en cuenta los pagos de dividendos y splits de acciones. Puede normalizar esto individualmente para cada bien con ese método. Los valores aceptados (reemplaza la X) son Raw, Adjusted, SplitAdjusted y TotalReturn.
- securityejemplo.**SetLeverage**(float)***: para establecer el coeficiente de "palanca" o leverage. (Razón de deudas sobre valor de acciones).
- .**SetBrokerageModel**(BrokerageName.X): los modelos de brokerage o corretaje configuran rápidamente las tarifas y modelos y los tipos de órdenes admitidos en el brokerage. Es la forma más rápida de preparar el algoritmo para que haga el trabajo. Los valores que puede tomar X son:
    - InteractiveBrokersBrokerage
    - OandaBrokerage
    - Bitfinex
    - GDAX
    - FxcmBrokerage

## Herramientas en OnData(self, data):

- **.debug**("string"): análogo de print() en Python normal.
- **.MarketOrder**("ticker", int.): establecer una orden de compra de un título valor y la cantidad de acciones en integers.
    - El precio de tal título valor es modelizado en backtesting y se puede acceder con Portfolio["ticker"].AveragePrice. En trading real, se utiliza obviamente el precio real.
- **.StopMarketOrder**("tickerr", int en negativo, precio en int): vende los assets cuando baja de un cierto precio indicado.
- .**Time.X**: devuelve info. con respecto al tiempo. Devuelve un integer. X puede ser:
    - year
    - month
    - day
    - hour
    - minute
- data[]: es un diccionario que contiene Forex, y cada objeto tiene propiedades del precio Bid/Ask como las 4 cotizaciones o quotes.

## Herramientas en OnOrdenEvent(self, orderEvent):