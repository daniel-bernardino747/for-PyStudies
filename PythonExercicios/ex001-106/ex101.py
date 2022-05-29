def voto(ano):
    """
    Define se o ano digitado pentence ao grupo votante brasileiro.
    :param ano: ano de nascimento
    :return: resposta do voto com idade
    """
    from datetime import datetime

    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or 65 < idade:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


resp = voto(int(input('\033[97mDigite ano de nascimento: ')))
print(f'{resp}')
