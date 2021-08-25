"""Learning about dictionaries, key value pair
How to acces to the value through the key"""

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # Print each value by accesing through the key name
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    try: 
        print(poblacion_paises['Bolivia'])
    except KeyError:
        print('Key does not exist')
        

    # Loop the dictionary just with keys
    for pais in poblacion_paises.keys():
        print(pais)

    # Just with values
    for pais in poblacion_paises.values():
        print(pais)

    #the loop for 'explore' the dictionary, first the key then values
    #key is the country value is the amount of people
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()
