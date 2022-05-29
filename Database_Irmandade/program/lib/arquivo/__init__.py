def openFile(msg):
    try:
        a = open(msg, 'r')
        a.close()
    except FileNotFoundError:
        res = 'Esse Documento não existe. Vou criá-lo.'
        a = open(msg, 'x')
        a.close()
        return res
    else:
        res = 'Esse Documento existe.'
        return res


def readFile(msg):
    try:
        a = open(msg, 'r')
    except FileNotFoundError:
        print('\033[91mO Documento não foi encontrado.')
    except (ValueError, TypeError):
        print('Tivemos algum problema na apresesentação do Documento, consulte o Suporte.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'| {dado[0]:19}{dado[1]:18}{dado[2]:20}|')


def writeFile(local, name='<desconhecido>', age='<desconhecida>', marital='<desconhecido>'):
    a = open(local, 'a')
    a.write(f'{name};{age};{marital}\n')
    a.close()

