from random import randint
from time import sleep

""" Variaveis """
num = randint(1, 5)

""" Comandos """
print('\nVou pensar em um número entre 0 e 5. tente adivinhar...\n{}'.format('¨¨¨¨' * 15))
r = int(input('Em que número estou pensando? '))
if 1 <= r <= 5:
    print('Analizando....')
    sleep(2)
    print('-=-' * 15)
    if r == num:
        print('{:^45}'.format('Parabens você ganhou!!!'))
    else:
        print('Você perdeu, mais sorte na proxima vez.')
    print('-=-' * 15)
else:
    print('Numero Invalido.')
print('END.')
