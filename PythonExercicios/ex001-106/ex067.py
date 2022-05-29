count = 0
while True:
    n = int(input('\033[97mQuer ver a tabuada de qual valor? '))
    print('=' * 30)
    if n < 0:
        break
    while count != 10:
        count += 1
        print(f'{n} X {count:2} = {n * count:2}')
    count = 0
    print('=' * 30)
    if n == 0:
        break
