matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('\033[97m')
for i in range(0, 3):
    for s in range(0, 3):
        matriz[i][s] = int(input(f'Digite um valor para [{i}, {s}]: '))
print('.' * 30)
for i in range(0, 3):
    for s in range(0, 3):
        print(f'[{matriz[i][s]:^7}]', end='')
    print()