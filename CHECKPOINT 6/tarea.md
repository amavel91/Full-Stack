## I. Clases en Python

En Python, las **clases** permiten agrupar datos y comportamientos en una misma estructura, lo cual facilita la organización, reutilización y claridad del código. Este enfoque se conoce como **programación orientada a objetos**. Con una clase se pueden crear objetos que comparten atributos y funciones, lo que resulta muy últil cuando se desea representar entidades del mundo real dentro de un programa, como por ejemplo autos, estudiantes o cuentas bancarias (Python.org, s.f.).

## 1.1. ¿Qué es una clase?

Una clase es como una plantilla. Define las características (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella. En otras palabras, permite encapsular información y acciones en una sola unidad. Por ejemplo, una clase llamada `Coche` podría tener atributos como `marca`, `color` y `año`, y métodos como `arrancar()` o `frenar()` (Ionos, s.f.).

Este tipo de estructura ayuda a mantener el código ordenado, porque separa cada tipo de objeto con sus propias funciones. Además, permite que varios objetos compartan el mismo comportamiento, sin necesidad de repetir instrucciones.

## 1.2. ¿Para qué sirve usar clases?

Usar clases en Python tiene varias ventajas importantes:

- **Evitar la repetición de código**, creando una sola vez una estructura que se puede usar muchas veces.
- **Organizar mejor los programas**, dividiendo cada tipo de información en bloques independientes.
- **Facilitar el mantenimiento y la lectura del código**, porque cada clase agrupa lo que necesita para funcionar.
- **Crear programas más escalables**, ya que se pueden agregar nuevas clases o modificar las existentes sin afectar otras partes del programa.
- **Reutilizar código**, gracias a conceptos como la herencia, donde una clase puede tomar elementos de otra.

La programación orientada a objetos permite resolver problemas complejos con estructuras simples y reutilizables, lo que la convierte en una herramienta poderosa para desarrollar proyectos grandes y profesionales (Python.org, s.f.).

## 1.3. Ejemplo de una clase simple

A continuación se muestra un ejemplo de cómo se puede definir y utilizar una clase en Python:

```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def describir(self):
        return f"Este coche es un {self.marca} de color {self.color}."

mi_coche = Coche("Toyota", "rojo")
print(mi_coche.describir())
```

En este ejemplo:

- `__init__` es un método especial que se ejecuta al crear el objeto. Sirve para darle valores iniciales a sus atributos.
- `self` representa al propio objeto, y se usa para acceder a sus atributos o llamar a sus métodos.
- `describir` es un método que devuelve una frase usando la información del objeto.
- `mi_coche` es una instancia de la clase `Coche`.


Las clases en Python permiten modelar situaciones reales mediante estructuras que combinan datos y acciones. Su uso facilita la creación de programas más ordenados, reutilizables y fáciles de mantener. Además, fomentan una forma de programar muy utilizada en la industria: la programación orientada a objetos.

## II. El método que se ejecuta al crear una instancia de clase

Cuando se crea un objeto a partir de una clase en Python, hay un método especial que se ejecuta automáticamente: se llama `__init__`. Este método sirve para darle al nuevo objeto sus primeros valores, como si se le llenaran los "datos de nacimiento" apenas es creado (MyGreatLearning, s.f.).

### 2.1. ¿Qué hace exactamente el método `__init__`?

El método `__init__` es parte de algo llamado **métodos especiales** o "métodos mágicos" en Python. Se reconoce porque empieza y termina con dos guiones bajos. Cuando se llama a una clase para crear un objeto, Python busca si esa clase tiene definido un `__init__`. Si lo tiene, lo ejecuta de inmediato, sin que haya que llamarlo a mano (RealPython, s.f.).

Este método recibe al menos un parámetro: `self`, que representa al objeto que se está creando. Además, se pueden incluir otros parámetros que servirán para darle valores al objeto. Por ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Crear una instancia
persona1 = Persona("Lucía", 15)
print(persona1.saludar())
```

**Resultado:**
```
Hola, me llamo Lucía y tengo 15 años.
```

En este ejemplo, cuando se escribe `Persona("Lucía", 15)`, Python ejecuta el método `__init__` automáticamente, y le da al nuevo objeto los valores `nombre = "Lucía"` y `edad = 15`.

### 2.2. Diferencia entre `__init__` y `__new__`

Técnicamente, hay otro método llamado `__new__` que se ejecuta justo antes que `__init__`. Este se encarga de crear el objeto, pero rara vez se usa directamente. En la mayoría de los programas en Python, el que se usa y personaliza es `__init__` (Udacity, s.f.).

Se puede pensar en una clase como un formulario para inscribirse a una actividad. Al completar el formulario (crear una instancia), alguien lo revisa y guarda los datos donde corresponde. Esa persona que guarda los datos es el método `__init__`, que toma lo que escribiste en el formulario y lo pone en los espacios correctos del sistema.

### 2.3. Beneficios de `__init__`

- Evita escribir muchas veces el mismo código para dar valores iniciales.
- Hace que los objetos estén listos para usarse apenas se crean.
- Permite que cada objeto tenga valores personalizados desde el inicio.

El método `__init__` en Python se ejecuta automáticamente al crear una instancia de clase. Es el encargado de darle sus primeros datos al nuevo objeto. Gracias a este método, cada objeto puede comenzar con valores propios, lo que hace que trabajar con clases sea mucho más ordenado y flexible (RealPython, s.f.; MyGreatLearning, s.f.).

## III. Principales verbos de una API

Cuando se trabaja con una API (Interfaz de Programación de Aplicaciones), es común usar ciertos **verbos HTTP** para indicar lo que se quiere hacer con los datos. Estos verbos forman parte del protocolo HTTP, que es el lenguaje que utilizan los navegadores y los servidores para comunicarse.

Aunque existen varios, hay tres que se consideran los principales porque representan las acciones más comunes que se hacen al interactuar con una API: **GET**, **POST** y **PUT** (Mozilla Developer Network, s.f.).

### 3.1. GET: obtener información

El verbo **GET** se usa para **leer datos**. Es como cuando se pide una página web o se consulta información en una app. No modifica nada, solo obtiene lo que ya existe en el servidor. Por ejemplo, una API podría usar GET para devolver una lista de usuarios o los detalles de un producto (Mozilla Developer Network, s.f.).

### 3.2. POST: crear un nuevo recurso

El verbo **POST** sirve para **enviar información nueva** al servidor. Esto se usa cuando se quiere crear un nuevo recurso, como registrar un nuevo usuario o agregar un comentario. En este caso, los datos se envían en el cuerpo del mensaje, y el servidor los recibe y los guarda (Código Facilito, s.f.).

### 3.3. PUT: actualizar información

El verbo **PUT** se utiliza para **modificar un recurso existente** o **crear uno si no existe**. A diferencia de POST, que solo crea, PUT puede actualizar algo que ya existe. Por ejemplo, cambiar el nombre de un usuario en el sistema. Es importante saber que PUT reemplaza por completo el contenido anterior del recurso (KeepCoding, s.f.).

### 3.4. Relación con las operaciones CRUD

Estos tres verbos se relacionan con las operaciones **CRUD**, que son las acciones básicas que se hacen en la mayoría de las aplicaciones:

- **C**reate (crear) → POST
- **R**ead (leer) → GET
- **U**pdate (actualizar) → PUT
- **D**elete (eliminar) → DELETE

DELETE también es un verbo muy usado. Es bueno conocerlo porque completa el ciclo de trabajo con recursos. Ejemplo:

```
GET /usuarios            Obtener lista de usuarios
POST /usuarios           Crear un nuevo usuario
PUT /usuarios/1          Actualizar información del usuario con ID 1
```

Los verbos GET, POST y PUT son los más utilizados al trabajar con APIs. Permiten consultar, crear o actualizar datos de manera ordenada y clara. Gracias a estos verbos, los programas pueden comunicarse con servicios externos de forma sencilla y predecible (Mozilla Developer Network, s.f.; Código Facilito, s.f.).

## IV. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos **NoSQL**, lo que significa que no utiliza el lenguaje SQL ni la estructura de tablas con filas y columnas como las bases de datos tradicionales. En lugar de eso, guarda la información en **documentos** con un formato muy similar a JSON, dentro de estructuras llamadas **colecciones** (Oracle, s.f.).

### 4.1. Diferencias clave con bases de datos SQL

Las bases de datos SQL, como MySQL o PostgreSQL, trabajan con esquemas fijos: cada tabla tiene columnas definidas, y todos los datos deben seguir ese formato. En cambio, MongoDB es más flexible. Cada documento dentro de una colección puede tener campos diferentes, lo que permite adaptarse a cambios sin necesidad de modificar una estructura fija (PureStorage, s.f.).

Por ejemplo:
```json
{
  "nombre": "Lucía",
  "edad": 15,
  "materias": ["Matemáticas", "Física"]
}
```

Este documento puede convivir con otro que tenga campos distintos:
```json
{
  "nombre": "Carlos",
  "ciudad": "Bogotá"
}
```

Este tipo de flexibilidad es una de las razones por las que MongoDB es tan popular en proyectos donde los datos cambian rápido o no tienen una estructura fija.

### 4.2. Escalabilidad y rendimiento

MongoDB también está diseñado para **escalar horizontalmente**, es decir, para funcionar con muchos servidores a la vez. Esto lo hace ideal para manejar grandes cantidades de información. Esta técnica se llama **sharding**, y permite repartir los datos entre diferentes máquinas, manteniendo buen rendimiento incluso con millones de registros (Oracle, s.f.).

MongoDB no es una base de datos SQL. Es parte del grupo de bases de datos NoSQL, caracterizadas por ser más flexibles, rápidas para ciertos usos y fáciles de escalar. Gracias a su modelo basado en documentos, MongoDB permite guardar datos con estructuras variadas, lo que la hace muy útil para proyectos modernos y en constante evolución (PureStorage, s.f.; Oracle, s.f.).

## V. ¿Qué es una API?

Una **API** (por sus siglas en inglés: *Application Programming Interface*, o en español, Interfaz de Programación de Aplicaciones) es un conjunto de reglas que permite que dos programas se comuniquen entre sí. Es como un **puente** que conecta distintos sistemas para que puedan intercambiar información de forma ordenada y segura (IBM, s.f.).

Por ejemplo, imagina que estás en una app de comida a domicilio. Cuando eliges un restaurante y haces un pedido, la app se comunica con el sistema del restaurante para verificar el menú y registrar la orden. Esa comunicación entre la app y el sistema del restaurante ocurre mediante una API (BBVA, s.f.).

Es decir, la API funciona como un **mesero digital**: lleva tu pedido a la cocina (servidor) y regresa con la comida (la información).

Existen varios tipos de APIs, pero algunas de las más comunes son:

- **APIs web**: Funcionan a través de internet usando HTTP. Por ejemplo, las APIs de Google o Twitter.
- **APIs abiertas**: Pueden ser usadas por cualquier persona. También se conocen como *public APIs*.
- **APIs privadas**: Son internas y solo pueden ser usadas dentro de una empresa.

### 5.1. ¿Para qué sirve una API?

Las APIs se usan para:

- Permitir que diferentes programas trabajen juntos.
- Conectar servicios externos, como pasarelas de pago, mapas o redes sociales.
- Automatizar tareas y facilitar el desarrollo de aplicaciones modernas.

Por ejemplo, una API de clima permite que una app muestre el tiempo actual sin tener que medirlo por su cuenta. Solo pide los datos al servicio del clima mediante una API (Red Hat, s.f.).

### 5.2. ¿Cómo funciona una API?

Cuando una aplicación quiere acceder a información o realizar una acción, hace una **solicitud** a la API. Luego, la API responde con los datos pedidos o una confirmación. Este intercambio se realiza con mensajes muy estructurados, casi siempre en formato JSON.

Ejemplo simple de una solicitud a una API:
```
GET https://api.ejemplo.com/usuarios/123
```
Esto pediría los datos del usuario con ID 123.

Una API es una herramienta fundamental para que las aplicaciones modernas funcionen. Permite que diferentes sistemas se entiendan y trabajen juntos, como si hablaran el mismo idioma. Gracias a las APIs, es posible crear apps más completas, rápidas y conectadas (IBM, s.f.; Red Hat, s.f.).

## VI. ¿Qué es Postman?

**Postman** es una herramienta que ayuda a los programadores a trabajar con APIs de forma sencilla y ordenada. Sirve para **probar, crear, organizar y documentar** cómo una aplicación se comunica con otra. Es muy popular porque tiene una interfaz fácil de usar, incluso para quienes están aprendiendo a programar (Postman, s.f.).

Cuando una app necesita pedir datos a un servidor (como obtener el clima, acceder a una cuenta o mostrar un mapa), se usa una API. Con Postman, se puede simular esta comunicación para comprobar si la API está funcionando bien. En lugar de escribir todo en código, Postman permite llenar unos campos, hacer clic en "Enviar" y ver la respuesta que da la API (Formadores IT, 2023).

### 6.1. Características principales

- **Enviar solicitudes HTTP**: como GET, POST, PUT o DELETE. Esto ayuda a ver cómo responde una API ante diferentes acciones.
- **Probar APIs sin escribir código**: ideal para estudiantes o personas que están empezando.
- **Guardar y organizar pruebas**: se pueden crear colecciones con muchas pruebas y guardarlas por proyecto.
- **Automatizar pruebas**: se pueden escribir pequeños scripts para comprobar si la API responde bien bajo ciertas condiciones (Postman, s.f.).
- **Compartir con otros**: se puede invitar a compañeros de equipo y trabajar juntos sobre las mismas pruebas y documentación.

Por ejemplo, imagina que estás haciendo una app que muestra información del clima. Con Postman se puede:

1. Ingresar la dirección de la API del clima.
2. Elegir el tipo de solicitud (por ejemplo, GET).
3. Enviar la petición.
4. Ver si la respuesta tiene los datos que necesitas (como temperatura o humedad).

Así puedes probar todo sin tener que ejecutar el código completo de tu app. Entre las ventajas de usar Postman:
- **Ahorra tiempo** al desarrollar y hacer pruebas.
- **Facilita el aprendizaje** de cómo funcionan las APIs.
- **Ayuda a detectar errores rápido**.
- **Organiza todo en un solo lugar**, lo cual es muy útil para proyectos grandes.
- **Se puede usar en equipo**, lo que mejora la colaboración (Formadores IT, 2023).

Postman no solo sirve para hacer pruebas. También permite:

- Diseñar nuevas APIs desde cero.
- Escribir la documentación que explica cómo usar una API.
- Hacer pruebas automáticas cada vez que cambia el código.
- Supervisar el comportamiento de una API con el tiempo (Postman, s.f.).

Por eso, muchas empresas usan Postman como una herramienta central para todo lo relacionado con sus APIs.

## VII. ¿Qué es el polimorfismo?

En la **programación orientada a objetos (POO)**, el **polimorfismo** es la capacidad que tienen los objetos de diferentes clases para responder al mismo mensaje o método de distintas maneras. Es decir, aunque se utilice una misma interfaz o método, cada objeto puede ejecutar una acción específica según su tipo (El Libro de Python, s.f.).

Existen principalmente dos tipos de polimorfismo:

- **Polimorfismo en tiempo de compilación (estático):** Se refiere a la capacidad de una función o método para comportarse de diferentes maneras según los parámetros que recibe. Un ejemplo común es la **sobrecarga de métodos**, donde varias funciones tienen el mismo nombre pero diferentes listas de parámetros (Ifgeekthen, s.f.).

- **Polimorfismo en tiempo de ejecución (dinámico):** Ocurre cuando una subclase redefine un método de su superclase. En este caso, aunque se invoque el método desde una referencia de la superclase, se ejecutará la versión correspondiente a la subclase (Microsoft Learn, 2023).

### 7.1. Beneficios del polimorfismo

El polimorfismo ofrece varias ventajas en el desarrollo de software:

- **Flexibilidad y reutilización del código:** Permite escribir código más genérico y adaptable, ya que las funciones pueden operar con objetos de diferentes tipos sin necesidad de conocer su implementación específica.

- **Extensibilidad:** Facilita la adición de nuevas clases y funcionalidades sin modificar el código existente, promoviendo un diseño más modular y mantenible (Desarrollo Web, 2021). Por ejemplo:

Imaginemos una clase base llamada `Animal` con un método `hacerSonido()`. Las clases derivadas, como `Perro` y `Gato`, pueden sobrescribir este método para proporcionar su propia implementación:

```python
class Animal:
    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "Ladrido"

class Gato(Animal):
    def hacerSonido(self):
        return "Maullido"

animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hacerSonido())
```

En este ejemplo, aunque se llama al mismo método `hacerSonido()` en cada objeto, cada uno responde de manera diferente según su tipo específico (El Libro de Python, s.f.).

El polimorfismo es un concepto fundamental en la programación orientada a objetos que permite que objetos de diferentes clases respondan al mismo mensaje de maneras específicas. Esto facilita la creación de sistemas flexibles, extensibles y fáciles de mantener (Desarrollo Web, 2021).

## VIII. ¿Qué es un método dunder?

En **Python**, los **métodos dunder** (abreviación de *double underscore*, que significa "doble guion bajo") son funciones especiales que comienzan y terminan con dos guiones bajos. Ejemplos comunes son `__init__`, `__str__`, `__len__` o `__add__`. Python los usa internamente para ejecutar ciertas operaciones automáticas o personalizar el comportamiento de objetos definidos por el usuario (Luis Llamas, s.f.).

### 8.1. ¿Para qué sirven los métodos dunder?

Los métodos dunder permiten que una clase se comporte de manera especial cuando se utilizan ciertas funciones o símbolos. Algunas de sus funciones principales son:

- **Inicializar un objeto**: `__init__` se ejecuta cuando se crea una instancia.
- **Mostrar el objeto como texto**: `__str__` define cómo se imprime un objeto.
- **Sumar, restar y otras operaciones**: `__add__`, `__sub__`, `__mul__`, etc., permiten usar operadores como `+`, `-`, `*`.
- **Acceder a elementos como si fuera una lista**: `__getitem__`, `__setitem__`, `__delitem__`.

Estos métodos hacen que los objetos sean más fáciles de usar y se comporten de forma intuitiva. Por ejemplo:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  
```
En este ejemplo:

