d = float(input('Escreva a distancia percorrida em Km: '))
t = int(input('Escreva o tempo alugado em dias: '))
print('O aluguel do carro atualmente é: R${:.2f}'.format((d*0.15)+(t*60)))
