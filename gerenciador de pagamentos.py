valor = float(input('Digite o valor do seu produto: '))
dinheiro = (valor * 10) / 100
cartao = (valor * 5) / 100

print('='*20)
print('FORMAS DE PAGAMENTOS')
print('='*20)
opc = int(input('DIGITE... \n'
      '[1] PAGAMENTO A VISTA NO DINHEIRO/CHEQUE - 10% DE DESCONTO \n'
      '[2] PAGAMENTO  A VISTA NO CARTAO - 5% DE DESCONTO \n'
      '[3] PAGAMENTO DIVIDIDO EM ATÉ 2X NO CARTÃO \n'
      '[4] PAGAMENTO DIVIDIDO EM 3X OU MAIS NO CARTÃO - 20% DE JUROS \n  '))
print('='* 50)
print('CALCULANDO O VALOR DO PRODUTO...')
print('='* 50)
if opc == 1:
    print(f' VALOR A SER PAGO: R${valor - dinheiro:.2f}')
    print('=' * 50)
elif opc == 2:
    print(f'VALOR A SER PAGO: R${valor - cartao:.2f}')
    print('=' * 50)
elif opc == 3:
    print(f'VALOR A SER PAGO: 2X DE R${valor / 2:.2f}')
    print('=' * 50)
elif opc == 4:
    x = int(input('em quantas vezes: '))
    porcentagem = (valor * 20) / 100
    print(f'Valor A SER PAGO COM JUROS: {x}x DE R${valor / x + porcentagem  :.2f }')
