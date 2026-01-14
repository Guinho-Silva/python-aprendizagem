'''
2) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado;
'''

from random import randint


Dado = dict()

for valores in range(1,7):
    Dado[f'{valores}°Jogador'] = randint(1, 6)

for key, values in Dado.items():
    print(f'{key:}: {values}')



