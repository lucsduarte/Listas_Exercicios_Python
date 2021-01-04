# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
# assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
# a - Maior e Menor Acerto;
# b - Total de Alunos que utilizaram o sistema;
# c - A Média das Notas da Turma.


# Função para o professor entrar com gabarito
def gabarito():
    print('Professor, digite o gabarito da prova: ')
    gabarito = []

    for i in range(0, 10):
        alternativa = (input('Questão {}: '.format(i+1))).upper()
        gabarito.append(alternativa)
    return gabarito


# Função que pede os alunos para entrar com suas respostas
def pegar_respostas_aluno():
    respostas_aluno = []

    for i in range(0, 10):
        resp = (input('Resposta da questão {}: '.format(i+1))).upper()
        respostas_aluno.append(resp)
    return respostas_aluno


gabarito = gabarito()
continuar = 'S'
lista_de_notas = []
rodou = 0
while continuar == 'S':
    aluno = input('Nome do aluno: ').title()
    respostas_aluno = pegar_respostas_aluno()
    print('\n\n')
    print(' *** Gabarito ***        *** Resposta {} *** '.format(aluno))
    for i in range(1, 11):
        print('      {} - {}                        {}'.format(i, gabarito[i - 1], respostas_aluno[i - 1]))


    pontos = 0
    for i in range(0, 10):
        if gabarito[i] == respostas_aluno[i]:
            pontos += 1
        else:
            pass
    print('O aluno {} acertou {} questões, sua nota é {}'.format(aluno, pontos, pontos))

    lista_de_notas.append(pontos)
    rodou += 1
    continuar = input('Outro aluno deseja conferir a nota? S/N ').upper()
print('\n\n\n')
print('A maior quantidade de acertou foi: {}'.format(max(lista_de_notas)))
print('A menor quantidade de acertou foi: {}'.format(min(lista_de_notas)))
print('{} alunos utilizaram o sistema'.format(rodou))
media = sum(lista_de_notas)/len(lista_de_notas)
print('A média da turma é {:.2f}'.format(media))






