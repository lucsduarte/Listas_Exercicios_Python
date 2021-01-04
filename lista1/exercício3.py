# Faça um Programa que peça dois números e imprima a soma.

def soma():
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    soma = a + b
    return print("A soma dos números é {}".format(soma))

soma()