- `__init__` define los valores iniciales.
- `__add__` permite usar `+` entre dos vectores.
- `__repr__` muestra el objeto de forma clara al imprimirlo (Luis Llamas, s.f.).

### 8.2. Ventajas de usar métodos dunder

- **Facilitan la lectura del código**: porque permiten que los objetos se comporten como elementos del lenguaje.
- **Hacen las clases más potentes y personalizables**.
- **Se integran mejor con funciones como `print()`, `len()` o con operadores como `+`, `==`, `in`**, entre otros (Netinetidesign, 2022).

Los métodos dunder permiten definir comportamientos especiales en las clases de Python. Gracias a ellos, los objetos pueden ser usados de manera más flexible y natural, como si fueran parte del propio lenguaje. Esto hace que el código sea más limpio, claro y poderoso (Luis Llamas, s.f.; Python Intermedio, s.f.).

## IX. ¿Qué es un decorador en Python?

En **Python**, un **decorador** es una función que permite modificar o extender el comportamiento de otra función o método sin alterar su código original. Esto es posible porque en Python las funciones se pueden tratar como objetos: se pueden pasar como argumentos, retornarse desde otras funciones y guardarse en variables (Platzi, 2024).

Un decorador recibe una función como entrada, define una nueva función (llamada *envoltura* o *wrapper*) que añade alguna funcionalidad, y luego devuelve esa nueva función. De este modo, se puede modificar el comportamiento de la función original sin tener que cambiar su código (Código Facilito, s.f.).

