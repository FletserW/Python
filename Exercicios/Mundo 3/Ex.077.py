lista = ("""APRENDER PROGRAMAR LINGUAGEM PYTHON CURSO GRATIS ESTUDAR PRATICAR TRABALHAR MERCADO PROGRAMADOR 
FUTURO""").split()
for c in lista:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')
