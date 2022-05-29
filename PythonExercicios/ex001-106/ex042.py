print('=' * 152)
print('''{:>5}{}
{:>5}== FORMANDO E ANALISANDO TRIÂNGULOS ==
{:>5}{}{}\n'''.format('\033[96m', '=' * 38, '\033[96m', '\033[96m', '=' * 38, '\033[97m'))
r1 = float(input('Digite o valor da reta número 01: '))
r2 = float(input('Digite o valor da reta número 02: '))
r3 = float(input('Digite o valor da reta número 03: '))
list = [r1, r2, r3]
ordem = sorted(list)
maior = max(list)
if maior < ordem[0] + ordem[1] and r1 == r2 == r3:
    print('\n\033[32m{}'.format('É possível criar um triângulo com esses valores.'))
    print('\033[97mEsse triângulo é {}Equilátero'.format('\033[96m'))

elif maior < ordem[0] + ordem[1] and r1 == r2 or r1 == r3 or r2 == r3:
    print('\n\033[32m{}'.format('É possível criar um triângulo com esses valores.'))
    print('\033[97mEsse triângulo é {}Isóceles'.format('\033[96m'))

elif maior < ordem[0] + ordem[1] and r1 != r2 != r3:
    print('\n\033[32m{}'.format('É possível criar um triângulo com esses valores.'))
    print('\033[97mEsse triângulo é {}Equilátero'.format('\033[96m'))

else:
    print('\n\033[91m{}'.format('Não possível criar um triãngulo com esses valores.'))
