def linha(line='-', tam=30):
    print('\033[91m', end='')
    print(f'{line}' * tam, '\033[m')


def header(title, line='-', tam=0):
    n = 48 + tam
    linha(line, n)
    print(f'  >> \033[1:97m{title:^38}\033[m <<  ')
    linha(line, n)


def options(*msg):
    print('\033[97m', end='')
    for i, v in enumerate(msg):
        print(f'\033[93m{i + 1:>3}\033[m > \033[97m{v}\033[m')


def question(msg):
    print('\033[93m >>>\033[97m', end=' ')
    try:
        return int(input(msg))
    except (ValueError, TypeError):
        print('\033[mValor não encontrado. Tente uma das opções acima.\033[97m')
        return
