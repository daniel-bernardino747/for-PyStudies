"""from time import sleep
print('Vamos descobrir se o ano é BISSEXTO')
print('-=-' * 12)
data = int(input('Digite um ano: '))
print('Processando...')
sleep(2)
bissexto = data % 4
if bissexto == 0:
    print('O ano {} é um ano BISSEXTO'.format(data))
else:
    print('O ano {} não é BISSEXTO'.format(data))"""
print('=' * 154)
print('\033[96m{:^154}'.format(':' * 24))
print('\033[1:96m{:^154}\033[0:96m'.format(':: ANO BISSEXTO ::'))
print('{:^154}\033[97m'.format(':' * 24))
data = float(input('\n{:>83}'.format('Digite um ano: ')))
print('\033[37m{:^154}\033[97m'.format('Processando...'))
bissexto = data % 4
if bissexto == 0:
    print('{:^164}'.format('O ano {} é um ano {}BISSEXTO{}'.format(data, '\033[92m', '\033[97m')))
else:
    print('{:^164}'.format('O ano {} {}não é BISSEXTO{}'.format(data, '\033[91m', '\033[97m')))