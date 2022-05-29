"""print('\033[97m')
s = 0
resultado = 1
count = 1
x = int(input('Digite um valor para fatoriar: '))
y = x
print(f'{x}! = ', end='')
while count <= x:
    if y == 1:
        print('1 = ', end='')
    else:
        print(y, 'x ', end='')
    resultado *= count
    count += 1
    y -= 1
print(resultado)"""
print('\033[97m')
numero = int(input('Digite um valor para fatoriar: '))
c = numero
f = 1
print(f'{numero}! =', end=' ')
for a in range(numero, 0, -1):
    print(a, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)
