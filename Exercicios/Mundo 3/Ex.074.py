from random import randint
lista = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram:{lista}\n'
      f'O maior número sorteado foi {max(lista)}\n'
      f'O menor número sorteado foi {min(lista)}')
