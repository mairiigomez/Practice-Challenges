"""Aprendiendo asserts 
El assert asegura que algo es cierto y sino levanta un assertion error, que esta escrito
después de la ',' coma. Y lo mandamos al except part del código"""

def primera_letra(list):
    primeras_letras = []

    for palabra in list:
        try:
            # Afirmo que esto y sino mando una assert error y los
            #imprimo en el bloque except
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, 'No se permiten vacíos'
            # Si la palabra lo hace hasta este punto se agrega a la lista
            # solo el primer digito
            primeras_letras.append(palabra[0])

        except AssertionError as e:
            print(e)

    return primeras_letras

lista = ['Rosmaira', 5.5, '', 2, '43434', 0.35]
# Antes de imprimir va a la función y ejecutar el código y al final
# ejecuta el print y lo que la función retorna
print('Primeras letras validas son: ', primera_letra(lista))