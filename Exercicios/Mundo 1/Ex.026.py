frase = str(input('Escreva uma frase: ').lower()).strip()
print('A letra (a) aparece {} vezes, sendo a {}° letra o primeiro eo {}° letra o ultimo.'
      ''.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))

