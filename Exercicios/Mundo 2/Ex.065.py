pi = 0
soma = 0
cont = 1
menor = maior = 0

while pi < 5:
    num = int(input('Digite o {}° valor: '.format(cont)))
    if cont == 1:
        menor = maior = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    cont += 1
    pi += 1
    if pi == 5:
        reset = int(input('Deseja continuar?\n'
                          '[ 1 ] Sim\n'
                          '[ 2 ] Não\n'
                          'Qual sua resposta: '))
        if reset == 1:
            pi = 0
media = soma / (cont - 1)
print("""A media de todos os {} valores foi {}  
O maior valor: {}
O menor valor: {}""".format(cont - 1, media, maior, menor))
