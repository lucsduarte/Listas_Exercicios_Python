# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = float(input("Entre com um primeiro numero: "))
b = float(input("Enter com um segundo numero: "))
c = float(input("Enter com um terceiro numero: "))

lista = [a, b, c]
lista.sort(reverse=True)
print("Em ordem decrescente os números são: {}".format(lista))


