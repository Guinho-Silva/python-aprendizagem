
'''sexo = ['F', 'M']

Todosnomes = []

IdadesPessoas = []

for c in range (1, 4 + 1):
    idade = int(input('Digite sua IDADE: '))
    nome = str(input('Digite seu NOME: '))
    sexo = str(input('Digite seu SEXO: '))

    Todosnomes.append(nome)
    
    IdadesPessoas.append(idade)


    print('A média de idades é de: ')
    if sexo == 'F':
        print(Todosnomes, min(IdadesPessoas))
    else:
        print(Todosnomes, max(IdadesPessoas))
        '''


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4

print('A média de idade do grupo é de {} anos'.format(mediaidade))

print('O homem mais velho tem {} anos e se chama {}'. format(maioridadehomem, nomevelho))

print('Ao todo saõ {} mulheres com menos de 20 anos'.format(totmulher20))