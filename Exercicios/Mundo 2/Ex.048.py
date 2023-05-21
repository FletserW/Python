print('A soma de todos os números impares entre 1 e 500:')
num = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        num = num + c
print(num)
