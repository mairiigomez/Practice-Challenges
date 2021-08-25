"""Iterar entre dos while loops
Mientras la condicion del primer while sea verdad, 
ejecutar el segundo while y resetear el segundo while 
para que vuelva entrar en la segunda iteración """

contador_1 = 0
contador_2 = 0

while contador_1 <= 10:
    while contador_2 <10:
        print(contador_1, contador_2)
        contador_2 += 1
    contador_1 += 1 
    contador_2 = 0
