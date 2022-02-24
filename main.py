from formas import Circulo, Cuadrado, Rectangulo
import random

# c = Cuadrado(1)
# print(c.area())
# print(c)

class Manejador():
    @classmethod
    def get_figura(self, numero):
        if numero == 1:
            return Circulo(random.randint(1,10))
        if numero == 2:
            return Cuadrado(random.randint(1,10))
        if numero == 3:
            return Rectangulo(random.randint(1,10),random.randint(1,10))
        
        raise Exception('El número debe estar entre 1 y 3')

#------------------

figuras = []

for i in range(10):
    figuras.append(Manejador.get_figura(random.randint(1,3)))


# figuras = [Circulo(2), Cuadrado(33),Rectangulo(12,3)]

for f in figuras:
    print(f'La figura {f} tiene un área de {f.area()} y un perímetro de {f.perimetro()}')
