cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7:30m'}
pi = 1
print(f"{cores['azul']}{'Calculadora Fatorial':=^40}{cores['limpar']}")
num = int(input('Digite um numero: '))
x = num
while pi < num - 1:
    x = x * (num - pi)
    pi += 1
print('O numero fatorial de {} é {}'.format(num, x))
