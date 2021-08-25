"""Algoritmo de búsqueda binaria, uno de los más importantes de CS
Requisitos: 1. Nuestro conjunto de búsqueda tiene que estar ordenado
***Cortar nuestro espacio de búsqueda a la mitad cada vez
"""
import time
start = time.time()
objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
#limite inferior
bajo = 0.0
#max nos regresa el valor más alto entre dos valores
#regresa 1.0 o el objetivo, si el objetivo es menor a 1.0
#regresa y empieza directamente 1.0 
alto = max(1.0, objetivo)
#algoritmo 
respuesta = (alto + bajo) / 2
#funcion abs absolute value para encontrar valores absolutos
#nos estamos acercando al objetivo y para no pasarnos usamos
#la condición que cuando sea mayor que epsilon es porque todavía
#el numero elevado a la dos esta lejos del numero ingresado por 
#el usuario 

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo} alto={alto} respuesta={respuesta}')

    ## si respuesta al cuadrado si nuestro número medio al cuadrado
    # es menor que el objetivo el numero del usuario ahora empieza
    #a buscar desde respuesta para arriba entonces asigna el limite
    ## inferior al valor de respuesta 
    if respuesta**2 < objetivo:
        bajo = respuesta
    #de lo contrario si es muy alto que nuestro limite más alto sea
    #respuesta 
    else:
        alto = respuesta
    
    #reasigna el valor de respuesta 
    
    respuesta = (alto + bajo) / 2

end = time.time()

print(f"Runtime of the program is {end-start}")
print(f"La raiz cuadrada de {objetivo} es {respuesta}")

