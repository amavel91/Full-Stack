#Ejercicio 1
comidas = ["pollo", "res", "cerdo", "pavo", "pescado", "vegetariano"]

for comida in comidas:
    print("El  menú para hoy será", comida + "!")

#Ejercicio 2
def ganancias(a, b, c):
    resultado = a + b + c
    return resultado

resultado = ganancias(40, 50, 35)
print("La ganacia total es de", resultado)

#Ejercicio 3
ganancias_lambda = lambda a, b, c : a + b + c

resultado = ganancias_lambda(40, 50, 35)
print("La ganacia total es de", resultado)

#Ejercicio 4
nombre = 'Enrique'
lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombre:
    print("El nombre", nombre, "está en la lista.")
else:
    print("El nombre", nombre, "NO está en la lista.")
