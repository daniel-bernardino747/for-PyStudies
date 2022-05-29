print('\033[30m==' * 12, '\033[97m')
p = float(input('Preço do produto: '))
d = float(input('Quantos porcento de desconto: '))
n1 = p * (d/100)
n2 = p - n1
print('\033[mO desconto é: {:.2f} reais.\033[1:97m'.format(n1))
print('O novo preço é: \033[34m{:.2f}\033[97m reais.'.format(n2))
print('\033[30m==' * 12, '\033[97m')
