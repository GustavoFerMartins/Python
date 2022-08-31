from random import randrange

print('Bem-Vindo AO JOGO')


def jogar():
    print('Chute um número entre 1 e 100')
    numsec = randrange(1, 101)
    chute = int(input('Chute o número: '))
    
    while(chute != numsec):
        if(chute < numsec):
            print('Você errou! Tente um número maior')
            chute = int(input('Chute um número maior: '))
            
        elif(chute > numsec):
            print('Você errou! Tente um número menor')
            chute = int(input('Chute um número menor: '))
            
    print('Você acertou!')
    
def jogar_novamente():
    novamente = 'Você quer jogar novamente? (Sim/Nao)'
    print(novamente)
    resposta_do_usuario = input('Digite Sim ou Não: ').strip().upper()
    
    while(resposta_do_usuario != 'NÃO' and resposta_do_usuario != 'NAO'):
        jogar()
        print(novamente)
        resposta_do_usuario = input('Digite Sim ou Não: ').strip().upper()
        
    print('Obrigado por jogar!')
    
jogar()
jogar_novamente()