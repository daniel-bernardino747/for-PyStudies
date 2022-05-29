# OBS.: Não trava
def impares():
    valor = 1
    while True:
        yield valor
        valor += 2


n = impares()
for i in n:
    print(i)
