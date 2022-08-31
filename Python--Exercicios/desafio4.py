dado = input('Digite um dado para saber o tipo dele: ')
a = dado.isnumeric()
b = dado.isalpha()
c = dado.isupper()
d = dado.isalnum()
e = dado.istitle()
f = dado.islower()
g = dado.isspace()

print('True = VERDADEIRO\nFalse = FALSO')
print('----------------------------------------------')
print(f'É numerico? {a}\nÉ uma letra? {b}\nÉ Maiuscula? {c}\nÉ letra e numero? {d}\n'
      f'Esta capitalizada? {e}\nEsta em minuscula? {f}\nSó tem espaço? {g}')