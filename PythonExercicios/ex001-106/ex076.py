list = ('Lápis', 1.95, 'Caneta', 2.10, 'Borracha', 2.40, 'Régua', 4.10,
        'Caderno', 14.50, 'Agenda', 18.99, 'Mochila', 244.99, 'Estojo', 34.99,
        'Transferidor', 8.90, 'Compasso', 7.50, 'Lápis_de_cor', 15.90, 'Fichário', 145.99,
        'Caderno_Fichário', 13.80, 'Mochila_com_rodas', 260.50, 'Papel_colorido', 14.90, 'Corretivo', 15.98)
print('''\033[97m{}
{:^44}
{}'''.format('=' * 45, 'LOJA BOM PREÇO', '=' * 45))
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print('{:.<35}'.format(list[pos]), end=' ')
    else:
        print('R$ \033[92m{:>6.2f}\033[97m'.format(list[pos]))
print('=' * 45)
