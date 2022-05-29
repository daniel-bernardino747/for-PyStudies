banco_de_dados = dict()
banco_de_dados['nome'] = str(input('\033[97mNome: '))
banco_de_dados['media'] = float(input('Média: '))
if banco_de_dados['media'] >= 7.0:
    banco_de_dados['Situação'] = 'Aprovado'
else:
    banco_de_dados['Situação'] = 'Reprovado'
print(f'O \033[94m{banco_de_dados["nome"]}\033[97m teve média \033[94m{banco_de_dados["media"]}\033[97m.'
      f'\nEste aluno está \033[93m{banco_de_dados["Situação"]}\033[97m.')
print(f'{"=" * 30}\n Dicionário: {banco_de_dados}\n{"=" * 30}')
