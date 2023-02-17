class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1=punto1
        self.punto2=punto2

    def perimetro(self,punto1,punto2):
        perimetro=2*(punto1+punto2)

    def area(self,punto1,punto2):
        area=punto1*punto2

    def cuadrado(self,punto1,punto2):
        if punto1==punto2:
            print("es un cuadrado")
        else:
            print("no es un cuadrado")
