print('=' * 152)
print('''{}{}
{}== DESCUBRA SEU IMC ==
{}{}{}\n'''.format('\033[95m', '=' * 22, '\033[1:95m', '\033[0:95m', '=' * 22, '\033[97m'))
alt = float(input('Qual sua altura? '))
peso = float(input('E qual o seu peso? '))
imc = peso / alt ** 2
if imc < 18.5:
    print('Você está {}ABAIXO DO PESO{}.'.format('\033[93m', '\033[97m'))
elif 18.5 <= imc < 25:
    print('Você está no {}PESO NORMAL{}.'.format('\033[92m', '\033[97m'))
elif 25 <= imc < 30:
    print('Você está {}SOBREPESO{}.'.format('\033[93m', '\033[97m'))
elif 30 <= imc < 35:
    print('Você está em {}OBESIDADE I{}.'.format('\033[93m', '\033[97m'))
elif 34 < imc < 40:
    print('Você está em {}OBESIDADE II{}.'.format('\033[91m', '\033[97m'))
else:
    print('Você está em {}OBESIDADE III{}.'.format('\033[91m', '\033[97m'))
