from time import sleep
""" VARIAVEIS """
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:30m'}
print('-=-' * 18)
casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual o seu salario? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (anos*12)
print('-=-' * 18)

""" COMANDO """
print('Analizando...')
sleep(2)
if parcela > (30/100 * salario):
    print('{}Seu empréstimo foi negado.{}'.format(cores['vermelho'], cores['limpar']))
else:
    print('{}Seu empréstimo foi aprovado.{}\n'
          'A prestação em {} anos será de R${:.2f}'.format(cores['verde'], cores['limpar'], anos, parcela))
print('-=-' * 18)
