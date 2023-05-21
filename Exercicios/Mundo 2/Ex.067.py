cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    cont = 0
    if num < 0:
        print('Programa tabuada encerrado. Volte Sempre!')
        break
    print('-' * 35)
    while cont < 10:
        cont += 1
        print(f'{num} X {cont:2} = {num * cont}')

    print('-' * 35)

