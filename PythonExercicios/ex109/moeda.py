def moeda(n=0, brl='R$'):
    res = f'{brl}{n:>.2f}'.replace('.', ',')
    return res


def metade(n=0, show=False):
    res = n / 2
    return res if show is False else moeda(res)


def dobro(n=0, show=False):
    res = n * 2
    return res if show is False else moeda(res)


def aumentar(n=0, porc=100, show=False):
    res = n + (n / 100 * porc)
    return res if show is False else moeda(res)


def diminuir(n=0, porc=100, show=False):
    res = n - (n / 100 * porc)
    return res if show is False else moeda(res)
