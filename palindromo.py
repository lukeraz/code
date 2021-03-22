frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]
print(junto, inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print('Essa frase não é palindroma')



