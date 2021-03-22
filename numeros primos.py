n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
        print('\033[1;32m', end=' ')
    else:
        print('\033[1;31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} Foi divisivel {cont} vezes')
if cont == 2:
    print(' é um numero primo.')
else:
    print(f' não é primo.')




