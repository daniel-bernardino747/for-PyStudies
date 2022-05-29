def arqexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createarq(name):
    try:
        a = open(name, 'x')
        a.close()
    except:
        print('Não consegui criar o arquivo.')
    else:
        return


def readarq(name):
    try:
        a = open(name, 'r')
    except:
        print('Erro na leitura do arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{">":>3} \033[97m{dado[0]:15}\033[m ||  \033[97mIdade: {dado[1]:>3} anos\033[m')


def register(arq, name='<desconhecido>', age=0):
    try:
        a = open(arq, 'a')
        a.write(f'{name};{age}\n')
        a.close()
    except:
        print('Não conseguimos cadastrar.')
    else:
        print(f'{"Cadastrado com sucesso.":^48}')
