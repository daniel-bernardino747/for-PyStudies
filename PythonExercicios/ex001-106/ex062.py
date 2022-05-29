print('\033[97m')
primeiro = int(input('Digite o primeiro valor da PA: '))
r = int(input('Digite o valor da razão da PA: '))
termo = primeiro
count = 1
mais = 10
maiso = 0
while count <= mais:
    print(f'{termo} -> ', end=' ')
    termo += r
    count += 1
    if count == mais + 1:
        print('PAUSA')
        maiso = int(input('Quer saber mais quantos termos? '))
        mais += maiso
        if maiso == 0:
            print(f'Foram apresentados {mais} termos.')
        else:
            pass
    else:
        pass
