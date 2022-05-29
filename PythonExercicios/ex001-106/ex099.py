from time import sleep


def maior(* num):
    count = mair = 0
    sleep(0.4)
    print('\033[97mAnalisando os valores recebidos...\033[96m')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.4)
        if count == 0:
            mair = valor
        else:
            if valor > mair:
                mair = valor
        count += 1
    print(f'\n\033[97mO maior valor recebido foi: \033[95m{mair}\033[97m\n')


maior(6, 9, 6, 3, 1, 10, 3, 4)
maior(5, 3, 7, 2, 5, 8, 0)