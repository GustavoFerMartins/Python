print('||\|||||||||||||||||||||/||')
print('|||\Bem-vindo a tabuada/|||')
print('||||\|||||||||||||||||/||||')

#Função que faz a tabuada
def tabuada():
    num = int(input('Digite um número: '))
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)
        
#Função que faz uma nova tabuada caso voce queira      
def novamente():
    denovo = ('Você quer jogar novamente? (Sim/Nao)')
    print(denovo)
    resposta = input('Digite Sim ou Não: ').strip().upper()
    
    while(resposta != 'NÃO' and resposta != 'NAO'):
        
        if(resposta == 'SIM'):
            tabuada()
            print(denovo)
            resposta = input('Digite Sim ou Não: ').strip().upper()
            
        elif(resposta):
            print('Comando incorreto, digite novamente')
            print(denovo)
            resposta = input('Digite Sim ou Não: ').strip().upper()
    print('Você saiu!')
            
tabuada()
novamente()