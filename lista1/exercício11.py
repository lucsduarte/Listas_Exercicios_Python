# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável 'excesso' a quantidade de quilos além do limite e na variável 'multa' o valor da multa
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def calc_multa(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        if excesso == 1:
            print("A multa pelos kilo excedente é: 4 reais")
        else:
            print("A multa pelos {:.2f} kilos excedentes é: {:.2f} reais".format(excesso, multa))
    else:
        print("Peso não excede o limite, então não há multa.")
    return None


peso = float(input("Qual peso do peixe em kilos?: "))
calc_multa(peso)
