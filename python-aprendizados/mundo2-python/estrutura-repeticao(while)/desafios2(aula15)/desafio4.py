'''4) Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:

a) quantas pessoas tem mais de 18 anos

b) Quantos homens foram cadastrados.

c) Quantas mulheres tem menos de 20 anos'''


Homens = 0

idadeTotal = 0

IdadeMulher = 0


while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()

    while sexo not in ('M','F'):
        print('Valor inválido. Digite Novamente.')
        sexo = input('Digite seu sexo [M/F]: ').strip().upper()
    
    if idade > 18:
        idadeTotal += 1
    
    if sexo == 'M':
        Homens +=1
    if sexo == 'F' and idade < 20:
        IdadeMulher += 1

    novamente = input('Deseja cadastrar mais pessoas? [S/N]:').strip().upper()

    if novamente == 'N':
        break


    
print('----RESULTADOS----')

print(f'pessoa scom maiores de 18 anos: {idadeTotal}')
print(f'Homens cadastrados: {Homens}')
print(f'Mulheres com menos de 20 anos: {IdadeMulher}')