print('=' * 154)
print('\033[92m{:^154}'.format(':' * 26))
print('\033[1:92m{:^154}\033[0:92m'.format('::: BASES DE CONVERSÃO :::'))
print('{:^154}\n\033[97m'.format(':' * 26))

print('{:64}{}'.format('', 'Iremos converter um número'))
print('{:64}{}'.format('', 'inteiro para binário, octal'))
print('{:64}{}'.format('', 'ou hexadecimal, vamos?'))

while True:
    print('\n{:64}{}'.format('', 'Escolha sua opção:'))
    print('{:64}{}'.format('', '\033[92m[1]\033[97m para binário.'))
    print('{:64}{}'.format('', '\033[92m[2]\033[97m para octal.'))
    print('{:64}{}'.format('', '\033[92m[3]\033[97m para hexadecimal.'))
    print('{:64}{}'.format('', '\033[92m[4]\033[97m para todos.'))
    print('{:64}{}'.format('', '\033[92m[x]\033[97m para sair.'))
    ans = str(input('{:64}{}'.format('', '\033[mDigite aqui:\033[97m '))).strip().lower()
    if ans == '1':
        ine = int(input('\n{:>79}'.format('Valor inteiro: ')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em binário |', format(ine, 'b')))
        print('\n{:64}{}'.format('', '\033[92m[0]\033[97m para repetir.'))
        print('{:64}{}'.format('', '\033[92m[x]\033[97m para sair.'))
        a = str(input('{:64}{}'.format('', '\033[mDigite aqui:\033[97m '))).strip().lower()
        if a == 'x':
            break
        elif a == '0':
            b = True

    elif ans == '2':
        ine = int(input('\n{:>79}'.format('Valor inteiro: ')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em octal |', format(ine, 'o')))
        print('\n{:64}{}'.format('', '\033[92m[0]\033[97m para repetir.'))
        print('{:64}{}'.format('', '\033[92m[x]\033[97m para sair.'))
        a = str(input('{:64}{}'.format('', '\033[mDigite aqui:\033[97m '))).strip().lower()
        if a == 'x':
            break
        elif a == '0':
            b = True

    elif ans == '3':
        ine = int(input('\n{:>79}'.format('Valor inteiro: ')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em hexadecimal |', format(ine, 'x')))
        print('\n{:64}{}'.format('', '\033[92m[0]\033[97m para repetir.'))
        print('{:64}{}'.format('', '\033[92m[x]\033[97m para sair.'))
        a = str(input('{:64}{}'.format('', '\033[mDigite aqui:\033[97m '))).strip().lower()
        if a == 'x':
            break
        elif a == '0':
            b = True

    elif ans == '4':
        ine = int(input('\n{:>79}'.format('Valor inteiro: ')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em binário |', format(ine, 'b')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em octal |', format(ine, 'o')))
        print('{:64}{} \033[93m{}\033[97m'.format('', 'Em hexadecimal |', format(ine, 'x')))
        print('\n{:64}{}'.format('', '\033[92m[0]\033[97m para repetir.'))
        print('{:64}{}'.format('', '\033[92m[x]\033[97m para sair.'))
        a = str(input('{:64}{}'.format('', '\033[mDigite aqui:\033[97m '))).strip().lower()
        if a == 'x':
            break
        elif a == '0':
            b = True

    elif ans == 'x':
        break
    else:
        print('{:^154}'.format('Não entendi sua resposta, então encerrarei.'))
        break
