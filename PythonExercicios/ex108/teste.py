from ex108 import moeda

num = float(input('Digite um número: R$'))
print(f'''O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}
A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}
Aumentado em 10%: {moeda.moeda(moeda.aumentar(num, 10))}
Diminuído em 10%: {moeda.moeda(moeda.diminuir(num, 10))}''')
