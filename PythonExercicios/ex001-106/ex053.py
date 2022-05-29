n = str(input('\033[97mDigite algo: ')).upper().replace('', ' ').split()
junto = ''.join(n)
inverso = ''
for a in range(len(n) - 1, -1, -1):
    inverso += junto[a]
print(inverso)
if inverso == junto:
    print('Esse é um \033[93mpalíndromo\033[97m.')
else:
    print('Esse \033[91mnão\033[97m é um palíndromo.')
