# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
# a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. Desconto do IR:
# - Salário Bruto até 900 (inclusive) - isento
# - Salário Bruto até 1500 (inclusive) - desconto de 5%
# - Salário Bruto até 2500 (inclusive) - desconto de 10%
# - Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""     Salário Bruto:                  : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""


def salario_bruto():
    valor_por_hora = float(input('Quanto ganhas por horas? '))
    horas_trabalhadas = float(input('Quantas horas trabalhaste? '))
    sal_bruto = valor_por_hora*horas_trabalhadas
    return sal_bruto


def desconto_impostorenda(sal_bruto):
    if sal_bruto <= 900:
        desc_ir = 0
    elif sal_bruto > 900 and sal_bruto <= 1500:
        desc_ir = sal_bruto*0.05
    elif sal_bruto > 1500 and sal_bruto <= 2500:
        desc_ir = sal_bruto*0.1
    else:
        desc_ir = sal_bruto*0.2
    return desc_ir


def desconto_inss(sal_bruto):
    desc_inss = sal_bruto*0.1
    return desc_inss


def desconto_sindicato(sal_bruto):
    desc_sindicato = sal_bruto*0.03
    return desc_sindicato


def fgts(sal_bruto):
    fgts = sal_bruto*0.11
    return fgts


sal_bruto = salario_bruto()
descIR = desconto_impostorenda(sal_bruto)
descInss = desconto_inss(sal_bruto)
descSind = desconto_sindicato(sal_bruto)
fgts = fgts(sal_bruto)
salario_liquido = sal_bruto - descSind - descInss - descIR

print('                  ********* FOLHA DE PAGAMENTO *********')
print('    SALÁRIO BRUTO -------------------------------------- R$ {:.2f}'.format(sal_bruto))
print('    FGTS (3%) ------------------------------------------ R$ {:.2f}'.format(descSind))
print('(-) IR (5%) -------------------------------------------- R$ {:.2f}'.format(descIR))
print('(-) INSS (10%) ----------------------------------------- R$ {:.2f}'.format(descInss))
print('(-) SINDICATO (3%) ------------------------------------- R$ {:.2f}'.format(descSind))
print('    TOTAL DE DESCONTOS --------------------------------- R$ {:.2f}'.format(descSind+descIR+descInss))
print('    SALÁRIO LIQUIDO ------------------------------------ R$ {:.2f}'.format(salario_liquido))
