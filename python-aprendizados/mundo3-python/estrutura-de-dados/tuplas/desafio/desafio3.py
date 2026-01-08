'''3) Crie um programa que vai gera cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados o menor e o maior valor que estão na tupla
'''
import random

NumGerados = (
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10))


print(f'Os números gerados foi: {NumGerados}')

print(f'O menor valor foi: {min(NumGerados)}')

print(f'O maior valor {max(NumGerados)}')

'''import random

NumGerados = ()
NovoNum = ()

'NumAlet = random.random(0,5)'

for cont in range(5):
    NovoNum = random.randint(1,5)

    NovoNum = (NovoNum, ) 

    NumGerados += NovoNum

    print(NumGerados)
print('Fim')
print(len(NumGerados))'''

