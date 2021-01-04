# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.

salario = float(input("Qual seu salario? "))

if salario <= 280.0:
    sal_aumentado = salario + salario*0.2
    print("Seu salário era {}, foi aumentado 20% o que é {}, novo salario é {}.".format(salario, salario*0.2,
                                                                                        sal_aumentado))
elif salario > 280 and salario <= 700:
    sal_aumentado = salario + salario*0.15
    print("Seu salário era {}, foi aumentado 15% o que é {}, novo salario é {}.".format(salario, salario * 0.15,
                                                                                        sal_aumentado))
elif salario > 700 and salario <= 1500:
    sal_aumentado = salario + salario*0.1
    print("Seu salário era {}, foi aumentado 10% o que é {}, novo salario é {}.".format(salario, salario * 0.1,
                                                                                        sal_aumentado))
else:
    sal_aumentado = salario + salario*0.05
    print("Seu salário era {}, foi aumentado 5% o que é {}, novo salario é {}.".format(salario, salario * 0.05,
                                                                                        sal_aumentado))

