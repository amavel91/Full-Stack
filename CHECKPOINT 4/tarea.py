#Exercise 1
ingredientes = ['huevo', 'tomate', 'cebolla', 'sal', 'pimienta']
print(ingredientes)
semana = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')
print(semana)
número_flotante = 5.20
print(número_flotante)
número_entero = 22
print(número_entero)

from decimal import Decimal

número_decimal = Decimal('15.89')
print(número_decimal)

cantante_género = {
    'maría': 'balada',
    'pablo': 'llanera',
    'pepe': 'disco',
    'lola': 'salsa',
}
print(cantante_género)

#Exercise 2
import math
número_flotante = 5.20
redondeado = math.ceil(número_flotante)
print(redondeado)

#Exercise 3
raiz = math.sqrt(número_flotante)
print(raiz)

#Exercise 4

primer_elemento = list(cantante_género.keys())[0]
primer_valor = cantante_género[primer_elemento]
print(f"primer_elemento: {primer_elemento}, primer_valor: {primer_valor}")

#Exercise 5
semana = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')
segundo_elemento = semana[1]
print(segundo_elemento)

#Exercise 6
ingredientes = ['huevo', 'tomate', 'cebolla', 'sal', 'pimienta']
ingredientes.append('limón')
print(ingredientes)

#Exercise 7
ingredientes[0] = 'pan'
print(ingredientes)

#Exercise 8
ingredientes.sort()
print(ingredientes)

#Exercise 9
semana += ('fin de semana',)
print(semana)

