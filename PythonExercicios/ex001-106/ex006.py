n1 = int(input('\033[2:97mDigite um valor: \033[m'))
n2 = n1 * 2
n3 = n1 * 3
nr = n1 ** (1/2)
c = {'clean': '\033[m',
     'white': '\033[97m',
     'nyellow': '\033[1:33m'}
print('{}O dobro desse valor é {}{}{}{} \n{}O triplo dele é {}{}{}{} \n{}E a raiz quadrada dele é {}{}{:.3f}{}'.format(
    c['white'], c['clean'], c['nyellow'], n2, c['clean'], c['white'], c['clean'], c['nyellow'], n3, c['clean'],
    c['white'], c['clean'], c['nyellow'], nr, c['clean']))
