print('''\033[97m{}
{:^30}
{}'''.format('=' * 30, 'CADASTRE UMA PESSOA', '=' * 30))

homens = mulheres = maior_idade = 0
while True:
    print('.' * 30)
    nome = str(input('Nome Completo: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        maior_idade += 1
    if sexo == 'F':
        if idade <= 20:
            mulheres += 1
        else:
            pass
    elif sexo == 'M':
        homens += 1
    else:
        while True:
            sexo = str(input('Não consegui entender. Responda com M (masculino) ou F (feminino): ')).upper().strip()[0]
            if sexo == 'F':
                if idade <= 20:
                    mulheres += 1
                    break
                else:
                    pass
            elif sexo == 'M':
                homens += 1
                break
    print('-' * 10)
    next = str(input('Deseja continuar cadastrando? [S/N] ')).upper().strip()[0]
    if next == 'N':
        break
    elif next == 'S':
        pass
    else:
        while True:
            next = str(input('Não consegui entender. Responda com Sim ou Não: ')).upper().strip()[0]
            if next == 'N':
                break
            if next == 'S':
                break
    if next == 'N':
        break

print('''\033[97m
{}'''.format('=' * 30))

print(f'''Em nosso sistema temos:
* Total de mulheres com menos de 20 anos: {mulheres}
* Total de homens: {homens}
* Total de pessoas com mais de 18 anos: {maior_idade}''')
print('=' * 30)
