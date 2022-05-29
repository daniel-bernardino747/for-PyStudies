from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
palpites = int(input('Quantas vezes quer que eu sorteie? '))
while tot <= palpites:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for c, l in enumerate(jogos):
    print(f'{c+1:2}º Jogo: {l}')
    sleep(1)
