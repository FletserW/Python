n = int(input('Escreva o valor em metros a ser convertido: '))
print('O valor {}M convertido em:\n'
      '# Quilometros: {}km\n'
      '# Hectrometro: {}hm\n'
      '# Decametro: {}dam\n'
      '# Decimetro: {}dm\n'
      '# Centímentros: {}cm\n'
      '# Milímentos: {}mm'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))
