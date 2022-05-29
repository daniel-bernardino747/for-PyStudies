print('{}{}{}'.format('\033[97m', '==' * 33, '\033[1:35m'))
print('PRECIFICAÇÃO DO ALUGUEL DE CARRO')
print('{}{}{}'.format('\033[0:97m', '==' * 33, '\033[97m'))
day = int(input('\nPor quantos \033[4:97mdias\033[0:97m você usou seu carro alugado? '))
km = float(input('Quantos \033[4:97mKm\033[0:97m você percorreu com ele? '))
pd = day * 60
pkm = km * 0.15
print('\n{}{}{}'.format('\033[97m', '==' * 33, '\033[1:35m'))
print('\033[1:35mPREÇO:\033[0:97m')
print('O valor a ser pago pelo seu uso de \033[4:33m{}\033[0:97m km por \033[4:33m{}\033[0:97m dias é '
      'R$ \033[4:32m{}\033[0:97m.'.format(km, day, (pd + pkm)))
print('{}{}{}'.format('\033[97m', '==' * 33, '\033[1:35m'))
