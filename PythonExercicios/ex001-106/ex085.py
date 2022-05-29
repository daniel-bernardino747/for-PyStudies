numeros = 0
princ = [[], []]
for s in range(1, 9):
    numeros = (int(input(f'Digite o {s}º valor: ')))
    if numeros % 2 == 0:
        princ[0].append(numeros)
    else:
        princ[1].append(numeros)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram: {princ[0]}\nOs valores ímpares foram: {princ[1]}')
