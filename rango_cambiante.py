def run():
    limite_inferior = int(input("Ingrese su límite inferior:  "))
    limite_superior = int(input("Ingrese su límite superior:  "))
    comparacion = int(input("Ingrese su número de comparación:  "))
    bandera = True

    while bandera == True : 
        if comparacion >= limite_inferior and comparacion <= limite_superior:
            print(comparacion)
            bandera = False
        else:
            print(comparacion)
            comparacion = int(input("Por favor ingrese otro número:  "))
            bandera = True


if __name__ == '__main__':
    run()