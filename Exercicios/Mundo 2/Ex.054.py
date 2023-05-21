from datetime import date
ano = date.today().year
maior = 0
for c in range(1, 8):
    nasce = int(input('Em que ano a {}° nasceu: '.format(c)))
    idade = ano - nasce
    if idade >= 21:
        maior = maior + 1
print('{} pessoas ainda não atingiram a maior idade.\n'
      '{} atingiram a maior idade.'.format(7 - maior, maior))
