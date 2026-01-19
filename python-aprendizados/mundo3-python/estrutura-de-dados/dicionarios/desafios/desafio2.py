'''
2) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado;
'''

from random import randint
from operator import itemgetter

Dado = dict()

for valores in range(1,5):
    Dado[f'{valores}°Jogador'] = randint(1, 6)

rank = dict()
for key, values in Dado.items():
    print(f'{key:}: {values}')

rank = sorted(Dado.items(), key=itemgetter(1), reverse=True)

print('-='*30)
print('  == RANKING ==  ')
for keys, valores in enumerate(rank):
    print(f'{keys + 1} lugar:  {valores[0]} com {valores[1]}')


