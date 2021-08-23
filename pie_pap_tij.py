"""Versión 1. 15 mayo 2021
Mi first functional code, I remember the excitement after this code worked. 
"""
def run():
    print("""Juguemos piedra papel o tijera
    si quieres elegir piedra ingresa el número 1
    si quieres elegir papel ingresa el número 2
    si quieres elegir tijera ingresa el número 3""")
    
    conteojugador1 = 0
    conteojugador2 = 0 

    for i in range(3):
        jugador1 = int(input("Jugador 1, ¿Cuál es tu elección?: "))
        jugador2 = int(input("Jugador 2, ¿Cuál es tu elección?: "))
        if jugador1 == jugador2:
            print("Nadie obtuvo puntos") 
            conteojugador1 += 0
            conteojugador2 += 0
        elif jugador1 == 1 and jugador2 == 3:
            print("Gana Jugador 1")
            conteojugador1 += 1
            conteojugador2 += 0
        elif jugador1 == 2 and jugador2 == 3:
            print("Gana Jugador 2")
            conteojugador1 += 0
            conteojugador2 += 1
        elif jugador1 == 1 and jugador2 == 2:
            print("Gana Jugador 2")
            conteojugador1 += 0
            conteojugador2 += 1
        elif jugador1 == 3 and jugador2 == 2:
            print("Gana Jugador 1")
            conteojugador1 += 1
            conteojugador2 += 0
        elif jugador1 == 2 and jugador2 == 1:
            print("Gana Jugador 1")
            conteojugador1 += 1
            conteojugador2 += 0
        elif jugador1 == 3 and jugador2 == 1:
            print("Gana Jugador 2")
            conteojugador1 += 0
            conteojugador2 += 1
        else: 
            print("Por favor ingrese una opción correcta")
    
    print('El jugador 1 tiene ' + str(conteojugador1) + ' puntos')
    print('El jugador 2 tiene ' + str(conteojugador2) + ' puntos')

    if conteojugador1 > conteojugador2:
        print("Jugador 1, buen trabajo")
    elif conteojugador1 == conteojugador2:
        print("Han empatado")
    else:
        print("Jugador 2, buen trabajo")
        

if __name__ == '__main__':
    run()  