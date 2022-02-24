from math import pi

class Forma():
    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self) -> str:
        return type(self).__name__

class Circulo(Forma):
    def __init__(self,radio) -> None:
        if type(radio) in (int,float) and radio > 0:
                self.radio = radio
        else:
            raise Exception('El radio ser un número positivo \n...O simplemente un número ¡Zoquete!')

    def area(self):
        return pi * self.radio * self.radio

    def perimetro(self):
        return 2 * pi * self.radio

class Rectangulo(Forma):
    def __init__(self,base,altura) -> None:
        self.__base = base
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)        

class Cuadrado(Rectangulo):
    def __init__(self,lado) -> None:
        super().__init__(lado, lado)

    # def area(self):
    #     return super().area()

    # def perimetro(self):
    #     return super().perimetro()
