'''
1) Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo de estrutura na tela;'''

Aluno = dict()

Aluno['Nome'] = str(input('Nome: '))
Aluno['Média'] = float(input('Média: '))
if Aluno['Média'] >= 7:
    Aluno['Situação'] = 'Aprovado'
else:
    Aluno['Situação'] = 'Reprovado'

for keys, valores in Aluno.items():
    print(f'{keys} é igual a: {valores}')



'''print(f'Nome do aluno: {Aluno["Nome"]}')
print(f'A média do {Aluno["Nome"]} foi de: {Aluno["Média"]}')
print(f'Sua situação (Aprovado/Reprovado) foi de: {Aluno["Situação"]}')'''
