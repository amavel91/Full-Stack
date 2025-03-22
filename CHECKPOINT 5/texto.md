# I. Condicionales

En Python, las sentencias `if`, `else` y `elif` permiten que un programa tome decisiones, ejecutando ciertas instrucciones solo si se cumplen determinadas condiciones. Este tipo de lógica es fundamental en situaciones donde muchas acciones dependen de los valores y resultados que se están procesando.

En la vida diaria, las personas toman decisiones constantemente: **si llueve, se usa paraguas; si hace frío, se usa abrigo**. En la programación sucede algo similar: los programas deben "decidir" qué hacer en función de ciertas condiciones.

Estas decisiones se manejan con **sentencias condicionales**, que en Python tienen varias formas: `if`, `if-else`, `if` anidado e `if-elif-else`. (DataScientest, s.f.)

---

## 1.1. Funcionamiento de la sentencia `if`

La sentencia `if` permite ejecutar un bloque de código únicamente si una condición es verdadera. Se escribe la palabra `if`, seguida de la condición, y debajo el bloque de código que debe ejecutarse si esa condición se cumple.  
**Ejemplo:**

```python
if edad > 18:
    print("Acceso permitido")
```

# II. Tipos de bucles en Python y su utilidad

Normalmente, cuando se ejecuta un programa en Python, el código va de arriba hacia abajo, línea por línea. Pero a veces es necesario repetir algo muchas veces, como cuando se canta una canción con varias estrofas iguales o se cuentan cosas una y otra vez. Para eso existen los bucles, también llamados ciclos o loops (EBAC, s.f.).

Los bucles permiten que un programa repita un bloque de instrucciones tantas veces como se necesite, sin tener que escribir el mismo código una y otra vez.

Un bucle sirve para repetir acciones. Cuando se quiere que una tarea se haga varias veces seguidas, se utiliza un bucle. Cada vez que el bucle repite la acción, se llama una iteración. El bucle se repite mientras se cumpla una condición. Cuando la condición ya no se cumple, el programa sale del bucle y sigue con el resto del código.

Python tiene dos tipos principales de bucles:
- **Bucle while**, que se usa cuando no se sabe cuántas veces se va a repetir algo.
- **Bucle for**, que se usa cuando ya se conoce cuántas veces debe repetirse una acción.

Los bucles en Python permiten que el programa repita acciones automáticamente, lo cual es muy útil cuando se necesita hacer algo muchas veces. Con `while` se controla la repetición según una condición, y con `for` se repite sobre elementos de una lista, una cadena o una secuencia de números. Aprender a usar estos bucles ayuda a escribir programas más inteligentes y eficientes.

---

### 2.1. El bucle `while`

El bucle `while` funciona como una especie de “pregunta” que se hace el programa: ¿todavía debo seguir repitiendo esto? Si la respuesta es sí, repite el código; si es no, sale del bucle.  
**Ejemplo:**

```python
x = 5
while x > 0:
    x -= 1
    print(x)
print("Okay")
```

---

### III. Argumento en Python

En Python, un **argumento** es un valor que se le pasa a una función cuando se llama, para que pueda realizar su tarea utilizando esa información.

Las funciones en Python se definen con **parámetros**, que son variables que actúan como espacios vacíos. Al llamar la función, esos espacios se llenan con argumentos específicos.  
**Por ejemplo:**

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Lucía")
```

En este caso, `"Lucía"` es el argumento que se pasa al parámetro `nombre`. Al ejecutar el código, la función imprime:

```
Hola Lucía
```

Los argumentos permiten que una misma función se use de distintas formas, simplemente cambiando el valor que se le proporciona. Esto hace que el código sea más reutilizable y flexible.

Los argumentos pueden ser valores como **números**, **textos**, **listas**, o cualquier otro tipo de dato que necesite la función para funcionar correctamente.

## IV. Función lambda en Python

En Python, una **función lambda** es una forma rápida de escribir funciones muy cortas. También se llaman **funciones anónimas**, porque no tienen nombre como las funciones normales que se escriben con `def`.

Estas funciones se usan cuando se necesita hacer algo simple y rápido, como sumar dos números, calcular un descuento, o convertir un nombre a mayúsculas. Solo pueden hacer **una sola cosa** (una sola línea de código), y por eso no sirven para tareas largas o con muchas instrucciones (Juncotic, s.f.).

Por ejemplo, si se quiere calcular el doble de un número:

```python
def doble(x):
    return x * 2

