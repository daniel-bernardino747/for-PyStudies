print('=' * 154)
print('\033[94m{:^154}'.format(':' * 24))
print('\033[1:94m{:^154}\033[0:94m'.format(':: LIMITE DE VELOCIDADE ::'))
print('{:^154}\033[97m'.format(':' * 24))
speed = int(input('\n{:>90}'.format('Qual a velocidade do carro em Km/h? ')))
if speed > 80:
    multa = float((speed - 80) * 7)
    print('\n\033[93m{:^154}'.format('Caramba, você excedeu o limite de velocidade.'))
    print('\033[93m{:^162}'.format('Sua multa é de R$\033[91m{:.2f}\033[93m!'.format(multa)))
else:
    print('\n\033[92m{:^154}'.format('Que bom que você estava dentro do limite de velocidade!'))
