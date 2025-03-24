# I. Condicionales

En Python, las sentencias `if`, `else` y `elif` permiten que un programa tome decisiones, ejecutando ciertas instrucciones solo si se cumplen determinadas condiciones. Este tipo de lógica es fundamental en situaciones donde muchas acciones dependen de los valores y resultados que se están procesando.

En la vida diaria, las personas toman decisiones constantemente: si llueve, se usa paraguas; si hace frío, se usa abrigo. En la programación sucede algo similar: los programas deben "decidir" qué hacer en función de ciertas condiciones.

Estas decisiones se manejan con sentencias condicionales, que en Python tienen varias formas: `if`, `if-else`, `if anidado` e `if-elif-else`. (DataScientest, s.f.)

Imagina que un programa es como un amigo que te pregunta: “¿Quieres jugar afuera?” y tú respondes según el clima. Así, si la condición se cumple, el programa actúa; de lo contrario, hace otra cosa. Es una forma de enseñar a la computadora a tomar decisiones simples de forma ordenada (Python.org, s.f.; W3Schools, s.f.).

## 1.1. Funcionamiento de la sentencia if

La sentencia `if` permite ejecutar un bloque de código únicamente si una condición es verdadera. Se escribe la palabra `if`, seguida de la condición, y debajo el bloque de código que debe ejecutarse si esa condición se cumple. Ejemplo:

```python
if edad > 18:
    print("Acceso permitido")
```

Si la edad es mayor que 18, el programa mostrará "Puedes entrar". Si no, no hará nada. **Importante:** en Python usamos espacios (lo que se llama *indentación*) para decir qué parte del código pertenece al "if".

Piensa en el "if" como una puerta que solo se abre si se da la respuesta correcta. Si la condición (por ejemplo, que la edad sea mayor que 18) se cumple, la puerta se abre (se ejecuta el código dentro del if). La indentación es como el sello de la puerta que indica a qué grupo pertenece esa acción (W3Schools, s.f.; Tutorialspoint, s.f.).

## 1.2. Funcionamiento de la sentencia if-else

A veces no solo quieres hacer algo si se cumple una condición, sino también hacer otra cosa si no se cumple. Para eso usamos `else`, que significa "si no". Ejemplo:

```python
if edad > 18:
    print("Puedes entrar")
else:
    print("No puedes entrar")
```

Así, el programa siempre hace algo, ya sea que la condición se cumpla o no.  
Esta estructura es como elegir entre dos caminos: si hace sol, sales a jugar; si llueve, te quedas en casa. De esta forma, el programa siempre tiene una respuesta, lo que evita que se "quede pensando" qué hacer.

## 1.3. Funcionamiento de la sentencia if anidada

Es cuando pones una condición dentro de otra. Por ejemplo, imagina que quieres saber si alguien puede entrar a un parque, y dentro de eso, ver si tiene un pase especial.

```python
if edad > 10:
    if tiene_pase:
        print("Puedes usar los juegos especiales")
```

Este tipo de estructura se llama *if anidado*. Puede usarse muchas veces, pero si lo haces demasiado, el código se vuelve más complicado de leer, así que es mejor no abusar.

Es similar a hacer dos preguntas seguidas: primero se pregunta si la persona es lo suficientemente grande y luego si tiene el pase. Es una manera de filtrar opciones, pero hay que tener cuidado de no complicar demasiado la "conversación" del programa.

## 1.4. Funcionamiento de la sentencia if-elif-else

A veces no basta con solo dos opciones. ¿Qué pasa si hay muchas posibilidades? Ahí usamos `elif`, que es como decir "si no, pero si..." Por ejemplo:

```python
if nota >= 90:
    print("Tienes una A")
elif nota >= 80:
    print("Tienes una B")
elif nota >= 70:
    print("Tienes una C")
else:
    print("Necesitas mejorar")
```
Primero se revisa la condición del `if`, y si no se cumple, se va probando cada `elif`. Si ninguna condición se cumple, entonces se ejecuta el `else`.

Piensa en esto como una serie de escalones: el programa revisa cada escalón (cada condición) hasta encontrar el que corresponde. Si ninguno es el correcto, se elige la última opción. Esto ayuda a cubrir todas las posibilidades de manera ordenada (Tutorialspoint, s.f.; W3Schools, s.f.).