resultado = doble(5)
print(resultado)
```

Esto mostrará:

```
10
```

Usando `lambda`, se puede escribir en una sola línea:

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

También se pueden hacer funciones lambda con dos o más datos.  
Por ejemplo, si se quiere calcular el precio con descuento:

```python
precio_final = lambda precio, descuento: precio - (precio * descuento / 100)
resultado = precio_final(100, 20)
print(resultado)
```

Esto muestra:

```
80
```

que es el precio final con un 20% de descuento.

---

### Funciones lambda con otras funciones útiles

Las funciones lambda se usan mucho junto con otras funciones de Python como `map`, `filter`, `sort` o `reduce`, que sirven para trabajar con listas de manera rápida.

---

### 🔹 Transformar elementos con `map`

Por ejemplo, si se tiene una lista de precios y se quiere aplicar un impuesto del 10% a todos:

```python
precios = [100, 200, 300]
con_impuesto = list(map(lambda x: x * 1.10, precios))
print(con_impuesto)
```

---

### 🔹 Filtrar valores con `filter`

Por ejemplo, una lista de edades, y se quiere filtrar solo las personas que son mayores de edad (18 años o más):

```python
edades = [15, 22, 17, 30, 12]
mayores = list(filter(lambda x: x >= 18, edades))
print(mayores)
```

Resultado:

```
[22, 30]
```

---

### 🔹 Ordenar con `sort`

Por ejemplo, hay una lista de nombres y se quiere ordenarlos ignorando si están en mayúsculas o minúsculas:

```python
nombres = ["Carlos", "ana", "Beatriz", "carlos", "Ana"]
nombres.sort(key=lambda x: x.lower())
print(nombres)
```

Resultado:

```
['ana', 'Ana', 'Beatriz', 'Carlos', 'carlos']
```

---

### 🔹 Reducir datos con `reduce`

Por ejemplo, si se quiere sumar todos los precios de una lista para saber el total de una compra:

```python
from functools import reduce

precios = [50, 75, 100]
total = reduce(lambda x, y: x + y, precios)
print(total)
```

Resultado:

```
225
```

## V. Paquete `pip`

Los **paquetes de software en Python** son conjuntos de herramientas reutilizables que agrupan módulos y bibliotecas. Estos paquetes permiten realizar diferentes tareas, desde operaciones matemáticas hasta conexión con bases de datos o análisis de datos. En lugar de escribir todo el código desde cero, se pueden usar estos paquetes ya preparados para ahorrar tiempo y esfuerzo. 

Para gestionar estos paquetes, Python utiliza una herramienta llamada **`pip`**. Este gestor simplifica el proceso de instalación, actualización y eliminación de paquetes, además de encargarse automáticamente de instalar otros paquetes necesarios para que todo funcione correctamente (ABC Xperts, s.f.).

Con `pip`, también es posible acceder a miles de paquetes creados por otros desarrolladores en una gran biblioteca pública llamada **PyPI**. Además, quienes desarrollan sus propios paquetes pueden compartirlos fácilmente con la comunidad.

Entre las funciones más importantes de `pip` se encuentran:

- Instalar paquetes desde PyPI u otras fuentes.  
- Actualizar paquetes a su versión más reciente.  
- Desinstalar paquetes que ya no se necesiten.  
- Ver la lista de paquetes instalados en el sistema.  
- Gestionar las dependencias de cada paquete, es decir, otros paquetes que necesita para funcionar bien.  
- Instalar desde diferentes fuentes, como archivos guardados localmente o enlaces a repositorios.  

---

### 🖥️ Comandos básicos de `pip`

El uso de `pip` se realiza desde la **línea de comandos**, con instrucciones simples. Por ejemplo:

- Para instalar un paquete:

```bash
pip install nombre_del_paquete
```

- Para actualizarlo:

```bash
pip install --upgrade nombre_del_paquete
```

- Para desinstalarlo:

```bash
pip uninstall nombre_del_paquete
```

- Para ver qué paquetes están instalados:

```bash
pip list
```

---

### ⚙️ Otras funciones útiles de `pip`

- Crear y compartir paquetes propios, lo cual permite que otras personas usen ese código en sus proyectos.
- Instalar paquetes dentro de un **entorno virtual**, lo que permite separar los paquetes que se usan en distintos proyectos.
- Elegir versiones específicas de un paquete:

```bash
pip install nombre_del_paquete==1.0.0
```

- Instalar varios paquetes a la vez desde un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

- Ver información detallada de un paquete:

```bash
pip show nombre_del_paquete
```

- Buscar paquetes disponibles (este comando ya no funciona en versiones recientes):

```bash
pip search nombre_del_paquete
```

---

En resumen, `pip` es una herramienta fundamental para trabajar con Python, ya que facilita todo lo relacionado con los paquetes: instalarlos, actualizarlos, eliminarlos o compartirlos. Gracias a `pip`, se puede aprovechar el trabajo de miles de personas y construir proyectos más rápido, más fácil y con menos errores.

---

## VI. Bibliografía

- DataScientest. (s.f.). *Python If, Else: todo sobre las sentencias condicionales*. Recuperado el 22 de marzo de 2025, de https://datascientest.com/es/python-if-else  
- EBAC. (s.f.). *Ciclos en Python: cómo funcionan los bucles For y While y cómo hacerlos*. Recuperado el 22 de marzo de 2025, de https://ebac.mx/blog/ciclos-en-python  
- Juncotic. (s.f.). *Función lambda en Python*. Recuperado el 22 de marzo de 2025, de https://juncotic.com/funcion-lambda-en-python/  
- ABC Xperts. (s.f.). *¿Qué es pip?* Recuperado el 22 de marzo de 2025, de https://abcxperts.com/que-es-pip/