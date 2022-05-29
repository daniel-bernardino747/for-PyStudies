dados = list()
pessoa = dict()
mulheres = list()
print(f'\033[97m{"=" * 39}\n{" BANCO DE DADOS ":^39}\n{"=" * 39}')
soma = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    dados.append(pessoa.copy())
    if pessoa['Sexo'] in 'F':
        mulheres.append(pessoa.copy())
    soma += pessoa['Idade']
    pessoa.clear()
    while True:
        sair = str(input('Continuar? [S/N} '))
        if sair in 'Ss':
            print('=' * 10)
            break
        elif sair in 'Nn':
            break
        else:
            print(f'{"=" * 10}\nEu não entendi, pode repetir?')
    if sair in 'Nn':
        break
media = soma / len(dados)
print(f'''{"=" * 30}
>>> O número de pessoas cadastradas foi: {len(dados)}
>>> A média do grupo é: {media}
>>> As mulheres são:''')
for i, v in enumerate(mulheres):
    print(f'   >> {v["Nome"]} com {v["Idade"]} anos.')
print(f'>>> Estão acima da média de idade: ')
for i, v in enumerate(dados):
    if v["Idade"] > media:
        print(f'   >> {v["Nome"]} com {v["Idade"]} anos.')
print(f'{"=" * 30}\n Dicionário: {dados}\n{"=" * 30}')
