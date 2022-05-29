"""import random
a = input('Digite algo: ')
b = input('Digite algo: ')
c = input('Digite algo: ')
lista = [a, b, c]
random.shuffle(lista)
resultado = '{:>91} {}'
print(resultado.format('Primeiro |', lista[0]))
print(resultado.format('Primeiro |', lista[1]))
print(resultado.format('Primeiro |', lista[2]))"""
"""print('{:>91} {}'.format('Primeiro |', '{}'.format(lista[0])))
print('{:>91} {}'.format('Segundo |', '{}'.format(lista[1])))
print('{:>91} {}'.format('Terceiro |', '{}'.format(lista[2])))"""
"""for a in range(0,10):
    if a == 2:
        print('\033[97m', end='')
    print(a, end=' ')"""
"""resultado = 1
count = 1
numero = int(input('Digite um número: '))
while count <= numero:
    resultado *= count
    count += 1
print(resultado, end=' ')"""
"""

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('\033[97m')
for i in range(0, 3):
    for s in range(0, 3):
        matriz[i][s] = int(input(f'Digite um valor para [{i}, {s}]: '))
print('.' * 30)
for i in range(0, 3):
    for s in range(0, 3):
        print(f'[{matriz[i][s]:^7}]', end='')
        matriz
    print()