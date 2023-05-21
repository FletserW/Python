""" VARIAVEIS """
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite mais um valor: '))

""" CONTROLES """
print('Analizando...\n{}'.format('-' * 40))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses comprimentos formam um triangulo.')
else:
    print('Esses comprimento não forma um triangulo.')
print('-' * 40)
