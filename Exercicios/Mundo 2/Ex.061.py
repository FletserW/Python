num = int(input('Primeiro termo: '))
r = int(input('Ração: '))
pi = 0
c = num - r
while pi < 10:
    c += r
    print(c, '→', end=' ')
    pi += 1
print('Fim')
