# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# Faça um programa que gere a série até que o valor seja maior que 500.

n = int(input('Entre com a qtd de termos da sequência de Fibonacci: '))
seq = [0, 1]
for i in range(1, n - 1):
    num = seq[i] + seq[i - 1]
    seq.append(num)
print(f'A sequência de Fibonacci até termo {n} é {seq}')

# ----------------------------------------------------------------------------------

seq = [0, 1]
m = 1
while seq[m] <= 500:
    num = seq[m] + seq[m - 1]
    seq.append(num)
    print(seq)
    m += 1

