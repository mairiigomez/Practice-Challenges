"""Programa que obtiene el radio de un circulo
y muestra en pantalla diametro, área y circunferencia"""

# Obtener la medida del radio
r = int(input("Enter radius: "))
pi = 3.14159 
d = (2*r)
area = pi * r**2
longitud = 2 * pi * r  

print(f"el diámetro es: {d}. El área es: {area}. La longitud es: {longitud}")