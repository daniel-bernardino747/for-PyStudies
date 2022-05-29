numeros_guardados = (int(input('\033[97mDigite um valor: ')),
                     int(input('\033[97mDigite outro valor: ')),
                     int(input('\033[97mDigite mais um valor: ')),
                     int(input('\033[97mDigite o último valor: ')))
n = numeros_guardados
s = 0
print(f'Você digitou os números: {n}')
if numeros_guardados.count(9) == 0:
    print('O número 9 não aparece nenhuma vez.')
elif numeros_guardados.count(9) == 1:
    print('O número 9 aparece uma vez.')
else:
    print(f'O número 9 aparece {numeros_guardados.count(9)} vezes.')
if 3 in numeros_guardados:
    print(f'O valor 3 aparece na {numeros_guardados.index(3) + 1}ª posição.')
else:
    print('O valor 3 não aparece nenhuma vez.')
for r in range(0, len(numeros_guardados)):
    if numeros_guardados[r] != 0:
        if numeros_guardados[r] % 2 == 0:
            s += 1
        else:
            pass
    else:
        pass
print(f'Existem {s} números pares.')
