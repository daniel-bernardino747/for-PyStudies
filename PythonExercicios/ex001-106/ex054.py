from datetime import date

datatual = date.today().year
s = 0
c = 0
print('\033[97m')
for a in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {a}ª pessoa: '))
    if (datatual - n) < 18:
        s += 1
    else:
        c += 1
print(f'\nExistem \033[93m{s}\033[97m pessoas menores de idade e \033[93m{c}\033[97m maiores de idade.')
