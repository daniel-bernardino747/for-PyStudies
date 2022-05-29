print('\033[30m{:^39}'.format('==' * 14))
print('{:^10} \033[1:35mAUMENTO SALARIAL \033[0:30m{:^10}'.format('==' * 5, '==' * 5))
print('{:^39}\033[97m'.format('==' * 14))
s = float(input('\nSalário atual: '))
print('\033[m(Aumento de 15%)\033[1:97m')
au = 1.15
ns = s * au
print('O novo salário será de \033[35m{:.2f}\033[97m reais.'.format(ns))
