print('Boas Vindas Digite uma nota de 0.0 a 10.0')
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
media = (a * 3.5 + b * 7.5) / 11

if a and b <= 10:
    print(f'media = { media :.5f}')
else:
    print('Comando errado Tente Novamente')




