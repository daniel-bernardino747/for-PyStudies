from datetime import date
print('=' * 152)
print('''{:>5}{}
{:>5}== DIVISÓRIA DE CAMPEONATO ==
{:>5}{}{}\n'''.format('\033[95m', '=' * 29, '\033[95m', '\033[95m', '=' * 29, '\033[97m'))
data = int(input('Data de nascimento: '))
idade = date.today().year - data
if idade <= 9:
    print('\nEssa pessoa está na classificação {}MIRIM{} já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
elif 9 < idade <= 14:
    print('\nEssa pessoa está na classificação {}INFANTIL{} já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
elif 14 < idade <= 19:
    print('\nEssa pessoa está na classificação {}JUNIOR{} já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
elif 19 < idade <= 20:
    print('\nEssa pessoa está na classificação {}SÊNIOR{} já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
elif 20 < idade <= 43:
    print('\nEssa pessoa está na classificação {}MASTER{} já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
else:
    print('\nEssa pessoa {}NÃO É RECOMENDADA{} para jogar, já que tem {} anos.'.format('\033[95m', '\033[97m', idade))
