num = int(input('Primeiro termo: '))
r = int(input('Ração: '))
for c in range(num, num + r * 10, r):
    print(c)
