def run():
    opcion = int(input(" 1. Kilometros to Millas \n 2. Millas to Kilometros "))
    if opcion == 1:
        kil = int(input("¿Cuántos Kilometros quiere convertir?:  "))
        convertkil = kil/1.609344
        print("Son " + str(convertkil) + " Millas")
    elif opcion == 2:
        mil = int(input("¿Cuántas millas quiere convertir?:  "))
        convertmil = mil*1.609344
        print("Son " + str(convertmil) + " Kilometros")
    else:
        print("Escoja una opción del menú")

if __name__ == '__main__':
    run()