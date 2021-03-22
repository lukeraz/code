soma = 0
for c in range(0, 7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma = soma + n1
print(f' A soma dos numeros pares da um total de {soma}')
