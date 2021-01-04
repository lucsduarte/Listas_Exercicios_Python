# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def mediaf():
    soma = 0
    for i in range(1, 5):
        nota = float(input("digite a nota{}: ".format(i)))
        soma += nota
    media = soma/4
    return print("Média das notas é {m:.4}".format(m=media))

mediaf()

