matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('\033[97m')
for i in range(0, 3):
    for s in range(0, 3):
        matriz[i][s] = int(input(f'Digite um valor para [{i}, {s}]: '))
print('.' * 30)
spar = scol = maior = 0
for i in range(0, 3):
    for s in range(0, 3):
        if matriz[i][s] % 2 == 0:
            spar += matriz[i][s]
        else:
            pass
        if i == 1 and s == 0:
            maior = matriz[i][s]
        elif matriz[1][s] > maior:
            maior = matriz[1][s]
        print(f'[{matriz[i][s]:^7}]', end='')
    scol += matriz[i][2]
    print()
print(f'A soma dos números pares é: {spar}')
print(f'A soma dos valores da 3ª coluna é {scol}')
print(f'O maior valor da 2ª linha é {maior}')
