from random import randint
maior = menor = 0
numeros_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'\033[97mOs números sorteados foram: {numeros_aleatorios}')
for r in range(0, 5):
    if r == 0:
        maior = menor = numeros_aleatorios[0]
    else:
        if numeros_aleatorios[r] > maior:
            maior = numeros_aleatorios[r]
        elif numeros_aleatorios[r] < menor:
            menor = numeros_aleatorios[r]

print(f'O maior número sorteado é {maior}.\nO menor número sorteado é {menor}.')
