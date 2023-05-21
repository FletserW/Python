total = cont = menor = 0
barato = ''
print('-' * 50)
print(f"{'FLETSER SHOP':^40}")
print('-' * 50)
while cont >= 0:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        cont += 1
    if total == preco or preco < menor:
        menor = preco
        barato = nome
    while cont >= 0:
        reset = str(input('Quer continuar [S/N] ')).strip().upper()[0]
        if reset in 'SN':
            if reset in 'S':
                print('-' * 30)
                break
            else:
                print(f'{" FIM DO PROGRAMA ":=^50}')
                print(f'O total da comapra foi R${total:.2f}\n'
                      f'Temos {cont} produtos custando mais de R$1.000,00\n'
                      f'O produto mais barato foi a {barato} que custa R${menor:.2f}')
                cont = -1
