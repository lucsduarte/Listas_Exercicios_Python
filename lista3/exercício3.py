# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def vog_con(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        print("{} é vogal".format(a))
    else:
        print("{} é consoante".format(a))


a = input("Digite uma letra, saiba se ela é vogal ou consotante: ")
vog_con(a)

