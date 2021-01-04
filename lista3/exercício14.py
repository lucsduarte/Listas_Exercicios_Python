# Faça um Programa que peça um número correspondente a um determinado ano
# em seguida informe se este ano é ou não bissexto.

def bissexto(ano):
    if ano % 4 == 0:
        if not (ano % 100 == 0):
            print('O ano {} é bissexto.'.format(ano))
        elif ano % 400 == 0:
            print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))


ano = int(input('Digite o ano para saber se ele é bissexto: '))
bissexto(ano)


