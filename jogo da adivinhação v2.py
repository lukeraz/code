from random import randint
maquina = randint(0, 10)
print('Seja bem vindo ao jogo de adivinhação 2.0, estarei pensando em um numero de 0 a 10, tente adivinhar')
n = 0
c = 0
while n != maquina:
    n = int(input('Digite um numero de 0 a 10: '))
    if n != maquina:
        c += 1
        print('Voce errou, tente novamente.')
    else:
        print(f'Parabens, voce ganhou com {c + 1} palpites.')

