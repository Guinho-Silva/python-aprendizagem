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
soma = 0

while True:
    Dicionario = dict()
    Dicionario['Nome'] = str(input('Nome: '))
    
    while True:
        Dicionario['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if Dicionario['Sexo'] in 'MF':
            break
        print('Sexo inválido! Digite "M" para masculino e "F" para feminino: ')       

    Dicionario['Idade'] = int(input('Idade: '))
    
    soma += Dicionario['Idade']

    ListaCadastro.append(Dicionario)

    
    if Dicionario['Sexo'] == 'F':
        ListaMulher.append(Dicionario)
    
    while True:

        resposta = str(input('Quer cadastrar mais alguém?[S/N]: ')).upper()
        
        if resposta in 'SN':
            break
        print('Resposta inválida! Digite "S" para continuar e "N" para encerrar: ')
        

    if resposta == 'N':
            break
mediaIdade = soma / len(ListaCadastro)

print(f'Foram cadastrados {len(ListaCadastro)} nomes: ',end=' ')
for nomes in ListaCadastro:
    print(nomes['Nome'], end=', ')

print()

print(f'A média das idades é de {mediaIdade}')

print(f'foram cadastrada(as) {len(ListaMulher)} mulheres, sendo elas: ', end=' ')
for mulheres in ListaMulher:
    print(mulheres['Nome'])

print('Pessoas com idade acima da média:', end='')

for pessoa in ListaCadastro:
    if pessoa['Idade'] > mediaIdade:
        print(f"Nome: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa['Idade']}")
