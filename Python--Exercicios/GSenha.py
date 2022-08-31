import random
import string

tamanho = 16
gerar = input('OLÁ SEJA BEM-VINDO(A) \nSim | PARA GERAR SENHA |\nNão | NÃO PARA SAIR: ').upper()

while gerar != 'NÃO':
    if gerar == 'SIM':
        chars = string.ascii_letters + string.digits + '!@#$%&*()-=+'

        rnd = random.SystemRandom()

        print(''.join(rnd.choice(chars)for i in range(tamanho)))

        gerar = input('QUAL É A SUA OPÇÃO\nSim | PARA GERAR SENHA |\nNão | NÃO PARA SAIR: ').upper()

    elif gerar:
        print('COMANDO INCORRETO DIGITE NOVAMENTE\nSim | PARA GERAR SENHA |\nNão | NÃO PARA SAIR |')
        gerar = input('QUAL É A SUA OPÇÃO: ').upper()

print('Voce saiu!')



