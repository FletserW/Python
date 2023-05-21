""" VARIAVEIS """
valores = list()
maior = 0
menor = 0

""" COMANDOS """
for p in range(0, 5):
    valores.append(int(input(f"Digite um valor para posição {p}: ")))
    if p == 0:
        menor = maior = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]
print('-' * 15)
print(f"Você digitou os valores {valores}")
print(f"O Menor valor digitado foi {menor} nas posições ", end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
print()
print(f"O Maior valor digitado foi {maior} nas posições ", end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print()
