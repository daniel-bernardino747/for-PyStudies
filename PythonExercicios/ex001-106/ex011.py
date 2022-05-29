c = {'0': '\033[m',
     '1': '\033[0:97m',
     '2': '\033[1:30m',
     '3': '\033[33m',
     '4': '\033[33m',
     '5': '\033[34m'}

print('{}{:^59}{}'.format(c['2'], '==' * 25, c['0']))
print('{}{} {}MEDIDOR DE TINTA{} {}{}'.format(c['2'], '==' * 10, c['4'], c['2'], '==' * 10, c['0']))
print('{}{:^59}{}'.format(c['2'], '==' * 25, c['0']))
print('\n{}Iremos calcular a quantidade de tinta que você usará para \npintar uma parede, definida por você, '
      'mais a sua mão de \nobra, calculada pelo área a ser pintada, aberturas e \ne cura da tinta.'
      '\n\n======= \033[33m(coloque as unidades em metros)\033[97m ======='.format(c['1']))

# Quantidade de tinta e preço dela
lrg = float(input('Primeiro, qual a largura da parede? '))
alt = float(input('E a altura dela? '))
pared = float(input('Quantas paredes são? '))
demao = float(input('Qual a quantidade de demão que serão feitas? '))
A = ((lrg * alt) * pared) * demao
print('Certo, então temos uma área de {}{:.2f}{} metros quadrados pra ser pintada.'.format(c['3'], A, c['1']))
tinta = A / 2
tintacomprada = int(A / 2) + 1

# Valor mão de obra (tempo de trabalho / aberturas / de-mão / cura tinta
mdo = float(input('\nQuanto custa sua mão de obra \033[m(Recomendação: R$9-20.00 por metro quadrado)\033[0:97m? '))
pmdo = mdo * A
cura = float(input('Qual o tempo de cura da tinta (se não souber coloque 4)? '))
job = pmdo + (((demao * 5) + cura) * 15)
print(' ')
print('{}{}{}'.format(c['2'], '==' * 19, c['1']))
print('O valor do seu serviço será de \033[33m{}\033[0:97m.'.format(job))
print('{}{}{}'.format(c['2'], '==' * 19, c['1']))
