words = ('PYTHON', 'CURSOEMVIDEO', 'DANIEL', 'AUTODIDATA', 'TRABALHO',
         'VIDANOVA', 'LINGUAGEM', 'PROGRAMAÇAO', 'PRATICAR', 'MERCADO',
         'OPORTUNIDADE', 'FUTURO', 'ESTABILIDADE', 'ALEGRIA', 'PAZ')
for ordem in words:
    print(f'\n\033[97mNa palavra \033[94m{ordem}\033[97m temos as vogais: ', end='')
    for letra in ordem:
        if letra in 'AEIOU':
            print(f'\033[94m{letra}\033[97m', end=' ')
