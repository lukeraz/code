s = 0
cont = 0

for c in range (1, 501, 2):
   if c % 3 == 0:
        s+= c
        cont = cont +1
print(f'A soma de todos os {cont} valores encontrados é {s}')



