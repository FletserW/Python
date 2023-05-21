from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
print('O aluno que irá apagar o quadro será: {}'.format(choice(alunos)))
