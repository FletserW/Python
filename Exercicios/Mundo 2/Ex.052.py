num = int(input('Digite um valor: '))
divisivel = 0
for c in range(1, 11):
    if num % c == 0:
        divisivel = divisivel + 1
        print(c, end=' ')
if  divisivel < 3:
    print('\nEsse número é primo.')
else:
    print('\nEsse número não é primo.')
