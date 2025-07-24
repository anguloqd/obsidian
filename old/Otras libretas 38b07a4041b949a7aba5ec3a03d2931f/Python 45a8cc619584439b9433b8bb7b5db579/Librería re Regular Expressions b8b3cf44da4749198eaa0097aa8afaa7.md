# Librería re: Regular Expressions

Date de création: December 6, 2020 4:16 AM
Modifié: August 17, 2022 1:00 PM

Regular Expresions (re, regex) es una librería para interactuar avanzadamente con strings.

```python
import re
```

- **Buscar `str` (primera coincidencia)**. `re.match('str a buscar', 'str donde buscar')`. Devuelve la posición de la primera letra de la str hallada.
- **Confirmar presencia de `str` en una variable**. `re.search('str a buscar', 'str donde buscar')`.
- **Separar `str` en una lista con respecto a un caracter “separador”**. `re.split('separador', 'str a separar')`.
- **Lista con todas las coincidencias de una `str`**. `re.findall('str a buscar', 'str donde buscar')`.

[https://stackoverflow.com/questions/20791207/using-asterix-character-as-joker-in-python-string-replacement](https://stackoverflow.com/questions/20791207/using-asterix-character-as-joker-in-python-string-replacement)