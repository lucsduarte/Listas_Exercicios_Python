# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = float(input("Entre com o primeiro numero: "))
b = float(input("Entre com o segundo numero: "))
c = float(input("Entre com o terceiro numero: "))

numbers = [a, b, c]
print("O maior número entre eles é {} e o menor é {}.".format(max(numbers), min(numbers)))

