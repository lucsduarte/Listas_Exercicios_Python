# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:

""" Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120 """


def fat(numero_fatorial):
    fatorial = 1

    for i in range(1, numero_fatorial + 1):
        fatorial = fatorial*i
    return fatorial


def imprimir(numero_fatorial, fatorial):
    i = numero_fatorial
    mensagem = ''

    while i >= 2:
        mensagem += f'{i} . '
        i -= 1
    mensagem_final = f'{numero_fatorial}! = ' + mensagem + f'1 = {fatorial}'
    print(f'FATORIAL DE: {numero_fatorial}')
    print(mensagem_final)


numero_fatorial = int(input('Digite um numero inteiro para saber seu fatorial: '))
fatorial = fat(numero_fatorial)
imprimir(numero_fatorial, fatorial)

