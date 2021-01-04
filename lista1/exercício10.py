# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo. (fnc1)
# b) a soma do triplo do primeiro com o terceiro. (fnc2)
# c) o terceiro elevado ao cubo. (fnc3)

def fnc1(int_1, int_2):
    op = (2*int_1)*(int_2/2)
    return print("a) {:.1f}".format(op))


def fnc2(int_1, flt_1):
    op = 3*int_1 + flt_1
    return print("b) {:.1f}".format(op))


def fnc3(flt_1):
    op = flt_1**3
    return print("c) {:.3f}".format(op))


int_1 = int(input("Entre com um numero inteiro: "))
int_2 = int(input("Entre com outro numero inteiro: "))
flt_1 = float(input("Entre com um numero real: "))


fnc1(int_1, int_2)
fnc2(int_1, flt_1)
fnc3(flt_1)







