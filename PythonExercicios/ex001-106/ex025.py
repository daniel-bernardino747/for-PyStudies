print('=' * 154)
print('\033[30m{:^154}\033[93m'.format('-=-' * 8))
print('{:^154}'.format('SERÁ QUE SUA FAMÍLIA É DAS BOAS?'))
print('\033[30m{:^154}\033[97m'.format('-=-' * 8))
n = str(input('{:>77}'.format('Qual seu nome completo? ')))
res = 'madrigal' in n.lower().strip()
if res is False:
    print('\n\033[31m{:^154}'.format('Infelimente você não é um dos sortudos.'))
else:
    print('\n\033[92m{:^154}'.format('Finalmente, achei você, só a família Madrigal pode resolver esse problema.'))
