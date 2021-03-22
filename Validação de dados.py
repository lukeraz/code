sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Comando invalido, por favor digite apenas [M/F] para definir o seu sexo.')
    else:
        print('Cadastro concluido')

