# Faça um programa que leia 5 números e informe o maior número.
# Faça um programa que leia 5 números e informe a soma e a média dos números.

def maior_num():                                            # resolvendo com While
    cont = 0
    maior = -99999999999
    while cont < 5:
        num = float(input('informe um numero: '))
        if num > maior:
            maior = num
        cont += 1
    return maior


maior = maior_num()
print(f'O maior numero entre os cinco é o {maior}!')


def soma_cinco():
    i = 0
    soma = 0
    while i < 5:
        num = float(input('Informe um numero: '))
        soma += num
        i += 1
    return soma


soma = soma_cinco()
print('Soma dos números é {}'.format(soma))


#------------------------------------------------------------------------------------------------------

def maior_for():                                                         # resolvendo com for
    maior = -9999999999999
    for i in range(5):
        num = float(input('Entre com um numero: '))
        if num > maior:
            maior = num
    return maior


maior = maior_for()
print('O maior numero entre esses é o {}!'.format(maior))



soma = 0
for i in range(1, 6):
    num = float(input('Entre com um numero: '))
    soma += num

media = soma/5
print('Soma = {}  Média = {}'.format(soma, media))







