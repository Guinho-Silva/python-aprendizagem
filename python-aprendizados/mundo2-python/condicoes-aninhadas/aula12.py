nome = str(input('Qual é o seu nome: '))

if nome == 'Iago': #Condição Simples
    print('Que nome bonito!')

elif nome == 'Maria' or nome == 'Adão':
    print('Seu nome é bem popular no Brasil.')

elif nome  in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))