c = True
numeros = ('zero um dois tres quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis '
           'dezessete dezoito dezenove vinte').split()
while c:
    num = int((input('Digite um número: [Entre 0 e 20] ')))
    while True:
        if 0 <= num <= 20:
            break
        else:
            num = int(input('Tente Novamente. Digite um número: [Entre 0 e 20] '))
    print(f'Você digitou o número {numeros[num]}')
    print('-' * 32)
    while True:
        reset = str(input('Deseja continuar: [S/N] ')).strip().upper()
        if reset[0] in 'SN':
            if reset[0] == 'S':
                break
            else:
                c = False
                break
