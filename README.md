# Validador-de-contraseñas
Analizador básico de contraseñas, desarrollado en Python.

## FUNCIONALIDADES ACTUALES
- Validación de espacios.
- Detección de mayúsculas.
- Detección de minúsculas.
- Detección de números.
- Detección de caracteres especiales.
- Sistema básico de puntuación.

## PRÓXIMAS MEJORAS
- [x] Separación mediante funciones.
- [x] Separación de módulos.

## EXPLICACIÓN DE CÓDIGOS.
### PARA ENCONTRAR ESPACIOS EN BLANCO:

```
cadena="Hola Mundo"
while ' ' in cadena:
```

Con esta parte del código hacemos que analice si hay un espacio en la cadena entre en un `while` , lo cual en esta situación entraría en bucle infinito, por ello agregamos dentro de la condicional `while`:
```
  cadena=input("Por favor ingrese la contraseña sin espacios")
```

### FUNCIONES SENCILLAS DE Python

Para este código se recordó varias funciones básicas en Python como lo es:

### `len()`

Sirve para obtener la cantidad de elementos o la longitud de un objeto, como una lista, una cadena de texto (String), una tupla o un diccionario. Siempre devuelve un número entero.

Su uso es:
```
len(cadena)
```

### `sum()``
Sirve para sumar de forma rápida y eficiente los elementos numéricos de un objeto iterable como listas o tuplas.

Su uso es:
```
sum(iterable,start)
```
- Iterable: Una secuencia de números.
- **start**(opcional): Un valor base que se suma al total final. Por defecto es `0`

```
numeros=[1,2,3,4,5]
resultado=sum(numeros)
print(resultado) # Muestra 15
```

### `isupper()`:
Es una función integrada que se aplica a las cadenas (strings). Su propósito es determinar si todos los caracteres en una cadena están en mayúsculas.

### `islower()`:

Es una función integrada que se aplica a las cadenas (strings). Su propósito es determinar si todos los caracteres en una cadena están en minúsculas.

### `isdigit()`:
Es una función integrada que se aplica a las cadenas (strings). Su propósito es determinar si todos los caracteres en una cadena están en minúsculas.


### `string.punctuation`
Es una función de la Liberia `string` en el cual su propósito en este código es para contar los signos utilizados, para su uso debe ser de la siguiente manera.

```
import string
signos= sum(1 for c in cadena if c in string.punctuation)
```



### BUCLE `for` CON CONDICIONAL `if`
En Python sirve para recorrer una lista de elementos y aplicar una regla lógica para decidir que hacer con cada uno de ellos.

#### CÓMO FUNCIONA LA COMBINACIÓN:
- **Bucle `for`:** Permite pasar por cada elemento de una secuencia (como lista o un texto) de forma ordenada.
- **Condicional `if`:** Evalúa si una afirmación es verdadera para decidir si ejecuta una acción.
- **Anidación:** Se coloca el `if` dentro del bloque `for` para que examine cada elemento individualmente.

En el código realizado se observa de la siguiente manera:
```
mayusculas= sum(1 for c in cadena if c.isupper())
# LO QUE NOS DEJA ES UN NÚMERO ENTERO CON
LA CANTIDAD DE LETRAS MAYUSCULAS EN LA CADENA
```
