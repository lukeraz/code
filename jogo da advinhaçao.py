import random
n = int(input('Seja bem vindo ao jogo de adivinhação... estou pensando em um numero de 0 a 5 tente adivinhar. '))

lista = [0, 1, 2, 3, 4, 5]
if n == 5:
    print('Parabens!! voce acertou!!!')
else:
    print('Voce errou! esta me devendo uma coca!!')