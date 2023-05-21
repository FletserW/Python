from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor de cateto adjacente: '))
print('O valor da hipotenusa de {} e {} é: {:.2f}.'.format(co, ca, hypot(co, ca)))
