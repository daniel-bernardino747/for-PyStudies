print('=' * 154)
print('\033[97m{:^154}'.format('-==-' * 6))
f = str(input('{:>50}{}'.format(' ', 'Escreva uma frase: ')).strip().lower())
print('{:>50}{}'.format(' ', 'Nessa frase existe uma quantidade de \033[92m{}\033[97m letras "A".'
                        .format(f.count('a'))))
pp = f.find('a')
lp = f.rfind('a')
print('{:>50}{}'.format(' ', 'O primeiro "A" aparece na posição \033[92m{}\033[97m e o último na posição'
                             ' \033[92m{}\033[97m.'.format(pp + 1, lp + 1)))
print('\033[97m{:^154}'.format('-==-' * 6))
