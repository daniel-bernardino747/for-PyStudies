"""lista = list()
for r in range(0, 5):
    num = int(input('Digite um valor: '))
    if r == 0 or num >= lista[len(lista) - 1]:
        lista.append(num)
        print('Valor adicionado como último da lista.')
    else:
        if num <= lista[0]:
            lista.insert(0, num)
            print('Valor adicionado como primeiro da lista.')
        elif lista[0] <= num <= lista[1]:
            lista.insert(1, num)
            print('Valor adicionado como segundo da lista.')
        elif lista[1] <= num <= lista[2]:
            lista.insert(2, num)
            print('Valor adicionado como terceiro da lista.')
        elif lista[2] <= num <= lista[3]:
            lista.insert(3, num)
            print('Valor adicionado como quarto da lista.')
print(lista)"""
lista = list()
for r in range(0, 5):
    num = int(input('\033[97mDigite um valor: '))
    if r == 0 or num >= lista[len(lista) - 1]:
        lista.append(num)
        print('Valor adicionado como último da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Número adicionado na posição {pos}.')
                break
            pos += 1
print(lista)
