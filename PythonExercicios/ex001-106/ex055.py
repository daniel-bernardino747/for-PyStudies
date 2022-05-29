print('\033[97m')
maior = 0
menor = 0
for a in range(1, 5):
    peso = float(input(f'Digite o peso da {a}ª pessoa: '))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior} kg e o menor é {menor} kg.')