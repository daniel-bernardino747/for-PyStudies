from time import sleep


def contador(inic, fim, passo):
    print('=' * 30)
    if inic < fim:
        print(f'\033[97mContagem de \033[94m{inic}\033[97m até \033[94m{fim}\033[97m com '
              f'intervalo de \033[93m{passo}\033[97m.')
    elif inic > fim:
        print(f'\033[97mContagem regressiva de \033[94m{inic}\033[97m até \033[94m{fim}\033[97m com '
              f'intervalo de \033[93m{passo}\033[97m.')
    for i in range(inic, fim + 1, passo):
        print(i, end=' ', flush=True)
        sleep(0.4)
    print('\033[95mFim\033[97m\n')


contador(1, 10, 1)
contador(10, 0, -2)
contador(inic=int(input('Digite o valor de ínício: ')), fim=int(input('Valor de fim: ')),
         passo=int(input('Digite o intervalo: ')))
