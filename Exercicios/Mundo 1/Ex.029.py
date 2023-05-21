from time import sleep
""" VARIAVEIS """
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretoebranco':'\033[7:30m'}
v = float(input('Digite a velocidade corrida: '))

""" COMANDOS """
print('Analizando...')
sleep(2)
if v > 80.0:
    print('-' * 70)
    print('\033[31mMultado!\033[m Vocé ultrapassou o limite de velocidade permitida de 80Km/h\n'
          'O valor da multa é: R${}'.format((v - 80) * 7))
    print('-' * 70)
else:
    print('-' * 45)
    print('Continue tomando cuidado e tenha um bom dia.')
    print('-' * 45)
print('End.')
