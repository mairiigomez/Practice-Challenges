"""
Aprendiendo Funciones
Imprimir razones por las cuales aprender python, envia una diferente razon a la funcion
de acuerdo al input del usuario.
"""
def aprendiendopython(razon):
    print("Tomaste una gran decisión")
    print("Vas a probarte a ti mismo")
    print(razon)
    print("vas por buen camino")

variable = input("¿Por qué python: ")
print("""opción 1 : Fácil de aprender 
opción 2 : Data Science 
opción 3 : Machine Learning 
opción 4 : Pensar lógicamente""")

if variable == "1":
    aprendiendopython("Vas a aprenderlo con constancia")
elif variable == "2":
    aprendiendopython("Serás un gran Data Scients")
elif variable == "3":
    aprendiendopython("Vas a enseñar a una computadora")
elif variable == "4":
    aprendiendopython("Nada te quedará grande")
else:
    aprendiendopython("Sabemos vas a encontrar una buena razón")
 




