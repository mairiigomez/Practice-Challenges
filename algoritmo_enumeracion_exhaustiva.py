objetivo = int(input("escoge un numero entero:  "))
respuesta = 0 

while respuesta**2 < objetivo:
    respuesta += 1 

if respuesta**2 == objetivo:
    print(f"La raiz de {objetivo} es {respuesta} ")
else:
    print(f"{objetivo} no tiene raiz")

"""Other implementation of this algorithm """
it_is_primo = 0
contador = 1
while contador <= objetivo:
    if objetivo % contador == 0:
        it_is_primo += 1
    contador += 1

if it_is_primo == 2:
    print(f"El numero {objetivo} es primmo")

else: 
    print(f"El numero {objetivo} no es primo")