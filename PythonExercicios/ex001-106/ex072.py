numero_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
                  'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero_decimal = int(input('\033[97mDigite um valor entre 0 e 20: '))
    if 0 <= numero_decimal <= 20:
        print(f'Você digitou o número: \033[94m{numero_extenso[numero_decimal]}\033[97m.')
        novamente = str(input('Aperte Enter caso deseja continuar, senão, digite qualquer coisa: '))
        if novamente == '':
            pass
        else:
            break
    else:
        print('\033[mNúmero inválido.', end=' ')
print('\nObrigado por jogar comigo.')
