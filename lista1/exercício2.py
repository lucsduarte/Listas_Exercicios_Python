# Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]"

def insira_numero():
    numero = int(input("Insira um numero: "))
    return numero                                       # A função precisa retornar um valor

def print_numero(numero):
    return print("O numero informado foi: {}".format(numero))

numero = insira_numero()
print_numero(numero)

