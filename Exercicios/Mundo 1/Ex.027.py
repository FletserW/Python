name = input('Escreva seu nome: ').strip()
name = name.split()
print('Primeiro nome: {}\n'
      'Último nome: {}'.format(name[0], name[len(name)-1]))
