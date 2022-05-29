def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[91m(O usuário preferiu não digitar.)')
            return 0
        except (TypeError, ValueError):
            print(f'\033[91mERRO: Por favor, digite um número inteiro válido.\033[97m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            min = float(input(msg))
        except KeyboardInterrupt:
            print('\033[91m(O usuário preferiu não digitar.)')
            return 0
        except (TypeError, ValueError):
            print(f'\033[91mERRO: Por favor, digite um número inteiro válido.\033[97m')
            continue
        else:
            return min


n = leiaint('\033[97mDigite um número inteiro: ')
min = leiafloat('Digite um número real: ')
print(f"Você acabou de digitar os números {n} e {min}.")
