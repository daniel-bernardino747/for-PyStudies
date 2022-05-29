print('=' * 154)
print('\033[93m{:^154}'.format(':' * 24))
print('\033[1:93m{:^154}\033[0:93m'.format(':: ÍMPAR E PAR ::'))
print('{:^154}\033[97m'.format(':' * 24))
num = int(input('\n{:>85}'.format('Digite um número: ')))
u = (num // 1 % 10)
list1 = [2, 4, 6, 8, 0]
if u in list1:
    print('\n{:^163}'.format('Esse número é \033[94mpar\033[97m.'))
else:
    print('\n{:^163}'.format('Esse número é \033[92mímpar\033[97m.'))
