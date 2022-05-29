mensagem = 'Olá, Brasil!!!'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'baw': '\033[7:97m'}
print('{}{}{}'.format(cores['verde'], '-=-' * 10, cores['limpa']))
print('{}{}{}'.format(cores['amarelo'], '-=-' * 10, cores['limpa']))
print('{}{}{}'.format(cores['azul'], '-=-' * 10, cores['limpa']))
print('{}{:^30}{}'.format(cores['baw'], mensagem, cores['limpa']))
print('{}{}{}'.format(cores['azul'], '-=-' * 10, cores['limpa']))
print('{}{}{}'.format(cores['amarelo'], '-=-' * 10, cores['limpa']))
print('{}{}{}'.format(cores['verde'], '-=-' * 10, cores['limpa']))
