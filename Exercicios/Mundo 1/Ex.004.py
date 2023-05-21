x = input('Write something: ')
print('O tipo primitivo desse valor é: {}\n'
      'Só tem espaços?: {}\n'
      'É um numero?: {}\n'
      'É alfabético?: {}\n'
      'Está em minusculo?: {}\n'
      'Está em maiúsculo?: {}\n'
      'Está capitalizado?: {}'
      .format(type(x), x.isspace(), x.isnumeric(), x.isalpha(), x.islower(), x.isupper(), x.istitle()))
