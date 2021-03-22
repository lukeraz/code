nome = str((input("Digite o seu nome: "))).strip()

print('Analisando o seu nome...')
print(f'Seu nome em maiusculas {nome.upper()}')
print(f'Seu nome em minusculas {nome.lower()}')
print(f'A quantidade de letras que seu nome tem {len(nome) - nome.count(nome)} ')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')