# III. Tipos de bucles en Python y su utilidad

Normalmente, cuando se ejecuta un programa en Python, el código va de arriba hacia abajo, línea por línea. Pero a veces es necesario repetir algo muchas veces, como cuando se canta una canción con varias estrofas iguales o se cuentan cosas una y otra vez. Para eso existen los bucles, también llamados ciclos o *loops* (EBAC, s.f.).

Los bucles permiten que un programa repita un bloque de instrucciones tantas veces como se necesite, sin tener que escribir el mismo código una y otra vez.

Un bucle sirve para repetir acciones. Cuando se quiere que una tarea se haga varias veces seguidas, se utiliza un bucle. Cada vez que el bucle repite la acción, se llama una *iteración*. El bucle se repite mientras se cumpla una condición. Cuando la condición ya no se cumple, el programa sale del bucle y sigue con el resto del código.

Python tiene dos tipos principales de bucles:
- **Bucle while**, que se usa cuando no se sabe cuántas veces se va a repetir algo.
- **Bucle for**, que se usa cuando ya se conoce cuántas veces debe repetirse una acción.

Los bucles en Python permiten que el programa repita acciones automáticamente, lo cual es muy útil cuando se necesita hacer algo muchas veces. Con `while` se controla la repetición según una condición, y con `for` se repite sobre elementos de una lista, una cadena o una secuencia de números. Aprender a usar estos bucles ayuda a escribir programas más inteligentes y eficientes.

## 2.1. El bucle while

El bucle `while` funciona como una especie de “pregunta” que se hace el programa: ¿todavía debo seguir repitiendo esto? Si la respuesta es sí, repite el código; si es no, sale del bucle. Ejemplo:

```python
x = 5
while x > 0:
    x -= 1
    print(x)
print("Okay")
```

# III. Lista por comprensión en Python

Según *El Libro de Python* (s.f.), una de las cosas más interesantes de Python es que permite escribir lo mismo de varias maneras distintas, gracias a su sintaxis tan flexible. Una de esas formas se llama **list comprehension** o *comprensiones de listas*. Básicamente, es una forma muy corta y clara de crear listas.

Por ejemplo, si se quiere una lista con los cuadrados de los primeros cinco números, se puede escribir así en una sola línea:

```python
cuadrados = [i**2 for i in range(5)]
Resultado: [0, 1, 4, 9, 16]
```

Esto se puede hacer también con un bucle normal:

```python
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
```

Ambas formas hacen lo mismo, pero la primera es más compacta y fácil de leer. La forma general de una list comprehension es: 
[expresión for elemento in iterable]

Esto significa que se toma cada valor del iterable (como una lista o un rango), se hace algo con él (la expresión) y ese resultado se guarda en una nueva lista. Por ejemplo, si se quiere una lista de cinco unos:

```python
unos = [1 for i in range(5)]
#Resultado: [1, 1, 1, 1, 1]
```

También se puede usar una función dentro de la expresión:

```python
def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
Resultado: [0, 1, 4, 9, 16]
```

No sólo se puede usar range(), también se puede aplicar esto a listas u otros elementos iterables. Por ejemplo, si se quiere dividir todos los números de una lista por 10:
```python
lista = [10, 20, 30, 40, 50]
nueva_lista = [i/10 for i in lista]
Resultado: [1.0, 2.0, 3.0, 4.0, 5.0]
```

También se pueden agregar condiciones. Por ejemplo, si se quiere filtrar elementos según alguna regla, se puede usar if al final de la expresión:
[expresión for elemento in iterable if condición]

Un caso concreto sería contar cuántas veces aparece la letra "r" en una frase:

```python
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
print(len(erres))  # Resultado: 4
```

Además de listas, también se pueden usar comprensiones con sets. Lo único que cambia es que se usan llaves {} en vez de corchetes []. Como los sets no permiten duplicados, los elementos repetidos se eliminan:
```python
mi_set = {i for i in frase if i == "r"}
# Resultado: {'r'}
```

