listanum = list()
maior = menor = 0
for r in range(0, 5):
    listanum.append(int(input(f'\033[97mDigite um valor para a posição {r}: ')))
    if r == 0:
        maior = menor = listanum[r]
    else:
        if listanum[r] > maior:
            maior = listanum[r]
        elif listanum[r] < menor:
            menor = listanum[r]
print(f'O maior número da lista é {maior} e está nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(i, end='..')
print(f'\nO menor número da lista é {menor} e está nas posições: ', end='')
for l, m in enumerate(listanum):
    if m == menor:
        print(l, end='..')
