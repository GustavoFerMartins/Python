from datetime import datetime
import random

nome = input('Qual é o seu nome?')
idade = int(input('Quanto anos voce tem?'))
cadastro = datetime.now()

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)


niver = datetime.strptime(input('Digite a data do seu ANIVERSÁRIO (dd/mm/aaaa): '), '%d/%m/%Y')

print(f'Olá {nome}, seu registro foi concluido com sucesso no dia {cadastro.day}/{cadastro.month}/{cadastro.year} Parabéns, houve um sorteio e voce ganhou um cartao de compras no valor de {cartao}')