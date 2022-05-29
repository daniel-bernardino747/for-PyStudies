print('=' * 154)
print('\033[91m{:^154}'.format(':' * 24))
print('\033[1:91m{:^154}\033[0:91m'.format(':: PASSAGEM ::'))
print('{:^154}\033[97m'.format(':' * 24))
d = float(input('\n{:>93}'.format('Digite a distância percorrida em km: ')))
if d < 200:
    p = d * 0.5
    print('{:^154}'.format('O valor da passagem é de R${:>2f}'.format(p)))
else:
    f = d * 0.45
    print('{:^154}'.format('O valor da passagem é de R${:.2f}'.format(f)))
print('\n\033[91m{:^154}'.format(':' * 41))
print('{:^154}'.format('Não se esqueça de fazer uma boa viagem.'))
print('\033[91m{:^154}'.format(':' * 41))

