# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def perguntas():
    p1 = ((input("Telefonou para a vítima? ")).lower()).capitalize()
    p2 = ((input("Esteve no local do crime? ")).lower()).capitalize()
    p3 = ((input("Mora perto da vítima? ")).lower()).capitalize()
    p4 = ((input("Devia para a vítima? ")).lower()).capitalize()
    p5 = ((input("Já trabalhou com a vítima? ")).lower()).capitalize()
    respostas = [p1, p2, p3, p4, p5]
    return respostas


def analise(respostas_positivas):
    if respostas_positivas <= 1:
        print('*** INOCENTE ***')
    elif respostas_positivas == 2:
        print('*** SUSPEITA ***')
    elif respostas_positivas <= 4:
        print('*** CÚMPLICE ***')
    else:
        print('*** ASSASSINO ***')


respostas = perguntas()
respostas_positivas = respostas.count('Sim')
analise(respostas_positivas)











