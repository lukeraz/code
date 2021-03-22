velocidade = float(input('Em qual velocidade em km/h voce esta agora? '))
if velocidade >80:
    print(f'voce ultrapassou a velocidade permitida, sua multa é de R${(velocidade - 80) * 7}')
else:
    print('voce esta dentro da velocidade permitida.')