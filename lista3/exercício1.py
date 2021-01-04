# Faça um Programa que peça dois números e imprima o maior deles.

def maior(a, b):
    if a > b:
        print("O numero {:.2f} é maior que o numero {:.2f}".format(a, b))
    else:
        print("O numero {:.2f} é menor que o numero {:.2f}".format(a, b))


a = float(input("Digite um número a: "))
b = float(input("Digite um número b: "))

maior(a, b)



