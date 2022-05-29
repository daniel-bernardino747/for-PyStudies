def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, porc=100):
    res = n + (n / 100 * porc)
    return res


def diminuir(n=0, porc=100):
    res = n - (n / 100 * porc)
    return res


def moeda(n=0, brl='R$'):
    res = f'{brl}{n:>.2f}'.replace('.', ',')
    return res
