lista = list()
while True:
    lista.append(int(input('\033[97mDigite um valor: ')))
    lista.sort(reverse=True)
    sair = str(input('Digite \033[95m[S]\033[97m para continuar e \033[95m[N]\033[97m para sair: ')).upper().strip()[0]
    if sair in 'N':
        break
print(f'Foram digitados {len(lista)} números.\nFormando a lista: {lista}')
if 5 in lista:
    print('O número cinco aparece na lista.')
else:
    print('O número cinco \033[91mnão\033[97m aparece na lista.')
