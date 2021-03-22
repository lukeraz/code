r = ''
while r == '5':
    n = int(input('Digite um valor: '))
    r = str(input('''Opções
             [1] SOMAR
             [2] MULTIPLICAR
             [3] NUMERO MAIOR
             [4] NOVOS NUMEROS
             [5] SAIR              : '''))
    n2 = int(input('Digite outro valor: '))
    if r == 1:
        soma = n + n2
        print(f'O resultado da soma deu {soma}')
    if r == 2:
        multiplicar = n * n2
        print(f'O resultado da multiplicação deu {multiplicar}')
    if r == 3:
        if n > n2:
            print(f' O numero maior é {n}')
        else:
            print(f'O numero maior é {n2}')




