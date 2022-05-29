print('=' * 154)
print('{:^229}\n'.format('{}(){}( ){}()'.format('\033[97m', '\033[96m', '\033[97m') * 5))
print('{:^154}'.format('Em que cidade você nasceu?'))
cid = str(input('{:>77}'.format(': ')).lower().strip())
ver = 'santo' in cid
if ver is True:
    print('\033[1:32m{:^154}\033[m'.format('(Encontramos Santo nessa cidade.)'))
else:
    print('\033[1:31m{:^154}\033[m'.format('(Não encontramos Santo nessa cidade.)'))
print('\n{:^229}'.format('{}(){}( ){}()'.format('\033[97m', '\033[96m', '\033[97m') * 5))
