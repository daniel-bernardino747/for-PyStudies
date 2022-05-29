soma = count = 0
while True:
    valor = int(input('\033[97m>>> Digite um valor [999 para parar]: '))
    if valor == 999:
        break
    soma += valor
    count += 1
print(f'A soma dos {count} valores foi {soma}.')
