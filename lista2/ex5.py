# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
# Faça um programa que receba dois números inteiros e gere os números
#  inteiros que estão no intervalo compreendido por eles


def impares():
    for i in range(1, 50, 2):  # numeros ímpares até 50
        print(i)


def intervalo():
    a = int(input('Entre com um numero: '))
    b = int(input('Entre com outro numero: '))
    for i in range(a + 1, b):
        print(i)


impares()
intervalo()

