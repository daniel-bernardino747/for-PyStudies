from datetime import date
print('=' * 154)
print('''{}{:^154}
{}{:^154}
{}{:^154}'''.format('\033[94m', ':' * 25, '\033[1:94m', ':: ANALISANDO NASCIMENTO ::', '\033[0:94m', ':' * 25))
print('''\n{:>45}\033[97mVamos analisar a data de nascimento de um homem e
{:>45}determinar o ano de alistamento.'''.format('', ''))
n1 = int(input('\n{:>45}Ano de nascimento: '.format('')))
idade = date.today().year - n1
if idade == 18:
    print('''\n{:>45}\033[97mDe acordo com nosso cálculo, essa pessoa tem {}{}{} anos.
    {:>41}{}Por isso, ele deverá se alistar esse ano!{} '''.format('', '\033[91m', idade, '\033[97m', '', '\033[94m',
                                                                   '\033[97m'))
elif idade == 17:
    print('''\n{:>45}\033[97mDe acordo com nosso cálculo, essa pessoa tem {}{}{} anos.
    {:>41}{}Por isso, ele deverá se alistar ano que vêm!{} '''.format('', '\033[91m', idade, '\033[97m', '', '\033[94m',
                                                                   '\033[97m'))
elif idade > 18:
    print('''\n{:>45}\033[97mDe acordo com nosso cálculo, essa pessoa tem {}{}{} anos.
    {:>41}{}Por isso, seu ano de alistamento já passou!{} '''.format('', '\033[91m', idade, '\033[97m', '', '\033[94m',
                                                                   '\033[97m'))
else:
    print('''\n{:>45}\033[97mDe acordo com nosso cálculo, essa pessoa tem {}{}{} anos.
    {:>41}{}Por isso, ele não pode se alistar ainda!{} '''.format('', '\033[91m', idade, '\033[97m', '', '\033[94m',
                                                                   '\033[97m'))
