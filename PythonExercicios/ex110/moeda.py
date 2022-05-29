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


def resumo(n=0, aum=0, dim=0):
    dic = {'Preço analisado:': moeda(n), 'Dobro do preço:': dobro(n, True), 'Metade do preço:': metade(n, True),
           f'{aum}% de aumento:': aumentar(n, aum, True), f'{dim}% de redução:': diminuir(n, dim, True)}
    print(f'{"=" * 29}\n{"RESUMO DO VALOR":^30}\n{"=" * 29}')
    for i, v in dic.items():
        print(f'{i:18}{v:>11}')
    print(f'{"=" * 29}')