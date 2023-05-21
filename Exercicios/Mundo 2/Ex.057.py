from time import sleep
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
sex = ''
pi = 0
while True:
    sex = str(input('Qual o seu sexo?\n'
                    '[M] ou [F]: ')).strip().upper()

    if sex in 'MF':
        break
    else:
        print('{}CODIGO INVALIDO.\nTente novamente.{}'.format(cores['vermelho'], cores['limpar']))
    print('-=' * 15)
    sleep(0.5)
print('{}Sexo {} registrado com sucesso.{}'.format(cores['verde'], sex, cores['limpar']))
