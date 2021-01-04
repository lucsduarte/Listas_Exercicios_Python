# Faça um Programa que peça um valor e mostre na tela se o valor é positivo, negativo o zero


def pos_neg(a):
    if a > 0:
        print("Numero positivo")
    elif a < 0:
        print("Numero negativo")
    else:
        print("Numero é igual a zero")


a = float(input("Entre com um numero para saber se ele é positivo, negativo ou zero: "))
pos_neg(a)
