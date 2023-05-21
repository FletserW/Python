from time import sleep
""" VARIAVEIS """
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
print('-=-' * 10)
print('{}Confira sua situação escolar.{}'.format(cores['azul'], cores['limpar']))
print('-=-' * 10)
n1 = float(input('Primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2

""" COMANDO """
print('Analizando...')
sleep(2)
print('-=-' * 5)
if media < 5:
    print('{}   REPROVADO{}'.format(cores['vermelho'], cores['limpar']))
elif 5 < media < 6.9:
    print('{}  RECUPERAÇÃO{}'.format(cores['amarelo'], cores['limpar']))
else:
    print('{}   APROVADO{}'.format(cores['verde'], cores['limpar']))
print('-=-' * 5)
