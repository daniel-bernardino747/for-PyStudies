def gen():
    print('começo')
    yield 1
    print('meio')
    yield 2
    print('fim')
    yield 3

g = gen()
try:
    next(g)
    next(g)
    next(g)
    next(g)
except StopIteration:
    print('error')