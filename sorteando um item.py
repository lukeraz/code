import random
n1 = input("Digite um nome: ")
n2 = input("Digite um nome: ")
n3 = input("Digite um nome: ")
n4 = input("Digite um nome: ")
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f"O vencedor do sorteio foi: {escolhido}")
