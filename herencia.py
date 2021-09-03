class Rectanfulo: 
    def __init__ (self, base, altura):
        self.base  = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado (Rectanfulo):
    def __init__ (self, lado):
        super ().__init__(lado,lado)


if __name__ =='__main__':
    rectangulo = Rectanfulo(base = 3, altura= 4)
    print (rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print (cuadrado.area())