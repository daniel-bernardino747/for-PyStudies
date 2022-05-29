def title(msg):
    letras = len(msg) + 4
    print('\033[07m\033[1:97m\033[108m', end='')
    print(f'{"=" * letras:^150}')
    print(f'{msg:^150}')
    print(f'{"=" * letras:^150}')
    print('\033[m', end='')


def comando(msg):
    print('\033[07m\033[1:92m\033[108m', end='')
    help(msg)
    print('\033[m')


while True:
    ok = True
    title('SISTEMA PYTHON')
    com = str(input('\033[97m>>> Função: '))
    if com.upper() == 'FIM':
        break
    else:
        comando(com)
title('ATÉ LOGO!')
