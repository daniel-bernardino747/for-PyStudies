print('''\033[97m{}
{:^30}
{}'''.format('=' * 30, 'BANCO DANIELSON', '=' * 30))
saque = int(input('Qual o valor do saque? '))
cinquenta = saque // 50
resto = saque - (50 * cinquenta)
vinte = resto // 20
resto = resto - (20 * vinte)
dez = resto // 10
resto = resto - (10 * dez)
um = resto // 1
print(f'''Você receberá um total de:
* \033[95m{cinquenta}\033[97m cédulas de R$50,00
* \033[95m{vinte}\033[97m cédulas de R$20,00
* \033[95m{dez}\033[97m cédulas de R$10,00
* \033[95m{um}\033[97m cédulas de R$1,00''')
