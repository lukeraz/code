cont = 0
n1 = int(input('Digite um numero de 1 a 10 para ver a taboada do mesmo: '))
for c in range(1, 11):
    cont = cont +1
    m = n1 * c
    print(f'{n1} x {cont} = {m}')