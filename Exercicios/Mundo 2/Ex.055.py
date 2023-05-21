
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg e o menor {}Kg.'.format(maior, menor))
