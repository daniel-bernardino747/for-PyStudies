def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[91mDigite um número inteiro válido.\033[97m')
        if ok:
            break
    return valor


n = leiaint('\033[97mDigite algo: ')
print(f"Você acabou de digitar o número {n}.")
