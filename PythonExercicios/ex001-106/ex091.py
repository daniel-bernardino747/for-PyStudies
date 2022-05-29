from time import sleep
from random import randint
from operator import itemgetter
ranking = list()
jogadores = {'Jogador_01': randint(1, 6), 'Jogador_02': randint(1, 6),
             'Jogador_03': randint(1, 6), 'Jogador_04': randint(1, 6)}
print(f'\033[97m{"=" * 39}\n{" LISTA DE JOGADORES ":^39}\n{"=" * 39}')
for i, v in jogadores.items():
    print(f'>>> O \033[95m{i}\033[97m escolheu o número \033[93m{v}\033[97m')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"=" * 39}\n{" RANKING JOGADORES ":^39}\n{"=" * 39}')
for i, v in enumerate(ranking):
    print(f'Em {i + 1}º lugar ficou \033[95m{v[0]}\033[97m com o número \033[93m{v[1]}\033[97m.')
    sleep(1)
print(f'{"=" * 30}\n Dicionário: {jogadores.items()}\n Lista: {ranking}\n{"=" * 30}')