lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compassa', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
cont = 1
print('-' * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-' * 40)
for c in lista:
    if cont % 2 != 0:
        print(f"{c:.<30}", end='')
    else:
        print(f"R${c:>7}")
    cont += 1
print('-' * 40)
    