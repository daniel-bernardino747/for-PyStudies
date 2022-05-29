from datetime import datetime

bncdd = dict()
bncdd['Nome'] = str(input('\033[97mDigite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
bncdd['Idade'] = datetime.now().year - nascimento
bncdd['CTPS'] = int(input('Número da Carteira de Trabalho (responda 0 se não tiver): '))
if bncdd['CTPS'] != 0:
    bncdd['Contratação'] = int(input('Ano de Contratação: '))
    bncdd['Salário'] = float(input('Salário: '))
    bncdd['Aposentadoria'] = bncdd['Idade'] + ((bncdd['Contratação'] + 35) - datetime.now().year)
print(f'{"=" * 30}')
for i, v in bncdd.items():
    print(f'>>> {i} = {v}')
print(f'{"=" * 30}\n Dicionário: {bncdd.items()}\n{"=" * 30}')
