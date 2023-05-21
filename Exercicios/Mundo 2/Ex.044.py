from time import sleep
""" VARIEDADE """
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
print('{}{:#^40}{}'.format( cores['azul'],' Atacado Fletser ', cores['limpar']))
valor = float(input('Qual o valor do produto? '))
print('-' * 33)
pagamento = int(input('Escolha um metodo de pagamento:\n'
                      'Dinheiro/Cheque = [ 1 ]\n'
                      'À vista cartão  = [ 2 ]\n'
                      '2x no cartão    = [ 3 ]\n'
                      '3x no cartão    = [ 4 ]\n'
                      'Metodo de pagamento: '))
print('-' * 33)
print('Analizando...\n')
sleep(2)

""" COMANDOS """
if pagamento == 1:
    print('À vista fica: R${:.2f}'.format(valor - (10/100 * valor)))
elif pagamento == 2:
    print('À vista no cartã0 fica: R${:.2f}'.format(valor - (5/100 * valor)))
elif pagamento == 3:
    print('2X no cartão fica R${:.2f} a parcela e R${:.2f} no total'.format(valor / 2, valor))
elif pagamento == 4:
    total = valor + (20/100 * valor)
    parcela = int(input('Qual o numero de parcelas? '))
    print('{}X no cartão fica R${:.2f} as parcelas e R${:.2f} no total.'.format(parcela, total / parcela, total))
else:
    print('Metodo de pagamento invalido.')
