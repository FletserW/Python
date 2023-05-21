num = (int(input(f'Digite o 1° Número: ')),
    int(input(f'Digite o 2° Número: ')),
    int(input(f'Digite o 3° Número: ')),
    int(input(f'Digite o 4° Número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print('O valor 3 apareceu na {}° posição'.format(num.index(3) + 1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares)
