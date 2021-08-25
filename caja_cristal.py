"""Desarrollar test que verifiquen que la función se comporta
de la manera correcta """
import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    elif edad < 18:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_mayor_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)  

        self.assertEqual(resultado, True) 

    def test_menor_edad(self):
        edad = 15

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, False)
     

#si el nombre del script es mainn y solo es main cuando se ejecuta
#directamente desde el script ejecuta el código

if __name__ == '__main__':
    unittest.main()