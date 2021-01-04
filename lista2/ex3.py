# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

def ano_necessarios(a, b):
    i = 0
    while b > a:
        a += a*0.03
        b += b*0.015
        i += 1
    return print('Foram necessários {} anos para a população de A se igualar a de B!'.format(i))


a = 80000
b = 200000
ano_necessarios(a, b)



