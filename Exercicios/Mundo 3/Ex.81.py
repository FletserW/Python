""" Variaveis """
pi = n = 0
num = list()

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
print(f'Você digitou {n} elementos.')
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista')
