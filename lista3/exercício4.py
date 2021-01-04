# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.


def media(nt_1, nt_2):
    media = (nt_1 + nt_2) / 2
    return media


def resultado(media):
    if media == 10:
        print("Aprovado com distinção!")
    elif media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")


nt_1 = float(input("Entre com a nota 1: "))
nt_2 = float(input("Entre com a nota 2: "))

resultado(media(nt_1, nt_2))

