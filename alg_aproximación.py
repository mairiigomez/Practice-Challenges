objetivo = int(input("Ingresa un entero: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

#La respuesta al cuadrado se está acercando al objetivo mas cercano a 0.01 epsilon
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'no se encontro la raiz cuadrada del {objetivo}')

else:
    print(F"La raiz cuadrada de {objetivo} es {respuesta}")

