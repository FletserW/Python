""" Variaveis """
pi = n = 0
num = list()
par = list()
impar = list()

""" COMANDOS """
while pi == 0:
    num.append(int(input('Digite um valor: ')))
    n += 1
    while True:
        reset = str(input('Quer continuar? [S/N] ')).upper().strip()
        if reset in 'N':
            pi = 1
            break
        if reset in 'S':
            break
        else:
            print('Comando invalido!, tente novamente.')
print('-=' * 25)
print(f'A lista completa é {num}')
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
