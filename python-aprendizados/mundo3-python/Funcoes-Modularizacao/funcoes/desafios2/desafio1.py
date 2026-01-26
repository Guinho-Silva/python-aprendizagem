'''
1)Crie um programa eu uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto negado, opcional ou obrigatório nas eleições.
'''

from datetime import date
def voto(ano):

    anoAtual = date.today().year
    IdadeTotal = anoAtual - ano

    if ano < 16:
        return 'NEGADO!'
    elif 16 <= Idade < 18 or Idade >= 70 :
        return 'OPICIONAL!'
    else:
        return 'OBRIGATÓRIO!'

Idade = int(input('Digite sua idade: '))

print(f'Com {Idade} anos o seu voto é: {voto(Idade)}')