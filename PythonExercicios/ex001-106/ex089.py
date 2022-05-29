print('\033[97m')
dados = list()
alumni = list()
media = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 01: '))
    n2 = float(input('Nota 02: '))
    alumni.append(nome)
    media.append(n1)
    media.append(n2)
    alumni.append(media[:])
    media.clear()
    dados.append(alumni[:])
    alumni.clear()
    while True:
        sair = str(input('Quer continuar? [S/N] '))
        if sair in 'Ss':
            print('.' * 25)
            break
        elif sair in 'Nn':
            break
    if sair in 'Nn':
        break
dados.sort()
print('''{}
\033[94mNo. {:15} {:>4}\033[97m
{}'''.format('.' * 25, 'NOME', 'MÉDIA', '-' * 30))
for i, v in enumerate(dados):
    boletim = (dados[i][1][0] + dados[i][1][1]) / 2
    print(f'{i:2}  {v[0]:15}{boletim:>4}')
print('-' * 30)
while True:
    notas = int(input('Quer mostrar as notas de qual aluno? [999 interrompe] '))
    if notas == 999:
        break
    elif notas > len(dados) - 1:
        print('Não entendi, tente novamente: ', end='')
    else:
        print(f'Aluno(a): \033[94m{dados[notas][0]:10}\033[97m \nNota 01: {dados[notas][1][0]}'
              f'\nNota 02: {dados[notas][1][1]}\n')
