print('=' * 154)
print('''{}{:^154}
{}{:^154}
{}{:^154}'''.format('\033[94m', ':' * 24, '\033[1:94m', ':: CALCULANDO MÉDIA ::', '\033[0:94m', ':' * 24))
print('''\n{:>45}\033[97mVamos analisar três notas de provas para calcular
{:>45}a média desse trimestre.'''.format('', ''))
n1 = float(input('\n{:>45}Primeira nota: '.format('')))
n2 = float(input('{:>45}Segunda nota: '.format('')))
n3 = float(input('{:>45}Terceira nota: '.format('')))
media = (n1 + n2 + n3) / 3
if media < 6:
    print('''\n{:>45}\033[97mEsse aluno tem média {}{:.1f}{}.
    {:>41}{}Infelizmente, esse aluno {}NÃO PASSOU{}!{} '''.format('', '\033[93m', media, '\033[97m', '', '\033[94m',
                                                                  '\033[91m', '\033[93m', '\033[97m'))
elif 6 <= media < 7:
    print('''\n{:>45}\033[97mEsse aluno tem média {}{:.1f}{}.
    {:>41}{}Por isso, ele precisa de {}RECUPERAÇÃO{}!{} '''.format('', '\033[93m', media, '\033[97m', '', '\033[94m',
                                                                   '\033[93m', '\033[97m', '\033[97m'))
elif media >= 7:
    print('''\n{:>45}\033[97mEsse aluno tem média {}{:.1f}{}.
    {:>41}{}Esse aluno {}PASSOU{}!{} '''.format('', '\033[93m', media, '\033[97m', '', '\033[94m',
                                                '\033[92m', '\033[93m', '\033[97m'))
