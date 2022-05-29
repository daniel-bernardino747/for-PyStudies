password = 'password'


def wrong_pass(msg):
    print(f'<A senha digitada foi {msg}, mas não é a correta>')
    yield 1
    print(f'<A senha digitada foi {msg}, mas não é a correta>')
    yield 2
    print(f'<CUIDADO: Essa é sua última tentativa.>')
    yield 3


def correct_pass(msg):
    print(f'<A senha digitada foi {msg}, está correta>')


msg = str(input('Digite sua senha: '))
error = wrong_pass(msg)
while True:
    try:
        if msg == password:
            correct_pass(msg)
            break
        else:
            next(error)
        msg = str(input('Digite sua senha: '))
    except StopIteration:
        print('\033[91mCONTA BLOQUEADA.')
        break
