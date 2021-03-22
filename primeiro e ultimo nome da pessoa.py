nome = str(input('insira o seu nome: ')).strip()

print(f'O primeiro nome {nome.split()[0]}')
print(f'O segundo nome {nome.rsplit(maxsplit=1)[1]}')