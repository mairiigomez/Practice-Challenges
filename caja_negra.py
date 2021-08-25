"""Planteamos nuestro test y vamos arreglando el código
de acuerdo a los errores van surgiendo"""
#modulo python que permite crear pruebas

import unittest 

#Creando el test por medio de una clase 

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


#para correr los test tenemos que definir que es un modulo principal

if __name__ == '__main__':
    unittest.main()