### 9.1. Sintaxis de un decorador

Para aplicar un decorador se utiliza el símbolo `@` justo encima de la definición de la función:
```python
@nombre_del_decorador
def mi_funcion():
    # Código
```

Esto es equivalente a:

```python
def mi_funcion():
    # Código

mi_funcion = nombre_del_decorador(mi_funcion)
```
Por ejemplo:
```python
def mayusculas(funcion):
    def envoltura():
        resultado = funcion()
        return resultado.upper()
    return envoltura

@mayusculas
def saludo():
    return 'Hola, mundo'

print(saludo())  
```

En este caso, el decorador `mayusculas` cambia el texto retornado por la función `saludo` a letras mayúsculas (El Libro de Python, s.f.).

### 9.2. ¿Para qué se usan los decoradores?

Los decoradores son muy útiles cuando se necesita repetir cierta lógica en varias funciones. Algunos usos comunes son:

- **Registrar eventos** (logging): guardar información sobre la ejecución del programa.
- **Controlar el acceso** a funciones sensibles (por ejemplo, verificar si un usuario está autorizado).
- **Medir el tiempo** que tarda una función en ejecutarse.
- **Validar datos** antes de que la función los procese.

Un decorador en Python es una forma elegante de cambiar o ampliar el comportamiento de una función sin modificar su código. Esto permite crear código más limpio, reutilizable y organizado. Por eso, los decoradores se usan mucho en proyectos grandes y en el desarrollo profesional (Platzi, 2024; Código Facilito, s.f.).

