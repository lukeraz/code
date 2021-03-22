from math import pow, sqrt
b = float(input("Insira o comprimento do cateto oposto: "))
c = float(input("insira o comprimento do cateto adjacente: "))
a = pow(b, 2) + pow(c, 2)
r = sqrt(a)
print(f"O valor da hipotenusa é: {r}")