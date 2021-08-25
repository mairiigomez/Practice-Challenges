"""Aprendiendo condicionales """

def mayor_edad():
    edad = int(input("Escribe tu edad: "))
    if edad > 17:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

def numero_mayor():
    numero = int(input('Escribe un número: '))

    if numero > 5:
        print('Es mayor a 5')
    elif numero == 5:
        print('Es igual a 5')
    else:
        print('Es menor a 5')

def run():
    print("""Escoge una opción:\n
    \t 1. Saber si eres o no mayor de edad
    \t 2. Saber si un numero es mayor, igual o menor que 5""")
    opcion = input('Tú opcion: ')

    if opcion == 1:
        mayor_edad()
    
    if opcion == 2:
        numero_mayor()


if __name__ == '__main__':
    run()
 