## X. Bibliografía

- Ionos. (s.f.). *Clases en Python: definición y ejemplos*. Recuperado el 2 de abril de 2025, de https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/python-classes  
- Python.org. (s.f.). *7. Clases*. Recuperado el 2 de abril de 2025, de https://docs.python.org/es/3.10/tutorial/classes.html
- MyGreatLearning. (s.f.). *Python __init__ method: Everything you need to know*. Recuperado el 2 de abril de 2025, de https://www.mygreatlearning.com/blog/python-init/
- RealPython. (s.f.). *Python Class Constructors: Control Your Object Instantiation*. Recuperado el 2 de abril de 2025, de https://realpython.com/python-class-constructor/
- Udacity. (s.f.). *__init__ in Python: An Overview*. Recuperado el 2 de abril de 2025, de https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html
- Código Facilito. (s.f.). *Verbos HTTP: Qué son y para qué sirven*. Recuperado el 2 de abril de 2025, de https://blog.codigofacilito.com/http-verbs/
- KeepCoding. (s.f.). *Verbos HTTP y operaciones CRUD*. Recuperado el 2 de abril de 2025, de https://keepcoding.io/blog/verbos-http-y-crud/
- Mozilla Developer Network. (s.f.). *Referencia de métodos HTTP*. Recuperado el 2 de abril de 2025, de https://developer.mozilla.org/es/docs/Web/HTTP/Methods
- Oracle. (s.f.). *¿Qué es MongoDB?* Recuperado el 2 de abril de 2025, de https://www.oracle.com/ar/database/mongodb/
- PureStorage. (s.f.). *¿Qué es MongoDB?* Recuperado el 2 de abril de 2025, de https://www.purestorage.com/es/knowledge/what-is-mongodb.html
- BBVA. (s.f.). *¿Qué es una API y cómo funciona?* Recuperado el 2 de abril de 2025, de https://www.bbva.com/es/que-es-una-api-y-como-funciona/
- IBM. (s.f.). *Application Programming Interface (API)*. Recuperado el 2 de abril de 2025, de https://www.ibm.com/es-es/topics/api
- Red Hat. (s.f.). *¿Qué es una API?* Recuperado el 2 de abril de 2025, de https://www.redhat.com/es/topics/api/what-are-application-programming-interfaces
- Postman. (s.f.). *¿Qué es Postman?* Recuperado el 3 de abril de 2025, de https://www.postman.com/product/what-is-postman/
- Postman. (s.f.). *Herramientas de API | Plataforma API de Postman*. Recuperado el 3 de abril de 2025, de https://www.postman.com/product/tools/
- Formadores IT. (2023). *¿Qué es Postman? ¿Cuáles son sus principales ventajas?* Recuperado el 3 de abril de 2025, de https://formadoresit.es/que-es-postman-cuales-son-sus-principales-ventajas/
- Desarrollo Web. (2021). *Polimorfismo en Programación Orientada a Objetos*. Recuperado el 3 de abril de 2025, de https://desarrolloweb.com/articulos/polimorfismo-programacion-orientada-objetos-concepto.html
- El Libro de Python. (s.f.). *Polimorfismo en programación*. Recuperado el 3 de abril de 2025, de https://ellibrodepython.com/polimorfismo-en-programacion
- Ifgeekthen. (s.f.). *Polimorfismo en Java*. Recuperado el 3 de abril de 2025, de https://ifgeekthen.nttdata.com/s/post/polimorfismo-en-java-programacion-orientada-objetos-MCIU2TZFKR6FFIJMDQQASC7CU75I
- Microsoft Learn. (2023). *Polimorfismo - C#*. Recuperado el 3 de abril de 2025, de https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/object-oriented/polymorphism
- Luis Llamas. (s.f.). *Métodos Dunder en Python*. Recuperado el 3 de abril de 2025, de https://www.luisllamas.es/metodos-dunder-python/  
- Netinetidesign. (2022). *Métodos especiales en Python*. Recuperado el 3 de abril de 2025, de https://www.netinetidesign.com/post/metodos-especiales-en-python/  
- Python Intermedio. (s.f.). *17. Clases*. Recuperado el 3 de abril de 2025, de https://python-intermedio.readthedocs.io/es/latest/classes.html
- Código Facilito. (s.f.). *Decoradores en Python*. Recuperado el 3 de abril de 2025, de https://codigofacilito.com/articulos/decoradores-python
- El Libro de Python. (s.f.). *Decoradores*. Recuperado el 3 de abril de 2025, de https://ellibrodepython.com/decoradores-python
- Platzi. (2024). *Decoradores en Python: qué son y cómo funcionan*. Recuperado el 3 de abril de 2025, de https://platzi.com/blog/decoradores-en-python-que-son-y-como-funcionan/
