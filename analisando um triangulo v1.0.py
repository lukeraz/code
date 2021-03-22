print('Analisador de triangulos!!')
n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o teceiro seguimento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('com esses seguimentos e possivel formar um triangulo')
else:
    print('com esses seguimentos nao sera possivel formar um triangulo.')



