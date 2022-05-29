print('\033[1:35m°*o*°\033[m' * 12)
print('\033[36m°*o*°' * 3,   '\033[1:36m VAMOS BRINCAR DE TABUADA   \033[m', '\033[36m°*o*°' * 3)
print('\033[1:35m°*o*°' * 3, ' ' * 28, '\033[1:35m°*o*°\033[m' * 3)
print('\033[0:97m')
# sleep(0.2)
while True:
    num = float(input('=== Quer saber a tabuada de que número? '))
    print('\033[1:97m')
    print('\033[1:36m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('1', num,
                                                                             (num * 1)), '\033[1:35m°*o*°' * 3)
    print('\033[1:35m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('2', num,
                                                                             (num * 2)), '\033[1:36m°*o*°' * 3)
    print('\033[1:36m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('3', num,
                                                                             (num * 3)), '\033[1:35m°*o*°' * 3)
    print('\033[1:35m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('4', num,
                                                                             (num * 4)), '\033[1:36m°*o*°' * 3)
    print('\033[1:36m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('5', num,
                                                                             (num * 5)), '\033[1:35m°*o*°' * 3)
    print('\033[1:35m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('6', num,
                                                                             (num * 6)), '\033[1:36m°*o*°' * 3)
    print('\033[1:36m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('7', num,
                                                                             (num * 7)), '\033[1:35m°*o*°' * 3)
    print('\033[1:35m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('8', num,
                                                                             (num * 8)), '\033[1:36m°*o*°' * 3)
    print('\033[1:36m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('9', num,
                                                                             (num * 9)), '\033[1:35m°*o*°' * 3)
    print('\033[1:35m°*o*°' * 3, ' \033[35m{:2}\033[1:97m x {} = {} '.format('10', num,
                                                                             (num * 10)), '\033[1:36m°*o*°' * 3)
    a = input('\n\033[0:97mVamos com outro número? ')
    if a in ['sim', 'ss', 's', 'si']:
        loop = True
    else:
        print('Obrigado por brincar comigo!')
        exit()
