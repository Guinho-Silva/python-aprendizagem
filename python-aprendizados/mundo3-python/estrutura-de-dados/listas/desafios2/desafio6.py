'''
6)Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
'''
from statistics import mean

notas = []

resposta = ''


while True:
    nome = str(input('Nome: '))
   
    n1 = float(input('Digite sua nota 1: '))

    n2 = float(input('Digite sua nota 2: '))

    CalcuMedia = (n1 + n2)/2

    aluno = [nome, 
             [n1, n2],CalcuMedia
            ]

    notas.append(aluno)

    resposta = str(input('Quer continuar? [S/N]: ')).upper()

    if resposta == "N":
        break

print(f'{"ID.":<4}{"NOME":<10}{"MÉDIA":>8}')
print()
for i, a in enumerate(notas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opcao = int(input('Quer mostrar a nota de qual aluno? ("999" para o programa): '))

    if opcao == 999:
        break
    if opcao <= len(notas) - 1:
        print(f'Notas de {notas[opcao][0]} são {notas[opcao][1]}')



