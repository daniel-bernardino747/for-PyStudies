"""a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('È Alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())"""

print('\033[33m-=-\033[m' * 10)
a = input('Digite algo: ')
print('\033[33m-=-\033[m' * 10)
print('O tipo primitivo desse valor é', type(a))
if a.isspace() is True:
    print('Só tem espaços?' '\033[32m', a.isspace(), '\033[m')
else:
    print('Só tem espaços?' '\033[31m', a.isspace(), '\033[m')
if a.isnumeric() is True:
    print('Sò tem números?' '\033[32m', a.isnumeric(), '\033[m')
else:
    print('Só tem espaços?' '\033[31m', a.isnumeric(), '\033[m')
if a.isalpha() is True:
    print('Só tem letras?' '\033[32m', a.isalpha(), '\033[m')
else:
    print('Só tem letras?' '\033[31m', a.isalpha(), '\033[m')
if a.isalnum() is True:
    print('É alfanumérico?' '\033[32m', a.isalnum(), '\033[m')
else:
    print('É alfanumérico?' '\033[31m', a.isalnum(), '\033[m')
if a.isupper() is True:
    print('Está em maiúsculo?' '\033[32m', a.isupper(), '\033[m')
else:
    print('Está em maiúsculo?' '\033[31m', a.isupper(), '\033[m')
if a.islower() is True:
    print('Está em minúsculo?' '\033[32m', a.islower(), '\033[m')
else:
    print('Está em minúsculo?', '\033[31m', a.islower(), '\033[m')

if a.istitle() is True:
    print('Está capitalizado?' '\033[32m', a.istitle(), '\033[m')
else:
    print('Está capitalizado?' '\033[31m', a.istitle(), '\033[m')
print('\033[33m-=-\033[m' * 10)
