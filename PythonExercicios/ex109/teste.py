from ex109 import moeda

num = float(input('Digite um número: R$'))
print(f'''O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}
A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}
Aumentado em 10%: {moeda.aumentar(num, 10, True)}
Diminuído em 13%: {moeda.diminuir(num, 13, True)}''')
