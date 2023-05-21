""" VARIAVEIS """
num = int(input('Digite um valor inteiro: '))
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:30m'}

""" COMANDOS """
print('-' * 20)
if num % 2 == 0:
    print('{}Esse numero é Par{}.'.format(cores['verde'], cores['limpar']))
else:
    print('{}Esse numero é Impar.{}'.format(cores['azul'], cores['limpar']))

print('-' * 20)
