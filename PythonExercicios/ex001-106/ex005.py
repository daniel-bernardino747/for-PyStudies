n1 = int(input('\033[34mDigite um valor: \033[m'))
n2 = n1 - 1
n3 = n1 + 1
cores = {'red': '\033[31m',
         'baw': '\033[0:30:107m',
         'clean': '\033[m'}
print('\033[31m=-=\033[m' * 22)
print('{} O antecessor do número {} é o número {} e seu sucessor é o número {}!{}'.format(
    cores['baw'], n1, n2, n3, cores['clean']))
print('\033[31m=-=\033[m' * 22)
