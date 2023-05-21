pi = 998
cont = 1
soma = 0
while pi != 999:
    num = int(input('digite o {}° valor: '.format(cont)))
    if num != 999:
        soma += num
        cont += 1
    if num == 999:
        pi += 1
print('Foram digitados {} valores e a soma entre eles é {}'.format(cont - 1, soma))
