# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada

def tabuada():
    a = int(input('Digite um número e veja sua tabuada: '))
    for i in range(0, 11):
        print(f'{a} x {i} = {a*i}')


print('****** GERADOR DE TABUADA ******')
tabuada()