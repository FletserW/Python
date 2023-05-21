print('A soma de numeros pares:')
s = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1

print('A soma do {} valores pares é: {}'.format(cont, s))
