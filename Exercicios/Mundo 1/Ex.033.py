""" VARIAVEIS """
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite mais um numero: '))

""" COMANDOS """
# verificar menor valor.
menor = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c

# Verificar maior valor.
maior = a
if b < a and b < c:
    maior = b
if c < a and c < b:
    maior = c
print('O menor valor é: {}\n'
      'O maior valor é: {}'.format(maior, menor))
