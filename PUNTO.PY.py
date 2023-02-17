import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def mostrar(self):
        print(f"coordenadas del punto x:,{self.x}coordenadas del punto y : {self.y}")


    def mover(self, nuevo_x, nuevo_y):
        self.x += nuevo_x
        self.y += nuevo_y


    def calcular_distancia(self, punto_2x, punto_2y):
        distancia = math.sqrt((punto_2x - x) ** 2 + (punto_2y - y) ** 2)
