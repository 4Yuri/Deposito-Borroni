"""Crea una classe chiamata Punto.
Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel
piano.
Un metodo muovi che prenda in input un valore per dx e un valore
per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto
dall'origine (0,0) del piano.
"""


import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)
    
mio_punto = Punto(3, 4)
print("Coordinate iniziali: (" + str(mio_punto.x) + ", " + str(mio_punto.y) + ")")

print("Distanza dall'origine: " + str(mio_punto.distanza_da_origine()))

mio_punto.muovi(dx=2, dy=-1)
print("\nNuove coordinate dopo lo spostamento: (" + str(mio_punto.x) + ", " + str(mio_punto.y) + ")")

print("Nuova distanza dall'origine: " + str(mio_punto.distanza_da_origine()))
