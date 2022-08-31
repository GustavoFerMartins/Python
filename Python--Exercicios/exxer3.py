frase1 = "Desafio manipulação de strings"
frase2 = "jhonatan,rafael,carol,camilla"

palavras1 = frase1.split()
print(palavras1)

palavras2 = frase2.split()
print(palavras2)

palavras1 = frase1.split(' ')
print(','.join(palavras1))

palavras2 = frase2.split(',')
print(' & '.join(palavras2))