# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido

def salario(por_hora, horas_mes):
    sal = por_hora*horas_mes
    return sal

def inss(sal):
    desc_inss = sal*0.08
    return desc_inss

def imp_renda(sal):
    desc_imp_renda = sal*0.11
    return desc_imp_renda


def sindicato(sal):
    desc_sindicato = sal*0.05
    return desc_sindicato


por_hora = float(input("Quantas unidades monetarias voce ganha por hora trabalhada? "))
horas_mes = float(input("Quantas horas você trabalhou no mês? "))
sal = salario(por_hora, horas_mes)
sal_liquido = sal - inss(sal) - imp_renda(sal) - sindicato(sal)
print("O salário bruto é {:.2f}".format(sal))
print("O desconto do INSS é {:.2f}".format(inss(sal)))
print("O desconto do Imposto de renda é {:.2f}".format(imp_renda(sal)))
print("O desconto do sindicato é {:.2f}".format(sindicato(sal)))
print("O salário líquido é {:.2f}".format(sal_liquido))



