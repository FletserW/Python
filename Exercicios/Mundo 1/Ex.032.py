from datetime import date
""" VARIAVEIS """
ano = int(input('Digite o ano a ser analizado: '))
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:30m'}

""" COMANDOS """
print('Analizando...\n{}'.format('-' * 30))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}Esse ano {} é Bissexto.{}'.format(cores['verde'], ano, cores['limpar']))
else:
    print('{}Esse ano {} Não é bissexto.{}'.format(cores['vermelho'], ano, cores['limpar']))
print('-' * 30)
