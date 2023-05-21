from time import sleep
from random import randint
pi = ''
cont = 0
print('=-' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-' * 20)
while True:
    pc = randint(0, 11)
    num = int(input('Diga um valor? '))
    jg = ''
    while True:
        jg = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        if jg in 'PI':
            break
    pi = 'Par' if (num + pc) % 2 == 0 else 'Impar'
    print('-' * 30)
    print(f'Você jogou {num} e o Computador {pc}. Total de {num + pc} deu {pi}')
    print('-' * 30)
    if pi == 'Par' and jg in 'P' or pi == 'Impar' and jg in 'I':
        sleep(2)
        print('Você VENCEU!\nVamos jogar novamente...')
        cont += 1
        print('=-' * 15)
    else:
        sleep(2)
        print('Você PERDEU.')
        break
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
