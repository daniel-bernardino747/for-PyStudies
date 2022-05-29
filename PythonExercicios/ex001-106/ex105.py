"""def notas(*num, sit=False):
    dic = dict()
    maior = menor = soma = 0
    dic['total'] = len(num)
    for i, v in enumerate(num):
        soma += v
        if i == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            elif v < menor:
                menor = v
    print()
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = soma / len(num)
    if sit:
        if dic['media'] < 6:
            dic['situação'] = 'Ruim'
        elif 6 <= dic['media'] <= 7:
            dic['situação'] = 'Razoável'
        elif dic['media'] > 7:
            dic['situação'] = 'Boa'
    return dic
"""


def notas(*num, sit=False):
    """
    Recolhe números em float, calculando a média, a maior nota, a menor e situação.
    :param num: notas
    :param sit: se True, mostra a situação; se False, não mostra
    :return: retorna um dicionário com 'Total', 'Maior', 'Menor', 'Media' e 'situação'.
    """
    dic = dict()
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Media'] = sum(num) / len(num)
    if sit:
        if dic['Media'] < 6:
            dic['situação'] = 'Ruim'
        elif 6 <= dic['Media'] <= 7:
            dic['situação'] = 'Razoável'
        elif dic['Media'] > 7:
            dic['situação'] = 'Boa'
    return dic


resp = notas(float(input('Primeira nota: ')), float(input('Segunda nota: ')), float(input('Terceira nota: ')), sit=True)
print(resp)
