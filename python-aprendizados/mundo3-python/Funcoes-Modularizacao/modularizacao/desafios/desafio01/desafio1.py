'''
1)Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Modulo moeda

import moedas

n = int(input('Digite um número: '))

print(f'O reajute pra + do produto é de {moedas.aumentar(n)}')

print(f'O reajuste pra - do produto é de {moedas.diminuir(n)}')

print(f'O dobro do produto é de {moedas.dobro(n)}')

print(f'A metade do produto é de {moedas.metade(n)}')