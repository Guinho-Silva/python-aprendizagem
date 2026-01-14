# Aula 19 - Dicionarios

'''pessoas = {'nome': 'Iago', 'idade': 20, 'sexo': 'M'}

print(pessoas['nome'])

print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')

# Usando keys

print(pessoas.keys())

#Usando values

print(pessoas.values())

# Usando  items

print(pessoas.items())


# Usando laços para mostrar keys

for k in pessoas.keys():
    print(k)

# Usando laços para mostrar values

for v in pessoas.values():
    print(v)

# Usando laços para mostrar items

for k, v in pessoas.items():
    print(f'{k} = {v}')

# Criando um dicionario dentro de uma lista

brasil = []

estado = {
    'UF': 'São Paulo', 'Sigla': 'SP'
}

estado2 = {
    'UF': 'Rio de Janero', 'Sigla': 'RJ'
}

brasil.append(estado)
brasil.append(estado2)

print(brasil[0]['UF']['Sigla'])'''

# criando uma copia de dicionarios

estado = dict()
brasil = list()

for contador in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for state in brasil:
    for v in state.values():
        print(v, end=' ')

    print()