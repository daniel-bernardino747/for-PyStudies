print('\033[97m\n', '=' * 60)
print(' Digite o primeiro termo da \033[95mProgressão Aritmética\033[97m depois a razão dela.')
print('\033[97m', '=' * 60)
pt = int(input('\nDigite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
PA = pt + (10 - 1) * r
for a in range(pt, PA + r, r):
    print(a, end=' -> ')
print('ACABOU')
