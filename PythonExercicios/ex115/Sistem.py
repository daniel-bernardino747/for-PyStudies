from ex115.lib import interface as inter
from ex115.lib import arquivo as file
from time import sleep

arq = 'cursoemvideo.txt'
if not file.arqexist(arq):
    file.createarq(arq)

while True:
    inter.header('MENU PRINCIPAL DE CADASTRO', '=', )
    inter.options('Cadastrar nova Pessoa.', 'Verificar pessoas cadastradas.', 'Sair do Menu.')
    inter.linha('=', 48)
    sleep(0.5)
    while True:
        resp = inter.question('Sua opção: ')
        sleep(0.7)
        try:
            if resp == 1:
                inter.header('NOVO CADASTRO', '=')
                while True:
                    try:
                        nome = str(input('\033[93m >>>\033[97m Nome: '))
                    except(ValueError, TypeError):
                        print('\033[mInformação inválida, tente novamente.')
                    else:
                        break
                while True:
                    try:
                        idade = int(input('\033[93m >>>\033[97m Idade: '))
                    except(ValueError, TypeError):
                        print('\033[mInformação inválida, tente novamente.')
                    else:
                        break
                file.register(arq, nome, idade)
                inter.linha('=', 48)
            elif resp == 2:
                inter.header('LISTA DE CADASTRADOS', '=')
                sleep(0.3)
                file.readarq(arq)
                inter.linha('=', 48)
            elif resp == 3:
                inter.header('PROGRAMA ENCERRADO', '=')
                break
            elif resp > 3:
                print('\033[mNão existe essa opção.')
        except:
            print('\033[mValor não encontrado. Tente uma das opções acima.\033[97m')
        sleep(2)
        break
    if resp == 3:
        break
