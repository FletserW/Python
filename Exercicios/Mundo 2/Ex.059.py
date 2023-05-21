from time import sleep
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
pi = maior = 0
n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
while pi == 0:

    print('{}{:-^25}{}'.format(cores['azul'], 'Menu', cores['limpar']))
    print("""[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Verificar maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa""")
    comando = int(input('>>>> O que deseja? '))
    print('-=' * 20)
    if comando == 1:
        print('{:^40}'.format('A soma de ({}) + ({}) é ({})'.format(n1, n2, n1 + n2)))
    elif comando == 2:
        print('{:^40}'.format('O resultado de ({}) X ({}) é ({})'.format(n1, n2, n1 * n2)))
    elif comando == 3:
        if n1 > n2:
            maior += n1
        else:
            maior += n2
        print('{:^40}'.format('O maior número é {}'.format(maior)))
    elif comando == 4:
        print('Informe os numeros novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif comando == 5:
        pi += 1
    else:
        print('Comando Invalido')
    print('-=' * 20)
    sleep(4)
    print('\n\n')

