# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

def conv(farh):
    celsius = 5 * ((farh - 32) / 9)
    return print("Temperatura em Celsius é {:.3f} graus".format(celsius))


fahr = float(input("Temperatura em Fahrenheit a converter para Celsius: "))
conv(fahr)