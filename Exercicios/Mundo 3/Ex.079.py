""" VARIAVEIS """
cores = {"limpar": '\033[m',
         "azul": '\033[34m',
         "amarelo": '\033[33m',
         "vermelho": '\033[31m',
         "verde": '\033[32m',
         "pretoebranco": '\033[7:30m'}
num = list()
pi = 0

""" COMANDOS """
while pi == 0:
    x = int(input('Digite um valor: '))
    if x in num:
        print(f'{cores["vermelho"]}Valor duplicado! Não vou adicionar...{cores["limpar"]}')
    else:
        num.append(x)
        print(f'{cores["verde"]}Valor adicionado com sucesso...{cores["limpar"]}')

    while True:
        reset = str(input('Quer continua? [S/N] ')).strip().upper()
        if reset in "N":
            pi = 1
            break
        if reset in "S":
            break
        else:
            print("Erro! opção invalida.")
print('-=' * 25)
num.sort()
print(f'Você digitou os valores {num}')
