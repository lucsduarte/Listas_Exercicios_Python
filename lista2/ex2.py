# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

def login(nome, senha):
    while nome == senha:
        print('Nome é igual a senha, tente um nome ou senha diferentes... ')
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
    return print('Nome e senha válidos')


nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
login(nome, senha)
