dias = int(input("Por quantos dias voce alugou o carro?: "))
km = float(input("Quantos km voce percorreu?: "))
soma = (dias * 60) + km * 0.15
print(f"O total a pagar é: R${soma}")