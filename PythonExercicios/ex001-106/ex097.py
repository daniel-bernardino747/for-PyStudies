def escreva(msg):
    a = len(msg) + 4
    print('=' * a)
    print(f'  {msg}')
    print('=' * a)


escreva(str(input('\033[97mDigite o título: ')))
