# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

p = 0
im = 0

for i in range(1, 11):
    a = int(input('Digite um numero inteiro: '))
    if a % 2 == 0:
        p += 1
    else:
        im += 1

print(f'{p} números pares e {im} números ímpares!')