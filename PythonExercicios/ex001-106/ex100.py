from random import randint
from time import sleep


def sorteia():
    for i in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)


def somaPar():
    soma = maior = 0
    print('\033[97mOs números sorteados na lista são:')
    for v in numeros:
        print(f'{v}', end=' ', flush=True)
        if v % 2 == 0:
            soma += v
        sleep(0.4)
    print(f'\033[m\nRecolhendo os pares...\033[97m')
    sleep(1)
    print(f'\033[mSomando eles...\033[97m')
    sleep(2)
    print(f'A soma dos números pares é: {soma}')


numeros = list()
sorteia()
somaPar()
