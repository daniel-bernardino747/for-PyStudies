
print('\033[1:30m=~=.\033[m' * 15)
print('\033[1:97m¬-=-\033[m' * 5, '\033[1:31mCONVERSOR DE MOEDA', '\033[1:97m¬-=-\033[m' * 5)
print('\033[1:30m=~=¨\033[m' * 15)
print('\033[97m')
while True:
    br = float(input('Valor a ser calculado em real: '))
    eua = br / 4.74
    n1 = 'DOLAR'
    n2 = 'REAIS'
    print('{:^42}'.format('==' * 16))
    print('\033[1:33m{:^20} | {:^20}\033[m'.format(n2, n1))
    print('\033[1:32m{:^20} | {:^20.1f}\033[m'.format(br, eua))
    print('\033[97m{:^42}'.format('==' * 16))
    b = input('\nOutro valor? ').lower().strip()
    if b in ['sim', 'ss', 's', 'si']:
        loop = True
    else:
        exit()

