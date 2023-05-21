""" VARIAVEIS """
s = float(input('Qual seu salario atual: '))

""" COMANDOS """
print('Analizando...\n{}'.format('-' * 55))
if s > 1250.00:
    print('Você recebeu um aumento seu salario agora é: R${:.2f}'.format(s + (10/100*s)))
else:
    print('Você recebeu um aumento seu novo salario é: R${:.2f}'.format(s + (15/100*s)))
print('-' * 55)
