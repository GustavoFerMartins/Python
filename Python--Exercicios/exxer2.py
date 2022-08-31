a = "é"
b = "MELHOR"
c = "QUE"
d = "feito"
e = "perfeito"

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')

biblioteca = "Biblioteca"
frase = "Desenvolvimento De Aplicações"
print(biblioteca.index("o"))
print(frase[16:29])
indice_d = frase.rindex("D")
indice_s = frase.rindex("s")
print(frase[indice_d:indice_s+1])