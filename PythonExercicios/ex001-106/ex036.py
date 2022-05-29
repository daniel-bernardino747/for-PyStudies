print('=' * 154)
print('\033[91m{:^154}'.format(':' * 25))
print('\033[1:91m{:^154}\033[0:91m'.format(':: FINANCIAMENTO ::'))
print('{:^154}\033[97m\n'.format(':' * 25))
house = float(input('{:>78}'.format('Valor da casa: ')))
cash = float(input('{:>78}'.format('Salário fixo total da família: ')))
year = float(input('{:>78}'.format('Em quantos anos deseja pagar: ')))
prestacao = house / (year * 12)
pagavel = cash * 0.3
print('\n{:^170}\n'.format('[A prestação da casa ficará no valor de R$ {}{:.2f}{}, enquanto a pessoa física pode pagar '
                           'até R$ {}{:.2f}{} mensais]'.format('\033[93m', prestacao, '\033[97m', '\033[93m', pagavel,
                                                           '\033[97m')))
if prestacao < pagavel:
    print('\033[92m{:^154}'.format('FINANCIAMENTO ACEITO'))
elif prestacao == pagavel:
    print('\033[93m{:^154}'.format('FINANCIAMENTO COM RISCO'))
elif prestacao >= pagavel:
    print('\033[91m{:^154}'.format('FINANCIAMENTO NEGADO'))
