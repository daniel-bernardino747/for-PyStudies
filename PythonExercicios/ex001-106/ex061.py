print('\033[97m')
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a = 10
t = 10
u = 0
while a != 0:
    PA = pt + (t - a) * r
    print(PA, end=' -> ')
    a -= 1
print('ACABOU')
