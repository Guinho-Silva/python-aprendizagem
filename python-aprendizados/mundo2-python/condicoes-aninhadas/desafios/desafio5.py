from datetime import date

IdadeAtleta = int(input('Digite o seu ANO de nascimento: '))

AnoAtual = date.today().year

ConversaoIdade = AnoAtual - IdadeAtleta

if ConversaoIdade <= 9:
    print('Categoria: MIRIM')

elif ConversaoIdade <= 14:
    print('Categoria: INFANTIL')

elif ConversaoIdade <= 19:
    print('Categoria: JUNIOR')

elif ConversaoIdade <= 30:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')