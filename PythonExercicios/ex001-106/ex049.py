c = {'1': '\033[91m',
     '2': '\033[92m',
     '3': '\033[93m',
     '4': '\033[94m',
     '5': '\033[95m',
     '6': '\033[96m',
     '7': '\033[97m'}
print('\033[97m\n', '=' * 60)
print(' Digite um número inteiro e veja sua tabuada até o número 10.')
print('\033[97m', '=' * 60)
n = int(input('\n{}Digite um número: '.format(c['7'])))

'''tabuada = [n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10]
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(f'A Tabuada de {n} é:')
for a in tabuada:
    print('{} X {} = {}'.format(n, n + 1, a))'''

for a in range(1, 11):
    print('{} X {:2} = {:2}'.format(n, a, n * a))
