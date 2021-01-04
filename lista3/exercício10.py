# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural, exemplo
# 326 = 3 centenas 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

numero = input('Entre com um numero inteiro entre maior ou igual a 1 e menor ou igual a 999. ')
if len(numero) > 3:
    print('**** VALOR NAO PERMITIDO *****')
elif int(numero) <= 0:
    print('**** VALOR NAO PERMITIDO *****')
else:
    if len(numero) == 1:
        if int(numero) == 1:
            print('{} = {} unidade'.format(numero, numero))
        else:
            print('{} = {} unidades'.format(numero, numero))

    elif len(numero) == 2 and int(numero[0]) == 1:
        if int(numero[1]) == 1:
            print('{} = {} dezena e {} unidade'.format(numero, numero[0], numero[1]))
        else:
            print('{} = {} dezena e {} unidades'.format(numero, numero[0], numero[1]))

    elif len(numero) == 2:
        if int(numero[1]) == 1:
            print('{} = {} dezenas e {} unidade'.format(numero, numero[0], numero[1]))
        else:
            print('{} = {} dezenas e {} unidades'.format(numero, numero[0], numero[1]))

    else:
        if int(numero[0]) == 1:
            if int(numero[1]) == 1 and int(numero[2]) == 1:
                print('{} = {} centena {} dezena e {} unidade'.format(numero, numero[0], numero[1], numero[2]))
            elif int(numero[1]) == 1:
                print('{} = {} centena {} dezena e {} unidades'.format(numero, numero[0], numero[1], numero[2]))
            elif int(numero[2]) == 1:
                print('{} = {} centena {} dezenas e {} unidade'.format(numero, numero[0], numero[1], numero[2]))
            else:
                print('{} = {} centena {} dezenas e {} unidades'.format(numero, numero[0], numero[1], numero[2]))

        elif int(numero[1]) == 1:
            if int(numero[2]) == 1:
                print('{} = {} centenas {} dezena e {} unidade'.format(numero, numero[0], numero[1], numero[2]))
            else:
                print('{} = {} centenas {} dezena e {} unidades'.format(numero, numero[0], numero[1], numero[2]))

        elif int(numero[2]) == 1:
            print('{} = {} centenas {} dezenas e {} unidade'.format(numero, numero[0], numero[1], numero[2]))

        else:
            print('{} = {} centenas {} dezenas e {} unidades'.format(numero, numero[0], numero[1], numero[2]))




