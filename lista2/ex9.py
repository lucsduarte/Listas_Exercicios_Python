# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
"""
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""


def media(notas):
    notas = sorted(notas)
    notas = notas[1:6]
    media = sum(notas) / len(notas)
    return media


def notas():
    notas = []
    for i in range(0, 7):
        nota = float(input('Nota do jurado {}: '.format(i+1)))
        notas.append(nota)
    return notas


nome = (input('Nome do atleta: ').lower()).title()
notas = notas()
media = media(notas)

print('Atleta: {}'.format(nome))
for nota in notas:
    print('Nota: {}'.format(nota))
print('\n\n\n')
print('<<<< resultado final >>>>'.upper())
print('Atleta: {}'.format(nome))
print('Melhor nota: {}'.format(max(notas)))
print('Pior nota: {}'.format(min(notas)))
print('Média: {}'.format(media))
