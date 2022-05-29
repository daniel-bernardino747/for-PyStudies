time = list()
jogador = dict()
partidas = list()
print(f'\033[97m{"=" * 39}\n{" ANALISE JOGADOR ":^39}\n{"=" * 39}')
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).title()
    tot = int(input(f'Digite o nº de partidas que {jogador["Nome"]} jogou: '))
    partidas.clear()
    for i in range(0, tot):
        partidas.append(int(input(f'Gols na partida {i + 1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        sair = str(input('Continuar? [S/N} '))
        if sair in 'Ss':
            print('=' * 10)
            break
        elif sair in 'Nn':
            break
        else:
            print(f'{"=" * 10}\nEu não entendi, pode repetir?')
    if sair in 'Nn':
        break
print(f'\033[97m{"=" * 20}\n{"Nº":>3} {"Jogador":16}{"Gols":15} {"Total"}\n{"=" * 50}')
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for i in v.values():
        print(f'{str(i):15} ', end='')
    print()
print('=' * 50)
while True:
    levantamento = int(input('Ver levantamento de jogo de qual jogador? [999 pra parar] '))
    if levantamento == 999:
        break
    elif levantamento > len(time):
        print('>>> ERRO!  Esse jogador não existe.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {time[levantamento]["Nome"]}')
        for i, g in enumerate(time[levantamento]["Gols"]):
            print(f'>>> No jogo {i+1} fez {g} gols.')
        print()
print('<< Volte Sempre >>')
