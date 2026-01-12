'''1)Faça um programa que leia nome e peso várias pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.

b) Uma listagem com as pessoas mais pesadas.

c) Uma listagem com as pessoas mais leves.
'''
ListaPrincipal = list()

nome = list()

peso = list()

continuar = ''

TotPessoas = TotPessoasPesada = TotPessoasLeves = 0


while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    continuar = input('Quer continuar [S/N]: ').upper()
    ListaPrincipal.append([nome, peso])
    
    TotPessoas += 1

    if len(ListaPrincipal) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    if continuar == 'N':
        break


print(f'\nTotal de pessoas cadastradas: {len(ListaPrincipal)}')

print(f'\nPessoas mais pesadas ({maior_peso}kg):', end=' ')
for pessoa in ListaPrincipal:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end=' ')
print()
print(f'\nPessoas mais leves ({menor_peso}kg):', end=' ')
for pessoa in ListaPrincipal:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end=' ')
print()
print(ListaPrincipal)
