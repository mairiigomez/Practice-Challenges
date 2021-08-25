import math

def areatriangulo(base, height):
    area = (base * height)/2
    print('El area de tu triángulo es:  ' + str(area))
       

def run():
    base = int(input('Escribe la base de tu triángulo:  '))
    height = int(input('Escribe la altura de tu triángulo:  '))
    areatriangulo(base, height)
    lado1 = int(input('Escribe uno de los lados de tu triángulo:  '))
    lado2 = int(input('Escribe el otro lado del triángulo:  '))
    if base == lado1 and base == lado2:
        print('Es un triángulo equilátero')
    elif base == lado1 or base == lado2 or lado1 == lado2:
        print('Es una triángulo isósceles')
    else:
        print('Es un triángulo escaleno')


if __name__ == '__main__':
    run()