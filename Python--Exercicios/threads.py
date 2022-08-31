from threading import Thread

def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        print(f'Carro1: Km: {trajeto}\n')

def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        print(f'Carro2: Km: {trajeto}\n')

t_carro1 = Thread(target=carro1, args=[1])
t_carro2 = Thread(target=carro2, args=[1.5])

t_carro1.start()
t_carro2.start()