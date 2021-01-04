# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

def soma(n):
    soma = 0

    for i in range(0, n):
        soma += (i + 1) / (2 * i + 1)
    return print(f'<<< Soma = {soma} >>>')


def mostrar(n):
    string_soma_parcial = ''

    for i in range(0, n - 1):
        string_soma_parcial += f'{i + 1}/{2 * i + 1} + '
    string_soma_final = string_soma_parcial + f'{n}/{2 * n - 1}'
    return print(string_soma_final)


n = int(input('Digite um número: '))
mostrar(n)
soma(n)

