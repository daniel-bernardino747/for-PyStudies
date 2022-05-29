"""from random import randint
# from time import sleep
n1 = int(randint(0, 5))
print('{}'.format('-=-' * 18))
print("Oi, te desafio a saber que número eu estou pensando.")
print('Hmmmm... Pronto, pensei em um número entre 0 e 5.')
print('-=-' * 18)
n = int(input('Qual você acha que é? '))
print('Processando...')
# sleep(3)
if n == n1:
    print('COMO VOCÊ SABIA QUE ERA {}???'.format(n1))
    print('Uau, você acertou, eu não consegui dessa vez. Parabéns!')
else:
    print('HAHAH você errou, eu pensei no número {}.'.format(n1))
    print('Jà que você errou, morre!')"""
from random import randint
print('=' * 154)
print('\033[97m{:^154}'.format(':' * 21))
print('\033[1:97m{:^154}\033[0:97m'.format(':: ADIVINHE O NÚMERO ::'))
print('{:^154}\033[m'.format(':' * 21))
num = int(randint(0, 5))
print('\n\033[93m{:^154}'.format('Estou pensando em um número de 0 a 5'))
print('\033[1:93m{:^154}\033[0:93m'.format('Quual você acha que é?'))
tent = int(input('\033[97m{:>76}'.format('-> ')))
print('\033[37m{:^154}\033[97m'.format('processando...'))
if num == tent:
    print('\n\033[1:92m{:^154}\033[97m'.format('Parabéns, você acertou. Nós pensamos no número {}.'.format(num)))
else:
    print('\n\033[91m{:^154}\033[97m'.format('Que pena, não foi dessa vez, eu pensei no número {}.'.format(num)))