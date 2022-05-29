print('=' * 154)
print('\033[94m{:^154}'.format(':' * 31))
print('\033[1:95m{:^154}'.format('::::   SISTEMA DE UNIDADES   ::::'))
print('\033[0:94m{:^154}\033[m'.format(':' * 31))
print('{:^154}'.format('Digite um número entre 0 e 9999'))
num = int(input('\033[97m{:>78}'.format('Número  ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if u == 1:
    print('{:>75} | {}'.format('Unidade', u))
else:
    print('{:>75} | {}'.format('Unidades', u))
if d == 1:
    print('{:>75} | {}'.format('Dezena', d))
else:
    print('{:>75} | {}'.format('Dezenas', d))
if c == 1:
    print('{:>75} | {}'.format('Centena', c))
else:
    print('{:>75} | {}'.format('Centenas', c))
if m == 1:
    print('{:>75} | {}'.format('Milhar', m))
else:
    print('{:>75} | {}'.format('Milhares', m))
print('\033[m{:^154}'.format('==='))

