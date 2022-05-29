n1 = int(input('Digite um número: '))
n2 = int(input('Agora mais um número: '))
value = (n1 + n2)
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
print(f'O valor da soma de {cores["amarelo"]}{n1} + {n2}{cores["limpa"]} é {cores["verde"]}{value}{cores["limpa"]}!')
