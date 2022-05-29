"""from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do número {:.3f} é {}.'.format(num, trunc(num)))"""

print('{}'.format('==' * 77))
print('{}{}{}'.format('\033[1:34m\033[3:34m', 'ACHANDO A PARTE INTEIRA', '\033[0:37m'))
print('(Digite um valor quebrado. Exemplo: \033[4:37m455.344\033[0:37m)')
num = float(input('\033[1:97mDigite um número real: '))
print('\033[0:97mO valor digitado é \033[4:97m{}\033[0:97m e sua parte inteira é '
      '\033[1:97m\033[4:97m{}\033[0:97m.'.format(num, int(num)))