Y también existe la comprensión de diccionarios. Aquí, en lugar de solo guardar un valor, se guarda una clave y un valor, usando `:` entre ellos. Por ejemplo, si se tienen dos listas y se quiere convertirlas en un diccionario:

```python
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']
mi_dict = {i: j for i, j in zip(lista1, lista2)}
# Resultado: {'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
```


En resumen, las comprensiones en Python (de listas, sets o diccionarios) son muy útiles para escribir código más corto y claro. Son una forma práctica de transformar o filtrar datos sin tener que escribir muchos bucles. Además, a veces también son más rápidas. Eso sí, hay que usarlas con cuidado para que el código no se vuelva difícil de leer.

# IV. Argumento en Python

En Python, un argumento es un valor que se le pasa a una función cuando se llama, para que pueda realizar su tarea utilizando esa información.

Las funciones en Python se definen con parámetros, que son variables que actúan como espacios vacíos. Al llamar la función, esos espacios se llenan con argumentos específicos. Por ejemplo:

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Lucía")
```

En este caso, "Lucía" es el argumento que se pasa al parámetro nombre. Al ejecutar el código, la función imprime:
```python
Hola Lucía
```

Los argumentos permiten que una misma función se use de distintas formas, simplemente cambiando el valor que se le proporciona. Esto hace que el código sea más reutilizable y flexible.

Los argumentos pueden ser valores como números, textos, listas, o cualquier otro tipo de dato que necesite la función para funcionar correctamente.

Podemos comparar los argumentos con los ingredientes de una receta. La función es la receta, y los argumentos son los ingredientes que varían para obtener resultados diferentes cada vez (Tutorialspoint, s.f.).

# V. Función lambda en Python

En Python, una función lambda es una forma rápida de escribir funciones muy cortas. También se llaman funciones anónimas, porque no tienen nombre como las funciones normales que se escriben con def.

Estas funciones se usan cuando se necesita hacer algo simple y rápido, como sumar dos números, calcular un descuento, o convertir un nombre a mayúsculas. Solo pueden hacer una sola cosa (una sola línea de código), y por eso no sirven para tareas largas o con muchas instrucciones (Juncotic, s.f.).

Por ejemplo, si se quiere calcular el doble de un número:

```python
def doble(x):
    return x * 2

resultado = doble(5)
print(resultado)
```

Esto mostrará: 10

Usando lambda, se puede escribir en una sola línea:
```python
doble = lambda x: x * 2
resultado = doble(5)
print(resultado)
```

También se puede hacer todo junto sin guardar la función:
```python
resultado = (lambda x: x * 2)(5)
print(resultado)
```

También se pueden hacer funciones lambda con dos o más datos. Por ejemplo, si se quiere calcular el precio con descuento:
```python
precio_final = lambda precio, descuento: precio - (precio * descuento / 100)
resultado = precio_final(100, 20)
print(resultado)
```

Esto muestra: 80

que es el precio final con un 20% de descuento.

## 5.1. Funciones lambda con otras funciones útiles

Las funciones lambda se usan mucho junto con otras funciones de Python como `map`, `filter`, `sort` o `reduce`, que sirven para trabajar con listas de manera rápida.

- **Transformar elementos con map**

Por ejemplo, si se tiene una lista de precios y se quiere aplicar un impuesto del 10% a todos:

```python
precios = [100, 200, 300]
con_impuesto = list(map(lambda x: x * 1.10, precios))
print(con_impuesto)
```
- **Filtrar valores con filter**

Por ejemplo, una lista de edades, y se quiere filtrar solo las personas que son mayores de edad (18 años o más):

```python
edades = [15, 22, 17, 30, 12]
mayores = list(filter(lambda x: x >= 18, edades))
print(mayores)
 Resultado: [22, 30]
```

- **Ordenar con sort**

Por ejemplo, hay una lista de nombres y se quiere ordenarlos ignorando si están en mayúsculas o minúsculas:
```python
nombres = ["Carlos", "ana", "Beatriz", "carlos", "Ana"]
nombres.sort(key=lambda x: x.lower())
print(nombres)
# Resultado:
['ana', 'Ana', 'Beatriz', 'Carlos', 'carlos']
```

- **Reducir datos con reduce**

Por ejemplo, si se quiere sumar todos los precios de una lista para saber el total de una compra:
```python
from functools import reduce

