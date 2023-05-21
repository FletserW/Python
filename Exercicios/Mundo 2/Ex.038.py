from time import sleep
""" VARIAVEIS """
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:'))

""" COMANDOS"""
print('-=-' * 10)
print('Analizando...')
sleep(2)
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
print('-=-' * 10)
