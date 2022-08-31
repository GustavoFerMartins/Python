from datetime import datetime
niver = datetime.strptime(input('Digite a data do seu ANIVERSÁRIO (dd/mm/aaaa): '), '%d/%m/%Y')
hoje = datetime.now()
prazo = niver - hoje

if prazo.days < 0:
    print('Você já fez aniversário!')
else: 
    print('Faltam {} dias para o seu aniversário'.format(prazo.days))