from time import sleep
from random import randint
""" VARIAVEIS """
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 3)
print('-=-' * 13)
print('{}   Ola gostaria de jogar Jokenpô?{}'.format(cores['azul'], cores['limpar']))
print('-=-' * 13)
play = str(input('{}S{} ou {}N{}: '
                 .format(cores['verde'], cores['limpar'], cores['vermelho'], cores['limpar']))).upper()

""" COMANDOS """
if 'S' in play:
    print("""Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")
    jogado = int(input('Qual será sua jogada? '))
    if 0 <= jogado <4:
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!')
        sleep(0.5)
        print('-=' * 12)
        if jogado == pc:
            print('{}{:^24}{}'.format(cores['amarelo'], 'Empatou', cores['limpar']))
        elif jogado == 'PEDRA' and pc == 'TESOURA':
            print('{}Parabens, você ganhou{}!'.format(cores['verde'], cores['limpar']))
        elif jogado == 'PAPEL' and pc == 'PEDRA':
            print('{}Parabens, você ganhou{}!'.format(cores['verde'], cores['limpar']))
        elif jogado == 'TESOURA' and pc == 'PAPEL':
            print('{}Parabens, você ganhou{}!'.format(cores['verde'], cores['limpar']))
        else:
            print('{}Você perdeu, ksksksks{}'.format(cores['vermelho'], cores['limpar']))
        print('-=' * 12)
    else:
        print('{}#ERRO#{}'.format(cores['vermelho'], cores['limpar']))
elif 'N' in play:
    print('\nOk, tenha um bom dia.')
else:
    print('Você não sabe lê?')
