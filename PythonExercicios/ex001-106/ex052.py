n = int(input('\033[97mDigite um número inteiro: '))
s = 0
for a in range(1, n + 1):
    if n % a == 0:
        print('\033[92m', end='')
    else:
        print('\033[91m', end='')
    print(a, end=' ')
    s += (n % a == 0)
if s == 2:
    print('\n\033[97mEsse número é \033[93mprimo\033[97m.')
else:
    print(f'\n\033[97mEsse número \033[91mNÃO\033[97m é primo, pois possui \033[93m{s}\033[97m divisores.')
