n = int(input('Quantos números da Sequência de Fibonacci você quer ver? '))
t1 = 0
t2 = 1
count = 3
mais = 0
print(f'{t1} -> {t2} -> ', end='')
while count <= n:
    t3 = t1 + t2
    if count == n:
        print(f'{t3}', end='')
        mais = int(input('Quer ver mais quantos termos? '))
    else:
        print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    count += 1
