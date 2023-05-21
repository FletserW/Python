from  random import randint
from time import sleep

""" VARIAVEIS """
num = randint(1, 11)
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
tentativas = pi = 1
""" COMANDOS """
print('-=' * 25)
print('{}Adivinhe o numero que estou pensando entre 0 e 10{}'.format(cores['azul'], cores['limpar']))
print('-=' * 25)

while pi == 1:
    r = int(input('Digite um numero entre 0 e 10: '))
    print('Analizando... .')
    sleep(2)
    if r == num:
        print('\033[32m', '-' * 45)
        print('Parabéns você acertou!, na sua {}° tentativa.'.format(tentativas))
        print('-' * 45, '{}'.format(cores['limpar']))
        pi += 1
    elif r < num:
        print('\033[31m', '-' * 35)
        print('{:^35}'.format('Mais... Tente novamente.'))
        print('-' * 35, '{}'.format(cores['limpar']))
        tentativas += 1
    elif r > num:
        print('\033[31m', '-' * 35)
        print('{:^35}'.format('Menos... Tente novamente.'))
        print('-' * 35, '{}'.format(cores['limpar']))
        tentativas += 1
