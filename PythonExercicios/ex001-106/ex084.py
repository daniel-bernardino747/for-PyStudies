dados = list()
pessoa = list()
peso_maior = peso_menor = 0
while True:
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    dados.append(pessoa[:])
    pessoa.clear()
    if len(dados) == 1:
        peso_maior = peso_menor = dados[0][1]
    else:
        if dados[-1][1] >= peso_maior:
            peso_maior = dados[-1][1]
        elif dados[-1][1] <= peso_menor:
            peso_menor = dados[-1][1]
    sair = str(input('Adicionar mais? [S/N] '))
    if sair in 'Nn':
        break
print(dados[0][1])
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'O peso mais pesado é {peso_maior} kg.')
print(f'O peso mais leve é {peso_menor} kg.')
print('Os mais pesados são: ', end='')
for p in dados:
    if p[1] == peso_maior:
        print(f'{p[0]}', end=' ')
print('\nOs mais leves são: ', end='')
for p in dados:
    if p[1] == peso_menor:
        print(f'{p[0]}', end=' ')
