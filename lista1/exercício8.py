# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.


def salario(por_hora, horas_mes):
    sal = por_hora*horas_mes
    return print("Salário é {:.2f} unidades monetarias".format(sal))


por_hora = float(input("Quantas unidades monetarias voce ganha por hora trabalhada? "))
horas_mes = float(input("Quantas horas você trabalhou no mês? "))
salario(por_hora, horas_mes)
