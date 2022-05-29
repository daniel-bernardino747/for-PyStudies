"""jogador = dict()
print(f'\033[97m{"=" * 39}\n{" ANALISE JOGADOR ":^39}\n{"=" * 39}')
jogador['Nome'] = str(input('Nome do Jogador: ')).title()
jogador['Partidas'] = int(input('Nº de partidas jogadas: '))
jogador['totgols'] = 0
for i in range(0, jogador['Partidas']):
    jogador[f'gols{i+1}'] = int(input(f'Gols na {i+1} partida: '))
    jogador['totgols'] += jogador[f'gols{i+1}']
print(f'{"=" * 30}')
for i, v in jogador.items():
    print(f'>>> {i} = {v}')
print(f'{"=" * 30}\n Dicionário: {jogador.items()}\n{"=" * 30}')
"""
jogador = dict()
partidas = list()
print(f'\033[97m{"=" * 39}\n{" ANALISE JOGADOR ":^39}\n{"=" * 39}')
jogador['Nome'] = str(input('Nome do Jogador: ')).title()
tot = int(input(f'Digite o nº de partidas que {jogador["Nome"]} jogou: '))
for i in range(0, tot):
    partidas.append(int(input(f'Gols na partida {i+1}: ')))
jogador['Gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(f'{"=" * 30}')
for i, v in jogador.items():
    print(f'>>> {i} = {v}')
print(f'{"=" * 30}\n Dicionário: {jogador}\n Lista: {partidas}\n{"=" * 30}')