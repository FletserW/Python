frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for c in range(len(juntar) -1, -1, -1):
    inverso += juntar[c]
if inverso == juntar:
    print('Essa frase é um palímetro')
else:
    print('Essa frase não é um palímetro')
