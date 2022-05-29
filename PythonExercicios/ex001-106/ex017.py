"""from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt((pow(co, 2)) + (pow(ca, 2)))
print('A hipotenusa desse triângulo vale {:.1f}.'.format(h))"""
from math import hypot
print('{}'.format('==' * 77))
print('\033[1:97m{}'.format('|' * 39))
print('{:^40}'.format('CALCULANDO A HIPOTENUSA'))
print('{}'.format('|' * 39))
co = float(input('\033[1:36mDigite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('O valor da hipontenusa é \033[97m{:.2f}'.format(h))
print('\033[1:97m{}'.format('|' * 39))
