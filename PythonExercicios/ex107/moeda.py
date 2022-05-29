def metade(n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res


def aumentar(n, porc=100):
    res = n + (n / 100 * porc)
    return res


def diminuir(n, porc=100):
    res = n - (n / 100 * porc)
    return res
