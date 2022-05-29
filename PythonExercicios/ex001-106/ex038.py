print('=' * 154)
print('''{}{:^154}
{}{:^154}
{}{:^154}'''.format('\033[93m', ':' * 26, '\033[1:93m', ':: COMPARANDO NÚMEROS ::', '\033[0:93m', ':' * 26))
print('''{:>45}\033[97mVamos comparar dois números e então diremos qual é maior,
{:>45}qual é menor e/ou se eles são iguais.'''.format('', ''))
n1 = float(input('\n\033[94m{:>48} - Digite o primeiro número: '.format('')))
n2 = float(input('\033[95m{:>48} - Digite o segundo número: '.format('')))
print('\n{:>45}\033[97m Calculando...'.format(''))
if n1 > n2:
    print('{:^168}'.format('\033[97mO \033[94mPRIMEIRO\033[97m número é o maior!'))
elif n2 > n1:
    print('{:^168}'.format('\033[97mO \033[95mSEGUNDO\033[97m número é o maior!'))
elif n1 == n2:
    print('{:^168}'.format('\033[97mOs \033[93mDOIS\033[97m números são iguais!'))
