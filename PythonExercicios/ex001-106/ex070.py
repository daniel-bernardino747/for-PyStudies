print('''\033[97m{}
{:^30}
{}'''.format('=' * 30, 'LOJA BOM PREÇO', '=' * 30))
mais_barato = mais_caro = total = count = maisqmil = 0
nome_caro = nome_barato = ''
while True:
    print('.' * 30)
    nome = str(input('Nome do produto: ')).upper().strip()
    valor = float(input('Preço do produto: '))
    print('-' * 10)
    count += 1
    total += valor
    if valor > 1000:
        maisqmil += 1
    if count == 1:
        mais_barato = valor
        mais_caro = valor
        nome_caro = nome
        nome_barato = nome
    elif count != 1:
        if valor > mais_caro:
            mais_caro = valor
            nome_caro = nome
        elif valor < mais_barato:
            mais_barato = valor
            nome_barato = nome
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
* Total da Compra: {total}
* Produto mais barato: {nome_barato}; valendo R${mais_barato}
* Total de produtos mais caros que mil reais: {maisqmil}
* Produto mais caro: {nome_caro}; valendo R${mais_caro}.''')
print('=' * 30)
