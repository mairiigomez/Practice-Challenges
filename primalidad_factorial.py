"""Un numero primo, solo es divisible por 1 Y por si mismo
código que diga si es primo o no primo, haciendo division entera, residuo 0 
número primo sale la criptografía = ciberseguridad

De qué manera se puede saber si un numero es primo o no 
solución: dividirlo por todos los números primos antes que él"""

from math import factorial

numero = int(input('Ingresa número: '))
resultado = (factorial(numero-1)) + 1 
if numero != 1 and resultado % numero == 0:
    print ('es primo')
else:
    print('Es compuesto')

