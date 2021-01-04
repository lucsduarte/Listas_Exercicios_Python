# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
# informados também pelo usuário, conforme exemplo abaixo:

"""
    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
"""


def mensagem():
    print('\n')
    print('Montar a tabuada de: {}'.format(num_tabuada))
    print('Começar por: {}'.format(iniciando))
    print('Terminar em: {}'.format(finaliza))


def tabuada(num_tabuada):
    i = iniciando
    while i <= finaliza:
        print(f'{num_tabuada} x {i} = {num_tabuada*i}')
        i += 1



num_tabuada = int(input('Tabuada do número... '))
iniciando = int(input('Inicia em: '))
finaliza = int(input('Termina em: '))

if finaliza > iniciando:
    mensagem()
    print('\n')
    print('Vou montar a tabuada do {} começando em {} e terminando em {}'.format(num_tabuada, iniciando, finaliza))
    tabuada(num_tabuada)

else:
    print('*** INVÁLIDO ***')



