# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.
"""
                    Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

"""


def preco_total(tipo_carne):

    def cartao():
        resp = (input('Vai ser pago com cartão Tabajara? ')).capitalize()
        if resp == 'Sim':
            return True
        else:
            return False

    if tipo_carne.count('File') == 1:
        if qtd_carne > 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 5.8 * 0.05 + qtd_carne * 5.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 5.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
        if qtd_carne <= 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 4.9 * 0.05 + qtd_carne * 4.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 4.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))

    if tipo_carne == 'Alcatra':
        if qtd_carne > 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 6.8 * 0.05 + qtd_carne * 6.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 6.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
        if qtd_carne <= 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 5.9 * 0.05 + qtd_carne * 5.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 5.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))

    if tipo_carne == 'Picanha':
        if qtd_carne > 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 7.8 * 0.05 + qtd_carne * 7.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 7.8
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
        if qtd_carne <= 5:
            cartao = cartao()
            if cartao:
                preco_pagar = qtd_carne * 6.9 * 0.05 + qtd_carne * 6.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))
            else:
                preco_pagar = qtd_carne * 6.9
                print('Sua compra deu R$ {:.2f}'.format(preco_pagar))


tipo_carne = (input('Qual tipo de carne comprada? ')).capitalize()
qtd_carne = float(input('Qual a quantidade em kilos de {} comprada? '.format(tipo_carne)))
preco_total(tipo_carne)

