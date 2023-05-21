from time import sleep
""" VARIAVEIS """
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:31:30m'}
print('Calculadora de IMC')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura * altura)

""" COMANDOS """
print('-' * 20)
if imc < 18.5:
    print('Você está {}Abaixo do peso{}'.format(cores['amarelo'], cores['limpar']))
elif 18.5 <= imc < 25:
    print('Você está com {}Peso ideal{}'.format(cores['verde'], cores['limpar']))
elif 25 <= imc < 30:
    print('Você está com {}Sobrepeso{}'.format(cores['amarelo'], cores['limpar']))
elif 30 <= imc < 40:
    print('Você está {}Obesidade{}'.format(cores['vermelho'], cores['limpar']))
else:
    print('Você está com {}Obsidade Mórbida{}'.format(cores['pretoebranco'], cores['limpar']))
print('-' * 20)
