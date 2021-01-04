""" O cardápio de uma lanchonete é o seguinte:

         Especificação        Código        Preço
        Cachorro Quente        100         R$ 1,20
         Bauru Simples         101         R$ 1,30
         Bauru com ovo         102         R$ 1,50
          Hambúrguer           103         R$ 1,20
         Cheeseburguer         104         R$ 1,30
         Refrigerante          105         R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
"""


def imprimir_cardapio():
    print('  Especificação         Código         Preço'.upper())
    print(' Cachorro Quente         100          R$ 1,20 ')
    print('  Bauru Simples          101          R$ 1,30 ')
    print('  Bauru com Ovo          102          R$ 1,50 ')
    print('   Hambúrguer            103          R$ 1,20 ')
    print('  Cheeseburguer          104          R$ 1,30 ')
    print('  Refrigerante           105          R$ 1,00 ')


imprimir_cardapio()

pedido = []
nota = {}
adicionar = 'S'

print('\n')
print('faça seu pedido'.upper())

while adicionar == 'S':
    codigo = input('Código da Especificação: ')
    if 100 <= int(codigo) <= 105:
        quantidade = int(input('Quantidade: '))
        if int(codigo) == 100:
            print('Adicionado Cachorro Quente')
            produto = round(quantidade*1.2, 2)
            pedido.append(produto)
            nota['Cachorro Quente'] = produto
        elif int(codigo) == 101:
            print('Adicionado Bauru Simples')
            produto = round(quantidade * 1.3, 2)
            pedido.append(produto)
            nota['Bauru Simples'] = produto
        elif int(codigo) == 102:
            print('Adicionado Bauru com Ovo')
            produto = round(quantidade * 1.5, 2)
            pedido.append(produto)
            nota['Bauru com Ovo'] = produto
        elif int(codigo) == 103:
            print('Adicionado Hambúrguer')
            produto = round(quantidade * 1.2, 2)
            pedido.append(produto)
            nota['Hambúrguer'] = produto
        elif int(codigo) == 104:
            print('Adicionado Cheeseburguer')
            produto = round(quantidade * 1.3, 2)
            pedido.append(produto)
            nota['Cheeseburguer'] = produto
        else:
            print('Adicionado Refrigerante')
            produto = quantidade*1.00
            pedido.append(produto)
            nota['Refrigerante'] = produto
    else:
        print('*** CÓDIGO INVÁLIDO ***')
        pass
    adicionar = input('Deseja pedir mais alguma coisa? S/N ').upper()


print('\n')
print('------ NOTA FISCAL ------')

for chave, valor in nota.items():
    print('Gasto em', chave, ': ', valor)

print(f'            Total        R$ {sum(pedido)}')





















