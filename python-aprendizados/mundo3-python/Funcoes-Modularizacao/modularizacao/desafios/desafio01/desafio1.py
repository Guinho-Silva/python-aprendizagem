'''
1)Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Modulo moeda

import moedas

n = float(input('Digite o preço: '))

print(f'O reajute de 10% de {n} é de {moedas.aumentar(n)}')

print(f'O reajuste de 13% de desconto de {n} é de {moedas.diminuir(n)}')

print(f'O dobro de {n} é de {moedas.dobro(n)}')

print(f'A metade de {n} é de {moedas.metade(n)}')