precios = [50, 75, 100]
total = reduce(lambda x, y: x + y, precios)
print(total)
# Resultado: 225
```
Las funciones lambda son como pequeños atajos para realizar cálculos rápidos. Al combinarlas con funciones como map o filter, se pueden transformar y analizar listas de forma sencilla, haciendo el código más corto y comprensible (Juncotic, s.f.; Codeacademy, s.f.).

#VI. Paquete pip

Los paquetes de software en Python son conjuntos de herramientas reutilizables que agrupan módulos y bibliotecas. Estos paquetes permiten realizar diferentes tareas, desde operaciones matemáticas hasta conexión con bases de datos o análisis de datos. En lugar de escribir todo el código desde cero, se pueden usar estos paquetes ya preparados para ahorrar tiempo y esfuerzo.

Para gestionar estos paquetes, Python utiliza una herramienta llamada pip. Este gestor simplifica el proceso de instalación, actualización y eliminación de paquetes, además de encargarse automáticamente de instalar otros paquetes necesarios para que todo funcione correctamente (ABC Xperts, s.f.).

Con pip, también es posible acceder a miles de paquetes creados por otros desarrolladores en una gran biblioteca pública llamada PyPI. Además, quienes desarrollan sus propios paquetes pueden compartirlos fácilmente con la comunidad.
Entre las funciones más importantes de pip se encuentran:
- **Instalar paquetes desde PyPI u otras fuentes. **
- **Actualizar paquetes a su versión más reciente. **
- **Desinstalar paquetes que ya no se necesiten. **
- **Ver la lista de paquetes instalados en el sistema. **
- **Gestionar las dependencias de cada paquete, es decir, otros paquetes que necesita para funcionar bien. **
- **Instalar desde diferentes fuentes, como archivos guardados localmente o enlaces a repositorios. **

## 6.1. Comandos básicos de pip

El uso de pip se realiza desde la línea de comandos, con instrucciones simples. Por ejemplo:
-Para instalar un paquete:
pip install nombre_del_paquete
-Para actualizarlo:
pip install --upgrade nombre_del_paquete
-Para desinstalarlo:
pip uninstall nombre_del_paquete
-Para ver qué paquetes están instalados:
pip list

## 6.2. Otras funciones útiles de pip

-Crear y compartir paquetes propios, lo cual permite que otras personas usen ese código en sus proyectos.
-Instalar paquetes dentro de un entorno virtual, lo que permite separar los paquetes que se usan en distintos proyectos.
-Elegir versiones específicas de un paquete:
pip install nombre_del_paquete==1.0.0
-Instalar varios paquetes a la vez desde un archivo requirements.txt:
pip install -r requirements.txt
-Ver información detallada de un paquete:
pip show nombre_del_paquete
-Buscar paquetes disponibles (este comando ya no funciona en versiones recientes):
pip search nombre_del_paquete

En resumen, pip es una herramienta fundamental para trabajar con Python, ya que facilita todo lo relacionado con los paquetes: instalarlos, actualizarlos, eliminarlos o compartirlos. Gracias a pip, se puede aprovechar el trabajo de miles de personas y construir proyectos más rápido, más fácil y con menos errores.

#VII. Bibliografía

-DataScientest. (s.f.). Python If, Else: todo sobre las sentencias condicionales. Recuperado el 22 de marzo de 2025, de https://datascientest.com/es/python-if-else
-EBAC. (s.f.). Ciclos en Python: cómo funcionan los bucles For y While y cómo hacerlos. Recuperado el 22 de marzo de 2025, de https://ebac.mx/blog/ciclos-en-python
-El Libro de Python. (s.f.). List comprehensions en Python. Recuperado el 24 de marzo de 2025, de https://ellibrodepython.com/list-comprehension-python
-Juncotic. (s.f.). Función lambda en Python. Recuperado el 22 de marzo de 2025, de https://juncotic.com/funcion-lambda-en-python/
-ABC Xperts. (s.f.). ¿Qué es pip? Recuperado el 22 de marzo de 2025, de https://abcxperts.com/que-es-pip/