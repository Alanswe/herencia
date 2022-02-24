import unittest
from formas import Circulo, Forma, Rectangulo, Cuadrado
from math import pi

class Test_formas(unittest.TestCase):

    def test_existencia(self):
        f = Forma()
        self.assertNotEqual(f,None)
        self.assertIsNotNone(f)

    def test_nombre_forma(self):
        f = Forma()
        self.assertEqual(f.__str__(),'Forma')

class Test_Circulo(unittest.TestCase):

    def test_existencia(self):
        c = Circulo(1)
        self.assertIsNotNone(c)
    
    def test_area(self):
        c = Circulo(1)
        area = c.area()
        self.assertEqual(area,3.141592653589793)
        self.assertEqual(area,pi)

    def test_perimetro(self):
        c = Circulo(1)
        perimetro = c.perimetro()
        self.assertEqual(perimetro,6.283185307179586)
        self.assertEqual(perimetro,2*pi)

    def test_radio_negaivo_2(self):
        with self.assertRaises(Exception):
            Circulo(-1)

class Test_rectangulo(unittest.TestCase):
    def test_existencia(self):
        re = Rectangulo(10,20)
        self.assertIsNotNone(re)

    def test_perimetro(self):
        re = Rectangulo(10,20)
        perimetro = re.perimetro()
        self.assertEqual(perimetro,60)

class Test_cuadrado(unittest.TestCase):
    
    def test_existenica(self):
        cua = Cuadrado(1)
        self.assertIsNotNone(cua)

    def test_lado_1_perimetro(self):
        cua = Cuadrado(1)
        perimetro = cua.perimetro()
        self.assertEqual(perimetro,4)

    def test_area_lado_1(self):
        cua = Cuadrado(1)
        area = cua.area()
        self.assertEqual(area,1)
