'''
1)Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Modulo moeda

def aumentar(num):

    while True:
        valor = num * (1 + 10/100)
        break
    return valor


def diminuir(num):

    while True:
        reajuste = num * (1 - 13/100)
        break
    return reajuste

def dobro(num):

    while True:
        dobro = num * 2
        break
    return dobro

def metade(num):

    while True:
        
        metade = num / 2
        break
    return metade

n = int(input('Digite um número: '))

print(f'O reajute pra + do produto é de {aumentar(n)}')

print(f'O dobro do produto é de {dobro(n)}')

print(f'A metade do produto é de {metade(n)}')