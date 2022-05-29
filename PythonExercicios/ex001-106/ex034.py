# from time import sleep
print('=' * 154)
print('\033[94m{:^154}'.format(':' * 22))
print('\033[1:94m{:^154}\033[0:94m'.format(':: NOVO SALÁRIO ::'))
print('{:^154}\033[97m'.format(':' * 22))
s = float(input('\n{:>83}'.format('Seu salário atual é R$ ')))
if s <= 1250.00:
    rs = s * 1.15
    print('{:^161}'.format('Seu novo salário será R$\033[93m{:.2f}\033[97m'.format(rs)))
else:
    rs = s * 1.1
    print('{:^152}'.format('Seu novo salário será R$\033[93m{:.2f}\033[97m'.format(rs)))
# sleep(1.5)
print('\n\033[0:94m{:^154}'.format(':' * 22))
print('\033[1:94m{:^154}\033[0:94m'.format(':: VOCÊ MERECE ::'))
print('{:^154}\033[97m'.format(':' * 22))
