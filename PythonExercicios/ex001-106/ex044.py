print('=' * 152)
print('''{}{}
{}== FORMA DE PAGAMENTO ==
{}{}{}\n'''.format('\033[94m', '=' * 24, '\033[1:94m', '\033[0:94m', '=' * 24, '\033[97m'))
valor = float(input('Valor da Compra: '))
print('''Selecione uma das opções de pagamento:
 [ 1 ] \033[3:97mÀ vista\033[0:97m em Dinheiro/Cheque;
 [ 2 ] \033[3:97mÀ vista\033[0:97m no Cartão; 
 [ 3 ] Até \033[3:97m2x\033[0:97m no Cartão;
 [ 4 ] \033[3:97m3x ou mais\033[0:97m no Cartão;''')
ans = int(input('Qual a opção? '))
if ans == 1:
    desconto = valor * 0.9
    print(f'O valor com desconto de 10% é de \033[1:94m{desconto} reais\033[1:97m.')
elif ans == 2:
    desconto = valor * 0.95
    print(f'O valor com desconto de 5% é de \033[1:97m{desconto} reais\033[1:97m. ')
elif ans == 3:
    print(f'Nessa opção de pagamento não realizamos desconto, o preço permanece inalterado no valor de {valor} reais '
          f'parcelado duas vezes.')
elif ans == 4:
    n = int(input('Quantidade de parcelas: '))
    juros = valor * 0.2
    parcela = (valor + juros) / n
    print(f'O valor total com juros é de \033[1:94m{valor + juros}\033[0:97m reais e, pelo número de \033[1:94m{n}'
          f'\033[0:97m parcelas, cada parcela fica no valor de \033[1:94m{parcela}\033[0:97m reais.')
