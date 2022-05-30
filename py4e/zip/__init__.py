a = ('Daniel', 'Gabriel', 'Emanuel')
b = ('18', '8', '15')
c = ('M', 'M', 'M')
d = ('1.73', '1.35', '1.81')
x = zip(a, b, c, d)
y = list(x)

if __name__ == '__main__':
    for i, v in enumerate(y):
        print(f'{i} = {v[0]}')
    print('=' * 5)
    m, n, o, p = zip(*y)
    print('m =', m)
    print('n =', n[1])
    print('o =', o[1])
    print('p =', p[-1])
