from time import sleep
from datetime import date
""" VARIAVEIS """
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
print('-=-' * 16)
print('{}{:^50}{}'.format(cores['azul'], 'Consultar alistamento.', cores['limpar']))
print('-=-' * 16)
nasceu = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nasceu
print('Analizando...')
sleep(2)

""" COMANDO """
print('-=-' * 16)
if idade == 18:
    print('{}Está na hora de se alistar,{}\nse dirija ao quartel mais proximo.'.format(cores['verde'], cores['limpar']))
elif 0 < idade < 18:
    print('{}Está chegando a hora de se alistar, falta {} anos.\n'
          'Seu alistamento será em {}{}'.format(cores['amarelo'], 18 - idade, ano + (18 - idade), cores['limpar']))
elif idade < 0:
    print('{}#ERRO#{}'.format(cores['vermelho'], cores['limpar']))
else:
    print('Vocé deverio ou foi ao exército há {} anos.'.format(idade - 18))
