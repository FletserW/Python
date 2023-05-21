maior = man = woman = 0
while True:
    print('=-' * 15)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('=-' * 15)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'MF':
            if sexo in 'M':
                man += 1
            elif sexo in 'F' and idade > 20:
                woman += 1
            break
    print('-' * 30)
    while True:
        reset = str(input('Quer continuar? [S/N] ')).strip().upper()
        if reset in 'SN':
            break
    if reset in 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^30}')
print(f"""Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {man} homens cadastrados
E temos {woman} mulheres com menos de 20 anos""")
