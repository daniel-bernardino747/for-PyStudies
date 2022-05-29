print('\033[97m')
play = 'S'
while play == 'S':
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''Escolha uma das opção abaixo:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Qual é o maior?
    [ 4 ] Sair do programa.''')
    escolha = int(input('Digite sua opção: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} é {soma}.')
        play = str(input('Voltar ao menu principal? [S/N] ')).upper().strip()[0]
    if escolha == 2:
        multiplica = n1 * n2
        print(f'A multiplicação dos valores {n1} X {n2} é {multiplica}.')
        play = str(input('Voltar ao menu principal? [S/N] ')).upper().strip()[0]
    if escolha == 3:
        maior = n1
        menor = n2
        if n2 > n1:
            maior = n2
            menor = n1
        else:
            pass
        print(f'O maior dos dois valores é o número {maior} e o menor é o número {menor}.')
        play = str(input('Voltar ao menu principal? [S/N] ')).upper().strip()[0]
    if escolha == 4:
        break
