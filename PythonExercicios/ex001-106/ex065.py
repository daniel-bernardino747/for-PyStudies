resposta = ''
soma = count = maior = menor = 0
while resposta != 'N':
    print('\033[97m~' * 30)
    count += 1
    n = int(input('Digite um número: '))
    resposta = str(input('>>> Quer continuar? [S/N] ')).upper().strip()[0]
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
media = soma / count
print(f'Você digitou {count} números e a média deles é {media}.\n'
      f'O maior número é {maior} e o menor é {menor}.')
