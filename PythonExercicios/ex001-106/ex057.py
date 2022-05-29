print('\033[97m')
a = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while a != 'M' and a != 'F':
    a = str(input('Desculpe, não consegui compreender. Pode me dizer qual o seu sexo? ')).upper().strip()
if a == 'F':
    print(f'O sexo FEMININO foi registrado com sucesso.')
elif a == 'M':
    print(f'O sexo MASCULINO foi registrado com sucesso.')
