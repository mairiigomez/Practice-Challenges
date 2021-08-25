"""Calcular la potencia de 2 hasta que la potencia sea menor que 1000"""

def run():
    LIMITE = 1000

    contador = 0 
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f"La potencia de 2 por {contador} es {potencia_2}")
        contador = contador + 1 
        potencia_2 = 2**contador       

if __name__ == '__main__':
    run()