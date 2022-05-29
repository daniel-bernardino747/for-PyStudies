list1 = list()
pares = list()
impares = list()
while True:
    list1.append(int(input('Digite um valor: ')))
    """if list1[-1] % 2 == 0:
        list2.append(list1[-1])
    else:
        list3.append(list1[-1])"""
    sair = str(input('Deseja continuar? [S/N] '))
    if sair in 'Nn':
        break
for i, v in enumerate(list1):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(list1)
print(pares)
print(impares)
