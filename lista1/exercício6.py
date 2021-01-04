# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

def area():
    raio = float(input("Dê o raio de um círculo para saber sua área: "))
    area = math.pi * raio**2
    return print("Area do circulo é {:.3f}".format(area))

area()
