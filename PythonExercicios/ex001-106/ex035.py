from time import sleep
sleep(1)
print('=' * 154)
print('\033[93m{:^154}'.format(':' * 23))
print('\033[1:93m{:^154}\033[0:93m'.format(':: FORMANDO TRIÂNGULOS ::'))
print('{:^154}\033[97m'.format(':' * 23))
r1 = float(input('\n{:>90}'.format('Comprimento da primeira reta: ')))
r2 = float(input('{:>90}'.format('Comprimento da segunda reta: ')))
r3 = float(input('{:>90}'.format('Comprimento da terceira reta: ')))
sleep(1)
list = [r1, r2, r3]
ordem = sorted(list)
maior = max(list)
if maior >= ordem[0] + ordem[1]:
    print('\n\033[93m{:^154}'.format(':' * 23))
    print('\033[31m{:^154}'.format('Não é possível criar um triângulo com esses valores.'))
    print('\033[93m{:^154}'.format(':' * 23))
else:
    print('\n\033[93m{:^154}'.format(':' * 23))
    print('\033[92m{:^154}'.format('È possível criar um triãngulo com esses valores.'))
    print('\033[93m{:^154}'.format(':' * 23))
