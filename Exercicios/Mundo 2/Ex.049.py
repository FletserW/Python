n = int(input("Digite o numero que deseje a tabuada: "))
print('-' * 13)
for c in range(2, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))
print('-' * 13)
