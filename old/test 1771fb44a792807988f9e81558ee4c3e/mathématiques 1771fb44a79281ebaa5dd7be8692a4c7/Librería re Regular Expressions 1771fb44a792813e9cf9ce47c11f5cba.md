# Librería re: Regular Expressions

Date de création: January 10, 2025 11:44 AM
Modifié: January 10, 2025 11:44 AM

Regular Expresions (re, regex) es una librería para interactuar avanzadamente con strings.

```python
import re
```

- **Buscar `str` (primera coincidencia)**. `re.match('str a buscar', 'str donde buscar')`. Devuelve la posición de la primera letra de la str hallada.
- **Confirmar presencia de `str` en una variable**. `re.search('str a buscar', 'str donde buscar')`.
- **Separar `str` en una lista con respecto a un caracter “separador”**. `re.split('separador', 'str a separar')`.
- **Lista con todas las coincidencias de una `str`**. `re.findall('str a buscar', 'str donde buscar')`.

[https://stackoverflow.com/questions/20791207/using-asterix-character-as-joker-in-python-string-replacement](https://stackoverflow.com/questions/20791207/using-asterix-character-as-joker-in-python-string-replacement)