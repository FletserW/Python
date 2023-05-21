from math import radians, sin, cos, tan

num = float(input('Digite um ângulo: '))
ang = radians(num)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(ang), cos(ang), tan(ang)))

