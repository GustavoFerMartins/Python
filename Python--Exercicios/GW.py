import itertools

plvra = input('String a ser permutada: ')

resultado = itertools.permutations(plvra, len(plvra))

for i in resultado:
    print(''.join(i))
