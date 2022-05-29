# from time import sleep
c = {'clean': '\033[m',
     'white': '\033[0:97m',
     'blue': '\033[34m',
     'green': '\033[1:32m'}
print('\033[34m=\033[m' * 70)
print('{}Vamos calcular sua média trimestral.{}'.format(c['white'], c['clean']))
# sleep(1.7)
n1 = float(input('{}Digite sua {}primeira nota{}: {}'.format(c['white'], c['blue'], c['white'], c['clean'])))
# sleep(0.2)
n2 = float(input('{}Agora sua {}segunda nota{}: {}'.format(c['white'], c['blue'], c['white'], c['clean'])))
# sleep(0.2)
n3 = float(input('{}Por fim sua {}última nota{}: {}'.format(c['white'], c['blue'], c['white'], c['clean'])))
# sleep(0.3)
print('{}Um momento...{}'.format(c['white'], c['clean']))
# sleep(0.5)
m = ((n1 + n2 + n3) / 3)
if m >= 7.1:
    n = ('\033[1:32m {:.2f} \033[m'.format(m))
    print('{}Com base nas suas notas, sua {}média trimestral {}é {}{}{}!'.format(c['white'], c['blue'], c['white'],
                                                                                     c['clean'], n, c['white']))
    print('Esse trimestre você foi muito bem, continue se esforçando!')

elif m < 7.1 and m >= 7:
     n = ('\033[1:33m {:.2f} \033[m'.format(m))
     print('{}Com base nas suas notas, sua {}média trimestral {}é {}{}{}!'.format(c['white'], c['blue'], c['white'],
                                                                                  c['clean'], n, c['white']))
     print('Esse trimestre você foi em cima da linha, né!? Vamos nós esforçar mais no próximo!')

else:
     n = ('\033[1:31m {:.2f} \033[m'.format(m))
     print('{}Com base nas suas notas, sua {}média trimestral {}é {}{}{}!'.format(c['white'], c['blue'], c['white'],
                                                                                  c['clean'], n, c['white']))
     print('Infelizmente você ficou de recuperação, mas veja isso como uma oportunidade de aprender'
           ' ainda mais o conteúdo!')
