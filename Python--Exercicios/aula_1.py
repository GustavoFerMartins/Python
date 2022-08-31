#Começando Python: Orientação a Objetos

#Dados da conta
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

conta = cria_conta(1253, "Nico", 55.0, 1000.0) 
print(conta)


'''Nós conseguimos agrupar os dados e encapsular a criação dentro de uma função. 
Porém, ficou trabalhoso saber o nome das chaves'''

#Dados e comportamentos

#Depositando dinheiro na conta
def deposita(conta, valor):
    conta['saldo'] += valor

#Sacando dinheiro de uma conta
def saca(conta, valor):
    conta['saldo'] -= valor

#Mostrando o saldo da conta
def extrato(conta):
    print('Saldo: {}'.format(conta['saldo']))

#Chamando as funções e passando os parametros/dados
deposita(conta, 105.0)
extrato(conta)
saca(conta, 40.0)
extrato(conta)