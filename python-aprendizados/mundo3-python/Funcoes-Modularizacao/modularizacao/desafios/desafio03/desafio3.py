'''
3)Modifique as funções que foram criadas no desafio 1 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108
'''

import moeda

print(f'O valor com um aumento de 10% é de: {moeda.aumentar(500,True)}')

print(f'O valor com um desconto de 13% é de: {moeda.diminuir(500,True)}')

print(f'O valor dobrado é de: {moeda.dobro(500, Show=True)}')

print(f'A metade do valor é de: {moeda.metade(500, True)}')