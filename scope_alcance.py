def funcion_1(argumento_a,funcion_b):
    def funcion_pequena(otro_arg):
        return otro_arg * 2

    valor = funcion_pequena(argumento_a)
    return funcion_b(valor)

argumento_a = 1

def otra_funcion(x_argumento):
    return x_argumento + 5

funcion_1(argumento_a, otra_funcion)
print(funcion_1)