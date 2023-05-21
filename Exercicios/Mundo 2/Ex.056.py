""" VARIAVEIS """
somaidade = 0
medidade = 0
idadehomem = 0
velho = 0
contmulher = 0

""" COMANDOS """
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sex in 'Mm':
        idadehomem = idade
        velho = nome
    if sex in 'Mm' and idade > idadehomem:
        idadehomem = idade
        velho = nome
    if sex in 'Ff' and idade < 20:
        contmulher += 1
medidade = somaidade / 4
print('-=' * 20)
print('A média de idade do grupo é de {} anos'.format(medidade))
print('O homem mais velho tem {} e se chama {}.'.format(idadehomem, velho))
print('O número de mulheres com menos de 20 anos é {}.'.format(contmulher))
print('-=' * 20)
