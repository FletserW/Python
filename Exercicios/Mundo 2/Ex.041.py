from datetime import date
""" VARIAVEIS """
num = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = (ano - num)
""" COMANDOS """
print('-=-' * 12)
print('O atleta possui {} anos ele é:'.format(idade))
if 0 < idade < 10:
    print('  MIRIM')
elif idade < 15:
    print('  INFANCIL')
elif idade < 20:
    print('  Junior')
elif idade < 21:
    print('  SÊNIOR')
elif 20 < idade:
    print('  MASTER')
else:
    print('  #ERRO#')
print('-=-' * 12)
