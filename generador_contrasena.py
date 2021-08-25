"""Generar una contrasea con el módulo random
1. Mezcla todas las letras y caracteres en una variable
2. Escoge una caracter random en un ciclo de 15 veces
3. Lo agrega cada vez a una lista
4. Lo convierte en string con .join()
5. Muestra la contraseña al usario """

import random

def generar_contrasena():
    """Function to generate the random password"""

    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    """Main function that runs in the program"""
    
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
