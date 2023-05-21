# from time import sleep
valor = cont = 0
nota = 0
print('=' * 30)
print(f'{"BANCO FLETSER":^30}')
print('=' * 30)
num = int(input('Que valor você quer sacar? R$'))
while True:
    if num == 0:
        break
    else:
        if num >= 50:
            nota = 50
        elif num >= 20:
            nota = 20
        elif num >= 10:
            nota = 10
        elif num >= 1:
            nota = 1
    num -= nota
    cont += 1
    if num < nota:
        print(f'Total de {cont} cédulas de R${nota}')
        cont = 0
print('=' * 30)
print('Volte sempre ao Banco Fletser! Tenha um bom dia!')
