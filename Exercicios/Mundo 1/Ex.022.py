nome = str(input('Seu nome: ')).strip()
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
n = nome.replace(' ', '')
print('Seu nome possui ao todo {} letras.'.format(len(n)))
print('Seu primeiro nome possui {} letras.'.format(nome.find(' ')))
