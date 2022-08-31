from random import randrange

print("-------------------------------")
print('Bem-Vindo ao jogo de advinhação')
print('-------------------------------')

#Voce quer Jogar?
def jogar():
    jogo = randrange(1, 51)
    chute = int(input("Chute um número entre 0 e 50: "))
    while(chute != jogo):
        if(chute > jogo):
            print("Você errou! Tente um número menor")
            chute = int(input("Chute outro número entre 0 e 50: "))
        elif(chute < jogo):
            print("Você errou! Tente um número maior")
            chute = int(input("Chute outro número entre 0 e 50: "))    
    print("Você acertou!")

#Você acertou! Mas quer jogar novamente?  
def jogar_novamente():
    print("Você quer jogar novamente? (Sim/Nao)? ")
    resposta = input("Digite Sim ou Não: ").strip().upper()
    if(resposta == "SIM"):
        jogar()
    else:
        print("Até a próxima!")

jogar()
jogar_novamente()