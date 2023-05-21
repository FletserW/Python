""" VARIAVEIS """
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

""" CONTROLES """
print('Analizando...\n{}'.format('-' * 30))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Esse triangulo é equilátero.')
    elif n1 != n2 != n3 != n1:
        print('Esse triângulo é Escaleno.')
    else:
        print('Esse triângulo é Isósceles.')
else:
    print('Isso não é um triângulo.')
print('-' * 30)
