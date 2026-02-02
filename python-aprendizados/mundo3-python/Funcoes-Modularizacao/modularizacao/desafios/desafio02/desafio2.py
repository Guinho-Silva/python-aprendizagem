'''
2)Adapte o código do desafio 1, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado
'''

import moeda

n = int(input('Digite um número: '))

print(f'O reajute pra + do produto é de {moeda.moeda(moeda.aumentar(n))}')


print(f'O reajuste pra - do produto é de {moeda.moeda(moeda.diminuir(n))}')

print(f'O dobro do produto é de {moeda.moeda(moeda.dobro(n))}')

print(f'A metade do produto é de {moeda.moeda(moeda.metade(n))}')