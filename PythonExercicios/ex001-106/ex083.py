frase = str(input('Digite uma expressão que comece e termine com parênteses: ')).strip()
t = list(frase)
soma = 0
for i, v in enumerate(t):
    if v == '(':
        soma += 1
    elif v == ')':
        soma -= 1
if soma == 0:
    print('Essa expressão está correta.')
else:
    print('Essa expressão está errada.')
