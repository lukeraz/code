import random

n1 = input("Insira o nome para o sorteio da apresentação: ")
n2 = input("Insira o nome para o sorteio de apresentação: ")
n3 = input("Insira o nome para o sorteio de apresentação: ")
n4 = input("Insira o nome para o sorteio de apresentação: ")
lista =[n1, n2, n3, n4]
random.shuffle(lista)
print(f"A ordem de apresentação sera: {lista}")