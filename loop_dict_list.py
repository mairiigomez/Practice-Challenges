"""Diferent ways to loop through a super list and super dictionaries """

def run():

    my_superlist = [
        {"First_name": "Mairi", "last_name": "Gomez"},
        {"First_name": "Rosita", "last_name": "Pushaina"},
        {"First_name": "Jose", "last_name": "Vega"},
    ]

    my_superdict = {
        "valor_entero": [1,2,3,4],
        "valor_flotante": [0.5, 0.6, 1.5]
    }
    print("===============================================================")
    print("Looping key and value pair in the super dictionary")
    for key, value in my_superdict.items():
        print(key, "-", value)

    print("===============================================================")
    print("Looping the super list and each item in the super list is a dict")
    for data in my_superlist:
       for key, value in data.items():
           print(key, "-", value)
    
    print("===============================================================")
    print("Just looping the superlist and it print the complete dict")
    for value in my_superlist:
        print(value)
    
    print("===============================================================")
    print("Lookk for the key and value individually in each item of the super list")
    for i in my_superlist:
        print(i["First_name"], "-", i["last_name"])
    
    print("===============================================================")
    print("print the items together without looping of the item in the superlist")
    for i in my_superlist:
        print(i.items())
    
    print("===============================================================")
    print("Looping through the super list print just value")
    for values in my_superlist:
        for key, value in values.items():
            '''Deshabilitar el salto de linea entre los valores
            se especifica un string de espacio vacio con el argumento
            end''' 
            print(value), end= ' ')
        '''el argumento sep indica un separador de los elementos
        a imprimir, en este caso un salto de linea para separar
        elementos del super list'''
        print('', sep='\n')

if __name__ == '__main__':
    run()