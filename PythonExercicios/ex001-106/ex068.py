from random import randint
print('\033[95m')
print('=' * 30)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=' * 30)
print('\033[97m')
num_comp = randint(0, 20)
count1 = count2 = 0
while True:
    n = int(input('Digite seu número: '))
    if n == 0:
        break
    soma = n + num_comp
    mao = str(input('Você escolhe par ou ímpar? [P/I] ')).upper().strip()[0]
    count1 += 1
    if mao == 'P':
        if soma % 2 == 0:
            count2 += 1
            print(f'Você venceu. A soma dos números escolhidos é {soma}, um número par.\nVamos mais uma vez!')
        else:
            print(f'Você perdeu. Das {count1} jogadas, você ganhou {count2}. Parabéns.')
            break
    elif mao == 'I':
        if soma % 2 != 0:
            count2 += 1
            print(f'Você venceu. A soma dos números escolhidos é {soma}, um número ímpar.\nVamos mais uma vez!')
        else:
            print(f'Você perdeu. Das {count1} jogadas, você ganhou {count2}. Parabéns.')
            break
    else:
        print('Eu não entendi. Pode repetir?')
print('\nObrigado por brincar comigo! Nos vemos em uma próxima vez.')

