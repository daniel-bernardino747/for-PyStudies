print('{}{}{}'.format('\033[1:36m', 'o*0§0*o' * 5, '\033[m'))
print('{}{:^35}{}'.format('\033[1:31m', 'CONVERSOR DE TEMPERATURA', '\033[m'))
print('{}{}{}'.format('\033[1:36m', 'o*0§0*o' * 5, '\033[m'))
Celsius = float(input('\n\033[97mQual é a temperatura em °C? '))
Kelvin = Celsius + 273
Fahrenheit = ((Celsius * 9) / 5) + 32
print('Isso equivale à {}{} K{}.'.format('\033[33m', Kelvin, '\033[97m'))
print('E equivale à {}{} °F{}.'.format('\033[33m', Fahrenheit, '\033[97m'))
print('\n{}{}{}'.format('\033[1:36m', 'o*0§0*o' * 5, '\033[m'))
