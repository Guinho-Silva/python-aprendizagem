from datetime import date

AnoNascimento = int(input('Digite a sua data de nascimento: '))

AnoAtual = date.today().year

Idade = AnoAtual - AnoNascimento

if Idade == 18:
    print('Você possui idade para se alistar no exército!')

elif Idade < 18:
    faltam = 18 - Idade
    print('Você ainda não possui idade miníma para se alistar! Faltam {} anos'.format(faltam))

else:
    passou = Idade - 18
    print('Já passou da hora de se alistar! Já passou {} anos'.format(passou))

'''
Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade:

- Se ela ainda vai se alistar

- Se é hora de se alistar

- Se ja passou da hora

p programa também deverá mostrar o tempo que falta ou que ja passou
'''