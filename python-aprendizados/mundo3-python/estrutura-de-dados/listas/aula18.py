'''---------Aula 18---------'''

Teste = list()

Teste.append('Iago')
Teste.append(20)

print(Teste)

#Ligação entre as estruturas

Galera = list()
Galera.append(Teste)
Teste[0] = 'Maria'
Teste[1] = 22
Galera.append(Teste)

print(Galera)

#Cópia de dados entre as listas

Galera = list()
Galera.append(Teste[:])
Teste[0] = 'Maria'
Teste[1] = 22
Galera.append(Teste[:])

print(Galera)

# Teste

Galera = [['Pedro, 25'], ['Maria', 19], ['João', 32]]

print(Galera[0]) #Mostra todos os dados do João

print(Galera[0] [0])
#Mostra o dado de quem está no indicie 0 que é João

# Teste 2

Galera = [['Pedro, 25'], ['Maria', 19], ['João', 32]]

for pessoas in Galera:
    print(pessoas[0])

    print(f'{pessoas[0]} tem {pessoas[1]} anos de idade.')

# Teste 3

Galera = list()
dados = list()

for c in range(0,3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    Galera.append(dados[:]) #Cria uma cópia de dados sem altera-lo
    dados.clear() #Limpa uma estrutura de lista
print(Galera)

# Teste 4

Galera = list()
dados = list()
TotMaior = 0
TotMenor = 0

for c in range(0,3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    Galera.append(dados[:]) #Cria uma cópia de dados sem altera-lo
    dados.clear() #Limpa uma estrutura de lista

for pessoas in Galera:
    if pessoas[1] >= 21:
        print(f'{pessoas[0]} é maior de idade')

        TotMaior +=1
    else:
        print(f'{pessoas[0]} é menor de idade')

        TotMenor +=1

print(f'Temos {TotMaior} maiores e {TotMenor} menores idade.')

