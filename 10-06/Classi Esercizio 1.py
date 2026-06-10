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
    
