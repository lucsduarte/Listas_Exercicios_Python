# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
#   não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

def raizes(a, b, c):
    if a == 0:
        return print('*** Equação do primeiro grau ***')
    else:
        delta = (b ** 2) - 4 * a * c
        if delta < 0:
            return print('A equação não possui raízes reais')
        elif delta == 0:
            x1 = -1 * (b / 2)
            return print('A raíz única é: {:.2f}'.format(x1))
        else:
            x1 = -1 * (b / 2) + (math.sqrt(delta)) / 2
            x2 = -1 * (b / 2) - (math.sqrt(delta)) / 2
            return print('As raízes são {:.2f} e {:.2f}'.format(x1, x2))


print('Seja a equação de segundo grau na forma ax^2 + bx +c = 0 ...')
a = float(input('Informe o valor de a ... '))
b = float(input('Informe o valor de b ... '))
c = float(input('Informe o valor de c ... '))

raizes(a, b, c)


