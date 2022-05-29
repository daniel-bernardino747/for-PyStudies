from random import randint

print('\033[97m')
jogar = str(input('Vamos brincar de adivinhar? [S/N] ')).upper().strip()[0]
aceito = 0
while jogar == 'S':
    n = randint(1, 10)
    tentativas = 1
    print('\nO Computador pensou em número entre 1 até 10.')
    escolha_jogador = int(input('Qual número você acha que o computador pensou? '))
    while escolha_jogador != n:
        if tentativas < 1:
            print('Não foi esse o número que ele pensou, tente outro.')
        elif tentativas < 3:
            print('Também não foi esse número, tente outro.')
        elif tentativas < 5:
            print('Tenta mais um pouco, acredito que tá quase.')
        elif 5 <= tentativas:
            print('Tente de novo.')
        escolha_jogador = int(input('Qual número? '))
        tentativas += 1
    if tentativas == 1:
        print(f'UAU! Você acertou de primeira. Vocês dois pensaram no número {n}. Estou vendo que você tem sorte.')
    elif 1 < tentativas <= 5:
        print(f'Caramba, você conseguiu vencer o computador e só precisou de {tentativas} para acertar o número {n}. '
              f'Parabéns.')
    elif 5 < tentativas <= 9:
        print(f'Poxa, vida. Dessa vez demorou {tentativas} tentativas para acertar. Tenho certeza que na próxima será '
              f'mais rápido.')
    elif tentativas == 10:
        print('Você realmente não tem sorte. Tentou todos os números e só no último foi acertar. Na próxima você vai '
              'ter mais sorte.')
    aceito += 1
    jogar = str(input('Vamos jogar de novo? [S/N] ')).upper().strip()
if aceito == 0:
    print('Que pena você não querer brincar comigo. Mas tudo bem, até uma próxima vez.')
else:
    print('Foi muito bom brincar com você. Nos vemos na próxima.')