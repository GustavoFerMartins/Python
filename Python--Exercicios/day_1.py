#Começando com Python - Day 1
#É bom começar com um programa simples

hello = "Hello World"
print(hello)

#Começando com jogo de advinhação
print("Bem-Vindo ao jogo de advinhação")

num_secreto = 27
chute = int(input("Chute um número entre 0 e 50:"))

print("Você chutou", chute)
#(if) = SE / Se o chute for igual ao número secreto então, imprima "Você acertou"
if(chute == num_secreto):
    print("Você acertou!")
#(else) = SENÃO / Se o chute não for igual ao número secreto então, imprima "Você errou "
else:
    print("Você errou!")

#Esse foi o primeiro dia começando com Python