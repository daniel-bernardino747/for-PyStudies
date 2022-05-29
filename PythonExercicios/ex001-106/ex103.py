def ficha(name='<desconhecido>', gols=0):
    print(f'O jogador {name} fez {gols} gol(s) no campeonato.')


m = str(input('\033[97mNome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if m.strip() == '':
    ficha(gols=g)
else:
    ficha(m, g)
