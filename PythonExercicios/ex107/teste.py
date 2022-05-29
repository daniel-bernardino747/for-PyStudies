from ex107 import moeda

num = float(input('Digite um número: R$'))
print(f'''O dobro de {num} é {moeda.dobro(num)}
A metade de {num} é {moeda.metade(num)}
Aumentado em 10%: {moeda.aumentar(num, 10)}
Diminuído em 10%: {moeda.diminuir(num, 10)}''')
