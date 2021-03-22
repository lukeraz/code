import  random
print('='* 50)
print('BEM VINDO AO JOKEMPO V1.0')
print('='* 50)
pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
usuario = str(input('escolha entre pedra, papel e tesoura: ')).upper()
print('='*50)
print('ANALISANDO AS ESCOLHAS...')
print('='*50)
print(f'[MAQUINA] {pc} VS {usuario} [VOCE] ')
print('='*50)
if pc == 'PEDRA' and usuario == 'TESOURA':
    print(f'{pc} ganha de {usuario} VOCE PERDEU!')
elif pc == 'TESOURA' and usuario == 'PEDRA':
    print(f'{usuario} ganha de {pc}, PARABENS VOCE GANHOU!!')
elif pc == 'PAPEL' and usuario == 'PEDRA':
    print(f'{pc} ganha de {usuario}, VOCE PERDEU!')
elif pc == 'PEDRA' and usuario == 'PAPEL':
    print(f'{usuario} ganha de {pc}, PARABENS VOCE GANHOU!!')
elif pc == 'TESOURA' and usuario == 'PAPEL':
    print(f'{pc} ganha de {usuario}, VOCE PERDEU!')
elif pc == 'PAPEL' and usuario == 'TESOURA':
    print(f'{usuario} ganha de {pc}, PARABENS VOCE GANHOU!!')
else:
    print('EMPATE!!')