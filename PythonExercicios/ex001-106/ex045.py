import random

print('=' * 154)
print('''{}{}
{}== JOKENPÔ ==
{}{}{}\n'''.format('\033[95m', '=' * 13, '\033[1:95m', '\033[0:95m', '=' * 13, '\033[97m'))
c0 = '\033[0:97m'
c1 = '\033[1:94m'
print(f'''Escolha sua jogada:
{c1}[ 1 ]{c0} PEDRA
{c1}[ 2 ]{c0} PAPEL
{c1}[ 3 ]{c0} TESOURA''')
escolha = int(input('Qual sua escolha: '))
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(opcao)

if escolha == 1:
    if computador == opcao[0]:
        print('''\n=-=-=-=-=-=-=-=-=-=
Você         jogou PEDRA
Computador   jogou PEDRA
=-=-=-=-=-=-=-=-=-=''')
        print('EMPATE')
    elif computador == opcao[1]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou PEDRA
Computador   jogou PAPEL
=-=-=-=-=-=-=-=-=-=''')
        print('COMPUTADOR GANHOU')
    elif computador == opcao[2]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou PEDRA
Computador   jogou TESOURA
=-=-=-=-=-=-=-=-=-=''')
        print('VOCÊ VENCEU')

if escolha == 2:
    if computador == opcao[0]:
        print('''\n=-=-=-=-=-=-=-=-=-=
Você         jogou PAPEL
Computador   jogou PEDRA
=-=-=-=-=-=-=-=-=-=''')
        print('VOCÊ VENCEU')
    elif computador == opcao[1]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou PAPEL
Computador   jogou PAPEL
=-=-=-=-=-=-=-=-=-=''')
        print('EMPATE')
    elif computador == opcao[2]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou PAPEL
Computador   jogou TESOURA
=-=-=-=-=-=-=-=-=-=''')
        print('COMPUTADOR GANHOU')

if escolha == 3:
    if computador == opcao[0]:
        print('''\n=-=-=-=-=-=-=-=-=-=
Você         jogou TESOURA
Computador   jogou PEDRA
=-=-=-=-=-=-=-=-=-=''')
        print('COMPUTADOR GANHOU')
    elif computador == opcao[1]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou TESOURA
Computador   jogou PAPEL
=-=-=-=-=-=-=-=-=-=''')
        print('VOCÊ VENCE')
    elif computador == opcao[2]:
        print('''=-=-=-=-=-=-=-=-=-=
Você         jogou TESOURA
Computador   jogou TESOURA
=-=-=-=-=-=-=-=-=-=''')
        print('EMPATE')
