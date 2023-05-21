from time import sleep
num = int(input('Primeiro termo: '))
r = int(input('Ração: '))
pi = 0
c = num - r
termos = 10
while pi < termos:
    c += r
    print(c, '→', end=' ')
    print('Pausa')
    pi += 1
    if pi == termos:
        termos = int(input('\nQuantos termos você quer mostrar a mais? '))
        pi = 0
        print('-' * 50)

print('fim')
