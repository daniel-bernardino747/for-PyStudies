t = list()
answer = 'S'
while answer != 'N':
    a = int(input('\033[97mDigite um valor: '))
    if a not in t:
        t.append(a)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não iremos adicionar esse valor.')
    answer = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
t.sort()
print(t)
