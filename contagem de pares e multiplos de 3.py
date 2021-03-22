cont = 0
a = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        a = a + c
print(f'A soma de todos os {cont} valores solicitados é: {a}')

