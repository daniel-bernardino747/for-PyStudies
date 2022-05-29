from program.lib import interface as inface
from program.lib import arquivo as arq

irmandade = 'database_irmandade.txt'
arq.openFile('database_irmandade.txt')

inface.MenuPrincipal('PAZ DE DEUS')
resp = inface.options('Ver Lista Completa da Irmandade', 'Adicionar Nova Pessoa', 'Alterar um Cadastro')
if resp == 1:
    inface.c()
    inface.MenuPrincipal('IRMANDADE')
    arq.readFile(irmandade)
elif resp == 2:
    inface.c()
    inface.MenuPrincipal('Cadastro de Nova Pessoa')
    name = str(input(f''
                     f'{inface.stl.inverse}{inface.stl.bright}'
                     f'{" >>> DIGITE O NOME:":}'
                     f'{inface.stl.reset_all}{inface.fg.white} '))
    idade = int(input(f''
                      f'{inface.stl.inverse}{inface.stl.bright}'
                      f'{" >>> DIGITE A IDADE:":30}'
                      f'{inface.stl.reset_all}{inface.fg.white} '))
    estado = str(input(f''
                       f'{inface.stl.inverse}{inface.stl.bright}'
                       f'{" >>> DIGITE O ESTADO CIVIL:":}'
                       f'{inface.stl.reset_all}{inface.fg.white} '))


elif resp == 3:
    inface.c()
    inface.MenuPrincipal('Alteração de Informações')
elif resp == 0:
    inface.c()
    inface.MenuPrincipal(nexit='Saindo do programa', aexit=True)
