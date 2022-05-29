tabela_brasileirao = ('Corinthians', 'Santos', 'América-MG', 'Bragantino', 'São Paulo', 'Atlético-MG', 'Botafogo',
                      'Internacional', 'Coritiba', 'Avaí', 'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo',
                      'Fluminense', 'Goiás', 'Ceará', 'Juventude', 'Atlético-GO', 'Fortaleza')
print('\033[97m{:_^50}'.format('TIMES DO BRASILEIRÃO'))
print(tabela_brasileirao)
print('_' * 50)

print('\033[94m{:.^40}\033[97m'.format('TOP 5 BRASILEIRÃO'))
print(tabela_brasileirao[:5])
print('\n\033[94m{:.^40}\033[97m'.format('4 PIORES DO BRASILEIRÃO'))
print(tabela_brasileirao[-4:])
print('\n\033[94m{:.^40}\033[97m'.format('BRASILEIRÃO EM ORDEM ALFABÉTICA'))
print(sorted(tabela_brasileirao))
print('\n\033[94m{:.^40}\033[97m'.format('POSIÇÃO DO JUVENTUDE'))
print(f'O Time Juventude está na {tabela_brasileirao.index("Juventude") + 1}ª posição.')
