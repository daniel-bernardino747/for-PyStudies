s = 0
cont = 0
for a in range(1, 7):
    n = int(input(f'\033[97mDigite seu 0{a} número: '))
    if n % 2 != 0:
        cont += 1
        s += n
print(f'\nDentre esses números, encontramos {cont} números ÍMPARES, que somados resultam em {s}.')