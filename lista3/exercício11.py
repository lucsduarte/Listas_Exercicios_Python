# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

x = input('Entre com um número: ')
condition = '.' in x
if condition:
    print('*** NÚMERO É DECIMAL ***')
else:
    print('*** NÚMERO É INTEIRO ***')

