'''
5) Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas

B) A média de idade do grupo

c) Uma lista com todas as mulheres

D) Uma lista com todas as pessoas com idade acima da média.

'''
from statistics import mean
ListaMulher = list()
ListaCadastro = list()
resposta = ''
mediaIdade = 0
while True:
    Dicionario = dict()
    Dicionario['Nome'] = str(input('Nome: '))
    Dicionario['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    Dicionario['Idade'] = int(input('Idade: '))
    
    ListaCadastro.append(Dicionario)

    if Dicionario['Sexo'] == 'F':
        ListaMulher.append(Dicionario)

    resposta = str(input('Quer cadastrar mais alguém?[S/N]: ')).upper()

    if resposta == 'N':
        break

print(f'Foram cadastrados {len(ListaCadastro)} nomes: ',end=' ')
for nomes in ListaCadastro:
    print(nomes['Nome'], end=', ')

print()

print(f'foram cadastrada(as) {len(ListaMulher)} mulheres, sendo elas: ', end=' ')
for mulheres in ListaMulher:
    print(mulheres['Nome'], end=', ')