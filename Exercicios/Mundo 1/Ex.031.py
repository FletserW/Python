from time import sleep
""" VARIAVEIS """
d = int(input('Qual a distancia de sua viagem em Km: '))
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:30m'}

""" COMANDOS """
print('{}Analizando...{}\n{}'.format(cores['verde'], cores['limpar'], '-' * 35))
sleep(2)
if d > 200:
    print('O valor da viagem será: R${:.2f}'.format(d * 0.45))
else:
    print('O valor da viagem será: R${:.2f}'.format(d * 0.50))
print('-' * 35)
