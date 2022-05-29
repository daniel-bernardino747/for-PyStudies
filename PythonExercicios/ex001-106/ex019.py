import random
print('{}'.format('=' * 154))
print('{}{:^154}{}'.format('\033[1:95m', 'SORTEADOR DE NOMES', '\033[97m'))
n1 = str(input('{:>78}'.format('Primeiro aluno: ')).strip().title())
n2 = str(input('{:>78}'.format('Segundo aluno: ')).strip().title())
n3 = str(input('{:>78}'.format('Terceiro aluno: ')).strip().title())
n4 = str(input('{:>78}'.format('Quarto aluno: ')).strip().title())
lista = [n1, n2, n3, n4]
sorteado = random.choices(lista)
print('{:^154}'.format('=' * 20))
print('{:^154}'.format('O sorteado é'))
print('{:>97}'.format('\033[1:93m{}\033[1:97m'.format(sorteado)))
print('{:^154}'.format('=' * 20))
