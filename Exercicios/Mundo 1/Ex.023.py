num = int(input('Digite um numero entre 0 e 9999: '))
print('Numero escolhido: {}\n'
      'Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(num, num//1 % 10, num//10 % 10, num//100 % 10, num//1000 % 10))
