print('\033[97m')
numero = count = soma = 0
while numero != 999:
    numero = int(input('Digite um valor [999 para parar]: '))
    if numero != 999:
        soma += numero
        count += 1
    else:
        pass
if count <= 1:
    print(f'Foi coletado apenas {count} número que é {soma}.')
else:
    print(f'Foram coletados {count} números e sua soma é {soma}.')
