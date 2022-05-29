print('\033[97m')
soma_idades = 0
mais_velho = ''
maior_idade = 0
mulher_jovem = 0
for a in range(1, 5):
    print(f'==== {a}ª PESSOA ====')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    soma_idades += idade
    if sexo == 'M':
        if a == 1:
            maior_idade = idade
            mais_velho = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                mais_velho = nome
            elif idade < maior_idade:
                maior_idade = maior_idade
    elif sexo == 'F':
        if idade < 20:
            mulher_jovem += 1
        else:
            pass
media = soma_idades / 4
print(f'\nA média das idades apresentadas é {media} anos')
print(f'O homem mais velho dos analisados é o {mais_velho}, com {maior_idade} anos.')
print(f'Nesse grupo há {mulher_jovem} mulheres abaixo de 20 anos.')