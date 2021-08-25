"""Funciones como objetos, complicado pero interesante
- Mandandolas como argumento, usando lambda y integrándolas en una estructura
de datos (lista)
"""
#Argumentos de otras funciones# 
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f,numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return(resultados)

nums = [1,2,3]
# Cuando llamamos a la función le pasamos otra función como argumento
print(aplicar_operacion(multiplicar_por_dos,nums))

#Funciones en expresiones#
sumar = lambda a,b : a + b
print(sumar(5,6))

#Funciones en estructuras de datos
def aplicar_operaciones(num):
    # Se le aplica valor absoluto y convertirlo a float
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    
    return resultado

print(aplicar_operaciones(-2))
