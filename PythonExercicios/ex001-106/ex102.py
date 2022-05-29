def fatorial(num, show=False):
    f = 1
    for a in range(num, 0, -1):
        f *= a
        if show:
            if a == 1:
                print(a, end=' = ')
            else:
                print(a, end=' x ')
    return f


print(fatorial(int(input('\033[97mDigite o número para fatoriar: ')), show=True))
