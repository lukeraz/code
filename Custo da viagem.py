viagem = float(input('Digite a distancia da sua viagem em km: '))
if viagem <=200:
    print(f'A sua viagem de {viagem}KM fica R${viagem * 0.50}')
else:
    print(f'A sua viagem de {viagem}KM fica R${viagem * 0.45} ')