print('\033[7:35m=========\033[m \033[3:35mVamos aprender sobre Conversão de Unidades\033[m \033[7:35m=========\033[m')
# sleep(0.4)
while True:
    ans = input('\n\033[97mPara começar, iremos trabalhar com metros, centímetros ou milímetros? ')
    c = ['milimetros', 'milímetros', 'milimetro', 'milímetro']
    # sleep(0.2)
    if ans in ['m', 'metros', 'metro']:
        print('\n\033[97mEntão trabalharemos com \033[4:97mmetros\033[0:97m!\n=======')
        m1 = float(input('Coloque um valor em metros: '))
        # sleep(0.1)
        print('\033[3:0mTransformando em centimetros e milímetros...\033[0:97m')
        # sleep(0.3)
        cm1 = m1 * 100
        mm1 = m1 * 1000
        print('\nEntão temos: \n- {} metros se tornam {} centímetros.'.format(m1, cm1))
        print('- {} metros se tornam {} milímetros.'.format(m1, mm1))
        print(' ')
        again = input('Vamos repetir? ').strip().lower()
        if again in ['sim', 's', 'ss', 'quero', 'bora']:
            loop = True
        else:
            print('Obrigado por jogar comigo')
            exit()

    elif ans in ['cm', 'centimetros', 'centímetros', 'centimetro', 'centímetro']:
        print('\n\033[97mEntão trabalharemos com \033[4:97mcentímetros\033[0:97m!\n=======')
        cm1 = float(input('Coloque um valor em centímetro(s): '))
        # sleep(0.1)
        print('\033[3:0mTransformando em metros e milímetros...\033[0:97m')
        # sleep(0.3)
        m1 = cm1 / 100
        mm1 = cm1 * 10
        print('\nEntão temos: \n- {} centímetros se tornam {} metros.'.format(cm1, m1))
        print('- {} centímetros se tornam {} milímetros.'.format(cm1, mm1))
        print(' ')
        again = input('Vamos repetir? ').strip().lower()
        if again in ['sim', 's', 'ss', 'quero', 'bora']:
            loop = True
        else:
            print('Obrigado por jogar comigo')
            exit()

    elif ans in ['mm', 'milimetros', 'milímetros', 'milimetro', 'milímetro']:
        print('\n\033[97mEntão trabalharemos com \033[4:97mmilímetros\033[0:97m!\n=======')
        mm1 = float(input('Coloque um valor em milímetro(s): '))
        # sleep(0.1)
        print('\033[3:0mTransformando em metros e milímetros...\033[0:97m')
        # sleep(0.3)
        m1 = mm1 / 1000
        cm1 = mm1 / 10
        print('\nEntão temos: \n- {} milímetros se tornam {} metros.'.format(mm1, m1))
        print('- {} milímetros se tornam {} centímetros.'.format(mm1, cm1))
        print(' ')
        again = input('Vamos repetir? ').strip().lower()
        if again in ['sim', 's', 'ss', 'quero', 'bora']:
            loop = True
        else:
            print('Obrigado por jogar comigo')
            exit()
